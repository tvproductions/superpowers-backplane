# Claude Code Package and Installation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver the native Claude Code package, a pinned installation guide, and one verified clean-install discovery run for issue #17.

**Architecture:** The Claude plugin manifest and marketplace live in `.claude-plugin/` at the repository root. The marketplace points to that root, so Claude Code discovers the two canonical `skills/` folders without a second authored copy. A guide describes a reviewed Git commit and native plugin installation; a disposable Claude configuration with separately installed Superpowers supplies the smoke evidence.

**Tech Stack:** Claude Code plugin and marketplace JSON, Markdown, PowerShell for host verification, Git, GitHub CLI (`gh`). PowerShell is a test-host tool, not an adopter project runtime.

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`; the approved scope allocation is in `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`.

**Issue:** https://github.com/tvproductions/superpowers-backplane/issues/17

**Issue revision consumed:** `2026-09-20T13:01:43Z` (complete native intake after the authorized `backplane:designing` transition; body and graph still match the approved rescope).

## Global Constraints

- Issue #17 owns Claude package metadata, the initial guide, and **one** clean-install/fresh-session smoke run. Setup modes and failure handling belong to #18; lifecycle, five-check conformance, and issue-state scenarios belong to #19; final host acceptance belongs to #11.
- Use only the root `skills/managing-superpowers-backlog/` and `skills/managing-superpowers-handoffs/` trees. Do not copy either skill or upstream Superpowers content.
- Install upstream Superpowers independently. The repository's `.agents/superpowers` is the authoritative stable `v6.4.1` checkout at `5bf4e78011075bcfc0dc295f0724994cd123ee71`; do not change its revision as part of #17.
- Require Git, authenticated `gh`, and an authenticated Claude Code session for a live check. Do not copy credentials into a disposable profile. If isolated Claude authentication is unavailable, record `UNKNOWN` and keep the smoke gate open.
- Use a reviewed, published immutable Backplane commit for the guide and smoke run. Publish the feature commit to the expected origin after package and guide review; replay the exact pinned guide before merge. After merge, verify that integrated package and guide content match the tested commit, rerunning any changed seam.
- Keep update, rollback, and uninstall instructions explicitly pending #19. Do not claim setup-mode coverage or full conformance from the smoke run.
- Before **every** Git mutation, require `git rev-parse --show-toplevel` to equal `C:/Users/Jeff/source/repos/agents/superpowers-backplane` exactly. The current project rule makes the root checkout the Git-mutation workspace; use disposable host fixtures for installation isolation. Require `origin` to resolve to `https://github.com/tvproductions/superpowers-backplane.git` before a GitHub operation or push.
- Re-read #17's complete native fields before each lifecycle transition. Reconcile any semantic change from the consumed revision. Exactly one Backplane lifecycle label must remain, with unrelated labels preserved.
- Do not publish a release, update upstream, modify a real adopter profile, or use a production backlog issue as test data.

## File Map

| File | Responsibility |
|---|---|
| `.claude-plugin/plugin.json` | Claude plugin identity and `0.1.0` version. |
| `.claude-plugin/marketplace.json` | One marketplace entry whose source is the repository root. |
| `docs/installing-claude-code.md` | Pinned install, setup request, first discovery, and deferred lifecycle boundary. |
| `README.md` | Link to the Claude guide. |
| `tests/scenarios/2026-09-20-claude-code-package-installation.md` | RED/GREEN results, host identity, fixture commands, and scored smoke evidence. |
| `tests/scenarios/transcripts/2026-09-20-claude-code-discovery.md` | Exact fresh-session discovery prompt, response, and interpretation. |

## Review Focus

1. **Wrong plugin root:** a marketplace entry pointing inside `.claude-plugin/` omits root skills. Task 1 checks the resolved source and both skill paths.
2. **Metadata drift:** Claude and Codex package identities or versions differ. Task 1 compares the Claude manifest, marketplace entry, and root `plugin.json`.
3. **False isolation:** a smoke run inherits the operator's installed plugins or writes into their profile. Task 3 checks the fresh configuration path and inventories it before and after install.
4. **Unproved upstream:** a checkout path alone does not show an operational, independent Claude plugin. Task 3 verifies upstream provenance, package identity, and fresh-session skill discovery.
5. **Unpinned or overclaimed guide:** a moving branch or unverified lifecycle steps look production-ready. Task 2 verifies the reviewed SHA and absence of lifecycle claims; Task 3 replays the published feature commit before review; Task 4 checks the integrated tree against that tested commit.

## Execution Entry After Plan Approval

This plan is presently a review artifact, not execution authority. After the user approves it and selects an execution method, integrate the plan through the project's branch-finishing workflow so it is reachable on `main`, then re-read #17 and link the durable plan in its Superpowers Artifacts section. The issue edit changes `updatedAt`; compare body semantics and record the new revision before execution. With the approved design, current plan, complete contract, and no unresolved native blocker, transition `backplane:designing` to `backplane:ready`. Transition `backplane:ready` to `backplane:active` immediately before the first Task 1 implementation action. Verify exactly one Backplane label and preserved unrelated labels after each transition. Create the implementation branch in the root checkout after verifying the Git root. Do not mark #17 ready or active while this plan awaits review.

---

### Task 1: Add the root Claude plugin and marketplace

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`
- Create: `tests/scenarios/2026-09-20-claude-code-package-installation.md`

**Interfaces:**
- Consumes: the existing root `skills/` tree and root `plugin.json` version `0.1.0`.
- Produces: `superpowers-backplane@superpowers-backplane` in Claude Code with both canonical skills. Tasks 2 and 3 use that exact ID.

- [ ] **Step 1: Recheck the host contract.** Read the current [Claude plugin format](https://code.claude.com/docs/en/plugins), [marketplace schema](https://code.claude.com/docs/en/plugin-marketplaces), and [install commands](https://code.claude.com/docs/en/discover-plugins). Run `claude --version`, `claude plugin marketplace add --help`, `claude plugin install --help`, and `claude plugin validate --help`; record the observed version and any changed requirements in the scenario file before editing metadata. The planning baseline observed Claude Code `2.1.241` on 2026-09-20; execution must recheck it.
- [ ] **Step 2: Capture RED.** Run `Test-Path .claude-plugin/plugin.json` and `Test-Path .claude-plugin/marketplace.json` from the verified project root. Both must be false at baseline. Record that Claude cannot resolve a Backplane marketplace from this source yet, along with the current root manifest version and the two canonical `SKILL.md` paths.
- [ ] **Step 3: Write the minimal native metadata.** Create the files below. The marketplace source `./` means the repository root, and its only plugin entry is Backplane. Set the marketplace entry version to `0.1.0` and verify it equals both Claude and root manifests, as the approved release contract requires. Do not add a copied `skills/` folder inside `.claude-plugin/`.

  `.claude-plugin/plugin.json`:

  ```json
  {
    "name": "superpowers-backplane",
    "description": "Native GitHub backlog continuity for upstream Superpowers",
    "version": "0.1.0",
    "repository": "https://github.com/tvproductions/superpowers-backplane"
  }
  ```

  `.claude-plugin/marketplace.json`:

  ```json
  {
    "name": "superpowers-backplane",
    "owner": {"name": "tvproductions"},
    "plugins": [{
      "name": "superpowers-backplane",
      "version": "0.1.0",
      "source": "./",
      "description": "Native GitHub backlog continuity for upstream Superpowers"
    }]
  }
  ```

- [ ] **Step 4: Verify GREEN.** Run `claude plugin validate --strict .` and parse both JSON files with `ConvertFrom-Json`. Assert Claude name and version equal the root `plugin.json`; marketplace name and plugin name are `superpowers-backplane`, and its entry version equals both manifests; its source is `./`; `skills/managing-superpowers-backlog/SKILL.md` and `skills/managing-superpowers-handoffs/SKILL.md` each occur once in tracked source. Inspect `git status --short --untracked-files=all` for only the intended metadata and scenario file. If this Claude version rejects root source `./`, stop and reconcile the package location against the approved spec and current primary docs; do not add a copied skill tree.
- [ ] **Step 5: Commit the package slice.** Run `git diff --check`, verify the Git top level immediately before `git add`, stage only the two JSON files and scenario record, run `git diff --cached --check`, verify the root again, and commit `feat: add root Claude Code plugin package`.

### Task 2: Write the pinned install and setup guide

**Files:**
- Create: `docs/installing-claude-code.md`
- Modify: `README.md`
- Modify: `tests/scenarios/2026-09-20-claude-code-package-installation.md`

**Interfaces:**
- Consumes: Task 1's Claude marketplace and plugin ID.
- Produces: a guide whose full pinned-source path Task 3 replays from a published feature commit before review.

- [ ] **Step 1: Capture documentation RED.** Read `README.md` as an adopter. Record the missing Claude guide link, reviewed-commit preflight, native marketplace and plugin commands, setup request, and fresh three-skill discovery as distinct missing expectations.
- [ ] **Step 2: Document the pinned checkout.** Link the Claude guide from `README.md`. In the guide, read a user-supplied revision with `$backplaneRevision = Read-Host 'Reviewed 40-character Backplane commit'`, require `^[0-9a-f]{40}$`, set `$backplaneCheckout = Join-Path (Get-Location) 'superpowers-backplane'`, and reject that path if already occupied. Show `gh repo clone tvproductions/superpowers-backplane $backplaneCheckout`, `git -C $backplaneCheckout checkout --detach $backplaneRevision`, `git -C $backplaneCheckout remote get-url origin`, and `gh api "repos/tvproductions/superpowers-backplane/commits/$backplaneRevision" --jq .sha`. Require the resolved origin and published SHA to match the requested source before installing. Tell the reader to inspect both manifests and root skills. Do not use moving `main` as the selected installation revision.
- [ ] **Step 3: Document native install and setup.** From that pinned checkout, show `claude plugin marketplace add $backplaneCheckout` followed by `claude plugin install superpowers-backplane@superpowers-backplane --scope user` and `claude plugin list`. Explain that a local-directory marketplace loads the checked-out source in place, so the checkout must remain at the recorded SHA until a separately verified update. In a new Claude session ask: `Set up Superpowers Backplane in this Claude Code session.` The setup response must identify one Backplane package, the two Backplane skills, independent operational upstream Superpowers with a source and observable version/revision, authenticated capability-complete `gh`, and fresh-session discovery of `superpowers:using-superpowers` plus both namespaced Backplane skills. If an input is unknown, report `UNKNOWN` and a recovery action without changing issue state. Mark update, rollback, and Backplane-only uninstall as pending #19 verification; direct readers to upstream's own installation channel for upstream changes.
- [ ] **Step 4: Verify the guide contract.** Compare every command and claim with the current Claude docs and the v0.1 spec. Assert the guide uses a 40-character reviewed revision, points to the canonical package, requests setup explicitly, and contains no unsupported lifecycle command. Assert it does not instruct users to alter `.agents/superpowers`, install a consuming-project runtime, or mutate issues during setup. Record GREEN results for the Step 1 expectations.
- [ ] **Step 5: Commit the guide slice.** Verify the exact Git top level before staging only `README.md`, the Claude guide, and the scenario file. Run `git diff --cached --check`, verify the root again, and commit `docs: explain pinned Claude Code installation`.

### Task 3: Run the isolated package smoke

**Files:**
- Modify: `tests/scenarios/2026-09-20-claude-code-package-installation.md`
- Create: `tests/scenarios/transcripts/2026-09-20-claude-code-discovery.md`

**Interfaces:**
- Consumes: Task 2's exact commands, Task 1's package, and independently installed upstream Superpowers.
- Produces: one scored clean-install and fresh-session discovery result without lifecycle or full-conformance claims.

- [ ] **Step 1: Establish isolation and credentials.** Create an unused temporary Claude configuration directory and set `CLAUDE_CONFIG_DIR` only for child Claude processes, as documented by [Claude's environment reference](https://code.claude.com/docs/en/env-vars). Run `claude auth status --json` in that profile; require `loggedIn: true` before a live session. If it is not authenticated, ask the operator to sign in to this isolated profile; do not copy credentials from the normal profile. Inventory the disposable profile's marketplaces and plugins before mutation, and record the path, `claude --version`, and `gh auth status` result without logging secrets. Run the full #17 intake command from `skills/managing-superpowers-backlog/references/github-issue-contract.md`, `gh issue edit --help`, and `gh issue close --help`; require all native fields, label edit flags, and closure reason support for the recorded `gh` capability result.
- [ ] **Step 2: Install independent upstream first.** Verify `.agents/superpowers` has exact `obra/superpowers` origin, stable `v6.4.1` manifest, required skill files, and recorded commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`. Resolve `$upstreamCheckout = (Resolve-Path -LiteralPath .agents/superpowers).Path` and, in the disposable profile, add its own `.claude-plugin/marketplace.json` via `claude plugin marketplace add $upstreamCheckout` and install `superpowers@superpowers-dev`. Record that upstream's marketplace and plugin entries exist before Backplane install; do not modify the upstream checkout.
- [ ] **Step 3: Replay the pinned guide from a published feature commit.** Verify the Git root, current origin, and clean intended diff; push the reviewed implementation branch without changing `main`, then record its full package-and-guide commit SHA as `$backplaneRevision`. Confirm `gh api "repos/tvproductions/superpowers-backplane/commits/$backplaneRevision" --jq .sha` returns that SHA. In an unused temporary directory outside this repository, run the guide's `gh repo clone tvproductions/superpowers-backplane $backplaneCheckout`, `git -C $backplaneCheckout checkout --detach $backplaneRevision`, and origin/SHA checks. Require both Claude manifests and both canonical skills in the checkout. From a neutral empty project directory, run the guide's `claude plugin marketplace add $backplaneCheckout` and `claude plugin install superpowers-backplane@superpowers-backplane --scope user` with only the isolated `CLAUDE_CONFIG_DIR` set. Assert exactly one Backplane plugin, the separately installed upstream plugin and marketplace unchanged, the installed Backplane version `0.1.0`, and both skill hashes matching the published commit. Record exact commands and paths.
- [ ] **Step 4: Score fresh setup request and discovery.** Start a fresh authenticated Claude session from a neutral empty project directory under the isolated profile, and submit the guide's exact request: `Set up Superpowers Backplane in this Claude Code session.` Capture the unedited response. In a second fresh session, inspect `/help` Custom commands for `superpowers:using-superpowers` and both namespaced Backplane skills, then invoke each with a harmless read-only prompt; Claude's plugin documentation treats the command listing and invocation as discovery checks. Capture the host listing, invocations, exact prompts, and responses in the transcript file. Cross-check each identity against the installed plugin ID, source path, and skill hash. Score each identity and setup response `PASS`, `FAIL`, or `UNKNOWN`; a model's statement alone cannot earn `PASS`. Record host version, Backplane SHA, upstream source/revision, `gh` capability result, and overall smoke result. Do not score #18/#19 obligations as passing.
- [ ] **Step 5: Verify preservation and commit evidence.** Re-inventory the disposable profile. Assert the independently installed upstream and every unrelated pre-existing marketplace entry are unchanged; inspect the normal profile inventory to ensure it was not used for the test. Verify the exact Git top level before staging the scenario and transcript, run `git diff --cached --check`, verify the root again, and commit `test: verify Claude Code clean installation`.

### Task 4: Review, integrate, and verify the pinned published source

**Files:**
- Modify: `tests/scenarios/2026-09-20-claude-code-package-installation.md` for final integrated evidence
- Modify: `docs/installing-claude-code.md` only for a correction proved by the smoke or integrated replay

**Interfaces:**
- Consumes: Tasks 1–3 and #17's complete native acceptance contract.
- Produces: reviewed integrated package and verified issue completion evidence; it does not deliver #18 or #19.

- [ ] **Step 1: Audit acceptance before review.** Require Task 3's overall smoke and each discovery identity to be `PASS`. Run `claude plugin validate --strict .`, `git diff --check origin/main...HEAD`, and `git status --short`. Inspect the full diff for duplicate skills, upstream files, credentials, and unverified lifecycle language. If isolated host authentication or a required observation is unavailable, keep #17 in its evidence-supported open state and record the exact unresolved gate.
- [ ] **Step 2: Request review and verify the branch.** Request independent review of the package, guide, pinned-source commands, and smoke evidence under `superpowers:requesting-code-review`; resolve Critical and Important findings. Run `superpowers:verification-before-completion`. Once implementation, review, and workspace verification support submission, re-read #17 and move `backplane:active` to `backplane:review`; verify label cardinality and preservation. Then use `superpowers:finishing-a-development-branch` for authorized integration. Do not treat PR creation as completion.
- [ ] **Step 3: Verify the integrated source.** After integration, verify the tested feature commit is reachable from `main` and at the expected GitHub origin. Compare the integrated Claude manifest, marketplace, guide, README link, and canonical skill hashes against the exact tested commit. Run `claude plugin validate --strict .` on integrated source and start one fresh session in the existing authorized isolated profile to confirm the three skills remain discoverable from the installed pinned commit. Record the integration commit, tree comparison, and fresh response. If any relevant package, guide, or skill content changed during integration, repeat the affected pinned install and discovery seam before claiming PASS. Keep #17 open for any `FAIL` or `UNKNOWN`.
- [ ] **Step 4: Reconcile and complete #17.** Re-read all required native issue fields and compare their current semantics to the approved design and plan; classify any drift before acting. After reviewed integration and the fresh published-source replay pass, close #17 with reason `completed`; re-fetch it and verify the closure reason, absence of an open lifecycle label, and the unchanged outgoing blocker to #18.
