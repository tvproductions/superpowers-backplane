# Issue #22 OpenCode V1 Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; not execution approval.
**Goal:** Verify V1 install/update/rollback/removal and all required conformance/lifecycle scenarios.
**Architecture:** Replay exact guide operations on an authenticated isolated native V1 installation, with per-operation source/preservation/load proofs. Keep conformance responses and real authorized issue transitions distinct.
**Tech Stack:** V1 1.18.31, Git/gh, managed Python 3.14/uv/Ruff/ty.
**Spec:** Approved adoption/rescope designs at `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` and `2026-09-19-host-installation-leaf-rescoping-design.md`; native https://github.com/tvproductions/superpowers-backplane/issues/22, consumed revision `2026-09-20T01:30:18Z`.

## Global Constraints

- Apply [the shared probe contract](2026-11-01-opencode-remaining-acceptance-probe-contract.md). #21 must be accepted/completed before readiness; V1 uses `plugin` and floor 1.18.29.
- No V2 contract change, upstream update/removal, invented rollback, unapproved production-issue experiment or release.
- Inline after approval; isolated native worktree and owned `.sp-bp/work/issue-22/`. Obtain exact remote fixture authorization before its creation/mutation.

## Review Focus

- A manager exit or local-directory edit must not prove a pinned Git-package update.
- The restored source, installed bytes and fresh loads must all match the recorded prior SHA.
- Failed candidate state must be captured before repair.
- Shared marketplaces, unrelated plugin state and upstream survive removal/recovery.
- Simulated lifecycle responses cannot substitute for mandatory authorized native transitions.

### Task 1: Verified V1 operation recipe and native replay

**Files:** Extend `docs/installing-opencode.md`; create `.sp-bp/work/issue-22/acceptance.py`, `test_acceptance.py`, ledger and tracked helper source; create the issue-22 assessment pair.
**Interfaces:** Consumes accepted #21 setup evidence and shared receipt/CLI contract; produces L-* operation rows with exact source and immediate preservation/load results.

- [ ] Re-read #22/#21 and reconcile approved plan and dependency satisfaction; verify native workspace, retained profile and source ownership.
- [ ] Write scorer controls for wrong restored SHA, missing post-operation load, removed unrelated plugin, unverified failure repair and synthetic update evidence. Observe intended failures, implement the minimal runner/recipe changes, and require controls PASS.
- [ ] Write exact V1 native configuration/command recipes for all eight L-* cases. Inspect pinned prior/candidate availability before changes and preserve a retrievable last-verified source.
- [ ] Execute each L-* case, recording before/candidate/restored SHAs, installed file blobs, fresh native skill results, failed-state snapshot and preservation. Require absence plus upstream-only availability after uninstall; restore the test fixture afterward.
- [ ] Run the shared gate and commit the operation guide/evidence slice. Missing mandatory native evidence blocks acceptance.

### Task 2: V1 conformance and authorized lifecycle

**Files:** Complete issue-22 assessment; propose the exact useful remote fixture body/title from the shared contract; retain source/captures under issue-22 transcripts.
**Interfaces:** Consumes Task 1 native installation; produces five scored named checks and actual authorized lifecycle observations for #12.

- [ ] Obtain explicit approval of the concrete V1 fixture proposal before creating it. No #34 reopening or incidental production mutation.
- [ ] Run five named checks using their existing rubrics, plus zero-mutation status/selection and all native fixture transitions in the shared contract. Record scope/revision/authority, unrelated labels, blocker/PR gates and verification-before-completion after actual integration.
- [ ] Map every exact #22 criterion/seam to native or explicitly supplementary evidence; all mandatory rows must PASS. Check whole source/graph/preservation snapshots.
- [ ] Run the full gate and fresh review; resolve material findings by controls, commit and use branch finishing. Concrete publication/integration authorization precedes hosted-target revalidation, immutable evaluation linking and authorized #22 completed closure.
