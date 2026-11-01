# Issue #23 OpenCode V2 Setup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; not execution approval.
**Goal:** Verify every supported V2 upstream setup mode and fail-closed case.
**Architecture:** Extend the shared guide with separately scored V2 native observations. Use V2's isolated global-config cwd and owned private server; retain one canonical shared adapter and root skills tree.
**Tech Stack:** V2 2.1.4, Git/gh, managed Python 3.14/uv/Ruff/ty.
**Spec:** Approved adoption/rescope designs at `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` and `2026-09-19-host-installation-leaf-rescoping-design.md`; native https://github.com/tvproductions/superpowers-backplane/issues/23, consumed revision `2026-09-20T01:30:21Z`.

## Global Constraints

- Apply [the shared probe contract](2026-11-01-opencode-remaining-acceptance-probe-contract.md). V2 floor is 2.0.4; use plural `plugins`.
- #20's accepted adapter remains the dependency; no second adapter, V1 regression, lifecycle claim, existing upstream update or unapproved remote mutation.
- Inline execution after approval; isolated native worktree for source/guide changes. Own `.sp-bp/work/issue-23/`; reuse authentication only through supported native paths.

## Review Focus

- Empty asynchronous inventory must be distinguished from completed plugin activation.
- A normal background server or ancestor discovery must not supply acceptance.
- Each of native/sibling/absent upstream modes needs its own attributable source and native loads.
- Failures preserve unrelated entries and user work before any repair.
- Actual unsupported V2 and versionless provenance must not become synthetic PASS results.

### Task 1: V2 guide and fixture controls

**Files:** Modify `docs/installing-opencode.md`; create `.sp-bp/work/issue-23/acceptance.py`, `test_acceptance.py` and ledger; archive issue-23 helper sources in tracked transcripts.
**Interfaces:** Consumes corrected tracked #20 source and shared `classify(row)`/CLI contract; produces V2-specific configuration, native event parsing and private readiness-controlled inventory.

- [ ] Reconcile full #23 intake and completed #20 evidence; establish approved plan, native worktree/shared Git identity and fixture ownership before execution.
- [ ] Write the shared scorer/environment negative controls plus empty-then-ready V2 inventory and `input.id` native-result controls. Observe failures, implement only the required V2 fixture changes, and require all controls PASS.
- [ ] Add exact V2 setup prompts, supported upstream source choices and safe recovery to the guide. Verify current primary documentation/installed help before choosing any new flag.
- [ ] Compile/parse guide blocks, run the shared quality gate and commit the independently reviewable guide/fixture slice.

### Task 2: Actual setup and failure acceptance

**Files:** Create `tests/scenarios/2026-11-01-issue-23-opencode-acceptance.md` and `.json`, with screened source/captures under the issue-23 transcript namespace.
**Interfaces:** Consumes Task 1's runner/guide; produces #23 criterion evidence and prerequisite evidence for #24/#12.

- [ ] Verify the retained authenticated V2 profile, isolated config/data/cache/temp/ProgramData roots, private loopback server and native source/model identities.
- [ ] Run all S-* and F-* setup cases in the shared contract. Require actual native Skill results and separate package identities; preserve before/after snapshots and exact failure/recovery messages.
- [ ] Run the actual below-2.0.4 native case. Keep failed fixture construction UNKNOWN; do not accept a shimmed version as native evidence.
- [ ] Map every exact current criterion and seam; require every mandatory row PASS, including no issue mutation and nontrivial unrelated-plugin preservation.
- [ ] Run the full gate and fresh review; fix material findings with controls, commit and use branch finishing. After concrete publication/integration authorization, install/verify the hosted target, publish/link SATISFIED evidence, and close #23 only under completed-closure authority.
