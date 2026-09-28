"""Verification and validation records are untrusted and revision-bound."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.evidence import (  # noqa: E402
    assess_verification,
    parse_evidence,
)


def evidence_body(
    *,
    kind: str = "verification",
    result: str = "pass",
    requirement_revision: str = "P1",
    outcome_revision: str = "I1",
    source: str = "a" * 40,
) -> str:
    record = {
        "schema": "backplane-evidence/v1",
        "kind": kind,
        "method": "test" if kind == "verification" else "stakeholder review",
        "result": result,
        "observed_at": "2026-09-27T00:00:00Z",
        "integrated_source": source,
        "requirements": [{"semantic_id": "R-1", "prd_revision": requirement_revision}],
        "outcomes": [
            {
                "semantic_id": "C2.3",
                "issue": "https://github.com/o/r/issues/32",
                "issue_revision": outcome_revision,
            }
        ],
        "success_criteria": ["SC-1"] if kind == "validation" else [],
        "users": ["maintainers"] if kind == "validation" else [],
        "accepted_by": "ahuimanu",
    }
    return "## Backplane Evidence\n\n```json\n" + json.dumps(record) + "\n```\n"


class EvidenceTests(unittest.TestCase):
    def test_exact_current_verification_and_changed_requirement(self) -> None:
        record = parse_evidence(evidence_body())
        current = assess_verification(
            record,
            requirement_id="R-1",
            prd_revision="P1",
            outcome_id="C2.3",
            issue_url="https://github.com/o/r/issues/32",
            issue_revision="I1",
            integrated_source="a" * 40,
            accepting_people={"ahuimanu"},
            artifact_checked=True,
        )
        self.assertEqual(current, "current")
        self.assertEqual(
            assess_verification(
                record,
                requirement_id="R-1",
                prd_revision="P2",
                outcome_id="C2.3",
                issue_url="https://github.com/o/r/issues/32",
                issue_revision="I1",
                integrated_source="a" * 40,
                accepting_people={"ahuimanu"},
                artifact_checked=True,
            ),
            "stale",
        )

    def test_validation_cannot_substitute_for_verification(self) -> None:
        validation = parse_evidence(evidence_body(kind="validation"))
        self.assertEqual(
            assess_verification(
                validation,
                requirement_id="R-1",
                prd_revision="P1",
                outcome_id="C2.3",
                issue_url="https://github.com/o/r/issues/32",
                issue_revision="I1",
                integrated_source="a" * 40,
                accepting_people={"ahuimanu"},
                artifact_checked=True,
            ),
            "missing",
        )

    def test_failed_unknown_or_unaccepted_result_never_passes(self) -> None:
        failed = parse_evidence(evidence_body(result="fail"))
        arguments = {
            "requirement_id": "R-1",
            "prd_revision": "P1",
            "outcome_id": "C2.3",
            "issue_url": "https://github.com/o/r/issues/32",
            "issue_revision": "I1",
            "integrated_source": "a" * 40,
        }
        self.assertEqual(
            assess_verification(
                failed, **arguments, accepting_people={"ahuimanu"}, artifact_checked=True
            ),
            "failed",
        )
        passed = parse_evidence(evidence_body())
        self.assertEqual(
            assess_verification(passed, **arguments, accepting_people=set(), artifact_checked=True),
            "unknown",
        )
        self.assertEqual(
            assess_verification(
                passed,
                **{**arguments, "integrated_source": "b" * 40},
                accepting_people={"ahuimanu"},
                artifact_checked=True,
            ),
            "stale",
        )
        self.assertEqual(
            assess_verification(
                passed,
                **{**arguments, "issue_url": "https://github.com/o/r/issues/99"},
                accepting_people={"ahuimanu"},
                artifact_checked=True,
            ),
            "stale",
        )
        self.assertEqual(
            assess_verification(
                passed, **arguments, accepting_people={"ahuimanu"}, artifact_checked=False
            ),
            "unknown",
        )

    def test_rejects_duplicate_keys_missing_claim_and_nonimmutable_source(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            parse_evidence(
                evidence_body().replace(
                    '"kind": "verification",', '"kind": "verification", "kind": "validation",'
                )
            )
        with self.assertRaisesRegex(ValueError, "integrated_source"):
            parse_evidence(evidence_body(source="main"))
        with self.assertRaisesRegex(ValueError, "validation.*users"):
            parse_evidence(evidence_body(kind="validation").replace('"maintainers"', ""))


if __name__ == "__main__":
    unittest.main()
