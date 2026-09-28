"""Requirement identity and wording extraction tests."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.prd import parse_requirements  # noqa: E402


class PRDTests(unittest.TestCase):
    def test_current_approved_prd_has_twelve_unique_requirements(self) -> None:
        path = Path(__file__).resolve().parents[2] / "docs/project/prd.md"
        requirements = parse_requirements(path.read_text(encoding="utf-8"))
        self.assertEqual(len(requirements), 12)
        self.assertIn("BP-R001", requirements)
        self.assertIn("BP-R012", requirements)
        self.assertIn("approved constitution", requirements["BP-R001"]["wording"])

    def test_duplicate_or_missing_wording_fails(self) -> None:
        header = (
            "| ID | Requirement wording | Measurable success criterion |\n| --- | --- | --- |\n"
        )
        row = "| `R-1` | A stable requirement. | Check it. |\n"
        with self.assertRaisesRegex(ValueError, "duplicate requirement ID"):
            parse_requirements(header + row + row)
        with self.assertRaisesRegex(ValueError, "missing requirement wording"):
            parse_requirements(header + "| `R-1` |  | Check it. |\n")

    def test_non_requirement_tables_are_ignored(self) -> None:
        text = (
            "| Other | Table | Here |\n| --- | --- | --- |\n| `X` | no | no |\n"
            "| ID | Requirement wording | Measurable success criterion |\n"
            "| --- | --- | --- |\n| `R-1` | Do one thing. | Observe one result. |\n"
        )
        self.assertEqual(set(parse_requirements(text)), {"R-1"})


if __name__ == "__main__":
    unittest.main()
