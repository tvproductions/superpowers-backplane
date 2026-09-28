"""Validate stable identities and typed issue links in a collected catalog."""

from __future__ import annotations

from collections import defaultdict
from typing import TypedDict
from urllib.parse import urlparse

from .record import _validate_record


class CatalogResult(TypedDict):
    by_id: dict[str, dict[str, object]]
    reverse: dict[str, list[tuple[str, str]]]


ISSUE_LINKS = {
    "belongs_to",
    "satisfies",
    "included_in",
    "gated_by",
    "released_in",
    "succeeds",
    "split_from",
    "merged_from",
    "supersedes",
}
DOCUMENT_LINKS = {
    "anchored_in_prd",
    "decided_by",
    "specified_by",
    "planned_by",
    "exemplified_by",
    "tested_by",
    "verified_by",
    "validated_by",
    "compatibility_reviewed_by",
    "authorized_by",
}
EXECUTION_LABELS = {
    "backplane:backlog",
    "backplane:designing",
    "backplane:ready",
    "backplane:active",
    "backplane:blocked",
    "backplane:review",
}


def _mapping(value: object, description: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"invalid {description}")
    return value


def _text(value: object, description: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError(f"invalid {description}")
    return value


def _validate_execution_labels(issue: dict[str, object], kind: object) -> None:
    state = issue.get("state")
    labels = issue.get("labels")
    if (
        not isinstance(state, str)
        or state not in {"OPEN", "CLOSED"}
        or not isinstance(labels, list)
    ):
        raise ValueError("issue missing state or labels")
    names: list[str] = []
    for item in labels:
        label = _mapping(item, "label")
        names.append(_text(label.get("name"), "label name"))
    execution = [name for name in names if name in EXECUTION_LABELS]
    if kind == "outcome" and state == "OPEN":
        if len(execution) != 1:
            raise ValueError("open outcome requires one execution label")
    elif execution:
        raise ValueError("non-open-outcome requires no execution label")


def validate_catalog(
    issues: list[dict[str, object]],
    requirement_ids: set[str],
    required_record_numbers: set[int] | None = None,
) -> CatalogResult:
    """Validate one complete collection; never infer absent IDs or edges."""
    if not isinstance(issues, list) or not isinstance(requirement_ids, set):
        raise ValueError("invalid catalog input")
    required_record_numbers = required_record_numbers or set()
    if any(type(number) is not int or number <= 0 for number in required_record_numbers):
        raise ValueError("invalid required record numbers")
    by_id: dict[str, dict[str, object]] = {}
    by_url: dict[str, dict[str, object]] = {}
    seen_numbers: set[int] = set()
    identities: set[str] = set()
    anchors: set[str] = set()
    for item in issues:
        issue = _mapping(item, "issue")
        number = issue.get("number")
        url = _text(issue.get("url"), "issue URL")
        if type(number) is not int or number <= 0 or not url.endswith(f"/issues/{number}"):
            raise ValueError("issue number/URL mismatch")
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError("invalid issue URL")
        if url in by_url:
            raise ValueError(f"duplicate issue URL: {url}")
        if number in seen_numbers:
            raise ValueError(f"duplicate issue number: {number}")
        seen_numbers.add(number)
        by_url[url] = issue
        if "record" not in issue:
            _validate_execution_labels(issue, "incidental")
            if number in required_record_numbers:
                raise ValueError(f"required Backplane Record missing on issue #{number}")
            continue
        record = _mapping(issue["record"], "issue record")
        _validate_record(record)
        kind = record.get("kind")
        _validate_execution_labels(issue, kind)
        if kind == "incidental":
            continue
        semantic_id = _text(record.get("semantic_id"), "semantic ID")
        if semantic_id in identities:
            raise ValueError(f"duplicate semantic ID: {semantic_id}")
        identities.add(semantic_id)
        by_id[semantic_id] = record
        if kind == "requirement":
            if semantic_id not in requirement_ids:
                raise ValueError(f"requirement {semantic_id} not in approved PRD")
            anchors.add(semantic_id)
    if missing := required_record_numbers - seen_numbers:
        raise ValueError(f"required issue missing from catalog: #{min(missing)}")
    for item in issues:
        if "record" not in item:
            continue
        record = _mapping(item["record"], "issue record")
        aliases = record.get("aliases", [])
        if not isinstance(aliases, list):
            raise ValueError("invalid aliases")
        for alias in aliases:
            name = _text(alias, "alias")
            if name in identities:
                raise ValueError(f"duplicate semantic ID or alias: {name}")
            identities.add(name)
    for semantic_id in sorted(requirement_ids - anchors):
        raise ValueError(f"missing requirement anchor: {semantic_id}")
    reverse: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for item in issues:
        if "record" not in item:
            continue
        record = _mapping(item["record"], "issue record")
        links = record.get("links")
        if not isinstance(links, list):
            raise ValueError("invalid links array")
        anchored = 0
        seen: set[tuple[str, str, str, str]] = set()
        for value in links:
            edge = _mapping(value, "typed link")
            link_type = _text(edge.get("type"), "link type")
            target = _mapping(edge.get("target"), "link target")
            key = (
                link_type,
                str(target.get("semantic_id", "")),
                str(target.get("issue", "")),
                str(target.get("locator", "")),
            )
            if key in seen:
                raise ValueError(f"duplicate typed link on issue #{item['number']}")
            seen.add(key)
            if link_type == "anchored_in_prd":
                anchored += 1
            target_id = _validate_link(record, link_type, target, by_url)
            if target_id is not None:
                reverse[target_id].append(
                    (_text(record.get("semantic_id"), "semantic ID"), link_type)
                )
        if record.get("kind") == "requirement" and anchored != 1:
            raise ValueError(f"requirement {record['semantic_id']} needs one anchored_in_prd link")
    return {"by_id": by_id, "reverse": dict(reverse)}


def _validate_link(
    source: dict[str, object],
    link_type: str,
    target: dict[str, object],
    by_url: dict[str, dict[str, object]],
) -> str | None:
    source_kind = source.get("kind")
    if link_type in ISSUE_LINKS:
        url = _text(target.get("issue"), "issue target")
        target_id = _text(target.get("semantic_id"), "target semantic ID")
        if "locator" in target or "revision" in target:
            raise ValueError("invalid issue target fields")
        if url not in by_url:
            raise ValueError(f"dangling target: {url}")
        destination = _mapping(by_url[url]["record"], "target record")
        if destination.get("semantic_id") != target_id:
            raise ValueError(f"target ID mismatch at {url}")
        target_kind = destination.get("kind")
        valid = {
            "belongs_to": source_kind == "outcome" and target_kind in {"capability", "epic"},
            "satisfies": source_kind == "outcome" and target_kind == "requirement",
            "included_in": source_kind == "outcome" and target_kind == "release",
            "released_in": source_kind == "outcome"
            and target_kind == "release"
            and destination.get("record_state") == "published",
            "gated_by": source_kind == "release" and target_kind == "gate",
            "split_from": source_kind == target_kind == "outcome"
            and source.get("semantic_id") != target_id,
            "merged_from": source_kind == target_kind == "outcome"
            and source.get("semantic_id") != target_id,
            "succeeds": source_kind == target_kind and source.get("semantic_id") != target_id,
            "supersedes": source_kind == target_kind and source.get("semantic_id") != target_id,
        }[link_type]
        if not valid:
            raise ValueError(f"invalid endpoint for {link_type}: {source_kind} -> {target_kind}")
        return target_id
    if link_type in DOCUMENT_LINKS:
        locator = _text(target.get("locator"), "document locator")
        _text(target.get("revision"), "document revision")
        if "issue" in target or "semantic_id" in target:
            raise ValueError("invalid document target fields")
        allowed = {
            "anchored_in_prd": source_kind == "requirement"
            and locator.rsplit("#", 1)[-1] == source.get("semantic_id"),
            "decided_by": source_kind not in {"incidental", None},
            "specified_by": source_kind == "outcome",
            "planned_by": source_kind == "outcome",
            "exemplified_by": source_kind in {"requirement", "outcome"},
            "tested_by": source_kind in {"requirement", "outcome"},
            "verified_by": source_kind in {"requirement", "outcome"},
            "validated_by": source_kind in {"outcome", "release"},
            "compatibility_reviewed_by": source_kind == "release",
            "authorized_by": source_kind == "release",
        }[link_type]
        if not allowed:
            raise ValueError(f"invalid endpoint for {link_type} from {source_kind}")
        return None
    raise ValueError(f"unknown link type: {link_type}")
