# First heavy-contract GREEN response

Read-only agent replay on 2026-09-27 after the first heavy skill edit, before the input-hash clarification. It read the edited backlog skill and the two issue-record references, but not the scenario expectations or ADR. No files or issues were edited by that agent.

## Verbatim response

This is a **read-only proposal**. The supplied facts establish that #30–#33 are open and that only #32 is executable. They do not establish the issues’ current record states, #32’s execution label, or its eligibility. I would first verify the selected heavy profile, the required governing approvals and installation compatibility, then fetch each issue’s body, labels, native relationships, linked PRs, URL, and `updatedAt` through `gh`.

| Issue | Heavy record and status to report | Links to verify |
|---|---|---|
| #30 | `kind: requirement`, `semantic_id: R-17`; open. Its `record_state` is `current`, `stale`, or `unresolved` only after reconciliation. | Exactly one `anchored_in_prd` link to the approved PRD requirement and revision. The issue does not approve or own R-17’s wording. |
| #31 | `kind: capability`, `semantic_id: C2`; open. Verify whether its `record_state` is `proposed`, `accepted`, or `retired`. | Catalog relationships and native children, checking any `belongs_to` claims against native edges. |
| #32 | `kind: outcome`, `semantic_id: C2.3`; open and the only executable issue. Verify its single `backplane:*` label; outcomes have no `record_state`. | `belongs_to` C2 initially, `satisfies` R-17 if that is its approved delivery claim, and current `planned_by` and design authority links. Inspect native parent, blockers, and the plan’s consumed issue URL and revision. |
| #33 | `kind: gate`; open. Verify its stable semantic ID and `record_state` (`pending`, `satisfied`, `failed`, or `cancelled`). It has no execution label. | Defined inputs and evidence. A release’s `gated_by` link points to this gate; native blocking edges are checked separately. |

Each cross-issue typed link must name the target’s semantic ID **and issue URL**. Document and evidence links need a locator and revision. A `satisfies` link is a delivery claim, not proof that R-17 has been verified. #32 is eligible only if its body contract, approved design authority, current plan, required links, clear native blockers, and `backplane:ready` label all check out.

For the administrative move, propose changing #32’s `belongs_to` target from C2 to C4 after catalog review, while retaining **C2.3** and its history; reconcile any native parent edge separately. For the later meaning split, propose two new, unique outcome IDs and issue anchors. Each would link `split_from` C2.3, state its own `satisfies` claims, and obtain its own current Superpowers design and plan before readiness. Preserve C2.3 and record its reviewed disposition.

`ROADMAP.md` is a generated, read-only view. Its source and freshness should be checked against the approved PRD and issue catalog. It does not govern requirement wording, issue state, or relationships. No issues or files have been edited.

## Scoring

Assertions 1–4 and 6 passed. Assertion 5 was incomplete: it described a generated view and a freshness check but did not require an input hash or revision recheck. The skill was tightened to name both before a second replay.
