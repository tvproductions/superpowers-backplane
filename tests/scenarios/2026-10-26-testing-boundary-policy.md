# Verification workspace policy correction

The operator identified that repository rules were preventing the testing needed
to prove Backplane. The immediate conflict was an exact-primary-root Git rule
with an alternate-workspace exception limited to issue #31. Issue #11 requires
disposable clone, dirty-checkout and provenance tests. The approved installation
design requires these checks; the old control rule obstructed them.

## Correction

`AGENTS.md` now distinguishes project source, registered project worktrees and
owned disposable verification repositories. An approved task/plan authorizes
its reversible local tests under ignored `.sp-bp/work/<task-or-plan>/`; each
fixture has a recorded canonical identity and target-specific mutation guard.
The guard rejects an unrelated root instead of rejecting every test repository.

Disposable host profiles and missing-dependency installation required by those
tests are included. Existing upstream installations and normal profiles retain
their protections. Copies made for deliberate failure tests are disposable
fixtures, not shipped installations. Local fixture clones cannot share writable
object stores or point at protected repositories through alternates.

Native bookkeeping outside the reserved upstream namespace and portable recovery
records now apply to all tasks. Future work no longer needs issue-number-specific
exceptions for these normal verification operations.

An approved local implementation plan is sufficient to begin local execution.
The earlier claim that plan publication must precede local testing was an agent
interpretation, not a requirement of the approved functional specification or
Superpowers. Publishing the branch, merging, releasing and changing production
upstream installations retain their separate authorization requirements.

The approved #11 plan/spec bytes are preserved. This correction supersedes the
old execution-boundary requests in the preparation report; they remain as dated
evidence of the original stop, not current pending approvals. #11's approved
scope, acceptance criteria and test requirements do not change.

## Observed verification

The companion JSON receipt contains the exact read-only/project and disposable
fixture commands, identity comparisons and outcomes. All eight assertions pass:

- Fixture location is ignored and canonically contained in the owned task area.
- A separate repository supports its own commit and branch.
- Deliberate dirty fixture content remains observable.
- A fixture-only lookalike origin can be staged without changing real upstream.
- The primary project root is rejected by the fixture mutation guard.
- The fixture has no object-store alternates.
- Primary project HEAD, branch and refs are unchanged by fixture operations.
- Development upstream HEAD, status and origin are unchanged.

The first adapter attempt compared stripped porcelain output with an unstripped
expected string and stopped at its assertion. The fixture was preserved. A new
unused fixture plus a corrected normalized comparison supplied the passing
receipt; no product defect or fixture-policy failure is inferred from that
orchestration error. Ruff lint and ty passed on the proof source. The first
format check after the comparison edit requested formatting; it was applied,
and the subsequent lint, format check and type check all passed. The executed
proof source is preserved in the companion transcript for reproduction, before
that final formatting-only change.

This is a local rule/proof correction, not completion of #11's live installation
matrix, a published release, or fresh whole-change review. The final #11 reviewer
must include this policy delta and its evidence.

## Shared policy source check

Reviewed starter development main `773e0d5c5b851b31c7023bdb92acc98b114647c7`
through gh on 2026-10-26: `docs/baseline-policy.md`, `docs/versioning.md` and
`CHANGELOG.md`. The receipt records reviewed input hashes; the immutable source
remains the authority. Development 0.7.0 is still unreleased. This is a scoped
check, not replacement of the October26 release-policy reconciliation at
`35ac0578dab0c7b603a9545d9b6b630ee006e551`.

Applicability: preserve independent workflow ownership, evidence-based
verification, compatible correction classification and separate publication
authority. The starter does not prescribe Backplane's old exact-root restriction
or an issue-specific test exception. No release-policy departure is introduced.
Broader Astral/tool freshness and engineering conformance remain separately scoped;
this correction changes no runtime, dependencies, release versions or support
claims. It does not adopt the starter bundle or certify full conformance.
