# Issue #5 Self-Hosting Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Approved by the operator on 2026-11-01; execution has not started.

**Approval:** The operator explicitly approved both reviewed #4/#5 plans with “approve both” in this conversation, after the review corrections and passing draft review. Execution method has not been selected. Publication, integration and closure retain their separate authority gates.

**Planning refresh:** 2026-11-01, standalone `main` at `d557b27452ba5fb60188f06c1736c8cdc8ce9d53`. Complete native intake during planning confirmed #5 remained OPEN/backlog at the consumed revision below, with #2/#10 CLOSED. Planning and the subsequent local approval record did not publish the plan or change GitHub state.

**Goal:** Assess and demonstrate Backplane's own native v0.1 lifecycle against the adopter contract using current graph observations and attributable accepted evidence.

**Architecture:** One dated readable assessment and structured receipt map issue-owned criteria to native GitHub state and immutable delivery/evidence identities. Existing lifecycle evidence is reused only where its inputs and scope remain applicable; missing seams receive bounded new verification.

**Tech Stack:** Direct Git/gh; Markdown/JSON; uv-managed Python 3.14 only for substantive aggregation and verification.

**Spec:** Human-approved bounded issue body at https://github.com/tvproductions/superpowers-backplane/issues/5 and `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`.

## Global Constraints

- Consumed issue `updatedAt`: `2026-09-19T14:16:55Z`; current body still describes design authority as pending. Reconcile that historical statement with completed #2 and approved contract before execution; do not silently reinterpret it as missing approval today.
- No Projects requirement, IssueOps, automated enforcement or competing local backlog authority.
- Fresh observation and historical evidence are separate. Closed issues, labels, plan checkboxes and merged commits alone do not establish satisfaction.
- Audit all open tracked issues for label cardinality; inspect the complete native release graph including closed members and all relationship pages.
- Scratch stays under ignored `.sp-bp/work/issue-5/`; no normal-profile writes, upstream changes or incidental cleanup.
- The request authorizes work on #5, not creation of remote fixtures, publication, release, closure of unrelated issues or blanket graph/body repairs. Propose newly discovered corrections with evidence.
- This planning request runs no lifecycle experiments. After plan approval, local disposable scenario probes are authorized by project policy; an actual new GitHub mutation fixture requires explicit target authorization. A local simulation alone cannot replace a mandatory native transition observation.

## Acceptance mapping

| Issue criterion | Deliverable and verification | Owner |
| --- | --- | --- |
| Every open tracked issue has one valid lifecycle label | Exhaustive repository issue listing and full per-issue native intake; counts against the six-label vocabulary | Task 1 |
| Release hierarchy and dependencies are native | Complete #1 membership and relationship capture, reciprocal parent checks and native blockers; body prose is not the graph | Task 1 |
| One executable leaf progresses through verified completion | Chronological immutable evidence trace, preferably #11, including approved plan revision and verification preceding closure | Task 2 |
| Authority layers remain correct | Issue/spec/plan/delivery/evaluation/closure identity mapping; exact historical and fresh evidence classified separately | Tasks 1–2 |

The verification seams additionally require status/recommendation/selection with
zero mutation, authorized designing/ready/active/blocked/review/completed paths,
unrelated-label preservation and blocker/PR gates. Record each seam separately;
a criterion table without those observations is incomplete.

## Evidence inputs and receipt shape

Start with `tests/scenarios/2026-10-26-issue-11-satisfaction.md`,
`tests/scenarios/2026-10-26-issue-11-lifecycle.json`,
`tests/scenarios/2026-10-26-issue-11-status-selection.json`,
`tests/scenarios/2026-10-26-issue-11-closeout.json`,
`tests/scenarios/2026-09-19-codex-installation.md` and the dated lifecycle
records they cite. These are leads, not proof that every seam passes. In
particular, #11's later acceptance of earlier #34 tests is not a fresh #34 run.

The JSON receipt has `schema: superpowers-backplane-issue-5-self-hosting/v1`,
`observed_at`, repository/root/branch/HEAD, full `issue5` intake, spec/plan blob
IDs, `enumeration`, `issues`, `relationships`, `lifecycle_trace`, `seams`,
`criteria`, `findings`, and `gaps`. Enumeration records query, pages, cursors or
links, counts and terminal-page evidence. Relationship rows retain nodes and
reported totals. Trace rows retain event time, issue revision, before/after
state, mutation authority source when available, delivery SHA, verification
time/result and immutable evidence path/blob. Seam rows distinguish fresh
native observation, applicable historical evidence and local simulation.
Use `PASS|FAIL|UNKNOWN` for checks and `SATISFIED|UNSATISFIED|UNKNOWN` for
criteria: a known unmet mandatory check is UNSATISFIED; insufficient evidence
without a known failure is UNKNOWN. A timeline assertion requires evidence of
ordering, not just the present closed state.

## Review Focus

- Relationship connections must use `nodes` and `totalCount`, with pagination completeness proved.
- A coherent graph does not prove correctly ordered historical lifecycle transitions; use exact receipts and revisions.
- Historical tests retain original host/runtime/source identities and do not become fresh runs through rewording.
- A current label defect must be reported explicitly rather than repaired as a side effect of read-only assessment.
- Missing historical authorization or predecessor evidence remains UNKNOWN; do not infer it from a handoff assertion.

### Task 1: Capture current graph and reconcile authority

**Files:** Create `tests/scenarios/2026-11-01-issue-5-self-hosting.md` and `.json`; create disposable ledger under `.sp-bp/work/issue-5/`.

**Interfaces:** Consumes complete native intake and approved adoption contract; produces a timestamped graph/authority observation and criterion inventory.

- [ ] Establish isolated workspace and repository identity; fetch #5 with every contract-required field. Reconcile its stale pending-design sentence against completed #2 and the approved specification without changing acceptance criteria.
- [ ] Capture full native intake of parent #1, every native child, and every other open tracked issue. Verify issue-list and relationship pagination, parent reciprocity, blockers, linked closing PRs, closure reasons and `updatedAt` values. Do not substitute body task lists for native edges.
- [ ] Assert exactly one valid lifecycle label on each open tracked issue, none on closed completed release children, and unchanged unrelated labels. Record exact issue revisions and anomalous cases.
- [ ] Observe current local/remote delivery identities and distinguish direct-main integration from PR delivery; never invent a PR for #11.
- [ ] Create a criterion-to-evidence table with SATISFIED/UNSATISFIED/UNKNOWN, check-level PASS/FAIL/UNKNOWN and missing probes; leave the assessment unsatisfied/unknown where evidence does not support a result.
- [ ] Commit the independently reviewable current-state assessment and receipt with `git add tests/scenarios/2026-11-01-issue-5-self-hosting.md tests/scenarios/2026-11-01-issue-5-self-hosting.json` then `git commit -m "test: capture native self-hosting graph assessment"`. Keep historical lifecycle criteria UNKNOWN until Task 2 traces them.

### Task 2: Trace one lifecycle and close evidence gaps

**Files:** Complete the Task 1 assessment pair; create an owned Python aggregation helper only if necessary, captured with its verification evidence.

**Interfaces:** Consumes current graph plus immutable prior issue/plan/review/acceptance receipts; produces an attributable self-hosting evaluation.

- [ ] Trace a completed executable leaf (prefer #11 if its existing receipts cover all required seams): issue design/plan revisions, backlog/designing/ready/active/review/completed observations, actual integration, verification-before-close and final label cleanup.
- [ ] Separately map status/recommendation/selection zero mutation, blocked/resume, review changes, unrelated-label preservation and dependency/PR gates to exact historical installed-package test evidence. Verify relevant source hashes and explain applicability to the assessed delivery.
- [ ] Identify genuinely missing or invalidated seams. Before new remote fixture creation or issue mutation beyond #5's authorized workflow, obtain explicit authorization for exact remote targets; local scenario fixtures remain allowed under project rules. Do not rerun completed host acceptance solely because scratch is absent.
- [ ] For any new processing helper, write an assertion-level negative control for malformed/incomplete connection data and unsupported satisfaction, then implement and run it through `uv run --no-project python`. Require Ruff check/format and ty for new owned Python code.
- [ ] Verify all cited paths, blob/commit identities and criterion mappings; parse the JSON receipt, check Markdown links and run `git diff --check`.
- [ ] Report findings separately from suggested issue-body or lifecycle corrections. Integration/publication and completed closure remain separate gates requiring their applicable authority and fresh checks.
- [ ] Commit the completed evidence trace and screened supporting transcripts with an explicit reviewed path list and `git commit -m "test: assess Backplane self-hosting lifecycle evidence"`. A completed assessment may legitimately report unresolved acceptance; do not equate writing the report with completing #5.
- [ ] Run the full completion gate below against the committed candidate and obtain fresh independent review. Resolve material findings, commit any corrections and review evidence, and rerun affected checks plus the full completion gate before invoking `superpowers:finishing-a-development-branch`. Integration/publication and any resulting acceptance checkpoint follow their separate authority gates; record the integrated delivery separately from later evidence-storage commits.

## Commands and completion gate

```text
git rev-parse --show-toplevel
git remote get-url origin
git status --short --branch
gh auth status
gh label list --repo tvproductions/superpowers-backplane --limit 100
gh api --paginate --slurp 'repos/tvproductions/superpowers-backplane/issues?state=all&per_page=100'
gh issue view 5 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
uv run --no-project python -m json.tool tests/scenarios/2026-11-01-issue-5-self-hosting.json
git diff --check
```

Pass the API endpoint as one literal argument (quote it in a shell). The REST
issue listing includes pull requests: exclude entries with `pull_request` before
building the issue set. Save every page and confirm terminal pagination; listing
fields are not a substitute for the full `gh issue view` intake above. Repeat
that view command for #1, every release member (open or closed), every other open
issue and referenced external blockers. Resolve cross-repository edges using
their actual owner/repo. If any connection's `totalCount` exceeds retrieved
nodes, retrieve remaining pages using `gh api graphql` and the connection's
`pageInfo.endCursor`; persist query, cursors and results until
`pageInfo.hasNextPage` is false and counts agree. If the CLI/API cannot expose
all relationship pages, mark that edge set UNKNOWN and name the failed probe.

Expected: correct repository and auth, all six canonical label definitions,
complete enumeration and relation counts, one lifecycle label on every open
tracked issue, parseable receipt and zero whitespace errors. Collect every label
whose name starts with `backplane:`; require exactly one on each open tracked
issue, then require that label to belong to the six-value lifecycle vocabulary
in `github-issue-contract.md`. Unknown `backplane:*` labels are invalid, not
unrelated labels to ignore. Preserve labels outside that namespace.
Report unrelated-label preservation only with an actual before/after comparison.
Re-read issues at the end of capture: reconcile changed `updatedAt` values or
recapture affected rows before describing the graph as one consistent observation.

For each historical source run `git rev-parse <commit>:<path>` and compare the
recorded blob; use `git merge-base --is-ancestor <delivery> HEAD` to establish
local reachability, and `gh api repos/tvproductions/superpowers-backplane/commits/<sha>`
for the exact remote commit. Exit zero establishes only that specific check,
not runtime behavior. Inspect actual PR state where a PR was used; direct main
integration for #11/#20 must remain explicitly separate from PR delivery.

If aggregation needs a helper, define
`.sp-bp/work/issue-5/verify_self_hosting.py` with
`validate(receipt: dict[str, object]) -> list[str]` (empty means valid evidence
structure, not satisfied criteria) and an explicit-path CLI that exits nonzero
on validation errors. First write `test_verify_self_hosting.py` controls for
truncated connections, missing issue pages, zero/two lifecycle labels, an unknown
`backplane:*` label alone, a valid label plus invalid `backplane:done`, missing
authorization, verification after closure, and unsupported PASS. Include a
positive control with exactly one valid lifecycle label plus an unrelated label;
the unrelated label must be preserved and excluded from lifecycle cardinality.
Observe each
intended assertion fail before implementing its check. Then run:

```text
uv run --no-project python -m unittest discover -s .sp-bp/work/issue-5 -p test_verify_self_hosting.py -v
uv run --no-project python .sp-bp/work/issue-5/verify_self_hosting.py tests/scenarios/2026-11-01-issue-5-self-hosting.json
uv run --no-project ruff check .sp-bp/work/issue-5
uv run --no-project ruff format --check .sp-bp/work/issue-5
uv run --no-project ty check .sp-bp/work/issue-5
```

Expected: all positive/negative controls PASS, validator distinguishes invalid
structure from legitimate UNKNOWN/UNSATISFIED results, and all tool checks exit
zero. Preserve any helper source and tests used for claims under
`tests/scenarios/transcripts/2026-11-01-issue-5-*`; ignored scratch must not be
the sole supporting source. Do not add an aggregation helper if direct evidence
review suffices. Final execution gate also runs
`node --test tests/opencode-adapter.test.mjs` (all tests PASS), JSON parsing,
evidence-link/blob checks and `git diff --check`. Fresh review must address all
Review Focus items. Keep audit completion, criterion satisfaction, integration,
publication and authorized closure distinct.
