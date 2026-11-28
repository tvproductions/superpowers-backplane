# Issue #12 OpenCode V2 integrated acceptance

**Result** — SATISFIED for issue #12. All 41 V2 matrix rows passed. The fresh
OpenCode V2 install matched all 110 files in the exact merged package and
completed three attributed native Skill calls.

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
for each case. Task 1 retained 19 observations and identified 22 for replay.

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

## Task 2 native verification

Supported-host replays ran in Windows OpenCode V2 2.1.4 with executable
SHA-256 `b12b0613e9b4a491e5b12d90a5e9bbae6d261fe9688c82bf73125a036963d399`.
Existing native and sibling setup used independent Superpowers v7.0.1 at
`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. The absent-upstream case
installed upstream stable v7.0.2 at `22f0b463e7a5e579904dd6211a520321035526f7`
in its owned profile and completed all three native Skill calls after restart.
The actual V2 2.0.3 negative remains a separately identified refusal.

- **Setup and failures.** Fifteen fresh replay rows passed. Each positive
  replay matched all 109 package blobs and attributed all three Skill results.
  The incompatible, missing-skill, versionless, dirty-update, conflicting
  install, missing GitHub capability, and missing model-authentication cases
  scored their observed refusals. Native issue snapshots and protected files
  matched across the applicable checks.
- **Lifecycle.** All eight operations replayed. The fresh current-main install
  matched 109 files. The lifecycle sequence used exact prior `d6f0f6a` with
  107 files and exact target `9bf8cba` with 109. Update, rollback, and failed
  verification recovery observed the required capabilities using gh 2.106.0.
  Uninstall removed only Backplane and loaded upstream. A separate read-only
  before-apply lookup at `2026-11-28T16:57:36Z` returned HTTP 422 with exit 1.
  The configuration SHA-256 stayed
  `12bcaf826c2f007fe0de826186541c6b819f322a5358fa2ab03f21426a5d881d`
  and the complete issue intake matched. The after-apply probes changed the
  owned configuration to exercise a resolver failure and a missing required
  Skill result, then restored the recorded package and configuration. A fresh
  recovery-only replay verified the prior pin, gh capabilities, and complete
  native state before and after both restorations. Each restored package
  matched 107 files and completed all three Skill calls.

The first replay stopped when the copied lifecycle harness rejected #12 under
its original #24-only issue assertion. The next profile passed. The sibling
setup initially failed scoring under a historical 70-file constant. Comparing
the actual installed set with the selected Git manifest resolved the scorer
failure without altering the capture. The old-gh intake capture reported its
actual rejected field and recovery action in a table. One focused control
failed before correcting the scorer's table handling. Both refusal controls
and the 46 existing helper tests passed afterward.

The [execution source](transcripts/2026-11-28-issue-12-replay.py.txt),
[copied-helper changes](transcripts/2026-11-28-issue-12-reused-helper-changes.diff.txt),
[matrix builder](transcripts/2026-11-28-issue-12-build_matrix.py.txt),
[screened receipt builder](transcripts/2026-11-28-issue-12-record_replays.py.txt),
[refusal controls](transcripts/2026-11-28-issue-12-test_refusal_receipt.py.txt),
and [review controls](transcripts/2026-11-28-issue-12-test_replay_evidence.py.txt)
identify the procedures. The copied-helper changes record the precise
substitutions to the archived #23/#24 inputs. Raw captures remain in owned
ignored fixtures and their screened observations are recorded in the matrix.

The candidate changes the README and guide introduction to reflect the V2
support scope and link the accepted source revisions. The setup/discovery
prompts, refusal threshold, maintenance commands, adapter and skills match
the replay inputs. The structured matrix records all 110 expected package
paths and Git blobs at local source `622bce7df4ba84c83cf75a67e0b1dcd2655d10f2`.
The 109-file tested package differs only in the README, guide introduction,
and approved plan. Task 3 checks the exact hosted installation against its
own Git manifest. Issue #4 owns the separate adopter-operations guide follow-up.

## Independent review

Fresh review of `9bf8cba..622bce7` found four Important gaps. The corrected
evidence stores the exact candidate manifest and a separate before-apply
receipt. Both recovery cases were replayed with prior-pin checks before
restoration and fresh discovery and capabilities afterward. The projection
reruns the owning scoped verifiers, checks reported Skill blobs and the
required maintenance results, and checks retained plan authority and fixture
ordering. The altered Skill blob reproduced the earlier gap with a failing
assertion. The corrected verifier rejected that altered blob, missing approval,
completion before integration, and missing capability evidence.

## Local engineering verification

The registered worktree ran the [canonical gate](../../docs/engineering/python.md#canonical-commands).
Managed Python 3.14.10, uv 0.13.10, Ruff 0.17.5 and ty 0.0.104 were directly
observed. The five repository unittests, four hooks, nine Node adapter checks
and whitespace checks passed. The five added scratch helpers passed locked
Ruff lint and format, ty with the explicit scratch import path, and Lizard's
20-complexity ceiling. All 54 scoped controls passed with deprecation warnings
treated as errors.

| Acceptance rows | Result and evidence |
| --- | --- |
| A01, A04, A05 | Verified registered workspace and locked project configuration. Actual managed Python and tool selections are identified above. |
| A06, A07, A08, A10, A17 | Retained the unchanged [accepted engineering baseline](2026-11-07-strict-astral-full-verification.md). Exact all-group sync, lock check, lint, format, type checking and test commands passed in this worktree. |
| A09 | All four local hooks passed. Exact merged CI passed on Windows, macOS, and Ubuntu. |
| A18 | Scoped deprecation check, Lizard, 54 receipt controls and guide verification passed. The whole-change review identified four evidence gaps and the corrected replay and verifier addressed them. |
| A02, A03, A11–A16 | N/A for the shipped Node adapter and Markdown skills. This non-package Python development scope delivers fixture and receipt tools, with no wheel, runtime API, private resolution, workspace or deployment target. |

## Integrated delivery and satisfaction

[PR #42](https://github.com/tvproductions/superpowers-backplane/pull/42) merged
reviewed head `73be83a6ecf7ee097c187e87f0758edc86165299` as
`3b03a49db79b6a276314d1477dfb3c68e1a4bac9` at
`2026-11-28T20:22:56Z`. The merged tree
`0d064bcf719725d9e10bcccafc43e77970bc6d36` exactly matches the reviewed tree.
[Exact merged CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46186109415)
passed on Windows, macOS, and Ubuntu. The complete locked local gate also
passed from a clean worktree at the merge commit. A09 includes exact-delivery
hosted verification.

The [fresh installed-package receipt](2026-11-28-issue-12-opencode-v2-integrated-delivery.json)
records Windows OpenCode V2 2.1.4 and separately resolved Superpowers v7.0.1.
All 110 installed package blobs matched the exact merged Git tree and the
reviewed package manifest. Native Skill calls completed for
`using-superpowers`, `managing-superpowers-backlog`, and
`managing-superpowers-handoffs`, with attributable sources in the independent
upstream and Backplane installations. The existing unrelated plugin and
fixture user files matched across the installation. Complete native issue
intake, the repository ref set, both project workspace statuses, and the
upstream checkout identity also matched. GitHub CLI 2.106.0 verified
authentication, the exact hosted revision, label edit flags, and completed
closure support before and after installation.

The evaluated issue revision was `2026-11-28T20:22:14Z`, with
`backplane:review`. The approved plan pointer and lifecycle transitions
changed the revision. Its original objective, scope, criteria, verification
seams, and native graph still govern the evaluation.

| Issue #12 criterion | Accepted evidence |
| --- | --- |
| Completed prerequisites and canonical V2 configuration | Fresh reads show #20, #23, and #24 closed completed. The reviewed adapter and exact hosted installation use V2 `plugins`. |
| Every mandatory supported-host row passes | The matrix records all 41 results, exact inputs and scoped native observations, with explicit applicability for refusal and removal cases. |
| Integrated setup, lifecycle, conformance, and authorized native issue-state checks | The product tree is identical to the reviewed candidate. The exact hosted installation passed. Changed setup and lifecycle seams were replayed, the five conformance checks passed, and the eleven authorized #39 states preserve their native evidence and verified completion ordering. |
| Actual below-floor refusal, fresh independent discovery, and preservation | The recorded V2 2.0.3 executable refused before package load. The merged package proved three source-attributed native Skill results, complete exact-manifest equality, and preservation. |

These observations cover the issue's comparison, fresh native behavior and
preservation, and platform/source identification verification seams. The
[hosted verification driver](transcripts/2026-11-28-issue-12-verify_hosted.py.txt)
and the receipt identify the tested merge independently of the later evidence
storage revision. Receipt SHA-256 is
`82568b7435f1af62ec0b26530d9d2265dc17cc59415d1081260bd1c1d86ccfaa`.
