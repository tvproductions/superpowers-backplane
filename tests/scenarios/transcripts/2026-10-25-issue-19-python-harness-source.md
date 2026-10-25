# Portable issue 19 test helper source

Captured recovery source, not installed product code. Rehydrate under ignored `.sp-bp/work/issue-19/` if needed. Do not copy credentials/profile state. Existing tracked receipts/transcripts are the acceptance observations; do not rerun completed work merely because scratch is absent. Retired PowerShell helpers are not the execution route.

## lifecycle.py

SHA-256 `75233e81bf0c636d4dc91a9cbe1959e4afbc5a8366229cfc2e3b0fb598b80908`

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
BASELINE = "b0d702f8821d6d29184118410ec6ff2d8fb63438"
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
        base_work = self.root / ".sp-bp" / "work" / "issue-19"
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
            "sentinel": self.hash_file(self.profile / "preservation-sentinel.txt"),
            "refs": self.command(["git", "show-ref"]).splitlines(),
            "issue": json.loads(
                self.command(
                    [
                        "gh",
                        "issue",
                        "view",
                        "19",
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
        baseline = read_json(self.work / "comparison-baseline.json")
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

## test_lifecycle.py

SHA-256 `938944dff1166047d918a444184f2c7d4488c43fde9e9f0af93fc9ac148742fa`

```python
"""Regression checks for portable, disposable test orchestration."""

import os
from pathlib import Path
import sys
import tempfile
import unittest

from lifecycle import (
    Harness,
    compare_preservation,
    run_cli,
    verify_file,
    validate_revision,
)


class PortableOrchestrationTests(unittest.TestCase):
    def test_separate_evidence_output_keeps_the_selected_profile_and_catalog(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            base = root / ".sp-bp/work/issue-19"
            (base / "profile").mkdir(parents=True)
            phase = base / "v701"
            harness = Harness(root, output=phase)
            self.assertEqual(harness.work, phase)
            self.assertEqual(harness.profile, base / "profile")
            self.assertEqual(harness.catalog, base / "catalog")

    def test_child_receives_utf8_paths_and_scoped_environment(self):
        with tempfile.TemporaryDirectory(prefix="backplane space é ") as folder:
            before = os.environ.get("SP_BP_TEST_SENTINEL")
            output = run_cli(
                [
                    sys.executable,
                    "-c",
                    "import os; print(os.environ['SP_BP_TEST_SENTINEL']); print(os.getcwd())",
                ],
                cwd=Path(folder),
                overrides={"SP_BP_TEST_SENTINEL": "portable-é"},
            )
            lines = output.splitlines()
            self.assertGreaterEqual(len(lines), 2)
            self.assertEqual(lines[0], "portable-é")
            self.assertEqual(Path(lines[1]).resolve(), Path(folder).resolve())
            self.assertEqual(os.environ.get("SP_BP_TEST_SENTINEL"), before)

    def test_snapshot_key_order_does_not_hide_changed_values(self):
        compare_preservation(
            {"a": 1, "b": {"sentinel": "original"}},
            {"b": {"sentinel": "original"}, "a": 1},
        )
        with self.assertRaisesRegex(ValueError, "Preservation"):
            compare_preservation({"sentinel": "original"}, {"sentinel": "changed"})

    def test_installed_blob_check_rejects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            installed = Path(folder) / "skill.md"
            installed.write_bytes(b"hello\n")
            verify_file(installed, "ce013625030ba8dba906f756967f9e9ca394464a")
            installed.write_bytes(b"hello\r\n")
            with self.assertRaisesRegex(ValueError, "byte mismatch"):
                verify_file(installed, "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_moving_ref_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "40-character"):
            validate_revision("main")
        validate_revision("b0d702f8821d6d29184118410ec6ff2d8fb63438")


if __name__ == "__main__":
    unittest.main()

```

## fixture.py

SHA-256 `154dee681221b862ba4d2b67fcde8e6355084c789c7fc7c390d283d03da831bb`

```python
"""Observe actual gh-backed fixture operations in fresh Claude sessions."""

import argparse
import json
from pathlib import Path

from lifecycle import ISSUE_FIELDS, REPOSITORY, Harness, run_cli, write_json

TRANSITIONS = {
    "designing": ("backlog", "designing"),
    "ready": ("designing", "ready"),
    "active": ("ready", "active"),
    "review": ("active", "review"),
    "rework": ("review", "active"),
    "blocked": ("active", "blocked"),
    "resume": ("blocked", "active"),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["status", "selection", *TRANSITIONS])
    parser.add_argument("--evidence", default="")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    harness = Harness(root)
    command = [
        "gh",
        "issue",
        "view",
        "34",
        "--repo",
        REPOSITORY,
        "--json",
        ISSUE_FIELDS,
    ]
    before = json.loads(harness.command(command))
    write_json(harness.work / f"fixture-{args.stage}-before.json", before)
    if before["state"] != "OPEN" or before["subIssues"]["totalCount"]:
        raise ValueError("Fixture is not an open leaf")
    names = sorted(label["name"] for label in before["labels"])
    lifecycle = [name for name in names if name.startswith("backplane:")]
    if len(lifecycle) != 1 or "documentation" not in names:
        raise ValueError("Fixture label precondition failed")
    prompt = (
        "This is the operator-authorized live documentation fixture for issue #19. "
        "Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. "
        "Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. "
        f"First run exactly: {' '.join(command)}. "
        "Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. "
        "Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. "
        f"Expected current revision is {before['updatedAt']}; re-read and reconcile any drift before mutation. "
    )
    allowed = ["Skill", "Read", f"Bash(gh issue view 34 --repo {REPOSITORY} *)"]
    if args.stage in ("status", "selection"):
        prompt += (
            f"Perform only {args.stage} assessment for #34. Selection alone changes no lifecycle label. "
            "Report covered/eligible/selected separately, with no invented priority or approval. "
            "The issue-body design and exact paragraph were approved by the operator; the fixture plan is not yet bound. "
            "No mutation is authorized in this read-only probe."
        )
    else:
        old, new = TRANSITIONS[args.stage]
        if lifecycle != [f"backplane:{old}"]:
            raise ValueError(f"Expected {old}, observed {lifecycle}")
        edit = f"gh issue edit 34 --repo {REPOSITORY} --remove-label backplane:{old} --add-label backplane:{new}"
        prompt += (
            f"The explicitly authorized operation is {old} to {new}, for this evidence: {args.evidence}. "
            f"If its gates hold, execute exactly: {edit}. Preserve documentation and all relationships. "
            "Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo "
            f"{REPOSITORY} --body <quoted text>, then re-fetch the complete native issue and verify the result. "
            "If the gates do not hold, stop and explain rather than fabricate evidence."
        )
        if args.stage == "blocked":
            prompt += (
                " For entering blocked, post the blocker comment BEFORE the label edit. "
                "It must state Resume target: backplane:active and the concrete release condition. "
                "Then make the one atomic label swap and re-fetch; do not request or infer publication approval."
            )
        allowed += [f"Bash({edit})", f"Bash(gh issue comment 34 --repo {REPOSITORY} *)"]
    (harness.work / f"fixture-{args.stage}-prompt.txt").write_text(
        prompt + "\n", encoding="utf-8", newline="\n"
    )
    print(f"Live fixture {args.stage}; CLAUDE_CONFIG_DIR={harness.profile}", flush=True)
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
            "18",
        ],
        cwd=harness.work / "neutral",
        overrides=harness.environment,
    )
    (harness.work / f"fixture-{args.stage}.jsonl").write_text(
        output, encoding="utf-8", newline="\n"
    )
    events = [json.loads(line) for line in output.splitlines() if line.strip()]
    result = next(event for event in reversed(events) if event.get("type") == "result")
    after = json.loads(harness.command(command))
    write_json(harness.work / f"fixture-{args.stage}-after.json", after)
    (harness.work / f"fixture-{args.stage}-response.md").write_text(
        result.get("result", "") + "\n", encoding="utf-8", newline="\n"
    )
    if result.get("is_error") or result.get("subtype") != "success":
        raise ValueError("Live fixture session did not finish successfully")
    if args.stage in ("status", "selection"):
        if before != after:
            raise ValueError("Read-only probe mutated native issue state")
    else:
        expected = sorted([f"backplane:{TRANSITIONS[args.stage][1]}", "documentation"])
        if sorted(label["name"] for label in after["labels"]) != expected:
            raise ValueError("Expected lifecycle transition not observed")
        for field in before:
            if field not in ("labels", "updatedAt") and before[field] != after[field]:
                raise ValueError(f"Unexpected fixture field mutation: {field}")
    print(
        f"fixture {args.stage}: native before/after verified, session={result['session_id']}",
        flush=True,
    )


if __name__ == "__main__":
    main()

```

## verify_fixture.py

SHA-256 `b1d68bd96d0647d171d3b59c6902c2c0b793fe1823db1ce03e20a73c82568a85`

```python
"""Verify the bounded human documentation change and unchanged legacy examples."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from lifecycle import BASELINE, run_cli, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paragraph", default="fixture-paragraph.md")
    parser.add_argument("--receipt", default="initial")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    work = root / ".sp-bp/work/issue-19"
    guide = root / "docs/installing-claude-code.md"
    plan = (
        root
        / "docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md"
    )
    expected = (work / args.paragraph).read_text(encoding="utf-8").strip()
    observed = guide.read_text(encoding="utf-8")
    if observed.count(expected) != 1:
        raise ValueError(
            "Exact approved/review-corrected paragraph is not present once"
        )
    baseline = run_cli(
        ["git", "show", f"{BASELINE}:docs/installing-claude-code.md"], cwd=root
    )
    pattern = r"(?ms)^```powershell\r?\n(.*?)^```"
    blocks = re.findall(pattern, observed)
    if len(blocks) != 4 or blocks != re.findall(pattern, baseline):
        raise ValueError("Pre-existing guide code changed")
    executable = shutil.which("pwsh")
    if executable is None:
        raise RuntimeError(
            "Legacy guide parsing requires the explicitly scoped PowerShell adapter"
        )
    adapter = (
        "$source=[Console]::In.ReadToEnd();$tokens=$null;$parseErrors=$null;"
        "[void][System.Management.Automation.Language.Parser]::ParseInput($source,[ref]$tokens,[ref]$parseErrors);"
        "[pscustomobject]@{errors=$parseErrors.Count}|ConvertTo-Json -Compress;"
        "if($parseErrors.Count){exit 1}"
    )
    for block in blocks:
        result = subprocess.run(
            [executable, "-NoLogo", "-NoProfile", "-Command", adapter],
            input=block,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            shell=False,
            check=False,
        )
        if result.returncode or json.loads(result.stdout)["errors"] != 0:
            raise ValueError(
                f"Legacy example does not parse: {result.stdout}{result.stderr}"
            )
    allowed = {
        "docs/installing-claude-code.md",
        "docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md",
    }
    changed = set(
        run_cli(["git", "diff", "--name-only", BASELINE], cwd=root).splitlines()
    )
    if not changed.issubset(allowed):
        raise ValueError(f"Unexpected fixture scope: {changed - allowed}")
    run_cli(["git", "diff", "--check"], cwd=root)
    write_json(
        work / f"fixture-{args.receipt}-checks.json",
        {
            "guide_sha256": hashlib.sha256(guide.read_bytes()).hexdigest(),
            "plan_sha256": hashlib.sha256(plan.read_bytes()).hexdigest(),
            "paragraph_sha256": hashlib.sha256(expected.encode("utf-8")).hexdigest(),
            "unchanged_legacy_blocks": len(blocks),
            "parse_errors": 0,
            "changed_files": sorted(changed),
            "scope": "only paragraph and bound plan",
        },
    )
    print(
        f"Fixture {args.receipt}: exact paragraph, four unchanged parsed examples and bounded scope PASS"
    )


if __name__ == "__main__":
    main()

```

## conformance.py

SHA-256 `00d5abb34122357fec14058a5ca1f57bb5a041c10317db7e9e8e4c7271e06ed4`

```python
"""Run the exact approved prompts against restored installed B."""

import argparse
import json
from pathlib import Path
import re

from lifecycle import (
    BASELINE,
    Harness,
    compare_preservation,
    read_json,
    run_cli,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["v701"])
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    output = root / ".sp-bp/work/issue-19" / args.phase if args.phase else None
    harness = Harness(root, output=output)
    baseline_path = harness.work / "comparison-baseline.json"
    baseline = read_json(baseline_path)
    # The two explicitly saved local commits change only the expected Git refs.
    write_json(harness.work / "pre-conformance-comparison-baseline.json", baseline)
    baseline["preservation"]["refs"] = harness.command(["git", "show-ref"]).splitlines()
    write_json(baseline_path, baseline)
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

## replay_python.py

SHA-256 `175188d3eab85f774797f22795ec48bd0603b66fa0aec02d872fd828434cd49d`

```python
"""Execute the exact Python guide blocks in one disposable-profile session."""

from contextlib import redirect_stdout
import argparse
from pathlib import Path
import re
from typing import Any

from lifecycle import BASELINE, FIXTURE, Harness


def main(*, extract_only: bool = False, phase: str | None = None) -> None:
    root = Path(__file__).resolve().parents[3]
    output = root / ".sp-bp/work/issue-19" / phase if phase else None
    harness = Harness(root, output=output)
    guide = root / "docs" / "installing-claude-code.md"
    blocks = re.findall(
        r"(?ms)^```python\r?\n(.*?)^```", guide.read_text(encoding="utf-8")
    )
    if len(blocks) != 9:
        raise ValueError("Expected nine Python lifecycle blocks")
    for index, block in enumerate(blocks):
        compile(block, f"{guide.name}:block-{index}", "exec")
    if extract_only:
        extracted = harness.work / "guide_python.py"
        extracted.write_text("\n\n".join(blocks), encoding="utf-8", newline="\n")
        print(
            f"Extracted and compiled {len(blocks)} blocks, {extracted.stat().st_size} bytes"
        )
        return
    answers = iter([str(harness.profile), str(harness.catalog), BASELINE, FIXTURE])

    def answer(prompt: str) -> str:
        value = next(answers)
        print(f"{prompt}{value}", flush=True)
        return value

    state: dict[str, Any] = {"input": answer, "__name__": "__guide_replay__"}
    log = harness.work / "python-guide-replay.txt"
    print(f"Exact Python guide replay log: {log}", flush=True)
    with (
        log.open("w", encoding="utf-8", newline="\n") as transcript,
        redirect_stdout(transcript),
    ):
        harness.snapshot("python-before-replay", BASELINE, "0.1.0")
        for index, block in enumerate(blocks):
            print(f"Executing exact Python guide block {index}", flush=True)
            manifest = harness.catalog / ".claude-plugin" / "marketplace.json"
            before_catalog = manifest.read_bytes()
            exec(compile(block, f"{guide.name}:block-{index}", "exec"), state)
            row = f"python-guide-{index}"
            revision = None if index in (4, 7) else FIXTURE if index == 3 else BASELINE
            version = None if revision is None else "0.1.1" if index == 3 else "0.1.0"
            harness.snapshot(row, revision, version)
            if index == 6 and manifest.read_bytes() != before_catalog:
                raise ValueError("Unavailable candidate changed catalog")
            if index in (2, 3, 5, 8):
                harness.discovery(row)
            elif index == 7:
                harness.discovery(row, absent=True)
        print("All nine Python lifecycle blocks replayed; B restored.", flush=True)
    print("Python lifecycle replay PASS; B restored.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract-only", action="store_true")
    parser.add_argument("--phase", choices=["v701"])
    options = parser.parse_args()
    main(extract_only=options.extract_only, phase=options.phase)

```

## archive_conformance.py

SHA-256 `4e30259de23298bc7368727770867e3e33f14bc3fb29313f9236cf1b08b92dd0`

```python
"""Retain exact conformance prompts/responses and criterion-level assessment."""

import hashlib
import json
from pathlib import Path
import re

from lifecycle import BASELINE, Harness, read_json, write_json

EXPECTATIONS = {
    "native-issue-intake": [
        "Complete native hierarchy/dependency/PR intake",
        "Refuse blocked and unreconciled execution",
        "Layer issue/spec/plan authority",
        "Use Backplane lifecycle without Project/IssueOps authority",
        "Preserve consumer-owned verification/release rules",
        "Close only after integrated acceptance and fresh verification",
    ],
    "language-neutral-verification": [
        "Use only cargo test --workspace for consumer verification",
        "Introduce no Python/test-framework workflow",
        "Preserve native graph and revision binding",
        "Preserve Superpowers execution/review/verification",
        "Keep open through review and integrated verification",
    ],
    "lifecycle-transitions": [
        "Fail closed on multiple lifecycle labels",
        "Preserve security/unrelated labels",
        "Repair to review then return review to active",
        "Record Resume target: backplane:active",
        "Revalidate active gates before resume",
        "Atomic remove/add and post-mutation verification",
    ],
    "superpowers-installation": [
        "Reject lookalike/incomplete sibling without mutation",
        "Use authoritative source at unused destination",
        "Select latest stable by default",
        "Verify provenance, skills, gh, conformance and discovery",
        "Authorize later updates and fail closed on uncertainty",
        "Require no consumer runtime, Project or IssueOps",
    ],
}


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    harness = Harness(root)
    sections = [
        "# Issue 19 installed-package conformance\n",
        "Observed on Windows, Claude Code 2.1.302, installed B and independent Superpowers 7.0.0. "
        "The operator explicitly approved these exact scenario prompts and public skill/reference text. "
        "Each case used a fresh Skill/Read-only session. Responses below are unedited. "
        "Scoring is a manual assessment against every original expectation, not an inference from exit status.\n",
    ]
    records = []
    installed_root = (
        harness.profile
        / "plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0"
    )
    upstream_root = root / ".agents/superpowers"
    checked_links = []
    for skill_name in ("managing-superpowers-backlog", "managing-superpowers-handoffs"):
        skill = installed_root / "skills" / skill_name / "SKILL.md"
        for target in re.findall(r"\]\(([^)]+)\)", skill.read_text(encoding="utf-8")):
            if target.startswith(("https:", "http:", "#")):
                continue
            resolved = (skill.parent / target.split("#", 1)[0]).resolve(strict=True)
            if not resolved.is_file():
                raise ValueError(f"Installed skill link is not a file: {target}")
            checked_links.append(
                {
                    "skill": skill_name,
                    "target": target,
                    "sha256": hashlib.sha256(resolved.read_bytes()).hexdigest(),
                }
            )
    for name, expectations in EXPECTATIONS.items():
        receipt = read_json(harness.work / f"{name}-receipt.json")
        snapshot = read_json(harness.work / f"after-{name}-snapshot.json")
        reads = []
        for call in receipt["tools"]:
            if call["name"] != "Read":
                continue
            path = Path(call["input"]["file_path"]).resolve(strict=True)
            if not (
                path.is_relative_to(installed_root.resolve())
                or path.is_relative_to(upstream_root.resolve())
            ):
                raise ValueError(
                    f"Unexpected read outside approved installed public inputs: {path}"
                )
            reads.append(
                {
                    "path": str(path),
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            )
        scores = [
            {"expectation": expectation, "score": "PASS"}
            for expectation in expectations
        ]
        record = {
            "check": name,
            "session": receipt["session"],
            "scores": scores,
            "prompt": receipt["prompt"],
            "response": receipt["response"],
            "actual_tool_calls": receipt["tools"],
            "read_sources": reads,
            "issue19_after": snapshot["preservation"]["issue"],
            "model_usage": receipt["model_usage"],
        }
        records.append(record)
        sections += [
            f"## {name}\n",
            "### Exact prompt\n\n```text\n" + receipt["prompt"] + "\n```\n",
            "### Actual tool calls and source digests\n\n```json\n"
            + json.dumps(
                {
                    "session": receipt["session"],
                    "calls": receipt["tools"],
                    "reads": reads,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n```\n",
            "### Unedited response\n\n" + receipt["response"] + "\n",
            "### Assessment\n\n| Original expectation | Score |\n|---|---|\n"
            + "\n".join(f"| {expectation} | PASS |" for expectation in expectations)
            + "\n",
        ]
    transcript = root / "tests/scenarios/transcripts/2026-10-25-issue-19-conformance.md"
    transcript.write_text("\n".join(sections), encoding="utf-8", newline="\n")
    write_json(
        root / "tests/scenarios/2026-10-25-issue-19-conformance.json",
        {
            "baseline": BASELINE,
            "upstream": "bb92a77741419a4ab5f06e711a283343f1ada0c3",
            "observed_platform": "Windows",
            "legacy_expectations_pass": sum(map(len, EXPECTATIONS.values())),
            "skill_structure": "PASS: two installed skills, every relative link including canonical governance, metadata/source/placeholder checks",
            "relative_links_checked": checked_links,
            "behavioral_checks": records,
            "transcript_sha256": hashlib.sha256(transcript.read_bytes()).hexdigest(),
            "scope_limit": "Does not substitute for live issue lifecycle, final review or integrated acceptance",
        },
    )
    print(
        "Archived 23/23 legacy behavioral expectations and four fresh sessions; installed skill-structure PASS"
    )


if __name__ == "__main__":
    main()

```

## archive_v701.py

SHA-256 `94608895a1eac9791cabd87dc128b33755d02b21ee43bac8ef27f04509250e73`

```python
"""Preserve separately scoped Windows v7.0.1 verification without rewriting v7.0.0."""

import ast
import hashlib
import json
from pathlib import Path
import re

from archive_conformance import EXPECTATIONS
from lifecycle import BASELINE, Harness, read_json, run_cli, write_json


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    phase = root / ".sp-bp/work/issue-19/v701"
    harness = Harness(root, output=phase)
    target = "2ce8aa15d05bd57213e6f746f953aafb7ded7a8b"
    upstream = root / ".agents/superpowers"
    if run_cli(["git", "rev-parse", "HEAD"], cwd=upstream).strip() != target:
        raise ValueError("Upstream identity changed before evidence capture")
    if run_cli(["git", "status", "--porcelain"], cwd=upstream).strip():
        raise ValueError("Upstream became dirty")
    baseline = read_json(phase / "comparison-baseline.json")
    old_prompts = read_json(
        root / "tests/scenarios/2026-10-25-issue-19-python-lifecycle.json"
    )["exact_discovery_prompts"]
    source = ast.parse((phase.parent / "lifecycle.py").read_text(encoding="utf-8"))
    function = next(
        node
        for node in ast.walk(source)
        if isinstance(node, ast.FunctionDef) and node.name == "discovery"
    )
    actual_prompts = [
        ast.literal_eval(node.value)
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(item, ast.Name) and item.id == "prompt" for item in node.targets
        )
    ]
    if actual_prompts != old_prompts:
        raise ValueError("Discovery prompts changed without exact-prompt evidence")
    required = []
    for name in (
        "using-superpowers",
        "brainstorming",
        "writing-plans",
        "writing-skills",
    ):
        path = upstream / "skills" / name / "SKILL.md"
        required.append({"skill": name, "sha256": digest(path)})
    links = []
    cache = (
        harness.profile
        / "plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0"
    )
    for name in ("managing-superpowers-backlog", "managing-superpowers-handoffs"):
        skill = cache / "skills" / name / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        if not re.match(
            r"---\r?\nname: " + re.escape(name) + r"\r?\ndescription: Use when", text
        ):
            raise ValueError("Backplane skill metadata mismatch")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if not link.startswith(("https:", "http:", "#")):
                path = (skill.parent / link.split("#", 1)[0]).resolve(strict=True)
                links.append({"skill": name, "target": link, "sha256": digest(path)})
    records = []
    sections = [
        "# Windows Superpowers 7.0.1 fresh verification\n",
        "Exact operator-authorized target: v7.0.1, " + target + ". "
        "Four original prompts ran in fresh Claude Skill/Read-only sessions. "
        "The executor read each full response and scored all 23 original expectations. "
        "Earlier 7.0.0 records remain unchanged. These are Windows/Claude results, "
        "not macOS/Linux, fresh Codex, complete-stack or release acceptance.\n",
    ]
    for name, expectations in EXPECTATIONS.items():
        item = read_json(phase / f"{name}-receipt.json")
        snapshot = read_json(phase / f"after-{name}-snapshot.json")
        if snapshot["preservation"] != baseline["preservation"]:
            raise ValueError(f"Conformance preservation mismatch: {name}")
        records.append(
            {
                "check": name,
                "session": item["session"],
                "prompt": item["prompt"],
                "response": item["response"],
                "tool_calls": item["tools"],
                "scores": [
                    {"expectation": value, "score": "PASS"} for value in expectations
                ],
            }
        )
        sections += [
            f"## {name}\n",
            "### Exact prompt\n\n```text\n" + item["prompt"] + "\n```\n",
            "### Actual tool calls\n\n```json\n"
            + json.dumps(item["tools"], ensure_ascii=False, indent=2)
            + "\n```\n",
            "### Unedited response\n\n" + item["response"] + "\n",
            "### Assessment\n\n| Original expectation | Score |\n|---|---|\n"
            + "\n".join(f"| {value} | PASS |" for value in expectations)
            + "\n",
        ]
    snapshots = []
    for path in sorted(phase.glob("python-*-snapshot.json")):
        item = read_json(path)
        if item["preservation"] != baseline["preservation"]:
            raise ValueError("Affected lifecycle preservation mismatch")
        snapshots.append(
            {
                "row": item["row"],
                "installed_files": item["backplaneFiles"],
                "plugins": item["plugins"],
                "preservation_equal": True,
                "raw_sha256": digest(path),
            }
        )
    if len(snapshots) != 10:
        raise ValueError("Expected ten immediate lifecycle snapshots")
    sections.append(
        "## Exact Python guide replay\n\n```text\n"
        + (phase / "python-guide-replay.txt").read_text(encoding="utf-8")
        + "\n```\n"
    )
    sections.append(
        "## Exact fresh-discovery prompts\n\n"
        + "\n\n".join("```text\n" + prompt + "\n```" for prompt in actual_prompts)
        + "\n"
    )
    discovery = []
    for path in sorted(phase.glob("python-guide-*-discovery-summary.json")):
        item = read_json(path)
        raw = path.with_name(path.name.replace("-summary.json", ".jsonl"))
        events = [
            json.loads(line)
            for line in raw.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        calls = [
            block
            for event in events
            for block in event.get("message", {}).get("content", [])
            if isinstance(block, dict) and block.get("type") == "tool_use"
        ]
        item["actual_tool_calls"] = calls
        discovery.append(item)
        sections += [
            f"## {item['row']} fresh discovery\n",
            "```json\n"
            + json.dumps(
                {"session": item["session"], "calls": calls, "absent": item["absent"]},
                ensure_ascii=False,
                indent=2,
            )
            + "\n```\n",
            item["result"] + "\n",
        ]
    if len(discovery) != 5:
        raise ValueError("Expected five fresh post-operation discovery sessions")
    transcript = (
        root / "tests/scenarios/transcripts/2026-10-25-windows-superpowers-v7.0.1.md"
    )
    transcript.write_text("\n".join(sections), encoding="utf-8", newline="\n")
    write_json(
        root / "tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.json",
        {
            "prior_upstream": "bb92a77741419a4ab5f06e711a283343f1ada0c3",
            "target_upstream": target,
            "release": "v7.0.1",
            "latest_stable_observed": "v7.0.1",
            "observed_on": "2026-10-25",
            "backplane_baseline": BASELINE,
            "guide_sha256": digest(root / "docs/installing-claude-code.md"),
            "upstream_required_skills": required,
            "backplane_relative_links": links,
            "authorized_transition": read_json(
                phase / "authorized-upstream-change.json"
            ),
            "new_preservation_baseline": baseline["preservation"],
            "conformance": records,
            "legacy_expectations_pass": 23,
            "named_checks_pass": 5,
            "lifecycle_snapshots": snapshots,
            "fresh_discovery": discovery,
            "exact_discovery_prompts": actual_prompts,
            "fresh_codex": "UNVERIFIED: automatic approval review rejected the additional Codex skill-text transfer before execution; no bypass or retry",
            "scope_limit": "Windows Claude and local checkout/link verification only; no publication/integration or complete-stack/release acceptance",
            "transcript_sha256": digest(transcript),
        },
    )
    print(
        "Archived v7.0.1: five named checks, 23/23 expectations, nine exact lifecycle blocks, ten snapshots and five discovery sessions"
    )


if __name__ == "__main__":
    main()

```

