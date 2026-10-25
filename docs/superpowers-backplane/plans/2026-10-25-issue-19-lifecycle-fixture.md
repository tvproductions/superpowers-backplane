# Claude Guide Source Verification Fixture Plan

> Execute inline under the already approved issue #19 recovery plan, Task 4.
> Native bookkeeping stays under ignored `.sp-bp/work/issue-19/`.

**Goal:** Integrate one useful guide clarification while observing #34's real
native lifecycle, preservation and verified closure.

**Issue:** https://github.com/tvproductions/superpowers-backplane/issues/34

**Consumed issue revision:** `2026-10-25T16:50:27Z`.

**Design authority:** The exact bounded issue body and paragraph approved by the
operator's `yes` after the explicit fixture-creation/lifecycle request. The
approved #19 recovery plan's Task 4 prescribes this work; this fixture plan binds
that already approved task to its actual issue, rather than adding new scope.

**Architecture:** One paragraph and this plan, on a branch from verified remote
main, in the authorized standalone root. Native GitHub state supplies observed
lifecycle evidence; local intentions and dry runs never count as transitions.

**Tools:** gh for GitHub; Git for local guarded branch/file history. Python via
uv for portable orchestration, Ruff and ty for Python checks. The existing four
guide PowerShell blocks are parsed through an explicitly scoped adapter only;
they are not re-executed or a new portability requirement for Backplane.

## Constraints and verification

- Root must be exactly `U:/repos/agents/superpowers-backplane` before each Git
  mutation. Do not mutate another checkout or upstream installation.
- Branch: `test/issue-19-doc-lifecycle`, from the freshly verified published
  main commit. Refuse a collision. Preserve the #19 recovery branch.
- Allowed files: `docs/installing-claude-code.md` and
  `docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md` only.
- Keep every existing guide block unchanged; add only the approved source/update
  verification heading and paragraph next to the local-directory explanation.
- Preserve `documentation` and exactly one Backplane label while open. Keep
  native parent/dependency relationships unchanged. No #19/#11 closure.
- Use full issue fields from the native issue contract before and after every
  mutation; compare body, relationships and unrelated labels. Reconcile every
  timestamp change against the consumed revision before execution.
- Verify the exact guide paragraph and plan against their committed blobs.
  Run `git diff --check`; parse all four unchanged PowerShell blocks using
  PowerShell's parser, driven by Python with argument arrays and UTF-8.
- Consistency evidence: B `b0d702f8821d6d29184118410ec6ff2d8fb63438`,
  F `5e01704fcdda13eefeeac52d8892da26e7164ffd`, and the retained #19 Python
  lifecycle replay receipt and transcript.
- Publication/integration require the separately presented operator approval.
  A PR uses `Refs #34`, never automatic closing intent. Close only after actual
  integration, exact-byte arrival and fresh verification. Retain evidence and
  fixture source branches until separately authorized cleanup; no tag/release.

## Steps

1. Observe status and selection with zero mutation, then move backlog→designing
   when this plan is bound. Reconcile the issue's current semantics with the
   approved body and record artifact availability honestly.
2. Review this bound plan, approve no new scope, move designing→ready only when
   every leaf gate holds, then ready→active as the paragraph work starts.
3. In the same root, create the guarded fixture branch from verified main. Add
   exactly the approved paragraph plus this plan. Run the checks above and commit
   only these two files.
4. Obtain a fresh read-only review of the useful contribution. Use only actual
   findings for the requested-change scenario; never manufacture a correction.
   Transition active→review only when the worktree/review evidence supports it;
   return review→active if a real review correction requires work, then reverify.
5. If a real impediment stops progress, record `Resume target: backplane:active`
   and its concrete release condition before active→blocked. Publication approval
   is currently separate; do not publish merely to avoid a blocker. After actual
   release of the impediment, revalidate all active-entry gates before resumption.
6. Present the exact reviewed contribution and integration commands for operator
   approval. After authorized PR publication/integration, verify the actual target
   guide/plan blobs and parsing again, then close completed with only the unrelated
   documentation label retained.
7. Preserve all full native snapshots, actual Claude tool calls and unedited
   responses in #19's tracked evidence. Switch back to the recovery branch and
   incorporate the verified fixture integration only after authorization.

## Review focus

- Recording an installed version/hash must not be mistaken for comparison with
  the selected immutable source.
- The paragraph must require actual post-restart skill discovery, not an
  inventory entry or model assertion alone.
- All guide code and canonical package bytes outside the two allowed files stay
  unchanged. A source transport correction is not a new installed identity.
- Missing review change, missing authorization or unavailable integration is
  UNKNOWN/pending, not a fabricated successful lifecycle row.

## Review and authority record

This is the mechanical issue binding of the operator-approved Task 4 and exact
fixture body/paragraph. The operator authorized creation and exercise in this
session; scope and observable acceptance match that approval. Publication and
integration are explicitly excluded until separately approved. The executor's
preflight checked every acceptance criterion and verification seam against the
steps above; no new architectural decision or extra package/runtime is added.
