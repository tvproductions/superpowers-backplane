# Issue #4 License and Adopter Operations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Approved by the operator on 2026-11-01; implementation has not started.

**Approval:** The operator explicitly approved both reviewed #4/#5 plans with “approve both” in this conversation, after the review corrections and passing draft review. Execution method has not been selected. Publication, integration and closure retain their separate authority gates.

**Planning refresh:** 2026-11-01, standalone `main` at `d557b27452ba5fb60188f06c1736c8cdc8ce9d53`. Complete native intake during planning confirmed #4 remained OPEN/backlog at the consumed revision below. Planning and the subsequent local approval record did not publish the plan or change GitHub state.

**Goal:** Add the operator-selected MIT license and accurate, verified adopter operations guidance.

**Architecture:** Root license and README provide legal identity and entry points; host guides retain native command ownership. A compact operations document links those guides and distinguishes verified support from pending work.

**Tech Stack:** Markdown, Git/gh, native host commands; uv-managed Python 3.14 for any substantive verification processing.

**Spec:** Human-approved issue body at https://github.com/tvproductions/superpowers-backplane/issues/4 plus `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`. The operator explicitly selected MIT in this conversation on 2026-11-01.

## Global Constraints

- Consumed issue `updatedAt`: `2026-08-23T13:55:22Z`; reconcile full intake before execution and mutations.
- MIT is selected; confirm copyright holder from authoritative repository/operator identity, without inventing legal ownership or adding a contributor assignment requirement.
- Preserve independent Superpowers ownership. No copied upstream license standing in for Backplane's license.
- No consumer runtime, required GitHub Projects, IssueOps, unverified host support, or publication/release authority.
- Fixtures/profiles/ledgers remain under ignored `.sp-bp/work/issue-4/`; normal profiles, installed caches, unrelated worktrees and upstream remain protected.
- #20 smoke evidence cannot establish OpenCode setup, update, rollback or uninstall acceptance. Full OpenCode adopter operations remain pending #21–#24/#12.
- Do not close #4 merely by omitting pending commands. If its adopter-operations criterion requires still-unverified OpenCode paths, report that acceptance gap and wait for the owning host evidence; do not invent a dependency edge or reduce the criterion.

## Acceptance mapping

| Issue criterion | Deliverable and verification | Owner |
| --- | --- | --- |
| GitHub recognizes the approved license | Standard root MIT license; hosted `licenseInfo.spdxId` equals `MIT` after authorized publication | Tasks 1–2 |
| README distinguishes supported, experimental and out-of-scope surfaces | Evidence-bound host table: accepted Codex and Claude scope, OpenCode initial smoke only, other harnesses outside v0.1 | Task 1 |
| Adopter setup, update, rollback and removal need no undocumented maintainer knowledge | Exhaustive guide-block inventory, exact replay and recovery results; unavailable mandatory paths prevent satisfaction | Task 2 |
| Projects and IssueOps are not required; no project runtime imposed | Explicit statements in README and operations guide, consistent with optional governance presentation and host-owned runtimes | Task 1 |

## Execution inputs and evidence shape

Read `docs/installing-codex.md`, `docs/installing-claude-code.md`,
`docs/installing-opencode.md`, the approved adoption specification and
`skills/managing-superpowers-backlog/references/installing-superpowers.md`.
Use `tests/scenarios/2026-09-19-codex-installation.md`,
`tests/scenarios/2026-10-26-issue-11-satisfaction.md` and
`tests/scenarios/2026-11-01-issue-20-satisfaction.md` as bounded historical
inputs, retaining their exact tested revisions rather than treating them as new runs.

The Task 1 JSON receipt has `schema: superpowers-backplane-issue-4-operations/v1`,
`observed_at`, repository/root/branch/HEAD, full `issue` intake, approved spec/plan
blob IDs, selected license and its attribution, `commands`, `criteria`, `checks`,
and `gaps`. Each command row has a stable `id` (`codex-install-01`, for example),
host/version/platform, guide path and blob/hash, heading and block ordinal,
literal command or session request, substitutions, source SHA, isolated profile
identity, prerequisites, expected outcome, actual exit/output evidence pointer,
before/after preservation pointers, and `PASS|FAIL|UNKNOWN`.
Inventory interactive session requests and recovery branches as well as shell
blocks. An intentionally unavailable operation stays present with its recovery
condition. Criterion results use `SATISFIED|UNSATISFIED|UNKNOWN`, with supporting
row IDs; any known failed mandatory row is UNSATISFIED, otherwise a missing
mandatory result is UNKNOWN. Evidence pairs contain no credentials or raw auth stores.

## Review Focus

- GitHub license recognition is a hosted observation; a local file match cannot satisfy that criterion.
- README support statements must retain host/revision/platform limits from accepted evidence.
- Guide commands may write outside the apparent cwd; replay only in contained child-scoped profiles.
- Rollback must restore exact prior source while preserving unrelated plugins; require operation-specific evidence.
- Current governance proposes Projects but allows explicit Issues-only operation; documentation must distinguish optional presentation from authoritative native issues.

### Task 1: License and support documentation

**Files:** Create `LICENSE`, `docs/adopter-operations.md`; modify `README.md`; create `tests/scenarios/2026-11-01-issue-4-license-and-operations.md` and `.json`.

**Interfaces:** Consumes MIT selection and accepted Codex/Claude evidence; produces a coherent adopter entry point and a command/evidence inventory.

- [ ] Establish isolated workspace identity and fresh complete #4 intake using the command below; reconcile unchanged issue semantics. At execution entry, validate approved design/plan and lifecycle gates before the authorized transition; preserve unrelated labels. Planning alone is not implementation.
- [ ] Inspect repository ownership and existing notices; resolve an ambiguous copyright holder with the operator. Add standard MIT text with the supported year and holder.
- [ ] Build a command inventory from `docs/installing-codex.md` and `docs/installing-claude-code.md`, retaining install, setup, update, rollback, uninstall, troubleshooting and authorization prerequisites. Include the OpenCode guide only to its verified scope.
- [ ] Write operations guidance linking host-owned commands, immutable source selection, separate upstream maintenance, safe failure recovery and issue-mutation authorization. Update README quick start and supported/pending/out-of-scope statements against exact accepted evidence.
- [ ] Check that every link resolves, no pending host operation is represented as verified, and the local license matches the standard MIT text apart from the copyright line. Run `git diff --check`.
- [ ] Commit the independently reviewable documents and initial evidence with `git add LICENSE README.md docs/adopter-operations.md tests/scenarios/2026-11-01-issue-4-license-and-operations.md tests/scenarios/2026-11-01-issue-4-license-and-operations.json` then `git commit -m "docs: add MIT license and adopter operations guidance"`. Record the commit in the owned ledger; this is not publication.

### Task 2: Replay and recognition acceptance

**Files:** Complete the Task 1 evidence pair; change host guides only for demonstrated command defects within #4 scope.

**Interfaces:** Consumes command inventory and protected fixtures; produces criterion-level PASS/FAIL/UNKNOWN results.

- [ ] Canonically verify contained fixture/profile paths, independently identifiable upstream and authenticated host prerequisites. Never copy credentials or use normal-profile fallback.
- [ ] Execute every claimed supported command path in clean adoption fixtures using immutable source refs. Capture native host identity, exact commands, installed skill identities and immediate protected-state comparisons. Record unavailable paths UNKNOWN and leave acceptance incomplete.
- [ ] If guide corrections change behavior, use an assertion/scenario negative control before the correction and rerun the affected installed seam; preserve historical captures unchanged.
- [ ] Run document-link and whitespace checks plus applicable guide compilation/parsing and owned-helper Ruff/format/ty checks. Map every criterion to available local evidence; retain hosted recognition and unavailable host acceptance as UNKNOWN.
- [ ] Commit final replay evidence and any demonstrated guide corrections using an explicit reviewed path list and `git commit -m "test: record adopter operations command replay"`. Retain incomplete hosted/host acceptance as UNKNOWN until its gate actually passes.
- [ ] Run the full completion gate below against the committed candidate and obtain fresh independent review. Resolve material findings, commit any corrections and review evidence, and rerun affected checks plus the full completion gate before invoking `superpowers:finishing-a-development-branch`. Finish only the fully committed, verified local candidate; hosted recognition remains a later checkpoint.
- [ ] After separately authorized integration/publication, run `gh repo view tvproductions/superpowers-backplane --json licenseInfo` and verify MIT recognition and exact published license bytes. Record the tested delivery separately from this later evidence-storage commit; rerun affected checks on the integrated target.
- [ ] Update criterion mappings with actual hosted results and commit the acceptance checkpoint separately using an explicit reviewed path list. Do not close #4 without accepted integration, fresh verification, hosted recognition and closure authority; absent authority or evidence leaves this checkpoint pending.

## Commands and completion gate

Run from the verified project root; record exit codes and relevant output.

```text
git rev-parse --show-toplevel
git remote get-url origin
git status --short --branch
gh auth status
gh issue view 4 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue edit --help
gh issue close --help
uv run --no-project python -m json.tool tests/scenarios/2026-11-01-issue-4-license-and-operations.json
git diff --check
```

Expected: exact standalone root or verified registered worktree, expected origin,
authenticated gh, complete native fields and supported lifecycle flags, parseable
receipt and no whitespace errors. Review the parsed receipt for a one-to-one
inventory of all guide blocks/requests and exact criterion coverage; valid JSON
alone proves neither. Parse PowerShell blocks with
`System.Management.Automation.Language.Parser.ParseInput` and require zero
parser errors; compile Python blocks with `compile(source, filename, 'exec')`
through the prescribed uv interpreter. Preserve the parsing script and output
under `tests/scenarios/transcripts/2026-11-01-issue-4-*` if used as evidence.
Parsing does not replace actual native command replay.

For new owned Python helpers only, use assertion-level negative controls before
implementation, then run `uv run --no-project ruff check` and
`uv run --no-project ruff format --check` and `uv run --no-project ty check`,
each with the explicit helper paths. No helper is required for prose alone.
Run the repository's `node --test tests/opencode-adapter.test.mjs` as the existing
package regression check at execution's final quality gate; expect all tests PASS.

After separately authorized publication only:

```text
gh repo view tvproductions/superpowers-backplane --json licenseInfo
```

Expected: `licenseInfo.spdxId` is `MIT`; verify published `LICENSE` bytes match
the reviewed local file. A missing result remains UNKNOWN. Review must cover
every Review Focus item against the inventory and actual replay, including
failed-candidate restoration and unrelated-plugin preservation. Report local
checks, integration, hosted recognition and issue satisfaction separately.
