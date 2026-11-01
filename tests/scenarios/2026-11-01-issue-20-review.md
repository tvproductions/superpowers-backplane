# Issue #20 independent review and correction record

A fresh gpt-6-astra reviewer assessed source range `337aa19..bc6d30e` and
the owned fixture scorer read-only. The reviewer did not spawn another agent
or mutate the checkout. The approved #20 plan/specs and all five Review Focus
conditions were supplied, along with the execution rulings and the explicit
pending-authentication limitation.

## Findings

Two Important findings, no Critical/Minor findings; declined-to-judge list empty.
No actionable adapter source defect was identified. The reviewer explicitly
withheld merge readiness because native fresh authenticated loads were pending.

1. The scorer recorded provenance/isolation without verifying the loaded
   upstream path or effective config sources. Read-only probes returned PASS
   for an untrusted origin and an unrelated upstream path.
2. The final gate only reclassified stored JSON. Probes also returned PASS
   for `auth_verified="unverified"`, `loaded="unverified"` and a local-directory
   package target. Capture integrity, current inventory, links, candidate
   applicability and stored-score checks were absent.

## One correction pass

The following four unittest cases were added and run before fixes; all four
failed while the prior seven passed:

- `test_untrusted_origin_and_unbound_upstream_path_cannot_pass`
- `test_only_real_boolean_verification_and_loads_can_pass`
- `test_local_directory_or_wrong_git_revision_cannot_pass`
- `test_capture_integrity_is_checked_against_actual_files`

Observed result: `Ran 11 tests` / `FAILED (failures=4)`. Corrections require
actual Booleans, a full-SHA Git target matching the candidate, bound canonical
upstream source/path and explicit effective-config containment. Inference is
gated on that provenance/configuration and installed inventory. The final
verification rechecks capture hashes, candidate/current/installed file
identities, source/installed reference links, upstream/executable identity,
current preservation snapshots and stored result consistency.

After the correction, all 11 unittest cases pass, Ruff/format/ty pass on five
helpers, and both real native records pass every current non-authentication
verification check. The final gate still exits 1 because both complete native
smoke scores remain UNKNOWN. Captured helper sources and exact file hashes
are in the [structured receipt](2026-11-01-issue-20-opencode-adapter.json).
No second independent review, fully passing acceptance, merge or closure is
claimed. There are no deferred Minors or declined judgments to disposition.
