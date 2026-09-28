"""Parse untrusted V&V artifacts and assess exact verification coverage."""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta
from typing import TypedDict, cast
from urllib.parse import urlparse

from .record import _pairs_without_duplicates

HEADING = "## Backplane Evidence"
SCHEMA = "backplane-evidence/v1"
KEYS = {
    "schema",
    "kind",
    "method",
    "result",
    "observed_at",
    "integrated_source",
    "requirements",
    "outcomes",
    "success_criteria",
    "users",
    "accepted_by",
}
SOURCE = re.compile(r"(?:[0-9a-f]{40}|sha256:[0-9a-f]{64})\Z")


class RequirementClaim(TypedDict):
    semantic_id: str
    prd_revision: str


class OutcomeClaim(TypedDict):
    semantic_id: str
    issue: str
    issue_revision: str


class EvidenceRecord(TypedDict):
    schema: str
    kind: str
    method: str
    result: str
    observed_at: str
    integrated_source: str
    requirements: list[RequirementClaim]
    outcomes: list[OutcomeClaim]
    success_criteria: list[str]
    users: list[str]
    accepted_by: str


def _text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError(f"invalid {field}")
    return value


def _text_list(value: object, field: str) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"invalid {field}")
    return [_text(item, field) for item in value]


def _claims(value: object, fields: set[str], description: str) -> list[dict[str, str]]:
    if not isinstance(value, list):
        raise ValueError(f"invalid {description}")
    result: list[dict[str, str]] = []
    for claim in value:
        if not isinstance(claim, dict) or set(claim) != fields:
            raise ValueError(f"invalid {description} claim")
        result.append({field: _text(claim[field], field) for field in fields})
    if len({item["semantic_id"] for item in result}) != len(result):
        raise ValueError(f"duplicate {description} claim")
    return result


def parse_evidence(markdown: str) -> EvidenceRecord:
    """Parse one evidence block; parsing does not approve its human or currency."""
    if not isinstance(markdown, str) or len(markdown.encode("utf-8")) > 1_048_576:
        raise ValueError("invalid evidence document")
    lines = markdown.replace("\r\n", "\n").split("\n")
    headings = [index for index, line in enumerate(lines) if line.strip() == HEADING]
    if len(headings) != 1:
        raise ValueError("expected exactly one Backplane Evidence section")
    start = headings[0] + 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start >= len(lines) or lines[start].strip() != "```json":
        raise ValueError("Backplane Evidence requires fenced json")
    end = start + 1
    while end < len(lines) and lines[end].strip() != "```":
        end += 1
    if end == len(lines):
        raise ValueError("unterminated Backplane Evidence JSON fence")
    raw = "\n".join(lines[start + 1 : end])
    if len(raw.encode("utf-8")) > 65_536:
        raise ValueError("Backplane Evidence JSON exceeds limit")
    decoder = json.JSONDecoder(object_pairs_hook=_pairs_without_duplicates)
    try:
        record, position = decoder.raw_decode(raw.lstrip())
    except (json.JSONDecodeError, ValueError) as error:
        raise ValueError(f"invalid Backplane Evidence JSON: {error}") from error
    if raw.lstrip()[position:].strip() or not isinstance(record, dict):
        raise ValueError("invalid Backplane Evidence JSON object")
    if set(record) != KEYS or record.get("schema") != SCHEMA:
        raise ValueError("invalid Backplane Evidence schema or fields")
    kind = _text(record["kind"], "kind")
    if kind not in {"verification", "validation", "impact_review"}:
        raise ValueError("invalid evidence kind")
    result = _text(record["result"], "result")
    if result not in {"pass", "fail", "unknown"}:
        raise ValueError("invalid evidence result")
    _text(record["method"], "method")
    observed = _text(record["observed_at"], "observed_at")
    try:
        timestamp = datetime.fromisoformat(observed.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("invalid observed_at") from error
    if timestamp.tzinfo is None or timestamp.utcoffset() != timedelta(0):
        raise ValueError("observed_at must be UTC")
    source = _text(record["integrated_source"], "integrated_source")
    if not SOURCE.fullmatch(source):
        raise ValueError("invalid integrated_source")
    requirements = _claims(record["requirements"], {"semantic_id", "prd_revision"}, "requirements")
    outcomes = _claims(record["outcomes"], {"semantic_id", "issue", "issue_revision"}, "outcomes")
    for outcome in outcomes:
        issue = urlparse(outcome["issue"])
        if (
            issue.scheme != "https"
            or not issue.netloc
            or not re.search(r"/issues/[1-9][0-9]*\Z", issue.path)
        ):
            raise ValueError("invalid outcome issue URL")
    users = _text_list(record["users"], "users")
    criteria = _text_list(record["success_criteria"], "success_criteria")
    _text(record["accepted_by"], "accepted_by")
    if kind == "verification" and (not requirements or not outcomes):
        raise ValueError("verification requires requirements and outcomes")
    if kind == "validation" and (not users or not criteria):
        raise ValueError("validation requires users and success_criteria")
    return cast("EvidenceRecord", record)


def assess_verification(
    record: EvidenceRecord,
    *,
    requirement_id: str,
    prd_revision: str,
    outcome_id: str,
    issue_url: str,
    issue_revision: str,
    integrated_source: str,
    accepting_people: set[str],
    artifact_checked: bool,
) -> str:
    """Assess one edge only after its linked artifact revision is checked."""
    if record["kind"] != "verification":
        return "missing"
    requirements = [
        item for item in record["requirements"] if item["semantic_id"] == requirement_id
    ]
    outcomes = [item for item in record["outcomes"] if item["semantic_id"] == outcome_id]
    if not requirements or not outcomes:
        return "missing"
    if (
        not any(item["prd_revision"] == prd_revision for item in requirements)
        or not any(
            item["issue"] == issue_url and item["issue_revision"] == issue_revision
            for item in outcomes
        )
        or record["integrated_source"] != integrated_source
    ):
        return "stale"
    if not artifact_checked:
        return "unknown"
    if record["accepted_by"] not in accepting_people:
        return "unknown"
    if record["result"] == "fail":
        return "failed"
    if record["result"] != "pass":
        return "unknown"
    return "current"
