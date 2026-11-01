# Issue #24 OpenCode V2 Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; not execution approval.
**Goal:** Verify V2 install/update/rollback/removal and required conformance/lifecycle scenarios.
**Architecture:** Use V2's native pinned package/configuration surface with private readiness-controlled inventory and per-operation file/load/preservation proofs. Score V2 independently from V1.
**Tech Stack:** V2 2.1.4, Git/gh, managed Python 3.14/uv/Ruff/ty.
**Spec:** Approved adoption/rescope designs at `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` and `2026-09-19-host-installation-leaf-rescoping-design.md`; native https://github.com/tvproductions/superpowers-backplane/issues/24, consumed revision `2026-09-20T01:30:23Z`.

## Global Constraints

- Apply [the shared probe contract](2026-11-01-opencode-remaining-acceptance-probe-contract.md). #23 must be accepted/completed before readiness; V2 floor is 2.0.4 and configuration uses `plugins`.
- No V1 configuration change, upstream update/removal, invented rollback, unapproved remote experiment or release.
- Inline after approval; isolated native worktree and `.sp-bp/work/issue-24/`. Explicit remote-fixture approval remains required.

## Review Focus

- Poll the same owned V2 server/location; an unrelated service cannot prove activation.
- Native resolver source and installed bytes must match at each stage, not merely a cached version string.
- Configuration edits must preserve unrelated entries and source ordering where meaningful.
- Recovery must restore actual verified prior bytes and successful fresh loads.
- Only actual approved native fixture transitions satisfy the mandatory lifecycle observations.

### Task 1: Verified V2 operation recipe and native replay

**Files:** Extend `docs/installing-opencode.md`; create owned issue-24 helper/tests/ledger and `tests/scenarios/2026-11-01-issue-24-opencode-acceptance.md`/.json; archive helper sources/captures.
**Interfaces:** Consumes accepted #23 setup evidence and shared scorer/CLI contract; produces separately attributable V2 L-* operation rows.

- [ ] Reconcile full #24/#23 intake, approval, dependency evidence, registered workspace and authenticated isolated profile before execution.
- [ ] Write negative controls for asynchronous stale inventory, wrong restored SHA, missing positive load result, preservation failure and synthetic/native confusion. Observe RED, implement minimal V2-specific processing and require GREEN.
- [ ] Write and replay all eight L-* guide operations using actual pinned Git packages. Preserve prior source availability; capture exact native source/files and fresh native results after each applicable stage.
- [ ] Compare snapshots immediately, including failure-before-repair, unrelated plugin/configuration/user state, upstream and GitHub. After removal require Backplane absent/upstream present, then restore only the owned test configuration.
- [ ] Run the shared quality gate, preserve sources/evidence and commit this reviewable slice.

### Task 2: V2 conformance and authorized lifecycle

**Files:** Complete issue-24 assessment; prepare the concrete V2 useful fixture proposal; preserve issue-24 screened transcripts.
**Interfaces:** Consumes Task 1's verified installed package; produces five named checks and V2 native lifecycle evidence for #12.

- [ ] Obtain explicit approval of the exact V2 fixture proposal before creation or mutation.
- [ ] Execute five named checks and all shared-contract native read-only/selection/transition/rework/blocked/completion cases. Preserve unrelated documentation labels and verify completion only after actual accepted integration.
- [ ] Map all exact #24 criteria/seams with source/authority/host identities; every mandatory native row must PASS. Do not borrow a V1 PASS.
- [ ] Run the full gate and one fresh review, fix material findings with demonstrated controls, commit and finish the branch. Concrete publication/integration authority precedes exact hosted-target verification, immutable evaluation pointers and authorized #24 closure.
