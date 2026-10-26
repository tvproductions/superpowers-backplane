# Issue #11 preparation transcript and source

Only read-only commands ran. No clone, checkout, profile installation, upstream acquisition, live model session, publication or native lifecycle fixture ran.

The approved in-place feature branch was created before preparation. #11 remains designing; setup execution awaits the fixture/publication boundaries described in the matrix report.

Auth email and organization fields are redacted in the input audit. No credential files were read or copied. Script sources below are the executed/formatted sources for the final audit and verification.

## Initial missing-matrix negative control

```text
Traceback (most recent call last):
  File "U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-11\verify_evidence.py", line 62, in <module>
    print(json.dumps(verify(args.phase), indent=2))
                     ~~~~~~^^^^^^^^^^^^
  File "U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-11\verify_evidence.py", line 25, in verify
    data = json.loads(BASE.with_suffix('.json').read_text(encoding='utf-8'))
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jeff\AppData\Roaming\uv\python\cpython-3.14.9-windows-x86_64-none\Lib\pathlib\__init__.py", line 787, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors, newline=newline) as f:
         ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Jeff\AppData\Roaming\uv\python\cpython-3.14.9-windows-x86_64-none\Lib\pathlib\__init__.py", line 771, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'U:\\repos\\agents\\superpowers-backplane\\tests\\scenarios\\2026-10-26-issue-11-claude-integrated-acceptance.json'
```

## Preparation verification commands

```text
["claude", "plugin", "validate", "--strict", "U:\\repos\\agents\\superpowers-backplane"]
exit=0
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.claude-plugin\marketplace.json

Plugin directory checks for U:\repos\agents\superpowers-backplane. The plugin directory is the catalog that plugins are submitted to; this is a subset of what it runs.

✘ Found 1 problem the plugin directory refuses a submission for:

  ❯ LICENSE: License missing (LICENSE_MISSING). This plugin has no LICENSE file and plugin.json has no `license`. The directory requires one of them.
    Fix: Add a LICENSE file to the plugin folder, or set `license` (an SPDX id) in plugin.json. A LICENSE at the repository root also counts for a plugin in a sub-folder.

⚠ Found 1 plugin directory warning:

  ❯ .claude-plugin/plugin.json icon: No icon (ICON_MISSING). No icon found in the plugin. The validator looked for `icon` in plugin.json and for a file at .claude-plugin/icon.png or .svg, assets/icon.png or .svg, or a similar path.
    Fix: Add a square PNG to the plugin folder at .claude-plugin/icon.png, or set `icon` in plugin.json to the path of a square PNG or JPEG in the plugin: 512 to 2048 px on each side, under 2 MB. SVG and WebP are not accepted. That file may become the listing icon only once: the first time the plugin is saved or submitted in the developer portal. Adding or changing it later does not change the icon.

About these checks:

  ❯ This folder also holds a marketplace manifest. The plugin directory treats such a folder as a plugin, so these checks cover only the plugin in this folder. To check another plugin that the marketplace lists, run validate on that plugin's folder.

These plugin directory checks do not change the result below. To fail on problems the directory refuses a submission for, run this command with --profile directory.

The directory also runs a safety scan and a policy review that this command does not.

ℹ Advice (does not change the verdict):

  ❯ U:\repos\agents\superpowers-backplane\README.md: This README has no line that installs "superpowers-backplane" from a marketplace. Add the install line, which works in one step on Claude Code 2.1.275 or later.
      /plugin install superpowers-backplane --marketplace tvproductions/superpowers-backplane

✔ Validation passed

```

```text
["pwsh", "-NoProfile", "-File", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\parse_guide.ps1"]
exit=0
PASS: 4 legacy PowerShell blocks parsed; none executed

```

```text
["uv", "run", "--no-project", "python", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_evidence.py", "--phase", "initial"]
exit=0
{
  "phase": "initial",
  "rows": 39,
  "counts": {
    "PASS": 1,
    "FAIL": 0,
    "UNKNOWN": 38
  },
  "compiled_python_blocks": 9
}

```

```text
["uv", "run", "--no-project", "python", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_evidence.py", "--phase", "acceptance"]
exit=1

Traceback (most recent call last):
  File "U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-11\verify_evidence.py", line 113, in <module>
    print(json.dumps(verify(args.phase), indent=2))
                     ~~~~~~^^^^^^^^^^^^
  File "U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-11\verify_evidence.py", line 90, in verify
    assert row["result"] == "PASS", (
           ^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Acceptance blocked: absent-setup=UNKNOWN
```

```text
["uv", "run", "--no-project", "ruff", "check", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\audit_inputs.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\create_matrix.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_evidence.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\finalize_preparation.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_transport.py"]
exit=0
All checks passed!

```

```text
["uv", "run", "--no-project", "ruff", "format", "--check", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\audit_inputs.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\create_matrix.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_evidence.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\finalize_preparation.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_transport.py"]
exit=0
5 files already formatted

```

```text
["uv", "run", "--no-project", "ty", "check", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\audit_inputs.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\create_matrix.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_evidence.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\finalize_preparation.py", "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-11\\verify_transport.py"]
exit=0
All checks passed!

```

## Preserved harness sources

### audit_inputs.py

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

### create_matrix.py

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

### verify_evidence.py

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

### parse_guide.ps1

SHA-256: `ea5cb26b109d3a1460a7cd9434eb2426dca35072f0a4ea0cab63dfc1c148f53b`

```powershell
$ErrorActionPreference = 'Stop'
$guide = Get-Content -LiteralPath 'docs/installing-claude-code.md' -Raw -Encoding utf8
$blocks = [regex]::Matches($guide, '(?ms)^```powershell\r?\n(.*?)^```')
if ($blocks.Count -ne 4) { throw "Expected four PowerShell guide blocks, found $($blocks.Count)" }
$number = 0
foreach ($block in $blocks) {
    $number++
    $tokens = $null
    $parseErrors = $null
    $null = [System.Management.Automation.Language.Parser]::ParseInput($block.Groups[1].Value, [ref]$tokens, [ref]$parseErrors)
    if ($parseErrors.Count) { throw "Guide block $number parse failure: $parseErrors" }
}
"PASS: $number legacy PowerShell blocks parsed; none executed"
```

### finalize_preparation.py

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

### verify_transport.py

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

## Transport hash regression: observed RED to GREEN

Default Windows newline translation produced CRLF in the new audit receipt; the staged Git blob contained LF. The transport verifier rejected the recorded hash before the fix. Explicit LF writers corrected the source of the mismatch. The final staged verifier output follows.

```text
Traceback (most recent call last):
  File "U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-11\verify_transport.py", line 15, in <module>
    assert hashlib.sha256(committed).hexdigest() == evidence['sha256'], f'Staged evidence hash differs: {path}'
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Staged evidence hash differs: tests/scenarios/2026-10-26-issue-11-input-audit.json

PASS: staged evidence retains all 39 rows and every content hash; working/staged bytes equal
```
