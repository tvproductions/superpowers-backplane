# Issues #4/#5 fresh review and fix disposition

Fresh reviewer `/root/review_issue4_5` examined `d557b27..93871be` read-only
under the upstream code-review template. It found no Critical or Minor findings,
two Important findings and no declined judgments. The review confirmed the
license holder, bounded support statements, immutable historical sources,
unchanged approved plans/canonical skills, and independently checked graph.

## Important findings and demonstrated fixes

1. The #5 validator accepted missing schema/trace/authority and invalid criterion
   results. Five new assertion-level controls failed against the old validator;
   after correction the complete suite passes 19/19. It requires essential
   report fields, schema, observation time and result vocabulary; a claimed
   lifecycle PASS requires its native trace stages; every supplied trace row
   requires historical authority, including rows without a `result` property.
   Completion ordering and unsupported overall satisfaction are checked.
   A legitimate UNKNOWN report remains valid. All five reviewer mutations of
   the actual receipt now return errors, captured in
   [actual-shape controls](transcripts/2026-11-01-issue-5-review-actual-shape.json).
2. The #4 inventory omitted prose-defined setup, discovery and recovery paths.
   Four behavioral tests first failed for the missing prose extractor, then
   passed against the implementation. The receipt retains its 25 original
   fenced/session representations and adds 74 unfenced instruction/recovery
   rows with exact source line, heading, expected requirement, prerequisites,
   recovery condition and explicit UNKNOWN. Some requests appear in both their
   fenced/session representation and their prose context; these are not extra
   native runs. Native CLI exits do not promote the prose checks to PASS.

Owned corrective sources/tests and RED/GREEN results are retained in the
`transcripts/2026-11-01-issue-4-*` and `issue-5-*` namespaces. All four files
pass Ruff check/format and ty; 4 inventory tests, 19 validator tests, five
actual-receipt mutation controls, current-receipt validation, document links,
guide syntax checks and the nine package regressions pass. Whitespace checks
pass. Initial import-order findings were corrected and final checks rerun.

This was the required single fix pass. Final corrected bytes were verified by
tests and evidence checks; no second independent review is claimed. No material
review finding remains unresolved. Full issue acceptance remains separate:
Codex native reads were blocked, per-operation payload/preservation evidence is
incomplete, OpenCode host work remains with its owners, and publication/hosted
recognition are pending. The later native recommendation's publication
prerequisite is explicitly rejected as readiness advice under AGENTS.md.

## Rulings and deferred obligations

- Use native files under `.sp-bp/work/` instead of upstream helpers that write
  reserved `.superpowers/`; this preserves project namespace ownership.
- Execute inline after the start instruction; retain one fresh whole-change
  review and its demonstrated fix pass.
- Keep remote #4/#5 OPEN/backlog after automatic approval review refused issue
  body publication and subsequent label-only transitions. Neither action ran;
  no workaround bypassed the rejection. Approved local work remains authorized
  by project verification policy; external publication requires operator approval.
- Preserve initial signed-out results. The operator completed sign-in; no
  credential was copied. Claude fresh three-skill loads passed; Codex's policy
  refusal remains UNKNOWN and was not bypassed.
- Reuse historical evidence only at its recorded scope when current relevant
  source bytes match; do not describe simulations as native mutations.
- Score native recommendation only for its observed no-priority/no-selection/
  zero-mutation behavior. Its extra remote-publication prerequisite is not
  authority and remains an explicit limitation for broader readiness advice.

No deferred Minor review finding exists. Remaining acceptance and publication
gaps are listed in the two issue assessments, not silently waived.
