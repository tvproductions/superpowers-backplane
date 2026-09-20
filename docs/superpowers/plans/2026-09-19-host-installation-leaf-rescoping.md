# Host Installation Leaf Rescoping Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Replace the oversized Claude Code and OpenCode implementation leaves with eight bounded native sub-issues while preserving the v0.1 host contract and pilot gate.

**Architecture:** Keep #11 and #12 under release parent #1 and keep their existing #6 pilot blocker edges. Add three Claude Code children and five OpenCode children, connect only their true prerequisites, then update parent continuity bodies and the verification ownership matrix. Each child remains backlog until its own approved implementation plan exists.

**Tech Stack:** Markdown, Git, GitHub CLI 2.101.0, native GitHub issue hierarchy and dependencies, PowerShell for local checks only.

**Spec:** docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md

## Global Constraints

- Functional authority remains docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md. This plan redistributes ownership only.
- Use gh for every GitHub operation. Do not use Projects, IssueOps, or a consuming-project runtime or test runner.
- Before each Git mutation, git rev-parse --show-toplevel must equal C:/Users/Jeff/source/repos/agents/superpowers-backplane exactly. Work from the standalone checkout, not a linked worktree.
- Verify origin equals https://github.com/tvproductions/superpowers-backplane.git and gh auth status succeeds before issue mutation.
- Re-read complete native fields of #1, #6, #11, and #12 immediately before mutation. Reconcile changed semantics; do not overwrite concurrent edits.
- Keep #11 and #12 at one backplane:backlog label during this redistribution. Every new child starts with exactly that label and Plan: not yet created. No child becomes ready in this plan.
- Keep #11/#12 as children of #1, their existing #2 blocker history, and their existing #6 blocking edges. Do not mutate #3, #6, upstream Superpowers, or any host installation.
- The eight child issue titles in the spec are unique creation keys. A repeated or partially failed run inspects existing issues and repairs only missing fields or edges; it never creates a duplicate.
- No release, host login, or implementation test is authorized by this plan.

## Review Focus

1. A parent issue changed since the recorded revisions: compare body, graph, and labels before editing; stop on semantic drift.
2. A create call returned an error after GitHub created the issue: find it by exact title and parent before retrying.
3. A child has a missing or reversed dependency: compare both blockedBy and blocking native fields and repair the single edge.
4. A parent or child loses a non-Backplane label or gains two lifecycle labels: compare pre/post label sets and restore only the affected issue.
5. The matrix points at a parent, an invented URL, or a missing pilot blocker: check actual child URLs and #6 blockedBy before claiming GREEN.

---

### Task 1: Capture the live baseline and prepare issue bodies

**Files:**
- Create: tests/scenarios/2026-09-19-host-leaf-rescoping.md
- Create locally for the mutation run: .superpowers/sdd/2026-09-19-host-leaf-rescoping/C1.md through O5.md, plus parent-11.md and parent-12.md; this directory is ignored

**Interfaces:**
- Consumes: approved rescoping spec and live #1/#6/#11/#12 graph
- Produces: a pre-mutation snapshot and eight complete executable issue bodies

- [ ] **Step 1: Verify the operator and repository.** Run gh auth status, git rev-parse --show-toplevel, git remote get-url origin, gh label list --repo tvproductions/superpowers-backplane --limit 100 --json name,description, gh issue create --help, and gh issue edit --help. Require the exact root and origin above, all six documented Backplane labels with matching descriptions, and installed --parent, --add-blocked-by, --body-file, and --label flags.
- [ ] **Step 2: Fetch full native intake.** For each issue 1, 6, 11, and 12, run the command below and record number, updatedAt, labels, parent, children, blockedBy, and blocking. #11 and #12 were last observed at 2026-09-19T14:11:46Z and 2026-09-19T14:11:57Z. A changed timestamp triggers semantic comparison; it is not an automatic failure.

~~~powershell
gh issue view 11 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
~~~

- [ ] **Step 3: Capture RED.** Assert #11 and #12 have zero sub-issues, their current bodies combine multiple deliverables, and the four-host matrix assigns Claude and both OpenCode variants to parent issue URLs. Record these observed ownership gaps without claiming that the existing functional checks failed.
- [ ] **Step 4: Prepare the eight body files.** Give each body the exact standard headings: Objective; Bounded Scope with Allowed and Out of Scope; Acceptance Criteria; Verification Seams; Superpowers Artifacts. Use the child contracts below. Add the approved v0.1 spec and rescoping spec paths as design authority and state Plan: not yet created. Keep native parentage and blockers out of body prose.
- [ ] **Step 5: Review body scope before creation.** Require each body to name one host or shared adapter outcome, specific PASS/FAIL/UNKNOWN evidence, fresh installed-package discovery where owned, and no implementation claim. Run gh issue list --repo tvproductions/superpowers-backplane --state all --limit 1000 --json number,title,url; check all eight exact titles against open and closed issues so a prior partial run cannot create duplicates.

#### Child body contracts

| Key | Objective and allowed output | Acceptance and verification boundary | Out of scope for this child |
|---|---|---|---|
| C1 | Claude Code manifest, marketplace, pinned install guide, canonical root skills. | One disposable clean install with compatible preinstalled upstream and fresh three-skill discovery; metadata and source revision recorded. | Multi-mode adoption, update, rollback, uninstall, full conformance. |
| C2 | Claude Code native/sibling/absent upstream setup and recovery. | Provenance, gh capability, fresh discovery, fail-closed unknown/versionless/duplicate/dirty/conflict cases; unrelated state preserved. | Package redesign, Backplane lifecycle mutation, release. |
| C3 | Claude Code repeat install and Backplane-only lifecycle. | Pinned update/rollback/uninstall guide replay; per-operation preservation, five named checks, authorized issue-state scenarios, integrated installed-package run. | OpenCode/Codex implementation, upstream update, pilot. |
| O1 | One shared OpenCode entry point, V1 plugin and V2 plugins guide. | Both supported variants load canonical root skills with compatible preinstalled upstream in a basic disposable fresh-session smoke run. | Full setup modes and lifecycle claims. |
| O2 | OpenCode V1 1.18.29+ setup and compatibility failures. | Upstream modes, gh preflight, fresh discovery, unknown/versionless/duplicate/dirty/conflict preservation, and below-1.18.29 unsupported result. | V2 behavior and lifecycle mutation. |
| O3 | OpenCode V1 Backplane lifecycle. | Repeat install, pinned update/rollback/uninstall guide replay, per-operation preservation, five named checks, authorized issue-state scenarios, integrated installed-package run. | V2 behavior, upstream update, pilot. |
| O4 | OpenCode V2 2.0.4+ setup and compatibility failures. | Upstream modes, gh preflight, fresh discovery, unknown/versionless/duplicate/dirty/conflict preservation, and below-2.0.4 unsupported result. | V1 behavior and lifecycle mutation. |
| O5 | OpenCode V2 Backplane lifecycle. | Repeat install, pinned update/rollback/uninstall guide replay, per-operation preservation, five named checks, authorized issue-state scenarios, integrated installed-package run. | V1 behavior, upstream update, pilot. |

Use the exact titles from the spec, not the keys, when invoking gh issue create. C3, O3, and O5 run all five named checks: skill-structure, native-issue-intake, language-neutral-verification, lifecycle-transitions, and superpowers-installation. Each test records host version, Backplane revision, upstream source and revision, gh capability, three installed skill identities, and scored outcomes.

### Task 2: Create Claude Code children and dependencies

**Files:**
- Modify: temporary body files for C1-C3 if preflight finds an omission
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md

**Interfaces:**
- Consumes: verified body files and unchanged #11 intake
- Produces: three native children of #11 with C1 -> C2 -> C3 blockers

- [ ] **Step 1: Re-read #11 and search exact titles.** Require it open under #1 with one backlog label and no unexpected child. For an existing exact-title child, verify its parent and body before adopting its number; do not create another.
- [ ] **Step 2: Create C1, C2, and C3 one at a time.** Invoke gh issue create with --repo tvproductions/superpowers-backplane, --parent 11, --label backplane:backlog, the exact spec title, and --body-file for that child's reviewed body. The first call is:

~~~powershell
$draftRoot = '.superpowers/sdd/2026-09-19-host-leaf-rescoping'
$C1Url = gh issue create --repo tvproductions/superpowers-backplane --parent 11 --label backplane:backlog --title 'Package and document Claude Code plugin installation' --body-file (Join-Path $draftRoot 'C1.md')
if ($LASTEXITCODE -ne 0) { throw 'Inspect exact-title issues before retrying C1 creation' }
$C1 = [int]($C1Url -replace '^.*/issues/', '')
~~~

Use the matching spec title and C2.md/C3.md for the next two calls. Assign $C2 and $C3 from their verified URLs before adding edges; record all three URLs in the scenario file.
- [ ] **Step 3: Verify each child immediately.** Run full gh issue view intake. Require parent #11, open state, one backlog label, standard headings, and no accidental plan or host-completion claim. If create returned nonzero, search by exact title and parent before any retry.
- [ ] **Step 4: Add the two dependencies.** Run gh issue edit $C2 --repo tvproductions/superpowers-backplane --add-blocked-by $C1 and gh issue edit $C3 --repo tvproductions/superpowers-backplane --add-blocked-by $C2. Re-fetch both endpoints of each edge; require reciprocal native blockedBy/blocking fields.
- [ ] **Step 5: Record Claude GREEN.** Record C1-C3 URLs and the observed native graph in the scenario file. Do not transition #11 or the children out of backlog.

### Task 3: Create OpenCode children and dependencies

**Files:**
- Modify: temporary body files for O1-O5 if preflight finds an omission
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md

**Interfaces:**
- Consumes: verified body files and unchanged #12 intake
- Produces: five native children of #12 with independent V1 and V2 paths

- [ ] **Step 1: Re-read #12 and search exact titles.** Require it open under #1 with one backlog label and no unexpected child. Recover a prior partial create by exact title and parent before making any new issue.
- [ ] **Step 2: Create O1-O5 one at a time.** Use gh issue create with --repo tvproductions/superpowers-backplane, --parent 12, --label backplane:backlog, the exact spec title, and O1.md through O5.md in $draftRoot. The first call is:

~~~powershell
$O1Url = gh issue create --repo tvproductions/superpowers-backplane --parent 12 --label backplane:backlog --title 'Build and document the shared OpenCode V1/V2 adapter' --body-file (Join-Path $draftRoot 'O1.md')
if ($LASTEXITCODE -ne 0) { throw 'Inspect exact-title issues before retrying O1 creation' }
$O1 = [int]($O1Url -replace '^.*/issues/', '')
~~~

Assign $O2 through $O5 from their verified URLs. Verify each new child with full native intake before proceeding.
- [ ] **Step 3: Add only the four intended edges.** O2 and O4 are blocked by O1; O3 is blocked by O2; O5 is blocked by O4. Run gh issue edit $O2 --repo tvproductions/superpowers-backplane --add-blocked-by $O1; repeat for $O4 blocked by $O1, $O3 blocked by $O2, and $O5 blocked by $O4, using the verified issue-number variables. Re-fetch reciprocal fields. Do not add V1-to-V2 dependencies.
- [ ] **Step 4: Record OpenCode GREEN.** Record O1-O5 URLs, both independent paths, V1 negative-floor ownership O2, and V2 negative-floor ownership O4 in the scenario file.

### Task 4: Reconcile parent contracts and repository ownership records

**Files:**
- Modify on GitHub: issue #11 and #12 bodies only
- Modify: docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md
- Modify: tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md
- Modify: HANDOFF.md
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md

**Interfaces:**
- Consumes: eight verified child URLs and existing parent/pilot graph
- Produces: continuity parent bodies and accurate host ownership documentation

- [ ] **Step 1: Draft each parent body.** Retain its host objective and all v0.1 exclusions, but replace the combined executable scope with aggregate child completion and integrated host matrix acceptance. State that child issues own implementation and each gets its own plan; the parent remains a continuity node. Link the approved design and this rescoping spec. Preserve all unrelated labels and native relationships.
- [ ] **Step 2: Re-read each parent, then edit its body only.** Use gh issue edit 11 --repo tvproductions/superpowers-backplane --body-file .superpowers/sdd/2026-09-19-host-leaf-rescoping/parent-11.md and gh issue edit 12 --repo tvproductions/superpowers-backplane --body-file .superpowers/sdd/2026-09-19-host-leaf-rescoping/parent-12.md. If updatedAt or semantics drift, reconcile and rewrite the body before editing. Re-fetch and verify one backlog label, unchanged parent #1, historical #2 blocker, and outgoing #6 edge.
- [ ] **Step 3: Correct the approved functional spec's ownership sentence.** In its Implementation boundary, state that this rescoping design supersedes only the #11/#12 executable-leaf assignment. Keep the package architecture, host floors, and all required tests unchanged.
- [ ] **Step 4: Update the four-host matrix.** Keep the original six scored assignment observations as historical. Add a current ownership section with actual child URLs: Claude C1/C2/C3, shared OpenCode O1, V1 O2/O3, V2 O4/O5, and negative floors O2/O4. Do not convert assignment scores into live host PASS results.
- [ ] **Step 5: Update HANDOFF and scenario evidence.** Record the graph, issue revisions, unchanged #6 blockers, and the next selected leaf only if a human has actually selected one. Otherwise list C1 and O1 as uncovered candidates without inventing priority.

### Task 5: Audit the graph and finish the planning branch

**Files:**
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md only for observed verification results
- Commit: rescoping spec, plan, functional-spec ownership note, matrix, handoff, scenario evidence

**Interfaces:**
- Consumes: all native issue mutations and repository edits
- Produces: reviewable, synchronized backlog evidence; no host implementation

- [ ] **Step 1: Run full native intake of #1, #6, #11, #12, and C1-C3/O1-O5.** Assert eight unique children under the intended parents, exactly one backlog label on every open new child, exact dependency edges, unchanged #1 parentage, and #6 blockedBy still containing #11 and #12 alongside its other original blockers.
- [ ] **Step 2: Audit the verification matrix.** For every current owner URL, fetch that issue and assert its parent and host/variant. Require C3, O3, and O5 to own the final host rows and O2/O4 the negative version rows. Check all standard child issue headings.
- [ ] **Step 3: Run the repository document gate.** Run git diff --check; inspect git diff --stat and the full staged diff; verify no package, skill, upstream checkout, or host guide file changed. Record the exact commands and observed counts in the scenario file. Do not rerun live host tests; this rescope has no host-code change.
- [ ] **Step 4: Review and commit the intended docs.** Use the repository's review workflow on the one planning branch. Recheck the exact Git root before git add and again before git commit; stage only the listed files; run git diff --cached --check; commit with a message describing the native host-leaf rescope. Include the spec and plan only if they changed during execution; do not recommit unchanged planning artifacts. Do not bypass hooks.
- [ ] **Step 5: Integrate only after authorized review.** Follow the branch-finishing workflow. After integration, re-read #6, #11, #12, and eight children and confirm the committed matrix matches the native graph. Do not close parents or change lifecycle labels as part of redistribution.

## Handoff

The rescope is complete only when both the native issue graph and integrated
ownership documentation agree. Host implementations remain separate future
work. C1 and O1 are the first dependency-free child candidates, but selection
belongs to the user or project policy. Each selected child gets its own current
Superpowers plan bound to its issue updatedAt before execution.
