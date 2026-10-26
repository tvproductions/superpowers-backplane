# Verification workspace policy proof source

The companion JSON receipt records the observed passing fixture commands and preservation assertions. Public starter source bodies are omitted from the receipt; their immutable source identity and reviewed hashes are retained. The first fixture was preserved after an adapter whitespace-comparison assertion; the passing run used a new unused fixture.

Source SHA-256: `0ccd443cefa4f698bcd4b46a65f19a5f78343af7db1565092da2ee69fdbbdd5d`

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
    command(["git", "-C", str(FIXTURE), "status", "--porcelain=v1"])
    == "M sentinel.txt"
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
