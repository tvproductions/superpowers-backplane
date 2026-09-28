"""Read-only GitHub CLI collection boundary for heavy issue snapshots."""

from __future__ import annotations

import json
import re
import subprocess
from collections.abc import Callable

from .record import HEADING, parse_record

FIELDS = (
    "number,title,body,state,stateReason,labels,assignees,url,updatedAt,"
    "issueType,parent,subIssues,blockedBy,blocking,closedByPullRequestsReferences"
)
COUNT_QUERY = (
    "query($owner:String!,$name:String!){repository(owner:$owner,name:$name)"
    "{issues(states:[OPEN,CLOSED],first:1){totalCount}}}"
)
REPO_PATTERN = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")


def _run(arguments: list[str]) -> str:
    """Invoke gh without a shell and require strict UTF-8 JSON output."""
    try:
        result = subprocess.run(
            arguments,
            capture_output=True,
            check=False,
            shell=False,
            timeout=120,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError("gh timed out") from error
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"gh failed ({result.returncode}): {detail}")
    try:
        return result.stdout.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise RuntimeError("gh returned non-UTF-8 output") from error


def _json_object(value: str) -> dict[str, object]:
    parsed = json.loads(value)
    if not isinstance(parsed, dict):
        raise ValueError("gh response is not an object")
    return parsed


class GhIssueGateway:
    """Collect all issue fields and independently check cardinality/revisions."""

    def __init__(self, repository: str, runner: Callable[[list[str]], str] = _run) -> None:
        if not REPO_PATTERN.fullmatch(repository):
            raise ValueError("repository must be OWNER/REPO")
        self.repository = repository
        self.owner, self.name = repository.split("/", 1)
        self.runner = runner

    def total_count(self) -> int:
        response = _json_object(
            self.runner(
                [
                    "gh",
                    "api",
                    "graphql",
                    "-f",
                    f"query={COUNT_QUERY}",
                    "-f",
                    f"owner={self.owner}",
                    "-f",
                    f"name={self.name}",
                ]
            )
        )
        data = response.get("data")
        if not isinstance(data, dict):
            raise ValueError("GraphQL issue count unavailable")
        repository = data.get("repository")
        if not isinstance(repository, dict):
            raise ValueError("GraphQL repository unavailable")
        issues = repository.get("issues")
        if not isinstance(issues, dict):
            raise ValueError("GraphQL issue count unavailable")
        count = issues.get("totalCount")
        if type(count) is not int or count < 0:
            raise ValueError("invalid GraphQL issue count")
        return count

    def list_issues(self) -> list[dict[str, object]]:
        expected = self.total_count()
        raw = json.loads(
            self.runner(
                [
                    "gh",
                    "issue",
                    "list",
                    "--repo",
                    self.repository,
                    "--state",
                    "all",
                    "--limit",
                    str(max(1, expected + 1)),
                    "--json",
                    FIELDS,
                ]
            )
        )
        if not isinstance(raw, list) or len(raw) != expected:
            raise ValueError("issue count does not match independent GraphQL total")
        issues: list[dict[str, object]] = []
        for value in raw:
            if not isinstance(value, dict):
                raise ValueError("invalid issue in gh response")
            issue: dict[str, object] = value
            number = issue.get("number")
            body = issue.get("body")
            if type(number) is not int or not isinstance(body, str):
                raise ValueError("issue missing number or body")
            for key in ("subIssues", "blockedBy", "blocking"):
                edge = issue.get(key)
                if not isinstance(edge, dict):
                    raise ValueError(f"missing {key} on issue #{number}")
                nodes, total = edge.get("nodes"), edge.get("totalCount")
                if not isinstance(nodes, list) or type(total) is not int or len(nodes) != total:
                    raise ValueError(f"incomplete {key} on issue #{number}")
            if HEADING in body.splitlines():
                issue["record"] = parse_record(body)
            issues.append(issue)
        return issues

    def revisions(self, numbers: list[int]) -> dict[int, str]:
        results: dict[int, str] = {}
        for number in numbers:
            if type(number) is not int or number <= 0 or number in results:
                raise ValueError("invalid issue revision request")
            item = _json_object(
                self.runner(
                    [
                        "gh",
                        "issue",
                        "view",
                        str(number),
                        "--repo",
                        self.repository,
                        "--json",
                        "number,url,updatedAt",
                    ]
                )
            )
            expected_url = f"https://github.com/{self.repository}/issues/{number}"
            updated = item.get("updatedAt")
            if item.get("number") != number or item.get("url") != expected_url:
                raise ValueError(f"issue revision identity mismatch: #{number}")
            if not isinstance(updated, str) or not updated:
                raise ValueError(f"issue revision unavailable: #{number}")
            results[number] = updated
        return results
