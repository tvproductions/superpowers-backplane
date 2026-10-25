# Integrated verification helpers

Test-only exact sources. Execution and storage identities remain distinct.

## verify_integrated.py

SHA-256: `7982c4ea3ed7f52d99a2444edf6e160a6fa8f64ae6f08422f64c729869ca8369`

````python
"""Verify exact integrated #19 inputs and fresh native installed delivery."""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from lifecycle import BASELINE, ISSUE_FIELDS, Harness, read_json, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "integrated"
out.mkdir(exist_ok=True)
(out / "neutral").mkdir(exist_ok=True)
h = Harness(root, output=out)
delivery = "7d7ecac36f8dc74ce1a0895ab934468332f92f53"
candidate = "ade4e438d156ea7bb68a5e3b009718fde3b39a43"
assert sys.version_info[:3] == (3, 14, 9)
assert h.command(["git", "rev-parse", "HEAD"]).strip() == delivery
tree = h.command(["git", "rev-parse", f"{delivery}^{{tree}}"]).strip()
assert tree == h.command(["git", "rev-parse", f"{candidate}^{{tree}}"]).strip()
assert not h.command(["git", "status", "--porcelain"]).strip()
issue = json.loads(
    h.command(
        [
            "gh",
            "issue",
            "view",
            "19",
            "--repo",
            "tvproductions/superpowers-backplane",
            "--json",
            ISSUE_FIELDS,
        ]
    )
)
assert (
    issue
    == read_json(root / "tests/scenarios/2026-10-25-issue-19-review-submission.json")[
        "after"
    ]
)
baseline = read_json(work / "py314/python-guide-8-snapshot.json")
prior_issue = baseline["preservation"]["issue"]
for key in prior_issue:
    if key not in ("labels", "updatedAt"):
        assert prior_issue[key] == issue[key], key
baseline["preservation"]["issue"] = issue
old_refs = dict(line.split(" ", 1)[::-1] for line in baseline["preservation"]["refs"])
ref_lines = h.command(["git", "show-ref"]).splitlines()
new_refs = dict(line.split(" ", 1)[::-1] for line in ref_lines)
delta = {
    k: {"before": old_refs.get(k), "after": new_refs.get(k)}
    for k in old_refs.keys() | new_refs.keys()
    if old_refs.get(k) != new_refs.get(k)
}
assert set(delta) <= {
    "refs/heads/main",
    "refs/heads/recovery/issue-19-windows",
    "refs/remotes/origin/main",
    "refs/remotes/origin/recovery/issue-19-windows",
    "refs/remotes/origin/HEAD",
}
baseline["preservation"]["refs"] = ref_lines
write_json(out / "comparison-baseline.json", baseline)
write_json(
    out / "authorized-delta.json",
    {
        "refs": delta,
        "issue": {"before": prior_issue, "after": issue},
        "authority": "operator-approved local evidence commits, final publication/PR36 merge and earlier authorized native review submission",
    },
)
guide = root / "docs/installing-claude-code.md"
text = guide.read_text(encoding="utf-8")
replay = read_json(root / "tests/scenarios/2026-10-25-issue-19-python-3.14.json")
assert hashlib.sha256(guide.read_bytes()).hexdigest() == replay["guide_sha256"]
blocks = re.findall(r"(?ms)^```python\r?\n(.*?)^```", text)
assert len(blocks) == 9
assert [hashlib.sha256(b.encode("utf-8")).hexdigest() for b in blocks] == replay[
    "blocks_sha256"
]
for i, block in enumerate(blocks):
    compile(block, f"integrated-guide:{i}", "exec")
legacy = re.findall(r"(?ms)^```powershell\r?\n(.*?)^```", text)
prior = h.command(["git", "show", f"{BASELINE}:docs/installing-claude-code.md"])
assert len(legacy) == 4 and legacy == re.findall(
    r"(?ms)^```powershell\r?\n(.*?)^```", prior
)
pwsh = shutil.which("pwsh")
if pwsh is None:
    raise RuntimeError("Legacy guide parser adapter unavailable")
adapter = "$source=[Console]::In.ReadToEnd();$tokens=$null;$errors=$null;[void][System.Management.Automation.Language.Parser]::ParseInput($source,[ref]$tokens,[ref]$errors);if($errors.Count){exit 1}"
for block in legacy:
    subprocess.run(
        [pwsh, "-NoLogo", "-NoProfile", "-Command", adapter],
        input=block,
        text=True,
        encoding="utf-8",
        check=True,
    )
strict = h.command(["claude", "plugin", "validate", "--strict", str(root)])
(out / "strict-validation.txt").write_text(strict, encoding="utf-8")
tracked = h.command(["git", "ls-tree", "-r", delivery]).splitlines()
candidate_tracked = h.command(["git", "ls-tree", "-r", candidate]).splitlines()
assert tracked == candidate_tracked
remote_tree = json.loads(
    h.command(
        [
            "gh",
            "api",
            f"repos/tvproductions/superpowers-backplane/git/trees/{tree}?recursive=1",
        ]
    )
)
assert not remote_tree.get("truncated")
remote_blobs = {x["path"]: x["sha"] for x in remote_tree["tree"] if x["type"] == "blob"}
for line in tracked:
    meta, path = line.split("\t", 1)
    assert remote_blobs[path] == meta.split()[2], path
h.snapshot("integrated-before-install", BASELINE, "0.1.0")
old_catalog = h.catalog / ".claude-plugin/marketplace.json"
(out / "prior-catalog.json").write_bytes(old_catalog.read_bytes())
commands = []


def native(*args):
    output = h.command(["claude", *args])
    commands.append({"args": ["claude", *args], "output": output})
    write_json(out / "native-commands.json", commands)


h.source(delivery)
native("plugin", "marketplace", "update", "superpowers-backplane")
native(
    "plugin",
    "uninstall",
    "superpowers-backplane@superpowers-backplane",
    "--scope",
    "user",
)
h.snapshot("integrated-after-uninstall", None, None)
native(
    "plugin",
    "install",
    "superpowers-backplane@superpowers-backplane",
    "--scope",
    "user",
)
h.snapshot("integrated-installed-D", delivery, "0.1.0")
h.discovery("integrated-D")
final = h.snapshot("integrated-final-D", delivery, "0.1.0")
write_json(
    out / "verification.json",
    {
        "result": "PASS",
        "delivery": delivery,
        "candidate": candidate,
        "identical_tree": tree,
        "remote_tracked_blobs_verified": len(tracked),
        "guide_sha256": replay["guide_sha256"],
        "python_blocks": 9,
        "unchanged_parsed_legacy_blocks": 4,
        "strict_validation": "PASS",
        "actual_runtime": sys.version,
        "installed_delivery": delivery,
        "installed_version": "0.1.0",
        "installed_source_files": len(final["backplaneFiles"]),
        "conformance_applicability": "Canonical skills, references and package manifests unchanged from B; retained exact 23/23 7.0.1 behavioral expectations and ten-link structure evidence. Fresh D discovery and exact installed blobs verified; no new behavioral prompt set claimed.",
        "lifecycle_applicability": "Exact nine Python blocks and runtime match the full Python3.14.9 replay; merged tree equals approved candidate. Native current delivery installed explicitly by documented reinstall because version remains 0.1.0.",
        "review": "Fresh whole-change review; sole Important shared-marketplace gap fixed with retained actual control; no unresolved Critical/Important findings",
        "deferred_minors": [
            "Historical SSH stderr trailing space",
            "Historical source-capture EOF blank line",
        ],
        "scope": "Windows Claude #19 only; #11, complete-stack and release acceptance remain separate",
    },
)
print(
    "Integrated exact tree, remote blobs, package, guide, installed D discovery and preservation PASS",
    flush=True,
)
````

## archive_integrated.py

SHA-256: `6c4a86be8926a8af365ae41b32176a6f61e2dc3dfba3722a568b81e222b0046b`

````python
"""Preserve #19 exact integrated-delivery verification separately from storage."""

import hashlib
import json
from pathlib import Path

from lifecycle import Harness, read_json, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "integrated"
h = Harness(root, output=out)
verification = read_json(out / "verification.json")
assert verification["result"] == "PASS"
summary = read_json(out / "integrated-D-discovery-summary.json")
events = [
    json.loads(line)
    for line in (out / "integrated-D-discovery.jsonl")
    .read_text(encoding="utf-8")
    .splitlines()
    if line.strip()
]
calls = []
for event in events:
    message = event.get("message", {})
    if isinstance(message, dict):
        calls.extend(
            block
            for block in message.get("content", [])
            if isinstance(block, dict)
            and block.get("type") in ("tool_use", "tool_result")
        )
receipt = {
    "verification": verification,
    "pr": json.loads(
        h.command(
            [
                "gh",
                "pr",
                "view",
                "36",
                "--repo",
                "tvproductions/superpowers-backplane",
                "--json",
                "number,url,state,headRefOid,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences",
            ]
        )
    ),
    "snapshots": [
        read_json(out / f"{name}-snapshot.json")
        for name in (
            "integrated-before-install",
            "integrated-after-uninstall",
            "integrated-installed-D",
            "integrated-final-D",
        )
    ],
    "commands": read_json(out / "native-commands.json"),
    "discovery": summary,
    "authorized_delta": read_json(out / "authorized-delta.json"),
    "strict_validation": (out / "strict-validation.txt").read_text(encoding="utf-8"),
    "regression_tests": "5/5 PASS freshly on integrated main, Python 3.14.9",
    "ruff": "PASS",
    "ty": "PASS",
    "whitespace": "All paths pass except two explicitly retained historical transcript-only minors",
    "ci": "PR36 statusCheckRollup empty; no CI run claimed",
    "closure": "Pending authorized native completed closure after this evaluation is published",
}
write_json(
    root / "tests/scenarios/2026-10-25-issue-19-integrated-verification.json", receipt
)
text = (
    "# Issue 19 integrated delivery discovery\n\nDelivery: `"
    + verification["delivery"]
    + "`. Fresh session: `"
    + summary["session"]
    + "`.\n\n## Unedited response\n\n"
    + summary["result"]
    + "\n\n## Actual tool calls and results\n\n````json\n"
    + json.dumps(calls, ensure_ascii=False, indent=2)
    + "\n````\n"
)
(
    root / "tests/scenarios/transcripts/2026-10-25-issue-19-integrated-verification.md"
).write_text(text, encoding="utf-8", newline="\n")
sections = [
    "# Integrated verification helpers\n",
    "Test-only exact sources. Execution and storage identities remain distinct.\n",
]
for name in ("verify_integrated.py", "archive_integrated.py"):
    path = work / name
    sections += [
        f"## {name}\n\nSHA-256: `{hashlib.sha256(path.read_bytes()).hexdigest()}`\n",
        "````python\n" + path.read_text(encoding="utf-8").rstrip() + "\n````\n",
    ]
(
    root / "tests/scenarios/transcripts/2026-10-25-issue-19-integrated-source.md"
).write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8", newline="\n")
print(
    "Integrated verification receipt, fresh discovery transcript and helper source saved"
)
````
