"""Build directional requirement/outcome trace from one validated issue graph."""

from __future__ import annotations

from typing import TypedDict, cast

from .catalog import validate_catalog


class TraceRow(TypedDict):
    requirement_id: str
    outcome_id: str
    link_currency: str


class TraceResult(TypedDict):
    forward: dict[str, list[TraceRow]]
    reverse: dict[str, list[TraceRow]]
    uncovered_requirements: list[str]


def _mapping(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError("invalid trace record")
    return value


def _links(record: dict[str, object]) -> list[dict[str, object]]:
    links = record.get("links")
    if not isinstance(links, list):
        raise ValueError("invalid trace links")
    return [cast("dict[str, object]", item) for item in links]


def _anchor_currency(record: dict[str, object], revision: str) -> str:
    if record.get("record_state") == "unresolved":
        return "unknown"
    if record.get("record_state") != "current":
        return "stale"
    anchors = [link for link in _links(record) if link.get("type") == "anchored_in_prd"]
    if len(anchors) != 1:
        return "unknown"
    target = _mapping(anchors[0].get("target"))
    return "current" if target.get("revision") == revision else "stale"


def build_trace(
    issues: list[dict[str, object]], requirement_revisions: dict[str, str]
) -> TraceResult:
    """Report link currency only; a current link is not passing verification."""
    validate_catalog(issues, set(requirement_revisions))
    by_id: dict[str, tuple[dict[str, object], dict[str, object]]] = {}
    for issue in issues:
        if "record" not in issue:
            continue
        record = _mapping(issue["record"])
        semantic_id = record.get("semantic_id")
        if isinstance(semantic_id, str):
            by_id[semantic_id] = (issue, record)

    forward: dict[str, list[TraceRow]] = {key: [] for key in sorted(requirement_revisions)}
    reverse: dict[str, list[TraceRow]] = {}
    for outcome_id, (issue, record) in sorted(by_id.items()):
        if record.get("kind") != "outcome":
            continue
        rows: list[TraceRow] = []
        for link in _links(record):
            if link.get("type") != "satisfies":
                continue
            target = _mapping(link.get("target"))
            requirement_id = target.get("semantic_id")
            if not isinstance(requirement_id, str):
                raise ValueError("invalid requirement target")
            requirement_record = by_id[requirement_id][1]
            currency = _anchor_currency(requirement_record, requirement_revisions[requirement_id])
            if link.get("source_revision") is not None and link["source_revision"] != issue.get(
                "updatedAt"
            ):
                currency = "stale"
            row: TraceRow = {
                "requirement_id": requirement_id,
                "outcome_id": outcome_id,
                "link_currency": currency,
            }
            forward[requirement_id].append(row)
            rows.append(row)
        reverse[outcome_id] = sorted(rows, key=lambda row: row["requirement_id"])
    for rows in forward.values():
        rows.sort(key=lambda row: row["outcome_id"])
    return {
        "forward": forward,
        "reverse": reverse,
        "uncovered_requirements": sorted(
            requirement_id for requirement_id, rows in forward.items() if not rows
        ),
    }
