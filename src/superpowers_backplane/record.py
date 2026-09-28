"""Parse untrusted issue record blocks without interpreting issue prose."""

from __future__ import annotations

import json

HEADING = "## Backplane Record"
SCHEMA = "backplane-heavy/v1"
STATES = {
    "requirement": {"current", "stale", "unresolved"},
    "capability": {"proposed", "accepted", "retired"},
    "epic": {"proposed", "accepted", "retired"},
    "milestone": {"planned", "met", "cancelled"},
    "gate": {"pending", "satisfied", "failed", "cancelled"},
    "boundary": {"open", "fulfilled", "cancelled"},
    "release": {"assembling", "candidate", "approved", "published", "cancelled"},
    "incidental": {"captured", "triaged", "promoted", "discarded"},
}
RECORD_KEYS = {
    "schema",
    "kind",
    "semantic_id",
    "aliases",
    "record_state",
    "links",
    "target_version",
    "published_tag",
    "published_release",
    "published_source",
}
LINK_KEYS = {"type", "target", "source_revision"}
TARGET_KEYS = {"semantic_id", "issue", "locator", "revision"}


def _pairs_without_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError(f"invalid {field}")
    return value


def parse_record(body: str) -> dict[str, object]:
    """Return a single validated record; raise ValueError on absent or unsafe data."""
    if not isinstance(body, str) or len(body.encode("utf-8")) > 1_048_576:
        raise ValueError("issue body exceeds record parser limit")
    lines = body.replace("\r\n", "\n").split("\n")
    headings = [index for index, line in enumerate(lines) if line.strip() == HEADING]
    if not headings:
        raise ValueError("missing Backplane Record section")
    if len(headings) != 1:
        raise ValueError("multiple Backplane Record sections")
    index = headings[0] + 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines) or lines[index].strip() != "```json":
        raise ValueError("Backplane Record requires one fenced json object")
    start = index + 1
    index = start
    while index < len(lines) and lines[index].strip() != "```":
        index += 1
    if index >= len(lines):
        raise ValueError("unterminated Backplane Record JSON fence")
    raw = "\n".join(lines[start:index])
    if len(raw.encode("utf-8")) > 65_536:
        raise ValueError("Backplane Record JSON exceeds limit")
    decoder = json.JSONDecoder(object_pairs_hook=_pairs_without_duplicates)
    try:
        record, end = decoder.raw_decode(raw.lstrip())
    except (json.JSONDecodeError, ValueError) as error:
        raise ValueError(f"invalid Backplane Record JSON: {error}") from error
    if raw.lstrip()[end:].strip():
        raise ValueError("trailing JSON after Backplane Record object")
    if not isinstance(record, dict):
        raise ValueError("Backplane Record JSON must be an object")
    _validate_record(record)
    return record


def _validate_record(record: dict[str, object]) -> None:
    unknown = set(record) - RECORD_KEYS
    if unknown:
        raise ValueError(f"unknown field: {sorted(unknown)[0]}")
    if record.get("schema") != SCHEMA:
        raise ValueError("unsupported Backplane Record schema")
    kind = record.get("kind")
    if not isinstance(kind, str) or kind not in STATES | {"outcome": set()}:
        raise ValueError("unknown Backplane Record kind")
    if kind == "outcome":
        if "record_state" in record:
            raise ValueError("outcome must not have record_state")
    else:
        state = record.get("record_state")
        if not isinstance(state, str) or state not in STATES[kind]:
            raise ValueError(f"invalid or missing record_state for {kind}")
    if kind == "incidental":
        if "semantic_id" in record:
            raise ValueError("incidental must not have semantic_id")
    else:
        _string(record.get("semantic_id"), "semantic_id")
    aliases = record.get("aliases", [])
    if (
        not isinstance(aliases, list)
        or any(
            not isinstance(alias, str) or not alias or alias.strip() != alias for alias in aliases
        )
        or len(aliases) != len(set(aliases))
    ):
        raise ValueError("invalid aliases")
    links = record.get("links")
    if not isinstance(links, list):
        raise ValueError("missing or invalid links array")
    for link in links:
        if not isinstance(link, dict) or set(link) - LINK_KEYS:
            raise ValueError("invalid link fields")
        _string(link.get("type"), "link type")
        target = link.get("target")
        if not isinstance(target, dict) or set(target) - TARGET_KEYS:
            raise ValueError("invalid link target fields")
        if "source_revision" in link:
            _string(link["source_revision"], "source_revision")
    publication_keys = {"published_tag", "published_release", "published_source"}
    if kind != "release":
        if set(record) & ({"target_version"} | publication_keys):
            raise ValueError("release fields on non-release record")
    else:
        state = record["record_state"]
        if state in {"candidate", "approved", "published"}:
            _string(record.get("target_version"), "target_version")
        if state != "published" and set(record) & publication_keys:
            raise ValueError(f"{sorted(set(record) & publication_keys)[0]} before publication")
        if state == "published":
            for key in publication_keys:
                _string(record.get(key), key)
