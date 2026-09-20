# Host Installation Leaf Rescoping Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Create eight smaller native installation work items while keeping #11 and #12 as executable final host acceptance leaves and preserving the pilot gate.

**Architecture:** The eight new issues are siblings of #11 and #12 under release parent #1. Native blocker edges put Claude and OpenCode implementation before the corresponding final host acceptance leaf. The approved functional host contract stays intact; the current ownership matrix is rewritten to show the new graph.

**Tech Stack:** Markdown, Git, GitHub CLI with native parent and dependency flags, PowerShell for local checks only.

**Spec:** docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md

## Global Constraints

- The approved v0.1 adoption specification governs package and host behavior. This plan changes issue ownership, not implementation requirements.
- Use gh for GitHub. Do not use Projects, IssueOps, or a consuming-project runtime or test runner.
- Before every Git mutation, git rev-parse --show-toplevel must equal C:/Users/Jeff/source/repos/agents/superpowers-backplane exactly. Do not execute Git mutations from a linked worktree.
- Verify origin equals https://github.com/tvproductions/superpowers-backplane.git and gh auth status succeeds before issue mutation.
- Re-read full native fields of #1, #6, #11, and #12 immediately before mutation. Reconcile changed semantics rather than overwriting concurrent edits.
- All eight new siblings and both existing final leaves retain exactly one backplane:backlog label during rescope. This plan does not select, ready, close, or implement a host issue.
- Keep #11/#12 parent #1, historical #2 blockers, and outgoing #6 pilot edges. Do not mutate #3 or #6.
- Check exact titles across open and closed issues before creation. Recover partial creates by title plus native parent; never create a duplicate.
- No host login, upstream update, pilot, release, or live host test is part of this graph change.

## Review Focus

1. A parent revision changed: compare body, native graph, and labels before edit.
2. A create command returned nonzero after GitHub created an issue: inspect exact title and parent before retry.
3. A dependency is missing, reversed, or duplicated: verify blockedBy and blocking on both endpoints.
4. A draft body omits a functional obligation: compare all ten body files with the approved v0.1 contract before any gh write.
5. The ownership matrix still presents #11/#12 as broad implementation owners or says #3 is open: replace current rows, mark old rows historical, and verify actual URLs.

---

### Task 1: Prepare exact issue text and a read-only baseline

**Files:**
- Create: tests/scenarios/2026-09-19-host-leaf-rescoping.md
- Create in ignored scratch: .superpowers/sdd/2026-09-19-host-leaf-rescoping/C1.md, C2.md, C3.md, O1.md, O2.md, O3.md, O4.md, O5.md, final-11.md, final-12.md
- Draft: current owner rows for tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md

**Interfaces:**
- Consumes: approved rescope design, v0.1 functional spec, and live issue graph
- Produces: ten complete reviewable issue bodies and the pre-mutation graph snapshot

- [x] **Step 1: Verify root, operator, and CLI.** Run git rev-parse --show-toplevel, git remote get-url origin, gh auth status, gh label list --repo tvproductions/superpowers-backplane --limit 100 --json name,description, gh issue create --help, and gh issue edit --help. Require the exact root/origin, six Backplane labels with matching descriptions, and --parent, --body-file, --label, and --add-blocked-by flags.
- [x] **Step 2: Fetch full intake.** Run the command below for #1, #6, #11, and #12, recording updatedAt, body, labels, parent, subIssues, blockedBy, blocking, and URL. Compare #11/#12 revisions with 2026-09-19T14:11:46Z and 2026-09-19T14:11:57Z. Timestamp drift triggers semantic reconciliation.

~~~powershell
gh issue view 11 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
~~~

- [x] **Step 3: Record RED ownership.** The present matrix names #11/#12 for whole-host work, its GREEN note says #3 is open, and #11/#12 have zero children. Record these exact observations; they are ownership gaps, not failed host behavior.
- [x] **Step 4: Prepare all ten body files before GitHub mutation.** Every new leaf body uses Objective, Bounded Scope with Allowed and Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. The artifact section names the approved v0.1 spec, the rescope spec, and Plan: not yet created. Native parentage/blockers stay out of body prose. The two final-leaf bodies narrow #11/#12 to integrated host acceptance and retain their original host exclusions.
- [x] **Step 5: Review the bodies against the spec.** C1/O1 cover package and guide smoke only. C2/O2/O4 cover upstream modes and failed preflight. C3/O3/O5 cover lifecycle, guide replay, preservation, the five named checks, and authorized issue-state scenarios. final-11.md requires completed C1-C3 and aggregate Claude evidence; final-12.md requires completed O1-O5 and distinct V1/V2 evidence. Record host revision, Backplane revision, upstream identity, gh capability, three installed skills, and PASS/FAIL/UNKNOWN requirements in the owning body.
- [x] **Step 6: Check duplicate titles.** Run gh issue list --repo tvproductions/superpowers-backplane --state all --limit 1000 --json number,title,url. Search the eight exact titles in the rescope design. If a title already exists, inspect full native parent and body before deciding whether it is a prior partial create.
- [x] **Step 7: Prepare the documentation diff.** Draft the functional spec's ownership correction and replacement current matrix table before creating issues. Use key names in the draft, not invented URLs. The final matrix receives actual URLs after creation. Review all ten body files and the documentation diff as one concrete mutation set.

### Task 2: Publish the approved planning authority

**Files:**
- Modify only if review requires: rescope design and this plan
- Keep: ten reviewed body files in ignored scratch for the mutation run

**Interfaces:**
- Consumes: approved planning branch and exact mutation set
- Produces: reachable design and plan revisions before issue bodies cite them

- [ ] **Step 1: Review the planning branch.** Require clean staged diff checks, no host package edits, and a review of the spec, plan, and ten issue body files. Do not start issue creation while an important review finding remains.
- [ ] **Step 2: Integrate the approved design and plan.** Use the repository branch-finishing workflow and authorized PR merge. Recheck the exact Git root before each Git mutation. Record the integrated source SHA in the scenario file; issue bodies cite the durable integrated design path.
- [ ] **Step 3: Re-read #1/#6/#11/#12.** Confirm their semantics and native relationships still match Task 1 before the first GitHub issue mutation. If they drifted, repair the local drafts and re-review the affected text.

### Task 3: Create eight sibling issues and dependency edges

**Files:**
- Consume: the eight reviewed scratch body files
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md

**Interfaces:**
- Consumes: integrated design/plan and reviewed body files
- Produces: eight native children of #1 and prerequisites into #11/#12

- [ ] **Step 1: Create C1-C3 one at a time.** Use the exact design titles and body files, --parent 1, and --label backplane:backlog. The first call is below. After every call, parse and record the returned URL/number; if gh returns nonzero, inspect exact-title issues before retrying.

~~~powershell
$draftRoot = '.superpowers/sdd/2026-09-19-host-leaf-rescoping'
$C1Url = gh issue create --repo tvproductions/superpowers-backplane --parent 1 --label backplane:backlog --title 'Package and document Claude Code plugin installation' --body-file (Join-Path $draftRoot 'C1.md')
if ($LASTEXITCODE -ne 0) { throw 'Inspect exact-title issues before retrying C1 creation' }
$C1 = [int]($C1Url -replace '^.*/issues/', '')
~~~

- [ ] **Step 2: Verify each Claude issue.** Fetch complete native intake. Require open state, parent #1, one backlog label, full body headings, and exact reviewed scope. Assign verified $C2 and $C3 numbers from their URLs.
- [ ] **Step 3: Add Claude blockers.** Run gh issue edit $C2 --repo tvproductions/superpowers-backplane --add-blocked-by $C1; then block $C3 by $C2 and #11 by $C3. Re-fetch both ends of each edge.
- [ ] **Step 4: Create O1-O5 one at a time.** Use --parent 1, --label backplane:backlog, exact design title and O1.md through O5.md body files. Verify each native issue before the next create; assign $O1 through $O5 from returned URLs.
- [ ] **Step 5: Add OpenCode blockers.** O2/O4 are blocked by O1; O3 by O2; O5 by O4; #12 by O3 and O5. Use gh issue edit --add-blocked-by and verify reciprocal fields. Do not connect V1 and V2 to each other.
- [ ] **Step 6: Record GREEN graph.** Record all eight URLs and exact blocker edges. Require #11/#12 still block #6 and #6 retains its other original blockers.

### Task 4: Narrow final leaves and publish current ownership

**Files:**
- Modify on GitHub: #11/#12 bodies only
- Modify: docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md
- Modify: tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md
- Modify: HANDOFF.md
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md

**Interfaces:**
- Consumes: verified sibling URLs and the two reviewed final-leaf bodies
- Produces: narrow executable host acceptance leaves and current ownership docs

- [ ] **Step 1: Re-read #11/#12 and edit body only.** Use gh issue edit 11 --repo tvproductions/superpowers-backplane --body-file .superpowers/sdd/2026-09-19-host-leaf-rescoping/final-11.md and the same command for 12/final-12.md. Reconcile changed semantics first. Preserve labels, parent #1, historical #2 blockers, and outgoing #6 edges.
- [ ] **Step 2: Correct functional ownership.** In the approved v0.1 spec's Implementation boundary, state that the eight new siblings own bounded implementation and #11/#12 own final host acceptance. Do not alter host floors or functional requirements.
- [ ] **Step 3: Replace current matrix ownership.** Move the original #11/#12 assignment table and GREEN note under a dated historical heading. Make one current table authoritative with actual URLs, #11 Claude final, #12 OpenCode cross-variant final, prerequisite evidence owners C1-C3/O1-O5, and negative floors O2/O4. Record #3 as closed/completed. Do not mark an assignment as a passing live host run.
- [ ] **Step 4: Update handoff and scenario evidence.** Record current issue revisions, exact graph, preserved #6 gate, and no selected next leaf unless the user actually selects one.

### Task 5: Verify, review, and integrate the graph record

**Files:**
- Modify: tests/scenarios/2026-09-19-host-leaf-rescoping.md for observed verification
- Commit: the functional-spec ownership correction, current matrix, handoff, and evidence

**Interfaces:**
- Consumes: the native issue graph and documentation edits
- Produces: integrated, matching graph and documentation evidence

- [ ] **Step 1: Run full intake of #1/#6/#11/#12 and all eight new issues.** Require native parent #1 for the new issues, exact blocker edges, one backlog label per open issue, and #6 still blocked by #11/#12 plus its other original blockers.
- [ ] **Step 2: Audit contracts and matrix.** Assert standard headings and observable acceptance in all eight new bodies and both narrowed final bodies. Fetch every current owner URL. Require V1/V2 negative-floor ownership and no stale #3-open claim.
- [ ] **Step 3: Run the document gate.** Run git diff --check, inspect the complete diff, and verify no package, guide, skill, or upstream file changed. Record observed counts and commands; do not rerun live host tests for a graph-only change.
- [ ] **Step 4: Review and commit.** Run the repository review workflow, recheck exact Git root before git add and commit, stage only intended documentation, run git diff --cached --check, and commit without bypassing hooks.
- [ ] **Step 5: Integrate after authorized review.** Finish the branch, then re-read the native graph and confirm the integrated matrix matches it. This rescope does not ready, select, close, or implement a host issue.

## Handoff

The redistribution is complete only when integrated documentation and the
native graph agree. #11/#12 remain executable final leaves. The first
dependency-free new issues are C1 and O1; no priority or selection is inferred.
Each chosen issue gets its own current Superpowers plan bound to its issue
revision before execution.
