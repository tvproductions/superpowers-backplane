# Heavy issue contract GREEN response

Read-only second replay on 2026-09-27. The agent read the edited backlog skill and its two issue-record references, but not the scenario expectations or ADR. It made no file or GitHub edit.

## Verbatim response

This is a **read-only proposal**. The supplied facts establish that #30–#33 are open and that only #32 is executable. They do not establish the issues’ record states, #32’s execution label, or its eligibility. Before claiming heavy status, I would verify the selected heavy profile, the named human’s constitution and PRD approvals and architecture review, and compatible installations on the declared harnesses.

| Issue | Status and record to verify | Metadata and links |
|---|---|---|
| #30 | Open requirement anchor for **R-17**. Its `record_state` must be verified as `current`, `stale`, or `unresolved`; it has no execution label. | Exactly one `anchored_in_prd` link to R-17 in the approved PRD at a checked revision. The PRD alone owns the requirement’s wording and approval. |
| #31 | Open capability **C2**. Verify `proposed`, `accepted`, or `retired`; no execution label. | Its catalog relationships and native parent/children. |
| #32 | Open outcome **C2.3**, the sole executable issue. It has no `record_state`; verify exactly one `backplane:*` execution label. | `belongs_to` C2 initially; `satisfies` R-17 if that is its approved claim; approved design authority and a current `planned_by` link before readiness. Check its native parent, blockers, issue URL, and the `updatedAt` revision consumed by its plan. |
| #33 | Open release gate. Verify its stable semantic ID and `pending`, `satisfied`, `failed`, or `cancelled` record state; no execution label. | Its defined inputs and evidence. A release points to it through `gated_by`; that typed link does not create a native blocking edge. |

I would fetch each issue’s body, labels, `issueType`, native parent and children, both blocking directions, linked closing PRs, URL, and `updatedAt` through `gh`. Each cross-issue typed link must include the target semantic ID and issue URL; document or evidence links need a locator and revision. #32 becomes eligible only after its full leaf contract, approved design, current plan, required links, cleared blockers, and `backplane:ready` label are verified. A `satisfies` link does not prove R-17 has been verified.

For the administrative move, propose updating #32’s `belongs_to` target from C2 to C4 after catalog review while retaining **C2.3** and its prior revision. Reconcile any native parent edge independently. For the later meaning split, propose two new, unique outcome IDs and issue anchors, each with a `split_from` link to C2.3, its own `satisfies` claims, and its own current Superpowers design and plan. Preserve the old anchor and evidence, and record C2.3’s reviewed disposition.

`ROADMAP.md` is a generated, read-only view of a validated approved-document and issue snapshot. Record its input hash and recheck source revisions before publication; if freshness cannot be proved, do not call it current. It does not govern PRD wording or issue state. **No issues or files were edited.**
