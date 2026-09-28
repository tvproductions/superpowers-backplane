"""The gh boundary rejects incomplete collection and untrusted body records."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path
from typing import cast
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.gh_adapter import GhIssueGateway  # noqa: E402


def issue(number: int, body: str = "", *, native_total: int = 0) -> dict[str, object]:
    return {
        "number": number,
        "url": f"https://github.com/o/r/issues/{number}",
        "body": body,
        "updatedAt": "I1",
        "subIssues": {"nodes": [], "totalCount": native_total},
        "blockedBy": {"nodes": [], "totalCount": 0},
        "blocking": {"nodes": [], "totalCount": 0},
    }


class FakeRunner:
    def __init__(self, issues: list[dict[str, object]], count: int | None = None) -> None:
        self.issues = issues
        self.count = len(issues) if count is None else count
        self.calls: list[list[str]] = []

    def __call__(self, arguments: list[str]) -> str:
        self.calls.append(arguments)
        if arguments[:3] == ["gh", "api", "graphql"]:
            return json.dumps({"data": {"repository": {"issues": {"totalCount": self.count}}}})
        if arguments[:3] == ["gh", "issue", "list"]:
            return json.dumps(self.issues)
        if arguments[:3] == ["gh", "issue", "view"]:
            number = int(arguments[3])
            return json.dumps(
                {
                    "number": number,
                    "url": f"https://github.com/o/r/issues/{number}",
                    "updatedAt": "I1",
                }
            )
        raise AssertionError(arguments)


class GhAdapterTests(unittest.TestCase):
    def test_complete_read_only_collection_and_record_parsing(self) -> None:
        record = {
            "schema": "backplane-heavy/v1",
            "kind": "outcome",
            "semantic_id": "C2.3",
            "links": [],
        }
        body = "## Backplane Record\n\n```json\n" + json.dumps(record) + "\n```\n"
        runner = FakeRunner([issue(1), issue(2, body)])
        gateway = GhIssueGateway("o/r", runner=runner)
        collected = gateway.list_issues()
        self.assertEqual(gateway.total_count(), 2)
        self.assertEqual(gateway.revisions([1, 2]), {1: "I1", 2: "I1"})
        self.assertNotIn("record", collected[0])
        self.assertEqual(cast("dict[str, object]", collected[1]["record"])["semantic_id"], "C2.3")
        self.assertEqual(runner.calls[1][:3], ["gh", "issue", "list"])
        self.assertIn("--repo", runner.calls[1])

    def test_count_and_native_edge_truncation_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "issue count"):
            GhIssueGateway("o/r", runner=FakeRunner([issue(1)], count=2)).list_issues()
        with self.assertRaisesRegex(ValueError, "incomplete subIssues"):
            GhIssueGateway("o/r", runner=FakeRunner([issue(1, native_total=1)])).list_issues()

    def test_malformed_record_is_not_treated_as_incidental(self) -> None:
        with self.assertRaisesRegex(ValueError, "Backplane Record"):
            GhIssueGateway(
                "o/r", runner=FakeRunner([issue(1, "## Backplane Record\nno json")])
            ).list_issues()

    def test_gh_timeout_is_reported_as_unavailable(self) -> None:
        with patch(
            "superpowers_backplane.gh_adapter.subprocess.run",
            side_effect=subprocess.TimeoutExpired(cmd=["gh"], timeout=120),
        ):
            with self.assertRaisesRegex(RuntimeError, "timed out"):
                GhIssueGateway("o/r").total_count()


if __name__ == "__main__":
    unittest.main()
