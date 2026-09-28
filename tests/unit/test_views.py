"""Generated roadmap and backlog bytes follow one validated source hash."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path
from typing import cast

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.snapshot import collect_snapshot  # noqa: E402
from superpowers_backplane.views import render_views  # noqa: E402
from tests.unit.test_snapshot import FakeGateway, fixture  # noqa: E402


class ViewTests(unittest.TestCase):
    def test_same_snapshot_produces_identical_readable_bytes(self) -> None:
        requirement = fixture(1, "requirement", "R-1", "I1")
        outcome = fixture(2, "outcome", "C2.3", "I1")
        outcome["title"] = "Deliver | trace"
        outcome["blockedBy"] = {"nodes": [], "totalCount": 0}
        record = cast("dict[str, object]", outcome["record"])
        record["links"] = [
            {
                "type": "satisfies",
                "target": {
                    "semantic_id": "R-1",
                    "issue": "https://github.com/o/r/issues/1",
                },
            }
        ]
        incidental: dict[str, object] = {
            "number": 3,
            "url": "https://github.com/o/r/issues/3",
            "title": "Unexpected bug",
            "updatedAt": "I1",
            "state": "OPEN",
            "labels": [],
            "blockedBy": {"nodes": [], "totalCount": 0},
        }
        issues = [requirement, outcome, incidental]
        snapshot = collect_snapshot(
            FakeGateway([issues], [{1: "I1", 2: "I1", 3: "I1"}]),
            lambda: {"docs/project/prd.md": b"P1"},
            {"R-1"},
        )
        first = render_views(snapshot, {"R-1": "P1"}, "o/r")
        second = render_views(snapshot, {"R-1": "P1"}, "o/r")
        self.assertEqual(first, second)
        for content in first.values():
            self.assertIn(snapshot["source_hash"].encode("ascii"), content)
            self.assertNotIn(b"collected_at", content)
        self.assertIn(b"C2.3", first["ROADMAP.md"])
        self.assertIn(b"Deliver \\| trace", first["BACKLOG.md"])
        self.assertIn(b"Unexpected bug", first["BACKLOG.md"])
        changed = copy.deepcopy(snapshot)
        changed["source_hash"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            render_views(changed, {"R-1": "P1"}, "o/r")
        changed = copy.deepcopy(snapshot)
        changed["issues"][1]["title"] = "changed after collection"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            render_views(changed, {"R-1": "P1"}, "o/r")


if __name__ == "__main__":
    unittest.main()
