# Codex Installation Surface Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the two canonical Backplane skills installable and verifiable as one Codex plugin while upstream Superpowers remains a separate installation.

**Architecture:** The repository root is the plugin root. A portable root manifest exposes the existing `skills/` directory, and a repository marketplace entry points at that root. Codex owns package installation; the existing Backplane installation reference governs the user-requested upstream setup and preflight. No installer, hook, copied skill, or consuming-project runtime is introduced.

**Tech Stack:** Agent Plugins 1.0 JSON, Codex plugin marketplace and CLI, Markdown, Git, GitHub CLI (`gh`)

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`

**Issue:** https://github.com/tvproductions/superpowers-backplane/issues/3

**Issue revision consumed:** `2026-09-19T18:12:33Z`. The body and native relationships were unchanged when planning moved `backplane:backlog` to `backplane:designing`; the prior body revision was `2026-09-19T14:13:20Z`. Re-read complete native issue fields before execution and reconcile any later change.

## Global Constraints

- One canonical Backplane `skills/` tree at the repository root; no copied Backplane or upstream Superpowers content.
- Codex package ID `superpowers-backplane`; planned v0.1 package version `0.1.0`. Release tagging and publication belong to later authorized work.
- Install Backplane and upstream Superpowers independently. Adopt a compatible native upstream package or sibling checkout; obtain stable upstream through Codex's documented channel if absent. Never update upstream as a side effect.
- Package installation does not run setup. The user requests setup in a Codex session; `skills/managing-superpowers-backlog/references/installing-superpowers.md` supplies its preflight.
- Use immutable Git revisions for tested install, update, and rollback; a moving branch is not the default install target. Preserve unrelated plugins, user files, issues, and dirty checkouts.
- Require Git and authenticated, lifecycle-capable `gh`. Do not require a consuming-project language runtime, GitHub Projects, IssueOps, or pytest.
- The Codex row in `tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md`, all five named Backplane conformance checks, and fresh discovery of three skills are acceptance gates.
- Before every Git mutation, require `git rev-parse --show-toplevel` to equal `C:/Users/Jeff/source/repos/agents/superpowers-backplane` exactly. The current project rule prevents Git mutations from a linked worktree; create a feature branch in this standalone checkout at execution entry. Do not publish or release.

## Review Focus

1. A marketplace entry aimed at `./` might be skipped by Codex; Task 1 must prove the root plugin resolves exactly once, and Task 3 must prove both skills appear in a fresh session.
2. The current `.gitignore` excludes `.agents/`; Task 1 must prove the marketplace file is tracked while the upstream checkout and discovery junctions remain ignored.
3. A duplicate Backplane plugin or upstream package with unknown source could look usable; Task 3 must score the setup response as unresolved without changing existing installations or issue state.
4. A dirty authoritative upstream checkout is adoptable in place but unsafe to update; Task 3 must test that distinction independently of lookalike provenance.
5. Updating or uninstalling Backplane could disturb an unrelated marketplace entry or upstream plugin; Task 3 must compare their identities and hashes before and after each operation.

## Execution entry after plan approval

1. Re-read issue #3 through the complete native intake query in `skills/managing-superpowers-backlog/references/github-issue-contract.md`. Reconcile changes against the consumed semantic revision above.
2. Verify the exact Git top level, create a feature branch in this checkout, and commit this approved plan. Recheck the Git root before each Git mutation.
3. Replace only `Plan: not yet created.` in issue #3 with this plan path using a reviewed temporary body file and `gh issue edit --body-file`. Re-fetch the issue and record the resulting editorial `updatedAt` in the scenario evidence. With approved design, current plan, and closed blocker #2, move `backplane:designing` to `backplane:ready` in one `gh issue edit` call.
4. Re-read the issue immediately before the first execution task. Move `backplane:ready` to `backplane:active` as Task 1 starts, preserving unrelated labels. A change in scope, acceptance, or native blockers returns to reconciliation before execution.

---

### Task 1: Prove the root Codex package and marketplace

**Files:**
- Modify: `.gitignore`
- Create: `plugin.json`
- Create: `.agents/plugins/marketplace.json`
- Create: `tests/scenarios/2026-09-19-codex-installation.md`

**Interfaces:**
- Consumes: canonical root `skills/` and the approved package architecture.
- Produces: root `plugin.json` with `name: superpowers-backplane`, `version: 0.1.0`, and a marketplace named `superpowers-backplane` whose sole Backplane entry resolves the repository root. Task 2 documents this exact selector and Task 3 installs it.

- [ ] **Step 1: Recheck the host contract.** Read https://developers.openai.com/plugins/build/plugins and `codex plugin --help`, `codex plugin marketplace add --help`, and `codex plugin add --help` afresh. Record the Codex version and any changed manifest, root skill, marketplace, or CLI behavior before editing metadata.
- [ ] **Step 2: Capture RED.** In this standalone checkout, run `git check-ignore -v .agents/plugins/marketplace.json` and `codex plugin list --available --json` from the repository root. Filter the JSON output to the `superpowers-backplane` selector; do not paste the entire installed plugin catalog into the evidence file. Record that `.agents/` is ignored and that `superpowers-backplane@superpowers-backplane` is absent. Record `codex --version` and the filtered output.
- [ ] **Step 3: Add minimal metadata.** Change `.gitignore` to ignore `.agents/*` while allowing `.agents/plugins/marketplace.json`; keep `.agents/superpowers` and `.agents/skills` ignored. Create the portable manifest with `$schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`, `name: superpowers-backplane`, `version: 0.1.0`, `description: Native GitHub backlog continuity for upstream Superpowers`, and the repository URL. Create marketplace JSON with top-level `name: superpowers-backplane`, `interface.displayName: Superpowers Backplane`, and one entry with matching name, `source: {source: local, path: ./}`, `policy: {installation: AVAILABLE, authentication: ON_USE}`, and `category: Productivity`. Do not declare legacy `skills`, hooks, apps, or MCP fields; portable Codex discovers root `skills/` automatically.

  The manifest content is:

  ```json
  {
    "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
    "name": "superpowers-backplane",
    "version": "0.1.0",
    "description": "Native GitHub backlog continuity for upstream Superpowers",
    "repository": "https://github.com/tvproductions/superpowers-backplane"
  }
  ```

  The marketplace content is:

  ```json
  {
    "name": "superpowers-backplane",
    "interface": {"displayName": "Superpowers Backplane"},
    "plugins": [{
      "name": "superpowers-backplane",
      "source": {"source": "local", "path": "./"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
      "category": "Productivity"
    }]
  }
  ```

  Replace the single `.agents/` ignore rule with these lines, preserving the `.worktrees/` rule:

  ```gitignore
  .agents/*
  !.agents/plugins/
  .agents/plugins/*
  !.agents/plugins/marketplace.json
  ```

- [ ] **Step 4: Verify GREEN.** Parse both JSON files with the host's JSON reader; assert the exact names, version, root path, policy fields, and that each existing `skills/*/SKILL.md` has only one authored copy. Run `git check-ignore -v .agents/superpowers .agents/skills/superpowers`, then `git check-ignore -q .agents/plugins/marketplace.json`, and `git status --short --untracked-files=all`. The first command must show ignored paths; the second must exit 1, proving the marketplace is unignored; the status must show the new marketplace file. Recheck the exact Git root separately before `git add` and before `git commit`. Run `codex plugin list --available --json` from the repository root and require a resolvable `superpowers-backplane@superpowers-backplane` entry. If Codex rejects `./`, stop and reconcile the root-package marketplace path against the approved spec and current primary Codex docs before changing package layout.

  Use the current Windows host's PowerShell for the metadata assertions; this is a verification command, not a consuming-project runtime:

  ```powershell
  $manifest = Get-Content plugin.json -Raw | ConvertFrom-Json
  $marketplace = Get-Content .agents/plugins/marketplace.json -Raw | ConvertFrom-Json
  if ($manifest.name -ne 'superpowers-backplane' -or $manifest.version -ne '0.1.0') { throw 'Wrong plugin identity' }
  if ($manifest.'$schema' -ne 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json') { throw 'Wrong schema' }
  if ($marketplace.name -ne 'superpowers-backplane' -or @($marketplace.plugins).Count -ne 1) { throw 'Wrong marketplace identity' }
  $entry = $marketplace.plugins[0]
  if ($entry.name -ne 'superpowers-backplane' -or $entry.source.source -ne 'local' -or $entry.source.path -ne './') { throw 'Wrong root source' }
  if (@(Get-ChildItem skills -Recurse -Filter SKILL.md).Count -ne 2) { throw 'Unexpected canonical skill count' }
  $catalog = codex plugin list --available --json | ConvertFrom-Json
  $matching = @(@($catalog.installed) + @($catalog.available) | Where-Object pluginId -eq 'superpowers-backplane@superpowers-backplane')
  if ($matching.Count -ne 1) { throw 'Codex did not resolve the root package exactly once' }
  ```

- [ ] **Step 5: Commit the package slice.** Verify the exact Git top level, stage only these four files, run `git diff --cached --check`, commit `feat: add root Codex plugin package`, and record the commit SHA in the scenario file's later lifecycle evidence.

### Task 2: Document Codex install and setup preflight

**Files:**
- Modify: `README.md`
- Create: `docs/installing-codex.md`
- Modify: `tests/scenarios/2026-09-19-codex-installation.md`

**Interfaces:**
- Consumes: Task 1's resolved `superpowers-backplane@superpowers-backplane` selector and `skills/managing-superpowers-backlog/references/installing-superpowers.md`.
- Produces: a Codex install and setup guide. Task 3 adds lifecycle commands only after observing them in a disposable Codex profile.

- [ ] **Step 1: Capture RED.** Read the current `README.md` as an adopter. Record the absent pinned install command, explicit setup request, upstream provenance check, and fresh-session discovery check as four failing documentation expectations in the scenario file.
- [ ] **Step 2: Write the install path.** Link `docs/installing-codex.md` from `README.md`. In the guide, require a reviewed Backplane checkout at a published immutable commit, then show these exact PowerShell commands. Record the resolved SHA before installing; do not use moving `main` as the installed ref.

  ```powershell
  $backplaneRevision = (git rev-parse HEAD).Trim()
  codex plugin marketplace add tvproductions/superpowers-backplane --ref $backplaneRevision
  codex plugin add superpowers-backplane@superpowers-backplane
  codex plugin list --json
  ```

  The guide must state that package installation does not run setup. Direct the adopter to ask a new Codex session: `Set up Superpowers Backplane in this Codex session.` The setup response must report exactly one Backplane plugin, both canonical Backplane skills, an independently identified upstream Superpowers source and version/revision, authenticated lifecycle-capable `gh`, and fresh-session discovery of all three skills. If upstream is absent, follow Codex's upstream-documented stable channel; leave any upstream update separate under `SUPERPOWERS.md`.
- [ ] **Step 3: Verify the read-only preflight.** Re-read the current upstream Codex installation instructions and run `gh auth status`, `gh issue view 3 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`, `gh issue edit --help`, and `gh issue close --help`. Record the actual host version, upstream provenance, required skill paths, and `gh` capability results. A missing field or command is `UNKNOWN` compatibility; do not claim setup success.
- [ ] **Step 4: Commit the install guide.** Compare the guide with the approved spec and installation reference; require all four RED documentation expectations to be answered, with no implied upstream mutation or issue transition. Verify the exact Git top level before staging only the README, guide, and scenario; run `git diff --cached --check`; verify the root again before committing `docs: explain Codex installation and setup`.

### Task 3: Verify Codex lifecycle and finish the guide

**Files:**
- Modify: `docs/installing-codex.md`
- Modify: `tests/scenarios/2026-09-19-codex-installation.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-host-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-failure-probes.md`

**Interfaces:**
- Consumes: Task 2's install command, Task 1's package revision, and Codex's documented marketplace commands.
- Produces: observed install, repeat install, update, rollback, uninstall, and failure behavior with an executable guide. Task 4 uses this verified package state for fresh conformance.

- [ ] **Step 1: Establish a disposable host.** From the verified project root, create a temporary directory and archive the committed package with the commands below. The expanded project contains no `.git`, `.agents/superpowers`, or user configuration. Record the source commit and exact fixture paths in the scenario evidence. Create a separate temporary Codex state directory. Pass that directory as `CODEX_HOME` only to child `codex` processes and run `codex plugin marketplace list --json`; require no user marketplace in the fixture. Record the exact paths, `codex --version`, Backplane commit SHA, both Backplane skill hashes, upstream source/version or checkout commit, and `gh --version`. A failure to prove isolation stops install/remove tests against the live user profile.

  On the current Windows host, create and inspect the fixture with:

  ```powershell
  if ((git rev-parse --show-toplevel) -ne 'C:/Users/Jeff/source/repos/agents/superpowers-backplane') { throw 'Wrong repository root' }
  $fixtureRoot = Join-Path ([IO.Path]::GetTempPath()) ('backplane-codex-' + [guid]::NewGuid().ToString('N'))
  $fixtureProject = Join-Path $fixtureRoot 'project'
  $fixtureCodexState = Join-Path $fixtureRoot 'codex-state'
  $fixtureArchive = Join-Path $fixtureRoot 'backplane.zip'
  New-Item -ItemType Directory -Path $fixtureRoot | Out-Null
  New-Item -ItemType Directory -Path $fixtureProject, $fixtureCodexState | Out-Null
  git archive --format=zip HEAD -o $fixtureArchive
  if ($LASTEXITCODE -ne 0) { throw 'Could not archive the committed package' }
  Expand-Archive -LiteralPath $fixtureArchive -DestinationPath $fixtureProject
  $fixtureOutput = Join-Path $fixtureRoot 'marketplaces.json'
  $fixtureError = Join-Path $fixtureRoot 'marketplaces.stderr.txt'
  $fixtureProcess = Start-Process -FilePath (Get-Command codex).Source -ArgumentList @('plugin','marketplace','list','--json') -WorkingDirectory $fixtureRoot -Environment @{ CODEX_HOME = $fixtureCodexState } -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput $fixtureOutput -RedirectStandardError $fixtureError
  if ($fixtureProcess.ExitCode -ne 0) { throw 'Isolated Codex marketplace listing failed' }
  Get-Content $fixtureOutput -Raw | ConvertFrom-Json | Select-Object -ExpandProperty marketplaces | Select-Object name,root
  ```

- [ ] **Step 2: Seed a preservation sentinel.** In a disposable copy of the marketplace, add a second plugin entry pointing to a temporary sibling folder with a valid portable manifest named `backplane-preservation-sentinel` at version `0.0.1`. Install that entry in the isolated Codex state and record its plugin ID, marketplace entry, and file hashes. Leave the tracked repository marketplace at one Backplane entry. This sentinel must survive Backplane update, rollback, and uninstall.

  The fixture-only plugin manifest at `$fixtureProject/backplane-preservation-sentinel/plugin.json` is:

  ```json
  {
    "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
    "name": "backplane-preservation-sentinel",
    "version": "0.0.1",
    "description": "Disposable preservation probe"
  }
  ```

  Append this entry to the fixture copy of `$fixtureProject/.agents/plugins/marketplace.json`:

  ```json
  {
    "name": "backplane-preservation-sentinel",
    "source": {"source": "local", "path": "./backplane-preservation-sentinel"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
    "category": "Productivity"
  }
  ```

  Then add that local marketplace and install `backplane-preservation-sentinel@superpowers-backplane` using child `codex plugin marketplace add` and `codex plugin add` processes with the fixture's `CODEX_HOME`. Record `codex plugin list --json` and file hashes before changing Backplane.

- [ ] **Step 3: Score positive modes.** In three separately seeded disposable Codex states, install the preservation sentinel and run setup with an authoritative native Superpowers package, an authoritative sibling checkout, and no upstream installation. In the absent case, obtain the latest compatible stable upstream only through Codex's current upstream-documented channel. For each mode, record source/catalog or exact origin, version or commit, required upstream skills, `gh` preflight, and fresh-session discovery of `superpowers:using-superpowers` plus both Backplane skills. Repeat Backplane install and require one effective installation. Test update and rollback with two inspected package snapshots: use the committed `0.1.0` package as the prior version and a disposable copy whose only package change is a fixture-only `0.1.1` version in `plugin.json` as the candidate. Record both manifest hashes, the before/after installed versions, and the Codex commands that actually restore `0.1.0`. Never commit the fixture-only version to source. Remove Backplane with `codex plugin remove superpowers-backplane@superpowers-backplane`; preserve the sentinel, upstream, and user files.
- [ ] **Step 4: Score independent failures.** In disposable copies, separately test duplicate Backplane installation, unknown or versionless native upstream, dirty authoritative sibling checkout before upstream update, lookalike checkout origin, path collision, and missing `gh` native fields or lifecycle flags. A dirty authoritative checkout may be adopted in place but must not be updated. Each failure record must contain the observed failed check, a specific recovery action, unchanged sentinel/upstream/user-file hashes, and no GitHub issue mutation. Record `PASS`, `FAIL`, or `UNKNOWN` for every Codex matrix case.
- [ ] **Step 5: Write only verified lifecycle commands.** Complete `docs/installing-codex.md` with the exact observed Codex commands for changing the pinned marketplace ref, reinstalling the selected plugin, restoring the recorded prior ref, and uninstalling only Backplane. Include preflight before mutation, post-operation three-skill discovery, and restoration if candidate verification fails. If the host cannot pin or restore the prior version, mark rollback unsupported and keep issue #3 out of review until a tested recovery path exists. Re-run the written commands in the disposable host, then verify the exact Git root before staging the guide and evidence, run `git diff --cached --check`, verify the root again, and commit `test: verify Codex plugin lifecycle`.

### Task 4: Complete conformance, review, and integration evidence

**Files:**
- Modify: `tests/scenarios/2026-09-19-codex-installation.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-skill-structure.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-native-issue-intake.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-language-neutral-verification.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-lifecycle-transitions.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-superpowers-installation.md`
- Create: `tests/scenarios/transcripts/2026-09-19-codex-native-lifecycle.md`
- Modify: `docs/installing-codex.md` only for a correction proved by final verification

**Interfaces:**
- Consumes: Task 3's verified lifecycle and `skills/managing-superpowers-backlog/references/installing-superpowers.md` conformance rubric.
- Produces: fresh Codex session evidence for issue #3's acceptance and a reviewed branch ready for integration.

- [ ] **Step 1: Run all five conformance checks.** Execute `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation` as mapped in the installation reference. Use a fresh Codex session per behavioral prompt, preserve the exact prompt and response in `tests/scenarios/transcripts/`, and score every named expectation. Record the host version, Backplane SHA, upstream source/version or commit, `gh` capability result, and three skill identities. Missing capture or an unscored expectation is `UNKNOWN`.
- [ ] **Step 2: Score native lifecycle behavior.** Use issue #3's actual authorized designing, ready, and active transitions as integration evidence when their gates occur. Run status and selection prompts read-only against #3 and compare `updatedAt` and labels before and after. For blocked and review-reversal cases, use an explicitly authorized disposable issue; if none is available, record `UNKNOWN` and leave that acceptance gate open. Require exactly one Backplane label on an open issue and preservation of unrelated labels. Reserve issue #3's review and completed scores for Steps 3 and 4. Never use production backlog issues as disposable test data.
- [ ] **Step 3: Verify the branch and request review.** Require every pre-integration Codex matrix case and conformance expectation to be `PASS`; reserve the remote pinned install and issue #3 completion scores for Step 4. Run `git diff --check`, inspect tracked files for copied upstream content or duplicate Backplane skills, and confirm the exact Git root. Commit final response records after checking `git diff --cached --check`. Request code review and address findings through `superpowers:receiving-code-review`; then run `superpowers:verification-before-completion` and hand the branch to `superpowers:finishing-a-development-branch`.
- [ ] **Step 4: Verify the integrated Git source before closure.** After authorized integration makes the package revision available from the remote, require both the Task 1 package commit and the integrated package commit to remain reachable through immutable remote SHAs until verification finishes. In a disposable Codex state, install from the first SHA, update to the integrated SHA, roll back to the first SHA, and remove Backplane; run fresh three-skill discovery after each installed state. Record both resolved remote revisions and compare them with the reviewed commits. This remote probe checks pinned Git ref restoration; Task 3's fixture checks a version change. Do not present either probe as a released-version update. If two remote revisions are unavailable, mark remote ref restoration `UNKNOWN` and keep issue #3 open. Re-read issue #3's full native fields, reconcile any changed semantics, score its review and verified completion transitions, and require every remaining Codex matrix and lifecycle expectation to be `PASS`. Close with reason `completed` only when the integrated target passes all acceptance checks; otherwise keep the issue open at its evidence-supported lifecycle state.
