# Claude Code Setup and Upstream Adoption Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify issue #18's three Claude Code upstream setup modes and failure preservation, and make the existing installation guide accurately describe the verified behavior.

**Architecture:** Keep the root Claude plugin and canonical Backplane skills from #17. Refine the guide's setup section without adding a second installer or changing the shared skill contract. Use isolated Claude profiles and disposable source fixtures to observe native package adoption, sibling checkout adoption, and absent-upstream installation. Record each host result and each failure probe with before/after preservation evidence.

**Tech Stack:** Markdown, Claude Code native plugin CLI, PowerShell as a Windows verification host, Git, and GitHub CLI (`gh`). PowerShell is not an adopter-project runtime.

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`, with scope allocation in `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`.

**Issue:** https://github.com/tvproductions/superpowers-backplane/issues/18

**Issue revision consumed:** `2026-09-20T16:12:58Z` (complete native intake after the `backplane:designing` transition; body and native graph retained their previous semantics).

**Design authority:** The approved functional and rescope specifications plus the complete #18 issue body. This is a bounded continuation of the existing Claude package and guide; no new package architecture is proposed.

## Global Constraints

- #18 owns native-package, sibling-checkout, and absent-upstream setup; provenance, duplicate-install and `gh` preflight; fresh three-skill discovery; and failure preservation. #19 owns repeat install, update, rollback, uninstall, five-check conformance, and authorized issue-state scenarios. #11 owns final Claude acceptance.
- Keep the two authored Backplane skills only under root `skills/`. Preserve `.claude-plugin/` package identity and version unless current host evidence proves a required correction. Upstream Superpowers remains a separate installation.
- A native upstream package must have an upstream-documented authoritative source and an observable installed version or resolved revision. A sibling checkout must have exact `obra/superpowers` origin, observable commit, required skills, and operational discovery. Unknown or versionless source stays `UNKNOWN`.
- A dirty authoritative sibling checkout may be adopted in place if compatible and discoverable; an update of that checkout must be refused. Do not update, replace, or remove any existing upstream installation as a side effect of setup.
- Use the current upstream-documented stable Claude Code installation channel when upstream is absent. The upstream default branch requires an explicit edge selection. Do not advance this repository's `.agents/superpowers` checkout.
- Live checks require an authenticated **disposable** Claude Code profile. Never copy credentials or repeatedly initiate login. If the disposable profile is signed out, record `UNKNOWN`, request authentication once, and pause only the dependent live checks.
- Use `gh` for GitHub. Setup and all failed probes are read-only with respect to issue state. Use an existing issue only for complete native intake; never use a production issue as mutation test data.
- For each mode record Claude Code version, pinned Backplane revision, upstream package/source and version or commit, `gh` auth/intake/label/closure-reason capability, three actual skill identities, and `PASS`/`FAIL`/`UNKNOWN` with evidence.
- Before **every** Git mutation, `git rev-parse --show-toplevel` must equal `C:/Users/Jeff/source/repos/agents/superpowers-backplane` exactly. Use the root checkout for Git mutation, as required by `AGENTS.md`; isolate host installation in disposable profiles and fixtures. Confirm origin is `https://github.com/tvproductions/superpowers-backplane.git` before a GitHub operation or push.
- Re-read #18's complete native fields before each lifecycle transition. Reconcile any change from the consumed revision; preserve unrelated labels and exactly one `backplane:*` label while open. Do not ready or activate #18 before this plan is approved and execution starts.
- No release, new remote, upstream update, skill-text edit, OpenCode work, or full lifecycle claim belongs to this issue.

## File Map

| File | Responsibility |
|---|---|
| `docs/installing-claude-code.md` | Explain the three supported upstream modes, ordered setup preflight, and actionable failures. |
| `tests/scenarios/2026-09-20-claude-code-setup.md` | Record RED baseline, fixture identities, three-mode results, failure matrix, preservation comparisons, and integrated result. |
| `tests/scenarios/transcripts/2026-09-20-claude-code-setup.md` | Preserve exact setup prompts, relevant unedited host responses, and direct skill-invocation observations without credentials. |

## Shared Host Check Recipe

Run native and sibling adoption checks from a neutral disposable project directory with a profile that is already authenticated. Pass Task 1's recorded absolute profile path as `-IsolatedProfile`; for sibling mode also pass the resolved authoritative checkout as `-SiblingCheckout`. The function sets `CLAUDE_CONFIG_DIR` only while its child commands run and restores it afterward. Every fresh sibling session receives `--plugin-dir`, including each direct skill check. Task 5 uses a separate interactive recipe because it must install upstream during setup. Capture output outside tracked source until it has been screened for secrets.

```powershell
function Invoke-BackplaneHostCheck {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)][ValidateScript({ Test-Path -LiteralPath $_ -PathType Container })][string]$IsolatedProfile,
    [Parameter(Mandatory = $true)][ValidateSet('native','sibling')][string]$Mode,
    [string]$SiblingCheckout
  )
  $pluginArgs = @()
  if ($Mode -eq 'sibling') {
    if ([string]::IsNullOrWhiteSpace($SiblingCheckout)) { throw 'Sibling checkout path is required' }
    $pluginArgs = @('--plugin-dir', (Resolve-Path -LiteralPath $SiblingCheckout -ErrorAction Stop).Path)
  }
  $oldClaudeConfig = $env:CLAUDE_CONFIG_DIR
  try {
    $env:CLAUDE_CONFIG_DIR = $IsolatedProfile
    $auth = claude auth status --json | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0 -or -not $auth.loggedIn) { throw 'Disposable Claude profile is not authenticated' }
    $beforeIssue = gh issue view 18 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
    if ($LASTEXITCODE -ne 0) { throw 'Initial issue intake failed' }
    claude @pluginArgs -p 'Set up Superpowers Backplane in this Claude Code session.' --permission-mode plan --output-format json --max-turns 20 --append-system-prompt 'Use existing issue tvproductions/superpowers-backplane#18 for read-only intake. Report source, revision, capabilities, and skill identities. Do not mutate GitHub issue state.'
    if ($LASTEXITCODE -ne 0) { throw 'Setup discovery session failed' }
    foreach ($skill in @('superpowers:using-superpowers','superpowers-backplane:managing-superpowers-backlog','superpowers-backplane:managing-superpowers-handoffs')) {
      claude @pluginArgs -p "Invoke $skill for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package." --permission-mode plan --tools Skill --output-format json --max-turns 3
      if ($LASTEXITCODE -ne 0) { throw "Skill discovery failed: $skill" }
    }
    $afterIssue = gh issue view 18 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
    if ($LASTEXITCODE -ne 0 -or $beforeIssue -ne $afterIssue) { throw 'Issue intake changed or failed during setup check' }
  } finally {
    if ($null -eq $oldClaudeConfig) { Remove-Item Env:CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    else { $env:CLAUDE_CONFIG_DIR = $oldClaudeConfig }
  }
}
```

Call `Invoke-BackplaneHostCheck` once per mode with Task 1's recorded disposable profile path and `-Mode native` or `-Mode sibling -SiblingCheckout` set to the resolved `.agents/superpowers` checkout. The direct skill calls and source roots must appear in host output or its session record. A model's final statement alone is insufficient. If the setup run reaches its turn limit, preserve that as UNKNOWN, inspect the actual tool record, and continue only the report in the same session without claiming an unobserved check. If Claude itself updates session metadata, exclude only those identified metadata files from preservation comparisons.

## Interactive Host Probe Recipe

Use this runner for Task 4 failure probes and Task 5's absent-upstream setup. Supply the absolute second-profile path recorded in Task 3. It must resolve below the system temporary directory; an accidental normal-profile path fails before Claude starts. The runner creates and records a neutral disposable project directory, verifies authentication and plugin inventory in the selected profile, passes a sibling checkout to the session when supplied, limits a `gh` fixture to its named probe, and restores location and process environment on exit. Keep the interactive Claude session open through any Task 5 marketplace and plugin commands; type the exact task prompt after it starts. Preserve the tool and permission record, then compare state before fixture teardown.

```powershell
function Start-BackplaneInteractiveProbe {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)][string]$IsolatedProfile,
    [string]$SiblingCheckout,
    [ValidateSet('none','auth','intake','label','closure')][string]$GhProbe = 'none',
    [string]$ShimDirectory
  )
  $profile = (Resolve-Path -LiteralPath $IsolatedProfile -ErrorAction Stop).Path
  $temporaryParent = (Resolve-Path -LiteralPath $env:TEMP -ErrorAction Stop).Path.TrimEnd('\','/')
  if (-not $profile.StartsWith(($temporaryParent + '\'), [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Claude profile must be a disposable directory below the system temporary directory'
  }
  $pluginArgs = @()
  $resolvedSibling = $null
  if ($SiblingCheckout) {
    $resolvedSibling = (Resolve-Path -LiteralPath $SiblingCheckout -ErrorAction Stop).Path
    $pluginArgs = @('--plugin-dir', $resolvedSibling)
  }
  if ($GhProbe -ne 'none' -and -not (Test-Path -LiteralPath (Join-Path $ShimDirectory 'gh.cmd') -PathType Leaf)) {
    throw 'The requested gh probe needs the verified temporary gh.cmd fixture'
  }
  $previous = @{
    CLAUDE_CONFIG_DIR = [Environment]::GetEnvironmentVariable('CLAUDE_CONFIG_DIR','Process')
    PATH = [Environment]::GetEnvironmentVariable('PATH','Process')
    BACKPLANE_GH_PROBE = [Environment]::GetEnvironmentVariable('BACKPLANE_GH_PROBE','Process')
    BACKPLANE_REAL_GH = [Environment]::GetEnvironmentVariable('BACKPLANE_REAL_GH','Process')
  }
  $pushed = $false
  try {
    $env:CLAUDE_CONFIG_DIR = $profile
    if ($GhProbe -ne 'none') {
      $realGh = (Get-Command gh.exe -CommandType Application -ErrorAction Stop).Source
      $env:BACKPLANE_REAL_GH = $realGh
      $env:BACKPLANE_GH_PROBE = $GhProbe
      $env:PATH = (Resolve-Path -LiteralPath $ShimDirectory -ErrorAction Stop).Path + [IO.Path]::PathSeparator + $previous.PATH
      $selectedGh = (Get-Command gh -CommandType Application -ErrorAction Stop).Source
      if ($selectedGh -ne (Join-Path (Resolve-Path -LiteralPath $ShimDirectory).Path 'gh.cmd')) {
        throw 'Temporary gh fixture is not first on PATH'
      }
    }
    $auth = claude auth status --json | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0 -or -not $auth.loggedIn) { throw 'Disposable Claude profile is not authenticated' }
    $inventory = claude plugin list --json | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0) { throw 'Disposable plugin inventory failed' }
    $sessionDirectory = Join-Path $env:TEMP ('backplane-claude-18-session-' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $sessionDirectory -ErrorAction Stop | Out-Null
    Write-Output "Profile: $profile"
    Write-Output "Session directory: $sessionDirectory"
    Write-Output "Sibling checkout: $resolvedSibling"
    Write-Output "gh probe: $GhProbe"
    Push-Location -LiteralPath $sessionDirectory
    $pushed = $true
    claude @pluginArgs --permission-mode default
    if ($LASTEXITCODE -ne 0) { throw 'Interactive Claude session failed; record UNKNOWN' }
  } finally {
    if ($pushed) { Pop-Location }
    foreach ($name in $previous.Keys) {
      [Environment]::SetEnvironmentVariable($name, $previous[$name], 'Process')
    }
  }
}
```

For each invocation, first compare the profile path, selected `gh` executable when a shim is active, plugin inventory, and sibling path with the intended fixture. If any differs, stop and mark that probe `UNKNOWN`. The standard interactive prompt is: “Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state.” Append the case-specific instruction from Task 4, or the absent-upstream instruction from Task 5. Record the exact combined prompt and permission decisions.

## Review Focus

1. **Native source with no observable version:** the setup report must stay `UNKNOWN`, even if a skill with the right name loads. Tasks 3–5 check package source, version or revision, and skill identity independently.
2. **Dirty authoritative checkout:** adoption without update may pass; an attempted update must stop before mutation. Task 4 tests both paths separately.
3. **Duplicate effective Backplane packages:** an extra marketplace or plugin namespace must produce a conflict and a specific repair action, with unrelated entries preserved. Task 4 inventories both scopes before and after.
4. **Failed preflight changing state:** a missing `gh` capability or occupied checkout path must leave plugin configuration, user files, upstream source, and the existing issue unchanged. Task 4 compares hashes and native fields.
5. **Stale host authentication or source:** #17's prior PASS is not #18 evidence. Task 1 checks the current disposable profile and exact source identities; Tasks 3 and 5 require new fresh-session observations.

## Execution Entry After Plan Approval

Integrate the approved plan so its path is reachable on `main`, then re-read #18. Link the integrated plan in its `Superpowers Artifacts` section and reconcile the resulting `updatedAt`. With the approved design, current plan, and resolved #17 blocker, move `backplane:designing` to `backplane:ready`. Move `backplane:ready` to `backplane:active` immediately before the first Task 1 execution action. Re-fetch after each transition and verify one expected Backplane label and preserved unrelated labels. Work on an issue branch in the root checkout after checking the exact Git top level; use disposable host fixtures for isolation. Do not turn a signed-out Claude host into a fabricated PASS.

---

### Task 1: Establish a current, isolated setup baseline

**Files:**
- Create: `tests/scenarios/2026-09-20-claude-code-setup.md`

**Interfaces:**
- Consumes: #17's integrated Claude package and guide, approved installation reference, and current upstream Claude installation documentation.
- Produces: the pinned source and profile inventory that Tasks 2–5 compare against.

- [ ] **Step 1: Recheck current host and authoritative documentation.** Read [Claude plugin structure](https://code.claude.com/docs/en/plugins), [marketplace sources and CLI](https://code.claude.com/docs/en/plugin-marketplaces), [plugin installation](https://code.claude.com/docs/en/discover-plugins), [configuration isolation](https://code.claude.com/docs/en/env-vars), and the installed upstream README's Claude Code installation section. Run `claude --version`, `claude plugin marketplace list --help`, `claude plugin list --help`, `claude plugin install --help`, and `claude auth status --json`. Record the observed version, supported flags, and authentication result. Planning observed Claude Code `2.1.241` and a signed-out default profile; neither is a future live-session result.
- [ ] **Step 2: Record the RED gap.** Verify that the guide has the #17 clean-install path but no three-mode procedure or complete failure table, and that no #18 scenario/transcript exists yet. Record these observations and the #17 tested package/guide commit and integrated package bytes. Do not rerun #17's smoke as a substitute for #18.
- [ ] **Step 3: Establish source and GitHub preflight.** Run the following read-only commands and record exact output identities rather than credentials:

  ```powershell
  git rev-parse --show-toplevel
  git remote get-url origin
  git rev-parse HEAD
  git status --porcelain=v1 -uall
  git -C .agents/superpowers remote get-url origin
  git -C .agents/superpowers rev-parse HEAD
  git -C .agents/superpowers status --porcelain=v1
  gh auth status
  gh issue view 18 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
  gh issue edit --help
  gh issue close --help
  ```

  Require exact project and upstream origins, all 15 issue fields, label add/remove flags, and closure-reason support. The issue query is read-only. Record the Backplane commit chosen for host tests; require its exact full SHA and published availability before using it in an installation guide replay.
- [ ] **Step 4: Check disposable-profile readiness without copying auth.** Read the #17 scenario's recorded disposable profile path; if it still exists, set `CLAUDE_CONFIG_DIR` for child commands only and run `claude auth status --json`, `claude plugin marketplace list --json`, and `claude plugin list --json`. Record only identity and login status, not tokens or settings contents. If it is absent or signed out, create a new unused profile under the system temporary directory and request one interactive authentication for that profile before Tasks 3–5; keep live scores `UNKNOWN` until then. Do not change the normal Claude profile.
- [ ] **Step 5: Save and check the baseline.** Create the scenario with a table for each mode and failure case: input/source, expected result, actual result, preservation evidence, and `PASS`/`FAIL`/`UNKNOWN`. Run `git diff --check` and compare the file against this task's observed outputs. Verify the exact Git root, stage only the scenario, run `git diff --cached --check`, verify the root again, and commit `test: record Claude setup baseline`.

### Task 2: Make the Claude setup guide cover each supported mode

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-09-20-claude-code-setup.md`

**Interfaces:**
- Consumes: Task 1's current host/docs baseline and existing pinned Backplane installation instructions.
- Produces: commands and decision rules replayed by Tasks 3–5.

- [ ] **Step 1: Capture guide RED.** Search the current guide for distinct native-package, sibling-checkout, and absent-upstream steps; for exact authoritative-source/version recording; and for recovery actions for unknown source, duplicates, dirty update, occupied path, unavailable `gh`, and incompatible required skills. Record the missing items in the scenario.
- [ ] **Step 2: Add an ordered preflight section after the setup request.** Keep the existing pinned Backplane clone/install block. Add these rules in this order: (1) inspect `claude plugin marketplace list --json` and `claude plugin list --json`, requiring exactly one effective Backplane plugin and both canonical skills; (2) classify upstream as an already installed native package, a supplied sibling checkout exposed through Claude's supported `--plugin-dir` discovery, or absent; (3) verify upstream source, observable version/revision, and `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`; (4) run `gh auth status`, complete read-only issue intake, and edit/close help checks; (5) start a fresh session and invoke all three skills. State that setup changes no issue state.
- [ ] **Step 3: Give each mode an exact operator path.** Native mode adopts an already installed, independently identified upstream plugin in place. Sibling mode records its resolved path, exact `obra/superpowers` Git origin, HEAD, clean/dirty status, and required skills; pass `--plugin-dir` with that checkout to setup and every fresh three-skill discovery session without relocating it. Absent mode starts setup with no upstream plugin in a disposable profile under normal interactive permissions; the setup workflow reads current upstream Claude instructions, requests approval for the documented official marketplace registration if needed and native `superpowers@claude-plugins-official` installation, runs the approved commands in that same setup session, and records the resulting installed version and source before fresh-session discovery. None of these modes implicitly selects upstream's default branch or changes `.agents/superpowers`.
- [ ] **Step 4: Add a failure/recovery table with explicit stop rules.** Unknown/lookalike source or versionless native package → `UNKNOWN`, identify an authoritative source and observable version/revision. Duplicate Backplane → stop, identify the conflicting ID/scope and remove only after a separately reviewed choice. Dirty authoritative sibling → adopt only without update; refuse an update until owner resolves changes. Occupied checkout path → stop and choose an unused path without deletion. Missing `gh` field/label/closure capability → stop and repair `gh`. Missing upstream skill or incompatible host/source → stop and install/select a compatible authoritative source. An unauthenticated Claude session → `UNKNOWN` and authenticate the disposable profile once. State preservation of user files, unrelated plugins, upstream, and issue state for every failure.
- [ ] **Step 5: Check the guide against current sources.** Parse every PowerShell command block with the PowerShell parser. Verify the guide still pins a 40-character Backplane commit, requires an existing issue for read-only intake, points to the canonical skill tree, and keeps #19 lifecycle claims pending. Record the checks and `git diff --check`; verify the exact Git root, stage only the guide and scenario, check the staged diff, verify the root again, and commit `docs: describe Claude upstream setup modes`.

### Task 3: Verify native-package and sibling-checkout adoption

**Files:**
- Modify: `tests/scenarios/2026-09-20-claude-code-setup.md`
- Create: `tests/scenarios/transcripts/2026-09-20-claude-code-setup.md`

**Interfaces:**
- Consumes: Task 2's exact guide commands, Task 1's pinned Backplane source, and an authenticated disposable Claude profile.
- Produces: two separately scored mode rows and an authenticated profile with Backplane installed but no upstream plugin for Tasks 4–5.

- [ ] **Step 1: Recheck the live gate.** With `CLAUDE_CONFIG_DIR` set only for the chosen disposable profile, run `claude auth status --json` and both plugin inventory commands. If authentication is false, leave the dependent live rows `UNKNOWN` and stop those checks until that profile is authenticated; do not attempt another login or copy credentials. Confirm the profile is not the normal Claude profile. Record profile and plugin-config file hashes before mutation, excluding credential material from the transcript.
- [ ] **Step 2: Native package adoption.** In the authenticated #17 disposable profile if still valid, inspect the enabled `superpowers@superpowers-dev` version and authoritative checkout-backed marketplace from #17; verify source, revision, required skills, and Backplane's separate plugin. Run `Invoke-BackplaneHostCheck` with `-IsolatedProfile` set to that profile and `-Mode native` from a neutral disposable directory; the recipe runs setup once and then invokes `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs` in separate fresh read-only sessions. Record host tool calls and source roots, not only model assertions. Require no upstream or issue mutation.
- [ ] **Step 3: Sibling checkout adoption.** Prepare a second disposable profile with the already reviewed pinned Backplane plugin and no installed upstream plugin. Authenticate that profile once if needed. Run `Invoke-BackplaneHostCheck` with `-IsolatedProfile` set to that profile, `-Mode sibling`, and `-SiblingCheckout` set to the resolved clean, authoritative `.agents/superpowers` checkout; its setup request and each separate direct skill session must receive `--plugin-dir`. Verify the session resolves upstream separately from Backplane, observes exact origin/HEAD/required skills, checks `gh`, and directly invokes all three skills. Require that setup neither clones nor installs another upstream package and that `.agents/superpowers` HEAD/status remain unchanged.
- [ ] **Step 4: Score and record these two modes.** For native and sibling cases require an authenticated session, exact Backplane revision, authoritative and observable upstream version/revision, all gh capabilities, three direct skill invocations, and unchanged issue state. Capture exact prompts and unedited relevant responses in the transcript, redacting credential-bearing or private data. Compare disposable inventories and upstream checkout before/after. Require that the second profile still has no installed upstream package after sibling adoption; Tasks 4 and 5 need that state. An unresolved required observation is UNKNOWN.
- [ ] **Step 5: Commit the evidence.** Run git diff --check, inspect the evidence for credentials, verify the exact Git root, stage only scenario/transcript, check the staged diff, verify the root again, and commit test: verify Claude native and sibling setup.
### Task 4: Verify failure stops and preservation

**Files:**
- Modify: `tests/scenarios/2026-09-20-claude-code-setup.md`
- Modify: `tests/scenarios/transcripts/2026-09-20-claude-code-setup.md`

**Interfaces:**
- Consumes: Task 2's failure/recovery table and Task 3's authenticated second profile before official upstream installation.
- Produces: one observed result and preservation comparison for each #18 failure class.

- [ ] **Step 1: Build disposable-only inputs and snapshots.** Use the authenticated second disposable profile from Task 3 while it still has Backplane only and no installed upstream plugin. If that profile is signed out, leave live probes UNKNOWN until the same profile is authenticated; do not create a third profile or initiate repeated login. Under an unused system-temporary parent, clone obra/superpowers with gh repo clone and detach at the recorded stable commit; verify exact origin and clean status. Clone a second authoritative fixture and modify only its tracked README.md to create a dirty checkout. In a third fixture remove skills/writing-plans/SKILL.md to isolate missing-skill behavior. Prepare two separate provenance cases: a lookalike plugin with an observable version but false source, and a versionless inventory with an official source field but no installed version or resolved revision. If the current CLI cannot produce the latter, test it as an explicitly synthetic read-only decision probe; never present that as a live-host PASS. Create a second Backplane marketplace identity, an occupied checkout destination, and a read-only gh.cmd shim with selectable auth, intake, label-help, and closure-help failures; the interactive runner puts that shim first on PATH only for its named case. Require each fixture to trigger its intended precondition. For each probe, stage its intended fixture first, then record hashes of target user files and Claude plugin configuration, installed-plugin inventory, fixture HEAD/status, and complete read-only #18 native fields before requesting setup. Never edit .agents/superpowers or a normal Claude profile.
  Begin the checkout, dirty-state, path-collision, and missing-gh fixtures with these exact commands from the verified repository root. Check every command's exit status and record the resulting path and source; a failed fixture setup is UNKNOWN evidence.

```powershell
$secondProfile = (Resolve-Path -LiteralPath (Read-Host 'Task 3 recorded second disposable Claude profile path') -ErrorAction Stop).Path
$fixtureRoot = Join-Path $env:TEMP ('backplane-claude-18-' + [guid]::NewGuid().ToString('N'))
if (Test-Path -LiteralPath $fixtureRoot) { throw 'Fixture path collision' }
New-Item -ItemType Directory -Path $fixtureRoot | Out-Null
$upstreamRevision = '5bf4e78011075bcfc0dc295f0724994cd123ee71'
function Assert-BackplaneRoot {
  $root = git rev-parse --show-toplevel
  if ($LASTEXITCODE -ne 0 -or $root -cne 'C:/Users/Jeff/source/repos/agents/superpowers-backplane') { throw "Unexpected Git root: $root" }
}
foreach ($name in @('clean','dirty','missing-skill','lookalike')) {
  $checkout = Join-Path $fixtureRoot $name
  Assert-BackplaneRoot
  gh repo clone obra/superpowers $checkout
  if ($LASTEXITCODE -ne 0) { throw "Upstream fixture clone failed: $name" }
  Assert-BackplaneRoot
  git -C $checkout checkout --detach $upstreamRevision
  if ($LASTEXITCODE -ne 0) { throw "Upstream fixture pin failed: $name" }
}
Add-Content -LiteralPath (Join-Path $fixtureRoot 'dirty/README.md') -Value 'Disposable dirty-checkout fixture'
Remove-Item -LiteralPath (Join-Path $fixtureRoot 'missing-skill/skills/writing-plans/SKILL.md')
Assert-BackplaneRoot
git -C (Join-Path $fixtureRoot 'lookalike') remote set-url origin https://github.com/obrafake/superpowers.git
$occupied = Join-Path $fixtureRoot 'occupied'
New-Item -ItemType Directory -Path $occupied | Out-Null
Set-Content -LiteralPath (Join-Path $occupied 'sentinel.txt') -Value 'Preserve this file'
$shim = Join-Path $fixtureRoot 'shim'
New-Item -ItemType Directory -Path $shim | Out-Null
$shimSource = @'
@echo off
if /I "%~1"=="--version" goto forward
if /I "%~1"=="auth" if /I "%~2"=="status" goto auth
if /I "%~1"=="issue" if /I "%~2"=="view" goto intake
if /I "%~1"=="issue" if /I "%~2"=="edit" if /I "%~3"=="--help" goto label
if /I "%~1"=="issue" if /I "%~2"=="close" if /I "%~3"=="--help" goto closure
echo gh fixture blocks commands outside read-only preflight 1>&2
exit /b 1
:auth
if /I "%BACKPLANE_GH_PROBE%"=="auth" goto unavailable
goto forward
:intake
if /I "%BACKPLANE_GH_PROBE%"=="intake" (
  echo unknown JSON field: closedByPullRequestsReferences 1>&2
  exit /b 1
)
goto forward
:label
if /I "%BACKPLANE_GH_PROBE%"=="label" (
  echo Usage: gh issue edit ISSUE
  echo Flags: --title --body
  exit /b 0
)
goto forward
:closure
if /I "%BACKPLANE_GH_PROBE%"=="closure" (
  echo Usage: gh issue close ISSUE
  echo Flags: --comment
  exit /b 0
)
goto forward
:unavailable
echo gh fixture capability unavailable 1>&2
exit /b 1
:forward
"%BACKPLANE_REAL_GH%" %*
exit /b %ERRORLEVEL%
'@
Set-Content -LiteralPath (Join-Path $shim 'gh.cmd') -Value $shimSource -Encoding ascii
```

  The temporary gh shim forwards only read-only preflight commands to the real gh executable and blocks every mutation command. Verify each selected failure response before running Claude. Supply the occupied directory as the requested checkout destination; require its sentinel hash to remain unchanged. Build the duplicate Backplane marketplace from a separate disposable clone of the pinned test revision by changing only its marketplace name to backplane-conflict, then check both plugin IDs with claude plugin list --json. The missing-version case is a separately labeled synthetic inventory decision probe if the native CLI cannot produce that state.
- [ ] **Step 2: Define the immediate preservation check.** For each case, immediately after its setup probe and before any fixture teardown, re-run the exact before snapshot for plugin config, unrelated marketplace/plugin entries, fixture/user files, upstream checkout, and #18's native issue fields. Require unchanged content and native state for a stopped setup and for adoption of a dirty checkout without update. Compare the duplicate case against its snapshot with both plugins installed, before removing the test-only plugin. If the host itself writes incidental session metadata, identify and exclude only those observed files, never a plugin or issue change. Record commands, exit statuses, unedited failure result, and precise before/after comparison. Do not repair a fixture by deleting an unverified path.
- [ ] **Step 3: Run the distinct negative cases.** Use `Start-BackplaneInteractiveProbe` with `-IsolatedProfile $secondProfile` for each fresh normal-permission case. Follow the case matrix below for checkout and gh-shim arguments. Record separate rows for lookalike source, live missing version/revision if constructible, duplicate Backplane installations, occupied path, missing required upstream skill, and four gh failures: auth, issue intake, label help, and closure help. Confirm the intended failure is reached; a failed fixture setup is UNKNOWN. Approve read-only preflight and fixture-scoped actions needed to reach the failing condition. If setup requests a write to user files, plugin configuration, existing upstream, or issue state before reporting the failed check, record the request as FAIL and deny it. Do not score preservation from a plan-mode run alone. If no native versionless inventory can be constructed, run the synthetic read-only decision probe as supplementary policy evidence, leave the live versionless row UNKNOWN, and keep #18 out of submission and closure. For the duplicate case, set `$env:CLAUDE_CONFIG_DIR = $secondProfile` for the fixture installation commands, verify that profile before mutation, and restore the prior value immediately afterward, install the second Backplane marketplace/plugin there, and observe both IDs. Take the case's before snapshot with both installed, run the refusal probe, and perform Step 2's comparison before removing the test-only entry. After comparison, remove that entry and separately verify that the original entry remains. Require the expected refusal for the intended reason, the failed check, a specific repair action, and Step 2 preservation evidence; score the probe PASS only when all are observed. A probe that never reaches its intended condition is UNKNOWN, not a PASS.

  Bind each live probe to the exact runner arguments and append the indicated sentence to the standard prompt. Paste the resolved absolute `$occupied` path into that case's prompt; the Claude session cannot read a PowerShell variable from its parent shell. For each gh case verify that the shim forwards the other three read-only checks and fails only the selected capability.

  | Probe | Runner arguments after `-IsolatedProfile $secondProfile` | Prompt addition |
  |---|---|---|
  | Lookalike source | `-SiblingCheckout (Join-Path $fixtureRoot 'lookalike')` | “Adopt the supplied upstream checkout only if its Git origin is authoritative.” |
  | Missing upstream skill | `-SiblingCheckout (Join-Path $fixtureRoot 'missing-skill')` | “Check every required skill in the supplied upstream checkout.” |
  | Duplicate Backplane | None; stage both plugin IDs before the snapshot. | “Check whether exactly one effective Backplane plugin is installed.” |
  | Occupied checkout | None; stage the occupied destination before the snapshot. | “Use the supplied occupied destination for a requested checkout-based upstream installation; preserve its existing contents.” |
  | Missing `gh` auth | `-SiblingCheckout (Join-Path $fixtureRoot 'clean') -ShimDirectory $shim -GhProbe auth` | “Run the complete GitHub CLI preflight before reporting setup ready.” |
  | Missing intake field | `-SiblingCheckout (Join-Path $fixtureRoot 'clean') -ShimDirectory $shim -GhProbe intake` | “Run the complete GitHub CLI preflight before reporting setup ready.” |
  | Missing label flags | `-SiblingCheckout (Join-Path $fixtureRoot 'clean') -ShimDirectory $shim -GhProbe label` | “Run the complete GitHub CLI preflight before reporting setup ready.” |
  | Missing closure reason | `-SiblingCheckout (Join-Path $fixtureRoot 'clean') -ShimDirectory $shim -GhProbe closure` | “Run the complete GitHub CLI preflight before reporting setup ready.” |
  | Live versionless native package, if constructible | None; stage the candidate package and source inventory before the snapshot. | “Report compatibility only if the package has an observable installed version or resolved revision.” |

  Run `Start-BackplaneInteractiveProbe` for each row, record the exact combined prompt and arguments, and apply Step 2's before/after comparison immediately. A case whose fixture is not active in the Claude tool process is `UNKNOWN`.

- [ ] **Step 4: Separate dirty adoption from unsafe update.** Use `Start-BackplaneInteractiveProbe -IsolatedProfile $secondProfile -SiblingCheckout (Join-Path $fixtureRoot 'dirty')` to present the authoritative dirty sibling checkout through `--plugin-dir` in each fresh session for adoption without update and verify that compatible provenance, revision, skills, and discovery can still pass while the checkout remains dirty and unchanged. In a distinct normal-permission session with the same `--plugin-dir` checkout, request an update and require a refusal before any Git or plugin mutation and an owner-directed cleanup action; apply Step 2's immediate preservation comparison before fixture teardown. This distinction follows `skills/managing-superpowers-backlog/references/installing-superpowers.md` and avoids conflating dirty state with lookalike provenance.
- [ ] **Step 5: Restore the fixture, score, and commit.** Require the second profile again to contain only the pinned Backplane plugin and no upstream plugin before Task 5; otherwise stop and reconcile the fixture. Mark each case `PASS`, `FAIL`, or `UNKNOWN` against its expected stop and preservation result. Require every named #18 failure class to have its own row; a combined probe cannot substitute for an isolated class. Run `git diff --check`, inspect the exact transcript for credentials, verify the Git root, stage only scenario/transcript, check the staged diff, verify the root again, and commit `test: verify Claude setup failure preservation`.

### Task 5: Verify absent-upstream installation through the stable channel

**Files:**
- Modify: tests/scenarios/2026-09-20-claude-code-setup.md
- Modify: tests/scenarios/transcripts/2026-09-20-claude-code-setup.md

**Interfaces:**
- Consumes: Task 4's restored, authenticated second profile with only Backplane installed and Task 2's guide.
- Produces: the third supported mode score and independently installed official upstream identity.

- [ ] **Step 1: Prove absence.** Resolve the Task 3 recorded second-profile path as `$secondProfile` again if this is a new PowerShell session; require it to equal the Task 4 recorded path. Save `$env:CLAUDE_CONFIG_DIR`, set it to `$secondProfile` inside a `try` block, run `claude auth status --json`, `claude plugin marketplace list --json`, and `claude plugin list --json`, then restore the prior environment value in `finally`. Start without `--plugin-dir` and require the inventory to show exactly one effective Backplane plugin and no upstream plugin. Confirm the auth result is still logged in. If source or login differs, record UNKNOWN and reconcile before installation.
- [ ] **Step 2: Start the absent-upstream setup workflow.** Independently read the current upstream README's Claude installation section and official Claude marketplace documentation to establish the expected stable channel. Run `Start-BackplaneInteractiveProbe -IsolatedProfile $secondProfile` with no sibling checkout or gh shim; verify its printed profile and empty sibling path before typing the standard prompt followed by: “Upstream is absent. Obtain the current compatible stable Superpowers release through Claude Code's documented native channel after requesting host approval.” Require the setup workflow itself to observe absence, identify the upstream-documented `claude-plugins-official` channel, and request the exact native installation commands. Record the initial prompt, source check, proposed commands, and any host permission prompts; do not infer a branch checkout.
- [ ] **Step 3: Complete installation in that setup session.** After checking the tool subprocess still has `CLAUDE_CONFIG_DIR` equal to `$secondProfile` and that the commands target only the official documented source, approve the setup workflow's `claude plugin marketplace add anthropics/claude-plugins-official` only if needed and `claude plugin install superpowers@claude-plugins-official --scope user`. Require the setup session to execute the approved commands and record tool calls, approvals, exit statuses, marketplace source, and installed upstream version or resolved revision. Re-read both JSON inventories and confirm a separate Backplane identity. If installation is performed manually outside that setup session or cannot complete there, score the absent-upstream workflow UNKNOWN rather than treating later adoption as its PASS. Never change `.agents/superpowers` or the normal profile.
- [ ] **Step 4: Verify fresh discovery and score.** In a new Claude session run the shared host check recipe with the now-installed second profile and `-Mode native`; require its setup request and separate direct invocations of `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. Require gh auth/intake/label/closure capability and unchanged issue state. Record exact prompts, relevant unedited responses, host tool calls, source roots, inventories, and preservation comparison from the initial absent state through installation and fresh discovery. If installed version/revision or any other required observation is unavailable, score UNKNOWN rather than PASS.
- [ ] **Step 5: Commit the mode result.** Run git diff --check, inspect both evidence files for credentials, verify the exact Git root, stage only scenario/transcript, check the staged diff, verify the root again, and commit test: verify Claude absent-upstream setup.
### Task 6: Review integrated #18 evidence and finish the issue

**Files:**
- Modify: `tests/scenarios/2026-09-20-claude-code-setup.md` only if integration evidence is needed.

**Interfaces:**
- Consumes: Tasks 1–5's reviewed guide and all mandatory PASS results.
- Produces: an integrated, reviewable #18 result without claiming #19 or #11 completion.

- [ ] **Step 1: Run the document and package gate.** Run `claude plugin validate --strict .`, PowerShell-parse every guide command block, `git diff --check`, and inspect the full issue-branch diff. Require no edits to canonical skills, Claude manifests, upstream checkout, or unrelated host files. Re-read #18 and reconcile any semantic revision change.
- [ ] **Step 2: Check coverage and preservation.** Compare every #18 acceptance criterion and verification seam with a named scenario row and transcript evidence. Require three supported modes PASS and every failure class PASS, including auth, intake, label-help, and closure-help gh failures plus separate dirty adoption and dirty-update refusal. A synthetic versionless decision result never satisfies the live versionless failure row. An unresolved `FAIL` or `UNKNOWN` prevents submission/completion; record the exact missing observation rather than inferring success from #17.
- [ ] **Step 3: Review and submit.** Use the repository review workflow on the complete change, resolve Critical and Important findings, then repeat affected checks. Recheck the Git root before each mutation and commit any evidence correction. Submit through the branch-finishing workflow; transition `backplane:active` to `backplane:review` only when the reviewed implementation and worktree verification support it.
- [ ] **Step 4: Verify integration before closure.** After authorized integration, compare integrated guide and scenario bytes with the tested branch; rerun any seam whose relevant input changed. Run fresh `claude plugin validate --strict .`, document checks, native issue intake, and one installed-package three-skill discovery in the authenticated disposable profile. Confirm the final evidence is reachable from integrated `main`, then close #18 with reason `completed` only if all acceptance criteria pass. Preserve #19 and #11 as open successors and do not claim lifecycle conformance.

## Handoff

This plan is a review artifact until the operator approves its contents and chooses an execution method. The default Claude profile was signed out during planning; the previously authorized #17 disposable profile was observed signed in with separate Backplane and Superpowers plugins. Recheck it at execution. The second disposable profile needs one independent authentication for sibling, failure, and absent-upstream checks; no login is needed to review this plan. #18 remains `backplane:designing` until an approved, current plan and resolved blocker justify readiness.
