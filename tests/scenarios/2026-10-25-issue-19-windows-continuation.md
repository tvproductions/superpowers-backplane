# Issue 19 Windows continuation

## Authority and reconciliation

The operator requested continuation of #19 on 2026-10-25. This executes the
approved recovery plan at `docs/superpowers-backplane/plans/2026-10-24-issue-19-claude-lifecycle-recovery.md`;
it does not replace its scope or acceptance criteria. Historical Mac evidence
remains at its original identity.

Current root: `U:/repos/agents/superpowers-backplane`; current branch:
`recovery/issue-19-windows`, based on published recovery commit
`742392c`. Git reports this exact standalone root. The operator's current
AGENTS instructions authorize this root; no other worktree is mutated.

Live #19 remains OPEN/designing at revision `2026-10-25T15:23:39Z`, parent #1,
closed blocker #18, blocking #11, no children or closing PRs. The publication
paragraph is editorial reconciliation; objective, acceptance and graph match
the approved recovery plan. Baseline B is
`b0d702f8821d6d29184118410ec6ff2d8fb63438`; published fixture F is
`5e01704fcdda13eefeeac52d8892da26e7164ffd`. F is reused without rebuilding,
merging, tagging, or republishing fixture bytes.

## Current prerequisite observations

- Claude Code: 2.1.302. PowerShell: 7.6.7.
- Selected disposable profile: `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile`.
  First probe was unauthenticated; after operator login a fresh probe reported
  `loggedIn: true`, `authMethod: claude.ai`. No credential was copied or printed.
  Initial plugin and marketplace inventories were empty arrays.
- Previous #17/#18 disposable profiles exist but report unauthenticated and
  empty inventories; they are not used for this continuation.
- The B-pinned hosted-source catalog passed strict validation. All four
  existing guide PowerShell blocks parse with zero errors; none of the old
  checkout/bootstrap blocks was executed.
- RED observation: the guide still marks pinned update, rollback and uninstall
  pending #19. No new lifecycle outcome is claimed by preparation.
- Current primary documentation confirms `github` plugin sources accept a
  full 40-character `sha`, separately from marketplace location:
  <https://code.claude.com/docs/en/plugins/marketplace-reference>.
  CLI help confirms named marketplace refresh and restart after plugin update.

## Execution rulings

1. Substitute the currently authorized Windows root and a new continuation
   branch for the Mac-only paths in the recovery plan. Preserve all B/F
   identities and task order. Cost if wrong: evidence remains host-specific
   and cannot establish another machine's results.
2. Use native bookkeeping under ignored `.sp-bp/work/issue-19/`, as the approved
   recovery plan requires. No upstream bookkeeping helper or reserved namespace
   is written. Cost if wrong: bookkeeping must be reconciled before acceptance.
3. Keep this repository's existing independently managed Superpowers v7.0.0
   at `bb92a77741419a4ab5f06e711a283343f1ada0c3` unchanged. Verify that exact
   source as the Windows test input; do not import Mac v7.0.1 claims or perform
   an implicit upstream update. Cost if wrong: affected compatibility rows must
   be rerun against the intended upstream input.

## Pre-flight interfaces

| Producer → consumer | Shared evidence | Gate |
|---|---|---|
| Task 1 → Tasks 2–4 | authenticated B, source identity, preservation inventory | no old install observation substitutes for B |
| Task 2 → Task 3 | installed F and unchanged B availability | no version-only update claim |
| Task 3 → Task 4 | restored B and direct fresh skill loads | installed source must match B |
| Tasks 1–4 → Task 5 | complete scored evidence and distinct contribution identities | mandatory FAIL/UNKNOWN blocks submission |

## Execution updates

The isolated profile installed B through the pinned GitHub-source catalog and
separately registered the existing upstream source through its own marketplace.
The baseline snapshot verifies 21 exact Git blob identities, the independent
upstream registry/source/files, normal-profile configuration hashes, the user
sentinel, Git refs and complete #19 JSON. The synced unrelated
`cowork-plugin-management@synced` v0.2.2 identity was present at that snapshot
and remained unchanged in every later recorded inventory.

Fresh session `3e007b9a-a75a-4c62-8ba4-b646f8bdacfc` invoked all three actual
Skill tools. Upstream loaded from `.agents/superpowers`; Backplane loaded from
the profile's fetched B package. Repeat-install session
`cbc61499-57eb-4e38-acd4-cf850cf68e15` loaded the same three skills.

After the baseline gates, authorized readiness and active transitions were
verified at `2026-10-25T16:21:32Z` and `2026-10-25T16:21:35Z`. Full final intake
and native label events were captured. The first guard refused mutation because
PowerShell converted ISO revision text to DateTime; an exact-string parse fixed
that guard. Attempted per-transition snapshot filenames containing `:` were
invalid on Windows and were not saved; no missing file is claimed as evidence.

The first native update failed while cloning via SSH (`Permission denied
(publickey)`). Immediate snapshot confirmed B and all protected inputs intact.
A child-only Git URL rewrite to HTTPS corrected transport without changing the
hosted source, persistent Git configuration or credentials. The corrected update
reached F/0.1.1, all 21 source blobs and the README marker matched, and fresh
session `7f0a9382-cd7a-4cd7-b6f4-b6d53a6ecd89` loaded all three skills.
Rollback restored B and discovery in session
`ac0f054a-7500-46dd-b813-d267d5ddc011`.

An intermediate PowerShell guide replay observed repeat/update/rollback,
unavailable-source rejection, uninstall and restoration with preservation.
That uncommitted intermediate guide is superseded by the Python correction
below; its results are Windows-only historical observations, not proof of the
final guide's exact bytes.

## Operator-directed portability correction

The operator explicitly required Python for cross-platform compatibility and
strict, thorough Astral tooling. `AGENTS.md` now records `uv`, Ruff, `ty` and
portable orchestration while retaining consuming-project language neutrality
and the repository's prohibition on pytest. This is separately requested policy
work, not an inferred expansion of #19's package contract.

Ruling: replace the temporary PowerShell orchestration and newly authored
lifecycle-guide code with Python, following this current operator direction.
Preserve historical observations without inferring cross-platform acceptance.
The four pre-existing setup PowerShell blocks belong to #17/#18 and remain
unchanged; the new lifecycle section uses Python. Cost if wrong: affected guide
commands and portability seams must be rerun before acceptance.

Python is executed through `uv` (observed interpreter 3.13.14 for the test
invocation). Four regression checks first failed at assertion level, then passed:
Unicode/space paths and child-scoped environment, key-order-independent
preservation that still rejects changed values, exact installed bytes including
CRLF mismatch, and rejection of a moving source ref. Ruff and `ty` passed on
the replacement helpers. Only Windows execution is observed; macOS/Linux live
runs remain unobserved.

## Final Python replay

All nine exact Python lifecycle blocks compiled and replayed successfully through
`uv`, including B repeat-install, B→F update, F→B rollback, unavailable-source
rejection, Backplane-only uninstall and B restoration. Ten immediate snapshots
verify source bytes and protected state; five fresh Claude sessions verify actual
skill loads, including native inventory absence of Backplane after uninstall.
The profile is restored to B. The four old setup blocks were not executed again.

Durable evidence:

- `tests/scenarios/2026-10-25-issue-19-python-lifecycle.json` retains the exact
  tested guide SHA-256, B/F identities, full protected baseline, per-operation
  plugin/source identities, installed file hashes, tool calls, roots and session
  identifiers. The protected baseline includes #19's explicitly authorized
  active transition; package operations change none of its issue fields.
- `tests/scenarios/transcripts/2026-10-25-issue-19-python-lifecycle.md` retains
  the exact commands and fresh-session prompts, native observations, original
  failed SSH update and unedited final discovery responses. Repeated injected
  public skill bodies are referenced by their source identity rather than copied.
- Ruff and `ty` passed on all nine extracted Python guide blocks and the native
  Python helpers. The four portability regression checks passed under Python
  3.13.14 after observed assertion-level failures. No macOS/Linux run is inferred.

## Previous checkpoint gates (before the operator's continuation approval)

Installed-skill structure checks pass for both B skills and all nine
directly linked references. The four behavioral conformance sessions and useful
documentation issue are pending their separately requested approval. Automatic
approval review rejected the conformance sessions because scenario prompt
transmission was additional to the approved skill-text payload. No rejected
session was run. Fixture issue creation, publication, integration, final review
and closure remain unperformed. #19 is OPEN/active, not complete; #11 remains
separate. No push, merge, tag or release has been made by this continuation.

## Approved continuation: conformance and live fixture

The operator subsequently answered `yes` to running the four published Claude
conformance prompts and creating/exercising the exact prepared documentation
fixture. That resolved the earlier payload-approval blocker. The four fresh
installed-B sessions scored **23/23 original behavioral expectations PASS**;
together with the installed skill-structure inspection, all five named checks
pass in this recorded Windows scope. Full prompts, unedited responses, actual
tool calls, approved-source read digests and native preservation are retained in
`2026-10-25-issue-19-conformance.json` and its companion transcript.
The final structure probe resolves all ten relative Markdown links across both
installed skills, including the canonical governance document in addition to the
nine links into reference folders; each target digest is retained in the receipt.

The exact approved fixture body created
[issue #34](https://github.com/tvproductions/superpowers-backplane/issues/34) at
revision `2026-10-25T16:50:27Z`, with documentation/backlog labels and no native
parent or dependency edges. Its mechanically bound Task 4 plan is committed on
the same-root `test/issue-19-doc-lifecycle` branch at `33d4300`, directly based
on verified published B. The issue's artifact paragraph explicitly records local
availability and the separate publication/integration gate; no unavailable
GitHub link is presented as published evidence.

Eight fresh Claude sessions executed actual gh operations restricted to #34:

| Operation | Observed outcome |
|---|---|
| Status and selection | Full native before/after JSON identical; no invented priority |
| Backlog → designing | Design preparation recorded; unrelated documentation label preserved |
| Designing → ready | Actual local plan read; old/current timestamp semantics reconciled explicitly |
| Ready → active | Exact paragraph work began; native entry gates rechecked |
| Active → review → active | Real independent draft-review finding recorded with its actual earlier timing; requested-change return observed |
| Active → blocked | Real publication-authorization dependency recorded before the atomic label change; `Resume target: backplane:active` and explicit release condition retained |

The independent fixture reviewer identified one Important defect in the original
approved paragraph: recording hashes alone does not prove that installed content
matches the selected source. The correction now explicitly requires the installed
commit/version/hashes to match that source and makes every mismatch fail
verification. The same review seat confirms the finding resolved and no remaining
fixture findings. This focused confirmation is not the final whole-#19 review.

Local fixture delivery: `22c5b8d917a09f275c23d99bd9c9645d6c1d2e35`, tree
`13a0093f73eadbdb9abbb2db409f2b2100f5ab5e`. Its complete diff from B changes
only one guide paragraph and the issue-bound fixture plan. The four pre-existing
PowerShell examples remain byte-identical and parse with zero errors; they were
not re-executed. Corrected exact-paragraph, bounded-scope and whitespace checks
pass. The reviewer did not certify integration or final #19 acceptance.

`2026-10-25-issue-19-live-fixture.json` and its transcript retain complete native
states, actual tool calls, unedited responses, real review/correction, local
source checks and the final protected installed-B snapshot. That final snapshot
confirms all 21 installed source blobs, independent upstream files/identity,
unrelated plugins, normal-profile configuration, sentinel and full #19 state
unchanged. Only explicitly authorized local branch/commit ref changes are
accounted separately; no remote ref was changed.

## Current remaining gates

- #34 is OPEN with exactly documentation and `backplane:blocked`, revision
  `2026-10-25T17:07:58Z`. Publication/integration authorization is the concrete
  release condition. Resume and verified-completion rows remain pending.
- Exact two-file publication payload and PR body are prepared locally. Proposed
  transport is gh Git Data API, then gh PR operations. A server-created commit
  may differ from the local review history; require identical tree/blobs and
  preserve both identities before proceeding. No publication has occurred.
- After authorized fixture integration: freshly verify target bytes/parser,
  close #34 with the unrelated documentation label retained, then incorporate
  the verified fixture contribution into the recovery branch and replay affected
  final-guide seams.
- Whole-#19 review, final publication/integration, integrated verification and
  #19 closeout remain separate gates. #19 remains OPEN/active at its unchanged
  native revision `2026-10-25T16:21:35Z`; #11 remains separate.

The executor returned to `recovery/issue-19-windows` after preserving the clean
fixture branch. Native Python bookkeeping replaces the retired scratch
PowerShell helpers; they are historical inputs, not the current execution route.
No other checkout, upstream source, reserved namespace, tag or release is changed.
