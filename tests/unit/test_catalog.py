"""Many-to-many catalog and stable-identity contract tests."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import cast

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.catalog import validate_catalog  # noqa: E402


def issue(
    number: int,
    kind: str,
    semantic_id: str,
    state: str = "",
    links: list[dict[str, object]] | None = None,
    aliases: list[str] | None = None,
) -> dict[str, object]:
    record: dict[str, object] = {
        "schema": "backplane-heavy/v1",
        "kind": kind,
        "semantic_id": semantic_id,
        "links": list(links or []),
    }
    if state:
        record["record_state"] = state
    if aliases is not None:
        record["aliases"] = aliases
    if kind == "requirement":
        record["links"].append(
            {
                "type": "anchored_in_prd",
                "target": {"locator": f"docs/project/prd.md#{semantic_id}", "revision": "P1"},
            }
        )
    return {
        "number": number,
        "url": f"https://github.com/o/r/issues/{number}",
        "state": "OPEN",
        "labels": [{"name": "backplane:backlog"}] if kind == "outcome" else [],
        "record": record,
    }


def issue_link(kind: str, number: int, semantic_id: str) -> dict[str, object]:
    return {
        "type": kind,
        "target": {"semantic_id": semantic_id, "issue": f"https://github.com/o/r/issues/{number}"},
    }


class CatalogTests(unittest.TestCase):
    def test_unrecorded_incidental_issue_is_addressable_without_a_semantic_id(self) -> None:
        requirement = issue(30, "requirement", "R-1", "current")
        incidental: dict[str, object] = {
            "number": 31,
            "url": "https://github.com/o/r/issues/31",
            "title": "Unexpected failure report",
            "state": "OPEN",
            "labels": [],
        }
        catalog = validate_catalog([requirement, incidental], {"R-1"})
        self.assertEqual(set(catalog["by_id"]), {"R-1"})
        with self.assertRaisesRegex(ValueError, "required Backplane Record.*31"):
            validate_catalog([requirement, incidental], {"R-1"}, required_record_numbers={31})

    def test_many_to_many_and_family_move_keep_stable_id(self) -> None:
        records = [
            issue(30, "requirement", "R-1", "current"),
            issue(31, "requirement", "R-2", "current"),
            issue(32, "capability", "C4", "accepted"),
            issue(
                33,
                "outcome",
                "C2.3",
                links=[
                    issue_link("belongs_to", 32, "C4"),
                    issue_link("satisfies", 30, "R-1"),
                    issue_link("satisfies", 31, "R-2"),
                ],
            ),
            issue(34, "outcome", "C2.4", links=[issue_link("satisfies", 31, "R-2")]),
        ]
        catalog = validate_catalog(records, {"R-1", "R-2"})
        self.assertEqual(catalog["by_id"]["C2.3"]["semantic_id"], "C2.3")
        self.assertEqual({source for source, _ in catalog["reverse"]["R-2"]}, {"C2.3", "C2.4"})

    def test_split_keeps_old_id_and_two_new_ids(self) -> None:
        records = [
            issue(40, "requirement", "R-1", "current"),
            issue(41, "outcome", "C2.3", links=[issue_link("satisfies", 40, "R-1")]),
            issue(
                42,
                "outcome",
                "C4.1",
                links=[issue_link("split_from", 41, "C2.3"), issue_link("satisfies", 40, "R-1")],
            ),
            issue(
                43,
                "outcome",
                "C4.2",
                links=[issue_link("split_from", 41, "C2.3"), issue_link("satisfies", 40, "R-1")],
            ),
        ]
        catalog = validate_catalog(records, {"R-1"})
        self.assertEqual(set(catalog["by_id"]), {"R-1", "C2.3", "C4.1", "C4.2"})

    def test_execution_labels_apply_only_to_open_outcomes(self) -> None:
        requirement = issue(30, "requirement", "R-1", "current")
        outcome = issue(31, "outcome", "C2.3")
        outcome["labels"] = []
        with self.assertRaisesRegex(ValueError, "one execution label"):
            validate_catalog([requirement, outcome], {"R-1"})
        outcome["labels"] = [{"name": "backplane:ready"}, {"name": "backplane:active"}]
        with self.assertRaisesRegex(ValueError, "one execution label"):
            validate_catalog([requirement, outcome], {"R-1"})
        outcome["state"] = "CLOSED"
        with self.assertRaisesRegex(ValueError, "no execution label"):
            validate_catalog([requirement, outcome], {"R-1"})
        outcome["labels"] = []
        validate_catalog([requirement, outcome], {"R-1"})
        requirement["labels"] = [{"name": "backplane:ready"}]
        with self.assertRaisesRegex(ValueError, "no execution label"):
            validate_catalog([requirement, outcome], {"R-1"})

    def test_catalog_rejects_unparsed_untrusted_record_shape(self) -> None:
        requirement = issue(30, "requirement", "R-1", "current")
        outcome = issue(31, "outcome", "C2.3")
        cast("dict[str, object]", outcome["record"])["kind"] = ["outcome"]
        with self.assertRaisesRegex(ValueError, "kind"):
            validate_catalog([requirement, outcome], {"R-1"})

    def test_rejects_identity_and_link_errors(self) -> None:
        requirement = issue(50, "requirement", "R-1", "current")
        cases = [
            (
                "duplicate ID",
                [requirement, issue(51, "outcome", "R-1")],
                {"R-1"},
                "duplicate semantic ID",
            ),
            ("missing anchor", [requirement], {"R-1", "R-2"}, "missing requirement anchor"),
            (
                "unknown PRD ID",
                [requirement, issue(51, "requirement", "R-2", "current")],
                {"R-1"},
                "not in approved PRD",
            ),
            (
                "dangling target",
                [
                    requirement,
                    issue(51, "outcome", "C2.3", links=[issue_link("satisfies", 99, "R-1")]),
                ],
                {"R-1"},
                "dangling target",
            ),
            (
                "mismatched target",
                [
                    requirement,
                    issue(51, "outcome", "C2.3", links=[issue_link("satisfies", 50, "R-2")]),
                ],
                {"R-1"},
                "target ID mismatch",
            ),
            (
                "wrong endpoint",
                [
                    requirement,
                    issue(51, "outcome", "C2.3", links=[issue_link("belongs_to", 50, "R-1")]),
                ],
                {"R-1"},
                "invalid endpoint",
            ),
            (
                "duplicate alias",
                [
                    requirement,
                    issue(51, "outcome", "C2.3", aliases=["C-old"]),
                    issue(52, "outcome", "C2.4", aliases=["C-old"]),
                ],
                {"R-1"},
                "duplicate semantic ID or alias",
            ),
        ]
        for name, records, requirement_ids, expected in cases:
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, expected):
                    validate_catalog(records, requirement_ids)


if __name__ == "__main__":
    unittest.main()
