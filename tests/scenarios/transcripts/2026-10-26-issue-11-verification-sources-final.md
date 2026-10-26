# Final owned verification helper sources

Post-format sources for reproducibility. The preceding verification-sources transcript preserves the earlier sources actually used for the live runs. These final sources include the executable-availability guard; no live result is relabeled as a rerun merely because formatting changed.

## absent_setup_probe.py

SHA-256: `43d86a2349a7ea32846796eacd2df3f483a97924ea8e559a58dfd63ea9246ea6`

```python
"""Exercise authorized missing-upstream acquisition in the isolated setup profile."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = (work / "setup-profile").resolve(strict=True)
captures = work / "absent-setup-captures"
assert not captures.exists()
captures.mkdir()
env = dict(
    os.environ,
    CLAUDE_CONFIG_DIR=str(profile),
    PYTHONIOENCODING="utf-8",
    TMPDIR=str(captures),
    TEMP=str(captures),
    TMP=str(captures),
)
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run(args, *, timeout=90, cwd=root):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def snapshot():
    normal = Path.home() / ".claude"
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "normal_profile": {
            str(p.relative_to(normal)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                normal / "settings.json",
                normal / "plugins/installed_plugins.json",
                normal / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "dev_upstream_head": run(
            ["git", "-C", str(root / ".agents/superpowers"), "rev-parse", "HEAD"]
        ),
        "dev_upstream_status": run(
            ["git", "-C", str(root / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }


before = snapshot()
assert not any(p["id"].startswith("superpowers@") for p in before["plugins"])
(work / "absent-before.json").write_text(
    json.dumps(before, indent=2) + "\n", encoding="utf-8", newline="\n"
)
prompt = (
    "Set up Superpowers Backplane in this Claude Code session. The target repository is "
    "tvproductions/superpowers-backplane and existing issue is #11, for read-only intake only. "
    "Use the installed Backplane backlog skill and its installation reference. "
    "This is the absent-upstream mode: this selected profile has Backplane but no upstream plugin, "
    "and no --plugin-dir upstream is supplied. Do not substitute the development checkout. "
    f"The exact isolated test profile is {profile}. The operator authorizes registering "
    "anthropics/claude-plugins-official and installing superpowers@claude-plugins-official "
    "with user scope only in this selected profile, as required by the approved setup test. "
    "Read the current upstream-documented native channel and inspect the actual catalog; "
    "the pre-install observation found catalog commit 58267944f92187b7d6a1c822165c96c81c864806 "
    "pins stable upstream bb92a77741419a4ab5f06e711a283343f1ada0c3 (7.0.0), "
    "distinct from the development checkout 7.0.1. Record the actual installed version/source. "
    "Do not replace or update any existing development/normal-profile upstream installation. "
    "Backplane is local immutable development candidate 91ea3bb7933b5aa2c7628595f17157810cafa701; "
    "do not claim it has been published. Verify source/version, one effective Backplane and required "
    "upstream skills, gh auth/full intake/label/closure help. Do not mutate GitHub or create a plan/handoff. "
    f"Capture any output only under {captures}; never enumerate environment variables or read credentials. "
    "After the installation/preflight, report any need for a fresh session and unperformed conformance honestly. "
    "Do not spawn additional Claude sessions yourself; the outer harness will run fresh discovery and conformance."
)
allowed = [
    "Skill",
    "Read",
    "Glob",
    "Bash(gh auth status*)",
    "Bash(gh issue view *)",
    "Bash(gh issue edit --help)",
    "Bash(gh issue close --help)",
    "Bash(gh release view *)",
    "Bash(gh api repos/obra/superpowers/*)",
    "Bash(gh api repos/anthropics/claude-plugins-official/*)",
    "Bash(claude plugin list *)",
    "Bash(claude plugin marketplace list *)",
    "Bash(claude plugin marketplace add anthropics/claude-plugins-official*)",
    "Bash(claude plugin install superpowers@claude-plugins-official*)",
    "Bash(git -C * rev-parse *)",
    "Bash(git -C * remote get-url *)",
    "Bash(git -C * status *)",
    "Bash(claude --version)",
    "Bash(gh --version)",
]
args = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash,Glob",
    "--allowedTools",
    *allowed,
    "--permission-mode",
    "default",
    "--disallowedTools",
    "Bash(env *)",
    "Bash(printenv *)",
    "--add-dir",
    str(captures),
    str(profile),
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "36",
]
stream = run(args, cwd=work / "native-neutral", timeout=360)
(work / "absent-setup.jsonl").write_text(stream, encoding="utf-8", newline="\n")
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
host = next(e for e in reversed(events) if e.get("type") == "result")
calls: list[dict[str, Any]] = []
results = []
for event in events:
    message = event.get("message")
    if not isinstance(message, dict):
        continue
    for block in message.get("content", []):
        if not isinstance(block, dict):
            continue
        if block.get("type") == "tool_use":
            calls.append(block)
        if block.get("type") == "tool_result":
            results.append(block)
after = snapshot()
same = all(
    before[key] == after[key]
    for key in (
        "normal_profile",
        "dev_upstream_head",
        "dev_upstream_status",
        "project_refs",
        "issue11",
    )
)
same &= [p for p in before["plugins"] if not p["id"].startswith("superpowers@")] == [
    p for p in after["plugins"] if not p["id"].startswith("superpowers@")
]
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "mode": "absent upstream",
    "prompt": prompt,
    "argv": args,
    "before": before,
    "after": after,
    "protected_state_preserved": same,
    "expected_changes": "Only new official upstream plugin and marketplace in the selected profile",
    "tool_calls": calls,
    "tool_results": results,
    "host_result": host,
    "result": "UNSCORED; inspect acquisition and preflight, then run fresh discovery",
}
(root / "tests/scenarios/2026-10-26-issue-11-absent-setup.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
assert same, "Unexpected protected state change; preserve evidence before repair"
assert host.get("subtype") == "success" and not host.get("is_error"), host.get(
    "subtype"
)
assert any(p["id"] == "superpowers@claude-plugins-official" for p in after["plugins"])
print(
    json.dumps(
        {
            "subtype": host.get("subtype"),
            "session": host.get("session_id"),
            "protected_state_preserved": same,
            "response": host.get("result"),
        },
        indent=2,
    )
)
```

## archive_verification.py

SHA-256: `7bc18085e4fa3d2770ea8ce5758abff5f163ae6482cb6d810fa3ecb8f278449e`

```python
"""Preserve bounded observations, reviewed responses and exact owned helper sources."""

import hashlib
import json
from pathlib import Path
import re

from lifecycle_helpers import write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
target = root / "tests/scenarios"
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compact_stream(text):
    events = [json.loads(line) for line in text.splitlines() if line.strip()]
    result = next((e for e in reversed(events) if e.get("type") == "result"), {})
    calls, results, bases = [], [], []
    for event in events:
        message = event.get("message")
        if not isinstance(message, dict):
            continue
        for block in message.get("content", []):
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                calls.append(block)
            if block.get("type") == "tool_result":
                content = block.get("content", "")
                encoded = json.dumps(content, ensure_ascii=False)
                results.append(
                    {
                        "tool_use_id": block.get("tool_use_id"),
                        "is_error": block.get("is_error", False),
                        "content_sha256": digest(encoded),
                        "content_characters": len(encoded),
                    }
                )
            if isinstance(block.get("text"), str):
                bases += re.findall(
                    r"Base directory for this skill: ([^\r\n]+)", block["text"]
                )
    return {
        "session": result.get("session_id"),
        "subtype": result.get("subtype"),
        "is_error": result.get("is_error"),
        "response": result.get("result"),
        "tool_calls": calls,
        "tool_result_observations": results,
        "skill_base_directories": bases,
        "raw_stream_sha256": digest(text),
        "capture_policy": "Raw stream retained only in ignored scratch. Tool-result bodies hashed to avoid copying upstream skills or private environment contents; final response and actual calls retained.",
    }


notes = {
    "native-issue-intake": [
        (
            "Complete native hierarchy/dependency/PR intake",
            "The initial full gh issue view lists every required field.",
        ),
        (
            "Refuse blocked or unreconciled execution",
            "Decision refuses #42 while #37 is unresolved and the post-plan edit is unreconciled.",
        ),
        (
            "Issue/spec/plan layered authority",
            "Authority section assigns current intent to issue, design to approved spec and execution to current plan.",
        ),
        (
            "Backplane lifecycle without Project/IssueOps authority",
            "Transitions use backplane labels and native relationships exclusively.",
        ),
        (
            "Consumer verification and release rules",
            "Uses project verification on integration and separates release authority.",
        ),
        (
            "Integrated acceptance and fresh verification before closure",
            "Closure requires merged target and fresh acceptance checks; PR readiness is insufficient.",
        ),
    ],
    "language-neutral-verification": [
        (
            "Only cargo test --workspace verifies project",
            "The sole verification command is repeated for worktree and integrated target.",
        ),
        (
            "No Python or prohibited test framework introduced",
            "Explicitly excludes Backplane's own Python/Astral policy from the consumer.",
        ),
        (
            "Native graph and revision binding",
            "Full native intake, leaf/parent/blocker validation and updatedAt reconciliation are specified.",
        ),
        (
            "Superpowers execution/review/verification",
            "Keeps approved issue-body design and committed plan, then execution, TDD, review, verification and finishing.",
        ),
        (
            "Review remains open until integrated verification",
            "Submission moves active to review; completion waits for accepted integration and current cargo output.",
        ),
    ],
    "lifecycle-transitions": [
        (
            "Fail closed on multiple labels",
            "Identifies dual active/review as invalid before transitioning.",
        ),
        (
            "Preserve unrelated security label",
            "Changes only backplane labels and checks security after edits.",
        ),
        (
            "Repair evidence-supported review before rework",
            "Removes accidental active, verifies review, then separately swaps review to active.",
        ),
        (
            "Record active resume target",
            "Blocked comment explicitly records Resume target: backplane:active.",
        ),
        (
            "Revalidate active entry gates before resume",
            "Requires resolved blocker, current plan/design and open leaf before return.",
        ),
        (
            "Atomic transitions and post-mutation verification",
            "Each transition uses one remove/add edit and a verifying fetch.",
        ),
    ],
    "superpowers-installation": [
        (
            "Reject unsafe sibling without modifying it",
            "Rejects lookalike origin and missing skill; leaves owner work intact.",
        ),
        (
            "Authoritative source in unused destination",
            "Selects obra/superpowers and /agents/upstream-superpowers after absence check.",
        ),
        (
            "Stable default",
            "Selects latest published compatible stable release, with no implicit edge branch.",
        ),
        (
            "Provenance/capability/conformance/discovery gates",
            "Names all five conformance checks, full issue fields, four upstream skill paths and fresh discovery.",
        ),
        (
            "Explicit later update authority and unknown fails closed",
            "Later revision change requires approval and repeats preflight/discovery; failed candidate is not compatible.",
        ),
        (
            "Language and Project/IssueOps neutrality",
            "No consumer programming runtime or competing GitHub state system is required.",
        ),
    ],
}
conformance = []
for directory, upstream in (
    ("conformance-final", "2ce8aa15d05bd57213e6f746f953aafb7ded7a8b"),
    ("conformance-official-ready", "bb92a77741419a4ab5f06e711a283343f1ada0c3"),
):
    mode = {
        "directory": directory,
        "candidate": candidate,
        "host": "2.1.311",
        "upstream": upstream,
        "checks": [],
    }
    for name, scores in notes.items():
        receipt = json.loads(
            (work / directory / f"{name}-receipt.json").read_text(encoding="utf-8")
        )
        before = json.loads(
            (work / directory / f"before-{name}-snapshot.json").read_text(
                encoding="utf-8"
            )
        )
        after = json.loads(
            (work / directory / f"after-{name}-snapshot.json").read_text(
                encoding="utf-8"
            )
        )
        assert before["preservation"] == after["preservation"]
        assert before["plugins"] == after["plugins"]
        assert len(after["backplaneFiles"]) == 21
        response = receipt["response"]
        if name == "language-neutral-verification":
            assert "authoriz" in response.lower() and "submit" in response.lower()
        mode["checks"].append(
            dict(
                receipt,
                scores=[
                    {"expectation": title, "score": "PASS", "observed": note}
                    for title, note in scores
                ],
                before=before,
                after=after,
                stream=compact_stream(
                    (work / directory / f"{name}.jsonl").read_text(encoding="utf-8")
                ),
            )
        )
    mode["manual_scoring"] = (
        "Executor read all eight full final responses against exact source rubrics. Six lifecycle acceptance bullets are scored, including the separate resume-gate bullet omitted from the historical five-row summary table."
    )
    mode["supplemental_authorization"] = {
        "result": "PASS",
        "observed": "Both full language responses explicitly carry start AND submit authorization forward while explaining closure conveys no closure authority; project publication rules remain controlling.",
    }
    conformance.append(mode)
write_json(
    target / "2026-10-26-issue-11-final-conformance.json",
    {"result": "PASS", "modes": conformance, "expectations_per_mode": 23},
)

streams = []
for path in sorted(work.rglob("*.jsonl")):
    # Avoid host-managed sessions, caches, credentials and arbitrary fixture content.
    relative = path.relative_to(work)
    if any(
        part in {"setup-profile", "profile", "fixtures", "gh-shims"}
        for part in relative.parts
    ):
        continue
    if path.name.startswith("gh-") or path.stat().st_size > 4_000_000:
        continue
    try:
        record = compact_stream(path.read_text(encoding="utf-8"))
    except (ValueError, KeyError):
        continue
    streams.append({"scratch_path": relative.as_posix(), **record})
write_json(
    target / "2026-10-26-issue-11-session-observations.json",
    {
        "observations": streams,
        "scope": "Includes failed/pilot observations, not an assertion that every session passed. Scored final rows select applicable sessions explicitly.",
    },
)

sources = [
    "# Issue #11 owned verification helper sources",
    "",
    "Exact sources captured before final formatting. These are Backplane-owned helpers, not copied upstream files. Historical variants preserve their original filenames; current variants are not asserted identical to earlier executions.",
    "",
]
for path in sorted(work.glob("*.py")):
    sources += [
        f"## {path.name}",
        "",
        f"SHA-256: `{hashlib.sha256(path.read_bytes()).hexdigest()}`",
        "",
        "```python",
        path.read_text(encoding="utf-8").rstrip(),
        "```",
        "",
    ]
(target / "transcripts/2026-10-26-issue-11-verification-sources.md").write_text(
    "\n".join(sources), encoding="utf-8", newline="\n"
)


# Replace only embedded full SDK streams, retaining hashes and bounded observations.
def reduce_streams(value):
    if isinstance(value, dict):
        return {key: reduce_streams(item) for key, item in value.items()}
    if isinstance(value, list):
        return [reduce_streams(item) for item in value]
    if isinstance(value, str) and value.startswith('{"type":') and "\n" in value:
        try:
            return compact_stream(value)
        except (ValueError, KeyError):
            return value
    return value


for path in target.glob("2026-10-26-issue-11-*.json"):
    if "claude-integrated-acceptance" in path.name:
        continue
    value = json.loads(path.read_text(encoding="utf-8"))
    write_json(path, reduce_streams(value))
print(
    f"Archived two final conformance modes, {len(streams)} bounded session observations and exact owned helper sources"
)
```

## audit_inputs.py

SHA-256: `9511dcbcb25bca953d2878e2485d7247848c75e1d7d3562741c1d560495524ca`

```python
"""Read-only issue-11 input audit; no installation or Git mutation commands."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path.cwd().resolve(strict=True)
EXPECTED = Path("U:/repos/agents/superpowers-backplane").resolve(strict=True)
assert ROOT == EXPECTED
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"
CANDIDATE = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
DELIVERY = "7d7ecac36f8dc74ce1a0895ab934468332f92f53"
PROFILE = ROOT / ".sp-bp/work/issue-19/profile"
OUT = ROOT / "tests/scenarios/2026-10-26-issue-11-input-audit.json"
records = []


def redact_auth(value):
    if isinstance(value, dict):
        return {
            key: "[REDACTED]"
            if key in ("email", "orgId", "orgName")
            else redact_auth(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact_auth(item) for item in value]
    return value


def run(args, *, profile=False, cwd=ROOT):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    if profile:
        env["CLAUDE_CONFIG_DIR"] = str(PROFILE.resolve(strict=True))
    executable = shutil.which(args[0])
    assert executable, args[0]
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=90,
        check=False,
        shell=False,
    )
    stdout = result.stdout
    if args[:3] == ["claude", "auth", "status"] and stdout.strip().startswith("{"):
        stdout = json.dumps(redact_auth(json.loads(stdout)), indent=2) + "\n"
    records.append(
        {
            "argv": args,
            "cwd": str(cwd),
            "profile": str(PROFILE) if profile else None,
            "exit": result.returncode,
            "stdout": stdout,
            "stderr": result.stderr,
        }
    )
    return result


def checked(args, **kwargs):
    result = run(args, **kwargs)
    assert result.returncode == 0, (args, result.stderr)
    return result.stdout.strip()


assert checked(["git", "rev-parse", "--show-toplevel"]) == ROOT.as_posix()
assert sys.version_info[:3] == (3, 14, 9)
assert Path(sys.prefix).resolve() == ROOT / ".venv"
assert checked(["git", "check-ignore", ".sp-bp/work/issue-11/audit_inputs.py"])
audit = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "candidate": CANDIDATE,
    "runtime": sys.version,
    "prefix": sys.prefix,
    "root": str(ROOT),
    "branch": checked(["git", "branch", "--show-current"]),
    "head": checked(["git", "rev-parse", "HEAD"]),
    "origin": checked(["git", "remote", "get-url", "origin"]),
    "commands": records,
}
for name, args in {
    "claude_version": ["claude", "--version"],
    "gh_version": ["gh", "--version"],
    "gh_auth": ["gh", "auth", "status"],
    "gh_edit_help": ["gh", "issue", "edit", "--help"],
    "gh_close_help": ["gh", "issue", "close", "--help"],
    "claude_validate_help": ["claude", "plugin", "validate", "--help"],
    "claude_marketplace_help": ["claude", "plugin", "marketplace", "--help"],
    "claude_install_help": ["claude", "plugin", "install", "--help"],
    "claude_update_help": ["claude", "plugin", "update", "--help"],
    "claude_uninstall_help": ["claude", "plugin", "uninstall", "--help"],
    "remote_main": ["git", "ls-remote", "origin", "refs/heads/main"],
    "candidate_available": [
        "gh",
        "api",
        f"repos/tvproductions/superpowers-backplane/commits/{CANDIDATE}",
        "--jq",
        ".sha",
    ],
}.items():
    audit[name] = checked(args)
audit["issues"] = {}
for number in (1, 2, 6, 11, 17, 18, 19, 34):
    audit["issues"][str(number)] = json.loads(
        checked(
            [
                "gh",
                "issue",
                "view",
                str(number),
                "--repo",
                "tvproductions/superpowers-backplane",
                "--json",
                FIELDS,
            ]
        )
    )
audit["labels"] = json.loads(
    checked(
        [
            "gh",
            "label",
            "list",
            "--repo",
            "tvproductions/superpowers-backplane",
            "--limit",
            "100",
            "--json",
            "name,description",
        ]
    )
)
upstream = ROOT / ".agents/superpowers"
audit["upstream"] = {
    key: checked(["git", *args], cwd=upstream)
    for key, args in {
        "root": ["rev-parse", "--show-toplevel"],
        "origin": ["remote", "get-url", "origin"],
        "head": ["rev-parse", "HEAD"],
        "status": ["status", "--porcelain=v1"],
    }.items()
}
paths = [
    ".claude-plugin",
    "plugin.json",
    "skills",
    "docs/installing-claude-code.md",
    "docs/superpowers-backplane/governance.md",
]
audit["trees"] = {}
for ref in (CANDIDATE, DELIVERY, "d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a"):
    listing = checked(["git", "ls-tree", "-r", ref, "--", *paths])
    audit["trees"][ref] = {
        line.split("\t", 1)[1]: line.split()[2] for line in listing.splitlines()
    }
audit["changes_since_issue19"] = checked(
    ["git", "diff", "--name-only", DELIVERY, CANDIDATE]
).splitlines()
audit["profile_exists"] = PROFILE.is_dir()
audit["profile"] = {}
if PROFILE.is_dir():
    for name, args in {
        "auth": ["claude", "auth", "status", "--json"],
        "plugins": ["claude", "plugin", "list", "--json"],
        "marketplaces": ["claude", "plugin", "marketplace", "list", "--json"],
    }.items():
        result = run(args, profile=True)
        audit["profile"][name] = {
            "exit": result.returncode,
            "value": redact_auth(json.loads(result.stdout))
            if result.stdout.strip().startswith(("{", "["))
            else result.stdout,
        }
    audit["profile"]["config_hashes"] = {
        p.relative_to(PROFILE).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (
            PROFILE / "settings.json",
            PROFILE / "plugins/installed_plugins.json",
            PROFILE / "plugins/known_marketplaces.json",
        )
        if p.is_file()
    }
    audit["profile"]["installed_sources"] = []
    plugin_value = audit["profile"]["plugins"]["value"]
    if isinstance(plugin_value, list):
        for plugin in plugin_value:
            if plugin.get("id") != "superpowers-backplane@superpowers-backplane":
                continue
            installed = Path(plugin["installPath"]).resolve(strict=True)
            files = audit["trees"][CANDIDATE]
            checks = []
            for name, blob in files.items():
                if not (
                    name.startswith(("skills/", ".claude-plugin/"))
                    or name == "plugin.json"
                ):
                    continue
                target = installed / name
                content = target.read_bytes() if target.is_file() else b""
                actual = hashlib.sha1(
                    f"blob {len(content)}\0".encode("ascii") + content,
                    usedforsecurity=False,
                ).hexdigest()
                checks.append(
                    {
                        "path": name,
                        "expected_blob": blob,
                        "actual_blob": actual,
                        "matches": actual == blob,
                    }
                )
            audit["profile"]["installed_sources"].append(
                {"install_path": str(installed), "files": checks}
            )
audit["source_hashes"] = {}
for name in (
    "AGENTS.md",
    "SUPERPOWERS.md",
    ".python-version",
    "tests/scenarios/2026-09-20-claude-code-package-installation.md",
    "tests/scenarios/2026-09-20-claude-code-setup.md",
    "tests/scenarios/2026-10-25-issue-19-satisfaction.md",
    "tests/scenarios/2026-10-25-issue-19-integrated-verification.json",
    "tests/scenarios/2026-10-25-issue-19-python-3.14.json",
    "tests/scenarios/2026-10-25-issue-19-shared-catalog.json",
    "tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.json",
):
    path = ROOT / name
    audit["source_hashes"][name] = hashlib.sha256(path.read_bytes()).hexdigest()
OUT.write_text(
    json.dumps(audit, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "out": OUT.relative_to(ROOT).as_posix(),
            "commands": len(records),
            "runtime": sys.version.split()[0],
            "profile_exists": audit["profile_exists"],
            "profile_logged_in": audit["profile"]
            .get("auth", {})
            .get("value", {})
            .get("loggedIn"),
            "candidate": CANDIDATE,
            "source_files": len(audit["trees"][CANDIDATE]),
        },
        indent=2,
    )
)
```

## authorization_reference_probe.py

SHA-256: `5bce077bbc59146b6621756b57f99994bd213b3a2171eb5e8e27f95838d24304`

```python
"""Replay the exact language-neutral scenario with the current reference context."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
skill_root = root / "skills/managing-superpowers-backlog"
scenario = (root / "tests/scenarios/2026-08-16-native-issue-intake-green.md").read_text(
    encoding="utf-8"
)
prompt = re.findall(r"(?ms)^```text\n(.*?)^```", scenario)[1].rstrip()
context = (
    "This is a read-only current-reference application test. The complete Backplane skill context follows. "
    f"Its source directory is {skill_root}. Read its required public references from that directory; "
    "do not inspect project/product state or credentials. In particular, read the current github-issue-contract.md "
    "from this source directory, rather than another cached edition. Do not claim a Skill tool invocation; "
    "the main skill is provided as source context for this reference check.\n\n"
    + (skill_root / "SKILL.md").read_text(encoding="utf-8")
)
env = dict(os.environ, CLAUDE_CONFIG_DIR=str(root / ".sp-bp/work/issue-19/profile"))
executable = shutil.which("claude")
assert executable is not None
args = [
    executable,
    "-p",
    prompt,
    "--append-system-prompt",
    context,
    "--tools",
    "Read",
    "--allowedTools",
    "Read",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "12",
]
result = subprocess.run(
    args,
    cwd=work / "native-neutral",
    env=env,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
    timeout=180,
    shell=False,
    check=False,
)
(work / "authorization-reference.jsonl").write_text(
    result.stdout, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
host = next(event for event in reversed(events) if event.get("type") == "result")
assert (
    result.returncode == 0
    and host.get("subtype") == "success"
    and not host.get("is_error")
)
response = host["result"]
assert "Only the start transition is covered" not in response
reads = [
    block
    for event in events
    if isinstance(event.get("message"), dict)
    for block in event["message"].get("content", [])
    if isinstance(block, dict)
    and block.get("type") == "tool_use"
    and block.get("name") == "Read"
]
contract = skill_root / "references/github-issue-contract.md"
assert any(
    Path(call["input"]["file_path"]).resolve() == contract.resolve() for call in reads
)
(work / "authorization-reference-response.md").write_text(
    response + "\n", encoding="utf-8", newline="\n"
)
(root / "tests/scenarios/2026-10-26-issue-11-authorization-reference.json").write_text(
    json.dumps(
        {
            "result": "UNSCORED; inspect scope interpretation",
            "prompt": prompt,
            "scope": "Current full reference context, not installed-package acceptance",
            "contract_sha256": hashlib.sha256(contract.read_bytes()).hexdigest(),
            "session_id": host.get("session_id"),
            "reads": reads,
            "response": response,
            "red_assertion": (work / "authorization-scope-red.txt").read_text(
                encoding="utf-8"
            ),
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps({"session": host.get("session_id"), "response": response}, indent=2))
```

## check_authorization_scope.py

SHA-256: `1c84854f53a16c1dfd571c903aa0100f75f320501816d69a3b8f9e01e9107610`

```python
"""Reject the observed denial of already-authorized conditional submission."""

from pathlib import Path
import sys

response = Path(sys.argv[1]).read_text(encoding="utf-8")
assert "Only the start transition is covered" not in response, (
    "The prompt explicitly authorized both start and submission; submission must not require a new approval solely because it occurs later"
)
print("PASS: response does not repeat the observed extra submission-approval gate")
```

## check_relationship_counts.py

SHA-256: `7eff35e286beeb7c247d89c53bde36005ec392c8f1eb0569e7c60115748813a2`

```python
"""Reject a native issue summary that counts connection keys as issues."""

import argparse
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument("receipt")
args = parser.parse_args()
data = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
issue = data["before"]["issue11"]
nodes = (
    issue["subIssues"]["nodes"]
    if isinstance(issue["subIssues"], dict)
    else issue["subIssues"]
)
response = data["host_result"]["result"]
claims = [int(match) for match in re.findall(r"(\d+) sub-issues", response)]
if re.search(r"\bno sub-issues\b", response, re.I):
    claims.append(0)
assert claims, "The selected baseline should contain an explicit count claim"
assert all(value == len(nodes) for value in claims), (
    f"Native sub-issue count must be {len(nodes)}, not object-key count {claims}"
)
print(f"PASS: every reported native sub-issue count equals {len(nodes)}")
```

## complete_matrix.py

SHA-256: `ec0010d34d392b9dedcc20a3eb315772c58181b6e83f0d89619cab7b10ca16d3`

```python
"""Publish the locally verified matrix while preserving original run identities."""

import hashlib
import json
from pathlib import Path

from lifecycle_helpers import write_json

root = Path.cwd().resolve(strict=True)
scenarios = root / "tests/scenarios"
work = root / ".sp-bp/work/issue-11"
prefix = "2026-10-26-issue-11-"
base = scenarios / (prefix + "claude-integrated-acceptance")
data = json.loads(base.with_suffix(".json").read_text(encoding="utf-8"))
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"
verification = prefix + "candidate-verification.json"
conformance = prefix + "final-conformance.json"
mapping = {
    "prerequisites": (
        [verification],
        "Fresh complete intake confirms #17/#18/#19 CLOSED/COMPLETED; integrated #19 delivery is an ancestor of E.",
    ),
    "clean-install": (
        [prefix + "native-setup.json", prefix + "final-candidate.json"],
        "Exact clean-install guide bootstrap C and final exact-E native installation passed; 21 installed package files match E.",
    ),
    "native-setup": (
        [
            prefix + "native-setup-workflow-2.json",
            prefix + "final-native-discovery.json",
            conformance,
        ],
        "Corrected owned-capture native setup preflight passed; E fresh native discovery and full conformance passed.",
    ),
    "sibling-setup": (
        [
            prefix + "sibling-setup-workflow-2.json",
            prefix + "final-sibling-discovery.json",
            conformance,
        ],
        "Backplane-only profile adopted separate sibling without persistent upstream install; E fresh sibling invocation loaded all three actual skill roots.",
    ),
    "absent-setup": (
        [
            prefix + "absent-setup.json",
            prefix + "final-official-discovery.json",
            conformance,
        ],
        "Actual absent-upstream acquisition installed official stable 7.0.0 separately; fresh E official discovery and 23 expectations passed at that source.",
    ),
    "lookalike-source": (
        [prefix + "lookalike-source.json"],
        "Actual installed setup rejected the lookalike origin and preserved fixture/protected state.",
    ),
    "versionless-package": (
        [
            prefix + "versionless-package-current.json",
            prefix + "native-failure-controls.json",
        ],
        "Actual native versionless package produced unknown compatibility and setup stopped without inventing provenance.",
    ),
    "duplicate-backplane": (
        [
            prefix + "duplicate-backplane-current.json",
            prefix + "native-failure-controls.json",
        ],
        "Two enabled native Backplane IDs were detected and setup stopped; exact fixture removal preserved other installed plugins.",
    ),
    "missing-upstream-skill": (
        [prefix + "missing-upstream-skill.json"],
        "Actual incomplete authoritative fixture was rejected for missing required writing-plans.",
    ),
    "dirty-adoption": (
        [prefix + "dirty-adoption-current.json"],
        "Authoritative dirty sibling accepted in place without update; fixture and actual upstream preserved.",
    ),
    "dirty-update-refusal": (
        [prefix + "dirty-update-refusal-current.json"],
        "Dirty-state update refused before fetch/checkout with concrete recovery and no lost files.",
    ),
    "occupied-destination": (
        [prefix + "occupied-destination.json"],
        "Existing destination rejected before checkout creation; sentinel preserved.",
    ),
    "gh-auth-failure": (
        [prefix + "gh-auth-failure.json", prefix + "gh-failure-controls.json"],
        "Injected authentication failure stopped setup; no credential copying or fallback.",
    ),
    "gh-intake-failure": (
        [prefix + "gh-intake-failure.json", prefix + "gh-failure-controls.json"],
        "Required issueType failure stopped setup rather than silently reducing intake.",
    ),
    "gh-label-failure": (
        [prefix + "gh-label-failure-current.json", prefix + "gh-failure-controls.json"],
        "Isolated missing label mutation capability stopped setup with corrected read-only adapter.",
    ),
    "gh-closure-failure": (
        [
            prefix + "gh-closure-failure-current.json",
            prefix + "relationship-reference.json",
        ],
        "Isolated missing closure-reason capability stopped setup; observed zero native subissues with fixed connection parsing.",
    ),
    "unauthenticated-host": (
        [prefix + "setup-auth.json"],
        "Before operator login, the separately scoped host returned exit 1/loggedIn false/authMethod none; no installation, credential copy or normal-profile fallback was performed.",
    ),
    "skill-structure": (
        [verification],
        "Strict package validation in both profiles, exact metadata and existing relative reference links passed.",
    ),
    "status": (
        [prefix + "status-selection.json"],
        "Fresh E installed status read complete actual #11 graph with zero protected-state change.",
    ),
    "selection": (
        [prefix + "status-selection.json"],
        "Fresh E selection confirmed operator-selected already-active #11; no invented priority or lifecycle mutation.",
    ),
    "design": (
        [prefix + "input-audit.json", prefix + "execution-start.json"],
        "Actual operator-selected #11 entered designing with unchanged scope/graph; approved local plan later linked honestly.",
    ),
    "ready": (
        [prefix + "execution-start.json"],
        "Actual #11 readiness followed approved plan and closed blockers, with full native before/after reconciliation.",
    ),
    "active": (
        [prefix + "execution-start.json", prefix + "status-selection.json"],
        "Actual approved #11 ready-to-active transition is preserved; fresh E observation confirms active, one lifecycle label and zero state mutation.",
    ),
    "fresh-discovery": (
        [
            prefix + f"final-{mode}-discovery.json"
            for mode in ("native", "sibling", "official")
        ],
        "Three fresh sessions invoked upstream and both Backplane skills from verified independent roots.",
    ),
    "preservation": (
        [
            prefix + "shared-catalog.json",
            prefix + "lifecycle.json",
            prefix + "status-selection.json",
            conformance,
        ],
        "Immediate valid operation snapshots preserve normal settings/registry/catalog hashes, unrelated plugins, user sentinel, real upstream files/revision, project refs and full issue state; shared-catalog installed sentinel also preserved.",
    ),
}
for row in (
    "repeat-install",
    "pinned-update",
    "rollback",
    "uninstall",
    "restoration",
    "failed-preflight",
):
    mapping[row] = (
        [prefix + "lifecycle.json", prefix + "shared-catalog.json"],
        "Nine exact guide blocks replayed C->test-only F->C with source/version byte proofs, unavailable-source refusal and fresh discovery. E payload installation and shared-catalog uninstall/restoration passed; unchanged guide/manifests retain mechanism applicability.",
    )
for row in (
    "native-issue-intake",
    "language-neutral-verification",
    "lifecycle-transitions",
    "superpowers-installation",
):
    mapping[row] = (
        [conformance],
        "Fresh E installed exact-prompt responses manually scored against all source expectations under development 7.0.1 and official 7.0.0; immediate preservation comparisons passed.",
    )
historical = [
    "2026-10-25-issue-19-live-fixture.json",
    "2026-10-25-issue-19-fixture-closeout.json",
    "2026-10-25-issue-19-review-submission.json",
]
for row in ("blocked-resume", "review", "rework", "verified-completion"):
    mapping[row] = (
        historical + [conformance],
        "Retained actual authorized #34 native transition/integrated-completion observations with original identities; current E fresh lifecycle/intake/closure/authorization responses verify affected behavior. No new #34 mutation or current #11 completion is claimed.",
    )
assert set(mapping) == {r["id"] for r in data["rows"]}
common_inputs = {
    "host": "2.1.311 (Claude Code)",
    "backplane": candidate,
    "upstream": {
        "development": "obra/superpowers v7.0.1 / 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b",
        "official": "anthropics/claude-plugins-official catalogue 1da406f428c285c701a1033a3aef368a9ab865dc, Superpowers 7.0.0 / bb92a77741419a4ab5f06e711a283343f1ada0c3",
    },
    "gh_capability": {
        "version": "2.103.2",
        "auth": "PASS",
        "complete_intake": "PASS",
        "label_help": "PASS",
        "closure_help": "PASS",
        "evidence": verification,
    },
    "installed_skills": {
        "upstream": "superpowers:using-superpowers from independently verified upstream source",
        "backlog": "superpowers-backplane:managing-superpowers-backlog from exact E package",
        "handoffs": "superpowers-backplane:managing-superpowers-handoffs from exact E package",
        "source_blob_files": 21,
        "fresh_loads": "PASS in native, sibling and official modes",
    },
}
for row in data["rows"]:
    paths, claim = mapping[row["id"]]
    paths = list(dict.fromkeys([*paths, verification]))
    row["candidate_inputs"] = common_inputs
    row["result"] = "PASS"
    row["disposition"] = (
        "retained"
        if row["id"]
        in (
            "blocked-resume",
            "review",
            "rework",
            "verified-completion",
            "pinned-update",
            "rollback",
            "repeat-install",
            "failed-preflight",
        )
        else "rerun"
    )
    row["observed_claim"] = claim
    row["reason"] = claim
    row["verified_input_comparison"] = (
        "Candidate verification receipt records exact unchanged component blobs, changed graph/authorization paragraphs, two final current conformance runs, final installed payload checks and explicit limits on original C/D/#34 observations. Candidate inputs describe the evaluated E environment; original identities remain in each linked actual-run receipt. Retained does not mean freshly replayed."
    )
    row["evidence"] = [
        {
            "path": "tests/scenarios/" + path,
            "sha256": hashlib.sha256((scenarios / path).read_bytes()).hexdigest(),
        }
        for path in paths
    ]
data.update(
    candidate=candidate,
    phase="local-candidate-verification",
    review="PENDING independent whole-change review",
    integrated_acceptance="PENDING authorized publication/integration and exact-target verification",
    publication="Not performed",
    acceptance_scope="39 local candidate checks; final #11 acceptance remains pending integration",
)
write_json(base.with_suffix(".json"), data)
historical_report = scenarios / (prefix + "preparation-history.md")
if not historical_report.exists():
    historical_report.write_text(
        base.with_suffix(".md").read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )
lines = [
    "# Issue #11 Claude candidate verification",
    "",
    f"Product candidate: `{candidate}` on `feat/issue-11-claude-acceptance`. Local verification: **39/39 PASS**. Independent review and final integrated acceptance remain pending. No push, PR, merge, closure or release has occurred.",
    "",
    "The approved implementation plan is unchanged. This report supersedes the dated preparation state preserved in [preparation history]("
    + historical_report.name
    + "). The generic testing-boundary correction removed the unnecessary per-fixture and prior-publication gates; local verification was already authorized.",
    "",
    "## Inputs and evidence",
    "",
    "Claude Code 2.1.311 and gh 2.103.2 on Windows; uv-managed Python 3.14.9. Existing development Superpowers remains clean at 7.0.1 (`2ce8aa1`). Absent-upstream acquisition used Claude's documented official marketplace and actually resolved Superpowers 7.0.0 (`bb92a77`), independently tested. Catalogue advanced from the pre-probe revision to `1da406f`; it was not forced to a different channel. Candidate E is locally installed and unpublished.",
    "",
    "Each mode passed all 23 behavioral expectations plus the structural check. Full prompts, unedited final responses, actual calls, immediate before/after source and preservation observations are in [final conformance]("
    + conformance
    + "). Three fresh discovery receipts identify separate roots. Native graph and authority defects found during these tests were corrected with recorded RED/GREEN evidence; package, guide and other skill behavior bytes remain unchanged.",
    "",
    "## Matrix",
    "",
    "| Check | Result | Owning issue | Observed scope |",
    "|---|---|---|---|",
]
for row in data["rows"]:
    lines.append(f"| {row['id']} | PASS | #{row['owner']} | {row['observed_claim']} |")
lines += [
    "",
    "## Applicability and exclusions",
    "",
    "The [candidate verification receipt]("
    + verification
    + ") records exact component blob comparisons. The nine-block lifecycle replay used C (`66c4c4f`) and excluded test-only F (`5e01704`), then rolled back to C. Its guide, manifests and installation guards equal E. E's changed reference payload was separately installed and checked byte-for-byte, freshly discovered, behaviorally tested, and removed/restored while an unrelated installed plugin shared its catalogue. This is not a claim of a hosted E update before publication.",
    "",
    "Actual #34 design/readiness/execution/blocked/rework/review/integrated closure observations remain historical. E fresh conformance covers the affected interpretation and authorization behavior, and fresh actual #11 status/selection preserves its state. No completed issue was reopened as a fixture. Predecessor gh exact version is unknown in the #34 receipt; current required capabilities are directly verified rather than assumed version-equal.",
    "",
    "Preserved excluded observations: the first native probe wrote unowned `/tmp/i11.json` and `/tmp/i11.err` despite instructions and exposed an ephemeral runtime messaging token through environment enumeration. Its result is UNKNOWN and it supports no user-file-preservation PASS. The corrected owned-capture probe is used. The first sibling parser stopped on a system string; its protected-state baseline is unavailable, so it supports no full comparison. Early dirty tests omitted the fixture path and are ungraded. The first capability adapter over-restricted a legitimate auth flag; corrected isolated repeats are used. The original closure response counted connection keys as two children; the fixed native repeat reads zero. The D language response unnecessarily requested submission approval; final E explicitly recognizes both authorized stages.",
    "",
    "A broad early conformance interval observed a normal-profile known-marketplaces hash change of unknown cause. No rollback or causal attribution was attempted. That interval supports no preservation PASS. Later final runs capture immediate per-operation baselines and compare all protected data without ignoring the file. The final official run's first attempt stopped before model execution because its sentinel had not been prepared; the subsequent correctly prepared run is separately identified.",
    "",
    "Raw SDK streams remain ignored. [Bounded session observations]("
    + prefix
    + "session-observations.json) retain exact final responses and actual calls, with tool-result hashes in place of upstream document bodies or environment contents. This avoids vendoring shipped upstream skills. Authentication fields and ephemeral assignments are redacted in publishable evidence. All fixtures and profiles are retained. Ruff's first broad scratch-directory check inadvertently included third-party copies; it made no edits. The corrected checks enumerate only owned helper files. A missing executable type guard and five formatting issues were corrected, then owned-file Ruff and ty passed.",
    "",
    "## Next step",
    "",
    "Finish evidence checks and one fresh whole-change review. Then present the concrete branch for publication/integration authorization under AGENTS. Final #11 acceptance requires actual integrated-target verification and a published satisfaction assessment before separately authorized closure. #1, #6 and other host acceptance remain independent.",
    "",
]
base.with_suffix(".md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(
    "39/39 local candidate rows reconciled; integrated acceptance and independent review pending"
)
```

## conformance.py

SHA-256: `b55d2459215b553b13f22717643c9237c44fe9fff7cfb2f61e89502ccff4a2ff`

```python
"""Run the exact approved prompts against restored installed B."""

import json
from pathlib import Path
import re

from lifecycle_helpers import (
    BASELINE,
    Harness,
    compare_preservation,
    read_json,
    run_cli,
    write_json,
)


def main() -> None:
    root = Path.cwd().resolve(strict=True)
    output = root / ".sp-bp/work/issue-11/lifecycle-run"
    harness = Harness(
        root,
        profile=root / ".sp-bp/work/issue-19/profile",
        catalog=root / ".sp-bp/work/issue-11/lifecycle-catalog",
        output=output,
    )
    baseline_path = harness.work / "comparison-baseline.json"
    baseline = read_json(baseline_path)
    # No project ref mutation is expected between lifecycle and these checks.
    harness.snapshot("conformance-start", BASELINE, "0.1.0")
    cases = [
        ("native-issue-intake", "2026-08-16-native-issue-intake-green.md", 0),
        ("language-neutral-verification", "2026-08-16-native-issue-intake-green.md", 1),
        ("lifecycle-transitions", "2026-08-16-lifecycle-transition-refactor.md", 0),
        (
            "superpowers-installation",
            "2026-08-16-superpowers-installation-refactor.md",
            0,
        ),
    ]
    for name, source, index in cases:
        text = (root / "tests" / "scenarios" / source).read_text(encoding="utf-8")
        prompts = re.findall(r"(?ms)^```text\r?\n(.*?)^```", text)
        prompt = prompts[index].rstrip()
        (harness.work / f"{name}-prompt.txt").write_text(
            prompt + "\n", encoding="utf-8", newline="\n"
        )
        print(
            f"Running approved exact prompt: {name}; CLAUDE_CONFIG_DIR={harness.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--append-system-prompt",
                "This is an explicitly authorized read-only installed-public-package conformance test. "
                "Load installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog through Skill. "
                "Read required public skill references only from those installed packages. "
                "Do not read credentials, profile settings, unrelated files or current working repository state. "
                "Hypothetical commands are response text, never actual actions.",
                "--tools",
                "Skill,Read",
                "--allowedTools",
                "Skill,Read",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "18",
            ],
            cwd=harness.work / "neutral",
            overrides=harness.environment,
        )
        raw = harness.work / f"{name}.jsonl"
        raw.write_text(output, encoding="utf-8", newline="\n")
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError(f"Incomplete conformance session: {name}")
        calls = [
            block
            for event in events
            if isinstance(event.get("message"), dict)
            for block in event.get("message", {}).get("content", [])
            if isinstance(block, dict) and block.get("type") == "tool_use"
        ]
        skills = [call["input"]["skill"] for call in calls if call["name"] == "Skill"]
        if "superpowers-backplane:managing-superpowers-backlog" not in skills:
            raise ValueError(f"No actual installed backlog skill invocation: {name}")
        (harness.work / f"{name}-response.md").write_text(
            result["result"] + "\n", encoding="utf-8", newline="\n"
        )
        write_json(
            harness.work / f"{name}-receipt.json",
            {
                "check": name,
                "session": result["session_id"],
                "tools": calls,
                "model_usage": result.get("modelUsage", {}),
                "source": source,
                "prompt": prompt,
                "response": result["result"],
                "result": result["subtype"],
            },
        )
        after = harness.snapshot(f"after-{name}", BASELINE, "0.1.0")
        compare_preservation(baseline["preservation"], after["preservation"])
        print(
            f"{name}: observed successful response; scoring pending; session={result['session_id']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
```

## conformance_immediate.py

SHA-256: `b1eea04947a372283ddc462e6181eb1e6a2acb11e4d94ee4cb8a845f4e898154`

```python
"""Run the exact approved prompts against restored installed B."""

import argparse
import json
from pathlib import Path
import re

from lifecycle_helpers import (
    BASELINE,
    Harness,
    compare_preservation,
    run_cli,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", default=BASELINE)
    parser.add_argument("--output-name", default="conformance-immediate")
    parser.add_argument("--profile", default=".sp-bp/work/issue-19/profile")
    parser.add_argument("--upstream-id", default="superpowers@superpowers-dev")
    options = parser.parse_args()
    assert re.fullmatch(r"[0-9a-f]{40}", options.candidate)
    assert re.fullmatch(r"[a-z0-9-]+", options.output_name)
    selected = options.candidate
    root = Path.cwd().resolve(strict=True)
    output = root / ".sp-bp/work/issue-11" / options.output_name
    assert not output.exists(), "Preserve prior conformance evidence"
    output.mkdir()
    (output / "neutral").mkdir()
    harness = Harness(
        root,
        profile=root / options.profile,
        catalog=root / ".sp-bp/work/issue-11/lifecycle-catalog",
        output=output,
        upstream_id=options.upstream_id,
    )
    harness.snapshot("conformance-start", selected, "0.1.0", capture_only=True)
    cases = [
        ("native-issue-intake", "2026-08-16-native-issue-intake-green.md", 0),
        ("language-neutral-verification", "2026-08-16-native-issue-intake-green.md", 1),
        ("lifecycle-transitions", "2026-08-16-lifecycle-transition-refactor.md", 0),
        (
            "superpowers-installation",
            "2026-08-16-superpowers-installation-refactor.md",
            0,
        ),
    ]
    for name, source, index in cases:
        baseline = harness.snapshot(
            f"before-{name}", selected, "0.1.0", capture_only=True
        )
        text = (root / "tests" / "scenarios" / source).read_text(encoding="utf-8")
        prompts = re.findall(r"(?ms)^```text\r?\n(.*?)^```", text)
        prompt = prompts[index].rstrip()
        (harness.work / f"{name}-prompt.txt").write_text(
            prompt + "\n", encoding="utf-8", newline="\n"
        )
        print(
            f"Running approved exact prompt: {name}; CLAUDE_CONFIG_DIR={harness.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--append-system-prompt",
                "This is an explicitly authorized read-only installed-public-package conformance test. "
                "Load installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog through Skill. "
                "Read required public skill references only from those installed packages. "
                "Do not read credentials, profile settings, unrelated files or current working repository state. "
                "Hypothetical commands are response text, never actual actions.",
                "--tools",
                "Skill,Read",
                "--allowedTools",
                "Skill,Read",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "18",
            ],
            cwd=harness.work / "neutral",
            overrides=harness.environment,
        )
        raw = harness.work / f"{name}.jsonl"
        raw.write_text(output, encoding="utf-8", newline="\n")
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError(f"Incomplete conformance session: {name}")
        calls = [
            block
            for event in events
            if isinstance(event.get("message"), dict)
            for block in event.get("message", {}).get("content", [])
            if isinstance(block, dict) and block.get("type") == "tool_use"
        ]
        skills = [call["input"]["skill"] for call in calls if call["name"] == "Skill"]
        if "superpowers-backplane:managing-superpowers-backlog" not in skills:
            raise ValueError(f"No actual installed backlog skill invocation: {name}")
        (harness.work / f"{name}-response.md").write_text(
            result["result"] + "\n", encoding="utf-8", newline="\n"
        )
        write_json(
            harness.work / f"{name}-receipt.json",
            {
                "check": name,
                "session": result["session_id"],
                "tools": calls,
                "model_usage": result.get("modelUsage", {}),
                "source": source,
                "candidate": selected,
                "prompt": prompt,
                "response": result["result"],
                "result": result["subtype"],
            },
        )
        after = harness.snapshot(
            f"after-{name}", selected, "0.1.0", compare_to=baseline
        )
        compare_preservation(baseline["preservation"], after["preservation"])
        print(
            f"{name}: observed successful response; scoring pending; session={result['session_id']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
```

## conformance_immediate_C.py

SHA-256: `3bd53a7d97df317924e9a40bdde9d4a82689e906a0143c9e485b358b683ed928`

```python
"""Run the exact approved prompts against restored installed B."""

import json
from pathlib import Path
import re

from lifecycle_helpers import (
    BASELINE,
    Harness,
    compare_preservation,
    run_cli,
    write_json,
)


def main() -> None:
    root = Path.cwd().resolve(strict=True)
    output = root / ".sp-bp/work/issue-11/conformance-immediate"
    assert not output.exists(), "Preserve prior conformance evidence"
    output.mkdir()
    (output / "neutral").mkdir()
    harness = Harness(
        root,
        profile=root / ".sp-bp/work/issue-19/profile",
        catalog=root / ".sp-bp/work/issue-11/lifecycle-catalog",
        output=output,
    )
    harness.snapshot("conformance-start", BASELINE, "0.1.0", capture_only=True)
    cases = [
        ("native-issue-intake", "2026-08-16-native-issue-intake-green.md", 0),
        ("language-neutral-verification", "2026-08-16-native-issue-intake-green.md", 1),
        ("lifecycle-transitions", "2026-08-16-lifecycle-transition-refactor.md", 0),
        (
            "superpowers-installation",
            "2026-08-16-superpowers-installation-refactor.md",
            0,
        ),
    ]
    for name, source, index in cases:
        baseline = harness.snapshot(
            f"before-{name}", BASELINE, "0.1.0", capture_only=True
        )
        text = (root / "tests" / "scenarios" / source).read_text(encoding="utf-8")
        prompts = re.findall(r"(?ms)^```text\r?\n(.*?)^```", text)
        prompt = prompts[index].rstrip()
        (harness.work / f"{name}-prompt.txt").write_text(
            prompt + "\n", encoding="utf-8", newline="\n"
        )
        print(
            f"Running approved exact prompt: {name}; CLAUDE_CONFIG_DIR={harness.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--append-system-prompt",
                "This is an explicitly authorized read-only installed-public-package conformance test. "
                "Load installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog through Skill. "
                "Read required public skill references only from those installed packages. "
                "Do not read credentials, profile settings, unrelated files or current working repository state. "
                "Hypothetical commands are response text, never actual actions.",
                "--tools",
                "Skill,Read",
                "--allowedTools",
                "Skill,Read",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "18",
            ],
            cwd=harness.work / "neutral",
            overrides=harness.environment,
        )
        raw = harness.work / f"{name}.jsonl"
        raw.write_text(output, encoding="utf-8", newline="\n")
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError(f"Incomplete conformance session: {name}")
        calls = [
            block
            for event in events
            if isinstance(event.get("message"), dict)
            for block in event.get("message", {}).get("content", [])
            if isinstance(block, dict) and block.get("type") == "tool_use"
        ]
        skills = [call["input"]["skill"] for call in calls if call["name"] == "Skill"]
        if "superpowers-backplane:managing-superpowers-backlog" not in skills:
            raise ValueError(f"No actual installed backlog skill invocation: {name}")
        (harness.work / f"{name}-response.md").write_text(
            result["result"] + "\n", encoding="utf-8", newline="\n"
        )
        write_json(
            harness.work / f"{name}-receipt.json",
            {
                "check": name,
                "session": result["session_id"],
                "tools": calls,
                "model_usage": result.get("modelUsage", {}),
                "source": source,
                "prompt": prompt,
                "response": result["result"],
                "result": result["subtype"],
            },
        )
        after = harness.snapshot(
            f"after-{name}", BASELINE, "0.1.0", compare_to=baseline
        )
        compare_preservation(baseline["preservation"], after["preservation"])
        print(
            f"{name}: observed successful response; scoring pending; session={result['session_id']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
```

## create_matrix.py

SHA-256: `0c9a9c2cde7959dd1300e5a4b361bee490b0fa8ff030031c9d2e54ba13981b88`

```python
"""Capture the initial issue-11 matrix; unknown observations stay unknown."""

import hashlib
import json
from pathlib import Path

from verify_evidence import EXPECTED

root = Path.cwd().resolve(strict=True)
base = root / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance"
audit_path = "tests/scenarios/2026-10-26-issue-11-input-audit.json"
audit = json.loads((root / audit_path).read_text(encoding="utf-8"))
setup = {
    "clean-install",
    "native-setup",
    "sibling-setup",
    "absent-setup",
    "lookalike-source",
    "versionless-package",
    "duplicate-backplane",
    "missing-upstream-skill",
    "dirty-adoption",
    "dirty-update-refusal",
    "occupied-destination",
    "gh-auth-failure",
    "gh-intake-failure",
    "gh-label-failure",
    "gh-closure-failure",
    "unauthenticated-host",
}
native = {
    "status",
    "selection",
    "design",
    "ready",
    "active",
    "blocked-resume",
    "review",
    "rework",
    "verified-completion",
}
skill_names = [
    "superpowers:using-superpowers",
    "superpowers-backplane:managing-superpowers-backlog",
    "superpowers-backplane:managing-superpowers-handoffs",
]
current = {
    "host": audit["claude_version"],
    "backplane": audit["candidate"],
    "upstream": audit["upstream"],
    "gh_capability": {
        "version": audit["gh_version"],
        "evidence": audit_path,
        "auth": "PASS",
        "complete_intake": "PASS",
        "label_help": "PASS"
        if "--add-label" in audit["gh_edit_help"]
        and "--remove-label" in audit["gh_edit_help"]
        else "FAIL",
        "closure_help": "PASS" if "--reason" in audit["gh_close_help"] else "FAIL",
    },
    "installed_skills": {
        "required_names": skill_names,
        "observed_source_files": 20,
        "source_blob_comparison": "PASS",
        "fresh_tool_loads": "NOT RUN",
    },
}
assert (
    current["gh_capability"]["label_help"]
    == current["gh_capability"]["closure_help"]
    == "PASS"
)
for number in (17, 18, 19):
    issue = audit["issues"][str(number)]
    assert issue["state"] == "CLOSED" and issue["stateReason"] == "COMPLETED"
assert audit["candidate_available"] == audit["candidate"]
assert audit["profile"]["auth"]["value"]["loggedIn"] is True
assert len(audit["profile"]["installed_sources"]) == 1
assert len(audit["profile"]["installed_sources"][0]["files"]) == 20
assert all(
    f["matches"]
    for source in audit["profile"]["installed_sources"]
    for f in source["files"]
)


def pointer(path):
    return {
        "path": path,
        "sha256": hashlib.sha256((root / path).read_bytes()).hexdigest(),
    }


rows = []
for name in sorted(EXPECTED):
    is_setup = name in setup
    historical_path = (
        "tests/scenarios/2026-09-20-claude-code-package-installation.md"
        if name == "clean-install"
        else "tests/scenarios/2026-09-20-claude-code-setup.md"
        if is_setup
        else "tests/scenarios/2026-10-25-issue-19-fixture-closeout.json"
        if name in native
        else "tests/scenarios/2026-10-25-issue-19-satisfaction.md"
    )
    original = {
        "host": "2.1.241" if is_setup else "2.1.302",
        "backplane": "d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a"
        if is_setup
        else "7d7ecac36f8dc74ce1a0895ab934468332f92f53",
        "upstream": "Superpowers 6.4.1 / official-channel 6.3.0, case-specific"
        if is_setup
        else "Superpowers 7.0.1 / 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b",
        "gh_capability": "Historical successful capabilities; full input comparison pending",
        "installed_skills": {
            "required_names": skill_names,
            "evidence": historical_path,
        },
    }
    changed = (
        ["Claude host", "upstream", "Backplane skill and guide bytes"]
        if is_setup
        else [
            "referenced governance document; assess effect before retaining behavior evidence"
        ]
    )
    row = {
        "id": name,
        "requirement": name.replace("-", " "),
        "owner": 17
        if name == "clean-install"
        else 18
        if is_setup
        else 11
        if name == "prerequisites"
        else 19,
        "mandatory": True,
        "original_inputs": original,
        "candidate_inputs": current,
        "changed_inputs": changed,
        "disposition": "rerun",
        "result": "UNKNOWN",
        "reason": "Changed setup inputs require fresh observed outcome"
        if is_setup
        else "Exact source audit alone does not establish the required live outcome or applicability",
        "evidence": [pointer(audit_path), pointer(historical_path)],
    }
    if name == "prerequisites":
        row.update(
            result="PASS",
            disposition="retained",
            original_inputs=current,
            changed_inputs=[],
            reason="Fresh native #17/#18/#19 states, candidate remote availability and inspected tracked evidence establish prerequisites only",
            observed_claim="All three prerequisite issues are CLOSED/COMPLETED; evidence paths and immutable source are reachable",
            verified_input_comparison="Fresh complete native intake in input audit; historical rows remain separately UNKNOWN",
        )
    rows.append(row)
data = {
    "format": "superpowers-backplane-issue11-acceptance/v1",
    "candidate": audit["candidate"],
    "issue": audit["issues"]["11"]["url"],
    "semantic_revision": "2026-09-20T01:31:32Z",
    "observed_revision": audit["issues"]["11"]["updatedAt"],
    "phase": "initial",
    "rows": rows,
    "rulings": [
        "Approved feature branch in exact standalone root replaces worktree creation; no reserved helper invoked",
        "Read-only preparation precedes ready/active until approved-plan publication and fixture boundary are resolved",
        "Evidence work uses direct validation/negative controls; any demonstrated product behavior correction requires TDD",
    ],
}
base.with_suffix(".json").write_text(
    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
lines = [
    "# Issue #11 Claude integrated acceptance — initial input ledger",
    "",
    f"Candidate: `{audit['candidate']}`. Branch: `{audit['branch']}`.",
    "",
    "This is a prepared matrix, not final acceptance. Every historical live result retains its original scope.",
    "",
    "| Mandatory row | Result | Owner | Current disposition |",
    "| --- | --- | --- | --- |",
]
lines += [
    f"| {r['id']} | {r['result']} | #{r['owner']} | {r['reason']} |" for r in rows
]
lines += [
    "",
    "## Fresh observations",
    "",
    "- 37 read-only command observations captured in `2026-10-26-issue-11-input-audit.json`.",
    "- Python 3.14.9 in the root .venv verified through uv; the earlier cache-lock denial is resolved by authorized execution.",
    "- Existing issue-19 disposable profile is authenticated. Auth account/organization fields are redacted; no credentials were read or copied.",
    "- All 20 installed canonical skill/reference and package-manifest files match candidate C; this is source identity, not fresh Skill invocation.",
    "- Candidate package/skills/guide match #19 delivery. Loaded governance document changed; its behavioral effect is not yet reconciled.",
    "- #17/#18 host/upstream/skill/guide inputs changed, requiring fresh setup and rejection evidence.",
    "- #11 remains OPEN/designing. Approved-plan publication and ready/active transitions have not occurred.",
    "",
    "## Execution boundaries",
    "",
    "The approved guide creates another Git root during clean-install bootstrap, and several failures require independent Git fixture identities. AGENTS requires every mutated Git root to equal the standalone root, with an exception only for #31. The #11-specific fixture exception remains required before those commands. No such commands have run.",
    "",
    "Plan publication, a new absent-upstream installation and any new native mutation fixture retain their scoped authority gates. Complete unaffected preparation before requesting the concrete missing authority.",
    "",
    "## Remaining verification",
    "",
    "Initial matrix coverage and guide syntax verification pending; every mandatory UNKNOWN blocks acceptance. No product source correction, fresh setup result, complete-stack acceptance or release is claimed.",
    "",
    "## Rulings",
    "",
]
lines += [f"- {r}" for r in data["rulings"]]
base.with_suffix(".md").write_text(
    "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
)
print(f"Created {len(rows)} rows; 1 prerequisite PASS, {len(rows) - 1} UNKNOWN")
```

## failure_probes.py

SHA-256: `e5387e00e03c67bd15779c247bddc30afb59e7e6189265cad3ad225c29c23dc7`

```python
"""Observe installed setup decisions against real local failure fixtures."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

ROOT = Path.cwd().resolve(strict=True)
WORK = ROOT / ".sp-bp/work/issue-11"
PROFILE = (WORK / "setup-profile").resolve(strict=True)
ATTEMPT = ""
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"
CASES = {
    "lookalike-source": (
        "upstream-lookalike",
        "Set up Backplane using the upstream checkout supplied for this session. Verify actual provenance before compatibility; do not trust its name or manifest repository field.",
    ),
    "missing-upstream-skill": (
        "upstream-missing-skill",
        "Set up Backplane using the supplied upstream checkout. Inspect every required upstream skill before compatibility, even when the plugin name and version look valid.",
    ),
    "dirty-adoption": (
        "upstream-dirty",
        "Set up Backplane by adopting the supplied authoritative sibling checkout in place. Do not update it. Inspect its dirty state and decide whether adoption without update is supported.",
    ),
    "dirty-update-refusal": (
        "upstream-dirty",
        "The operator requests an upstream update to the supplied authoritative checkout. Inspect its current state first. If a required safety precondition fails, stop before fetch/checkout and explain the concrete owner recovery. Do not actually mutate the checkout in this test.",
    ),
    "occupied-destination": (
        None,
        "Upstream is absent from this profile/session. The proposed fallback checkout destination is "
        + str(WORK / "fixtures/occupied-destination")
        + ". Inspect it before any checkout creation. Do not install or clone anything; report the setup stop and safe recovery for this existing destination.",
    ),
    "gh-auth-failure": (
        "upstream-clean",
        "Set up Backplane with the supplied compatible sibling checkout. Run the complete gh capability preflight; report any failed check and its recovery without bypassing it.",
    ),
    "gh-intake-failure": (
        "upstream-clean",
        "Set up Backplane with the supplied compatible sibling checkout. Run the complete gh capability preflight; require every native issue field and do not silently drop an unsupported one.",
    ),
    "gh-label-failure": (
        "upstream-clean",
        "Set up Backplane with the supplied compatible sibling checkout. Verify actual gh help for label addition/removal and closure reason; do not infer capabilities from its version.",
    ),
    "gh-closure-failure": (
        "upstream-clean",
        "Set up Backplane with the supplied compatible sibling checkout. Verify actual gh help for closure reason and label addition/removal; do not infer capabilities from its version.",
    ),
    "versionless-package": (
        None,
        "Set up Backplane with the currently installed versionless upstream native package. Inspect its actual native inventory, source and observable version/revision. A self-declared repository URL or an enclosing unrelated Git repository is not package provenance. Do not invent a version from cache naming.",
    ),
    "duplicate-backplane": (
        "upstream-clean",
        "Set up Backplane. Inspect the actual effective native plugin inventory and resolve duplicate/conflicting Backplane installations before any other adoption action. Do not remove or disable either fixture.",
    ),
}


def cli(args, env):
    executable = shutil.which(args[0], path=env["PATH"])
    assert executable is not None
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=90,
        shell=False,
        check=False,
    )
    assert result.returncode == 0, (args, result.stderr)
    return result.stdout


def snapshot(env, fixture):
    real_env = dict(env, PATH=os.environ["PATH"])
    value = {
        "plugins": json.loads(cli(["claude", "plugin", "list", "--json"], real_env)),
        "marketplaces": json.loads(
            cli(["claude", "plugin", "marketplace", "list", "--json"], real_env)
        ),
        "profile_hashes": {
            str(p.relative_to(PROFILE)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                PROFILE / "settings.json",
                PROFILE / "plugins/installed_plugins.json",
                PROFILE / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "issue11": json.loads(
            cli(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ],
                real_env,
            )
        ),
        "project_refs": cli(["git", "show-ref"], real_env),
        "real_upstream_head": cli(
            ["git", "-C", str(ROOT / ".agents/superpowers"), "rev-parse", "HEAD"],
            real_env,
        ),
        "real_upstream_status": cli(
            [
                "git",
                "-C",
                str(ROOT / ".agents/superpowers"),
                "status",
                "--porcelain=v1",
            ],
            real_env,
        ),
    }
    normal = Path.home() / ".claude"
    value["normal_profile_hashes"] = {
        str(p.relative_to(normal)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (
            normal / "settings.json",
            normal / "plugins/installed_plugins.json",
            normal / "plugins/known_marketplaces.json",
        )
        if p.is_file()
    }
    if fixture:
        value["fixture"] = {
            "root": str(fixture.resolve(strict=True)),
            "files": {
                p.relative_to(fixture).as_posix(): hashlib.sha256(
                    p.read_bytes()
                ).hexdigest()
                for p in fixture.rglob("*")
                if p.is_file() and ".git" not in p.relative_to(fixture).parts
            },
        }
        if (fixture / ".git").is_dir():
            value["fixture"]["git"] = {
                name: cli(["git", "-C", str(fixture), *args], real_env)
                for name, args in {
                    "head": ["rev-parse", "HEAD"],
                    "status": ["status", "--porcelain=v1"],
                    "origin": ["remote", "get-url", "origin"],
                    "refs": ["show-ref"],
                }.items()
            }
    return value


def probe(case):
    fixture_name, instruction = CASES[case]
    fixture = (
        WORK / "fixtures" / fixture_name
        if fixture_name
        else WORK / "fixtures/occupied-destination"
        if case == "occupied-destination"
        else None
    )
    if case == "versionless-package":
        fixture = WORK / "fixtures/versionless-upstream"
    elif case == "duplicate-backplane":
        fixture = WORK / "fixtures/duplicate-backplane"
    output = WORK / ("probe-" + case + ATTEMPT)
    assert not output.exists(), "Use an unused per-case output directory"
    output.mkdir()
    captures = output / "captures"
    captures.mkdir()
    neutral = output / "neutral"
    neutral.mkdir()
    env = dict(
        os.environ,
        CLAUDE_CONFIG_DIR=str(PROFILE),
        PYTHONIOENCODING="utf-8",
        TMPDIR=str(captures),
        TEMP=str(captures),
        TMP=str(captures),
    )
    env.update(
        SP_BP_GH_FAILURE="none",
        SP_BP_REAL_GH=(WORK / "real-gh-path.txt").read_text(encoding="utf-8"),
        PATH=str(WORK / "gh-shims") + os.pathsep + os.environ["PATH"],
    )
    if case.startswith("gh-"):
        variant = {
            "gh-auth-failure": "auth",
            "gh-intake-failure": "intake",
            "gh-label-failure": "labels",
            "gh-closure-failure": "closure",
        }[case]
        env.update(
            SP_BP_GH_FAILURE=variant,
            SP_BP_REAL_GH=(WORK / "real-gh-path.txt").read_text(encoding="utf-8"),
            PATH=str(WORK / "gh-shims") + os.pathsep + os.environ["PATH"],
        )
    before = snapshot(env, fixture)
    (output / "before.json").write_text(
        json.dumps(before, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    prompt = (
        "Use the installed superpowers-backplane:managing-superpowers-backlog skill and its installation reference for this real local fixture. "
        "Target repository tvproductions/superpowers-backplane, existing issue #11 (read-only). "
        + instruction
        + (
            f" The supplied fixture checkout path is {fixture}; --plugin-dir loads this exact path for this session. "
            if fixture_name
            else ""
        )
        + " Backplane is the explicitly selected local development candidate 4be5f0e9b6fa5acd3986584bbd8e617b6fc3e01e; do not claim it is remotely published. "
        + " Report the observed decision and a concrete recovery if blocked. "
        "Do not install/update/remove anything, edit user or package files, mutate GitHub or create a plan/handoff. "
        f"Capture any output only under the owned directory {captures}; never hardcode /tmp files. "
        f"The selected profile is {PROFILE}. Do not enumerate environment variables, read credentials, inspect other profiles, or silently substitute the real development checkout. "
        "Use the gh executable resolved by PATH for every capability check; do not bypass a failed preflight with an absolute gh.exe or different account. "
        "Do not run Python outside uv. Read source files directly when possible."
    )
    args = [
        "claude",
        "-p",
        prompt,
        "--tools",
        "Skill,Read,Bash,Glob",
        "--allowedTools",
        "Skill",
        "Read",
        "Glob",
        "Bash(gh *)",
        "Bash(git -C * remote get-url *)",
        "Bash(git -C * rev-parse *)",
        "Bash(git -C * status *)",
        "Bash(claude plugin list *)",
        "Bash(claude plugin marketplace list *)",
        "Bash(claude --version)",
        "--permission-mode",
        "default",
        "--disallowedTools",
        "Bash(env *)",
        "Bash(printenv *)",
        "Bash(* env *)",
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-turns",
        "24",
    ]
    if fixture_name:
        args += ["--plugin-dir", str(fixture)]
    args += ["--add-dir", str(output)]
    if fixture:
        args += ["--add-dir", str(fixture)]
    executable = shutil.which("claude")
    assert executable is not None
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=neutral,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
        shell=False,
        check=False,
    )
    (output / "events.jsonl").write_text(result.stdout, encoding="utf-8", newline="\n")
    (output / "stderr.txt").write_text(result.stderr, encoding="utf-8", newline="\n")
    events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    host = next((e for e in reversed(events) if e.get("type") == "result"), {})
    calls: list[dict[str, Any]] = []
    tool_results = []
    for event in events:
        message = event.get("message")
        if not isinstance(message, dict):
            continue
        for block in message.get("content", []):
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                calls.append(block)
            if block.get("type") == "tool_result":
                tool_results.append(block)
    after = snapshot(env, fixture)
    preserved = before == after
    receipt = {
        "case": case,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "prompt": prompt,
        "argv": args,
        "cli_exit": result.returncode,
        "host_result": host,
        "before": before,
        "after": after,
        "protected_state_preserved": preserved,
        "tool_calls": calls,
        "tool_results": tool_results,
        "result": "UNSCORED; inspect actual observed outcome against the case rubric",
    }
    (ROOT / f"tests/scenarios/2026-10-26-issue-11-{case}{ATTEMPT}.json").write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "case": case,
                "subtype": host.get("subtype"),
                "session": host.get("session_id"),
                "preserved": preserved,
                "tools": len(calls),
                "response": str(host.get("result", ""))[:550],
            }
        ),
        flush=True,
    )
    assert preserved, f"{case}: state changed; inspect saved evidence before repair"
    assert (
        result.returncode == 0
        and host.get("subtype") == "success"
        and not host.get("is_error")
    ), case


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", nargs="+", choices=list(CASES))
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--attempt", default="")
    options = parser.parse_args()
    ATTEMPT = options.attempt
    with ThreadPoolExecutor(max_workers=options.workers) as executor:
        list(executor.map(probe, options.cases))
```

## final_discovery.py

SHA-256: `1e3ec97e9fe390bd58cb2a170b15c51b5fded2790d9d7bc04d6b7f37d4d0ac85`

```python
"""Record actual final-candidate skill loads and source identities per upstream mode."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=("native", "sibling", "official"))
mode = parser.parse_args().mode
profile = (
    root / ".sp-bp/work/issue-19/profile"
    if mode == "native"
    else work / "setup-profile"
)
env = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile))


def run(args, *, timeout=90, cwd=root):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def state():
    normal = Path.home() / ".claude"
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "profile_hashes": {
            str(p.relative_to(profile)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                profile / "settings.json",
                profile / "plugins/installed_plugins.json",
                profile / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "normal_hashes": {
            str(p.relative_to(normal)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                normal / "settings.json",
                normal / "plugins/installed_plugins.json",
                normal / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "refs": run(["git", "show-ref"]),
    }


before = state()
prompt = (
    "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
    "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
    "and superpowers-backplane:managing-superpowers-handoffs, in that order. "
    "Only load them and report the actual three package roots. Do not run setup, read issues, "
    "create or resume a handoff, or create files. Report an unavailable skill honestly."
)
args = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill",
    "--allowedTools",
    "Skill",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "8",
]
if mode == "sibling":
    args += [
        "--settings",
        json.dumps({"enabledPlugins": {"superpowers@claude-plugins-official": False}}),
        "--plugin-dir",
        str(root / ".agents/superpowers"),
    ]
stream = run(args, cwd=work / "native-neutral", timeout=180)
(work / f"final-{mode}-discovery.jsonl").write_text(
    stream, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
host = next(e for e in reversed(events) if e.get("type") == "result")
assert host.get("subtype") == "success" and not host.get("is_error")
calls = []
tool_results = []
bases = []
for event in events:
    message = event.get("message")
    if not isinstance(message, dict):
        continue
    for block in message.get("content", []):
        if not isinstance(block, dict):
            continue
        if block.get("type") == "tool_use":
            calls.append(block)
        if block.get("type") == "tool_result":
            assert not block.get("is_error")
            tool_results.append(block)
        if isinstance(block.get("text"), str):
            bases += re.findall(
                r"Base directory for this skill: ([^\r\n]+)", block["text"]
            )
required = [
    "superpowers:using-superpowers",
    "superpowers-backplane:managing-superpowers-backlog",
    "superpowers-backplane:managing-superpowers-handoffs",
]
assert [call["input"]["skill"] for call in calls if call["name"] == "Skill"] == required
assert len(bases) >= 3, "Actual injected skill locators missing"
source = work / "fixtures/final-catalog/package"
expected = {name: source / "skills" / name.split(":")[1] for name in required[1:]}
if mode == "sibling":
    expected[required[0]] = root / ".agents/superpowers/skills/using-superpowers"
else:
    upstream_id = (
        "superpowers@superpowers-dev"
        if mode == "native"
        else "superpowers@claude-plugins-official"
    )
    upstream = next(p for p in before["plugins"] if p["id"] == upstream_id)
    expected[required[0]] = (
        Path(upstream.get("readFromFolder") or upstream["installPath"])
        / "skills/using-superpowers"
    )
resolved = [Path(path.strip()).resolve(strict=True) for path in bases]
for name, path in expected.items():
    assert any(actual.samefile(path) for actual in resolved), (name, str(path), bases)
after = state()
assert before == after, "Discovery changed protected configuration or refs"
registry = json.loads(
    (profile / "plugins/installed_plugins.json").read_text(encoding="utf-8")
)["plugins"]
assert (
    registry["superpowers-backplane@superpowers-backplane"][0]["gitCommitSha"]
    == "91ea3bb7933b5aa2c7628595f17157810cafa701"
)
receipt = {
    "result": "PASS",
    "mode": mode,
    "candidate": "91ea3bb7933b5aa2c7628595f17157810cafa701",
    "argv": args,
    "profile": str(profile),
    "before": before,
    "after": after,
    "session_id": host.get("session_id"),
    "tool_calls": calls,
    "tool_results": tool_results,
    "observed_skill_base_directories": bases,
    "response": host["result"],
    "source_selection": "Sibling mode disables only the existing official plugin for this invocation and supplies the verified sibling with --plugin-dir; persistent registry is preserved"
    if mode == "sibling"
    else "Native selected-profile registration",
    "raw_stream_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
}
(root / f"tests/scenarios/2026-10-26-issue-11-final-{mode}-discovery.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "result": "PASS",
            "mode": mode,
            "session": host.get("session_id"),
            "bases": bases,
        },
        indent=2,
    )
)
```

## finalize_candidate_evidence.py

SHA-256: `60bb00e8e032659e8babf641980da9eab2168911272e70fd2d7e9b5074802f1d`

```python
"""Reconcile original observations to the final local product candidate."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

from lifecycle_helpers import ISSUE_FIELDS, run_cli, write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
scenarios = root / "tests/scenarios"
prefix = "2026-10-26-issue-11-"
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"
baseline = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
commands = []


def command(args, env=None):
    text = run_cli(args, cwd=root, overrides=env)
    commands.append({"argv": args, "exit": 0, "stdout": text})
    return text


assert Path(command(["git", "rev-parse", "--show-toplevel"]).strip()).samefile(root)
assert (
    command(["git", "branch", "--show-current"]).strip()
    == "feat/issue-11-claude-acceptance"
)
assert command(["git", "rev-parse", "HEAD"]).strip() == candidate
source_comparison = {}
for path in (
    "docs/installing-claude-code.md",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "plugin.json",
    "skills/managing-superpowers-backlog/SKILL.md",
    "skills/managing-superpowers-handoffs/SKILL.md",
    "skills/managing-superpowers-backlog/references/installing-superpowers.md",
    "skills/managing-superpowers-backlog/references/superpowers-binding.md",
    "skills/managing-superpowers-backlog/references/pr-completion.md",
):
    first = command(["git", "rev-parse", f"{baseline}:{path}"]).strip()
    last = command(["git", "rev-parse", f"{candidate}:{path}"]).strip()
    assert first == last, path
    source_comparison[path] = {"original": first, "candidate": last, "equal": True}
diff = command(["git", "diff", baseline, candidate, "--", "skills"])
assert diff.count("diff --git") == 1 and "github-issue-contract.md" in diff
prerequisites = []
for number in (17, 18, 19):
    issue = json.loads(
        command(
            [
                "gh",
                "issue",
                "view",
                str(number),
                "--repo",
                "tvproductions/superpowers-backplane",
                "--json",
                ISSUE_FIELDS,
            ]
        )
    )
    assert issue["state"] == "CLOSED" and issue["stateReason"] == "COMPLETED"
    prerequisites.append(issue)
for rev in ("7d7ecac36f8dc74ce1a0895ab934468332f92f53", baseline):
    command(["git", "merge-base", "--is-ancestor", rev, candidate])
upstream_files = []
for mode, profile, uid, revision in (
    (
        "native",
        root / ".sp-bp/work/issue-19/profile",
        "superpowers@superpowers-dev",
        "2ce8aa15d05bd57213e6f746f953aafb7ded7a8b",
    ),
    (
        "official",
        work / "setup-profile",
        "superpowers@claude-plugins-official",
        "bb92a77741419a4ab5f06e711a283343f1ada0c3",
    ),
):
    env = {"CLAUDE_CONFIG_DIR": str(profile)}
    inventory = json.loads(command(["claude", "plugin", "list", "--json"], env))
    entry = next(p for p in inventory if p["id"] == uid)
    package = Path(entry.get("readFromFolder") or entry["installPath"])
    for path in (
        ".claude-plugin/plugin.json",
        "skills/using-superpowers/SKILL.md",
        "skills/brainstorming/SKILL.md",
        "skills/writing-plans/SKILL.md",
        "skills/writing-skills/SKILL.md",
    ):
        blob = command(
            [
                "git",
                "-C",
                str(root / ".agents/superpowers"),
                "rev-parse",
                f"{revision}:{path}",
            ]
        ).strip()
        content = (package / path).read_bytes()
        actual = hashlib.sha1(
            f"blob {len(content)}\0".encode("ascii") + content, usedforsecurity=False
        ).hexdigest()
        assert blob == actual
        upstream_files.append(
            {
                "mode": mode,
                "source": revision,
                "path": path,
                "blob": blob,
                "actual": actual,
            }
        )
    command(
        [
            "claude",
            "plugin",
            "validate",
            "--strict",
            str(work / "fixtures/final-catalog/package"),
        ],
        env,
    )
command(["pwsh", "-NoProfile", "-File", str(work / "parse_guide.ps1")])
structure = []
for name in ("managing-superpowers-backlog", "managing-superpowers-handoffs"):
    path = root / "skills" / name / "SKILL.md"
    content = path.read_text(encoding="utf-8")
    assert content.startswith("---\n") and f"name: {name}\n" in content
    assert re.search(r"^description: Use when ", content, re.M)
    links = []
    for link in re.findall(r"\]\(([^)]+)\)", content):
        if "://" in link or link.startswith("#"):
            continue
        target = (path.parent / link.split("#")[0]).resolve(strict=True)
        assert target.is_relative_to(root)
        links.append(
            {"link": link, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
        )
    assert links
    assert not re.search(r"TODO|FIXME|\[INSERT", content)
    structure.append({"skill": name, "links": links, "result": "PASS"})

# The read-only adapter must preserve help aliases without letting writes through.
real_gh = shutil.which("gh")
assert real_gh is not None
uv_executable = shutil.which("uv")
assert uv_executable is not None
aliases = []
for case in ("none", "intake", "labels", "closure"):
    for args in (
        ["auth", "status", "--hostname", "github.com"],
        ["issue", "edit", "-h"],
        ["issue", "close", "-h"],
    ):
        env = dict(os.environ, SP_BP_GH_FAILURE=case, SP_BP_REAL_GH=real_gh)
        result = subprocess.run(
            [
                uv_executable,
                "run",
                "--no-project",
                "python",
                str(work / "gh_stub.py"),
                *args,
            ],
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        assert result.returncode == 0, (case, args)
        if case == "labels" and args[1] == "edit":
            assert "--add-label" not in result.stdout
        if case == "closure" and args[1] == "close":
            assert "--reason" not in result.stdout
        aliases.append({"case": case, "argv": args, "exit": result.returncode})
write_json(
    scenarios / (prefix + "candidate-verification.json"),
    {
        "result": "PASS",
        "candidate": candidate,
        "host": command(["claude", "--version"]).strip(),
        "gh": command(["gh", "--version"]).strip(),
        "commands": commands,
        "unchanged_component_blobs": source_comparison,
        "skill_diff": diff,
        "upstream_source_blob_checks": upstream_files,
        "skill_structure": structure,
        "prerequisites": prerequisites,
        "adapter_alias_checks": aliases,
        "applicability": {
            "C_lifecycle_to_E": "Nine exact guide blocks, manifests, installation guard reference and discovery SKILL files are byte-identical. Retain C->test F->C package mechanism observations at original SHA/host; final E install, 21 installed-file comparisons, three fresh mode discoveries and shared-catalog uninstall/restoration cover changed payload delivery. No new E hosted update is claimed before publication.",
            "D_failures_to_E": "Only authorization carry-forward paragraph was added after D. Provenance, dirty/update, destination, duplicate, capability and versionless guards did not change. Final E conformance covers that paragraph and all setup expectations under both upstream sources; retain D negative fixture observations with original identity.",
            "historical_issue_mutations": "Retain actual #34 native transitions and integrated closure as historical state observations, not fresh Claude 2.1.311 mutations. Current E full conformance reruns intake, entry gates, cardinality, blocked/resume, rework, closure and authorization semantics. Fresh E #11 status/selection and actual authorized #11 design/ready/active observations supplement them. Current gh capabilities verified; predecessor gh exact version was not recorded in the #34 receipt, so no version-equality claim is made.",
        },
    },
)
print(
    "PASS: candidate source/applicability, two upstream identities, strict package validation, skill structure, PowerShell parse, prerequisite completion and gh adapter aliases"
)
```

## finalize_preparation.py

SHA-256: `f0694a79e09a3c6f0dc7accfea5edda15f4f1161fbfd162ac0081c08cb6ddd69`

```python
"""Preserve reproducible read-only preparation and its negative controls."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
base = root / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance"
audit = json.loads(
    (root / "tests/scenarios/2026-10-26-issue-11-input-audit.json").read_text(
        encoding="utf-8"
    )
)
data = json.loads(base.with_suffix(".json").read_text(encoding="utf-8"))
for row in data["rows"]:
    for evidence in row["evidence"]:
        evidence["sha256"] = hashlib.sha256(
            (root / evidence["path"]).read_bytes()
        ).hexdigest()
base.with_suffix(".json").write_text(
    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
profile = root / ".sp-bp/work/issue-19/profile"
environment = dict(os.environ, PYTHONIOENCODING="utf-8", CLAUDE_CONFIG_DIR=str(profile))
commands = []


def observe(argv, expected=0):
    executable = shutil.which(argv[0])
    assert executable
    result = subprocess.run(
        [executable, *argv[1:]],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=90,
        shell=False,
        check=False,
    )
    record = {
        "argv": argv,
        "exit": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    commands.append(record)
    assert result.returncode == expected, record
    return result


observe(["claude", "plugin", "validate", "--strict", str(root)])
observe(["pwsh", "-NoProfile", "-File", str(work / "parse_guide.ps1")])
observe(
    [
        "uv",
        "run",
        "--no-project",
        "python",
        str(work / "verify_evidence.py"),
        "--phase",
        "initial",
    ]
)
rejected = observe(
    [
        "uv",
        "run",
        "--no-project",
        "python",
        str(work / "verify_evidence.py"),
        "--phase",
        "acceptance",
    ],
    expected=1,
)
assert "Acceptance blocked:" in rejected.stderr
sources = [
    work / name
    for name in (
        "audit_inputs.py",
        "create_matrix.py",
        "verify_evidence.py",
        "parse_guide.ps1",
        "finalize_preparation.py",
        "verify_transport.py",
    )
]
python_sources = [str(path) for path in sources if path.suffix == ".py"]
observe(["uv", "run", "--no-project", "ruff", "check", *python_sources])
observe(["uv", "run", "--no-project", "ruff", "format", "--check", *python_sources])
observe(["uv", "run", "--no-project", "ty", "check", *python_sources])
after = {
    path: hashlib.sha256((profile / path).read_bytes()).hexdigest()
    for path in audit["profile"]["config_hashes"]
}
assert after == audit["profile"]["config_hashes"], (
    "Read-only preparation changed profile configuration"
)
plan = (
    root
    / "docs/superpowers-backplane/plans/2026-10-26-issue-11-claude-integrated-acceptance.md"
)
text_paths = [
    plan,
    base.with_suffix(".md"),
    base.with_suffix(".json"),
    root / "tests/scenarios/2026-10-26-issue-11-input-audit.json",
]
for path in text_paths:
    content = path.read_text(encoding="utf-8")
    assert not any(line.rstrip() != line for line in content.splitlines()), path
    assert not re.search(r"gh[pousr]_[A-Za-z0-9]{20,}", content), (
        "Possible token; refuse archive"
    )
    assert not re.search(r"[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}", content), (
        "Possible email; refuse archive"
    )
summary = {
    "phase": "preparation",
    "result": "PASS",
    "matrix_rows": 39,
    "prerequisite_pass": 1,
    "unknown": 38,
    "profile_configuration_unchanged": True,
    "guide_python_blocks_compiled": 9,
    "guide_powershell_blocks_parsed": 4,
    "execution_scope": "read-only preparation; no live acceptance PASS claimed",
    "commands": commands,
    "source_hashes": {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sources
    },
}
receipt_path = root / "tests/scenarios/2026-10-26-issue-11-preparation.json"
receipt_path.write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
lines = [
    "# Issue #11 preparation transcript and source",
    "",
    "Only read-only commands ran. No clone, checkout, profile installation, upstream acquisition, live model session, publication or native lifecycle fixture ran.",
    "",
    "The approved in-place feature branch was created before preparation. #11 remains designing; setup execution awaits the fixture/publication boundaries described in the matrix report.",
    "",
    "Auth email and organization fields are redacted in the input audit. No credential files were read or copied. Script sources below are the executed/formatted sources for the final audit and verification.",
    "",
    "## Initial missing-matrix negative control",
    "",
    "```text",
    (work / "missing-matrix-negative-control.txt").read_text(encoding="utf-8").rstrip(),
    "```",
    "",
    "## Preparation verification commands",
    "",
]
for command in commands:
    lines += [
        "```text",
        json.dumps(command["argv"]),
        f"exit={command['exit']}",
        command["stdout"].rstrip(),
        command["stderr"].rstrip(),
        "```",
        "",
    ]
lines += ["## Preserved harness sources", ""]
for source in sources:
    lines += [
        f"### {source.name}",
        "",
        f"SHA-256: `{summary['source_hashes'][source.name]}`",
        "",
        "```powershell" if source.suffix == ".ps1" else "```python",
        source.read_text(encoding="utf-8").rstrip(),
        "```",
        "",
    ]
transcript = (
    root
    / "tests/scenarios/transcripts/2026-10-26-issue-11-claude-integrated-acceptance.md"
)
transcript.write_text("\n".join(lines), encoding="utf-8", newline="\n")
issue = audit["issues"]["11"]
assert issue["body"].count("Plan: not yet created.") == 1
template = issue["body"].replace(
    "Plan: not yet created.",
    "Approved plan: [Claude Code integrated acceptance](https://github.com/tvproductions/superpowers-backplane/blob/PLAN_PUBLICATION_SHA/docs/superpowers-backplane/plans/2026-10-26-issue-11-claude-integrated-acceptance.md). Operator approved native execution on 2026-10-26. Consumed semantic revision `2026-09-20T01:31:32Z`; the later planning-label revision changes no scope or acceptance criteria.",
)
(work / "issue11-approved-plan-body-template.md").write_text(
    template, encoding="utf-8", newline="\n"
)
print(
    json.dumps(
        {
            key: value
            for key, value in summary.items()
            if key not in ("commands", "source_hashes")
        },
        indent=2,
    )
)
```

## finish_evidence_checks.py

SHA-256: `8238c678d38052d44cf7ed66362f54646c8c05be9c10d5712c20a32f55fa68a6`

```python
"""Run owned-helper quality checks and seal current evidence pointers."""

import hashlib
import json
from pathlib import Path

from lifecycle_helpers import run_cli, write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
base = root / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance"
helpers = sorted(work.glob("*.py"))
paths = [str(path.relative_to(root)) for path in helpers]
commands = []
for args in (
    ["uv", "run", "--no-project", "ruff", "check", *paths],
    ["uv", "run", "--no-project", "ruff", "format", "--check", *paths],
    ["uv", "run", "--no-project", "ty", "check", *paths],
):
    output = run_cli(args, cwd=root)
    commands.append({"argv": args, "exit": 0, "stdout": output})
    print(output.strip(), flush=True)
source = [
    "# Final owned verification helper sources",
    "",
    "Post-format sources for reproducibility. The preceding verification-sources transcript preserves the earlier sources actually used for the live runs. These final sources include the executable-availability guard; no live result is relabeled as a rerun merely because formatting changed.",
    "",
]
for path in helpers:
    source += [
        f"## {path.name}",
        "",
        f"SHA-256: `{hashlib.sha256(path.read_bytes()).hexdigest()}`",
        "",
        "```python",
        path.read_text(encoding="utf-8").rstrip(),
        "```",
        "",
    ]
(
    root
    / "tests/scenarios/transcripts/2026-10-26-issue-11-verification-sources-final.md"
).write_text("\n".join(source), encoding="utf-8", newline="\n")
data = json.loads(base.with_suffix(".json").read_text(encoding="utf-8"))
for row in data["rows"]:
    for evidence in row["evidence"]:
        evidence["sha256"] = hashlib.sha256(
            (root / evidence["path"]).read_bytes()
        ).hexdigest()
write_json(base.with_suffix(".json"), data)
args = [
    "uv",
    "run",
    "--no-project",
    "python",
    str(work / "verify_evidence.py"),
    "--phase",
    "acceptance",
]
output = run_cli(args, cwd=root)
commands.append({"argv": args, "exit": 0, "stdout": output})
print(output.strip(), flush=True)
write_json(
    root / "tests/scenarios/2026-10-26-issue-11-quality-checks.json",
    {
        "result": "PASS",
        "owned_python_files": paths,
        "commands": commands,
        "scope": "Enumerated owned helper files only; no upstream or host-managed cache is formatted or linted. Evidence gate checks 39 rows and compiles nine current Python guide blocks. Strict package and PowerShell checks are separately captured in candidate-verification receipt.",
    },
)
```

## gh_stub.py

SHA-256: `9b15030168741caa7d48030e0b76183d0bab66ed522c30b6ffbe098af11959f3`

```python
"""Read-only gh adapter with one selected capability failure per test session."""

import json
import os
from pathlib import Path
import subprocess
import sys

args = sys.argv[1:]
case = os.environ["SP_BP_GH_FAILURE"]
real = os.environ["SP_BP_REAL_GH"]
root = Path(__file__).resolve().parent
with (root / f"gh-{case}-calls.jsonl").open("a", encoding="utf-8", newline="\n") as log:
    log.write(json.dumps({"case": case, "argv": args}) + "\n")
if case == "auth" and args[:2] == ["auth", "status"]:
    print(
        "Fixture: gh authentication is unavailable; authenticate the selected account before setup",
        file=sys.stderr,
    )
    raise SystemExit(1)
if case == "intake" and args[:2] == ["issue", "view"]:
    print(
        "Fixture: required native JSON field issueType is unsupported", file=sys.stderr
    )
    raise SystemExit(1)
help_requested = "--help" in args or "-h" in args
if case == "labels" and args[:2] == ["issue", "edit"] and help_requested:
    print("Fixture gh issue edit help: label addition/removal capability unavailable")
    raise SystemExit(0)
if case == "closure" and args[:2] == ["issue", "close"] and help_requested:
    print("Fixture gh issue close help: closure-reason capability unavailable")
    raise SystemExit(0)
allowed = args in (
    ["--version"],
    ["auth", "status"],
    ["issue", "edit", "--help"],
    ["issue", "close", "--help"],
)
allowed |= (
    args[:2] == ["auth", "status"]
    and "--show-token" not in args
    and "--json" not in args
)
allowed |= args[:2] in (["issue", "edit"], ["issue", "close"]) and help_requested
allowed |= args[:2] in (
    ["issue", "view"],
    ["issue", "list"],
    ["label", "list"],
    ["release", "view"],
    ["repo", "view"],
)
if args[:1] == ["api"]:
    allowed = (
        len(args) > 1
        and args[1].startswith("repos/")
        and not any(
            arg in ("-X", "--method", "-f", "-F", "--field", "--raw-field", "--input")
            for arg in args
        )
    )
if not allowed:
    print("Fixture adapter refuses mutation or unsupported command", file=sys.stderr)
    raise SystemExit(64)
raise SystemExit(subprocess.call([real, *args], shell=False))
```

## install_current_candidate.py

SHA-256: `bdd3e0f8b1c5dc5b579fd55215e1cd40a5e62bbeef578f30d4e73063c66457b0`

```python
"""Install the immutable local reference-fix candidate into the two test profiles."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
candidate = "4be5f0e9b6fa5acd3986584bbd8e617b6fc3e01e"
catalog = work / "fixtures/current-catalog"
package = catalog / "package"
commands = []


def run(args, env=None):
    executable = shutil.which(args[0])
    assert executable is not None
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        check=False,
    )
    commands.append(
        {
            "argv": args,
            "profile": (env or {}).get("CLAUDE_CONFIG_DIR"),
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    assert result.returncode == 0, commands[-1]
    return result.stdout


assert (
    Path(run(["git", "rev-parse", "--show-toplevel"]).strip()).resolve(strict=True)
    == root
)
assert not catalog.exists()
catalog.mkdir()
run(
    [
        "git",
        "clone",
        "--no-hardlinks",
        "--branch",
        "feat/issue-11-claude-acceptance",
        str(root),
        str(package),
    ]
)
assert Path(
    run(["git", "-C", str(package), "rev-parse", "--show-toplevel"]).strip()
).resolve(strict=True) == package.resolve(strict=True)
assert run(["git", "-C", str(package), "rev-parse", "HEAD"]).strip() == candidate
with (work / "progress.md").open("a", encoding="utf-8", newline="\n") as ledger:
    ledger.write(
        f"- Current local candidate fixture registered before mutation: root={package.resolve()}; starting revision={candidate}; origin={root}; purpose=installed reference-fix validation.\n"
    )
run(["git", "-C", str(package), "checkout", "--detach", candidate])
run(
    [
        "git",
        "-C",
        str(package),
        "remote",
        "set-url",
        "origin",
        "https://github.com/tvproductions/superpowers-backplane.git",
    ]
)
assert not (package / ".git/objects/info/alternates").exists()
manifest = catalog / ".claude-plugin/marketplace.json"
manifest.parent.mkdir()
value = {
    "name": "superpowers-backplane",
    "description": "Current immutable local candidate and preservation controls",
    "owner": {"name": "tvproductions"},
    "plugins": [
        {
            "name": "superpowers-backplane",
            "description": "Issue11 immutable local development candidate",
            "source": "./package",
        }
    ],
}
manifest.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
source = run(
    [
        "git",
        "ls-tree",
        "-r",
        candidate,
        "--",
        "skills",
        "plugin.json",
        ".claude-plugin",
        "README.md",
    ]
)
profiles = []
for profile in (root / ".sp-bp/work/issue-19/profile", work / "setup-profile"):
    env = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile))
    before = json.loads(run(["claude", "plugin", "list", "--json"], env))
    markets = json.loads(
        run(["claude", "plugin", "marketplace", "list", "--json"], env)
    )
    entry = next(m for m in markets if m["name"] == "superpowers-backplane")
    old_root = Path(entry["path"])
    old_catalog = json.loads(
        (old_root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
    )
    assert [p["name"] for p in old_catalog["plugins"]] == ["superpowers-backplane"]
    run(["claude", "plugin", "validate", "--strict", str(catalog)], env)
    run(
        [
            "claude",
            "plugin",
            "uninstall",
            "superpowers-backplane@superpowers-backplane",
            "--scope",
            "user",
        ],
        env,
    )
    run(["claude", "plugin", "marketplace", "remove", "superpowers-backplane"], env)
    run(["claude", "plugin", "marketplace", "add", str(catalog)], env)
    run(
        [
            "claude",
            "plugin",
            "install",
            "superpowers-backplane@superpowers-backplane",
            "--scope",
            "user",
        ],
        env,
    )
    after = json.loads(run(["claude", "plugin", "list", "--json"], env))
    assert [
        p for p in before if p["id"] != "superpowers-backplane@superpowers-backplane"
    ] == [p for p in after if p["id"] != "superpowers-backplane@superpowers-backplane"]
    installed = next(
        p for p in after if p["id"] == "superpowers-backplane@superpowers-backplane"
    )
    installed_root = Path(
        installed.get("readFromFolder") or installed["installPath"]
    ).resolve(strict=True)
    checks = []
    for line in source.splitlines():
        metadata, name = line.split("\t", 1)
        expected = metadata.split()[2]
        content = (installed_root / name).read_bytes()
        actual = hashlib.sha1(
            f"blob {len(content)}\0".encode("ascii") + content, usedforsecurity=False
        ).hexdigest()
        assert actual == expected, name
        checks.append({"path": name, "expected": expected, "actual": actual})
    assert len(checks) == 21
    profiles.append(
        {
            "profile": str(profile),
            "before": before,
            "after": after,
            "installed_files": checks,
        }
    )
(root / "tests/scenarios/2026-10-26-issue-11-current-candidate.json").write_text(
    json.dumps(
        {
            "result": "PASS",
            "candidate": candidate,
            "publication": "local immutable commit; not yet published",
            "catalog": str(catalog),
            "package": str(package),
            "profiles": profiles,
            "commands": commands,
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    "PASS: local candidate 4be5f0e installed in both profiles; 21 files each match; unrelated plugins preserved"
)
```

## install_final_candidate.py

SHA-256: `dd4e088d1714e4f6853a13ec3f0df7988cfa80ca362f81cdd6e58b04057c5490`

```python
"""Install the immutable local reference-fix candidate into the two test profiles."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"
catalog = work / "fixtures/final-catalog"
package = catalog / "package"
commands = []


def run(args, env=None):
    executable = shutil.which(args[0])
    assert executable is not None
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        check=False,
    )
    commands.append(
        {
            "argv": args,
            "profile": (env or {}).get("CLAUDE_CONFIG_DIR"),
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    assert result.returncode == 0, commands[-1]
    return result.stdout


assert (
    Path(run(["git", "rev-parse", "--show-toplevel"]).strip()).resolve(strict=True)
    == root
)
assert not catalog.exists()
catalog.mkdir()
run(
    [
        "git",
        "clone",
        "--no-hardlinks",
        "--branch",
        "feat/issue-11-claude-acceptance",
        str(root),
        str(package),
    ]
)
assert Path(
    run(["git", "-C", str(package), "rev-parse", "--show-toplevel"]).strip()
).resolve(strict=True) == package.resolve(strict=True)
assert run(["git", "-C", str(package), "rev-parse", "HEAD"]).strip() == candidate
with (work / "progress.md").open("a", encoding="utf-8", newline="\n") as ledger:
    ledger.write(
        f"- Current local candidate fixture registered before mutation: root={package.resolve()}; starting revision={candidate}; origin={root}; purpose=installed reference-fix validation.\n"
    )
run(["git", "-C", str(package), "checkout", "--detach", candidate])
run(
    [
        "git",
        "-C",
        str(package),
        "remote",
        "set-url",
        "origin",
        "https://github.com/tvproductions/superpowers-backplane.git",
    ]
)
assert not (package / ".git/objects/info/alternates").exists()
manifest = catalog / ".claude-plugin/marketplace.json"
manifest.parent.mkdir()
value = {
    "name": "superpowers-backplane",
    "description": "Current immutable local candidate and preservation controls",
    "owner": {"name": "tvproductions"},
    "plugins": [
        {
            "name": "superpowers-backplane",
            "description": "Issue11 immutable local development candidate",
            "source": "./package",
        }
    ],
}
manifest.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
source = run(
    [
        "git",
        "ls-tree",
        "-r",
        candidate,
        "--",
        "skills",
        "plugin.json",
        ".claude-plugin",
        "README.md",
    ]
)
profiles = []
for profile in (root / ".sp-bp/work/issue-19/profile", work / "setup-profile"):
    env = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile))
    before = json.loads(run(["claude", "plugin", "list", "--json"], env))
    markets = json.loads(
        run(["claude", "plugin", "marketplace", "list", "--json"], env)
    )
    entry = next(m for m in markets if m["name"] == "superpowers-backplane")
    old_root = Path(entry["path"])
    old_catalog = json.loads(
        (old_root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
    )
    assert [p["name"] for p in old_catalog["plugins"]] == ["superpowers-backplane"]
    run(["claude", "plugin", "validate", "--strict", str(catalog)], env)
    run(
        [
            "claude",
            "plugin",
            "uninstall",
            "superpowers-backplane@superpowers-backplane",
            "--scope",
            "user",
        ],
        env,
    )
    run(["claude", "plugin", "marketplace", "remove", "superpowers-backplane"], env)
    run(["claude", "plugin", "marketplace", "add", str(catalog)], env)
    run(
        [
            "claude",
            "plugin",
            "install",
            "superpowers-backplane@superpowers-backplane",
            "--scope",
            "user",
        ],
        env,
    )
    after = json.loads(run(["claude", "plugin", "list", "--json"], env))
    assert [
        p for p in before if p["id"] != "superpowers-backplane@superpowers-backplane"
    ] == [p for p in after if p["id"] != "superpowers-backplane@superpowers-backplane"]
    installed = next(
        p for p in after if p["id"] == "superpowers-backplane@superpowers-backplane"
    )
    installed_root = Path(
        installed.get("readFromFolder") or installed["installPath"]
    ).resolve(strict=True)
    checks = []
    for line in source.splitlines():
        metadata, name = line.split("\t", 1)
        expected = metadata.split()[2]
        content = (installed_root / name).read_bytes()
        actual = hashlib.sha1(
            f"blob {len(content)}\0".encode("ascii") + content, usedforsecurity=False
        ).hexdigest()
        assert actual == expected, name
        checks.append({"path": name, "expected": expected, "actual": actual})
    assert len(checks) == 21
    profiles.append(
        {
            "profile": str(profile),
            "before": before,
            "after": after,
            "installed_files": checks,
        }
    )
(root / "tests/scenarios/2026-10-26-issue-11-final-candidate.json").write_text(
    json.dumps(
        {
            "result": "PASS",
            "candidate": candidate,
            "publication": "local immutable commit; not yet published",
            "catalog": str(catalog),
            "package": str(package),
            "profiles": profiles,
            "commands": commands,
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    "PASS: local candidate 91ea3bb installed in both profiles; 21 files each match; unrelated plugins preserved"
)
```

## lifecycle_helpers.py

SHA-256: `b20997f0adba17ba6f09b4506f7c4d2e8c6c7242ee90056fa215749d64e20cf8`

```python
"""Portable orchestration; no shell, profile fallback, or credential copying."""

from collections.abc import Mapping, Sequence
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any

REPOSITORY = "tvproductions/superpowers-backplane"
BASELINE = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
FIXTURE = "5e01704fcdda13eefeeac52d8892da26e7164ffd"
BACKPLANE = "superpowers-backplane@superpowers-backplane"
ISSUE_FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run_cli(
    arguments: Sequence[str], *, cwd: Path, overrides: Mapping[str, str] | None = None
) -> str:
    environment = dict(os.environ, PYTHONIOENCODING="utf-8")
    environment.update(overrides or {})
    executable = shutil.which(arguments[0])
    if executable is None:
        raise FileNotFoundError(f"Required executable unavailable: {arguments[0]}")
    result = subprocess.run(
        [executable, *arguments[1:]],
        cwd=cwd,
        env=environment,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"{arguments[0]} exited {result.returncode}: {result.stdout}{result.stderr}"
        )
    return result.stdout


def compare_preservation(before: Any, after: Any) -> None:
    if before != after:
        raise ValueError("Preservation mismatch; retain snapshot before repair")


def verify_file(path: Path, expected_blob: str) -> None:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("ascii")
    if (
        hashlib.sha1(header + content, usedforsecurity=False).hexdigest()
        != expected_blob
    ):
        raise ValueError(f"Installed byte mismatch: {path}")


def validate_revision(revision: str) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise ValueError("Use a full lowercase 40-character commit SHA")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


class Harness:
    def __init__(
        self,
        root: Path,
        profile: Path | None = None,
        catalog: Path | None = None,
        output: Path | None = None,
        upstream_id: str = "superpowers@superpowers-dev",
    ):
        self.root = root.resolve(strict=True)
        self.upstream_id = upstream_id
        base_work = self.root / ".sp-bp" / "work" / "issue-11"
        self.work = (output or base_work).resolve()
        self.profile = (profile or base_work / "profile").resolve(strict=True)
        self.catalog = (catalog or base_work / "catalog").resolve()
        self.environment = {"CLAUDE_CONFIG_DIR": str(self.profile)}
        index = int(os.environ.get("GIT_CONFIG_COUNT", "0") or "0")
        self.environment.update(
            {
                "GIT_CONFIG_COUNT": str(index + 1),
                f"GIT_CONFIG_KEY_{index}": f"url.https://github.com/{REPOSITORY}.insteadOf",
                f"GIT_CONFIG_VALUE_{index}": f"git@github.com:{REPOSITORY}",
            }
        )

    def command(self, arguments: Sequence[str]) -> str:
        return run_cli(arguments, cwd=self.root, overrides=self.environment)

    def claude(self, *arguments: str) -> str:
        print(f"CLAUDE_CONFIG_DIR={self.profile}", flush=True)
        output = self.command(["claude", *arguments])
        print(output, end="" if output.endswith("\n") else "\n", flush=True)
        return output

    def source(self, revision: str) -> None:
        validate_revision(revision)
        manifest = self.catalog / ".claude-plugin" / "marketplace.json"
        if self.catalog.exists():
            existing = read_json(manifest)
            entries = existing.get("plugins", [])
            if (
                existing.get("name") != "superpowers-backplane"
                or len(entries) != 1
                or entries[0].get("name") != "superpowers-backplane"
                or entries[0].get("source", {}).get("source") != "github"
                or entries[0].get("source", {}).get("repo") != REPOSITORY
            ):
                raise ValueError(
                    "Occupied catalog is not the verified dedicated Backplane source"
                )
        # Availability is checked before catalog or installed-package mutation.
        available = self.command(
            ["gh", "api", f"repos/{REPOSITORY}/commits/{revision}", "--jq", ".sha"]
        ).strip()
        if available != revision:
            raise ValueError(
                "Source unavailable; retain prior catalog and installation"
            )
        write_json(
            manifest,
            {
                "name": "superpowers-backplane",
                "description": "Pinned Backplane hosted-source catalog",
                "owner": {"name": "tvproductions"},
                "plugins": [
                    {
                        "name": "superpowers-backplane",
                        "description": "Pinned Backplane package",
                        "source": {
                            "source": "github",
                            "repo": REPOSITORY,
                            "sha": revision,
                        },
                    }
                ],
            },
        )

    def discovery(self, row: str, *, absent: bool = False) -> None:
        prompt = (
            "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
            "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
            "and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe "
            "requests only actual skill loading and reporting the three loaded package roots; "
            "it does not request setup, implementation, handoff creation/resume, issue intake "
            "or mutation. Do not create any file. Report any missing skill honestly."
        )
        if absent:
            prompt = (
                "Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. "
                "Then inspect your available Skill tool skill inventory and report whether "
                "superpowers-backplane:managing-superpowers-backlog and "
                "superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to "
                "install anything, read files, create a handoff, or mutate GitHub. Do not invent "
                "a successful load of unavailable skills."
            )
        print(
            f"{row}: fresh Skill-only discovery; CLAUDE_CONFIG_DIR={self.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--tools",
                "Skill",
                "--allowedTools",
                "Skill",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "8",
            ],
            cwd=self.work / "neutral",
            overrides=self.environment,
        )
        (self.work / f"{row}-discovery.jsonl").write_text(
            output, encoding="utf-8", newline="\n"
        )
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError("Fresh discovery session did not succeed")
        calls = []
        for event in events:
            for block in event.get("message", {}).get("content", []):
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    calls.append(block["input"]["skill"])
                if block.get("type") == "tool_result" and block.get("is_error"):
                    raise ValueError("Discovery tool load failed")
        required = ["superpowers:using-superpowers"]
        if not absent:
            required += [
                "superpowers-backplane:managing-superpowers-backlog",
                "superpowers-backplane:managing-superpowers-handoffs",
            ]
        if any(skill not in calls for skill in required):
            raise ValueError("Missing actual Skill tool invocation")
        if absent:
            initialization = next(
                event for event in events if event.get("subtype") == "init"
            )
            if "skills" not in initialization:
                raise ValueError("Native skill inventory unavailable")
            if any(
                "superpowers-backplane" in str(skill)
                for skill in initialization["skills"]
            ):
                raise ValueError("Backplane remains in fresh native skill inventory")
        write_json(
            self.work / f"{row}-discovery-summary.json",
            {
                "row": row,
                "session": result["session_id"],
                "skills": calls,
                "result": result["result"],
                "absent": absent,
            },
        )
        print(f"{row}: discovery PASS; session={result['session_id']}", flush=True)

    def snapshot(
        self,
        row: str,
        revision: str | None,
        version: str | None,
        *,
        capture_only: bool = False,
        compare_to: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        plugins = json.loads(self.command(["claude", "plugin", "list", "--json"]))
        marketplaces = json.loads(
            self.command(["claude", "plugin", "marketplace", "list", "--json"])
        )
        registry = read_json(self.profile / "plugins" / "installed_plugins.json")[
            "plugins"
        ]
        entries = registry.get(BACKPLANE, [])
        files = []
        if revision is None:
            if any(item["id"] == BACKPLANE for item in plugins):
                raise ValueError("Backplane expected absent")
        else:
            if (
                len(entries) != 1
                or entries[0]["gitCommitSha"] != revision
                or entries[0]["version"] != version
            ):
                raise ValueError("Installed revision/version/cardinality mismatch")
            tree = self.command(
                [
                    "git",
                    "ls-tree",
                    "-r",
                    revision,
                    "--",
                    "skills",
                    "plugin.json",
                    ".claude-plugin/plugin.json",
                    ".claude-plugin/marketplace.json",
                    "README.md",
                ]
            )
            for line in tree.splitlines():
                metadata, relative = line.split("\t", 1)
                blob = metadata.split()[2]
                installed = Path(entries[0]["installPath"]) / Path(relative)
                verify_file(installed, blob)
                files.append(
                    {
                        "path": relative,
                        "blob": blob,
                        "sha256": self.hash_file(installed),
                    }
                )
        upstream = self.root / ".agents" / "superpowers"
        tracked_upstream = run_cli(["git", "ls-files"], cwd=upstream).splitlines()
        normal = Path.home() / ".claude"
        normal_files = []
        for relative in (
            "settings.json",
            "plugins/installed_plugins.json",
            "plugins/known_marketplaces.json",
        ):
            if (normal / relative).is_file():
                normal_files.append(
                    {"path": relative, "sha256": self.hash_file(normal / relative)}
                )
        preservation = {
            "normalProfile": normal_files,
            "upstreamRegistry": registry[self.upstream_id],
            "upstreamMarketplace": [
                item
                for item in marketplaces
                if item["name"] == self.upstream_id.split("@", 1)[1]
            ],
            "upstreamFiles": [
                {"path": relative, "sha256": self.hash_file(upstream / relative)}
                for relative in tracked_upstream
                if (upstream / relative).is_file()
            ],
            "upstreamHead": run_cli(["git", "rev-parse", "HEAD"], cwd=upstream).strip(),
            "upstreamStatus": run_cli(
                ["git", "status", "--porcelain"], cwd=upstream
            ).splitlines(),
            "sentinel": self.hash_file(
                self.profile / "issue11-preservation-sentinel.txt"
            ),
            "refs": self.command(["git", "show-ref"]).splitlines(),
            "issue": json.loads(
                self.command(
                    [
                        "gh",
                        "issue",
                        "view",
                        "11",
                        "--repo",
                        REPOSITORY,
                        "--json",
                        ISSUE_FIELDS,
                    ]
                )
            ),
        }
        record = {
            "row": row,
            "plugins": plugins,
            "marketplaces": marketplaces,
            "backplaneFiles": files,
            "preservation": preservation,
        }
        write_json(self.work / f"{row}-snapshot.json", record)
        if capture_only:
            print(
                f"{row}: exact source verified; immediate pre-operation state captured",
                flush=True,
            )
            return record
        comparison = self.work / "comparison-baseline.json"
        if row == "lifecycle-baseline":
            if comparison.exists():
                raise ValueError("Do not overwrite an existing lifecycle baseline")
            write_json(comparison, record)
        baseline = compare_to if compare_to is not None else read_json(comparison)
        compare_preservation(baseline["preservation"], preservation)

        def unrelated(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
            return sorted(
                (item for item in items if item["id"] != BACKPLANE),
                key=lambda item: item["id"],
            )

        compare_preservation(unrelated(baseline["plugins"]), unrelated(plugins))
        print(f"{row}: {len(files)} exact source files; preservation PASS", flush=True)
        return record

    @staticmethod
    def hash_file(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest().upper()
```

## lifecycle_helpers_final_dev.py

SHA-256: `86e8f0f2fa83cb8c787c349d75f89896bc8b591c0a6a5bd73f3596d913869dbb`

```python
"""Portable orchestration; no shell, profile fallback, or credential copying."""

from collections.abc import Mapping, Sequence
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any

REPOSITORY = "tvproductions/superpowers-backplane"
BASELINE = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
FIXTURE = "5e01704fcdda13eefeeac52d8892da26e7164ffd"
BACKPLANE = "superpowers-backplane@superpowers-backplane"
ISSUE_FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run_cli(
    arguments: Sequence[str], *, cwd: Path, overrides: Mapping[str, str] | None = None
) -> str:
    environment = dict(os.environ, PYTHONIOENCODING="utf-8")
    environment.update(overrides or {})
    executable = shutil.which(arguments[0])
    if executable is None:
        raise FileNotFoundError(f"Required executable unavailable: {arguments[0]}")
    result = subprocess.run(
        [executable, *arguments[1:]],
        cwd=cwd,
        env=environment,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"{arguments[0]} exited {result.returncode}: {result.stdout}{result.stderr}"
        )
    return result.stdout


def compare_preservation(before: Any, after: Any) -> None:
    if before != after:
        raise ValueError("Preservation mismatch; retain snapshot before repair")


def verify_file(path: Path, expected_blob: str) -> None:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("ascii")
    if (
        hashlib.sha1(header + content, usedforsecurity=False).hexdigest()
        != expected_blob
    ):
        raise ValueError(f"Installed byte mismatch: {path}")


def validate_revision(revision: str) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise ValueError("Use a full lowercase 40-character commit SHA")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


class Harness:
    def __init__(
        self,
        root: Path,
        profile: Path | None = None,
        catalog: Path | None = None,
        output: Path | None = None,
    ):
        self.root = root.resolve(strict=True)
        base_work = self.root / ".sp-bp" / "work" / "issue-11"
        self.work = (output or base_work).resolve()
        self.profile = (profile or base_work / "profile").resolve(strict=True)
        self.catalog = (catalog or base_work / "catalog").resolve()
        self.environment = {"CLAUDE_CONFIG_DIR": str(self.profile)}
        index = int(os.environ.get("GIT_CONFIG_COUNT", "0") or "0")
        self.environment.update(
            {
                "GIT_CONFIG_COUNT": str(index + 1),
                f"GIT_CONFIG_KEY_{index}": f"url.https://github.com/{REPOSITORY}.insteadOf",
                f"GIT_CONFIG_VALUE_{index}": f"git@github.com:{REPOSITORY}",
            }
        )

    def command(self, arguments: Sequence[str]) -> str:
        return run_cli(arguments, cwd=self.root, overrides=self.environment)

    def claude(self, *arguments: str) -> str:
        print(f"CLAUDE_CONFIG_DIR={self.profile}", flush=True)
        output = self.command(["claude", *arguments])
        print(output, end="" if output.endswith("\n") else "\n", flush=True)
        return output

    def source(self, revision: str) -> None:
        validate_revision(revision)
        manifest = self.catalog / ".claude-plugin" / "marketplace.json"
        if self.catalog.exists():
            existing = read_json(manifest)
            entries = existing.get("plugins", [])
            if (
                existing.get("name") != "superpowers-backplane"
                or len(entries) != 1
                or entries[0].get("name") != "superpowers-backplane"
                or entries[0].get("source", {}).get("source") != "github"
                or entries[0].get("source", {}).get("repo") != REPOSITORY
            ):
                raise ValueError(
                    "Occupied catalog is not the verified dedicated Backplane source"
                )
        # Availability is checked before catalog or installed-package mutation.
        available = self.command(
            ["gh", "api", f"repos/{REPOSITORY}/commits/{revision}", "--jq", ".sha"]
        ).strip()
        if available != revision:
            raise ValueError(
                "Source unavailable; retain prior catalog and installation"
            )
        write_json(
            manifest,
            {
                "name": "superpowers-backplane",
                "description": "Pinned Backplane hosted-source catalog",
                "owner": {"name": "tvproductions"},
                "plugins": [
                    {
                        "name": "superpowers-backplane",
                        "description": "Pinned Backplane package",
                        "source": {
                            "source": "github",
                            "repo": REPOSITORY,
                            "sha": revision,
                        },
                    }
                ],
            },
        )

    def discovery(self, row: str, *, absent: bool = False) -> None:
        prompt = (
            "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
            "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
            "and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe "
            "requests only actual skill loading and reporting the three loaded package roots; "
            "it does not request setup, implementation, handoff creation/resume, issue intake "
            "or mutation. Do not create any file. Report any missing skill honestly."
        )
        if absent:
            prompt = (
                "Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. "
                "Then inspect your available Skill tool skill inventory and report whether "
                "superpowers-backplane:managing-superpowers-backlog and "
                "superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to "
                "install anything, read files, create a handoff, or mutate GitHub. Do not invent "
                "a successful load of unavailable skills."
            )
        print(
            f"{row}: fresh Skill-only discovery; CLAUDE_CONFIG_DIR={self.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--tools",
                "Skill",
                "--allowedTools",
                "Skill",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "8",
            ],
            cwd=self.work / "neutral",
            overrides=self.environment,
        )
        (self.work / f"{row}-discovery.jsonl").write_text(
            output, encoding="utf-8", newline="\n"
        )
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError("Fresh discovery session did not succeed")
        calls = []
        for event in events:
            for block in event.get("message", {}).get("content", []):
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    calls.append(block["input"]["skill"])
                if block.get("type") == "tool_result" and block.get("is_error"):
                    raise ValueError("Discovery tool load failed")
        required = ["superpowers:using-superpowers"]
        if not absent:
            required += [
                "superpowers-backplane:managing-superpowers-backlog",
                "superpowers-backplane:managing-superpowers-handoffs",
            ]
        if any(skill not in calls for skill in required):
            raise ValueError("Missing actual Skill tool invocation")
        if absent:
            initialization = next(
                event for event in events if event.get("subtype") == "init"
            )
            if "skills" not in initialization:
                raise ValueError("Native skill inventory unavailable")
            if any(
                "superpowers-backplane" in str(skill)
                for skill in initialization["skills"]
            ):
                raise ValueError("Backplane remains in fresh native skill inventory")
        write_json(
            self.work / f"{row}-discovery-summary.json",
            {
                "row": row,
                "session": result["session_id"],
                "skills": calls,
                "result": result["result"],
                "absent": absent,
            },
        )
        print(f"{row}: discovery PASS; session={result['session_id']}", flush=True)

    def snapshot(
        self,
        row: str,
        revision: str | None,
        version: str | None,
        *,
        capture_only: bool = False,
        compare_to: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        plugins = json.loads(self.command(["claude", "plugin", "list", "--json"]))
        marketplaces = json.loads(
            self.command(["claude", "plugin", "marketplace", "list", "--json"])
        )
        registry = read_json(self.profile / "plugins" / "installed_plugins.json")[
            "plugins"
        ]
        entries = registry.get(BACKPLANE, [])
        files = []
        if revision is None:
            if any(item["id"] == BACKPLANE for item in plugins):
                raise ValueError("Backplane expected absent")
        else:
            if (
                len(entries) != 1
                or entries[0]["gitCommitSha"] != revision
                or entries[0]["version"] != version
            ):
                raise ValueError("Installed revision/version/cardinality mismatch")
            tree = self.command(
                [
                    "git",
                    "ls-tree",
                    "-r",
                    revision,
                    "--",
                    "skills",
                    "plugin.json",
                    ".claude-plugin/plugin.json",
                    ".claude-plugin/marketplace.json",
                    "README.md",
                ]
            )
            for line in tree.splitlines():
                metadata, relative = line.split("\t", 1)
                blob = metadata.split()[2]
                installed = Path(entries[0]["installPath"]) / Path(relative)
                verify_file(installed, blob)
                files.append(
                    {
                        "path": relative,
                        "blob": blob,
                        "sha256": self.hash_file(installed),
                    }
                )
        upstream = self.root / ".agents" / "superpowers"
        tracked_upstream = run_cli(["git", "ls-files"], cwd=upstream).splitlines()
        normal = Path.home() / ".claude"
        normal_files = []
        for relative in (
            "settings.json",
            "plugins/installed_plugins.json",
            "plugins/known_marketplaces.json",
        ):
            if (normal / relative).is_file():
                normal_files.append(
                    {"path": relative, "sha256": self.hash_file(normal / relative)}
                )
        preservation = {
            "normalProfile": normal_files,
            "upstreamRegistry": registry["superpowers@superpowers-dev"],
            "upstreamMarketplace": [
                item for item in marketplaces if item["name"] == "superpowers-dev"
            ],
            "upstreamFiles": [
                {"path": relative, "sha256": self.hash_file(upstream / relative)}
                for relative in tracked_upstream
                if (upstream / relative).is_file()
            ],
            "upstreamHead": run_cli(["git", "rev-parse", "HEAD"], cwd=upstream).strip(),
            "upstreamStatus": run_cli(
                ["git", "status", "--porcelain"], cwd=upstream
            ).splitlines(),
            "sentinel": self.hash_file(
                self.profile / "issue11-preservation-sentinel.txt"
            ),
            "refs": self.command(["git", "show-ref"]).splitlines(),
            "issue": json.loads(
                self.command(
                    [
                        "gh",
                        "issue",
                        "view",
                        "11",
                        "--repo",
                        REPOSITORY,
                        "--json",
                        ISSUE_FIELDS,
                    ]
                )
            ),
        }
        record = {
            "row": row,
            "plugins": plugins,
            "marketplaces": marketplaces,
            "backplaneFiles": files,
            "preservation": preservation,
        }
        write_json(self.work / f"{row}-snapshot.json", record)
        if capture_only:
            print(
                f"{row}: exact source verified; immediate pre-operation state captured",
                flush=True,
            )
            return record
        comparison = self.work / "comparison-baseline.json"
        if row == "lifecycle-baseline":
            if comparison.exists():
                raise ValueError("Do not overwrite an existing lifecycle baseline")
            write_json(comparison, record)
        baseline = compare_to if compare_to is not None else read_json(comparison)
        compare_preservation(baseline["preservation"], preservation)

        def unrelated(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
            return sorted(
                (item for item in items if item["id"] != BACKPLANE),
                key=lambda item: item["id"],
            )

        compare_preservation(unrelated(baseline["plugins"]), unrelated(plugins))
        print(f"{row}: {len(files)} exact source files; preservation PASS", flush=True)
        return record

    @staticmethod
    def hash_file(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest().upper()
```

## lifecycle_helpers_replay.py

SHA-256: `1aa4814c81a49b52490f31520867b16f7be54861d7e57cdb3f7d529de6c15110`

```python
"""Portable orchestration; no shell, profile fallback, or credential copying."""

from collections.abc import Mapping, Sequence
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any

REPOSITORY = "tvproductions/superpowers-backplane"
BASELINE = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
FIXTURE = "5e01704fcdda13eefeeac52d8892da26e7164ffd"
BACKPLANE = "superpowers-backplane@superpowers-backplane"
ISSUE_FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run_cli(
    arguments: Sequence[str], *, cwd: Path, overrides: Mapping[str, str] | None = None
) -> str:
    environment = dict(os.environ, PYTHONIOENCODING="utf-8")
    environment.update(overrides or {})
    executable = shutil.which(arguments[0])
    if executable is None:
        raise FileNotFoundError(f"Required executable unavailable: {arguments[0]}")
    result = subprocess.run(
        [executable, *arguments[1:]],
        cwd=cwd,
        env=environment,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"{arguments[0]} exited {result.returncode}: {result.stdout}{result.stderr}"
        )
    return result.stdout


def compare_preservation(before: Any, after: Any) -> None:
    if before != after:
        raise ValueError("Preservation mismatch; retain snapshot before repair")


def verify_file(path: Path, expected_blob: str) -> None:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("ascii")
    if (
        hashlib.sha1(header + content, usedforsecurity=False).hexdigest()
        != expected_blob
    ):
        raise ValueError(f"Installed byte mismatch: {path}")


def validate_revision(revision: str) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise ValueError("Use a full lowercase 40-character commit SHA")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


class Harness:
    def __init__(
        self,
        root: Path,
        profile: Path | None = None,
        catalog: Path | None = None,
        output: Path | None = None,
    ):
        self.root = root.resolve(strict=True)
        base_work = self.root / ".sp-bp" / "work" / "issue-11"
        self.work = (output or base_work).resolve()
        self.profile = (profile or base_work / "profile").resolve(strict=True)
        self.catalog = (catalog or base_work / "catalog").resolve()
        self.environment = {"CLAUDE_CONFIG_DIR": str(self.profile)}
        index = int(os.environ.get("GIT_CONFIG_COUNT", "0") or "0")
        self.environment.update(
            {
                "GIT_CONFIG_COUNT": str(index + 1),
                f"GIT_CONFIG_KEY_{index}": f"url.https://github.com/{REPOSITORY}.insteadOf",
                f"GIT_CONFIG_VALUE_{index}": f"git@github.com:{REPOSITORY}",
            }
        )

    def command(self, arguments: Sequence[str]) -> str:
        return run_cli(arguments, cwd=self.root, overrides=self.environment)

    def claude(self, *arguments: str) -> str:
        print(f"CLAUDE_CONFIG_DIR={self.profile}", flush=True)
        output = self.command(["claude", *arguments])
        print(output, end="" if output.endswith("\n") else "\n", flush=True)
        return output

    def source(self, revision: str) -> None:
        validate_revision(revision)
        manifest = self.catalog / ".claude-plugin" / "marketplace.json"
        if self.catalog.exists():
            existing = read_json(manifest)
            entries = existing.get("plugins", [])
            if (
                existing.get("name") != "superpowers-backplane"
                or len(entries) != 1
                or entries[0].get("name") != "superpowers-backplane"
                or entries[0].get("source", {}).get("source") != "github"
                or entries[0].get("source", {}).get("repo") != REPOSITORY
            ):
                raise ValueError(
                    "Occupied catalog is not the verified dedicated Backplane source"
                )
        # Availability is checked before catalog or installed-package mutation.
        available = self.command(
            ["gh", "api", f"repos/{REPOSITORY}/commits/{revision}", "--jq", ".sha"]
        ).strip()
        if available != revision:
            raise ValueError(
                "Source unavailable; retain prior catalog and installation"
            )
        write_json(
            manifest,
            {
                "name": "superpowers-backplane",
                "description": "Pinned Backplane hosted-source catalog",
                "owner": {"name": "tvproductions"},
                "plugins": [
                    {
                        "name": "superpowers-backplane",
                        "description": "Pinned Backplane package",
                        "source": {
                            "source": "github",
                            "repo": REPOSITORY,
                            "sha": revision,
                        },
                    }
                ],
            },
        )

    def discovery(self, row: str, *, absent: bool = False) -> None:
        prompt = (
            "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
            "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
            "and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe "
            "requests only actual skill loading and reporting the three loaded package roots; "
            "it does not request setup, implementation, handoff creation/resume, issue intake "
            "or mutation. Do not create any file. Report any missing skill honestly."
        )
        if absent:
            prompt = (
                "Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. "
                "Then inspect your available Skill tool skill inventory and report whether "
                "superpowers-backplane:managing-superpowers-backlog and "
                "superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to "
                "install anything, read files, create a handoff, or mutate GitHub. Do not invent "
                "a successful load of unavailable skills."
            )
        print(
            f"{row}: fresh Skill-only discovery; CLAUDE_CONFIG_DIR={self.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--tools",
                "Skill",
                "--allowedTools",
                "Skill",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "8",
            ],
            cwd=self.work / "neutral",
            overrides=self.environment,
        )
        (self.work / f"{row}-discovery.jsonl").write_text(
            output, encoding="utf-8", newline="\n"
        )
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError("Fresh discovery session did not succeed")
        calls = []
        for event in events:
            for block in event.get("message", {}).get("content", []):
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    calls.append(block["input"]["skill"])
                if block.get("type") == "tool_result" and block.get("is_error"):
                    raise ValueError("Discovery tool load failed")
        required = ["superpowers:using-superpowers"]
        if not absent:
            required += [
                "superpowers-backplane:managing-superpowers-backlog",
                "superpowers-backplane:managing-superpowers-handoffs",
            ]
        if any(skill not in calls for skill in required):
            raise ValueError("Missing actual Skill tool invocation")
        if absent:
            initialization = next(
                event for event in events if event.get("subtype") == "init"
            )
            if "skills" not in initialization:
                raise ValueError("Native skill inventory unavailable")
            if any(
                "superpowers-backplane" in str(skill)
                for skill in initialization["skills"]
            ):
                raise ValueError("Backplane remains in fresh native skill inventory")
        write_json(
            self.work / f"{row}-discovery-summary.json",
            {
                "row": row,
                "session": result["session_id"],
                "skills": calls,
                "result": result["result"],
                "absent": absent,
            },
        )
        print(f"{row}: discovery PASS; session={result['session_id']}", flush=True)

    def snapshot(
        self, row: str, revision: str | None, version: str | None
    ) -> dict[str, Any]:
        plugins = json.loads(self.command(["claude", "plugin", "list", "--json"]))
        marketplaces = json.loads(
            self.command(["claude", "plugin", "marketplace", "list", "--json"])
        )
        registry = read_json(self.profile / "plugins" / "installed_plugins.json")[
            "plugins"
        ]
        entries = registry.get(BACKPLANE, [])
        files = []
        if revision is None:
            if any(item["id"] == BACKPLANE for item in plugins):
                raise ValueError("Backplane expected absent")
        else:
            if (
                len(entries) != 1
                or entries[0]["gitCommitSha"] != revision
                or entries[0]["version"] != version
            ):
                raise ValueError("Installed revision/version/cardinality mismatch")
            tree = self.command(
                [
                    "git",
                    "ls-tree",
                    "-r",
                    revision,
                    "--",
                    "skills",
                    "plugin.json",
                    ".claude-plugin/plugin.json",
                    ".claude-plugin/marketplace.json",
                    "README.md",
                ]
            )
            for line in tree.splitlines():
                metadata, relative = line.split("\t", 1)
                blob = metadata.split()[2]
                installed = Path(entries[0]["installPath"]) / Path(relative)
                verify_file(installed, blob)
                files.append(
                    {
                        "path": relative,
                        "blob": blob,
                        "sha256": self.hash_file(installed),
                    }
                )
        upstream = self.root / ".agents" / "superpowers"
        tracked_upstream = run_cli(["git", "ls-files"], cwd=upstream).splitlines()
        normal = Path.home() / ".claude"
        normal_files = []
        for relative in (
            "settings.json",
            "plugins/installed_plugins.json",
            "plugins/known_marketplaces.json",
        ):
            if (normal / relative).is_file():
                normal_files.append(
                    {"path": relative, "sha256": self.hash_file(normal / relative)}
                )
        preservation = {
            "normalProfile": normal_files,
            "upstreamRegistry": registry["superpowers@superpowers-dev"],
            "upstreamMarketplace": [
                item for item in marketplaces if item["name"] == "superpowers-dev"
            ],
            "upstreamFiles": [
                {"path": relative, "sha256": self.hash_file(upstream / relative)}
                for relative in tracked_upstream
                if (upstream / relative).is_file()
            ],
            "upstreamHead": run_cli(["git", "rev-parse", "HEAD"], cwd=upstream).strip(),
            "upstreamStatus": run_cli(
                ["git", "status", "--porcelain"], cwd=upstream
            ).splitlines(),
            "sentinel": self.hash_file(
                self.profile / "issue11-preservation-sentinel.txt"
            ),
            "refs": self.command(["git", "show-ref"]).splitlines(),
            "issue": json.loads(
                self.command(
                    [
                        "gh",
                        "issue",
                        "view",
                        "11",
                        "--repo",
                        REPOSITORY,
                        "--json",
                        ISSUE_FIELDS,
                    ]
                )
            ),
        }
        record = {
            "row": row,
            "plugins": plugins,
            "marketplaces": marketplaces,
            "backplaneFiles": files,
            "preservation": preservation,
        }
        write_json(self.work / f"{row}-snapshot.json", record)
        comparison = self.work / "comparison-baseline.json"
        if row == "lifecycle-baseline":
            if comparison.exists():
                raise ValueError("Do not overwrite an existing lifecycle baseline")
            write_json(comparison, record)
        baseline = read_json(comparison)
        compare_preservation(baseline["preservation"], preservation)

        def unrelated(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
            return sorted(
                (item for item in items if item["id"] != BACKPLANE),
                key=lambda item: item["id"],
            )

        compare_preservation(unrelated(baseline["plugins"]), unrelated(plugins))
        print(f"{row}: {len(files)} exact source files; preservation PASS", flush=True)
        return record

    @staticmethod
    def hash_file(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest().upper()
```

## live_native_setup.py

SHA-256: `74e82d6d1d53b4167876be8e10b547d1fab2ea62b0b8a53a041e98a12d8471d8`

```python
"""Replay the Claude guide in owned fixtures and the authorized disposable profile."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any

ROOT = Path.cwd().resolve(strict=True)
WORK = ROOT / ".sp-bp/work/issue-11"
PROFILE = (ROOT / ".sp-bp/work/issue-19/profile").resolve(strict=True)
PARENT = WORK / "fixtures/clean-install"
CLONE = PARENT / "superpowers-backplane"
NEUTRAL = WORK / "native-neutral"
CANDIDATE = "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"
OUT = ROOT / "tests/scenarios/2026-10-26-issue-11-native-setup.json"
env = dict(os.environ, CLAUDE_CONFIG_DIR=str(PROFILE), PYTHONIOENCODING="utf-8")
receipt: dict[str, Any] = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "candidate": CANDIDATE,
    "profile": str(PROFILE),
    "result": "IN PROGRESS",
    "commands": [],
    "snapshots": [],
}


def save():
    OUT.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def run(args, *, cwd=ROOT, timeout=120):
    executable = shutil.which(args[0])
    assert executable
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=cwd,
        env=env,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        check=False,
    )
    receipt["commands"].append(
        {
            "argv": args,
            "cwd": str(cwd),
            "profile": str(PROFILE),
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    save()
    assert result.returncode == 0, f"{args[:3]} failed; see preserved receipt"
    return result.stdout


def snapshot(name):
    plugins = json.loads(run(["claude", "plugin", "list", "--json"]))
    markets = json.loads(run(["claude", "plugin", "marketplace", "list", "--json"]))
    protected_files = [
        ROOT / ".agents/superpowers/.claude-plugin/plugin.json",
        ROOT / ".agents/superpowers/skills/using-superpowers/SKILL.md",
        Path.home() / ".claude/settings.json",
        Path.home() / ".claude/plugins/installed_plugins.json",
        Path.home() / ".claude/plugins/known_marketplaces.json",
    ]
    protected = {
        "unrelated_plugins": [
            p
            for p in plugins
            if p["id"] != "superpowers-backplane@superpowers-backplane"
        ],
        "unrelated_marketplaces": [
            m for m in markets if m["name"] != "superpowers-backplane"
        ],
        "files": {
            str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in protected_files
            if p.is_file()
        },
        "upstream_head": run(
            ["git", "-C", str(ROOT / ".agents/superpowers"), "rev-parse", "HEAD"]
        ).strip(),
        "upstream_status": run(
            ["git", "-C", str(ROOT / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }
    value = {
        "name": name,
        "plugins": plugins,
        "marketplaces": markets,
        "protected": protected,
    }
    receipt["snapshots"].append(value)
    save()
    return value


assert (
    Path(run(["git", "rev-parse", "--show-toplevel"]).strip()).resolve(strict=True)
    == ROOT
)
assert run(["git", "check-ignore", ".sp-bp/work/issue-11/fixtures/clean-install"])
assert not PARENT.exists(), "Use an unused owned parent for exact guide replay"
PARENT.mkdir(parents=True)
NEUTRAL.mkdir(exist_ok=True)
assert PARENT.resolve(strict=True).is_relative_to(WORK.resolve(strict=True))
claude_executable = shutil.which("claude")
assert claude_executable is not None
auth = json.loads(
    subprocess.check_output(
        [claude_executable, "auth", "status", "--json"],
        cwd=ROOT,
        env=env,
        text=True,
        encoding="utf-8",
    )
)
assert auth.get("loggedIn") is True
receipt["auth"] = {
    "loggedIn": True,
    "authMethod": auth.get("authMethod"),
    "account_fields": "[REDACTED]",
}
before = snapshot("before-guide-clone")
assert before["protected"]["issue11"]["labels"][0]["name"] == "backplane:active"
guide = (ROOT / "docs/installing-claude-code.md").read_text(encoding="utf-8")
blocks = re.findall(r"^```powershell\n(.*?)^```", guide, re.M | re.S)
assert len(blocks) == 4
code = blocks[0].replace(
    "Read-Host 'Reviewed 40-character Backplane commit'", f"'{CANDIDATE}'"
)
guard = """
$fixtureRoot = (git -C $backplaneCheckout rev-parse --show-toplevel).Trim()
if ($LASTEXITCODE -ne 0 -or [IO.Path]::GetFullPath($fixtureRoot) -ine [IO.Path]::GetFullPath($backplaneCheckout)) { throw 'Fixture identity mismatch before checkout' }
$fixtureOrigin = (git -C $backplaneCheckout remote get-url origin).Trim()
$fixtureHead = (git -C $backplaneCheckout rev-parse HEAD).Trim()
$fixtureRecord = @{root=$fixtureRoot; origin=$fixtureOrigin; starting_revision=$fixtureHead; purpose='issue-11 exact clean-install guide replay'} | ConvertTo-Json -Compress
Add-Content -LiteralPath $env:SP_BP_LEDGER -Value ('- Guide fixture registered before checkout: ' + $fixtureRecord) -Encoding utf8
"""
anchor = "if ($LASTEXITCODE -ne 0) { throw 'Backplane clone failed' }"
assert code.count(anchor) == 1
code = code.replace(anchor, anchor + "\n" + guard)
script = WORK / "guide-clean-install.ps1"
script.write_text(code, encoding="utf-8", newline="\n")
env["SP_BP_LEDGER"] = str(WORK / "progress.md")
receipt["guide_block"] = {
    "original_sha256": hashlib.sha256(blocks[0].encode("utf-8")).hexdigest(),
    "executed_sha256": hashlib.sha256(code.encode("utf-8")).hexdigest(),
    "adaptation": "Supply reviewed SHA as noninteractive Read-Host input; add fixture identity/ledger guard before checkout. All guide commands and conditions preserved.",
}
save()
run(["pwsh", "-NoProfile", "-File", str(script)], cwd=PARENT, timeout=180)
assert Path(
    run(["git", "-C", str(CLONE), "rev-parse", "--show-toplevel"]).strip()
).resolve(strict=True) == CLONE.resolve(strict=True)
assert run(["git", "-C", str(CLONE), "rev-parse", "HEAD"]).strip() == CANDIDATE
assert not run(["git", "-C", str(CLONE), "status", "--porcelain=v1"]).strip()
assert not (CLONE / ".git/objects/info/alternates").exists()
receipt["clone_verified"] = True
catalog = ROOT / ".sp-bp/work/issue-19/catalog/.claude-plugin/marketplace.json"
old_catalog = json.loads(catalog.read_text(encoding="utf-8"))
assert old_catalog["name"] == "superpowers-backplane"
assert [p["name"] for p in old_catalog["plugins"]] == ["superpowers-backplane"]
receipt["previous_catalog"] = old_catalog
save()
run(
    [
        "claude",
        "plugin",
        "uninstall",
        "superpowers-backplane@superpowers-backplane",
        "--scope",
        "user",
    ]
)
uninstalled = snapshot("backplane-absent-before-clean-install")
assert all(
    p["id"] != "superpowers-backplane@superpowers-backplane"
    for p in uninstalled["plugins"]
)
assert uninstalled["protected"] == before["protected"]
run(["claude", "plugin", "marketplace", "remove", "superpowers-backplane"])
removed = snapshot("dedicated-catalog-removed")
assert removed["protected"] == before["protected"]
run(["claude", "plugin", "marketplace", "add", str(CLONE)])
run(
    [
        "claude",
        "plugin",
        "install",
        "superpowers-backplane@superpowers-backplane",
        "--scope",
        "user",
    ]
)
installed = snapshot("clean-install-candidate")
assert installed["protected"] == before["protected"]
backplane = [
    p
    for p in installed["plugins"]
    if p["id"] == "superpowers-backplane@superpowers-backplane"
]
assert len(backplane) == 1 and backplane[0]["version"] == "0.1.0"
installed_root = Path(
    backplane[0].get("readFromFolder") or backplane[0]["installPath"]
).resolve(strict=True)
source_listing = run(
    ["git", "ls-tree", "-r", CANDIDATE, "--", ".claude-plugin", "skills", "plugin.json"]
)
receipt["installed_files"] = []
for line in source_listing.splitlines():
    meta, name = line.split("\t", 1)
    expected = meta.split()[2]
    content = (installed_root / name).read_bytes()
    actual = hashlib.sha1(
        f"blob {len(content)}\0".encode("ascii") + content, usedforsecurity=False
    ).hexdigest()
    assert actual == expected, name
    receipt["installed_files"].append(
        {"path": name, "expected_blob": expected, "actual_blob": actual}
    )
assert len(receipt["installed_files"]) == 20
prompt = (
    "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
    "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
    "and superpowers-backplane:managing-superpowers-handoffs, in that order. "
    "Only load these skills and report their actual package roots. Do not run setup, "
    "create/resume a handoff, read or mutate issues, or create any file."
)
stream = run(
    [
        "claude",
        "-p",
        prompt,
        "--tools",
        "Skill",
        "--allowedTools",
        "Skill",
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-turns",
        "8",
    ],
    cwd=NEUTRAL,
    timeout=240,
)
(WORK / "native-discovery.jsonl").write_text(stream, encoding="utf-8", newline="\n")
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
assert result.get("subtype") == "success" and not result.get("is_error"), result
calls = []
tool_results = []
for event in events:
    for block in event.get("message", {}).get("content", []):
        if block.get("type") == "tool_use" and block.get("name") == "Skill":
            calls.append(block["input"]["skill"])
        if block.get("type") == "tool_result":
            assert not block.get("is_error"), block
            tool_results.append(block)
required = [
    "superpowers:using-superpowers",
    "superpowers-backplane:managing-superpowers-backlog",
    "superpowers-backplane:managing-superpowers-handoffs",
]
assert all(skill in calls for skill in required)
after = snapshot("after-fresh-discovery")
assert after["protected"] == before["protected"]
receipt.update(
    result="PASS",
    scope="Current clean installation and fresh independent skill discovery; full setup/failure matrix remains separate",
    skill_calls=calls,
    skill_tool_results=tool_results,
    session_id=result.get("session_id"),
    host_version=run(["claude", "--version"]).strip(),
    gh_version=run(["gh", "--version"]).splitlines()[0],
)
save()
print(
    json.dumps(
        {
            "result": receipt["result"],
            "clone": str(CLONE),
            "candidate": CANDIDATE,
            "installed_files": len(receipt["installed_files"]),
            "skill_calls": calls,
            "protected_state_preserved": True,
            "session_id": receipt["session_id"],
        },
        indent=2,
    )
)
```

## login_setup_profile.py

SHA-256: `f4dbb8fcdd0ee575ef9b853c1311fb96a4654d0940161c313f3b977ff96a7038`

```python
"""Interactive sign-in for the isolated setup-test profile; run by the operator."""

import os
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
profile = (root / ".sp-bp/work/issue-11/setup-profile").resolve(strict=True)
assert profile.is_relative_to(root / ".sp-bp/work/issue-11")
executable = shutil.which("claude")
assert executable is not None
print(f"Signing in only this disposable test profile: {profile}", flush=True)
environment = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile))
raise SystemExit(
    subprocess.call(
        [executable, "auth", "login"], cwd=root, env=environment, shell=False
    )
)
```

## native_failure_controls.py

SHA-256: `825fddb83cc12d2e13a8034d6ea41c99550b0f707b9facf82f9d632d020f563e`

```python
"""Run native versionless/duplicate fixtures and remove only their owned entries."""

import json
import os
from pathlib import Path
import shutil
import subprocess

import failure_probes

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = work / "setup-profile"
env = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile))
commands = []


def native(*args):
    executable = shutil.which("claude")
    assert executable is not None
    result = subprocess.run(
        [executable, *args],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        check=False,
    )
    commands.append(
        {
            "argv": ["claude", *args],
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    assert result.returncode == 0, commands[-1]
    return result.stdout


failure_probes.ATTEMPT = "-current"
controls = []
for case, directory, marketplace, plugin in (
    (
        "versionless-package",
        "versionless-upstream",
        "versionless-superpowers",
        "superpowers",
    ),
    (
        "duplicate-backplane",
        "duplicate-backplane",
        "backplane-conflict",
        "superpowers-backplane",
    ),
):
    before = json.loads(native("plugin", "list", "--json"))
    markets = json.loads(native("plugin", "marketplace", "list", "--json"))
    assert not any(m["name"] == marketplace for m in markets)
    native("plugin", "marketplace", "add", str(work / "fixtures" / directory))
    native("plugin", "install", f"{plugin}@{marketplace}", "--scope", "user")
    staged = json.loads(native("plugin", "list", "--json"))
    assert any(p["id"] == f"{plugin}@{marketplace}" for p in staged)
    if case == "duplicate-backplane":
        assert (
            sum(
                p["id"].startswith("superpowers-backplane@") and p.get("enabled")
                for p in staged
            )
            == 2
        )
    failure_probes.probe(case)
    native("plugin", "uninstall", f"{plugin}@{marketplace}", "--scope", "user")
    native("plugin", "marketplace", "remove", marketplace)
    after = json.loads(native("plugin", "list", "--json"))
    assert before == after, "Fixture cleanup changed another installed plugin"
    controls.append(
        {
            "case": case,
            "before": before,
            "staged": staged,
            "after": after,
            "exact_fixture_removed": f"{plugin}@{marketplace}",
            "other_plugins_preserved": True,
        }
    )
(root / "tests/scenarios/2026-10-26-issue-11-native-failure-controls.json").write_text(
    json.dumps(
        {
            "result": "PASS",
            "profile": str(profile),
            "controls": controls,
            "commands": commands,
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    "PASS: actual native versionless and duplicate fixtures observed; only fixture entries removed"
)
```

## native_setup_probe.py

SHA-256: `f8418a2fdc0d4c62600963b7a4fd399c482163fa0ae096250e37a60e6eed35ed`

```python
"""Observe the actual installed native setup workflow in a read-only session."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = (root / ".sp-bp/work/issue-19/profile").resolve(strict=True)
environment = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile), PYTHONIOENCODING="utf-8")
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run(args, *, cwd=root, timeout=90):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=environment,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def protected():
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "profile_files": {
            str(p.relative_to(profile)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                profile / "settings.json",
                profile / "plugins/installed_plugins.json",
                profile / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "upstream_head": run(
            ["git", "-C", str(root / ".agents/superpowers"), "rev-parse", "HEAD"]
        ),
        "upstream_status": run(
            ["git", "-C", str(root / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }


before = protected()
prompt = (
    "Set up Superpowers Backplane in this Claude Code session. "
    "The target repository is tvproductions/superpowers-backplane and existing issue is #11. "
    "Use the installed managing-superpowers-backlog skill and its installation reference. "
    "Both native packages already exist; this is the existing-native-upstream mode. "
    "Verify their actual independent roots, source/version or commit, one effective Backplane, "
    "required upstream skills, and gh authentication/full native issue intake/label and closure help. "
    "Adopt existing packages in place. This is strictly read-only: do not install, update, remove, "
    "edit any file, create a plan or handoff, or mutate GitHub. Report unresolved checks honestly. "
    "Separate fresh direct loads of all three skills were observed after this installation; "
    "do not claim to have rerun those separate sessions. Use only read-only commands."
)
allow = [
    "Skill",
    "Read",
    "Bash(gh auth status)",
    "Bash(gh issue view *)",
    "Bash(gh issue edit --help)",
    "Bash(gh issue close --help)",
    "Bash(claude plugin list *)",
    "Bash(claude plugin marketplace list *)",
    "Bash(claude --version)",
    "Bash(gh --version)",
    "Bash(git -C * remote get-url origin)",
    "Bash(git -C * rev-parse *)",
    "Bash(git -C * status *)",
    "Bash(git remote get-url origin)",
    "Bash(git rev-parse *)",
    "Bash(git status *)",
]
arguments = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash",
    "--allowedTools",
    *allow,
    "--permission-mode",
    "plan",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "32",
]
stream = run(arguments, cwd=work / "native-neutral", timeout=300)
(work / "native-setup-workflow.jsonl").write_text(
    stream, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
calls: list[dict[str, Any]] = []
responses = []
for event in events:
    for block in event.get("message", {}).get("content", []):
        if block.get("type") == "tool_use":
            calls.append(
                {"name": block["name"], "input": block["input"], "id": block["id"]}
            )
        if block.get("type") == "tool_result":
            responses.append(block)
after = protected()
assert before == after, "Setup changed protected state; preserve before repair"
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "prompt": prompt,
    "argv": arguments,
    "profile": str(profile),
    "before": before,
    "after": after,
    "protected_state_preserved": True,
    "tool_calls": calls,
    "tool_results": responses,
    "host_result": result,
    "result": "UNSCORED; inspect actual tool results against setup contract",
    "raw_stream_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
}
(root / "tests/scenarios/2026-10-26-issue-11-native-setup-workflow.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "subtype": result.get("subtype"),
            "is_error": result.get("is_error"),
            "session_id": result.get("session_id"),
            "tools": len(calls),
            "protected_state_preserved": True,
            "report": result.get("result"),
        },
        indent=2,
    )
)
```

## native_setup_probe2.py

SHA-256: `36d4c20bf36d8d2cb36e1eca6a932bf784673454757b1365df51206d3c0d4578`

```python
"""Observe the actual installed native setup workflow in a read-only session."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = (root / ".sp-bp/work/issue-19/profile").resolve(strict=True)
environment = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile), PYTHONIOENCODING="utf-8")
captures = work / "native-setup-captures-2"
assert not captures.exists(), "Use an unused owned capture directory"
captures.mkdir()
for variable in ("TMPDIR", "TMP", "TEMP"):
    environment[variable] = str(captures.resolve())
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run(args, *, cwd=root, timeout=90):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=environment,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def protected():
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "profile_files": {
            str(p.relative_to(profile)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                profile / "settings.json",
                profile / "plugins/installed_plugins.json",
                profile / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "upstream_head": run(
            ["git", "-C", str(root / ".agents/superpowers"), "rev-parse", "HEAD"]
        ),
        "upstream_status": run(
            ["git", "-C", str(root / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }


before = protected()
prompt = (
    "Set up Superpowers Backplane in this Claude Code session. "
    "The target repository is tvproductions/superpowers-backplane and existing issue is #11. "
    "Use the installed managing-superpowers-backlog skill and its installation reference. "
    "Both native packages already exist; this is the existing-native-upstream mode. "
    "Verify their actual independent roots, source/version or commit, one effective Backplane, "
    "required upstream skills, and gh authentication/full native issue intake/label and closure help. "
    "Adopt existing packages in place. Do not install, update, remove, edit user or package files, "
    "create a plan or handoff, or mutate GitHub. Report unresolved checks honestly. "
    f"If you need to capture command output, create files only inside this pre-created owned directory: {captures}. "
    "Never use hardcoded /tmp/i11 files, enumerate environment variables, or read authentication secrets. "
    f"The intended profile is {profile}; inspect only its plugin inventory/metadata and the two verified package sources. "
    "Use claude plugin list --json and claude plugin marketplace list --json; do not inspect unrelated profiles or orphaned cache contents. "
    "Separate fresh direct loads of all three skills were observed after this installation; "
    "do not claim to have rerun those separate sessions. Use only read-only commands."
)
allow = [
    "Skill",
    "Read",
    "Bash(gh auth status)",
    "Bash(gh issue view *)",
    "Bash(gh issue edit --help)",
    "Bash(gh issue close --help)",
    "Bash(claude plugin list *)",
    "Bash(claude plugin marketplace list *)",
    "Bash(claude --version)",
    "Bash(gh --version)",
    "Bash(git -C * remote get-url origin)",
    "Bash(git -C * rev-parse *)",
    "Bash(git -C * status *)",
    "Bash(git remote get-url origin)",
    "Bash(git rev-parse *)",
    "Bash(git status *)",
]
arguments = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash",
    "--allowedTools",
    *allow,
    "--disallowedTools",
    "Bash(*env*)",
    "Bash(*printenv*)",
    "--permission-mode",
    "plan",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "32",
]
stream = run(arguments, cwd=work / "native-neutral", timeout=300)
(work / "native-setup-workflow-2.jsonl").write_text(
    stream, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
calls: list[dict[str, Any]] = []
responses = []
for event in events:
    for block in event.get("message", {}).get("content", []):
        if block.get("type") == "tool_use":
            calls.append(
                {"name": block["name"], "input": block["input"], "id": block["id"]}
            )
        if block.get("type") == "tool_result":
            responses.append(block)
after = protected()
assert before == after, "Setup changed protected state; preserve before repair"
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "prompt": prompt,
    "argv": arguments,
    "profile": str(profile),
    "before": before,
    "after": after,
    "protected_state_preserved": True,
    "tool_calls": calls,
    "tool_results": responses,
    "host_result": result,
    "result": "UNSCORED; inspect actual tool results against setup contract",
    "raw_stream_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
}
(root / "tests/scenarios/2026-10-26-issue-11-native-setup-workflow-2.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "subtype": result.get("subtype"),
            "is_error": result.get("is_error"),
            "session_id": result.get("session_id"),
            "tools": len(calls),
            "protected_state_preserved": True,
            "report": result.get("result"),
        },
        indent=2,
    )
)
```

## prepare_failure_fixtures.py

SHA-256: `3d0c6e9a9418aaa898cbc9746f783c59015dbfd2d9385c3a1b69cf9f304eab1a`

```python
"""Prepare independent immutable-source copies for the approved rejection tests."""

import json
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
fixtures = work / "fixtures"
upstream = root / ".agents/superpowers"
commands = []


def git(*args):
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    commands.append(
        {
            "argv": ["git", *args],
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    assert result.returncode == 0, commands[-1]
    return result.stdout.strip()


assert Path(git("rev-parse", "--show-toplevel")).resolve(strict=True) == root
before = {
    "head": git("-C", str(upstream), "rev-parse", "HEAD"),
    "status": git("-C", str(upstream), "status", "--porcelain=v1"),
}
assert before["head"] == "2ce8aa15d05bd57213e6f746f953aafb7ded7a8b"
for name in (
    "upstream-clean",
    "upstream-dirty",
    "upstream-lookalike",
    "upstream-missing-skill",
):
    target = fixtures / name
    assert not target.exists(), "Preserve occupied paths"
    assert target.parent.resolve(strict=True).is_relative_to(work.resolve(strict=True))
    git("clone", "--no-hardlinks", str(upstream), str(target))
    assert Path(git("-C", str(target), "rev-parse", "--show-toplevel")).resolve(
        strict=True
    ) == target.resolve(strict=True)
    assert not (target / ".git/objects/info/alternates").exists()
    with (work / "progress.md").open("a", encoding="utf-8", newline="\n") as ledger:
        ledger.write(
            "- Failure fixture identity before mutations: "
            + json.dumps(
                {
                    "root": str(target.resolve()),
                    "starting_revision": git("-C", str(target), "rev-parse", "HEAD"),
                    "initial_origin": git(
                        "-C", str(target), "remote", "get-url", "origin"
                    ),
                    "purpose": name,
                }
            )
            + "\n"
        )
    origin = (
        "https://github.com/obrafake/superpowers.git"
        if name == "upstream-lookalike"
        else "https://github.com/obra/superpowers.git"
    )
    git("-C", str(target), "remote", "set-url", "origin", origin)
    if name == "upstream-dirty":
        path = target / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\nIssue11 deliberate dirty fixture.\n",
            encoding="utf-8",
            newline="\n",
        )
    if name == "upstream-missing-skill":
        (target / "skills/writing-plans/SKILL.md").unlink()
versionless = fixtures / "versionless-upstream"
assert not versionless.exists()
shutil.copytree(
    fixtures / "upstream-clean", versionless, ignore=shutil.ignore_patterns(".git")
)
for name in ("plugin.json", "marketplace.json"):
    path = versionless / ".claude-plugin" / name
    value = json.loads(path.read_text(encoding="utf-8"))
    value.pop("version", None)
    if name == "marketplace.json":
        value["name"] = "versionless-superpowers"
        for plugin in value["plugins"]:
            plugin.pop("version", None)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
duplicate = fixtures / "duplicate-backplane"
assert not duplicate.exists()
source = fixtures / "clean-install/superpowers-backplane"
shutil.copytree(source, duplicate, ignore=shutil.ignore_patterns(".git"))
path = duplicate / ".claude-plugin/marketplace.json"
value = json.loads(path.read_text(encoding="utf-8"))
value["name"] = "backplane-conflict"
path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
occupied = fixtures / "occupied-destination"
assert not occupied.exists()
occupied.mkdir()
(occupied / "sentinel.txt").write_text(
    "Owned occupied-path preservation fixture\n", encoding="utf-8", newline="\n"
)
after = {
    "head": git("-C", str(upstream), "rev-parse", "HEAD"),
    "status": git("-C", str(upstream), "status", "--porcelain=v1"),
}
assert before == after
(root / "tests/scenarios/2026-10-26-issue-11-failure-fixtures.json").write_text(
    json.dumps(
        {
            "commands": commands,
            "upstream_before": before,
            "upstream_after": after,
            "source_preserved": True,
            "fixture_names": [
                "upstream-clean",
                "upstream-dirty",
                "upstream-lookalike",
                "upstream-missing-skill",
                "versionless-upstream",
                "duplicate-backplane",
                "occupied-destination",
            ],
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print("PASS: seven owned failure fixtures prepared; protected upstream unchanged")
```

## prepare_gh_shims.py

SHA-256: `96914a082bf1304c4ad40bca89759f48ebdd612585541be4309d43c66e91e110`

```python
"""Prove the four gh capability fixtures on Windows and Git Bash."""

import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
shim = work / "gh-shims"
assert not shim.exists()
shim.mkdir()
uv = shutil.which("uv")
real_gh = shutil.which("gh")
assert uv and real_gh
stub = work / "gh_stub.py"
shell = (
    '#!/usr/bin/env bash\nexec "'
    + uv.replace("\\", "/")
    + '" --directory "'
    + root.as_posix()
    + '" run --no-project python "'
    + stub.as_posix()
    + '" "$@"\n'
)
(shim / "gh").write_text(shell, encoding="utf-8", newline="\n")
(shim / "gh.cmd").write_text(
    '@echo off\r\n"'
    + uv
    + '" --directory "'
    + str(root)
    + '" run --no-project python "'
    + str(stub)
    + '" %*\r\n',
    encoding="utf-8",
    newline="",
)
bash = Path("C:/Program Files/Git/bin/bash.exe")
assert bash.is_file()
checks = []
for case in ("auth", "intake", "labels", "closure"):
    env = dict(
        os.environ,
        SP_BP_GH_FAILURE=case,
        SP_BP_REAL_GH=real_gh,
        PATH=str(shim) + os.pathsep + os.environ["PATH"],
    )
    for name, args in {
        "auth": ["auth", "status"],
        "intake": [
            "issue",
            "view",
            "11",
            "--repo",
            "tvproductions/superpowers-backplane",
            "--json",
            "number,issueType",
        ],
        "labels": ["issue", "edit", "--help"],
        "closure": ["issue", "close", "--help"],
    }.items():
        result = subprocess.run(
            [uv, "run", "--no-project", "python", str(stub), *args],
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            shell=False,
            check=False,
        )
        expected = 1 if case == name and case in ("auth", "intake") else 0
        assert result.returncode == expected, (case, name)
        if name == "labels":
            assert (
                "--add-label" in result.stdout and "--remove-label" in result.stdout
            ) == (case != "labels")
        if name == "closure":
            assert ("--reason" in result.stdout) == (case != "closure")
        checks.append(
            {
                "case": case,
                "capability": name,
                "argv": args,
                "exit": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        )
    probe = subprocess.run(
        [
            str(bash),
            "--noprofile",
            "--norc",
            "-c",
            "command -v gh; gh issue edit 11 --title forbidden",
        ],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=False,
        check=False,
    )
    assert probe.returncode == 64, (case, probe.stdout, probe.stderr)
    assert "gh-shims/gh" in probe.stdout.replace("\\", "/")
    checks.append(
        {
            "case": case,
            "git_bash_mutation_denied": True,
            "stdout": probe.stdout,
            "stderr": probe.stderr,
        }
    )
    windows = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-Command",
            "& " + "'" + str(shim / "gh.cmd") + "' --version",
        ],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=False,
        check=False,
    )
    assert windows.returncode == 0 and "gh version" in windows.stdout
(work / "real-gh-path.txt").write_text(real_gh, encoding="utf-8", newline="\n")
(root / "tests/scenarios/2026-10-26-issue-11-gh-failure-controls.json").write_text(
    json.dumps(
        {
            "result": "PASS",
            "isolated_capability_probes": 16,
            "git_bash_mutation_denials": 4,
            "windows_adapter_version_checks": 4,
            "checks": checks,
        },
        indent=2,
        ensure_ascii=False,
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    "PASS: four-by-four capability isolation; Git Bash mutation denial and Windows adapter checks"
)
```

## record_progress.py

SHA-256: `76284893cd4f6fda0765078ec32647c25a3efe9d7e7aa114f5f3711f213593da`

```python
"""Record only directly observed installation/discovery passes and safe sources."""

import hashlib
import json
from pathlib import Path
import re

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
base = root / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance"
data = json.loads(base.with_suffix(".json").read_text(encoding="utf-8"))
live_path = "tests/scenarios/2026-10-26-issue-11-native-setup.json"
live = json.loads((root / live_path).read_text(encoding="utf-8"))
flow_path = root / "tests/scenarios/2026-10-26-issue-11-native-setup-workflow.json"
flow = json.loads(flow_path.read_text(encoding="utf-8"))
redactions = []


def scrub(value):
    if isinstance(value, dict):
        return {key: scrub(item) for key, item in value.items()}
    if isinstance(value, list):
        return [scrub(item) for item in value]
    if isinstance(value, str):
        pattern = r"(?im)^([A-Z0-9_]*(?:TOKEN|SECRET|PASSWORD|API_KEY|ACCESS_KEY|CREDENTIAL)[A-Z0-9_]*=)([^\r\n]+)"

        def replace(match):
            redactions.append(match.group(1).rstrip("="))
            return match.group(1) + "[REDACTED]"

        return re.sub(pattern, replace, value)
    return value


flow = scrub(flow)
flow["assessment"] = {
    "result": "UNKNOWN",
    "reason": "Identity and capability observations plus protected-state comparison passed, but the session wrote an unowned /tmp/i11.json and /tmp/i11.err despite the no-file instruction; global user-file preservation was not established for that scratch write. Preserve as a failed probe method, not a native-setup PASS.",
    "current_host": live["host_version"],
    "host_drift": "Claude auto-updated from planning 2.1.302 to observed 2.1.311 before clean-install completion. Fresh live outcomes are recorded at 2.1.311; earlier host-dependent results require renewed applicability analysis.",
}
flow["redaction_screen"] = {
    "scope": "Credential-like environment assignments; heuristic, not a comprehensive secret guarantee",
    "redacted_variable_names": sorted(set(redactions)),
}
flow_path.write_text(
    json.dumps(flow, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
assert live["result"] == "PASS" and len(live["installed_files"]) == 20
pointer = {
    "path": live_path,
    "sha256": hashlib.sha256((root / live_path).read_bytes()).hexdigest(),
}
start = json.loads(
    (root / "tests/scenarios/2026-10-26-issue-11-execution-start.json").read_text(
        encoding="utf-8"
    )
)
data["phase"] = "execution"
data["observed_revision"] = start["active"]["updatedAt"]
data["execution_policy_correction"] = (
    "tests/scenarios/2026-10-26-testing-boundary-policy.md"
)
markdown = (
    base.with_suffix(".md")
    .read_text(encoding="utf-8")
    .split("\n## Execution update after policy correction")[0]
)
reasons = {
    "clean-install": "Fresh guide bootstrap and native installation passed for C; one Backplane identity, 20 exact installed blobs, independent upstream and immediate protected-state comparisons verified",
    "fresh-discovery": "Fresh session 2763f73f-d7f8-4f5b-8f61-9c0dcede1dc0 made all three actual Skill calls from independent packages; protected state unchanged",
}
for row in data["rows"]:
    if row["id"] in reasons:
        row.update(
            result="PASS",
            disposition="rerun",
            reason=reasons[row["id"]],
            observed_claim=reasons[row["id"]],
            verified_input_comparison="Fresh C detached clone, clean state and 20 installed blobs; native CLI/session observations and before/after comparisons",
        )
        if not any(e["path"] == live_path for e in row["evidence"]):
            row["evidence"].append(pointer)
        row["candidate_inputs"].update(
            host=live["host_version"],
            installed_skills={
                "required_names": live["skill_calls"],
                "session_id": live["session_id"],
                "fresh_tool_loads": "PASS",
                "evidence": live_path,
            },
        )
    elif row["id"] != "prerequisites":
        row["changed_inputs"].append(
            "Claude auto-update to 2.1.311; current affected live check required"
        )
    markdown = re.sub(
        r"^\| " + re.escape(row["id"]) + r" \|.*$",
        lambda match,
        row=row: f"| {row['id']} | {row['result']} | #{row['owner']} | {row['reason']} |",
        markdown,
        flags=re.M,
    )
counts = {
    value: sum(row["result"] == value for row in data["rows"])
    for value in ("PASS", "FAIL", "UNKNOWN")
}
data["counts"] = counts
base.with_suffix(".json").write_text(
    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
markdown += "\n## Execution update after policy correction\n\n"
markdown += (
    "The earlier boundary/publication requests are historical and superseded by the testing-boundary correction. "
    "Approved local testing resumed. Guide clean-install bootstrap and native installation passed for C; all 20 "
    "installed canonical files matched and a fresh session actually loaded all three skills. Normal-profile file "
    "hashes, independent upstream, unrelated plugins/catalogs, repository refs and complete issue state were preserved.\n\n"
    "Claude auto-updated from planning 2.1.302 to observed 2.1.311 before completion of the fresh clean-install run. "
    "Its live evidence records 2.1.311; prior host-dependent results cannot be retained without renewed reconciliation.\n\n"
    "The separate Backplane-only profile is unauthenticated. Its signed-out receipt preserves the external prerequisite "
    "for sibling and absent-upstream setup; the operator was given a child-scoped login command, without credential copying.\n\n"
    "The native setup workflow session returned identity/capability observations and preserved the captured protected state, "
    "but wrote unowned /tmp/i11.json and /tmp/i11.err despite an explicit no-file instruction. Native setup stays UNKNOWN "
    "pending a corrected probe with an owned capture area; do not infer complete user-file preservation from that run. "
    "The original observations and probe-source behavior are retained, with a heuristic credential-assignment screen.\n\n"
)
markdown += f"Current partial results: {counts}. No final #11 acceptance is claimed.\n"
base.with_suffix(".md").write_text(markdown, encoding="utf-8", newline="\n")
sources = [
    work / name
    for name in (
        "start_execution.py",
        "live_native_setup.py",
        "native_setup_probe.py",
        "login_setup_profile.py",
        "record_progress.py",
    )
]
lines = [
    "# Issue #11 live verification source",
    "",
    "The native installation receipt contains actual command/session observations. The workflow receipt is UNKNOWN because its test agent wrote unowned temporary files; this is disclosed rather than scored PASS. Only the clean-install and fresh-discovery rows are currently scored as fresh passes.",
    "",
    "The workflow receipt has a heuristic screen for credential-like environment assignments; it is not a comprehensive secret guarantee. Do not publish raw scratch streams without review.",
    "",
]
for source in sources:
    lines += [
        f"## {source.name}",
        "",
        f"SHA-256: `{hashlib.sha256(source.read_bytes()).hexdigest()}`",
        "",
        "```python",
        source.read_text(encoding="utf-8").rstrip(),
        "```",
        "",
    ]
(root / "tests/scenarios/transcripts/2026-10-26-issue-11-live-source.md").write_text(
    "\n".join(lines), encoding="utf-8", newline="\n"
)
print(
    json.dumps(
        {
            "counts": counts,
            "observed_claude": live["host_version"],
            "workflow_assessment": "UNKNOWN; unowned temp-file write",
            "credential_variables_redacted": sorted(set(redactions)),
        },
        indent=2,
    )
)
```

## relationship_reference_probe.py

SHA-256: `9ae46ce133d93b5a4c58bc2e4b6bf1211aa8a1cee556edf060e65f55290beb99`

```python
"""Apply the full corrected native issue reference to the observed JSON shape."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
contract = (
    root / "skills/managing-superpowers-backlog/references/github-issue-contract.md"
)
main_skill = root / "skills/managing-superpowers-backlog/SKILL.md"
baseline_path = root / "tests/scenarios/2026-10-26-issue-11-gh-closure-failure.json"
baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
issue = baseline["before"]["issue11"]
payload = {
    key: issue[key]
    for key in ("number", "state", "labels", "subIssues", "blockedBy", "blocking")
}
prompt = (
    f"Read the complete current native issue reference at {contract}. "
    "This is a read-only reference application check, not setup or issue execution. "
    "Summarize this actual gh issue snapshot for a maintainer who needs an immediate leaf/dependency decision. "
    "Do not inspect other project files or run commands. Return only one JSON object containing "
    "sub_issue_count, blocker_count, blocking_count, is_leaf, unresolved_blocker_count. "
    "Use the actual relationship data, with no invented issues.\n" + json.dumps(payload)
)
environment = dict(
    os.environ, CLAUDE_CONFIG_DIR=str(root / ".sp-bp/work/issue-19/profile")
)
executable = shutil.which("claude")
assert executable is not None
args = [
    executable,
    "-p",
    prompt,
    "--append-system-prompt",
    main_skill.read_text(encoding="utf-8"),
    "--tools",
    "Read",
    "--allowedTools",
    "Read",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "6",
]
result = subprocess.run(
    args,
    cwd=work / "native-neutral",
    env=environment,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
    timeout=120,
    shell=False,
    check=False,
)
(work / "relationship-reference.jsonl").write_text(
    result.stdout, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
host = next(e for e in reversed(events) if e.get("type") == "result")
assert (
    result.returncode == 0
    and host.get("subtype") == "success"
    and not host.get("is_error")
)
text = host["result"].strip()
if text.startswith("```"):
    text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
observed = json.loads(text)
expected = {
    "sub_issue_count": 0,
    "blocker_count": 2,
    "blocking_count": 1,
    "is_leaf": True,
    "unresolved_blocker_count": 0,
}
assert observed == expected, (observed, expected)
reads = [
    block
    for event in events
    if isinstance(event.get("message"), dict)
    for block in event["message"].get("content", [])
    if isinstance(block, dict)
    and block.get("type") == "tool_use"
    and block.get("name") == "Read"
]
assert any(
    Path(call["input"]["file_path"]).resolve() == contract.resolve() for call in reads
)
receipt = {
    "result": "PASS",
    "scope": "Full current reference application; not an installed-package acceptance run",
    "baseline": str(baseline_path.relative_to(root)),
    "red_assertion": (work / "relationship-counts-red.txt").read_text(encoding="utf-8"),
    "baseline_reported_sub_issue_count": 2,
    "actual_sub_issue_count": 0,
    "contract_sha256": hashlib.sha256(contract.read_bytes()).hexdigest(),
    "prompt": prompt,
    "observed": observed,
    "expected": expected,
    "session_id": host.get("session_id"),
    "reads": reads,
    "response": host["result"],
}
(root / "tests/scenarios/2026-10-26-issue-11-relationship-reference.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "result": "PASS",
            "baseline": "2 reported versus 0 actual",
            "green": observed,
            "session_id": host.get("session_id"),
        },
        indent=2,
    )
)
```

## replay_lifecycle.py

SHA-256: `0731f2c6d03edab9892bd1b4b2c84b9aae8185579ec82c6614c00dcf872f154b`

```python
"""Replay all nine unchanged guide blocks at current C and published test F."""

from contextlib import redirect_stdout
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

from lifecycle_helpers import BASELINE, FIXTURE, Harness, read_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11/lifecycle-run"
assert not work.exists(), "Use an unused execution output directory"
work.mkdir()
(work / "neutral").mkdir()
profile = root / ".sp-bp/work/issue-19/profile"
catalog = root / ".sp-bp/work/issue-11/lifecycle-catalog"
assert not catalog.exists(), "Use an unused owned dedicated catalog"
assert sys.version_info[:3] == (3, 14, 9)
h = Harness(root, profile=profile, catalog=catalog, output=work)
for ref in (BASELINE, FIXTURE):
    assert (
        h.command(
            [
                "gh",
                "api",
                f"repos/tvproductions/superpowers-backplane/commits/{ref}",
                "--jq",
                ".sha",
            ]
        ).strip()
        == ref
    )
trees = {
    ref: h.command(["git", "ls-tree", "-r", ref, "--", "skills"]).strip()
    for ref in (BASELINE, FIXTURE)
}
assert trees[BASELINE] == trees[FIXTURE], "Fixture skill bytes differ from current C"
sentinel = profile / "issue11-preservation-sentinel.txt"
assert not sentinel.exists(), "Do not overwrite an occupied sentinel path"
sentinel.write_text(
    "Issue11 lifecycle user-file preservation sentinel\n",
    encoding="utf-8",
    newline="\n",
)
before_plugins = json.loads(h.command(["claude", "plugin", "list", "--json"]))
assert (
    sum(
        p["id"] == "superpowers-backplane@superpowers-backplane" for p in before_plugins
    )
    == 1
)
old_catalog = (
    root
    / ".sp-bp/work/issue-11/fixtures/clean-install/superpowers-backplane/.claude-plugin/marketplace.json"
)
assert [p["name"] for p in read_json(old_catalog)["plugins"]] == [
    "superpowers-backplane"
]
log = work / "replay.txt"
blocks = re.findall(
    r"(?ms)^```python\n(.*?)^```",
    (root / "docs/installing-claude-code.md").read_text(encoding="utf-8"),
)
assert len(blocks) == 9
answers = iter((str(profile), str(catalog), BASELINE, FIXTURE))


def answer(prompt):
    value = next(answers)
    print(f"{prompt}{value}", flush=True)
    return value


state: dict[str, Any] = {"input": answer, "__name__": "__guide_replay__"}
with log.open("w", encoding="utf-8", newline="\n") as output, redirect_stdout(output):
    print(
        "Preparing dedicated hosted-source catalog; prior local-directory marketplace is verified Backplane-only."
    )
    h.claude(
        "plugin",
        "uninstall",
        "superpowers-backplane@superpowers-backplane",
        "--scope",
        "user",
    )
    h.claude("plugin", "marketplace", "remove", "superpowers-backplane")
    h.source(BASELINE)
    h.claude("plugin", "marketplace", "add", str(catalog), "--scope", "user")
    h.claude(
        "plugin",
        "install",
        "superpowers-backplane@superpowers-backplane",
        "--scope",
        "user",
    )
    h.snapshot("lifecycle-baseline", BASELINE, "0.1.0")
    for index, block in enumerate(blocks):
        print(f"Exact guide block {index}", flush=True)
        manifest = catalog / ".claude-plugin/marketplace.json"
        prior_catalog = manifest.read_bytes()
        exec(compile(block, f"claude-guide:block-{index}", "exec"), state)
        revision = None if index in (4, 7) else FIXTURE if index == 3 else BASELINE
        version = None if revision is None else "0.1.1" if index == 3 else "0.1.0"
        h.snapshot(f"guide-{index}", revision, version)
        if index == 6:
            assert manifest.read_bytes() == prior_catalog, (
                "Rejected source changed catalog"
            )
        if index in (2, 3, 5, 8):
            h.discovery(f"guide-{index}")
        elif index == 7:
            h.discovery(f"guide-{index}", absent=True)
    print(
        "PASS: nine exact blocks, ten snapshots and five fresh discovery sessions; exact C restored"
    )
receipt = {
    "result": "PASS",
    "runtime": sys.version,
    "host": h.command(["claude", "--version"]).strip(),
    "prior": BASELINE,
    "fixture": FIXTURE,
    "fixture_skill_bytes_equal_current_C": True,
    "exact_blocks": 9,
    "block_hashes": [hashlib.sha256(b.encode("utf-8")).hexdigest() for b in blocks],
    "snapshots": [
        read_json(work / f"{name}-snapshot.json")
        for name in ["lifecycle-baseline", *[f"guide-{i}" for i in range(9)]]
    ],
    "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
}
(root / "tests/scenarios/2026-10-26-issue-11-lifecycle.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {k: receipt[k] for k in ("result", "host", "prior", "fixture", "exact_blocks")},
        indent=2,
    )
)
```

## sanitize_evidence.py

SHA-256: `82f2d137f3151998b047472b0fb2739c43f7c97da34f21cea67b536afac616b5`

```python
"""Remove known incidental runtime assignments from publishable derived evidence."""

import json
from pathlib import Path
import re

from lifecycle_helpers import write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
scenarios = root / "tests/scenarios"
known = set()
for path in work.rglob("*.jsonl"):
    relative = path.relative_to(work)
    if any(p in {"fixtures", "setup-profile", "profile"} for p in relative.parts):
        continue
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            decoded = json.loads(line)
        except ValueError:
            continue

        def find(value):
            if isinstance(value, dict):
                for item in value.values():
                    find(item)
            elif isinstance(value, list):
                for item in value:
                    find(item)
            elif isinstance(value, str):
                known.update(
                    v
                    for v in re.findall(
                        r"CLAUDE_CODE_MESSAGING_TOKEN=([A-Za-z0-9_.-]+)", value
                    )
                    if len(v) > 20
                )

        find(decoded)
paths = list(scenarios.glob("2026-10-26-issue-11-*")) + list(
    (scenarios / "transcripts").glob("2026-10-26-issue-11-*")
)
changed = []
for path in paths:
    if not path.is_file() or path.suffix not in {".md", ".json"}:
        continue
    content = path.read_text(encoding="utf-8")
    revised = content
    for secret in known:
        revised = revised.replace(secret, "[REDACTED-RUNTIME-ASSIGNMENT]")
    revised = re.sub(
        r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}_[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}",
        "redacted-synced-owner",
        revised,
        flags=re.I,
    )
    if revised != content:
        path.write_text(revised, encoding="utf-8", newline="\n")
        changed.append(path.relative_to(root).as_posix())
    assert not any(secret in revised for secret in known)
    assert "<EXTREMELY-IMPORTANT>" not in revised
write_json(
    scenarios / "2026-10-26-issue-11-capture-policy.json",
    {
        "result": "PASS",
        "files_screened": len(paths),
        "derived_files_redacted": changed,
        "known_incidental_runtime_values": len(known),
        "policy": "Never inspect or copy credential stores. Known incidental values were identified only in previously captured ignored test streams. Replace them in derived publishable artifacts; raw streams stay ignored. Account/organization fields previously redacted; unrelated synced-owner path component consistently aliased. Upstream injected skill bodies omitted, retaining locator/hash observations. Historical unrelated evidence unchanged.",
    },
)
print(
    f"PASS: {len(paths)} derived evidence files screened; {len(known)} known incidental values excluded"
)
```

## shared_catalog_probe.py

SHA-256: `bf955b13367140765dfda8e45942143e93e855d2fa4089306ca02a2694febe2d`

```python
"""Prove exact Backplane removal preserves an installed shared-catalog plugin."""

import json
from pathlib import Path

from lifecycle_helpers import BACKPLANE, Harness, write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
output = work / "shared-catalog-probe"
assert not output.exists()
output.mkdir()
(output / "neutral").mkdir()
catalog = work / "fixtures/final-catalog"
assert catalog.resolve(strict=True).is_relative_to(work.resolve(strict=True))
assert (root / ".git").exists()
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"
h = Harness(root, profile=root / ".sp-bp/work/issue-19/profile", output=output)
commands = []


def native(*args):
    value = h.command(["claude", *args])
    commands.append({"argv": ["claude", *args], "stdout": value, "exit": 0})
    write_json(output / "commands.json", commands)
    return value


initial = h.snapshot("initial", candidate, "0.1.0", capture_only=True)
manifest = catalog / ".claude-plugin/marketplace.json"
original = json.loads(manifest.read_text(encoding="utf-8"))
assert original["name"] == "superpowers-backplane"
assert [p["name"] for p in original["plugins"]] == ["superpowers-backplane"]
assert original["plugins"][0]["source"] == "./package"
sentinel = catalog / "sentinel"
assert not sentinel.exists()
write_json(
    sentinel / ".claude-plugin/plugin.json",
    {
        "name": "sp-bp-preservation-sentinel",
        "version": "0.0.0",
        "description": "Metadata-only preservation test fixture",
        "author": {"name": "Backplane test"},
    },
)
(sentinel / "README.md").write_text(
    "Owned shared-marketplace sentinel.\n", encoding="utf-8", newline="\n"
)
extended = dict(
    original,
    plugins=[
        *original["plugins"],
        {
            "name": "sp-bp-preservation-sentinel",
            "source": "./sentinel",
            "description": "Metadata-only preservation test fixture",
        },
    ],
)
write_json(manifest, extended)
native("plugin", "marketplace", "update", "superpowers-backplane")
sid = "sp-bp-preservation-sentinel@superpowers-backplane"
native("plugin", "install", sid, "--scope", "user")
before = h.snapshot("before-uninstall", candidate, "0.1.0", capture_only=True)
registry_path = h.profile / "plugins/installed_plugins.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))["plugins"]
entry = registry[sid]
installed = Path(entry[0]["installPath"])
sentinel_files = {
    str(p.relative_to(installed)): h.hash_file(p)
    for p in installed.rglob("*")
    if p.is_file()
}
assert sentinel_files
native("plugin", "uninstall", BACKPLANE, "--scope", "user")
after = h.snapshot("after-uninstall", None, None, compare_to=before)
assert next(p for p in after["plugins"] if p["id"] == sid)["enabled"]
assert json.loads(registry_path.read_text(encoding="utf-8"))["plugins"][sid] == entry
assert {
    str(p.relative_to(installed)): h.hash_file(p)
    for p in installed.rglob("*")
    if p.is_file()
} == sentinel_files
h.discovery("uninstalled", absent=True)
native("plugin", "install", BACKPLANE, "--scope", "user")
restored = h.snapshot("restored", candidate, "0.1.0", compare_to=before)
assert json.loads(registry_path.read_text(encoding="utf-8"))["plugins"][sid] == entry
assert {
    str(p.relative_to(installed)): h.hash_file(p)
    for p in installed.rglob("*")
    if p.is_file()
} == sentinel_files
h.discovery("restored")
assert initial["preservation"] == restored["preservation"]
write_json(
    root / "tests/scenarios/2026-10-26-issue-11-shared-catalog.json",
    {
        "result": "PASS",
        "candidate": candidate,
        "profile": str(h.profile),
        "before": before,
        "after_uninstall": after,
        "restored": restored,
        "sentinel_registry": entry,
        "sentinel_file_hashes": sentinel_files,
        "commands": commands,
        "scope": "Native exact-plugin uninstall/restoration; installed unrelated shared-catalog sentinel and marketplace retained. Fixture retained; no cleanup or publication.",
    },
)
print(
    "PASS: shared-catalog sentinel preserved through exact Backplane uninstall and restoration",
    flush=True,
)
```

## sibling_setup_probe.py

SHA-256: `b4f2267a9662fc1c3eaa449910b839cf5488a0569a77514ff0ae6f84288ab2a2`

```python
"""Observe the actual installed native setup workflow in a read-only session."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = (work / "setup-profile").resolve(strict=True)
environment = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile), PYTHONIOENCODING="utf-8")
captures = work / "sibling-setup-captures"
assert not captures.exists(), "Use an unused owned capture directory"
captures.mkdir()
for variable in ("TMPDIR", "TMP", "TEMP"):
    environment[variable] = str(captures.resolve())
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run(args, *, cwd=root, timeout=90):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=environment,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def protected():
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "profile_files": {
            str(p.relative_to(profile)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                profile / "settings.json",
                profile / "plugins/installed_plugins.json",
                profile / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "upstream_head": run(
            ["git", "-C", str(root / ".agents/superpowers"), "rev-parse", "HEAD"]
        ),
        "upstream_status": run(
            ["git", "-C", str(root / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }


before = protected()
prompt = (
    "Set up Superpowers Backplane in this Claude Code session. "
    "The target repository is tvproductions/superpowers-backplane and existing issue is #11. "
    "Use the installed managing-superpowers-backlog skill and its installation reference. "
    "This is the compatible-sibling-checkout mode: the profile has only the Backplane native plugin. "
    f"Upstream is supplied for this session by --plugin-dir {root / '.agents/superpowers'}. "
    "Verify that separate authoritative checkout, adopt it in place, and do not register or install upstream in this profile. "
    "Verify their actual independent roots, source/version or commit, one effective Backplane, "
    "required upstream skills, and gh authentication/full native issue intake/label and closure help. "
    "Adopt existing packages in place. Do not install, update, remove, edit user or package files, "
    "create a plan or handoff, or mutate GitHub. Report unresolved checks honestly. "
    f"If you need to capture command output, create files only inside this pre-created owned directory: {captures}. "
    "Never use hardcoded /tmp/i11 files, enumerate environment variables, or read authentication secrets. "
    f"The intended profile is {profile}; inspect only its plugin inventory/metadata and the two verified package sources. "
    "Use claude plugin list --json and claude plugin marketplace list --json; do not inspect unrelated profiles or orphaned cache contents. "
    "Separate fresh direct loads of all three skills were observed after this installation; "
    "do not claim to have rerun those separate sessions. Use only read-only commands."
)
allow = [
    "Skill",
    "Read",
    "Bash(gh auth status)",
    "Bash(gh issue view *)",
    "Bash(gh issue edit --help)",
    "Bash(gh issue close --help)",
    "Bash(claude plugin list *)",
    "Bash(claude plugin marketplace list *)",
    "Bash(claude --version)",
    "Bash(gh --version)",
    "Bash(git -C * remote get-url origin)",
    "Bash(git -C * rev-parse *)",
    "Bash(git -C * status *)",
    "Bash(git remote get-url origin)",
    "Bash(git rev-parse *)",
    "Bash(git status *)",
]
arguments = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash",
    "--plugin-dir",
    str(root / ".agents/superpowers"),
    "--allowedTools",
    *allow,
    "--disallowedTools",
    "Bash(*env*)",
    "Bash(*printenv*)",
    "--permission-mode",
    "plan",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "32",
]
stream = run(arguments, cwd=work / "native-neutral", timeout=300)
(work / "sibling-setup-workflow.jsonl").write_text(
    stream, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
calls: list[dict[str, Any]] = []
responses = []
for event in events:
    for block in event.get("message", {}).get("content", []):
        if block.get("type") == "tool_use":
            calls.append(
                {"name": block["name"], "input": block["input"], "id": block["id"]}
            )
        if block.get("type") == "tool_result":
            responses.append(block)
after = protected()
assert before == after, "Setup changed protected state; preserve before repair"
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "prompt": prompt,
    "argv": arguments,
    "profile": str(profile),
    "before": before,
    "after": after,
    "protected_state_preserved": True,
    "tool_calls": calls,
    "tool_results": responses,
    "host_result": result,
    "result": "UNSCORED; inspect actual tool results against setup contract",
    "raw_stream_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
}
(root / "tests/scenarios/2026-10-26-issue-11-sibling-setup-workflow.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "subtype": result.get("subtype"),
            "is_error": result.get("is_error"),
            "session_id": result.get("session_id"),
            "tools": len(calls),
            "protected_state_preserved": True,
            "report": result.get("result"),
        },
        indent=2,
    )
)
```

## sibling_setup_probe2.py

SHA-256: `d08399c70cfb0df829537768afa12aca0dc39544c7e161216e0f70cf7bde59aa`

```python
"""Observe the actual installed native setup workflow in a read-only session."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
profile = (work / "setup-profile").resolve(strict=True)
environment = dict(os.environ, CLAUDE_CONFIG_DIR=str(profile), PYTHONIOENCODING="utf-8")
captures = work / "sibling-setup-captures-2"
assert not captures.exists(), "Use an unused owned capture directory"
captures.mkdir()
for variable in ("TMPDIR", "TMP", "TEMP"):
    environment[variable] = str(captures.resolve())
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run(args, *, cwd=root, timeout=90):
    executable = shutil.which(args[0])
    assert executable is not None
    return subprocess.check_output(
        [executable, *args[1:]],
        cwd=cwd,
        env=environment,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def protected():
    return {
        "plugins": json.loads(run(["claude", "plugin", "list", "--json"])),
        "marketplaces": json.loads(
            run(["claude", "plugin", "marketplace", "list", "--json"])
        ),
        "profile_files": {
            str(p.relative_to(profile)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (
                profile / "settings.json",
                profile / "plugins/installed_plugins.json",
                profile / "plugins/known_marketplaces.json",
            )
            if p.is_file()
        },
        "upstream_head": run(
            ["git", "-C", str(root / ".agents/superpowers"), "rev-parse", "HEAD"]
        ),
        "upstream_status": run(
            ["git", "-C", str(root / ".agents/superpowers"), "status", "--porcelain=v1"]
        ),
        "project_refs": run(["git", "show-ref"]),
        "issue11": json.loads(
            run(
                [
                    "gh",
                    "issue",
                    "view",
                    "11",
                    "--repo",
                    "tvproductions/superpowers-backplane",
                    "--json",
                    FIELDS,
                ]
            )
        ),
    }


before = protected()
(work / "sibling-before-2.json").write_text(
    json.dumps(before, indent=2) + "\n", encoding="utf-8", newline="\n"
)
prompt = (
    "Set up Superpowers Backplane in this Claude Code session. "
    "The target repository is tvproductions/superpowers-backplane and existing issue is #11. "
    "Use the installed managing-superpowers-backlog skill and its installation reference. "
    "This is the compatible-sibling-checkout mode: the profile has only the Backplane native plugin. "
    f"Upstream is supplied for this session by --plugin-dir {root / '.agents/superpowers'}. "
    "Verify that separate authoritative checkout, adopt it in place, and do not register or install upstream in this profile. "
    "Verify their actual independent roots, source/version or commit, one effective Backplane, "
    "required upstream skills, and gh authentication/full native issue intake/label and closure help. "
    "Adopt existing packages in place. Do not install, update, remove, edit user or package files, "
    "create a plan or handoff, or mutate GitHub. Report unresolved checks honestly. "
    f"If you need to capture command output, create files only inside this pre-created owned directory: {captures}. "
    "Never use hardcoded /tmp/i11 files, enumerate environment variables, or read authentication secrets. "
    f"The intended profile is {profile}; inspect only its plugin inventory/metadata and the two verified package sources. "
    "Use claude plugin list --json and claude plugin marketplace list --json; do not inspect unrelated profiles or orphaned cache contents. "
    "Separate fresh direct loads of all three skills were observed after this installation; "
    "do not claim to have rerun those separate sessions. Use only read-only commands."
)
allow = [
    "Skill",
    "Read",
    "Bash(gh auth status)",
    "Bash(gh issue view *)",
    "Bash(gh issue edit --help)",
    "Bash(gh issue close --help)",
    "Bash(claude plugin list *)",
    "Bash(claude plugin marketplace list *)",
    "Bash(claude --version)",
    "Bash(gh --version)",
    "Bash(git -C * remote get-url origin)",
    "Bash(git -C * rev-parse *)",
    "Bash(git -C * status *)",
    "Bash(git remote get-url origin)",
    "Bash(git rev-parse *)",
    "Bash(git status *)",
]
arguments = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash",
    "--plugin-dir",
    str(root / ".agents/superpowers"),
    "--allowedTools",
    *allow,
    "--disallowedTools",
    "Bash(*env*)",
    "Bash(*printenv*)",
    "--permission-mode",
    "plan",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "32",
]
stream = run(arguments, cwd=work / "native-neutral", timeout=300)
(work / "sibling-setup-workflow-2.jsonl").write_text(
    stream, encoding="utf-8", newline="\n"
)
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
calls: list[dict[str, Any]] = []
responses = []
for event in events:
    if not isinstance(event.get("message"), dict):
        continue
    for block in event.get("message", {}).get("content", []):
        if block.get("type") == "tool_use":
            calls.append(
                {"name": block["name"], "input": block["input"], "id": block["id"]}
            )
        if block.get("type") == "tool_result":
            responses.append(block)
after = protected()
assert before == after, "Setup changed protected state; preserve before repair"
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "prompt": prompt,
    "argv": arguments,
    "profile": str(profile),
    "before": before,
    "after": after,
    "protected_state_preserved": True,
    "tool_calls": calls,
    "tool_results": responses,
    "host_result": result,
    "result": "UNSCORED; inspect actual tool results against setup contract",
    "raw_stream_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
}
(root / "tests/scenarios/2026-10-26-issue-11-sibling-setup-workflow-2.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "subtype": result.get("subtype"),
            "is_error": result.get("is_error"),
            "session_id": result.get("session_id"),
            "tools": len(calls),
            "protected_state_preserved": True,
            "report": result.get("result"),
        },
        indent=2,
    )
)
```

## start_execution.py

SHA-256: `08abb6687eb4907da7ff5ad7338c542bc8a3d39317e750f7d37a5464fad7364f`

```python
"""Link the approved local plan and observe authorized ready/active transitions."""

import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path.cwd().resolve(strict=True)
WORK = ROOT / ".sp-bp/work/issue-11"
FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"
PLAN = "docs/superpowers-backplane/plans/2026-10-26-issue-11-claude-integrated-acceptance.md"
PLAN_COMMIT = "1d4ba0f7c2df54b92c19c24d543dc97d17933712"
gh = shutil.which("gh")
assert gh


def call(args):
    executable = gh
    assert executable is not None
    result = subprocess.run(
        [executable, *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        check=True,
    )
    return result.stdout


def read_issue():
    return json.loads(
        call(
            [
                "issue",
                "view",
                "11",
                "--repo",
                "tvproductions/superpowers-backplane",
                "--json",
                FIELDS,
            ]
        )
    )


def label(issue):
    names = [
        item["name"]
        for item in issue["labels"]
        if item["name"].startswith("backplane:")
    ]
    assert len(names) == 1
    return names[0]


assert (ROOT / PLAN).read_bytes() == subprocess.check_output(
    ["git", "show", f"{PLAN_COMMIT}:{PLAN}"], cwd=ROOT
)
before = read_issue()
assert before["state"] == "OPEN" and label(before) == "backplane:designing"
assert before["parent"]["number"] == 1 and not before["subIssues"]["nodes"]
assert all(node["state"] == "CLOSED" for node in before["blockedBy"]["nodes"])
assert before["body"].count("Plan: not yet created.") == 1
body = before["body"].replace(
    "Plan: not yet created.",
    f"Approved implementation plan: `{PLAN}` at local Git commit `{PLAN_COMMIT}`. "
    "The operator approved native execution on 2026-10-26 after reviewing the plan in the conversation. "
    "This consumes semantic issue revision `2026-09-20T01:31:32Z`; the later planning-label revision does not change scope or acceptance. "
    "The plan is available in the current execution repository; remote publication is pending and is not claimed. "
    "The current verification-workspace policy permits the approved local fixture tests without an issue-specific exception or prior push.",
)
body_file = WORK / "issue11-approved-local-plan-body.md"
body_file.write_text(body, encoding="utf-8", newline="\n")
call(
    [
        "issue",
        "edit",
        "11",
        "--repo",
        "tvproductions/superpowers-backplane",
        "--body-file",
        str(body_file),
        "--remove-label",
        "backplane:designing",
        "--add-label",
        "backplane:ready",
    ]
)
ready = read_issue()
assert ready["body"] == body and label(ready) == "backplane:ready"
for field in ("parent", "subIssues", "blockedBy", "blocking"):
    assert ready[field] == before[field], field
call(
    [
        "issue",
        "edit",
        "11",
        "--repo",
        "tvproductions/superpowers-backplane",
        "--remove-label",
        "backplane:ready",
        "--add-label",
        "backplane:active",
    ]
)
active = read_issue()
assert active["body"] == body and label(active) == "backplane:active"
for field in ("parent", "subIssues", "blockedBy", "blocking"):
    assert active[field] == before[field], field
receipt = {
    "authority": "Operator selected #11 and approved reviewed native execution; current AGENTS permits required local fixtures",
    "plan_commit": PLAN_COMMIT,
    "plan_path": PLAN,
    "plan_publication": "pending; local availability explicit",
    "before": before,
    "ready": ready,
    "active": active,
    "scope_and_graph_preserved": True,
}
(ROOT / "tests/scenarios/2026-10-26-issue-11-execution-start.json").write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            "state": active["state"],
            "label": label(active),
            "updatedAt": active["updatedAt"],
            "scope_and_graph_preserved": True,
            "plan_publication": "pending; not required for local execution",
        },
        indent=2,
    )
)
```

## status_selection_probe.py

SHA-256: `8bf99ecc9cdc7efb8e71c6b54841e997a08acf58510b2ccc73f7f4ac87e2fdd9`

```python
"""Fresh installed status/selection response with guarded read-only GitHub access."""

import json
import os
from pathlib import Path
import shutil

from lifecycle_helpers import Harness, run_cli, write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
output = work / "status-selection-final"
assert not output.exists()
output.mkdir()
(output / "neutral").mkdir()
candidate = "91ea3bb7933b5aa2c7628595f17157810cafa701"
h = Harness(
    root,
    profile=work / "setup-profile",
    output=output,
    upstream_id="superpowers@claude-plugins-official",
)
before = h.snapshot("before", candidate, "0.1.0", capture_only=True)
real_gh = shutil.which("gh")
assert real_gh is not None
env = dict(
    h.environment,
    PATH=str(work / "gh-shims") + os.pathsep + os.environ["PATH"],
    SP_BP_GH_FAILURE="none",
    SP_BP_REAL_GH=real_gh,
)
prompt = (
    "Use installed superpowers-backplane:managing-superpowers-backlog. This is a read-only "
    "status and work-selection check for tvproductions/superpowers-backplane#11. Retrieve its "
    "complete native issue intake through gh, report its actual state, graph and eligibility, "
    "and confirm this is the operator-selected issue already under execution. Do not invent "
    "priority or change labels, issue bodies, comments, files or Git. Selection alone never "
    "changes state. Do not start or submit anything. Do not enumerate environment variables, "
    "read credentials or profile files. gh is a read-only capability adapter for this test."
)
args = [
    "claude",
    "-p",
    prompt,
    "--tools",
    "Skill,Read,Bash",
    "--allowedTools",
    "Skill,Read,Bash",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    "16",
]
stream = run_cli(args, cwd=output / "neutral", overrides=env)
(output / "response.jsonl").write_text(stream, encoding="utf-8", newline="\n")
events = [json.loads(line) for line in stream.splitlines() if line.strip()]
result = next(e for e in reversed(events) if e.get("type") == "result")
assert result["subtype"] == "success" and not result.get("is_error")
calls = [
    b
    for e in events
    if isinstance(e.get("message"), dict)
    for b in e["message"].get("content", [])
    if isinstance(b, dict) and b.get("type") == "tool_use"
]
assert any(
    c["name"] == "Skill"
    and c["input"]["skill"] == "superpowers-backplane:managing-superpowers-backlog"
    for c in calls
)
assert any(
    c["name"] == "Bash" and "gh issue view" in c["input"].get("command", "")
    for c in calls
)
after = h.snapshot("after", candidate, "0.1.0", compare_to=before)
assert before == dict(after, row=before["row"])
write_json(
    root / "tests/scenarios/2026-10-26-issue-11-status-selection.json",
    {
        "result": "PASS",
        "candidate": candidate,
        "prompt": prompt,
        "session": result["session_id"],
        "response": result["result"],
        "calls": calls,
        "before": before,
        "after": after,
        "scope": "Fresh current native read-only observation; response requires manual status/selection scoring",
    },
)
print(result["result"], flush=True)
```

## verify_evidence.py

SHA-256: `82d36fe9baa391c5e12fc76629da26245580a83287b5b5594baaa8c54915a25f`

```python
"""Validate issue-11 evidence coverage without performing host operations."""

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path.cwd().resolve(strict=True)
BASE = ROOT / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance"
EXPECTED = {
    "prerequisites",
    "clean-install",
    "native-setup",
    "sibling-setup",
    "absent-setup",
    "lookalike-source",
    "versionless-package",
    "duplicate-backplane",
    "missing-upstream-skill",
    "dirty-adoption",
    "dirty-update-refusal",
    "occupied-destination",
    "gh-auth-failure",
    "gh-intake-failure",
    "gh-label-failure",
    "gh-closure-failure",
    "unauthenticated-host",
    "repeat-install",
    "pinned-update",
    "rollback",
    "uninstall",
    "restoration",
    "failed-preflight",
    "skill-structure",
    "native-issue-intake",
    "language-neutral-verification",
    "lifecycle-transitions",
    "superpowers-installation",
    "status",
    "selection",
    "design",
    "ready",
    "active",
    "blocked-resume",
    "review",
    "rework",
    "verified-completion",
    "fresh-discovery",
    "preservation",
}


def verify(phase):
    data = json.loads(BASE.with_suffix(".json").read_text(encoding="utf-8"))
    rows = data["rows"]
    assert len(rows) == len(EXPECTED), "Missing/duplicate mandatory rows"
    assert {row["id"] for row in rows} == EXPECTED, "Mandatory row set differs"
    markdown = BASE.with_suffix(".md").read_text(encoding="utf-8")
    for row in rows:
        assert row["mandatory"] is True
        assert row["result"] in ("PASS", "FAIL", "UNKNOWN")
        assert row["disposition"] in ("rerun", "retained")
        assert row["reason"] and row["requirement"] and row["owner"]
        for key in ("original_inputs", "candidate_inputs"):
            assert {
                "host",
                "backplane",
                "upstream",
                "gh_capability",
                "installed_skills",
            } <= row[key].keys(), (row["id"], key)
        assert isinstance(row["changed_inputs"], list)
        assert f"| {row['id']} | {row['result']} |" in markdown, row["id"]
        assert row["evidence"], f"Missing evidence pointer: {row['id']}"
        for evidence in row["evidence"]:
            target = (ROOT / evidence["path"]).resolve(strict=True)
            assert target.is_relative_to(ROOT), "Evidence escapes root"
            assert (
                hashlib.sha256(target.read_bytes()).hexdigest() == evidence["sha256"]
            ), (row["id"], evidence["path"])
        if row["result"] == "PASS":
            assert row.get("observed_claim"), (
                f"PASS without observed claim: {row['id']}"
            )
            assert row.get("verified_input_comparison"), (
                f"PASS without input comparison: {row['id']}"
            )
        if phase == "acceptance":
            assert row["result"] == "PASS", (
                f"Acceptance blocked: {row['id']}={row['result']}"
            )
    guide = (ROOT / "docs/installing-claude-code.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^```python\n(.*?)^```", guide, re.M | re.S)
    assert len(blocks) == 9, "Expected nine current Python guide blocks"
    for number, code in enumerate(blocks, 1):
        compile(code, f"claude-guide-block-{number}", "exec")
    return {
        "phase": phase,
        "rows": len(rows),
        "counts": {
            value: sum(r["result"] == value for r in rows)
            for value in ("PASS", "FAIL", "UNKNOWN")
        },
        "compiled_python_blocks": len(blocks),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("initial", "acceptance"), required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.phase), indent=2))
```

## verify_policy_boundary.py

SHA-256: `97fccb6a249b8353c08b2b0079f63a5c89e3b4b6162ad119009bd5c20991055b`

```python
"""Exercise the corrected local-fixture boundary without touching product Git state."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path.cwd().resolve(strict=True)
assert ROOT == Path("U:/repos/agents/superpowers-backplane").resolve(strict=True)
WORK = ROOT / ".sp-bp/work/issue-11"
FIXTURES = WORK / "fixtures"
FIXTURE = FIXTURES / "policy-boundary-probe-2"
RECEIPT = ROOT / "tests/scenarios/2026-10-26-testing-boundary-policy.json"
commands = []


def command(args, cwd=ROOT, expected=0):
    executable = shutil.which(args[0])
    assert executable
    result = subprocess.run(
        [executable, *args[1:]],
        cwd=cwd,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=90,
        check=False,
    )
    commands.append(
        {
            "argv": args,
            "cwd": str(cwd),
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    )
    assert result.returncode == expected, commands[-1]
    return result.stdout.strip()


def mutate_fixture(*args):
    observed = Path(
        command(["git", "-C", str(FIXTURE), "rev-parse", "--show-toplevel"])
    ).resolve(strict=True)
    assert observed == FIXTURE.resolve(strict=True)
    assert observed.is_relative_to(FIXTURES.resolve(strict=True))
    assert observed != ROOT
    return command(["git", "-C", str(FIXTURE), *args])


assert (
    Path(command(["git", "rev-parse", "--show-toplevel"])).resolve(strict=True) == ROOT
)
assert command(
    ["git", "check-ignore", ".sp-bp/work/issue-11/fixtures/policy-boundary-probe"]
)
project_before = {
    "head": command(["git", "rev-parse", "HEAD"]),
    "branch": command(["git", "branch", "--show-current"]),
    "refs": command(["git", "show-ref"]),
}
upstream = ROOT / ".agents/superpowers"
upstream_before = {
    key: command(["git", "-C", str(upstream), *args])
    for key, args in {
        "head": ["rev-parse", "HEAD"],
        "status": ["status", "--porcelain=v1"],
        "origin": ["remote", "get-url", "origin"],
    }.items()
}
assert not FIXTURE.exists(), "Occupied path; preserve rather than reuse unknown fixture"
FIXTURES.mkdir(parents=True, exist_ok=True)
assert FIXTURES.resolve(strict=True).is_relative_to(WORK.resolve(strict=True))
assert not WORK.is_symlink() and not FIXTURES.is_symlink()
FIXTURE.mkdir()
command(["git", "init", "-b", "fixture/main", str(FIXTURE)])
identity = {
    "root": str(FIXTURE.resolve(strict=True)),
    "origin": None,
    "starting_revision": None,
    "purpose": "fixture boundary and preservation policy regression",
}
with (WORK / "progress.md").open("a", encoding="utf-8", newline="\n") as ledger:
    ledger.write(
        "- Policy fixture registered before mutations: " + json.dumps(identity) + "\n"
    )
mutate_fixture("config", "user.name", "Backplane verification fixture")
mutate_fixture("config", "user.email", "fixture@example.invalid")
mutate_fixture(
    "remote", "add", "origin", "https://example.invalid/fixture-authority.git"
)
(FIXTURE / "sentinel.txt").write_text(
    "verified baseline\n", encoding="utf-8", newline="\n"
)
mutate_fixture("add", "--", "sentinel.txt")
mutate_fixture("commit", "-m", "test: establish isolated verification fixture")
baseline = command(["git", "-C", str(FIXTURE), "rev-parse", "HEAD"])
mutate_fixture("switch", "-c", "fixture/dirty-provenance")
(FIXTURE / "sentinel.txt").write_text(
    "deliberately dirty fixture\n", encoding="utf-8", newline="\n"
)
mutate_fixture("remote", "set-url", "origin", "https://example.invalid/lookalike.git")
assert (
    command(["git", "-C", str(FIXTURE), "status", "--porcelain=v1"]) == "M sentinel.txt"
)
assert (
    command(["git", "-C", str(FIXTURE), "remote", "get-url", "origin"])
    == "https://example.invalid/lookalike.git"
)
wrong_root_rejected = Path(command(["git", "rev-parse", "--show-toplevel"])).resolve(
    strict=True
) != FIXTURE.resolve(strict=True)
assert wrong_root_rejected, "Real project must not pass a fixture mutation guard"
assert not (FIXTURE / ".git/objects/info/alternates").exists()
project_after = {
    "head": command(["git", "rev-parse", "HEAD"]),
    "branch": command(["git", "branch", "--show-current"]),
    "refs": command(["git", "show-ref"]),
}
upstream_after = {
    key: command(["git", "-C", str(upstream), *args])
    for key, args in {
        "head": ["rev-parse", "HEAD"],
        "status": ["status", "--porcelain=v1"],
        "origin": ["remote", "get-url", "origin"],
    }.items()
}
assert project_before == project_after
assert upstream_before == upstream_after
source_sha = command(
    [
        "gh",
        "api",
        "repos/tvproductions/gz-skills-first-starter/commits/main",
        "--jq",
        ".sha",
    ]
)
source_dir = WORK / "policy-source"
source_dir.mkdir(exist_ok=True)
source_inputs = {}
for name in ("docs/baseline-policy.md", "docs/versioning.md", "CHANGELOG.md"):
    raw = command(
        [
            "gh",
            "api",
            f"repos/tvproductions/gz-skills-first-starter/contents/{name}?ref={source_sha}",
            "-H",
            "Accept: application/vnd.github.raw+json",
        ]
    )
    stored = source_dir / name.replace("/", "-")
    stored.write_text(raw + "\n", encoding="utf-8", newline="\n")
    source_inputs[name] = {
        "sha256": hashlib.sha256((raw + "\n").encode("utf-8")).hexdigest(),
        "lines": len(raw.splitlines()),
    }
result = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "result": "PASS",
    "project_root": str(ROOT),
    "fixture": identity,
    "fixture_baseline_commit": baseline,
    "fixture_final_branch": "fixture/dirty-provenance",
    "assertions": {
        "ignored_canonical_fixture_area": True,
        "fixture_commit_and_branch": True,
        "deliberately_dirty_fixture": True,
        "fixture_remote_change": True,
        "wrong_project_root_rejected": wrong_root_rejected,
        "no_alternates": True,
        "project_head_branch_refs_preserved": project_before == project_after,
        "upstream_head_status_origin_preserved": upstream_before == upstream_after,
    },
    "starter_source_revision": source_sha,
    "starter_inputs": source_inputs,
    "agents_sha256": hashlib.sha256((ROOT / "AGENTS.md").read_bytes()).hexdigest(),
    "commands": commands,
}
RECEIPT.write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(
    json.dumps(
        {
            key: result[key]
            for key in (
                "result",
                "fixture_baseline_commit",
                "assertions",
                "starter_source_revision",
            )
        },
        indent=2,
    )
)
```

## verify_transport.py

SHA-256: `ce4ae603508e2823488833af6f89087c08c09984b57d6adc6e517894b2c02578`

```python
"""Prove committed evidence bytes retain every recorded content hash."""

import hashlib
import json
from pathlib import Path
import subprocess

root = Path.cwd().resolve(strict=True)
matrix = root / "tests/scenarios/2026-10-26-issue-11-claude-integrated-acceptance.json"
data = json.loads(matrix.read_text(encoding="utf-8"))
for row in data["rows"]:
    for evidence in row["evidence"]:
        path = evidence["path"]
        committed = subprocess.check_output(["git", "show", ":" + path], cwd=root)
        assert hashlib.sha256(committed).hexdigest() == evidence["sha256"], (
            f"Staged evidence hash differs: {path}"
        )
for path in (
    subprocess.check_output(["git", "diff", "--cached", "--name-only"], cwd=root)
    .decode("utf-8")
    .splitlines()
):
    staged = subprocess.check_output(["git", "show", ":" + path], cwd=root)
    assert (root / path).read_bytes() == staged, (
        f"Working and staged bytes differ: {path}"
    )
print(
    "PASS: staged evidence retains all 39 rows and every content hash; working/staged bytes equal"
)
```
