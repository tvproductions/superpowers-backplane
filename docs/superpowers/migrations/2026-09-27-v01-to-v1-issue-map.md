# v0.1 to heavy SDD 1.0 issue migration map

**Status:** Before-map with proposed classifications, planned-node IDs, and new issue set. The PRD's requirement IDs and wording are approved, but this issue mapping and its exact mutation payloads are not. No semantic ID, PRD link, issue body, title, label, native edge, or closure state has been migrated live.

**Source:** [Complete native issue snapshot](../../../tests/scenarios/transcripts/2026-09-27-heavy-issue-before.json), observed 2026-09-27, SHA-256 `8AB1755EE78994A151A6AC1CF89E3EE3E71085110533F377F96E2C836C64B2F5`. The snapshot has 21 issues and exact `updatedAt` values. Re-read live records before any edit.

| Issue | Observed record | Candidate heavy kind | Migration review required |
| --- | --- | --- | --- |
| [#1](https://github.com/tvproductions/superpowers-backplane/issues/1) | Open `backplane:backlog`; v0.1 release parent; 17 direct children | `release` | The 1.0 PRD is approved; review whether its stable release record can retain this anchor. Change version target without erasing v0.1 history; remove execution label only after heavy contract is live. |
| [#2](https://github.com/tvproductions/superpowers-backplane/issues/2) | Closed; v0.1 adoption contract | `outcome` historical | Preserve completed design evidence; assess which 1.0 PRD requirements it supports and which need new outcomes. |
| [#3](https://github.com/tvproductions/superpowers-backplane/issues/3) | Closed; Codex installation | `outcome` historical | Preserve host evidence; recheck compatibility and new heavy behavior before a 1.0 verification claim. |
| [#4](https://github.com/tvproductions/superpowers-backplane/issues/4) | Open backlog; licensing and operations | `outcome` | Reassess acceptance against the 1.0 public contract and heavy operations. |
| [#5](https://github.com/tvproductions/superpowers-backplane/issues/5) | Open backlog; v0.1 self-hosting | `outcome` | Redefine self-hosting proof around approved PRD, full migrated graph, trace, views, V&V, and gate; retain native blockers unless review changes them. |
| [#6](https://github.com/tvproductions/superpowers-backplane/issues/6) | Open backlog; external pilot | `outcome` | Expand or replace pilot acceptance for heavy adoption and declared harnesses; retain observed five native blockers until reviewed. |
| [#7](https://github.com/tvproductions/superpowers-backplane/issues/7) | Open backlog; v0.1 publication, blocked by #6 | `gate` candidate | Decide whether the publication work needs a separate executable outcome plus gate record. Require 1.0 trace, V&V, compatibility, exact human approval, and tag evidence. |
| [#8](https://github.com/tvproductions/superpowers-backplane/issues/8) | Open backlog; additional harness evaluation | `incidental` candidate | Reassess as proposal outside or inside 1.0 scope; do not assign an enduring ID until promotion. |
| [#9](https://github.com/tvproductions/superpowers-backplane/issues/9) | Open backlog; deterministic helper evaluation | `incidental` candidate | Reassess against required derived-view freshness; do not silently treat the old evaluation as implementation approval. |
| [#10](https://github.com/tvproductions/superpowers-backplane/issues/10) | Closed; handoff continuity | `outcome` historical | Preserve result and evidence; no automatic current PRD verification. |
| [#11](https://github.com/tvproductions/superpowers-backplane/issues/11) | Open backlog; final Claude acceptance | `outcome` | Reconcile with #19 and new heavy conformance while preserving predecessor evidence. |
| [#12](https://github.com/tvproductions/superpowers-backplane/issues/12) | Open backlog; final OpenCode acceptance | `outcome` | Reconcile both OpenCode branches with heavy conformance. |
| [#13](https://github.com/tvproductions/superpowers-backplane/issues/13) | Closed disposable Codex fixture | `incidental` historical | Keep as fixture; do not assign a product ID or PRD satisfaction. |
| [#17](https://github.com/tvproductions/superpowers-backplane/issues/17) | Closed; Claude package | `outcome` historical | Preserve integration and installation evidence; recheck only affected 1.0 seams. |
| [#18](https://github.com/tvproductions/superpowers-backplane/issues/18) | Closed; Claude setup | `outcome` historical | Preserve upstream adoption evidence; recheck affected 1.0 seams. |
| [#19](https://github.com/tvproductions/superpowers-backplane/issues/19) | Open designing; Claude lifecycle; draft plan on separate branch | `outcome` | Reconcile scope and unapproved plan with 1.0 PRD before readiness or execution. Do not edit the other worktree. |
| [#20](https://github.com/tvproductions/superpowers-backplane/issues/20) | Open backlog; OpenCode adapter | `outcome` | Preserve shared adapter ownership; add heavy conformance only after reviewed scope change. |
| [#21](https://github.com/tvproductions/superpowers-backplane/issues/21) | Open backlog; OpenCode V1 setup | `outcome` | Reassess compatibility and 1.0 test floor. |
| [#22](https://github.com/tvproductions/superpowers-backplane/issues/22) | Open backlog; OpenCode V1 lifecycle | `outcome` | Reassess lifecycle and heavy conformance. |
| [#23](https://github.com/tvproductions/superpowers-backplane/issues/23) | Open backlog; OpenCode V2 setup | `outcome` | Reassess compatibility and 1.0 test floor. |
| [#24](https://github.com/tvproductions/superpowers-backplane/issues/24) | Open backlog; OpenCode V2 lifecycle | `outcome` | Reassess lifecycle and heavy conformance. |

## Decision log to complete before mutation

1. The operator has approved this repository's constitution, project PRD, architecture, and named approver. Review the proposed planned-node ID allocation below and create requirement anchors only after the complete before/after payload is approved. The PRD's twelve requirement IDs are already approved; no planned-node ID is minted by this document alone.
2. Decide #1's release-record continuity and #7's gate versus executable-publication split. The recommended choice is to keep #1 as the stable release record, use #7 as the gate, and create a separate bounded publication outcome if human-approved issue review finds its implementation work cannot live in a gate.
3. Review every completed issue against current PRD requirements and current evidence. Mark `historical`, `current`, or `needs re-verification` per typed edge; do not rewrite closure history.
4. Review every open issue's acceptance, blockers, owner, and target release. Record explicit preserve/revise/supersede/retire rationale and exact old/new body and label before asking for approval of live edits.
5. Re-fetch each issue's native revision. A changed `updatedAt` triggers semantic reconciliation; the snapshot alone never authorizes a mutation.

## 1.0 coverage and missing graph nodes

The 21 existing issues describe the v0.1 installation and publication arc. They do not, by themselves, represent the twelve approved 1.0 PRD requirements, the new heavy-model delivery outcomes, or a current release decision. The following is a **candidate planning crosswalk**, not an assertion of current trace or approved issue IDs. Each `BP-R...` row still needs its own approved requirement issue anchor and current typed outcome links. A requirement may govern several outcomes and an outcome may satisfy several requirements.

| Approved PRD scope | Relevant existing anchors | Additional 1.0 graph work |
| --- | --- | --- |
| `BP-R001` governance and three-component readiness | #2 and #5 contain historical adoption/self-hosting evidence | Anchor the requirement; plan and verify heavy readiness and compatible-set checks. `gz-skills` retains profile setup ownership. |
| `BP-R002` PRD authority | #5 can exercise self-hosting | Anchor the requirement; plan PRD revision/approval and impact reconciliation outcome. |
| `BP-R003` kinds and states; `BP-R004` stable IDs; `BP-R005` typed links | #5 can exercise the resulting graph; #9 explored tooling only | Anchor each requirement; add reviewable schema, validation, and migration outcomes with separate semantic IDs. |
| `BP-R006` trace currency; `BP-R007` verification and validation | #5 self-hosting and #6 pilot can provide later evidence | Anchor each requirement; add trace/evidence and intended-use validation outcomes. A closed v0.1 host issue is historical, not automatically current verification. |
| `BP-R008` generated roadmap/backlog | #9 is an old evaluation issue, not implementation approval | Anchor the requirement; add a view-generation/check outcome and any explicit tooling decision. Do not claim views current until snapshot races and offline behavior pass. |
| `BP-R009` release identity; `BP-R010` human gate | #1 release parent and #7 publication issue are candidates | Anchor both requirements; decide #1/#7 dispositions, add bounded implementation outcomes if their non-executable records cannot own the work, and retain exact human publication authorization as a later action. |
| `BP-R011` host adoption | #3, #11, #12, #17–#24 | Anchor the requirement; preserve completed installation evidence and revise open host acceptance for the 1.0 contract. Recheck affected Codex and Claude seams and finish both OpenCode variants. |
| `BP-R012` deliberate migration | All 21 historical issues; #5 self-hosting | Anchor the requirement; add migration and integrated self-hosting outcomes. Preserve aliases and closure history; report unresolved mappings. |

The current release chain also has product obligations outside the new schema implementation: #4 requires a human-selected license and tested adopter operations; #6 requires an authorized external repository and its own governing approvals for the 1.0 pilot; #19's unapproved draft plan needs reconciliation in its separate work stream; #7 cannot publish without fresh verification, distinct validation, compatibility review, and a human decision. These are not waived by approving the ADR or by completing Tasks 3–6 of the implementation plan.

## Proposed identity allocation and disposition

The following IDs are **proposals for review**, not allocated live identities. The approved `BP-R001`–`BP-R012` IDs stay in the PRD. The existing issue numbers stay tracker addresses. A review may alter a proposed ID before first use; after approval and first use it must never be recycled. An administrative family move changes `belongs_to` without renaming an ID. A changed meaning creates a new issue/ID and typed historical relation.

| Existing issue | Proposed kind and ID | 1.0 disposition | Candidate current PRD delivery claim |
| --- | --- | --- | --- |
| #1 | `release` `REL1` | Preserve the parent and its native children; revise target from v0.1.0 to `1.0.0` while retaining prior title/body history. The record remains assembling. | None: a release is not an executable outcome. |
| #2 | closed `outcome` `C1.1` | Preserve the completed v0.1 adoption contract as historical. A new 1.0 governance outcome succeeds it where meaning changed. | None until an explicit current-scope review. |
| #3 | closed `outcome` `C6.1` | Preserve Codex installation evidence; reverify affected 1.0 seams. | `BP-R011`, with evidence initially stale for 1.0. |
| #4 | open `outcome` `C7.1` | Revise licensing and adopter operations acceptance for 1.0; human license choice remains open. | `BP-R011` for operations; no legal decision inferred. |
| #5 | open `outcome` `C1.2` | Revise self-hosting acceptance for the approved PRD and complete heavy graph. | `BP-R001`, `BP-R012`; evidence initially missing. |
| #6 | open `outcome` `C1.3` | Revise external pilot acceptance for three installed components and declared harnesses. | `BP-R001`, `BP-R011`; intended-use validation is a separate result. |
| #7 | `gate` `G1` | Preserve the native blocker on #6; move publication *decision* into the gate and leave any executable publication preparation to a separate outcome. | None: the release implementation outcome covers `BP-R010`. |
| #8 | unrecorded `incidental` | Keep the additional-harness proposal outside the initial 1.0 scope unless later promoted. Remove its execution label only in the reviewed heavy migration batch. | None. |
| #9 | unrecorded `incidental` | Keep the old post-v0.1 helper evaluation as historical decision context. Create a distinct new view implementation outcome; do not rewrite #9 as if it approved that work. | None. |
| #10 | closed `outcome` `C1.4` | Preserve handoff continuity and completed evidence; review its fit to current 1.0 requirements separately. | None at first migration. |
| #11 | open `outcome` `C6.2` | Revise final Claude acceptance after #19's 1.0 plan is reviewed. | `BP-R011`; current evidence missing. |
| #12 | open `outcome` `C6.3` | Revise final OpenCode V1/V2 acceptance after both branches. | `BP-R011`; current evidence missing. |
| #13 | unrecorded closed `incidental` | Preserve the disposable verification fixture and `documentation` label. | None. |
| #17 | closed `outcome` `C6.4` | Preserve Claude package result; recheck affected 1.0 installation seams. | `BP-R011`, with evidence initially stale for 1.0. |
| #18 | closed `outcome` `C6.5` | Preserve Claude setup/upstream adoption result; recheck affected 1.0 seams. | `BP-R011`, with evidence initially stale for 1.0. |
| #19 | open `outcome` `C6.6` | Keep `backplane:designing`; reconcile the separate unapproved draft plan before readiness. | `BP-R011`; current plan and evidence missing. |
| #20 | open `outcome` `C6.7` | Preserve shared OpenCode adapter ownership; revise acceptance for heavy behavior. | `BP-R011`; current evidence missing. |
| #21 | open `outcome` `C6.8` | Revise V1 setup acceptance for 1.0. | `BP-R011`; current evidence missing. |
| #22 | open `outcome` `C6.9` | Revise V1 lifecycle acceptance for 1.0. | `BP-R011`; current evidence missing. |
| #23 | open `outcome` `C6.10` | Revise V2 setup acceptance for 1.0. | `BP-R011`; current evidence missing. |
| #24 | open `outcome` `C6.11` | Revise V2 lifecycle acceptance for 1.0. | `BP-R011`; current evidence missing. |

The candidate current claims above are not verification. Every `satisfies` edge needs the approved PRD revision, an issue anchor, current SP artifacts where applicable, and independent evidence. Closed historical host issues retain their original closure and results; their 1.0 link currency starts stale or unknown, never automatically current. Preserve all native parent, sub-issue, blocker, blocking, and closing-PR relationships unless a separate review changes one. An incidental issue needs no semantic ID or record block; #8 and #9 nevertheless remain explicit rows in this migration manifest so the old execution label cannot disappear without review.

## New 1.0 issue anchors required

Create one requirement issue per approved PRD ID `BP-R001`–`BP-R012`, each with one `anchored_in_prd` link to its exact approved PRD revision. Its body quotes or summarizes for navigation but cannot redefine the requirement. The current GitHub issue numbers are unknown until creation and will be recorded in the after-map; never derive the requirement ID from them.

The proposed capability family anchors are `C1` governing documents/readiness, `C2` catalog and migration, `C3` trace and V&V, `C4` derived views, `C5` release records/gates, `C6` host adoption, and `C7` adopter operations. Each needs its own issue and `capability` record. The existing outcome IDs above are grouped through `belongs_to`; their numeric prefix is historical identity, not a rule that constrains a later family move. Native #1 child relationships are preserved as observed and are not treated as a substitute for these semantic family links.

| New outcome ID | Reviewable 1.0 result | Proposed requirement links | Historical relation |
| --- | --- | --- | --- |
| `C1.5` | Approved-document authority and compatible three-component readiness are checked without SP-BP taking over gz-skills setup. | `BP-R001`, `BP-R002` | `succeeds` historical #2/`C1.1` only if the reviewed meaning comparison supports it. |
| `C2.1` | Heavy kind/state, stable-ID, and typed-link schema and validator work on full issue intake. | `BP-R003`, `BP-R004`, `BP-R005` | New scope. |
| `C2.2` | Every v0.1 issue is reconciled with an approved before/after map, preserved history, and checked native edges. | `BP-R012` | New scope; #5 later exercises the migrated result. |
| `C3.1` | Forward/reverse trace, impact analysis, verification, and distinct intended-use validation evidence are reconciled. | `BP-R006`, `BP-R007` | New scope. |
| `C4.1` | Deterministic ROADMAP/BACKLOG generate and freshness check pass source-race and offline cases. | `BP-R008` | New scope informed by #9, not a silent promotion of #9. |
| `C5.1` | Stable release record, selected outcomes, candidate digest, compatibility and human-authorization gate are checked. | `BP-R009`, `BP-R010` | New scope; #1 and #7 become the record and gate. |

These are the minimum missing implementation outcomes indicated by the approved PRD. They need issue anchors and SP specs/plans before execution. The current uncommitted Python modules are work toward these outcomes, not evidence that a live issue or requirement has been approved or verified. #4–#6, #11–#12, and #19–#24 continue as separately reviewable work under their reconciled acceptance. A separate publication-preparation outcome is created only if #7's reviewed executable work cannot be completed under `C5.1` and #4's operations scope; #7 itself must remain a decision gate.

## Application order and stop points

1. Freeze this proposed map at an exact revision. For each of the 21 observed issues, attach the original title, body hash, state, labels, `updatedAt`, native edges, and proposed disposition; write the complete replacement record block and any acceptance/title/label edits as a before/after payload. Re-fetch live revisions and reconcile any drift before approval.
2. Review the proposed ID allocation, #1 release continuity, #7 gate split, #8/#9 incidental treatment, each closed outcome's historical evidence, each open leaf's revised acceptance, and the complete new-issue set with the named human approver. **No `gh issue edit` or issue creation follows from this proposal alone.**
3. After approval, create requirement anchors and capability/outcome anchors in small batches with `gh`, recording assigned issue numbers and revisions. Add typed links only once targets exist. Keep native hierarchy and blockers. A batch that fails validation stops before the next batch.
4. Migrate existing records with the reviewed payloads. Non-executable #1/#7/#8/#9 lose their old execution labels only in the batch that establishes their heavy disposition. Open executable outcomes retain exactly one of the six labels. Re-read every affected issue and update the after-map with old/new revisions and any deviation requiring renewed review.
5. Reconcile approved PRD requirements against all issue anchors and outcomes; report missing/stale examples, tests, evidence, SP specs/plans, and release links. Only then generate/check the two derived views from a rechecked source snapshot. Keep verification, validation, candidate version, compatibility, human authorization, and published tag separate. #1 remains assembling and #7 pending until the full 1.0 gate passes.
