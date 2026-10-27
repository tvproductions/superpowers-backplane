# Local main verification helper

SHA-256: `7a0cadd388d47749b211d5846e81cf93d0cc73b72bffced9639aa820c3cde7b7`

```python
"""Verify exact local main installation without publishing the reviewed branch."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from lifecycle_helpers import BACKPLANE, Harness, run_cli, write_json

root = Path.cwd().resolve(strict=True)
work = root / ".sp-bp/work/issue-11"
output = work / "local-merge-verification"
assert not output.exists()
output.mkdir()
target = "3fd26061c8c5d8a220e4791d662d0bcf6a69c6bb"
product = "91ea3bb7933b5aa2c7628595f17157810cafa701"
commands = []


def git(*args, cwd=root):
    value = run_cli(["git", *args], cwd=cwd)
    commands.append(
        {"argv": ["git", *args], "cwd": str(cwd), "exit": 0, "stdout": value}
    )
    return value.strip()


assert Path(git("rev-parse", "--show-toplevel")).samefile(root)
assert git("branch", "--show-current") == "main"
assert git("rev-parse", "HEAD") == target
assert not git("status", "--porcelain=v1")
assert git("rev-parse", "origin/main") == "66c4c4fa937cf6ad8111a0dc2293f10c5a3a07b4"
unchanged = git(
    "diff",
    "--name-only",
    product,
    target,
    "--",
    "skills",
    ".claude-plugin",
    "plugin.json",
    "README.md",
    "docs/installing-claude-code.md",
    "AGENTS.md",
    "SUPERPOWERS.md",
)
assert unchanged == ""
profiles = []
for name, profile, uid in (
    ("native", root / ".sp-bp/work/issue-19/profile", "superpowers@superpowers-dev"),
    ("official", work / "setup-profile", "superpowers@claude-plugins-official"),
):
    directory = output / name
    directory.mkdir()
    (directory / "neutral").mkdir()
    h = Harness(root, profile=profile, output=directory, upstream_id=uid)
    before = h.snapshot("before", product, "0.1.0", capture_only=True)
    profiles.append((name, h, before))
package = work / "fixtures/final-catalog/package"
assert package.resolve(strict=True).is_relative_to(
    (work / "fixtures").resolve(strict=True)
)
assert Path(git("rev-parse", "--show-toplevel", cwd=package)).samefile(package)
assert (
    git("remote", "get-url", "origin", cwd=package)
    == "https://github.com/tvproductions/superpowers-backplane.git"
)
assert git("rev-parse", "HEAD", cwd=package) == product
assert not git("status", "--porcelain=v1", cwd=package)
assert not (package / ".git/objects/info/alternates").exists()
with (work / "progress.md").open("a", encoding="utf-8", newline="\n") as ledger:
    ledger.write(
        f"\n- Local integration fixture before mutation: root={package}; origin canonical; prior={product}; target={target}; owned standalone non-shared fixture verified; operator chose local main merge.\n"
    )
git("fetch", "--no-tags", str(root), target, cwd=package)
assert Path(git("rev-parse", "--show-toplevel", cwd=package)).samefile(package)
git("checkout", "--detach", target, cwd=package)
assert git("rev-parse", "HEAD", cwd=package) == target
records = []
for name, h, before in profiles:
    native_commands = []
    for args in (
        ["plugin", "uninstall", BACKPLANE, "--scope", "user"],
        ["plugin", "install", BACKPLANE, "--scope", "user"],
        ["plugin", "validate", "--strict", str(root)],
    ):
        text = h.command(["claude", *args])
        native_commands.append({"argv": ["claude", *args], "exit": 0, "stdout": text})
    after = h.snapshot("after", target, "0.1.0", compare_to=before)
    h.discovery("merged-main")
    final = h.snapshot("after-discovery", target, "0.1.0", compare_to=after)
    records.append(
        {
            "mode": name,
            "before": before,
            "after": after,
            "after_discovery": final,
            "commands": native_commands,
            "discovery": json.loads(
                (h.work / "merged-main-discovery-summary.json").read_text(
                    encoding="utf-8"
                )
            ),
        }
    )
receipt = {
    "result": "PASS",
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "operator_choice": "1: merge reviewed branch into main locally",
    "target": target,
    "product_candidate": product,
    "source_changes_since_product": unchanged,
    "project_commands": commands,
    "profiles": records,
    "scope": "Exact local integrated target installation, 21 package blobs per profile, actual three-skill discovery, strict package validation and protected/unrelated preservation. Product/guide/upstream inputs unchanged from reviewed runs, retained with original identities. No push, remote arrival, PR, closure, release or cleanup.",
}
write_json(
    root / "tests/scenarios/2026-10-26-issue-11-local-merge-verification.json", receipt
)
source = Path(__file__)
transcript = [
    "# Local main verification helper",
    "",
    f"SHA-256: `{hashlib.sha256(source.read_bytes()).hexdigest()}`",
    "",
    "```python",
    source.read_text(encoding="utf-8").rstrip(),
    "```",
    "",
]
(
    root / "tests/scenarios/transcripts/2026-10-26-issue-11-local-merge-verification.md"
).write_text("\n".join(transcript), encoding="utf-8", newline="\n")
print(
    f"PASS: exact local main {target}; two independent profile installations/discovery; unchanged reviewed product bytes",
    flush=True,
)
```
