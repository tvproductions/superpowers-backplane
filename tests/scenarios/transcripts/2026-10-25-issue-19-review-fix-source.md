# Whole-review fix and helper follow-up source

Test-only helpers, formatted and checked by Ruff and ty. Earlier execution-source captures remain unchanged. The two ty diagnostics were resolved by narrowing the pwsh executable and removing unnecessary console reconfiguration.

## shared_catalog.py

SHA-256: `51725f764f0636cdbbfd75fd0ff2481849a5f93bec62523c22d8fe99f08643a1`

````python
"""Observe native Backplane-only uninstall with a same-catalog sentinel."""

import argparse
import hashlib
import json
from pathlib import Path

from lifecycle import BACKPLANE, BASELINE, Harness, read_json, write_json

parser = argparse.ArgumentParser()
parser.add_argument("--negative-control", action="store_true")
args = parser.parse_args()
root = Path.cwd()
base = root / ".sp-bp/work/issue-19"
out = base / "shared-catalog"
out.mkdir(exist_ok=True)
(out / "neutral").mkdir(exist_ok=True)
h = Harness(root, output=out)
catalog = h.catalog / ".claude-plugin/marketplace.json"
sentinel_name = "issue19-preservation-sentinel"
sentinel_id = sentinel_name + "@superpowers-backplane"
original_bytes = catalog.read_bytes()
original = read_json(catalog)
if args.negative_control:
    assert any(p["name"] == sentinel_name for p in original["plugins"]), (
        "Missing actual unrelated entry in the Backplane marketplace: shared-entry preservation remains unproved"
    )
    raise SystemExit("Unexpected pre-existing sentinel")
assert (
    len(original["plugins"]) == 1
    and original["plugins"][0]["source"]["sha"] == BASELINE
)
assert not (out / "complete.json").exists(), "Preserve prior completed evidence"
(out / "original-catalog.json").write_bytes(original_bytes)
log = []


def command(*arguments):
    result = h.command(list(arguments))
    log.append({"arguments": arguments, "output": result})
    write_json(out / "native-commands.json", log)
    return result


def hashes(folder):
    return {
        p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in folder.rglob("*")
        if p.is_file()
    }


sentinel = h.catalog / sentinel_name
(sentinel / ".claude-plugin").mkdir(parents=True, exist_ok=True)
write_json(
    sentinel / ".claude-plugin/plugin.json",
    {
        "name": sentinel_name,
        "version": "0.0.0",
        "description": "Disposable same-marketplace preservation sentinel; no executable behavior",
    },
)
(sentinel / "README.md").write_text(
    "Issue 19 disposable preservation sentinel. No executable behavior.\n",
    encoding="utf-8",
    newline="\n",
)
candidate = json.loads(original_bytes)
candidate["plugins"].append(
    {
        "name": sentinel_name,
        "description": "Disposable same-marketplace preservation sentinel",
        "source": "./" + sentinel_name,
    }
)
write_json(catalog, candidate)
command("claude", "plugin", "marketplace", "update", "superpowers-backplane")
command("claude", "plugin", "install", sentinel_id, "--scope", "user")
registry = read_json(h.profile / "plugins/installed_plugins.json")["plugins"]
assert sentinel_id in registry and BACKPLANE in registry
known = read_json(h.profile / "plugins/known_marketplaces.json")
assert Path(known["superpowers-backplane"]["installLocation"]).resolve() == h.catalog
baseline = read_json(base / "final-guide/final-guide-after-discovery-snapshot.json")
before_refs = dict(
    line.split(" ", 1)[::-1] for line in baseline["preservation"]["refs"]
)
now_lines = h.command(["git", "show-ref"]).splitlines()
now_refs = dict(line.split(" ", 1)[::-1] for line in now_lines)
assert {
    k
    for k in before_refs.keys() | now_refs.keys()
    if before_refs.get(k) != now_refs.get(k)
} <= {"refs/heads/recovery/issue-19-windows"}
baseline["preservation"]["refs"] = now_lines
baseline["plugins"] = json.loads(command("claude", "plugin", "list", "--json"))
write_json(out / "comparison-baseline.json", baseline)
before = h.snapshot("before-uninstall", BASELINE, "0.1.0")
catalog_hashes = hashes(h.catalog)
sentinel_registry = registry[sentinel_id]
installed_sentinel = Path(sentinel_registry[0]["installPath"])
sentinel_hashes = hashes(installed_sentinel)
command("claude", "plugin", "uninstall", BACKPLANE, "--scope", "user")
after = h.snapshot("after-uninstall", None, None)
assert hashes(h.catalog) == catalog_hashes, "Shared catalog or source sentinel changed"
assert read_json(h.profile / "plugins/known_marketplaces.json") == known, (
    "Marketplace registration changed"
)
assert (
    read_json(h.profile / "plugins/installed_plugins.json")["plugins"][sentinel_id]
    == sentinel_registry
)
assert hashes(installed_sentinel) == sentinel_hashes, "Installed sentinel changed"
write_json(
    out / "uninstall-preservation.json",
    {
        "result": "PASS",
        "catalog_hashes": catalog_hashes,
        "sentinel_registry": sentinel_registry,
        "sentinel_hashes": sentinel_hashes,
        "marketplace_registration": known,
        "backplane_absent": True,
    },
)
command("claude", "plugin", "install", BACKPLANE, "--scope", "user")
h.snapshot("restored-B-shared-catalog", BASELINE, "0.1.0")
h.discovery("shared-catalog-restored-B")
h.snapshot("after-discovery-shared-catalog", BASELINE, "0.1.0")
assert hashes(h.catalog) == catalog_hashes
assert (
    read_json(h.profile / "plugins/installed_plugins.json")["plugins"][sentinel_id]
    == sentinel_registry
)
command("claude", "plugin", "uninstall", sentinel_id, "--scope", "user")
catalog.write_bytes(original_bytes)
command("claude", "plugin", "marketplace", "update", "superpowers-backplane")
assert catalog.read_bytes() == original_bytes
assert (
    sentinel_id
    not in read_json(h.profile / "plugins/installed_plugins.json")["plugins"]
)
baseline["plugins"] = [p for p in baseline["plugins"] if p["id"] != sentinel_id]
write_json(out / "comparison-baseline.json", baseline)
h.snapshot("final-restored-B-dedicated-catalog", BASELINE, "0.1.0")
write_json(
    out / "complete.json",
    {
        "result": "PASS",
        "baseline": BASELINE,
        "sentinel": sentinel_id,
        "same_marketplace": "superpowers-backplane",
        "native_uninstall_preservation": "exact catalog/source/installed sentinel/registry/marketplace registration unchanged",
        "restoration": "B exact 21 source blobs and fresh three-skill discovery; sentinel then removed natively and exact original catalog bytes restored",
        "negative_control": "Before fixture setup, assertion failed because no actual shared-catalog sentinel existed",
        "product_change": "none",
        "scope": "Windows disposable profile; no normal profile, upstream, other issue or repository ref mutation",
    },
)
print(
    "Shared catalog preservation PASS; B and original dedicated catalog restored",
    flush=True,
)
````

## integration-approval/prepare.py

SHA-256: `ddf09adcd5726ddcc7955499e8b3ade72ed264e90f46e5f853b38d2d4b3f585a`

````python
"""Reconcile the approved fixture's publication, retaining native snapshots."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lifecycle import Harness, ISSUE_FIELDS, REPOSITORY, write_json

h = Harness(Path.cwd())
out = Path(__file__).resolve().parent
before = json.loads(
    h.command(
        ["gh", "issue", "view", "34", "--repo", REPOSITORY, "--json", ISSUE_FIELDS]
    )
)
assert before["updatedAt"] == "2026-10-25T17:07:58Z"
assert sorted(x["name"] for x in before["labels"]) == [
    "backplane:blocked",
    "documentation",
]
write_json(out / "editorial-before.json", before)
old = "The local plan is not yet published; publication/integration require separately presented operator approval."
new = "The exact plan is now published at https://github.com/tvproductions/superpowers-backplane/blob/22c5b8d917a09f275c23d99bd9c9645d6c1d2e35/docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md . The operator explicitly approved PR creation, merge after fresh verification, integrated-byte verification and completed closure in the resumed session. This changes artifact availability and integration authority only; scope, acceptance and native graph are unchanged."
assert before["body"].count(old) == 1
body = (
    before["body"]
    .replace(old, new)
    .replace("at local commit `33d4300", "at original plan commit `33d4300")
)
p = out / "issue-body.md"
p.write_text(body, encoding="utf-8")
h.command(["gh", "issue", "edit", "34", "--repo", REPOSITORY, "--body-file", str(p)])
after = json.loads(
    h.command(
        ["gh", "issue", "view", "34", "--repo", REPOSITORY, "--json", ISSUE_FIELDS]
    )
)
assert after["body"] == body
for key in before:
    if key not in ("body", "updatedAt"):
        assert before[key] == after[key], key
write_json(out / "editorial-after.json", after)
(out / "pr-body.md").write_text(
    "Clarify that editing a local marketplace checkout does not prove a hosted update. Require installed commit, version and file hashes to match the selected immutable source, followed by a restart and direct discovery of all three skills.\n\nRefs #34. This PR contributes the exact reviewed paragraph and bound fixture plan; completed closure follows fresh integrated verification.\n\nReview: the independent reviewer's content-comparison finding was corrected at `22c5b8d`; focused confirmation found no remaining fixture findings.\n\nValidation: exact corrected paragraph, four unchanged PowerShell blocks parsed without errors, bounded two-file scope and `git diff --check` passed immediately before PR creation. Lifecycle B/F observations remain scoped to their recorded evidence. No package/version change or #19 acceptance is included.\n",
    encoding="utf-8",
)
print("Editorial reconciliation verified:", after["updatedAt"], flush=True)
print(h.command(["claude", "auth", "status"]), flush=True)
print(h.command(["claude", "plugin", "list", "--json"]), flush=True)
````

## integration-approval/close_fixture.py

SHA-256: `7a160af38b0e6b6351124d6785958b329a538877c9cf4897e3c5aa356d1ebf56`

````python
"""Observe verified fixture completion in a restricted fresh Claude session."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lifecycle import Harness, ISSUE_FIELDS, REPOSITORY, run_cli, write_json

root = Path.cwd()
out = Path(__file__).resolve().parent
h = Harness(root, output=out)
command = ["gh", "issue", "view", "34", "--repo", REPOSITORY, "--json", ISSUE_FIELDS]
before = json.loads(h.command(command))
write_json(out / "close-before.json", before)
assert before["state"] == "OPEN"
assert sorted(x["name"] for x in before["labels"]) == [
    "backplane:review",
    "documentation",
]
receipt = json.loads((out / "integrated-verification.json").read_text(encoding="utf-8"))
assert receipt["result"] == "PASS"
prompt = (
    "Operator-authorized real issue #34 verified completion under issue #19's approved useful fixture. "
    "Invoke installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog; read required references. "
    "Use gh only for GitHub and only issue 34 or PR 35 in tvproductions/superpowers-backplane. "
    f"First run exactly {' '.join(command)}. Expected revision {before['updatedAt']}; reconcile any drift. "
    "The operator explicitly approved this exact reviewed two-file PR creation, merge, integrated verification and completed closure. "
    f"Current fresh integrated verification receipt supplied by the operator's executor: {json.dumps(receipt)}. "
    "This session must inspect actual PR 35 merged state and full native issue intake before closure. "
    "The independent reviewer accepted the corrected paragraph at head 22c5b8d917a09f275c23d99bd9c9645d6c1d2e35 after its real Important finding was fixed. "
    "No remaining fixture findings. This does not establish #19 satisfaction. "
    "The exact issue acceptance criteria are satisfied by the integrated paragraph, immutable source matching requirement, post-restart actual skill discovery requirement and preserved documentation label. "
    "Reconcile editorial publication/approval and lifecycle/comment changes against semantic revision 2026-10-25T16:50:27Z; do not invent requirement changes. "
    "If every completion gate holds, post a concise evaluation comment including exact integration commit, reviewed head, guide/plan blobs, four unchanged parsed blocks, source-evidence scope, accepted review and no remaining fixture obligations. "
    "Then re-fetch full issue contract and relationships IMMEDIATELY before closure and reconcile any changed updatedAt. "
    "Close using gh issue close 34 --repo tvproductions/superpowers-backplane --reason completed, then remove only backplane:review using gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:review. "
    "Re-fetch full issue and verify CLOSED/COMPLETED with only documentation and unchanged native graph. "
    "Do not mutate #19, #11, other issues, local files, Git, plugins, Projects, releases or branches. If evidence is missing, stop and report it. "
)
(out / "close-prompt.txt").write_text(prompt, encoding="utf-8", newline="\n")
allowed = [
    "Skill",
    "Read",
    f"Bash(gh issue view 34 --repo {REPOSITORY} *)",
    f"Bash(gh pr view 35 --repo {REPOSITORY} *)",
    f"Bash(gh issue comment 34 --repo {REPOSITORY} *)",
    f"Bash(gh issue close 34 --repo {REPOSITORY} --reason completed)",
    f"Bash(gh issue edit 34 --repo {REPOSITORY} --remove-label backplane:review)",
]
print("Fresh verified-completion fixture session", flush=True)
output = run_cli(
    [
        "claude",
        "-p",
        prompt,
        "--tools",
        "Skill,Read,Bash",
        "--allowedTools",
        *allowed,
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-turns",
        "22",
    ],
    cwd=out / "neutral",
    overrides=h.environment,
)
(out / "close.jsonl").write_text(output, encoding="utf-8", newline="\n")
events = [json.loads(line) for line in output.splitlines() if line.strip()]
result = next(event for event in reversed(events) if event.get("type") == "result")
(out / "close-response.md").write_text(
    result.get("result", "") + "\n", encoding="utf-8", newline="\n"
)
after = json.loads(h.command(command))
write_json(out / "close-after.json", after)
assert result.get("subtype") == "success" and not result.get("is_error")
assert after["state"] == "CLOSED" and after["stateReason"] == "COMPLETED"
assert [x["name"] for x in after["labels"]] == ["documentation"]
for key in before:
    if key not in ("labels", "updatedAt", "state", "stateReason"):
        assert before[key] == after[key], key
print(
    "Fresh fixture verified-completion PASS; session=" + result["session_id"],
    flush=True,
)
````

## archive_closeout.py

SHA-256: `45c695523b08acb99125e6ab8d109201821d5d875f81408b106f04ec29c2d897`

````python
"""Retain fixture integration, closure and final guide seam evidence."""

import hashlib
import json
from pathlib import Path

from lifecycle import ISSUE_FIELDS, Harness, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "integration-approval"
h = Harness(root)
records = []
sections = [
    "# Issue 34 integration and verified completion\n",
    "Fresh Windows Claude sessions following explicit operator approval. Earlier fixture evidence remains unchanged. These results apply to #34 only; #19 and #11 remain open.\n",
]
for name, folder, prefix in [
    ("resume", work, "fixture-resume"),
    ("submission", out, "fixture-review"),
    ("completion", out, "close"),
]:
    events = [
        json.loads(line)
        for line in (folder / f"{prefix}.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    result = next(event for event in reversed(events) if event.get("type") == "result")
    assert result["subtype"] == "success" and not result.get("is_error")
    prompt = (folder / f"{prefix}-prompt.txt").read_text(encoding="utf-8")
    response = (folder / f"{prefix}-response.md").read_text(encoding="utf-8")
    calls = []
    results = []
    for event in events:
        message = event.get("message", {})
        if not isinstance(message, dict):
            continue
        for block in message.get("content", []):
            if isinstance(block, dict) and block.get("type") == "tool_use":
                calls.append({"name": block["name"], "input": block.get("input")})
            elif isinstance(block, dict) and block.get("type") == "tool_result":
                results.append(block)
    record = {
        "stage": name,
        "session": result["session_id"],
        "prompt": prompt,
        "response": response,
        "calls": calls,
        "tool_results": results,
        "before": json.loads(
            (folder / f"{prefix}-before.json").read_text(encoding="utf-8")
        ),
        "after": json.loads(
            (folder / f"{prefix}-after.json").read_text(encoding="utf-8")
        ),
        "raw_stream_sha256": hashlib.sha256(
            (folder / f"{prefix}.jsonl").read_bytes()
        ).hexdigest(),
    }
    assert any(
        call["name"] == "Skill"
        and call["input"]["skill"]
        == "superpowers-backplane:managing-superpowers-backlog"
        for call in calls
    )
    records.append(record)
    sections += [
        f"## {name}: {result['session_id']}\n",
        "### Exact prompt (JSON string preserves whitespace)\n",
        "```json\n" + json.dumps(prompt, ensure_ascii=False) + "\n```\n",
        "### Unedited response\n",
        response,
        "### Actual tool calls and results\n",
        "````json\n"
        + json.dumps({"calls": calls, "results": results}, ensure_ascii=False, indent=2)
        + "\n````\n",
    ]
final = json.loads(
    h.command(
        [
            "gh",
            "issue",
            "view",
            "34",
            "--repo",
            "tvproductions/superpowers-backplane",
            "--json",
            ISSUE_FIELDS,
        ]
    )
)
assert final["state"] == "CLOSED" and final["stateReason"] == "COMPLETED"
assert [x["name"] for x in final["labels"]] == ["documentation"]
receipt = {
    "issue": final["url"],
    "semantic_revision": "2026-10-25T16:50:27Z",
    "approval": "Operator explicitly approved the presented #34 PR creation, merge after fresh verification, integrated verification and closure in resumed session",
    "integration": json.loads(
        (out / "integrated-verification.json").read_text(encoding="utf-8")
    ),
    "editorial_before": json.loads(
        (out / "editorial-before.json").read_text(encoding="utf-8")
    ),
    "editorial_after": json.loads(
        (out / "editorial-after.json").read_text(encoding="utf-8")
    ),
    "stages": records,
    "final_issue": final,
    "satisfaction": {
        "paragraph_integrated": "SATISFIED",
        "local_vs_hosted_distinction": "SATISFIED",
        "source_matching_and_actual_discovery_requirement": "SATISFIED",
        "real_lifecycle_preservation_and_verified_completion": "SATISFIED",
    },
    "limits": [
        "Fixture #34 only, no #19 or #11 closeout",
        "No tag, release, branch cleanup or Project operation",
        "Historical B/F behavior remains scoped to its original exact inputs",
    ],
}
write_json(root / "tests/scenarios/2026-10-25-issue-19-fixture-closeout.json", receipt)
(
    root / "tests/scenarios/transcripts/2026-10-25-issue-19-fixture-closeout.md"
).write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8", newline="\n")
print("Archived all three fresh fixture sessions and exact integrated verification")
````

## final_guide.py

SHA-256: `d0419df655e88cca1a9cd81cf6f414870efc18ccbd41b6f5b3b78055ccd1ef79`

````python
"""Verify final guide seams, retaining prior exact executable-block replay."""

import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

from lifecycle import BASELINE, Harness, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "final-guide"
out.mkdir(exist_ok=True)
(out / "neutral").mkdir(exist_ok=True)
h = Harness(root, output=out)
old = json.loads((work / "v701/comparison-baseline.json").read_text(encoding="utf-8"))


def refs(lines):
    return dict(line.split(" ", 1)[::-1] for line in lines)


prior = refs(old["preservation"]["refs"])
current_lines = h.command(["git", "show-ref"]).splitlines()
current = refs(current_lines)
changed = [k for k in prior.keys() | current.keys() if prior.get(k) != current.get(k)]
allowed = {
    "refs/heads/main",
    "refs/heads/recovery/issue-19-windows",
    "refs/remotes/origin/main",
    "refs/remotes/origin/recovery/issue-19-windows",
    "refs/remotes/origin/test/issue-19-doc-lifecycle",
    "refs/remotes/origin/HEAD",
}
assert set(changed) <= allowed, changed
assert (
    h.command(["git", "symbolic-ref", "refs/remotes/origin/HEAD"]).strip()
    == "refs/remotes/origin/main"
)
write_json(
    out / "authorized-ref-delta.json",
    {
        "changed": {
            k: {"before": prior.get(k), "after": current.get(k)} for k in changed
        },
        "authority": "operator handoff/sync plus explicit fixture PR merge approval and approved recovery incorporation; origin HEAD aliases main",
    },
)
old["preservation"]["refs"] = current_lines
write_json(out / "comparison-baseline.json", old)
guide = (root / "docs/installing-claude-code.md").read_text(encoding="utf-8")
previous = h.command(
    [
        "git",
        "show",
        "0bbd5821cb751afc8dfdfac8c6812007d6fb63a2:docs/installing-claude-code.md",
    ]
)
blocks = re.findall(r"(?ms)^```python\r?\n(.*?)^```", guide)
assert len(blocks) == 9 and blocks == re.findall(
    r"(?ms)^```python\r?\n(.*?)^```", previous
)
for i, block in enumerate(blocks):
    compile(block, f"guide:{i}", "exec")
legacy = re.findall(r"(?ms)^```powershell\r?\n(.*?)^```", guide)
assert len(legacy) == 4 and legacy == re.findall(
    r"(?ms)^```powershell\r?\n(.*?)^```", previous
)
adapter = "$source=[Console]::In.ReadToEnd();$tokens=$null;$errors=$null;[void][System.Management.Automation.Language.Parser]::ParseInput($source,[ref]$tokens,[ref]$errors);if($errors.Count){exit 1}"
pwsh = shutil.which("pwsh")
if pwsh is None:
    raise RuntimeError(
        "Legacy guide parsing requires the explicitly scoped PowerShell adapter"
    )
for block in legacy:
    subprocess.run(
        [pwsh, "-NoLogo", "-NoProfile", "-Command", adapter],
        input=block,
        text=True,
        encoding="utf-8",
        check=True,
    )
(out / "guide_python.py").write_text(
    "\n\n".join(blocks), encoding="utf-8", newline="\n"
)
paragraph = (
    (work / "fixture-corrected-paragraph.md").read_text(encoding="utf-8").strip()
)
assert guide.count(paragraph) == 1
h.command(
    [
        "git",
        "diff",
        "--check",
        "main...HEAD",
        "--",
        ".",
        ":(exclude)tests/scenarios/transcripts/2026-10-25-issue-19-python-harness-source.md",
        ":(exclude)tests/scenarios/transcripts/2026-10-25-issue-19-python-lifecycle.md",
    ]
)
write_json(
    out / "static-verification.json",
    {
        "result": "PASS",
        "head": h.command(["git", "rev-parse", "HEAD"]).strip(),
        "guide_sha256": hashlib.sha256(
            (root / "docs/installing-claude-code.md").read_bytes()
        ).hexdigest(),
        "python_blocks": 9,
        "python_unchanged_from": "0bbd5821cb751afc8dfdfac8c6812007d6fb63a2",
        "powershell_blocks": 4,
        "powershell_parse_errors": 0,
        "fixture_paragraph": "exact reviewed bytes once",
        "retained_replay": "tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.json; unchanged executable blocks and installed B/package inputs",
    },
)
h.snapshot("final-guide-before-discovery", BASELINE, "0.1.0")
h.discovery("final-guide")
h.snapshot("final-guide-after-discovery", BASELINE, "0.1.0")
````

## archive_final.py

SHA-256: `71378c81460706f3fb1add6f46193a3a0f986fe4f13680c2203e7cf74b1ed350`

````python
"""Capture final guide verification without rewriting historical evidence."""

import hashlib
import json
from pathlib import Path

from lifecycle import BASELINE, Harness, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "final-guide"
h = Harness(root, output=out)
validation = h.command(["claude", "plugin", "validate", "--strict", str(root)])
(out / "strict-validation.txt").write_text(validation, encoding="utf-8")
assert not h.command(
    [
        "git",
        "diff",
        "--name-only",
        BASELINE,
        "HEAD",
        "--",
        "skills",
        "plugin.json",
        ".claude-plugin",
    ]
).strip()
static = json.loads((out / "static-verification.json").read_text(encoding="utf-8"))
summary = json.loads(
    (out / "final-guide-discovery-summary.json").read_text(encoding="utf-8")
)
receipt = {
    "static": static,
    "discovery": summary,
    "before": json.loads(
        (out / "final-guide-before-discovery-snapshot.json").read_text(encoding="utf-8")
    ),
    "after": json.loads(
        (out / "final-guide-after-discovery-snapshot.json").read_text(encoding="utf-8")
    ),
    "authorized_ref_delta": json.loads(
        (out / "authorized-ref-delta.json").read_text(encoding="utf-8")
    ),
    "strict_package_validation": validation,
    "ruff": "PASS",
    "ty": "PASS",
    "regression_tests": "5/5 PASS",
    "package_skills_manifests_unchanged_from": BASELINE,
    "whitespace_exceptions": [
        "Historical raw SSH stderr trailing space at tests/scenarios/transcripts/2026-10-25-issue-19-python-lifecycle.md:147",
        "Extra blank EOF line in tests/scenarios/transcripts/2026-10-25-issue-19-python-harness-source.md:1282",
    ],
    "retained_conformance": "23/23 original expectations plus skill structure from 2026-10-25-windows-superpowers-v7.0.1.json; identical installed B and upstream 7.0.1, no canonical skill changes",
    "retained_lifecycle": "Nine byte-identical executable Python blocks fully replayed in v7.0.1 evidence; added paragraph contains no executable changes. No claim of a new full lifecycle replay.",
}
write_json(root / "tests/scenarios/2026-10-25-issue-19-final-guide.json", receipt)
events = [
    json.loads(line)
    for line in (out / "final-guide-discovery.jsonl")
    .read_text(encoding="utf-8")
    .splitlines()
    if line.strip()
]
blocks = []
for event in events:
    message = event.get("message", {})
    if isinstance(message, dict):
        blocks.extend(
            x
            for x in message.get("content", [])
            if isinstance(x, dict) and x.get("type") in ("tool_use", "tool_result")
        )
text = (
    "# Final guide fresh discovery\n\nSession: "
    + summary["session"]
    + "\n\n## Unedited response\n\n"
    + summary["result"]
    + "\n\n## Actual skill calls and results\n\n````json\n"
    + json.dumps(blocks, ensure_ascii=False, indent=2)
    + "\n````\n"
)
(root / "tests/scenarios/transcripts/2026-10-25-issue-19-final-guide.md").write_text(
    text, encoding="utf-8", newline="\n"
)
sections = [
    "# Resumed fixture tooling source\n",
    "These are test-only helpers under ignored scratch, not product runtime. The earlier source capture remains unchanged.\n",
]
for relative in [
    "integration-approval/prepare.py",
    "integration-approval/close_fixture.py",
    "archive_closeout.py",
    "final_guide.py",
    "archive_final.py",
]:
    path = work / relative
    source = path.read_text(encoding="utf-8")
    sections += [
        f"## {relative}\n\nSHA-256: `{hashlib.sha256(path.read_bytes()).hexdigest()}`\n",
        "````python\n" + source.rstrip() + "\n````\n",
    ]
(
    root / "tests/scenarios/transcripts/2026-10-25-issue-19-resumed-harness-source.md"
).write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8", newline="\n")
print("Final guide receipt, transcript and resumed helper source saved")
````
