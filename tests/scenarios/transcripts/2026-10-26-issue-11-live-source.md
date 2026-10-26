# Issue #11 live verification source

The native installation receipt contains actual command/session observations. The workflow receipt is UNKNOWN because its test agent wrote unowned temporary files; this is disclosed rather than scored PASS. Only the clean-install and fresh-discovery rows are currently scored as fresh passes.

The workflow receipt has a heuristic screen for credential-like environment assignments; it is not a comprehensive secret guarantee. Do not publish raw scratch streams without review.

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
