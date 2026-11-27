# Issue #23 OpenCode V2 setup acceptance

This is the local Task 2 assessment for [issue #23](https://github.com/tvproductions/superpowers-backplane/issues/23), observed open and active at 2026-11-27T19:40:02Z. The issue is a leaf under #1, its sole prerequisite #20 is completed, and #23 blocks #24. The selected scope is V2 setup and compatibility failures.

The Windows worktree is c191 with the standalone repository's shared Git directory. The starting branch HEAD was 2ece74191b831f410a4ba4750f97165b220dd143, which stores the Task 1 handoff. The [approved plan](../../docs/superpowers-backplane/plans/2026-11-01-issue-23-opencode-v2-setup.md), [probe contract](../../docs/superpowers-backplane/plans/2026-11-01-opencode-remaining-acceptance-probe-contract.md), and [approval receipt](../../docs/superpowers-backplane/plans/2026-11-01-opencode-wrap-approval.json) retain their original blobs. ADR-0001 edition 1 continues to govern. This task uses the existing adapter and evidence model.

## Local result

17 of 17 mandatory setup and failure rows passed in the local Windows V2 fixture.

| Case | Result | What the probe exercised |
| --- | --- | --- |
| S-native | PASS | Existing authoritative native Superpowers package retained. |
| S-sibling | PASS | Existing independent checkout retained and Skill attributed to its path. |
| S-absent | PASS | Stable package added to the owned config and loaded after restart. |
| F-lookalike | PASS | Refusal of a clean private fixture with a lookalike Git origin. |
| F-versionless | PASS | Refusal with absent observable origin and revision. |
| F-duplicate | PASS | Conflicting configured Backplane package sources identified. |
| F-dirty-adopt | PASS | Compatible dirty upstream adopted read-only with its local work intact. |
| F-dirty-update | PASS | Update refused and uncommitted checkout contents preserved. |
| F-collision | PASS | Occupied local path and its user file preserved. |
| F-gh-auth | PASS | Native GitHub CLI with an empty isolated auth configuration. |
| F-gh-intake | PASS | Actual older GitHub CLI rejected a required native intake field. |
| F-gh-label | PASS | Actual older GitHub CLI lacked the native edit command. |
| F-gh-close | PASS | Actual older GitHub CLI lacked the native reason flag. |
| F-missing-skill | PASS | Required upstream bootstrap Skill missing from an independently owned checkout. |
| F-incompatible | PASS | Authoritative older release lacks the V2 entry point. |
| F-below-floor | PASS | Actual V2 2.0.3 refused by the acceptance guard before package loading. |
| F-unauthenticated | PASS | Fresh isolated V2 profile had no OpenAI sign-in and could not run the requested model. |

The [structured receipt](2026-11-01-issue-23-opencode-acceptance.json) records the complete issue fields, exact command vectors, fresh Skill call and session IDs, sources and Git blobs, scoped before/after hashes, and screened refusal excerpts. Full streams and isolated credentials remain in their owned local profiles.

## Native evidence and controls

- Each supported setup mode ran the V2 guide's setup request, then ran its Skill discovery request in a fresh session. The native and sibling modes used Superpowers v7.0.1 at 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b. The absent mode installed the separately pinned stable v7.0.2 at 22f0b463e7a5e579904dd6211a520321035526f7, then restarted the owned server. The Backplane package was the approved #20 delivery at 386bdb5a8570360f5d34359c68f68947eb7a90fc. Hosted verification of a later issue #23 delivery is a separate gate.
- Preflight verified the OpenCode V2 2.1.4 executable and hash, private loopback, and the retained isolated OpenAI session with openai/gpt-6.1-sol. The driver uses the build's documented run --server option to address the same isolated server whose inventory has completed. The child-only data pointer reuses previously authorized native auth. Other profile roots, including ProgramData and temporary directories, are issue-owned. No credentials were copied.
- A native unrelated plugin registered its own Skill and stayed configured beside the package under test. The fixture tracked its package and Skill files and unrelated user bytes. Setup permissions allowed the exact read-only GitHub commands, including the edit and close help probes. The absent case allowed the single owned configuration edit. Native issue snapshots contain all 15 required fields.
- The below-floor probe used the actual Windows executable from [OpenCode 2.0.3 on npm](https://registry.npmjs.org/@opencode%2fcli-windows-x64/2.0.3), verified against its distribution integrity digest. Its reported version was opencode v2.0.3. The Backplane acceptance guard refused before package loading, preserved a nonempty unrelated configuration, and left the package cache empty. Earlier native version output included the opencode v prefix, which the guard already recognizes.
- The older GitHub CLI binaries came from official releases with matching archive checksums. Version 2.40.1 could authenticate and rejected required native JSON fields. Version 1.0.0 lacked the edit command. Version 1.14.0 lacked the closure-reason flag. The two oldest binaries also could not authenticate against the retained profile. Separate native command/help probes established the label and reason gaps independently.
- The first authenticated OpenCode 2.1.4 run completed three Skill calls but the parser rejected them because it expected callID. The red test reproduced the discrepancy between native part.id and the distinct message partID. The correction passed the regression and recovered all three verified source paths from the original raw capture. A separate red/green control keeps upstream identity absent in the versionless and below-floor refusals while retaining UNKNOWN for missing identity in other cases.
- Initial positive attempts kept the unrelated plugin's failure visible. Its test Skill was missing a required path, so it was disabled. A corrected sentinel with an owned Skill file activated. The next attempt recovered three native Skill loads for both adoption modes but restricted public contract reads too tightly. The final setup replay allowed those reads and used disposable consumer repositories to prevent ancestor project instructions from affecting results. The Windows blob checks stream actual bytes to Git to handle deep installed paths.

- The independent whole-branch review found missing post-failure native observations, insufficient recovery evidence, and verifier and replay gaps in the provisional candidate. The revised refusal runs capture both native plugin inventories and package-tree hashes before any recovery. The revised verifier requires the exact 17 unique cases, host version bound to a measured binary hash, attributable Skill paths and blobs, and case-specific observations. Two focused controls reproduced the incomplete-matrix and missing-Skill-attribution problems before the fix.
- For unauthenticated OpenCode, the native host emitted a provider route error for the requested model. The replay runner retained that error and reported the recovery guidance from the existing installation guide, with its source recorded separately. The below-floor guard emitted its own supported-version recovery. Both cases replayed through the approved case entry point.

## Acceptance criteria and seams

| Issue requirement | Local evidence |
| --- | --- |
| Each supported upstream mode completes setup and discovers separate upstream and Backplane skills | S-native, S-sibling and S-absent contain two native sessions per case, the three terminal Skill results, and the accepted package's installed file comparisons. |
| A real V2 release below 2.0.4 is refused and unobservable provenance remains unknown | F-below-floor records the real 2.0.3 executable and before/after guard observations. F-versionless records a refused setup with absent upstream origin and revision. |
| Failure reports identify the failed check and recovery while preserving existing state | F-* rows record actual fixture conditions, the exact diagnostic or screened report, and the original and preserved snapshot identities. The dirty adoption and dirty update probes exercise separate actions. |
| Native issue intake, CLI capability, replay, and preservation seams | The receipt retains the full issue snapshot and relationship counts, authenticated setup and independent fresh Skill calls, private native inventory sources, installed blob comparisons, and exact failure-preservation checks. |

The [native case runner](transcripts/2026-11-01-issue-23-v2_cases.py.txt), [receipt builder](transcripts/2026-11-01-issue-23-task2_receipt.py.txt), [scorer](transcripts/2026-11-01-issue-23-acceptance.py.txt), and [regression tests](transcripts/2026-11-01-issue-23-test_acceptance.py.txt) are archived from the owned scratch. Replay through the locked uv project from the verified worktree and keep whole native streams ignored. The documented positive adjudication uses the fresh model session and independent native package and preservation evidence.

The case entry point is available after restoring the four archived Python helpers in the verified issue scratch directory and running the native package preflight. Choose a new attempt number for each replay. The Windows profile can be supplied through SP_BP_ISSUE23_AUTH_PROFILE when the original owned path differs.

```text
uv run --locked python .sp-bp/work/issue-23/acceptance.py run --case F-below-floor --attempt 6
uv run --locked python .sp-bp/work/issue-23/acceptance.py verify tests/scenarios/2026-11-01-issue-23-opencode-acceptance.json
```

Task 2 concerns setup and compatibility. Native lifecycle qualification in #24 and integrated acceptance in #12 remain separate. Issue #23 remains active at the recorded revision. Hosted verification, integration and issue closure have separate evidence gates.
