# Issue #21 OpenCode V1 Setup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; not execution approval.
**Goal:** Verify every supported V1 upstream setup mode and fail-closed case.
**Architecture:** Extend the existing guide and native fixture runner; root skills and the shared adapter remain canonical. Capture native results separately from scorer tests and preserve every failed/unknown observation.
**Tech Stack:** V1 1.18.31, Git/gh, managed Python 3.14/uv/Ruff/ty.
**Spec:** Approved adoption/rescope designs at `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` and `2026-09-19-host-installation-leaf-rescoping-design.md`; native https://github.com/tvproductions/superpowers-backplane/issues/21, consumed revision `2026-09-20T01:30:15Z`.

## Global Constraints

- Apply [the shared probe contract](2026-11-01-opencode-remaining-acceptance-probe-contract.md) in full. V1 floor is 1.18.29; use singular `plugin`.
- #20 must remain accepted/completed; current approval and semantic reconciliation precede readiness. No V2 adapter change, lifecycle claim, upstream update, release or unapproved remote fixture.
- Use inline execution after this plan is approved; isolated native worktree for guide/source changes. Own `.sp-bp/work/issue-21/`; retain authenticated profiles without credential transfer.

## Review Focus

- Ancestor links must not supply false installed discovery; assert effective roots.
- Native package identity must survive unknown/versionless or lookalike input; assert UNKNOWN/refusal without mutation.
- Dirty authoritative adoption and unsafe dirty update must be distinguished.
- Every failure comparison precedes repair and preserves a nontrivial unrelated plugin.
- A synthetic version response or failed fixture setup must not satisfy the actual below-floor case.

### Task 1: V1 guide and evidenced fixture controls

**Files:** Modify `docs/installing-opencode.md`; create owned `acceptance.py`, `test_acceptance.py` and ledger under `.sp-bp/work/issue-21/`; retain helper sources under `tests/scenarios/transcripts/2026-11-01-issue-21-*`.
**Interfaces:** Consumes the shared contract and corrected tracked #20 runner; produces `classify(row)`, `preflight`, `run --case` and `verify` interfaces defined there.

- [ ] Reconcile complete #21 intake and approved design/plan; verify #20's completed evidence, workspace registration and source baseline before authorized lifecycle entry.
- [ ] Write scorer/environment tests for every shared-contract negative control; run unittest and observe intended assertion failures before implementing the runner changes.
- [ ] Implement only V1 fixture/configuration support and the scorer, then require all negative/positive controls PASS. Test Windows short-cache containment and POSIX paths; no protected cache edits.
- [ ] Add exact V1 setup request, current documented upstream modes and recovery recipes to the guide; parse/compile all affected blocks and check links. Unsupported or unverified conditions stay explicit.
- [ ] Run the shared gate, retain source/output, and commit this independently reviewable guide/fixture slice with an explicit path list.

### Task 2: Actual setup and failure acceptance

**Files:** Create `tests/scenarios/2026-11-01-issue-21-opencode-acceptance.md` and `.json`; retained screened captures/sources use the issue-21 transcript namespace.
**Interfaces:** Consumes Task 1 runner/guide; produces exact criterion evidence for #21 and prerequisite evidence for #22/#12.

- [ ] Preflight the authenticated retained V1 profile, verified executable/model, separate upstream, gh capabilities and immediate protected baselines.
- [ ] Run S-native, S-sibling and S-absent plus every F-* case in the shared setup case set. Run exact guide prompts and fresh native three-skill loads for each supported mode. Keep installed-source hashes and successful tool results.
- [ ] Compare user files, unrelated plugin, upstream and complete issue snapshots immediately before/after each case. Record actual native below-floor refusal; unsupported construction remains UNKNOWN.
- [ ] Map all three exact native criteria and every verification seam. Require all mandatory cases PASS; never promote a scorer test or earlier #20 smoke into this acceptance.
- [ ] Run the full shared gate and fresh review, fix material findings by demonstrated controls, commit evidence, and use branch finishing. Publish/integrate only under concrete authorization, reverify the exact hosted delivery, then publish/link accepted evaluation and close #21 only when authorized and satisfied.
