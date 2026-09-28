"""Installed helper entry point stays read-only and reports exact collection status."""

from __future__ import annotations

import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.cli import main  # noqa: E402


class FakeGateway:
    def __init__(self, repository: str) -> None:
        self.repository = repository

    def list_issues(self) -> list[dict[str, object]]:
        return [{"number": 1}, {"number": 2, "record": {"kind": "outcome"}}]

    def total_count(self) -> int:
        return 2


class CliTests(unittest.TestCase):
    def test_preflight_reports_read_only_collection_without_claiming_heavy_readiness(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(["preflight", "--repo", "o/r"], gateway_factory=FakeGateway)
        self.assertEqual(code, 0)
        self.assertEqual(
            json.loads(output.getvalue()),
            {
                "repository": "o/r",
                "issue_count": 2,
                "recorded_issue_count": 1,
                "heavy_readiness": "UNKNOWN",
            },
        )

    def test_collection_failure_is_nonzero_and_does_not_claim_freshness(self) -> None:
        class Offline(FakeGateway):
            def list_issues(self) -> list[dict[str, object]]:
                raise OSError("unavailable")

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(["preflight", "--repo", "o/r"], gateway_factory=Offline)
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(output.getvalue())["heavy_readiness"], "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
