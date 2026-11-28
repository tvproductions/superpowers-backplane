# Issue #24 OpenCode V2 lifecycle verification

## Task 1 — Native package operations

The [OpenCode V2 guide](../../docs/installing-opencode.md#v2-lifecycle-verification-evidence)
links to the native package operation evidence for [issue #24](https://github.com/tvproductions/superpowers-backplane/issues/24).

The Windows OpenCode V2 2.1.4 replay used independent Superpowers v7.0.1
(`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`), prior Backplane
`386bdb5a8570360f5d34359c68f68947eb7a90fc`, and candidate Backplane
`8e1e2005025890776eb99bd4b9161996fbbe68ed`. All eight native package
cases passed. Fresh native Skill calls verified install, repeat, update,
rollback, recovery after an unavailable source, recovery after a failed
verification, and restoration of the owned test profile. Removal left the
independent Superpowers Skill loadable and both Backplane skills absent.

Issue #24 tracks the full conformance, native issue lifecycle, and exact
integrated-delivery evidence. This record captures the locally verified
package operations and their guide link for documentation fixture #39.
