# Issue #4 License and Adopter Operations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; implementation has not started.

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

## Review Focus

- GitHub license recognition is a hosted observation; a local file match cannot satisfy that criterion.
- README support statements must retain host/revision/platform limits from accepted evidence.
- Guide commands may write outside the apparent cwd; replay only in contained child-scoped profiles.
- Rollback must restore exact prior source while preserving unrelated plugins; require operation-specific evidence.
- Current governance proposes Projects but allows explicit Issues-only operation; documentation must distinguish optional presentation from authoritative native issues.

### Task 1: License and support documentation

**Files:** Create `LICENSE`, `docs/adopter-operations.md`; modify `README.md`; create `tests/scenarios/2026-11-01-issue-4-license-and-operations.md` and `.json`.

**Interfaces:** Consumes MIT selection and accepted Codex/Claude evidence; produces a coherent adopter entry point and a command/evidence inventory.

- [ ] Establish isolated workspace identity and fresh complete #4 intake; reconcile unchanged issue semantics and preserve unrelated labels in authorized designing transition.
- [ ] Inspect repository ownership and existing notices; resolve an ambiguous copyright holder with the operator. Add standard MIT text with the supported year and holder.
- [ ] Build a command inventory from `docs/installing-codex.md` and `docs/installing-claude-code.md`, retaining install, setup, update, rollback, uninstall, troubleshooting and authorization prerequisites. Include the OpenCode guide only to its verified scope.
- [ ] Write operations guidance linking host-owned commands, immutable source selection, separate upstream maintenance, safe failure recovery and issue-mutation authorization. Update README quick start and supported/pending/out-of-scope statements against exact accepted evidence.
- [ ] Check that every link resolves, no pending host operation is represented as verified, and the local license matches the standard MIT text apart from the copyright line. Run `git diff --check`.

### Task 2: Replay and recognition acceptance

**Files:** Complete the Task 1 evidence pair; change host guides only for demonstrated command defects within #4 scope.

**Interfaces:** Consumes command inventory and protected fixtures; produces criterion-level PASS/FAIL/UNKNOWN results.

- [ ] Canonically verify contained fixture/profile paths, independently identifiable upstream and authenticated host prerequisites. Never copy credentials or use normal-profile fallback.
- [ ] Execute every claimed supported command path in clean adoption fixtures using immutable source refs. Capture native host identity, exact commands, installed skill identities and immediate protected-state comparisons. Record unavailable paths UNKNOWN and leave acceptance incomplete.
- [ ] If guide corrections change behavior, use an assertion/scenario negative control before the correction and rerun the affected installed seam; preserve historical captures unchanged.
- [ ] Run document-link and whitespace checks plus applicable guide compilation/parsing and owned-helper Ruff/format/ty checks. Obtain fresh review and finish the branch after material findings are resolved.
- [ ] After separately authorized publication, run `gh repo view tvproductions/superpowers-backplane --json licenseInfo` and verify MIT recognition against the published source. Before publication this criterion remains UNKNOWN, not locally satisfied.
- [ ] Map every criterion to exact evidence. Do not close #4 without accepted integration, fresh verification, hosted recognition and closure authority.
