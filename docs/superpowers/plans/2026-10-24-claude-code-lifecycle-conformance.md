# Claude Code Lifecycle and Conformance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify the published Claude Code Backplane package through repeat install, pinned update, rollback, Backplane-only uninstall, preservation, fresh discovery, the five conformance checks, and authorized issue-state scenarios.

**Architecture:** Use one disposable Claude Code profile and pinned published clones of Backplane. The candidate lifecycle is exercised through Claude's native marketplace/plugin commands, with upstream Superpowers supplied separately as a sibling checkout and never updated by Backplane. Evidence is a dated scenario report plus prompt/response transcripts and a machine-readable receipt.

**Tech Stack:** Claude Code CLI, Git, GitHub CLI (`gh`), `jq`, `shasum`, Ruby YAML parsing, upstream Superpowers v7.0.1

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`, with the host-leaf rescope at `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`

## Global Constraints

- Work item is issue #19, observed revision `2026-09-27T14:09:57Z`; re-read complete native state before each issue mutation.
- Use the published Backplane source at `b0d702f8821d6d29184118410ec6ff2d8fb63438` as the candidate unless the operator selects a newer reviewed revision.
- Use upstream Superpowers v7.0.1 at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` from `.agents/superpowers`; do not update or relocate upstream as a side effect.
- Use a disposable Claude profile via `CLAUDE_CONFIG_DIR`; do not copy credentials and do not mutate the normal Claude profile.
- Preserve unrelated marketplaces/plugins, user files, upstream state, repository history, and GitHub issue state across every operation.
- Do not use pytest or introduce a project runtime, GitHub Project, or IssueOps system.
- Keep issue #19 `backplane:designing` until its plan is approved; selection does not move it to ready.
- No publication, tag, release, or issue closure is authorized by this plan.

## Review Focus

- A failed lifecycle candidate must leave the prior verified Backplane installation and profile intact; every update/rollback task must snapshot before mutation.
- The pinned update must observe a source/revision change, not merely the same declared version; rollback must prove the exact prior revision was restored.
- Uninstall must remove only Backplane-owned state and leave upstream, unrelated plugins, and issue state unchanged.
- Fresh-session discovery must show actual Skill tool loads from separate upstream and Backplane package roots, not inventory alone.
- Every issue-state scenario must preserve unrelated labels and fail closed when lifecycle cardinality or evidence is wrong.

---

### Task 1: Disposable profile and source preflight

**Files:**
- Create: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-10-24-claude-code-lifecycle.prompt.txt`

**Interfaces:**
- Consumes: approved #19 authorities and current host/upstream state
- Produces: the isolated profile, source identities, and baseline snapshots used by Tasks 2–6

- [ ] **Step 1: Record the host and source identities**

Run and record:
- `claude --version`
- `git -C .agents/superpowers rev-parse HEAD`
- `git -C .agents/superpowers remote get-url origin`
- `git -C .agents/superpowers status --porcelain=v1`
- `gh auth status`
- `gh issue view 19 --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`

Expected: Claude Code is operational, upstream is clean at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` with the authoritative `obra/superpowers` origin, `gh` is authenticated, and #19 is OPEN/`backplane:designing` at the recorded revision.

- [ ] **Step 2: Create the disposable Claude profile**

Create an unused directory under the approved temporary workspace and use it only as `CLAUDE_CONFIG_DIR` for child commands. Do not copy credentials. Capture its initial marketplace/plugin inventory.

Expected: an empty, disposable Claude profile exists; the normal Claude profile is unchanged.

- [ ] **Step 3: Publish and verify the pinned Backplane clone**

In an unused temporary parent:
- `gh repo clone tvproductions/superpowers-backplane <backplane-checkout>`
- `git -C <backplane-checkout> checkout --detach b0d702f8821d6d29184118410ec6ff2d8fb63438`
- Verify exact `tvproductions/superpowers-backplane` origin, HEAD, and clean status.
- `gh api repos/tvproductions/superpowers-backplane/commits/b0d702f8821d6d29184118410ec6ff2d8fb63438 --jq .sha`
- `claude plugin validate --strict <backplane-checkout>`
- Record SHA-256 values for `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `docs/installing-claude-code.md`, and both canonical `SKILL.md` files.

Expected: the pinned source is published, clean, valid, and at the selected candidate revision.

- [ ] **Step 4: Record the baseline evidence shell**

Create `tests/scenarios/2026-10-24-claude-code-lifecycle.md` with a scope section identifying #19, the candidate and upstream revisions, the disposable profile, and the rule that no lifecycle result is claimed yet.

Expected: the evidence file exists with no success claim.

### Task 2: Repeat install and preservation

**Files:**
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-10-24-claude-code-repeat-install.prompt.txt`

**Interfaces:**
- Consumes: Task 1 profile, source identities, and baseline snapshots
- Produces: the installed Backplane candidate identity and repeat-install evidence

- [ ] **Step 1: Install the candidate**

Run the guide's clean install path in the disposable profile:
- `claude plugin marketplace add <backplane-checkout>`
- `claude plugin install superpowers-backplane@superpowers-backplane --scope user`
- `claude plugin list --json`

Expected: exactly one effective Backplane plugin and marketplace; no unrelated entry is created.

- [ ] **Step 2: Replay the same install**

Run the same marketplace-add and plugin-install commands again. If the CLI asks for confirmation, use its documented noninteractive flags, but do not bypass an interactive safety prompt outside a disposable profile.

Expected: the second install remains one effective Backplane installation; no duplicate plugin ID or marketplace appears.

- [ ] **Step 3: Verify preservation**

Compare before/after:
- installed plugin IDs, versions, scopes, and enabled states
- marketplace IDs and source paths
- `installed_plugins.json`, `known_marketplaces.json`, and `settings.json` hashes, excluding volatile non-config data where the host forces it
- upstream checkout HEAD/status
- complete #19 native intake

Expected: only the expected install state changed; upstream and issue state remain unchanged.

### Task 3: Pinned update and rollback

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-10-24-claude-code-update-rollback.prompt.txt`

**Interfaces:**
- Consumes: Task 2 installed candidate and prior/published source clones
- Produces: documented and verified pinned update/rollback commands and identity evidence

- [ ] **Step 1: Add lifecycle documentation RED**

Search `docs/installing-claude-code.md` for exact operators' commands for:
- updating the pinned Backplane marketplace/plugin to a selected reviewed revision
- rolling back to the recorded prior revision
- Backplane-only uninstall

Expected: the update/rollback/uninstall anchors are absent or incomplete before this task.

- [ ] **Step 2: Add lifecycle documentation GREEN**

Extend `docs/installing-claude-code.md` with exact, pinned commands. Do not change package manifests, canonical skill bytes, or the existing clean-install/setup text except where required to link the new lifecycle section. Name the selected prior and candidate revisions and the safety/refusal behavior.

Expected: the guide now names exact update, rollback, and Backplane-only uninstall commands and preservation/refusal rules.

- [ ] **Step 3: Establish the recorded prior revision**

Use a fresh disposable profile, or first remove only the Task 2 candidate through the host's supported uninstall command. Install the recorded prior published revision `d774361919f3afdbede1710ec3ca109164523ff9` using the guide's clean-install path. Record the effective plugin/marketplace identity and source revision.

Expected: the update test starts at the recorded prior revision with no unrelated state mutated.

- [ ] **Step 4: Execute the pinned update**

Use the new guide commands to move the same Backplane marketplace/plugin to `b0d702f8821d6d29184118410ec6ff2d8fb63438`. Record source, plugin inventory, and installed package bytes/hashes.

Expected: the effective source/revision changes to the candidate; no unrelated marketplace/plugin changes.

- [ ] **Step 5: Execute rollback**

Use the guide rollback commands to restore `d774361919f3afdbede1710ec3ca109164523ff9`. Record before/after source and installed package identities.

Expected: the exact prior revision is restored and verified; the profile remains usable.

### Task 4: Backplane-only uninstall and fresh discovery

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-10-24-claude-code-discovery.prompt.txt`

**Interfaces:**
- Consumes: restored prior installation and upstream sibling mode
- Produces: uninstall evidence and three separate fresh Skill loads

- [ ] **Step 1: Add uninstall documentation GREEN**

Ensure the guide's Backplane-only uninstall section names the exact host command and the rule that upstream, unrelated plugins, and issue state remain unchanged. Use the CLI's supported uninstall command and scope.

Expected: the guide contains a concrete Backplane-only uninstall path.

- [ ] **Step 2: Run uninstall**

From the restored profile, run the guide uninstall command. Record before/after installed plugin IDs, marketplace IDs, and config hashes.

Expected: only the Backplane plugin/marketplace state is removed; upstream and unrelated state remain unchanged.

- [ ] **Step 3: Reinstall for discovery checks**

Reinstall the candidate from Task 3 using the guide clean-install path. Record the resulting identity.

Expected: one Backplane plugin is present again before fresh-session checks.

- [ ] **Step 4: Run three separate fresh discovery sessions**

Using upstream sibling mode (`--plugin-dir .agents/superpowers`), start three separate fresh Claude sessions and separately invoke:
- `superpowers:using-superpowers`
- `superpowers-backplane:managing-superpowers-backlog`
- `superpowers-backplane:managing-superpowers-handoffs`

Record the actual Skill tool calls and returned base directories in transcripts.

Expected: three successful loads from separate upstream and Backplane package roots.

### Task 5: Conformance checks and issue-state scenarios

**Files:**
- Create: `tests/scenarios/2026-10-24-claude-code-lifecycle.json`
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Create: `tests/scenarios/transcripts/2026-10-24-claude-code-conformance.prompt.txt`

**Interfaces:**
- Consumes: Tasks 1–4 installed candidate, disposable profile, and upstream sibling mode
- Produces: scored five-check receipt and authorized issue-state scenarios

- [ ] **Step 1: Run structural and capability checks**

Record:
- `gh issue edit --help` exposes `--add-label` and `--remove-label`
- `gh issue close --help` exposes a closure reason
- Backplane `SKILL.md` YAML delimiters, exact names, and `Use when` descriptions
- all direct linked reference targets exist
- no placeholder remains

Expected: all structural and capability checks pass with available native tooling.

- [ ] **Step 2: Run the behavioral conformance prompts**

Using the disposable profile and upstream sibling mode, run fresh sessions for:
- `native-issue-intake`
- `language-neutral-verification`
- `lifecycle-transitions`
- `superpowers-installation`

Use the exact prompts and rubrics mapped in `tests/scenarios/2026-08-16-native-issue-intake-green.md`, `tests/scenarios/2026-08-16-lifecycle-transition-refactor.md`, and `tests/scenarios/2026-08-16-superpowers-installation-refactor.md`. Capture each response without editing it.

Expected: every listed expectation is scored; no expectation is left unscored.

- [ ] **Step 3: Run authorized issue-state scenarios**

Create one disposable issue only after explicit operator authorization. Use it for:
- read-only/selection-only zero mutation
- exactly one correct Backplane label after an authorized transition
- unrelated label preservation
- blocked/resume or review reversal where the scenario rubric requires it
- completed closure only after integrated verification evidence

Record complete before/after native JSON and updatedAt values. If a scenario is not authorized, record it as not run rather than inventing a substitute.

Expected: all authorized issue-state scenarios preserve native relationships and fail closed on invalid state.

### Task 6: Integration and review evidence

**Files:**
- Modify: `docs/installing-claude-code.md`
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.md`
- Modify: `tests/scenarios/2026-10-24-claude-code-lifecycle.json`

**Interfaces:**
- Consumes: Tasks 1–5 results and guide updates
- Produces: whole-change evidence ready for review and submission

- [ ] **Step 1: Whole-change review**

Diff the branch against its base. Confirm the changed files are exactly the guide, lifecycle report/receipt, and transcripts; no package manifest or canonical skill bytes changed.

Expected: no unrelated file changes and no unexpected diff.

- [ ] **Step 2: Final checks**

Run:
- `git diff --check <base>...HEAD`
- `claude plugin validate --strict .`
- `jq -e '(.pass | type == "number") and (.fail == 0)' tests/scenarios/2026-10-24-claude-code-lifecycle.json`
- fresh complete #19 native intake

Expected: all checks pass; the issue remains OPEN/`backplane:designing` until approval and submission.

- [ ] **Step 3: Prepare submission**

After operator approval, move the work to a review-ready branch/PR. Submission does not close #19 or claim integrated completion.
