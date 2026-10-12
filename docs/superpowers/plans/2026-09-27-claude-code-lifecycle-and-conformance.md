# Claude Code Lifecycle and Conformance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify repeat installation, a pinned update between two disposable package revisions, rollback, Backplane-only removal, failed-candidate preservation, and the five Backplane conformance checks in Claude Code.

**Architecture:** Extend the existing Claude Code guide with commands proved in an authenticated disposable profile. Keep Backplane and upstream Superpowers as separate native plugins. Record each lifecycle operation and issue-state scenario in a scored evidence file, using immutable source revisions and before/after identity snapshots.

**Tech Stack:** Markdown, PowerShell, Git, `gh`, Claude Code native plugin CLI, isolated `CLAUDE_CONFIG_DIR` profiles.

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`; bounded owner: [issue #19](https://github.com/tvproductions/superpowers-backplane/issues/19), observed `updatedAt` `2026-09-27T14:09:57Z` after its evidence-backed move to `backplane:designing`. Its body and native relationships still match the semantic revision observed at `2026-09-20T01:29:21Z`.

## Global Constraints

- Read `AGENTS.md`, `HANDOFF.md`, `SUPERPOWERS.md`, the spec, and the complete current issue #19 intake before execution. Reconcile issue revision drift before a lifecycle transition.
- `git rev-parse --show-toplevel` must resolve exactly to `C:/Users/Jeff/source/repos/agents/superpowers-backplane` before every Git mutation. Perform tracked implementation on a feature branch in this standalone root worktree; do not treat it as a disposable feature worktree.
- Use `gh` for GitHub operations. Test issue mutations only on disposable or explicitly authorized issues; status and selection probes must leave native issue state unchanged.
- Backplane source revisions must be full, published 40-character commits. Record source, package version, and installed skill hashes before and after each operation. Do not use a moving branch as an installation revision.
- The current release arc targets `0.1.0`; the operator's longer-term goal is normal SemVer progression to `1.0.0`. Issue #19 verifies lifecycle mechanics using disposable source revisions and does not choose or publish a product release version. Version selection and publication belong to a separate release workflow.
- Do not create a remote repository or release without explicit operator authorization under `AGENTS.md`. Prepare and review the candidate before pushing it; leave dependent live-host rows `UNKNOWN` until an immutable candidate is reachable from the expected origin.
- Keep the installed upstream Superpowers plugin and checkout independently identifiable and unchanged. No implicit upstream update, removal, or source replacement.
- Keep exactly one effective Backplane plugin after repeat install, update, and rollback. Removal must affect only the Backplane plugin and Backplane-owned entries.
- Preserve unrelated plugin entries, user files, repository history, and GitHub issue state during package operations. A failed candidate must leave the prior verified Backplane installation available where the host supports restoration.
- Score every required row `PASS`, `FAIL`, or `UNKNOWN`; a mandatory `FAIL` or `UNKNOWN` blocks #19 submission and completion. Do not claim #11's final integrated acceptance here.
- Remain language-neutral and use project-owned scenario rubrics. Do not introduce a consuming-project runtime or test framework.

## Review Focus

1. A marketplace refresh sees a new source commit without a changed computed plugin version: stop before claiming an update; a successful CLI exit alone is insufficient.
2. A failed candidate preflight after replacement: verify restoration of the recorded prior source, version, skill hashes, and fresh discovery before claiming rollback.
3. An unrelated plugin or marketplace entry shares the disposable profile: compare its identity and files before and after every lifecycle operation.
4. The previous `0.1.0` revision is unavailable or the installed source cannot be identified: stop before replacement and report a specific recovery action; never claim rollback.
5. A read-only or selection request is mistaken for lifecycle authorization: compare complete native issue state before and after, and score any mutation `FAIL`.

---

### Task 1: Establish an isolated lifecycle baseline and document the missing guide paths

**Files:**
- Create: `tests/scenarios/2026-09-27-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-09-27-claude-code-lifecycle.md`
- Modify: `docs/installing-claude-code.md`

**Interfaces:**
- Consumes: integrated #17 package/guide, completed #18 setup evidence, approved #19 issue body.
- Produces: recorded prior revision/profile and baseline snapshots used by Tasks 2–4.

- [ ] **Step 1: Recheck authority and host.** Run the complete 15-field `gh issue view 19 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`; reconcile any change from the revision above. Run `claude --version`, `claude plugin marketplace update --help`, `claude plugin update --help`, `claude plugin uninstall --help`, `claude plugin list --json`, `gh auth status`, and the `gh` capability commands in `docs/installing-claude-code.md`. Record exact output and exits, excluding secrets.
- [ ] **Step 2: Confirm the fixture.** Reuse an authorized authenticated disposable Claude profile from #18 only after resolving its path, checking `claude auth status --json` within that `CLAUDE_CONFIG_DIR`, and proving its Backplane and upstream inventories. If unavailable, create one isolated profile and record authentication as an external prerequisite; do not copy credentials or use the normal profile. Record Claude version, profile path, both plugin IDs/scopes/sources/versions, separate upstream identity, three installed skill hashes, and current Git and issue #19 identities.
- [ ] **Step 3: Record RED guide and lifecycle evidence.** Show that `docs/installing-claude-code.md` currently ends with pending #19 update/rollback/uninstall instructions and that no #19 lifecycle score exists. Capture the exact guide section and native inventories in the scenario. Keep the transcript limited to exact commands, prompts, tool calls, results, and identity observations; redact auth values.
- [ ] **Step 4: Record the prior revision and candidate requirements.** Verify the current installed `0.1.0` Backplane commit with `gh api repos/tvproductions/superpowers-backplane/commits/<full-sha> --jq .sha`, exact repository origin, clean checkout, package metadata, and canonical skill paths. Record the pinned prior source and the host's source-replacement route. Task 2 prepares a disposable `0.1.1` version fixture for the update probe; do not treat that fixture as a product release.
- [ ] **Step 5: Establish before/after comparisons.** Snapshot `claude plugin marketplace list --json`, `claude plugin list --json`, the relevant disposable profile plugin configuration and unrelated file hashes, upstream source/revision/status, repository history, and complete read-only issue #19 JSON. Repeat this snapshot immediately after every Task 2–4 operation, before any cleanup or repair. Identify host-created session metadata explicitly rather than excluding plugin or issue changes.

### Task 2: Prove repeat installation and pinned update, then write the guide commands

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-09-27-claude-code-lifecycle.md`
- Modify: `tests/scenarios/transcripts/2026-09-27-claude-code-lifecycle.md`

**Interfaces:**
- Consumes: Task 1's authenticated isolated profile, two published revisions, and snapshots.
- Produces: replayed repeat-install and pinned-update commands plus installed candidate identity.

- [ ] **Step 1: Probe repeat install.** With only the prior Backplane and separate upstream installed, replay the guide's `claude plugin marketplace add <verified-prior-checkout>` and `claude plugin install superpowers-backplane@superpowers-backplane --scope user` as applicable to the observed CLI. Record whether the host reports already installed or succeeds. Require exactly one effective Backplane identity, unchanged installed skill hashes, unchanged upstream and unrelated entries, and a fresh three-skill session discovery.
- [ ] **Step 2: Prepare the pinned candidate fixture.** In an isolated disposable source copy, change only the product-version fields in `plugin.json`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` from `0.1.0` to `0.1.1`; leave the schema URL `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` unchanged because it identifies the schema. Validate the fixture with `claude plugin validate --strict <fixture-path>`, record its Git identity and all changed bytes, and make the fixture commit reachable through the approved test source. Keep the authoritative `0.1.0` prior revision available for restoration. Never merge or tag the fixture-only version.
- [ ] **Step 3: Probe pinned update.** Use a hosted Git marketplace test source with the prior `0.1.0` plugin installed, then make its catalog resolve the verified `0.1.1` fixture commit through the host's supported marketplace operation. Run `claude plugin marketplace update superpowers-backplane` and `claude plugin update superpowers-backplane@superpowers-backplane --scope user`. Record every command and restart requirement. Compare installed package source, version, and skill hashes with fixture bytes after restart and fresh direct Skill-tool invocations of `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. A local-directory in-place load does not count as the hosted update result.
- [ ] **Step 4: Handle version or cache failure.** If the host retains `0.1.0` after the marketplace refresh and explicit update, record `FAIL`, preserve or restore the prior installation, and diagnose the source/version resolution before rerunning with the reviewed fixture commit. Require installed `0.1.1` fixture bytes and matching root, Claude manifest, and marketplace versions; do not score a no-op as an update.
- [ ] **Step 5: Replay the guide.** Replace any draft command that differed from observed host behavior; include full-SHA source verification, expected inventory and restart checks, and recovery path. Replay the final guide commands from a clean copy of the documented starting state. Record a `PASS` only when installed candidate identity and fresh discovery match the selected revision and Task 1 preservation snapshots pass.

### Task 3: Prove rollback, Backplane-only uninstall, and failed-candidate preservation

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-09-27-claude-code-lifecycle.md`
- Modify: `tests/scenarios/transcripts/2026-09-27-claude-code-lifecycle.md`

**Interfaces:**
- Consumes: Task 2's installed candidate and recorded prior source.
- Produces: replayed rollback and uninstall instructions with preservation evidence.

- [ ] **Step 1: Roll back.** Use the recorded prior full SHA and host-supported marketplace source replacement/reinstallation commands. Restart the disposable host, inspect plugin source/version and both Backplane skill hashes, and invoke all three skills in fresh sessions. Require identity and hashes to equal the Task 1 prior snapshot; verify unrelated plugins, user files, upstream, history, and issue state immediately afterward.
- [ ] **Step 2: Test failed preflight.** Stage a candidate with a concrete incompatible or unverifiable source in an isolated clone; run the guide's preflight and require it to stop before changing the verified installation. If the host replaces the package before failure, execute the documented restoration path and prove the prior identity and fresh discovery. Record the exact failed condition and recovery action. Keep the fixture separate from the authoritative upstream checkout.
- [ ] **Step 3: Uninstall Backplane.** Replay `claude plugin uninstall superpowers-backplane@superpowers-backplane --scope user` in the disposable profile. Check the profile inventory and fresh session for absent Backplane skills and still-present upstream `using-superpowers`. Compare unrelated marketplace/plugin entries and user files; remove a dedicated Backplane marketplace only when the guide proves it owns no unrelated entry. Reinstall the recorded prior revision afterward as a separate fixture restoration, and verify its three-skill discovery.
- [ ] **Step 4: Publish exact instructions.** Write rollback, failed-candidate recovery, and uninstall commands into `docs/installing-claude-code.md`. Include the observed CLI behavior, pinned source and version checks, and the limit that an unprovable restoration is `UNKNOWN`. Replay the written commands, then score each operation with its immediate preservation comparison.

### Task 4: Run installed-package conformance and authorized issue-state scenarios

**Files:**
- Modify: `tests/scenarios/2026-09-27-claude-code-lifecycle.md`
- Modify: `tests/scenarios/transcripts/2026-09-27-claude-code-lifecycle.md`
- Create: `docs/superpowers/plans/2026-09-27-claude-lifecycle-fixture.md` for the disposable issue's execution authority.
- Create in ignored scratch: `.superpowers/sdd/2026-09-27-claude-lifecycle-fixture-body.md`.

**Interfaces:**
- Consumes: Task 3's restored verified package and independent upstream installation.
- Produces: five named check scores and complete issue-state scenario scores.

- [ ] **Step 1: Score skill structure.** Inspect the installed Backplane `SKILL.md` files for YAML delimiters, exact names, `Use when` descriptions, existing direct references, and no placeholders. Record installed hashes and `PASS`, `FAIL`, or `UNKNOWN` for `skill-structure`.
- [ ] **Step 2: Score four fresh behavioral checks.** In four fresh Claude sessions with the restored Backplane and separate upstream, submit the exact prompts from `tests/scenarios/2026-08-16-native-issue-intake-green.md` (primary and language-neutral variation), `tests/scenarios/2026-08-16-lifecycle-transition-refactor.md`, and `tests/scenarios/2026-08-16-superpowers-installation-refactor.md`. Capture unedited responses and actual Skill-tool loads, score every mapped rubric expectation, and report `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation` separately. A missing response or unscored expectation is `UNKNOWN`.
- [ ] **Step 3: Prove read-only paths.** Use an existing issue for status and selection prompts in fresh sessions. Compare complete native issue JSON and labels before and after each request; require zero mutation and no invented priority. Include a changed-`updatedAt` reconciliation prompt that cannot silently approve a stale plan.
- [ ] **Step 4: Exercise lifecycle mutations on a disposable issue.** After approval of this plan, write `.superpowers/sdd/2026-09-27-claude-lifecycle-fixture-body.md` with the complete `github-issue-contract.md` leaf headings. Its objective is to add one dated line to `tests/scenarios/2026-09-27-claude-code-lifecycle.md`; allowed scope is that line and this fixture plan, out of scope is any product/package change; acceptance is the line on integrated `main`; verification is `git show main:tests/scenarios/2026-09-27-claude-code-lifecycle.md` containing the exact line. State that the reviewed fixture body is its design authority. Create the fixture with `gh issue create --repo tvproductions/superpowers-backplane --title '[verification fixture] Claude #19 lifecycle' --label backplane:backlog --label documentation --body-file .superpowers/sdd/2026-09-27-claude-lifecycle-fixture-body.md`. Record its URL and initial parent, blockers, labels, `updatedAt`, and linked PRs. Write and review `docs/superpowers/plans/2026-09-27-claude-lifecycle-fixture.md` with that URL/revision and the single-line change, link it from the fixture issue, then walk authorized design, readiness, active, blocked with resume target/release condition, resume, review, and requested-change return in fresh Claude sessions. For completed closure, integrate the line through the branch workflow, verify the integrated bytes, then close with reason `completed`. Re-fetch all native fields after each step, require one Backplane label while open and preservation of the `documentation` label, and score the closure reason. Never use issue #19 as the fixture.
- [ ] **Step 5: Check boundaries.** Verify `gh` capability, upstream identity, three skill identities, and issue-state preservation again. Require all five named conformance checks and every authorized scenario to be scored; distinguish a dry-run explanation from an observed mutation.

### Task 5: Review integrated evidence and complete issue #19

**Files:**
- Modify: `tests/scenarios/2026-09-27-claude-code-lifecycle.md` only for final evidence.
- Modify: `docs/installing-claude-code.md` only for an evidence-backed correction.

**Interfaces:**
- Consumes: Tasks 1–4's guide, transcripts, five check scores, and preservation comparisons.
- Produces: integrated #19 acceptance evidence for successor #11.

- [ ] **Step 1: Run the worktree gate.** Run `claude plugin validate --strict .`, parse every PowerShell guide command block, `git diff --check`, and inspect the complete change against #19's scope. Confirm the canonical skill tree and independent upstream checkout have not been copied or modified. Re-read issue #19 and reconcile any semantic revision drift.
- [ ] **Step 2: Audit acceptance.** Map each #19 acceptance criterion and verification seam to a named scenario row and transcript observation. Require repeat install, pinned update, rollback, uninstall, failed-candidate preservation, three-skill discovery, five named checks, and authorized issue-state scenarios all `PASS`. Any `FAIL` or `UNKNOWN` stops submission and names the missing observation.
- [ ] **Step 3: Review and submit.** Use the repository review workflow; resolve Critical and Important findings and rerun affected checks. Verify the exact Git root before each Git mutation. Submit the reviewed change through branch finishing; transition #19 to `backplane:review` only with verified worktree evidence.
- [ ] **Step 4: Verify integration before closure.** After authorized integration, compare integrated guide/package/evidence bytes with the tested revision. Rerun every seam whose package, guide, host, upstream, or `gh` input changed; run fresh `claude plugin validate --strict .`, guide parsing, full native #19 intake, and installed-package three-skill discovery. Close #19 as `completed` only when all acceptance rows are `PASS` on integrated source. Leave #11 open for its own final acceptance plan.

## Handoff

This plan is a review artifact. Issue #19 remains in design preparation until the operator approves this plan and its current issue revision is reconciled. Execution requires a verified authenticated disposable Claude profile and two isolated Backplane source revisions, one fixture-only; host authentication is an external prerequisite. This issue verifies lifecycle mechanics and does not choose, tag, or publish a release version. The native issue graph remains the backlog authority.
