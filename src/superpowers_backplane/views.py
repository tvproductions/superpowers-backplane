"""Render deterministic, readable roadmap and backlog projections."""

from __future__ import annotations

import hashlib
import json
import re
from typing import cast

from .catalog import EXECUTION_LABELS
from .snapshot import SnapshotResult, _normalized
from .trace import build_trace

REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")


def _map(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError("invalid view input")
    return value


def _markdown(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("missing view text")
    return (
        value.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("`", "\\`")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\r", " ")
        .replace("\n", " ")
    )


def _links(record: dict[str, object], link_type: str) -> str:
    raw = record.get("links")
    if not isinstance(raw, list):
        raise ValueError("missing typed links")
    targets: list[str] = []
    for value in raw:
        link = _map(value)
        if link.get("type") == link_type:
            target = _map(link.get("target"))
            semantic_id = target.get("semantic_id")
            if not isinstance(semantic_id, str):
                raise ValueError("missing typed target ID")
            targets.append(semantic_id)
    return ", ".join(sorted(targets)) or "—"


def _label(issue: dict[str, object]) -> str:
    labels = issue.get("labels")
    if not isinstance(labels, list):
        raise ValueError("missing issue labels")
    names = [_map(item).get("name") for item in labels]
    execution = [name for name in names if isinstance(name, str) and name in EXECUTION_LABELS]
    return str(execution[0]) if execution else "closed"


def _blockers(issue: dict[str, object]) -> str:
    blocked = issue.get("blockedBy")
    if not isinstance(blocked, dict):
        return "UNKNOWN"
    nodes = blocked.get("nodes")
    if not isinstance(nodes, list):
        return "UNKNOWN"
    numbers = []
    for value in nodes:
        number = _map(value).get("number")
        if type(number) is not int:
            return "UNKNOWN"
        numbers.append(number)
    return ", ".join(f"#{number}" for number in sorted(numbers)) or "—"


def render_views(
    snapshot: SnapshotResult, requirement_revisions: dict[str, str], repository: str
) -> dict[str, bytes]:
    """Produce both view byte streams from one checked snapshot, without writes."""
    if not REPOSITORY.fullmatch(repository):
        raise ValueError("invalid repository")
    source_hash = snapshot["source_hash"]
    if hashlib.sha256(snapshot["canonical_bytes"]).hexdigest() != source_hash:
        raise ValueError("snapshot hash mismatch")
    source = json.loads(snapshot["canonical_bytes"])
    if (
        not isinstance(source, dict)
        or source.get("issues") != _normalized(snapshot["issues"])
        or source.get("documents") != snapshot["document_hashes"]
    ):
        raise ValueError("snapshot hash mismatch with render inputs")
    trace = build_trace(snapshot["issues"], requirement_revisions)
    header = f"<!-- backplane-view/v1 repository={repository} sha256={source_hash} -->\n"
    roadmap = [
        header,
        "# Roadmap\n",
        "Generated from the approved PRD and validated GitHub issue snapshot. "
        "Edit those sources, not this view.\n",
        "| ID | Kind | State | Issue | Family | Requirements | Target release | Blockers |\n",
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n",
    ]
    backlog = [
        header,
        "# Backlog\n",
        "Generated from the same validated source snapshot as ROADMAP.md.\n",
        "## Local outcomes\n",
        "| ID | Outcome | Execution | Issue | Requirements and link currency | "
        "Release | Blockers |\n",
        "| --- | --- | --- | --- | --- | --- | --- |\n",
    ]
    incidental: list[str] = []
    for issue in sorted(snapshot["issues"], key=lambda item: cast("int", item["number"])):
        number = issue["number"]
        url = issue["url"]
        title = _markdown(issue.get("title", f"Issue #{number}"))
        if "record" not in issue:
            incidental.append(f"| #{number} | {title} | {url} |\n")
            continue
        record = _map(issue["record"])
        kind = record.get("kind")
        semantic_id = record.get("semantic_id")
        if kind == "incidental":
            incidental.append(f"| #{number} | {title} | {url} |\n")
            continue
        if not isinstance(kind, str) or not isinstance(semantic_id, str):
            raise ValueError("invalid planned node in view")
        if kind == "requirement":
            continue
        state = _label(issue) if kind == "outcome" else _markdown(record.get("record_state"))
        requirements = _links(record, "satisfies") if kind == "outcome" else "—"
        roadmap.append(
            f"| {semantic_id} | {kind} | {state} | [#{number}]({url}) | "
            f"{_links(record, 'belongs_to')} | {requirements} | "
            f"{_links(record, 'included_in')} | {_blockers(issue)} |\n"
        )
        if kind == "outcome":
            rows = trace["reverse"].get(semantic_id, [])
            claims = (
                ", ".join(f"{row['requirement_id']} ({row['link_currency']})" for row in rows)
                or "—"
            )
            backlog.append(
                f"| {semantic_id} | {title} | {state} | [#{number}]({url}) | "
                f"{claims} | {_links(record, 'included_in')} | {_blockers(issue)} |\n"
            )
    backlog.extend(
        [
            "\n## Incidental intake\n",
            "| Issue | Intake | URL |\n",
            "| --- | --- | --- |\n",
            *incidental,
        ]
    )
    return {
        "ROADMAP.md": "".join(roadmap).encode("utf-8"),
        "BACKLOG.md": "".join(backlog).encode("utf-8"),
    }
