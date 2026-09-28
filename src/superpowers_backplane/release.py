"""Read-only release candidate identity and publication-gate assessment."""

from __future__ import annotations

import hashlib
import json
import re
from typing import TypedDict

REQUIRED_CANDIDATE = {
    "release_id",
    "issue",
    "issue_revision",
    "target_version",
    "selected_outcomes",
    "integrated_source",
    "prd_revision",
    "adr_revisions",
    "gate_id",
    "gate_revision",
    "evidence_revisions",
    "compatibility_revision",
    "source_hash",
}
MANDATORY_CHECKS = {"trace", "validation", "compatibility", "views", "blockers"}
VERDICTS = {"PASS", "FAIL", "UNKNOWN"}
VERSION = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\Z")


class ReleaseAssessment(TypedDict):
    status: str
    candidate_digest: str
    reasons: list[str]


def _nonempty(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError(f"invalid {field}")
    return value


def _revision_map(value: object, field: str, *, require_one: bool = False) -> dict[str, str]:
    if not isinstance(value, dict) or (require_one and not value):
        raise ValueError(f"invalid {field}")
    checked: dict[str, str] = {}
    for key, revision in value.items():
        checked[_nonempty(key, field)] = _nonempty(revision, field)
    return checked


def candidate_digest(candidate: dict[str, object]) -> str:
    """Hash exact pre-publication inputs, independent of JSON key order."""
    if set(candidate) != REQUIRED_CANDIDATE:
        raise ValueError("incomplete or unknown release candidate fields")
    for field in REQUIRED_CANDIDATE - {
        "selected_outcomes",
        "adr_revisions",
        "evidence_revisions",
    }:
        _nonempty(candidate[field], field)
    version = candidate["target_version"]
    source = candidate["integrated_source"]
    source_hash = candidate["source_hash"]
    if not isinstance(version, str) or not VERSION.fullmatch(version):
        raise ValueError("invalid target_version")
    if not isinstance(source, str) or not re.fullmatch(r"[0-9a-f]{40}", source):
        raise ValueError("invalid integrated_source")
    if not isinstance(source_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", source_hash):
        raise ValueError("invalid source_hash")
    _revision_map(candidate["selected_outcomes"], "selected_outcomes", require_one=True)
    _revision_map(candidate["adr_revisions"], "adr_revisions")
    _revision_map(candidate["evidence_revisions"], "evidence_revisions", require_one=True)
    canonical = (
        json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def assess_release(
    candidate: dict[str, object],
    checks: dict[str, object],
    named_approver: str,
    authorization: dict[str, object] | None,
) -> ReleaseAssessment:
    """Assess current facts; never create an approval, tag, or release."""
    digest = candidate_digest(candidate)
    _nonempty(named_approver, "named_approver")
    reasons: list[str] = []
    status = "PASS"
    selected = _revision_map(candidate["selected_outcomes"], "selected_outcomes")
    outcomes = checks.get("outcomes")
    if not isinstance(outcomes, dict) or set(outcomes) != set(selected):
        status = "UNKNOWN"
        reasons.append("selected outcome verification is incomplete")
    else:
        for outcome_id in sorted(selected):
            verdict = outcomes[outcome_id]
            if not isinstance(verdict, str) or verdict not in VERDICTS:
                verdict = "UNKNOWN"
            if verdict == "FAIL":
                status = "FAIL"
                reasons.append(f"{outcome_id} verification failed")
            elif verdict == "UNKNOWN" and status != "FAIL":
                status = "UNKNOWN"
                reasons.append(f"{outcome_id} verification unknown")
    for field in sorted(MANDATORY_CHECKS):
        verdict = checks.get(field, "UNKNOWN")
        if not isinstance(verdict, str) or verdict not in VERDICTS:
            verdict = "UNKNOWN"
        if verdict == "FAIL":
            status = "FAIL"
            reasons.append(f"{field} failed")
        elif verdict == "UNKNOWN" and status != "FAIL":
            status = "UNKNOWN"
            reasons.append(f"{field} unknown")
    if authorization is None:
        if status != "FAIL":
            status = "UNKNOWN"
        reasons.append("human authorization missing")
    elif authorization.get("checked") is not True:
        if status != "FAIL":
            status = "UNKNOWN"
        reasons.append("human authorization not independently checked")
    elif authorization.get("actor") != named_approver:
        if status != "FAIL":
            status = "UNKNOWN"
        reasons.append("authorization actor is not the named approver")
    elif (
        authorization.get("candidate_digest") != digest
        or authorization.get("version") != candidate["target_version"]
        or not authorization.get("scope")
    ):
        if status != "FAIL":
            status = "UNKNOWN"
        reasons.append("authorization does not cover the exact candidate")
    elif authorization.get("decision") == "reject":
        status = "FAIL"
        reasons.append("human rejected candidate")
    elif authorization.get("decision") != "approve":
        if status != "FAIL":
            status = "UNKNOWN"
        reasons.append("human decision unknown")
    return {"status": status, "candidate_digest": digest, "reasons": reasons}
