"""Collect a checked issue/document source identity without writing views."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable
from typing import Protocol, TypedDict

from .catalog import validate_catalog


class IssueGateway(Protocol):
    def list_issues(self) -> list[dict[str, object]]: ...

    def total_count(self) -> int: ...

    def revisions(self, numbers: list[int]) -> dict[int, str]: ...


class SnapshotResult(TypedDict):
    count: int
    issues: list[dict[str, object]]
    document_hashes: dict[str, str]
    canonical_bytes: bytes
    source_hash: str


def _hash_documents(documents: dict[str, bytes]) -> dict[str, str]:
    if not documents or any(
        not isinstance(path, str) or not path or not isinstance(content, bytes)
        for path, content in documents.items()
    ):
        raise ValueError("missing or invalid approved documents")
    return {
        path: hashlib.sha256(content).hexdigest() for path, content in sorted(documents.items())
    }


UNORDERED_FIELDS = {
    "labels",
    "assignees",
    "aliases",
    "links",
    "subIssues",
    "blockedBy",
    "blocking",
    "closingIssuesReferences",
}


def _normalized(value: object, field: str = "") -> object:
    """Remove ordering noise only from fields whose arrays are sets."""
    if isinstance(value, dict):
        return {key: _normalized(item, key) for key, item in sorted(value.items())}
    if isinstance(value, list):
        items = [_normalized(item) for item in value]
        if field in UNORDERED_FIELDS:
            return sorted(
                items,
                key=lambda item: json.dumps(
                    item, sort_keys=True, ensure_ascii=False, separators=(",", ":")
                ),
            )
        return items
    return value


def _revisions(issues: list[dict[str, object]]) -> dict[int, str]:
    revisions: dict[int, str] = {}
    for item in issues:
        number, updated = item.get("number"), item.get("updatedAt")
        if type(number) is not int or number <= 0 or not isinstance(updated, str) or not updated:
            raise ValueError("issue missing number or updatedAt")
        if number in revisions:
            raise ValueError(f"duplicate issue number: {number}")
        revisions[number] = updated
    return revisions


def _issue_number(item: dict[str, object]) -> int:
    number = item.get("number")
    if type(number) is not int:
        raise ValueError("issue missing number")
    return number


def collect_snapshot(
    gateway: IssueGateway,
    read_documents: Callable[[], dict[str, bytes]],
    requirement_ids: set[str],
    max_attempts: int = 2,
    required_record_numbers: set[int] | None = None,
) -> SnapshotResult:
    """Retry observed source drift; fail closed on incomplete or unknown input.

    The gateway must provide list_issues, total_count, and revisions. The
    document reader is invoked before and after each issue collection.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    for _ in range(max_attempts):
        try:
            before_documents = _hash_documents(read_documents())
            issues = gateway.list_issues()
            if not isinstance(issues, list):
                raise ValueError("issue collection is not a list")
            expected_count = gateway.total_count()
            if type(expected_count) is not int or len(issues) != expected_count:
                raise ValueError("issue count does not match independent total")
            revisions = _revisions(issues)
            validate_catalog(issues, requirement_ids, required_record_numbers)
            after_revisions = gateway.revisions(sorted(revisions))
            after_count = gateway.total_count()
            after_documents = _hash_documents(read_documents())
        except (OSError, RuntimeError, StopIteration) as error:
            raise ValueError(f"source unavailable: {error}") from error
        if (
            revisions != after_revisions
            or expected_count != after_count
            or before_documents != after_documents
        ):
            continue
        ordered_issues = sorted(issues, key=_issue_number)
        source = {
            "schema": "backplane-snapshot/v1",
            "documents": before_documents,
            "issues": _normalized(ordered_issues),
        }
        canonical = (
            json.dumps(source, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        return {
            "count": expected_count,
            "issues": ordered_issues,
            "document_hashes": before_documents,
            "canonical_bytes": canonical,
            "source_hash": hashlib.sha256(canonical).hexdigest(),
        }
    raise ValueError("source changed during collection; freshness unknown")
