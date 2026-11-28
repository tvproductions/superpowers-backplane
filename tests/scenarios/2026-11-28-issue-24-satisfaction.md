# Issue #24 OpenCode V2 lifecycle satisfaction

**SATISFIED** for the current criteria of [issue #24](https://github.com/tvproductions/superpowers-backplane/issues/24)
as observed in review at `2026-11-28T01:40:19Z`. Setup prerequisite #23 was
closed completed with its accepted V2 evidence.

The approved lifecycle plan uses blob `882b389bf49ced3e7de517a4146cfd822e9c29e5`,
the shared probe contract uses `1b856ff783c9cfd88d0e06184be894f16651898b`, and the
operator approval receipt uses `351746621c2dccf28ab9a7840dd587f5a64821dd`. The
plan consumed issue revision `2026-09-20T01:30:23Z`. The issue's V2 criteria
remained unchanged through submission and review. [Approved artifacts](../../docs/superpowers-backplane/plans/2026-11-01-opencode-wrap-approval.json)

[PR #41](https://github.com/tvproductions/superpowers-backplane/pull/41)
merged reviewed head `8b78f22f8d92772b3a0b798f413e1993d8f23214` onto
`aa6de36b092c486ca8ab07372905352af085a4b7` as delivery
`d6f0f6a378b4b91e2fab2c2987f8f18dd357f23d`, tree
`98abfe4ee0ddb4d142579876c4df77df70d75ee7`. Both the branch and PR passed CI on
Ubuntu, macOS, and Windows before merge. [Exact delivery CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46094332153)
passed on the same three platforms. The PR used a neutral reference to #24.

| Current acceptance criterion | Evidence | Result |
| --- | --- | --- |
| Repeat installation leaves one effective Backplane entry. Update reaches its chosen revision, rollback restores the prior revision, and uninstall removes only Backplane. | Eight native operation rows recorded the exact active revisions, full package manifests, independent Superpowers, before-and-after protected snapshots, and fresh Skill loads. The corrected guide replay matched 105 updated and 70 restored files with all three Skill loads and before-and-after `gh` capability checks. | SATISFIED |
| Exact V2 guide and fresh discovery checks pass. Failed preflight and verification retain or recover the last verified installation with a concrete action. | The unavailable SHA failed before apply and preserved configuration and the prior package. Separate after-apply resolver failure and denied native Skill observations captured the failure before repair and proved restoration. The hardened receipt verifier rejected eight altered observations and the original receipt passed all eight native rows and the preflight. | SATISFIED |
| Five conformance checks and authorized native lifecycle scenarios pass. | The read-only conformance record scores five checks and 23 behavioral rubric assertions. All eleven authorized #39 stages retain the actual native before-and-after states, preserve the `documentation` label, and verify completed closure after its separately accepted PR #40 integration. | SATISFIED |

The [lifecycle assessment](2026-11-01-issue-24-opencode-acceptance.md) records the
review corrections and links the scored receipts and native fixture evidence.

## Exact hosted delivery verification

A fresh owned Windows profile installed the hosted Git package at the delivery
SHA. The OpenCode V2 2.1.4 executable matched SHA-256
`b12b0613e9b4a491e5b12d90a5e9bbae6d261fe9688c82bf73125a036963d399`.
The independent Superpowers v7.0.1 package resolved to
`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. The native package inventory showed
one active Backplane entry after installation and its complete 107-file
manifest matched the merged Git tree. A fresh authenticated session used the
exact guide prompt and completed `using-superpowers`,
`managing-superpowers-backlog`, and `managing-superpowers-handoffs` from their
respective installed sources. The user files, unrelated native plugin,
upstream source, and complete issue snapshot matched across installation.

The [screened integrated receipt](2026-11-28-issue-24-integrated-delivery.json)
has SHA-256 `204f9fd7d35bda444f158958ebcc52fee809a6c7008567a1dfc5942b854b3cb4`.
The [verification driver](transcripts/2026-11-28-issue-24-verify_hosted24.py.txt)
derives package files from Git and requires actual native Skill results. This
assessment records the tested delivery, while the later evidence commit records
its storage. Integrated V2 acceptance proceeds under #12.
