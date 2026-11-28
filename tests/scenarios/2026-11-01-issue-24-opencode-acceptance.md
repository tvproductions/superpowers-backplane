# Issue #24 OpenCode V2 lifecycle verification

## Task 1 — Native package operations

This record covers the native operation portion of [issue #24](https://github.com/tvproductions/superpowers-backplane/issues/24). The issue was active at `2026-11-27T23:54:01Z` during replay. Its only prerequisite, [#23](https://github.com/tvproductions/superpowers-backplane/issues/23), was closed completed with a published satisfaction evaluation. The current #24 artifact pointer binds the approved plan and probe contract without changing the requirement inputs.

The [OpenCode guide](../../docs/installing-opencode.md#maintain-opencode-v2) documents the tested package operations. The verified Windows host was OpenCode V2 2.1.4, executable SHA-256 `b12b0613e9b4a491e5b12d90a5e9bbae6d261fe9688c82bf73125a036963d399`. The private server loaded Superpowers v7.0.1 at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. The prior Backplane pin was `386bdb5a8570360f5d34359c68f68947eb7a90fc`, and the update target was `8e1e2005025890776eb99bd4b9161996fbbe68ed`. Each was resolved from the actual hosted repository.

| Case | Result | Native observation |
| --- | --- | --- |
| L-install | PASS | One Backplane package at the prior pin, 70 Git blob matches, three fresh authenticated Skill calls. |
| L-repeat | PASS | The same exact configuration and single package after a repeat, with three fresh calls. |
| L-update | PASS | The candidate pin replaced the prior pin, 105 Git blob matches, three fresh calls. |
| L-rollback | PASS | Restored the prior commit after the update, with 70 blob matches and three fresh calls. |
| L-unavailable-source | PASS | The native resolver failed on the intentionally absent full commit. The before-repair snapshot preserved unrelated state. The earlier configuration bytes, 70 package files and three fresh calls were verified after restore. |
| L-failed-verification-recovery | PASS | The resolvable candidate activated. A controlled native Skill permission denied one required call while the remaining two completed. The previous configuration bytes, 70 files and all three fresh calls were then verified. |
| L-uninstall | PASS | The active Backplane package and both Backplane skills were absent. The upstream Skill loaded and the unrelated native plugin remained active. |
| L-test-restore | PASS | The disposable profile returned to the prior pin, with 70 Git blob matches and three fresh calls. |

Each case used a fresh private server, the isolated consuming project, and an authenticated native session on that server. Every retained row records the upstream Skill blob and matches the unaffected plugin entries, five protected fixture files, and the complete native #24 issue intake before and after the operation. The recovery captures record those comparisons before repair as well. Authentication was reused through the already authorized native data pointer.

The first unavailable-source attempt exposed a failed resolver inventory entry that contained source and failure state without a registered plugin ID. The original parser raised `KeyError` on that genuine native state. A regression test reproduced it, a focused correction distinguished the failed entry from an installed package, and a fresh isolated replay passed. The initial unqualified auth command timed out. The explicit private-server auth command returned exit zero and listed OpenAI. No earlier partial observation was scored as a completed case.

The [structured receipt](2026-11-01-issue-24-opencode-acceptance.json) retains separate attempts for positive and recovery operations, screened session and call identities, actual source and blob maps, and hashes of the raw captures. [Scorer](transcripts/2026-11-01-issue-24-lifecycle.py.txt), [native runner](transcripts/2026-11-01-issue-24-native_lifecycle.py.txt), [failure runner](transcripts/2026-11-01-issue-24-native_failures.py.txt), and [regression controls](transcripts/2026-11-01-issue-24-test_lifecycle.py.txt) are archived from the owned verification area. The native runner reuses the tracked corrected #23 helper sources in that area. Its observations remain separate from the synthetic processing tests.

## Task 2 — Installed conformance and native issue lifecycle

This Task 1 record establishes the package operation rows. The five named checks, the authorized fixture's native lifecycle evidence, whole-change review, and exact integrated delivery are separate stages of #24 acceptance.

### Read-only conformance

All five named checks passed on the exact hosted #23 package at
8e1e2005025890776eb99bd4b9161996fbbe68ed. The skill-structure check confirmed
both Backplane entry-point names, metadata, Git blobs, and ten directly linked
references. The four behavioral prompts ran in separate fresh authenticated
OpenCode V2 2.1.4 sessions. Each completed a native backlog Skill call, and all
23 rubric expectations passed. Native #24 intake and protected files matched
before and after the suite.

The [scored transcript](2026-11-01-issue-24-opencode-conformance.json) records
the exact prompts, responses, screened native events and scores. Its installation
scenario notes that the historical test sources are outside the installed
package. The verifier supplied the exact repository prompts and evaluated the
rubrics. The adopter guide links to the hosted evidence record so the installed
guide can reach it. The authorized fixture lifecycle is recorded below.

### Native issue-state fixture

The operator approved [fixture #39](https://github.com/tvproductions/superpowers-backplane/issues/39)
for the guide and evidence links. Eleven fresh authenticated OpenCode V2 2.1.4
sessions used the native backlog Skill from the exact hosted package at
`8e1e2005025890776eb99bd4b9161996fbbe68ed`. Each phase retained a complete
native GitHub read before and after its permitted actions. The protected owner
issue #24 and unrelated fixture files matched throughout.

| Operation | Observed result |
| --- | --- |
| Status and selection | Identical before and after native issue snapshots. |
| Design and readiness | Backlog to designing to ready with the approved issue-bound fixture plan and clear dependencies. |
| Start, block and resume | Ready to active, then blocked with a concrete release condition and the active resume target. Active resumed after the exact local link check. |
| Submission and rework | Active to review, review to active after independent feedback, then review after the immutable section link passed verification. |
| Completed closure | Native review-to-completed closure after the exact fixture delivery passed all three hosted checks. The final issue retained only its unrelated `documentation` label. |

[PR #40](https://github.com/tvproductions/superpowers-backplane/pull/40) merged
the two scoped fixture documents as `6f0c295d6e34d86dd516140092d91e628f52e8ec`.
GitHub served both matching file blobs and rendered the two linked headings.
[Exact-main CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46088154550)
passed on Ubuntu, macOS, and Windows. The fixture's first design and blocked
probes refused to write under insufficient fixture read permissions. Both
preserved native issue state and passed on a fresh, narrowly scoped retry.

The [screened native fixture receipt](2026-11-01-issue-24-opencode-native-fixture.json)
retains all eleven stage results, the actual command evidence, and hashes of
the separately retained raw captures.

### Whole-change review corrections

Independent review of `dff28c0725932e3c681f8cc79b1c5e4109cd1af1` identified
two gaps. The lifecycle scorer accepted incomplete or misattributed native
evidence, and the earlier replay covered recovery after an unavailable source
had been configured. Its discovery prompt also differed from the guide.
The earlier capture remains at its original commit.

The before-apply preflight replay used a real published candidate control and
a real unavailable SHA. GitHub returned HTTP 422 for the unavailable source.
The exact prior pin, configuration bytes, protected files and issue, and all
70 package files remained in place. The separate after-apply recovery replay
still covers the resolver failure and restoration.

All eight operation cases passed on replay. Each applicable positive stage
used the exact guide discovery request and reported all three installed
source paths. Removal reported the independently installed upstream source.
The capture verifier accepts the exact file or its exact skill directory,
and the private inventory supplies each individual file identity. The full
installed file set matches the canonical package paths and Git blobs.

Fifteen helper controls cover the original cases and the review corrections.
The new controls reject missing native tool events, an unsupported host,
out-of-cache attribution, missing required package files, and truncated
native relationships. Separate archived-receipt controls reject a missing
preflight and removal of the same path from both manifest maps.

The [reviewed replay builder](transcripts/2026-11-01-issue-24-archive_reviewed_operations.py.txt)
and [preflight probe](transcripts/2026-11-01-issue-24-native_preflight.py.txt)
bind these results to the screened operation receipt.


## Criterion mapping

| Issue #24 criterion | Evidence | Current result |
| --- | --- | --- |
| Repeat install leaves one effective package. Pinned update, rollback, and Backplane-only uninstall prove the actual revisions and preserve upstream. | `L-repeat`, `L-update`, `L-rollback`, `L-uninstall`, and `L-test-restore` record exact active inventory, Git package blobs, restored prior pin, and final upstream load. | PASS in the approved native operation replay |
| Exact guide operations and fresh discovery pass. Failed preflight or verification identifies recovery and retains the last verified installation when restorable. | The eight operation rows include authenticated fresh loads, failed-candidate observations before recovery, and byte-identical prior configuration after both recoveries. | PASS in the approved native operation replay |
| Five conformance checks and authorized native issue-state scenarios are scored for V2. | Exact read-only conformance transcript and all eleven approved #39 native stages, including completion after merged scope and fresh checks. | PASS in the approved native fixture |

The full #24 candidate still requires its own accepted review, exact integrated
package verification, and satisfaction closeout.
