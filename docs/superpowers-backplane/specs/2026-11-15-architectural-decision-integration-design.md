# Architectural decisions at existing Backplane checkpoints

Date: November 15, 2026. **DESIGN APPROVED; implementation-plan review pending.**
Edition: design-1. The maintainer explicitly approved both companion designs,
then required review in the main conversation. That review accepted the shared
responsibility split, checked the remote naming precedent and concluded with
“proceed with that design”. Separate actual architectural approval is captured
in [Current ADR-0001 edition 1](../../decisions/ADR-0001-001-reference-decisions-through-existing-checkpoints.md)
with the exact original bytes/response; design assent supplies no substitute.
No implemented integration, qualification or release is claimed here.

## Intent and source

Make consequential choices visible and separately approved before dependent
implementation, while allowing reuse of approved decisions and independent work.
Backplane owns this integration; gz-skills owns the portable ADR procedure and
template; Superpowers owns feature development. Keep their independent lifecycles.
Use the starter's [approved component contract](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/superpowers/specs/2026-11-08-adr-practice-design.md)
and [normative policy](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/engineering/architectural-decisions.md).
These source approvals do not approve Backplane's design or ADR.

Inspected Backplane main: `c1b63d8f72fba9996f0857120f8c97e9e8d5700d`.
Its governance, native issue contract, Superpowers binding, PR closeout and
checkpoint/v1 contracts supply the existing integration surfaces. No ADR-feature
owner issue or approved owner design was identified at intake. The November 14
paired records/commit design and November 7 release-doctrine transfer remain drafts.

## Naming precedent: remote GZKit drydock

Reviewed the remote [classic ADR change order](https://github.com/tvproductions/gzkit/blob/8208381d149b8b8704bd012849332ed3a1f2fb38/docs/governance/harbor-classic-adr-change-order.md) at
`8208381d149b8b8704bd012849332ed3a1f2fb38`, especially the settled design and
H5 ruling of November 8. Reuse its decision/edition grammar rather than presenting
this contribution as inventing a naming scheme:

- Stable identity: `ADR-[0-9]{4,}`, starting with `ADR-0001` in a new collection.
- Edition file: `ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md`; number and edition are
  zero-padded to minimum widths four and three, with no overflow rename or cap.
- Slug uses the stated `[a-z0-9-]+` grammar. Keep the readable kebab-case title;
  do not silently substitute a stricter parser contract.
- A revision changes the edition/filename, not the stable decision identity.
  Neither number is a product/release version. Preserve prior editions/history.
- Preserve suitable existing conventions and legacy records; an actual migration
  needs an explicit crossover and reconciliation, not a blanket rename.

The starter already uses `ADR-0001-001-title-in-kebab-case.md` from the shared
lightweight source. The precise width/slug rules above were reviewed in the main conversation
and accepted when the maintainer directed proceeding with this design.
GZKit records this as ratified planning; it is not proof of landed implementation.
Its drydock orders, resolver, ledger/event machinery, operator identity and
GZKit-specific crossover are outside this contribution. No GZKit dependency or
integration follows. Existing consumer policy retains authority.

## Approach and boundaries

Use a focused backlog reference plus explicit calls from existing relevant
checkpoints. The agent recommended this approach; the recorded design approval
and main-conversation continuation select it within the stated boundaries.
An instruction-only repository binding would leave portable backlog checkpoints
unqualified. A new ADR registry, typed checkpoint object or approval service would
expand capability unnecessarily. Select the existing-reference approach for review.

Do not add a ledger, event service, resolver, checkpoint capability, runtime,
dependency, hook or generic ADR skill. Do not change checkpoint/v1's exact schema,
native graph, six labels, mode definitions or reserved namespace rules. Preserve
project language, decision conventions and verification tools. Unrelated consumers
need neither the starter nor gz-skills; their own governing ADR workflow may be used.
Do not copy gz-skills' generic procedure/template into Backplane.

## Checkpoint behavior

Load the focused reference for a consequential architecture choice or an operation
consuming applicable architectural constraints. Routine bounded work need not load
unrelated procedures. Record actual decision ID, edition, locator/revision, approval
provenance and applicable constraint in existing design/plan/evidence references.

| Existing checkpoint | Required behavior |
| --- | --- |
| Design and planning | Inspect relevant current project instructions, decisions and design evidence. Cite/reuse applicable approved decisions. Surface a new/conflicting choice, alternatives and consequences; prepare an identified ADR edition and obtain separate explicit approval. |
| Eligibility, start and transitions | Re-read the issue and reconcile consumed revisions and applicable ADR evidence. A ready label, approved spec/plan, checkpoint index or previous transition supplies no missing architectural approval. Do not begin dependent implementation without it. |
| Active execution | Recheck affected constraints when new choices or changed inputs emerge. Preserve state and stop only dependent tasks. Continue independent already-authorized work. Use existing blocked/resume semantics only when the actual work-item condition warrants them. |
| Review and PR closeout | Compare delivery with applicable approved decisions; report/correct drift. Green checks or merge do not approve replacement architecture. Material replacement needs separate approval; closeout still requires the existing integrated acceptance gates. |
| Product checkpoint capture | Preserve exact decision/edition/content, approval and applicability references using existing records. Missing required evidence limits capture/current claims; capture installation and indexing never grant approval. |

Check actual human approval of the named edition, recoverable reviewed content and
context distinguishing ADR approval from design/plan/release assent. A conversation
without a durable URL may use the policy's short transcribed approval receipt,
embedded in or durably referenced by the ADR. Never invent URLs or approval history.
New drafts have no Current state. Preserve editorial-amendment, replacement and
retirement semantics from the governing policy; do not rewrite decisions to bless drift.
Requirements, plans, evidence and release changes trigger affected reconciliation,
not automatic ADR revision, matching version numbers or duplicate approval.

## Exact existing-record mapping

The mapping is a reference convention, not a schema extension. `Authority.kind`
remains `issue-body|specification|plan|approval|project-instructions`; an ADR must
not be relabelled as a specification or added as an unrecognised `adr` kind.

| Meaning | Existing representation |
| --- | --- |
| Decision identity, edition and applicability | Existing issue/spec/plan authority `content` states them with the immutable ADR locator and exact constraint. Preserve the same references in issue `Superpowers Artifacts` or participating `Backplane Record`, and plan constraints. |
| Reviewed decision record | `Evidence(kind=other)` preserves its locator, immutable revision, SHA-256/content and availability; its ID and purpose are referenced in the consuming authority's content and applicable evaluation `evidence_ids`. |
| Actual exact-edition approval | `Authority(kind=approval)` records approver, locator/revision, content and exact `approved_scope`; reference it through supported `approval_ids`. An accompanying `Evidence(kind=approval)` preserves the actual approval interaction and reviewed-edition identity, referenced by evaluation `evidence_ids` and the authority content. |
| Alignment review | Existing `Evaluation` binds exact criterion/requirement inputs and verified delivery to review/verification evidence; keep `review_approval_ids` for actual review approvals, distinct from ADR approval. |
| Availability or conflict | Existing availability, limitations, rechecks and result fields retain the gap; never convert missing evidence to empty successful observation or SATISFIED. |

Every ID must resolve to the appropriate existing typed collection. Human-readable
content must name referenced evidence IDs and retain their meaning; an arbitrary
string pointer alone does not prove availability or approval. No universal new
reference syntax or parser is introduced. Preserve immutable historical evaluations,
the source/delivery/storage identity distinction and existing pair acceptance rules.

## Product changes after approval

Create `skills/managing-superpowers-backlog/references/architectural-decisions.md`.
Keep it a focused integration contract consuming the project policy/workflow.
Update that skill's `SKILL.md` routing and references `superpowers-binding.md`,
`github-issue-contract.md`, `pr-completion.md` and `repository-checkpoint.md` at the
checkpoints above. Clarify architecture/reference ownership in `governance.md`.
Keep `checkpoint-format.md`'s fields and enums unchanged; document the mapping in
the focused reference and use a conforming fixture to demonstrate it.

Bind Backplane itself through AGENTS.md and a short repository-owned engineering
binding to the immutable starter policy, approved `docs/decisions/` records and
the actually selected portable workflow source. No generic template is authored
here. Preserve proposal bytes before any approved record/receipt is created.
Handoff/v1 already has authority/provenance fields: use them without schema changes.
Update changelog, handoff, owner work and release evidence for delivered scope.

## Approval, plan and release sequence

1. Run a fresh builder check of these drafts. Obtain approval of this identified
   design separately from explicit approval of ADR-0001 edition 1 and preserve
   the exact reviewed proposal bytes, human action and source context.
2. Reconcile an authorized bounded native owner leaf using the complete 15-field
   issue intake: number, title, body, state, stateReason, issueType, labels, parent,
   subIssues, subIssuesSummary, blockedBy, blocking,
   closedByPullRequestsReferences, updatedAt and url. Use the existing executable
   body headings, native graph and exactly-one open lifecycle label.
3. Approve one current issue-bound plan recording consumed issue/design revisions,
   applicable decision/edition/approval references, acceptance and verification
   seams. Re-read before starting and transitioning; preserve the existing
   designing/ready/active/blocked/review/completed gates and mutation authority.
4. Execute through Superpowers and skill-authoring procedures. Keep protected
   upstream read-only; use verified ignored `.sp-bp/work/` fixtures and retain
   portable supporting evidence. Current drafts authorize no implementation.
5. Review integration/alignment, run owner checks and behavioral qualification,
   integrate/push under applicable authority, observe exact-commit CI and publish
   an immutable owner release only after its gates pass. Recheck actual arrival.

Release accounting proposal: published 0.2.0 -> 0.3.0, a coherent minor adding
ADR checkpoint behavior and its own-project binding/evidence. Reconcile any valid
pending target at planning. No new major PRD is required for this minor. This
finite bundle excludes sidecar/commit schemas, release-doctrine transfer,
historical OpenCode/pilot completion and starter adoption. Keep those obligations
visible; do not apply an unrelated historical outcome's gates to this bundle.
No versions, tags or releases change through this design. Before publication,
reconcile source-policy applicability, required freshness/tool migration, version
mirrors/lock and current engineering/deeper-analysis applicability and evidence.

## Acceptance and evidence

Freeze the exact source/policy/workflow/fixture tuple and rubrics before evaluating.
Reuse the shared B01-B16 results only with explicit unchanged-input/applicability
justification; expand affected cases when integration changes shared behavior or
a targeted discrepancy appears. Run active-integration missing-approval stop and
approved-decision continuation controls at actual planning/start/execution/review
checkpoints, with conforming decision/edition/approval/evidence capture. Demonstrate
that lifecycle/index state cannot approve and that independent work proceeds.

Use fresh native model sessions with the actual skill and reachable references,
invented disposable repositories and observed tool/file actions. Preserve complete
prompts, fixture/source hashes, loaded sources, host/model/version/settings or
UNKNOWN, transcripts/actions, staged operator input, per-assertion verdicts and
failures/reruns under `tests/scenarios/`. Scripted fixture approval is not real
approval. Report only tested host scope; schema checks and historical transcripts
do not establish current behavioral compliance or cross-host/native readiness.

Require genuine Backplane internal use after actual separate ADR approval: cite
the approved decision while implementing this integration, then preserve a
source-linked alignment review. This does not replace negative fixture controls.
With Backplane disabled, project planning/review/handoff plus its portable workflow
retain responsibility; do not activate Backplane. Starter qualifies that disabled
binding separately from Backplane's owning active-integration proof.

Run the existing locked Ruff check/format, ty, unittest and four-hook pre-commit
gate, lock check, Node adapter regressions, resource/link/native metadata checks
and `git diff --check`; exact-commit hosted CI remains a separate observation.
Do not add another routine hook or runtime package. Structural tests cannot supply
agent behavior, human approval, genuine internal use or immutable publication.

Design and identified ADR approval are recorded in the sources above. Remaining
gates are native owner intake/current approved plan, final workflow tuple, actual
behavioral/native tests, internal use and release acceptance/publication. Those
execution and qualification results are not claimed by this design.
