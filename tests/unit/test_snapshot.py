"""Snapshot completeness, race, offline, and deterministic identity tests."""

from __future__ import annotations

import copy
import hashlib
import sys
import unittest
from pathlib import Path
from typing import cast

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.snapshot import collect_snapshot  # noqa: E402


def fixture(number: int, kind: str, semantic_id: str, updated: str) -> dict[str, object]:
    record: dict[str, object] = {
        "schema": "backplane-heavy/v1",
        "kind": kind,
        "semantic_id": semantic_id,
        "links": [],
    }
    if kind == "requirement":
        record["record_state"] = "current"
        record["links"].append(
            {
                "type": "anchored_in_prd",
                "target": {"locator": f"docs/project/prd.md#{semantic_id}", "revision": "P1"},
            }
        )
    return {
        "number": number,
        "url": f"https://github.com/o/r/issues/{number}",
        "updatedAt": updated,
        "state": "OPEN",
        "labels": [{"name": "backplane:backlog"}] if kind == "outcome" else [],
        "record": record,
    }


class FakeGateway:
    def __init__(
        self,
        pages: list[list[dict[str, object]]],
        rechecks: list[dict[int, str]],
        total: int | None = None,
    ) -> None:
        self.pages = pages
        self.rechecks = rechecks
        self.total = total if total is not None else len(pages[0])
        self.attempts = 0

    def list_issues(self) -> list[dict[str, object]]:
        position = min(self.attempts, len(self.pages) - 1)
        self.attempts += 1
        return copy.deepcopy(self.pages[position])

    def total_count(self) -> int:
        return self.total

    def revisions(self, numbers: list[int]) -> dict[int, str]:
        position = min(self.attempts - 1, len(self.rechecks) - 1)
        return self.rechecks[position]


class SnapshotTests(unittest.TestCase):
    def test_105_issues_and_api_order_produce_same_hash(self) -> None:
        records = [fixture(1, "requirement", "R-1", "I1")]
        records.extend(fixture(n, "outcome", f"C{n}", "I1") for n in range(2, 106))
        revisions = {n: "I1" for n in range(1, 106)}
        first = collect_snapshot(
            FakeGateway([records], [revisions]),
            lambda: {"docs/project/prd.md": b"approved P1"},
            {"R-1"},
        )
        second = collect_snapshot(
            FakeGateway([list(reversed(records))], [revisions]),
            lambda: {"docs/project/prd.md": b"approved P1"},
            {"R-1"},
        )
        self.assertEqual(first["count"], 105)
        self.assertEqual(first["source_hash"], second["source_hash"])
        self.assertEqual(first["canonical_bytes"], second["canonical_bytes"])

    def test_known_unordered_fields_normalize_without_erasing_other_array_order(self) -> None:
        one = fixture(1, "requirement", "R-1", "I1")
        one["labels"] = [{"name": "b"}, {"name": "a"}]
        cast("dict[str, object]", one["record"])["aliases"] = ["old-b", "old-a"]
        one["sequence"] = ["first", "second"]
        reordered = copy.deepcopy(one)
        cast("list[object]", reordered["labels"]).reverse()
        cast("list[object]", cast("dict[str, object]", reordered["record"])["aliases"]).reverse()
        baseline = collect_snapshot(
            FakeGateway([[one]], [{1: "I1"}]), lambda: {"prd": b"P1"}, {"R-1"}
        )
        reordered_snapshot = collect_snapshot(
            FakeGateway([[reordered]], [{1: "I1"}]), lambda: {"prd": b"P1"}, {"R-1"}
        )
        self.assertEqual(baseline["source_hash"], reordered_snapshot["source_hash"])
        cast("list[object]", reordered["sequence"]).reverse()
        changed = collect_snapshot(
            FakeGateway([[reordered]], [{1: "I1"}]), lambda: {"prd": b"P1"}, {"R-1"}
        )
        self.assertNotEqual(baseline["source_hash"], changed["source_hash"])

    def test_changed_issue_retries_and_uses_coherent_revision(self) -> None:
        first = [fixture(1, "requirement", "R-1", "I1")]
        second = [fixture(1, "requirement", "R-1", "I2")]
        gateway = FakeGateway([first, second], [{1: "I2"}, {1: "I2"}])
        snapshot = collect_snapshot(
            gateway, lambda: {"docs/project/prd.md": b"approved P1"}, {"R-1"}
        )
        self.assertEqual(gateway.attempts, 2)
        self.assertEqual(snapshot["issues"][0]["updatedAt"], "I2")

    def test_incomplete_or_offline_source_fails_closed(self) -> None:
        one = [fixture(1, "requirement", "R-1", "I1")]
        with self.assertRaisesRegex(ValueError, "count"):
            collect_snapshot(
                FakeGateway([one], [{1: "I1"}], total=2),
                lambda: {"docs/project/prd.md": b"P1"},
                {"R-1"},
            )

        with self.assertRaisesRegex(ValueError, "changed during collection"):
            collect_snapshot(
                FakeGateway([one, one], [{1: "I2"}, {1: "I2"}]),
                lambda: {"docs/project/prd.md": b"P1"},
                {"R-1"},
            )

        class OfflineGateway(FakeGateway):
            def list_issues(self) -> list[dict[str, object]]:
                raise OSError("GitHub unavailable")

        with self.assertRaisesRegex(ValueError, "source unavailable: GitHub unavailable"):
            collect_snapshot(
                OfflineGateway([one], [{1: "I1"}]),
                lambda: {"docs/project/prd.md": b"P1"},
                {"R-1"},
            )

    def test_reviewed_migration_plan_prevents_legacy_record_omission(self) -> None:
        requirement = fixture(1, "requirement", "R-1", "I1")
        legacy: dict[str, object] = {
            "number": 2,
            "url": "https://github.com/o/r/issues/2",
            "updatedAt": "I1",
            "state": "OPEN",
            "labels": [],
        }
        with self.assertRaisesRegex(ValueError, "required Backplane Record.*2"):
            collect_snapshot(
                FakeGateway([[requirement, legacy]], [{1: "I1", 2: "I1"}]),
                lambda: {"docs/project/prd.md": b"P1"},
                {"R-1"},
                required_record_numbers={1, 2},
            )

    def test_prd_change_changes_hash_without_issue_change(self) -> None:
        one = [fixture(1, "requirement", "R-1", "I1")]
        before = collect_snapshot(
            FakeGateway([one], [{1: "I1"}]),
            lambda: {"docs/project/prd.md": b"approved P1"},
            {"R-1"},
        )
        after = collect_snapshot(
            FakeGateway([one], [{1: "I1"}]),
            lambda: {"docs/project/prd.md": b"approved P2"},
            {"R-1"},
        )
        self.assertNotEqual(before["source_hash"], after["source_hash"])

    def test_document_change_during_collection_retries(self) -> None:
        one = [fixture(1, "requirement", "R-1", "I1")]
        reads = iter(
            [
                {"docs/project/prd.md": b"P1"},
                {"docs/project/prd.md": b"P2"},
                {"docs/project/prd.md": b"P2"},
                {"docs/project/prd.md": b"P2"},
            ]
        )
        gateway = FakeGateway([one, one], [{1: "I1"}, {1: "I1"}])
        snapshot = collect_snapshot(gateway, lambda: next(reads), {"R-1"})
        self.assertEqual(gateway.attempts, 2)
        self.assertEqual(
            snapshot["document_hashes"]["docs/project/prd.md"], hashlib.sha256(b"P2").hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
