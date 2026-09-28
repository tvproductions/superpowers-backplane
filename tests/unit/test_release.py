"""Release identity, evidence gate, and human authorization remain separate."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from superpowers_backplane.release import assess_release, candidate_digest  # noqa: E402


def candidate() -> dict[str, object]:
    return {
        "release_id": "REL-1",
        "issue": "https://github.com/o/r/issues/1",
        "issue_revision": "I1",
        "target_version": "1.0.0",
        "selected_outcomes": {"C2.3": "I2", "C2.4": "I3"},
        "integrated_source": "a" * 40,
        "prd_revision": "P2",
        "adr_revisions": {"docs/adr.md": "A1"},
        "gate_id": "G-1",
        "gate_revision": "G1",
        "evidence_revisions": {"docs/vv.md": "V1"},
        "compatibility_revision": "K1",
        "source_hash": "b" * 64,
    }


def checks() -> dict[str, object]:
    return {
        "outcomes": {"C2.3": "PASS", "C2.4": "PASS"},
        "trace": "PASS",
        "validation": "PASS",
        "compatibility": "PASS",
        "views": "PASS",
        "blockers": "PASS",
    }


def authorization(digest: str) -> dict[str, object]:
    return {
        "actor": "ahuimanu",
        "decision": "approve",
        "candidate_digest": digest,
        "version": "1.0.0",
        "scope": "publish tag and GitHub release",
        "checked": True,
    }


class ReleaseTests(unittest.TestCase):
    def test_current_candidate_needs_exact_checked_human_authorization(self) -> None:
        selected = candidate()
        digest = candidate_digest(selected)
        self.assertEqual(assess_release(selected, checks(), "ahuimanu", None)["status"], "UNKNOWN")
        self.assertEqual(
            assess_release(selected, checks(), "ahuimanu", authorization(digest))["status"],
            "PASS",
        )
        agent = authorization(digest)
        agent["actor"] = "backplane-agent"
        self.assertEqual(assess_release(selected, checks(), "ahuimanu", agent)["status"], "UNKNOWN")

    def test_release_slip_preserves_id_but_invalidates_authorization(self) -> None:
        selected = candidate()
        before = candidate_digest(selected)
        slipped = copy.deepcopy(selected)
        slipped["target_version"] = "1.1.0"
        self.assertEqual(slipped["release_id"], selected["release_id"])
        self.assertNotEqual(before, candidate_digest(slipped))
        self.assertEqual(
            assess_release(slipped, checks(), "ahuimanu", authorization(before))["status"],
            "UNKNOWN",
        )

    def test_missing_or_failed_mandatory_input_blocks_gate(self) -> None:
        selected = candidate()
        digest = candidate_digest(selected)
        missing = checks()
        missing["validation"] = "UNKNOWN"
        self.assertEqual(
            assess_release(selected, missing, "ahuimanu", authorization(digest))["status"],
            "UNKNOWN",
        )
        failed = checks()
        failed["outcomes"] = {"C2.3": "PASS", "C2.4": "FAIL"}
        self.assertEqual(
            assess_release(selected, failed, "ahuimanu", authorization(digest))["status"],
            "FAIL",
        )

    def test_selected_outcome_needs_explicit_current_verification(self) -> None:
        selected = candidate()
        incomplete = checks()
        incomplete["outcomes"] = {"C2.3": "PASS"}
        self.assertEqual(
            assess_release(
                selected, incomplete, "ahuimanu", authorization(candidate_digest(selected))
            )["status"],
            "UNKNOWN",
        )


if __name__ == "__main__":
    unittest.main()
