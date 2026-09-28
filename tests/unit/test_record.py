"""Contract tests for heavy issue record parsing."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.record import parse_record  # noqa: E402


def wrap_record(raw: str) -> str:
    return "## Backplane Record\n```json\n" + raw + "\n```\n"


class RecordParserTests(unittest.TestCase):
    def test_accepts_outcome_and_release(self) -> None:
        cases = [
            (
                "outcome",
                '{"schema":"backplane-heavy/v1","kind":"outcome","semantic_id":"C2.3","links":[]}',
                "C2.3",
            ),
            (
                "release",
                '{"schema":"backplane-heavy/v1","kind":"release",'
                '"semantic_id":"REL-A","record_state":"candidate",'
                '"target_version":"1.0.0","links":[]}',
                "REL-A",
            ),
        ]
        for kind, raw, expected_id in cases:
            with self.subTest(kind=kind):
                record = parse_record("# Work\n\n" + wrap_record(raw))
                self.assertEqual(record["kind"], kind)
                self.assertEqual(record["semantic_id"], expected_id)

    def test_rejects_untrusted_shapes(self) -> None:
        good = '{"schema":"backplane-heavy/v1","kind":"outcome","semantic_id":"C2.3","links":[]}'
        cases = [
            ("missing", "# ordinary issue\n", "missing Backplane Record"),
            (
                "duplicate section",
                wrap_record(good) + wrap_record(good),
                "multiple Backplane Record",
            ),
            (
                "unknown field",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"outcome",'
                    '"semantic_id":"C2.3","approved":true,"links":[]}'
                ),
                "unknown field",
            ),
            (
                "duplicate key",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"outcome",'
                    '"kind":"release","semantic_id":"C2.3","links":[]}'
                ),
                "duplicate JSON key",
            ),
            (
                "outcome state",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"outcome",'
                    '"semantic_id":"C2.3","record_state":"ready","links":[]}'
                ),
                "record_state",
            ),
            (
                "early publication",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"release",'
                    '"semantic_id":"REL-A","record_state":"candidate",'
                    '"target_version":"1.0.0","published_tag":"v1.0.0","links":[]}'
                ),
                "published_tag",
            ),
            ("bad schema", wrap_record(good.replace("backplane-heavy/v1", "other")), "schema"),
            ("trailing JSON", "## Backplane Record\n```json\n" + good + " true\n```\n", "JSON"),
            (
                "list state",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"gate",'
                    '"semantic_id":"G-1","record_state":[],"links":[]}'
                ),
                "record_state",
            ),
            (
                "list link type",
                wrap_record(
                    '{"schema":"backplane-heavy/v1","kind":"outcome",'
                    '"semantic_id":"C2.3","links":[{"type":[],"target":{}}]}'
                ),
                "link type",
            ),
        ]
        for name, body, expected in cases:
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, expected):
                    parse_record(body)


if __name__ == "__main__":
    unittest.main()
