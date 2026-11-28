# Issue #12 OpenCode V2 integrated acceptance

**Result** — UNKNOWN. The 41-row matrix is fixed. The remaining native replays
and exact hosted delivery verification determine integrated acceptance.

## Approved inputs

[Issue #12](https://github.com/tvproductions/superpowers-backplane/issues/12)
was open in `backplane:backlog` at `2026-11-27T08:47:30Z` on fresh native
intake. It is a leaf under #1 and blocks external pilot #6. Both native
blockers, #2 and #24, are closed completed. The shared adapter #20 and setup
owner #23 are also closed completed. The native graph and accepted deliveries
support criterion 1.

The operator approved the [V2-only plan](../../docs/superpowers-backplane/plans/2026-11-28-issue-12-opencode-v2-integrated-acceptance.md)
with the direct response “approved” to the linked draft in this session. The
approved file's SHA-256 is
`81923b92381bac0e17f12a2ac040d34db641c6ea6f4121cceaa04645122417e3`.
The [adoption contract](../../docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md),
[host-leaf design](../../docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md),
and [ADR-0001 edition 1](../../docs/decisions/ADR-0001-001-reference-decisions-through-existing-checkpoints.md)
remain applicable. The earlier dual-host plan and approval receipt retain
their original bytes.

Execution uses the registered detached `.sp-bp/work/issue-12/publication`
worktree at the verified starting commit
`9bf8cba0cf21a7e86b4979f1f6b416dd9e328b5c`. It shares the standalone
repository's Git directory and origin. Exact baseline CI on Windows, macOS,
and Ubuntu is recorded in [run 46095329767](https://github.com/tvproductions/superpowers-backplane/actions/runs/46095329767).

## Matrix reconciliation

The [structured matrix](2026-11-28-issue-12-opencode-v2-acceptance.json) lists
the original source, evidence locator, input identities, and applicability
for each case. It retains 19 observations and identifies 22 for replay.

| Cases | Task 1 disposition | Evidence |
| --- | --- | --- |
| Native setup and V2 2.0.3 refusal | Retain the #23 hosted V2 2.1.4 setup result and the actual 2.0.3 refusal before package loading. The threshold and setup procedure still apply. | [Setup assessment](2026-11-27-issue-23-satisfaction.md) |
| Other setup and failure cases | The archived case matrix uses `386bdb5`. The setup guide and backlog skill differ at the integrated source. Rerun affected cases, including sibling, absent-upstream and dirty adoption. | [Original cases](2026-11-01-issue-23-opencode-acceptance.json) |
| Eight lifecycle operations | Retain the unavailable-SHA preflight at the unchanged guide condition. Replay the other operations for the changed integrated package inputs. The corrected update and rollback observations remain tied to their recorded pins. | [Lifecycle receipt](2026-11-01-issue-24-opencode-acceptance.json) · [Capability replay](2026-11-28-issue-24-capability-replay.json) |
| Five conformance checks | Retain the tested rubrics and native skill results. The adapter and skill tree are unchanged from the conformance source. | [Conformance receipt](2026-11-01-issue-24-opencode-conformance.json) |
| Eleven native issue-state scenarios | Retain the authorized #39 observations. The consumed skills match. PR #40 merged at `00:29:31Z` and the actual completed closure event followed at `00:30:38Z`. The current issue retains only `documentation`. | [Fixture receipt](2026-11-01-issue-24-opencode-native-fixture.json) · [PR #40](https://github.com/tvproductions/superpowers-backplane/pull/40) |

The retained #23 and #24 hosted deliveries, `8e1e200` and `d6f0f6a`,
and the #12 baseline share adapter blob
`c96a668ce427f1f8017894f58e291882c82e171a` and skill tree
`a20788fd467af8c6fb22a7cc00fe9c396e3c1154`. The OpenCode guide changes from
`08a6348ecb3a83eaa91ce65d07e02b0032fd683d` to
`4d3e5597e5961c417c34666e5eff43a53995b1b4`. Its setup section and discovery
request are unchanged. The new maintenance section adds the exact-pin
preflight and post-update or restoration checks. The retained 2.4.2 result
covers inventory and file identity. Fresh supported-host Skill results use
the verified 2.1.4 executable.

## Local baseline gate

The verified worktree exact-synced with `uv sync --locked --all-groups` on
managed Python 3.14.10. The locked check, four pre-commit checks, nine Node
adapter tests, and tracked diff whitespace check passed. Candidate and native
delivery evidence will be recorded against their respective source revisions.
