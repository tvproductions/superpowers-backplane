"""Read exact requirement IDs, wording, and criteria from a canonical PRD table."""

from __future__ import annotations

import re

ID_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*$")


def _cells(line: str) -> list[str]:
    if not line.startswith("|") or not line.rstrip().endswith("|"):
        raise ValueError("malformed PRD requirement row")
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for character in line.strip()[1:-1]:
        if escaped:
            current.append(character)
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def parse_requirements(markdown: str) -> dict[str, dict[str, str]]:
    """Extract the approved PRD's canonical requirement table, without approving it."""
    if not isinstance(markdown, str):
        raise ValueError("PRD must be text")
    lines = markdown.splitlines()
    table = -1
    for index, line in enumerate(lines):
        if line.startswith("|"):
            cells = _cells(line)
            if len(cells) == 3 and cells[0] == "ID" and cells[1] == "Requirement wording":
                if table >= 0:
                    raise ValueError("multiple PRD requirement tables")
                table = index
    if table < 0 or table + 1 >= len(lines):
        raise ValueError("missing PRD requirement table")
    separator = _cells(lines[table + 1])
    if len(separator) != 3 or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
        raise ValueError("invalid PRD requirement table separator")
    requirements: dict[str, dict[str, str]] = {}
    for line in lines[table + 2 :]:
        if not line.startswith("|"):
            break
        cells = _cells(line)
        if len(cells) != 3:
            raise ValueError("malformed PRD requirement row")
        marker, wording, criterion = cells
        if not marker.startswith("`") or not marker.endswith("`"):
            raise ValueError("invalid requirement ID cell")
        semantic_id = marker[1:-1]
        if not ID_PATTERN.fullmatch(semantic_id):
            raise ValueError("invalid requirement ID")
        if semantic_id in requirements:
            raise ValueError(f"duplicate requirement ID: {semantic_id}")
        if not wording:
            raise ValueError(f"missing requirement wording: {semantic_id}")
        if not criterion:
            raise ValueError(f"missing success criterion: {semantic_id}")
        requirements[semantic_id] = {"wording": wording, "criterion": criterion}
    if not requirements:
        raise ValueError("empty PRD requirement table")
    return requirements
