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
