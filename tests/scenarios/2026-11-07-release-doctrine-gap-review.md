# Release-doctrine design gap review and reappraisal

Date: November 7, 2026. Scope: review and correction of the consolidated design,
followed by fresh independent reappraisal. No implementation, skill changes,
GitHub mutations or policy activation were requested in this pass.

Reviewed authority: the user's direction to keep Backplane independent, align
lite/heavy release semantics, and require starter enforcement; current Backplane
governance, modes, release binding and PR completion contract; starter versioning,
structure and actual helper boundaries; immutable gz-skills source identified in
the [initial source record](2026-11-07-release-doctrine-alignment.json).

The earlier builder check found sufficient information to plan, but did not
establish absence of design loopholes. This deeper review found and corrected
four Important gaps plus related contract ambiguities. The revised
[design](../../docs/superpowers-backplane/specs/2026-11-07-release-doctrine-alignment-design.md)
remains a proposal for reappraisal, not approved implementation authority.

## Findings and corrections

| ID | Finding in the prior draft | Correction in gap-review 2 | Required implementation proof |
| --- | --- | --- | --- |
| G1 — Important | A supplied feature list could omit a shipped addition or breaking change and still support a patch. Deferral could conceal distributed behavior. | Release-impact accounting now requires whole baseline-to-candidate path/component coverage, including generated resources and untracked feature contributions. Shipped deferred behavior still receives actual compatibility analysis. | Reject omitted addition, removal/default change and exposed experimental behavior marked no-impact solely because acceptance was deferred. |
| G2 — Important | A missing project checker could trigger manual fallback even when the adopted policy made it mandatory. | Results/mandatory-check rules distinguish optional automation from binding-required checks. Missing/older helpers block acceptance; only policy-permitted approved equivalent substitution can support conditional handling. | Required checker absent/incompatible is non-success; unrelated manual-policy consumer remains usable. |
| G3 — Important | Universal profile requirements would block starter self-release and encourage synthetic self-adoption. | Profiles/self-release distinguishes actual adopters from validated canonical starter repository context; independent Backplane consumers need no gz-skills settings. | Legitimate starter release without settings works; adopter spoofing self-release context fails; no settings are created. |
| G4 — Important | Exact commit checks could become self-referential or allow final release metadata/source to drift after verification. | Candidate identity separates tested delivery, distributed payload and later evidence-storage commits. The actual final release commit/package is reconciled; affected checks rerun for relevant changes. | Evidence-only storage preserves applicable evidence; payload/metadata change requires reconciliation and affected gates; no blanket evidence exclusion. |
| G5 — Supporting correction | A hash or asserted PASS might be mistaken for API compatibility, adequate PRD or accepted consumer impact. | Enforcement now distinguishes mechanically checked facts from exact-input judgments accepted by an authorized reviewer. Record contents are never executed. | Unaccepted judgments and missing/irrelevant major PRD cannot produce strict readiness. |
| G6 — Supporting correction | Canon ownership could drift across references, supplement requirements or offline updates. | Exact policy/supplement adoption, conflict handling, staged effective revisions, shared Backplane-owned conformance examples and verified offline snapshots are explicit. | Equivalent lite/heavy verdicts; privately changed expected verdicts rejected; unavailable mandatory current-source review remains a gap. |
| G7 — Supporting correction | Conditional acceptance and evidence reading lacked firm limits. | Conditional results remain non-success; exception permission, authority, owner and revisit are required. Paths, snapshots and parsing are bounded, with no arbitrary URL fetching or execution. | An unauthorized waiver, escaped artifact or embedded command cannot create readiness or publication effects. |
| G8 — Supporting correction | New alignment work might silently enter the already approved initial-release scope. | Design requires separate issue/scope and bundle decisions; documentation-only consolidation leaves enforcement visibly unimplemented. | Native intake and selected bundle preserve original obligations and approval boundaries. |

The first independent reviewer confirmed G1–G4 and supplied G2's mandatory-check
bypass finding. Other corrections arose from the primary review. Exact JSON
encoding and CLI numeric exit codes remain legitimate execution-plan decisions;
their required semantics are now specified. They are not evidence that a
checker exists.

## Source-state reconciliation

The starter maintenance was committed independently during review, first as
`f0f5428c3f9146c4caaab209822b1f5d5fd57daa`, then observed at
`e918dbbd02353258b697de5f63739a2431d65327` with a clean tree. This task made no
starter changes. Of 18 initially sampled files, 17 hashes remain identical;
only its handoff differs. The second commit changes Dependabot commentary and
compatibility evidence, without changing the release-ownership sources reviewed
here. Preserve the initial record as historical rather than replacing its hashes.

No new GitHub policy, source publication, native host acceptance, release-check
implementation or ensemble integration follows from these observations.

## Reappraisal and limits

The fresh reviewer assessed the corrected semantics independently after the
first gap-fix pass. Its final disposition and exact reviewed design identity are
recorded in the [review receipt](2026-11-07-release-doctrine-gap-review.json).
Any final source-state wording correction is editorial and has no effect on the
reviewed release contract.

This pass verifies design coherence and source/evidence consistency. Behavioral
acceptance remains unperformed until the owning implementation plans, negative
controls and repository gates run. The user is reappraising the design; execution
and publication remain separate.
