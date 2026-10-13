# Issue #31 Mac execution checkpoint

Updated: 2026-10-13; reviewed local implementation and one verified fix pass. This tracked execution summary is separate from
ignored scratch and from the product checkpoint format. It records actual Mac
implementation evidence, not recovered Windows completion.
The storage commit is the commit containing this file and its evidence; it is
not embedded in its own contents. Local commit acceptance and remote transport
remain distinct.

## Authority and inputs

- Work item: https://github.com/tvproductions/superpowers-backplane/issues/31
- Observed issue revision: `2026-10-12T01:29:48Z`; OPEN/Feature,
  exactly `backplane:active`, no native parent/children/blockers/closing PRs.
- Approved plan: `2026-10-11-github-governance-bridges-implementation.md`,
  SHA-256 `ae05361badc5be68474b4fc5ea19de01f806b31e245c5f9e88be99e1da3e72f1`.
- Approved specification: `../specs/2026-10-11-fdau-github-governance-design.md`,
  SHA-256 `677bcc5ce2707781f0ee05c15306bd1be0587a801ca48699fba195722681bdb0`.
- Frozen probe contract: `2026-10-11-governance-probe-contract.md`, version
  `governance-probes/v1`, SHA-256
  `fc23cbae20160535f0836eff9920649c0dc78fe50b17ac3082904f2b38710f81`.
- The original approved files remain unchanged. The prior recovery assessment
  records their published Git identities and the known Windows continuity gap.
- Current operator direction: "do 31" — execute the approved implementation on this Mac through verification and fresh review.
  The October 11 native-inline execution and protected-namespace exceptions
  remain in AGENTS.md; this record does not authorize publication or release.

## Actual Mac isolation identity

- Source repository: `/Users/jeff/Documents/Code/superpowers-backplane`.
- Native creation operation: `e4300ecb-c9ae-4e9b-ae44-3f7828c1e4fa`.
- Exact returned workspace:
  `/Users/jeff/.codex/worktrees/d181/superpowers-backplane`.
- Shared Git directory:
  `/Users/jeff/Documents/Code/superpowers-backplane/.git`.
- Starting HEAD: `82fa208cd81b1ae33a6b24e869220f90c9558312`.
- Branch state: detached HEAD, managed by the native harness.
- Root, registration, shared directory, clean starting state, and detached
  identity were independently verified before workspace mutations. The identity
  was first recorded in an external provisional ledger, then copied into the
  ignored workspace after its ignore rule was established.
- Root remains on `main`; the native worktree is retained for further work.
  A Mac path is not an alias for the unavailable Windows worktree.

Upstream is the separate development checkout at the source root's
`.agents/superpowers`, authoritative origin `obra/superpowers`, stable v7.0.0,
commit `bb92a77741419a4ab5f06e711a283343f1ada0c3`. The worktree's ignored
`.agents/superpowers` link adopts that existing source; local Backplane links
resolve to this worktree's own `skills/` tree. No upstream file is modified.

## Evidence and task disposition

[Mac setup evidence](../../../tests/scenarios/2026-10-12-mac-superpowers-v7.0.0-setup.md)
contains all five existing conformance results and fresh discovery. The five
complete captured responses are tracked with it. This is evaluated setup
behavior, not the new governance baseline or task completion.

| Task | Current disposition | Required next evidence |
| --- | --- | --- |
| 1: Negative controls and doctrine | verified at 30e25191d8a69c3fe371d6e603d1fc646d904c62 | Frozen baseline64 scored; doctrine and immutable input identities retained |
| 2: Product planning/intake bridge | verified at e4e63a40a6fe99c8e4a1cbd016b89e698b69c1e8 | Fresh cases1–4 pass27; final cases retained |
| 3: PR closeout bridge | verified at 2518eb2df8b67af12c6ee2750aded9227932cf56 | Fresh cases5/2 pass16; final cases retained |
| 4: Product checkpoint contract | verified at 423eb83, revalidated after review correction | Original18 plus5 native-edge outcomes pass23; all frozen behavioral cases and earlier12 file/Git outcomes remain scoped and retained |
| 5: Review and finishing | local implementation, regression and fresh review verified; finishing decision pending | Latest common-bundle64 governance/freshness +23 existing statements, five conformance checks; two format findings fixed, one Minor deferred |

No prior Windows result is promoted to verified. Its execution ledger and
implementation state remain unavailable. The earlier fixture receipt remains
fixture evidence only; it does not prove a live checkpoint commit or Task 1.
The preceding table records only independently substantiated Mac work; no
Windows task or implementation commit is promoted to verified.

## Portable execution procedure

This issue-specific correction uses the existing handoff approach and leaves
scratch under ignored `.sp-bp/work/`. At an interruption or machine/harness
handoff, preserve a tracked execution summary together with the evidence needed
to support every claimed verified task. Record plan/spec/probe and issue
revisions, actual workspace identity, input and evidence digests, implementation
commit identities where present, unresolved findings, and the first unsupported
task. An evidence pointer to ignored machine-local scratch is unavailable to
another host and cannot alone support a portable verified claim.

A local checkpoint is durable in Git only after its summary and necessary
supporting evidence are committed together. Before claiming another host can
resume, transport that commit through an authorized operation and verify arrival.
Do not confuse a proposed commit, uncommitted file, local accepted commit, and
remotely integrated checkpoint. Keep the source/verification identity separate
from the later checkpoint storage commit.

On another host, use current instructions, Git/GitHub state, artifact hashes,
and transported evidence to reconcile this summary. A path, branch, approval,
or result does not become current merely because it appears here. Missing or
changed inputs require revalidation; an unreadable predecessor stays unknown.
Never copy scratch into upstream or write to `.superpowers/`.

## Start here

The evaluated Mac setup and implementation checks pass. Recheck the exact
worktree identity, live issue/artifact revisions, final source hashes and captured
evidence. The remaining gate is the operator's concrete finishing decision: push a new
branch and create the prepared PR, or keep the native workspace as-is. Do not repeat verified tasks solely because the
prior Windows ledger was unavailable. The old plan's
historical Windows preservation and unpublished-artifact statements are drifted;
the approved design, task order, immutable probes, review, and verification
contracts remain binding. Use native bookkeeping under the recorded exception.

## Current Mac verification and review inputs

- Implementation starts at 33068051537dccfaeb6a6dbb82f5b293e9489203 after
  independently authorized setup commits. No prerequisite result is presented
  as governance implementation evidence.
- [Governance evidence](../../../tests/scenarios/2026-10-11-github-governance-bridges.md)
  links every captured result. The run manifest preserves immutable original
  prompts/rubrics, baseline findings, task candidates, candidate1 freshness R7
  UNKNOWN, and the final corrected common-bundle64 PASS. The final doctrine
  SHA-256 is 176ef7f079762e3cde482952ba37315d2e1693f94d03f2090764e628aa461827.
- [Existing conformance evidence](../../../tests/scenarios/2026-10-13-governance-regression-runs.json)
  retains exact mapped prompts and all23 scored expectations, plus both parsed
  frontmatters and direct-link checks. All five named conformance checks pass.
- [Execution ledger](../../../tests/scenarios/2026-10-13-issue-31-execution-ledger.md)
  carries native task order, inputs, rulings, verification and unresolved review
  gates. Supporting captures are tracked; scratch is not the sole resume source.
- Invented pair K0 b32f6473161ff199234a4011bad4ac6b5c13e1dc and K1
  32d9284af6c3188981c2883b91a9bc8400331f16 prove the exercised file/index/tree
  boundary only. No actual .sp-bp product pair, full live graph/Project capture,
  remote integration, another-host arrival or release is established.
- Issue31 is still OPEN/Feature/backplane:active with unchanged native revision
  2026-10-12T01:29:48Z. No PR is submitted; no lifecycle, body or relationship
  mutation occurred. Review/publish/integration/verification/closure stay distinct.
- Root and upstream preservation checks pass; the root's previously recorded
  dirty setup files remain preserved. The upstream source remains clean and
  protected paths remain absent. Retain the native workspace for PR feedback.

## Reviewed local delivery and next action

The fresh reviewer evaluated 82fa208..1fd90dffd2de585520677c414d8e99b29b55dc41.
[Review and disposition](../../../tests/scenarios/2026-10-13-issue-31-whole-change-review.md)
records all findings and declined judgments. Two representation findings were
regraded Important and fixed in one observed RED→GREEN pass. The separately
frozen native-edge contract preserves its exact pre-change source observations;
current format examples and candidate projections pass23 outcomes. Current
post-review-fix arms in both behavioral manifests pass64 and23 statements.
Earlier final-candidate records retain their historical source identities.

Deferred Minor: the disposable validator is not a general production engine;
complete Project paging and unavailable-body enforcement remain coverage gaps.
Operational capture guards are still mandatory. No general runtime is shipped.
The documented local evidence is sufficient for this skills-only slice, not a
live capture, production recovery, bundle/other-harness or integrated satisfaction
claim. The optional reviewer live query was blocked; local review completed.

[Prepared PR handoff](2026-10-13-issue-31-pr-handoff.md) names the issue, approved
authorities, D1–D8 contributions, current verification, scope limits and neutral
Refs #31. The native workspace remains detached and preserved; root main and
its12 protected dirty-file hashes and all238 upstream file hashes are unchanged.
Ignore scratch; the tracked ledger/captures/review carry the needed resume record.
A clean local Git export already validated portable evidence; remote transport
and another host's arrival have not occurred and must be verified separately.

No PR has been submitted. Issue31 remains OPEN/backplane:active at unchanged
2026-10-12T01:29:48Z in the final full native intake. The operator must select
push-as-new-branch/PR or keep-as-is under finishing. Subsequent integration needs
fresh target verification and separate authorized satisfaction/closure; no release
is part of this work. Do not repeat verified implementation tasks on resume
unless their actual authority/input/source identities changed.

Final reviewed implementation/fix commit: 64df352 (resolve the full object through
Git). A clean local export of that commit reproduces all52 recorded response
identities and the latest source bundle, review, ledger and prepared PR handoff,
without ignored scratch. Later storage of this export receipt changes no tested
skill/reference/fixture source. Remote transport/arrival remains unverified.
