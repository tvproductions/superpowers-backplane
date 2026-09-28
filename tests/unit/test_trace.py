"""Trace relation currency is separate from passing evidence."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.trace import build_trace  # noqa: E402


def issue(
    number: int, semantic_id: str, kind: str, links: list[dict[str, object]]
) -> dict[str, object]:
    record: dict[str, object] = {
        "schema": "backplane-heavy/v1",
        "kind": kind,
        "semantic_id": semantic_id,
        "links": links,
    }
    if kind == "requirement":
        record["record_state"] = "current"
    return {
        "number": number,
        "url": f"https://github.com/o/r/issues/{number}",
        "updatedAt": "I1",
        "state": "OPEN",
        "labels": [{"name": "backplane:backlog"}] if kind == "outcome" else [],
        "record": record,
    }


def prd_link(semantic_id: str, revision: str) -> dict[str, object]:
    return {
        "type": "anchored_in_prd",
        "target": {"locator": f"docs/project/prd.md#{semantic_id}", "revision": revision},
    }


def satisfies(number: int, semantic_id: str) -> dict[str, object]:
    return {
        "type": "satisfies",
        "target": {
            "semantic_id": semantic_id,
            "issue": f"https://github.com/o/r/issues/{number}",
        },
    }


class TraceTests(unittest.TestCase):
    def test_many_to_many_forward_reverse_and_changed_requirement(self) -> None:
        issues = [
            issue(30, "R-1", "requirement", [prd_link("R-1", "P1")]),
            issue(31, "R-2", "requirement", [prd_link("R-2", "P1")]),
            issue(32, "C2.3", "outcome", [satisfies(30, "R-1"), satisfies(31, "R-2")]),
            issue(33, "C2.4", "outcome", [satisfies(31, "R-2")]),
        ]
        trace = build_trace(issues, {"R-1": "P1", "R-2": "P2"})
        self.assertEqual([row["outcome_id"] for row in trace["forward"]["R-2"]], ["C2.3", "C2.4"])
        self.assertEqual(
            [row["requirement_id"] for row in trace["reverse"]["C2.3"]], ["R-1", "R-2"]
        )
        self.assertEqual(trace["forward"]["R-1"][0]["link_currency"], "current")
        self.assertEqual(
            [row["link_currency"] for row in trace["forward"]["R-2"]], ["stale", "stale"]
        )

    def test_missing_outcome_link_is_reported_without_invention(self) -> None:
        trace = build_trace(
            [issue(30, "R-1", "requirement", [prd_link("R-1", "P1")])],
            {"R-1": "P1"},
        )
        self.assertEqual(trace["forward"]["R-1"], [])
        self.assertEqual(trace["uncovered_requirements"], ["R-1"])


if __name__ == "__main__":
    unittest.main()
