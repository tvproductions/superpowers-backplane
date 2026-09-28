"""Bounded read-only entry point for installed Backplane collection checks."""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable
from typing import Protocol

from .gh_adapter import GhIssueGateway


class PreflightGateway(Protocol):
    def list_issues(self) -> list[dict[str, object]]: ...

    def total_count(self) -> int: ...


def main(
    argv: list[str] | None = None,
    *,
    gateway_factory: Callable[[str], PreflightGateway] = GhIssueGateway,
) -> int:
    """Run only declared read-only operations; readiness remains unknown."""
    parser = argparse.ArgumentParser(prog="backplane")
    commands = parser.add_subparsers(dest="command", required=True)
    preflight = commands.add_parser("preflight", help="check read-only issue collection")
    preflight.add_argument("--repo", required=True, help="GitHub OWNER/REPO")
    arguments = parser.parse_args(argv)
    try:
        gateway = gateway_factory(arguments.repo)
        issues = gateway.list_issues()
        count = gateway.total_count()
        if len(issues) != count:
            raise ValueError("issue count changed during preflight")
    except (OSError, RuntimeError, ValueError):
        print(json.dumps({"repository": arguments.repo, "heavy_readiness": "UNKNOWN"}))
        return 2
    print(
        json.dumps(
            {
                "repository": arguments.repo,
                "issue_count": count,
                "recorded_issue_count": sum("record" in issue for issue in issues),
                "heavy_readiness": "UNKNOWN",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
