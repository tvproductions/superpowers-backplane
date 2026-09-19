# Codex native lifecycle — 2026-09-19

Read-only fresh Codex CLI status and selection probe against real issue #3. The issue was OPEN with exactly one lifecycle label, backplane:active, and updatedAt 2026-09-19T19:37:32Z before and after. The full 15-field gh intake succeeded. Parent #1 was open, blocker #2 closed, and issue #3 blocks open #6. The response correctly kept completion open.

The authorized designing, ready, and active transitions are recorded in the issue and prior handoff. Review, blocked, review-reversal, and completed transitions remain separate gates. No issue mutation occurred in this probe.

## Exact prompt

```text
Use managing-superpowers-backlog and every required reference. Read only: do not edit any file, GitHub issue, label, or comment. In tvproductions/superpowers-backplane, inspect the complete native GitHub fields for issue #3 with gh. Report its current lifecycle label, parent and dependency facts, whether it is selected and eligible for continued implementation under the committed plan, and the exact current updatedAt. If a required field or capability is unavailable, say UNKNOWN. Do not infer completion from a commit or an untested install.```

## Exact final response

The raw response had a Markdown hard break (two trailing spaces) after the Plan link; this transcript removes that whitespace for the repository gate.

````text
## Issue #3 status

- **Lifecycle:** `backplane:active` — exactly one lifecycle label.
- **State:** Open.
- **Parent:** Open issue **#1**, “Ship an adoptable Backplane v0.1.0 release.”
- **Sub-issues:** None; #3 is an executable leaf.
- **Blocked by:** Issue **#2**, which is **closed**. No unresolved native blocker is shown.
- **Blocking:** Open issue **#6**, “Run an external adoption pilot and fresh conformance suite.”
- **Linked closing PRs:** None.
- **Issue type:** **UNKNOWN** (`issueType` returned `null`).
- **State reason:** **UNKNOWN** (empty value).
- **Exact `updatedAt`:** `2026-09-19T19:37:32Z`.

## Selection and continuation

- **Selected:** **Yes.** The handoff records human approval of the Codex #3 plan, and the issue has entered active execution.
- **Eligible under the strict intake definition:** **No.** Eligibility specifically requires `backplane:ready`; #3 has already advanced to `backplane:active`.
- **Authorized for continued implementation under the committed plan:** **Yes.** It is an open executable leaf, its required body contract is complete, its design and committed plan are linked, and its only native blocker is closed. The plan revision drift was reconciled through the editorial plan link and execution transition.
- **Complete:** **No.** Task 3 and later gates remain open. Fresh authenticated Codex discovery is **UNKNOWN**, and no linked closing PR or integrated verification evidence exists. Commits and the untested installation do not establish completion.

Plan: [2026-09-19-codex-installation-surface.md](C:/Users/Jeff/source/repos/agents/superpowers-backplane/docs/superpowers/plans/2026-09-19-codex-installation-surface.md)
Current checkpoint: [HANDOFF.md](C:/Users/Jeff/source/repos/agents/superpowers-backplane/HANDOFF.md)

No files or GitHub data were modified.
````

## Disposable native lifecycle issue #13

The approved plan's Task 4, Step 2 uses a disposable issue for transitions that
would misrepresent the real implementation issue. The fixture is
https://github.com/tvproductions/superpowers-backplane/issues/13. Its body
limits scope to lifecycle verification, links the approved design and plan,
and names `documentation` as the unrelated label to preserve.

The first pass used `gh issue view 13 --repo tvproductions/superpowers-backplane
--json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`
before every mutation, and re-fetched after every mutation. Each read returned
all 15 top-level fields, one expected `backplane:*` label, the
`documentation` label, and no native blocker. Two consecutive read-only
intakes left `updatedAt` unchanged.

| Transition | Exact `gh issue edit 13 --repo tvproductions/superpowers-backplane` label flags | Observed labels after |
|---|---|---|
| backlog → designing | `--remove-label backplane:backlog --add-label backplane:designing` | `documentation`, `backplane:designing` |
| designing → ready | `--remove-label backplane:designing --add-label backplane:ready` | `documentation`, `backplane:ready` |
| ready → active | `--remove-label backplane:ready --add-label backplane:active` | `documentation`, `backplane:active` |
| active → blocked | `--remove-label backplane:active --add-label backplane:blocked` | `documentation`, `backplane:blocked` |
| blocked → active | `--remove-label backplane:blocked --add-label backplane:active` | `documentation`, `backplane:active` |

Before blocking, `gh issue comment 13 --repo ... --body` recorded a concrete
fixture pause, `Resume target: backplane:active`, and the release condition:
full blocked-state intake confirms one blocked label and preserves
`documentation`. A second comment recorded that the condition passed, no
native blocker existed, and the active entry gate remained valid. Each comment
changed `updatedAt`; the script re-fetched the complete issue before the
subsequent atomic label edit.

The final native query returned `OPEN`, `documentation`,
`backplane:active`, no native blocker, and
`updatedAt=2026-09-19T22:16:19Z`. Real issue #3 remained `OPEN` with exactly
`backplane:active` and `updatedAt=2026-09-19T19:37:32Z`. Review reversal and
verified closure remain pending. This was a simulated impediment in a named
disposable fixture; it is not a product blocker on issue #3. The fixture
transitions prove the native label mechanics and preservation checks. Its
backlog-to-active path does not replace issue #3's genuine eligibility and
revision-binding evidence.
## Fixture review change request and rework

After commit `6cba46f52a32c67a5179e64ffb5f38409b39c1ff` was pushed, issue #13
moved from `backplane:active` to `backplane:review` in one `gh issue edit` call
after a full 15-field intake and a submission comment. The result was `OPEN`,
`documentation`, `backplane:review`, `updatedAt=2026-09-19T22:21:19Z`.

A fresh read-only reviewer fetched the complete native issue and all three
then-existing comments. It requested evidence for Acceptance Criterion 3. The
exact prompt and final response are below. A review change-request comment
was added at 2026-09-19T22:23:40Z. After another complete intake,
`gh issue edit 13 --repo tvproductions/superpowers-backplane --remove-label
backplane:review --add-label backplane:active` returned `OPEN`,
`documentation`, `backplane:active`,
`updatedAt=2026-09-19T22:23:42Z`. No other label changed. This is fixture
rework; the return to review is still pending at this checkpoint.

### Exact review prompt
````text
Use managing-superpowers-backlog and every required reference. Read only: do not edit files, comments, labels, or any issue. Review disposable verification issue #13 in tvproductions/superpowers-backplane against its own acceptance criteria and the committed evidence in tests/scenarios/transcripts/2026-09-19-codex-native-lifecycle.md. Fetch the complete native issue fields and comments. Decide whether the evidence is ready for verified completion or whether implementation changes are required; name one concrete missing or incorrect item and the exact recovery action. This is a fixture review for Codex issue #3, not a product implementation approval.````

### Exact review final response

````text
## Decision

**Implementation evidence changes are required. Issue #13 is not ready for verified completion.**

The concrete missing item is **Acceptance Criterion 3**: there is no observed or committed `backplane:review → backplane:active → backplane:review` change request and resubmission sequence. The transcript explicitly says review reversal remains pending.

## Current native state

- State: `OPEN`
- Lifecycle: exactly one label, `backplane:review`
- Unrelated label preserved: `documentation`
- `updatedAt`: `2026-09-19T22:21:19Z`
- Parent: none
- Subissues: none
- Blocked by: none
- Blocking: none
- Linked closing PRs: none
- Issue type: `UNKNOWN` (`null`)
- State reason: `UNKNOWN` (empty)
- Comments: three complete comments fetched:
  1. Blocked reason, active resume target, and release condition
  2. Release condition confirmation and active gate revalidation
  3. First pass review submission, explicitly without integration or closure

Acceptance Criteria 1, 2, and the recorded read-only portion of 4 have evidence. Criteria 3 and 5 remain unmet.

## Exact recovery action

On disposable issue #13:

1. Record a concrete review change request.
2. Re-fetch all native fields.
3. Atomically replace `backplane:review` with `backplane:active`, preserving `documentation`.
4. Address the fixture evidence request and run fresh verification.
5. Re-fetch, then atomically replace `backplane:active` with `backplane:review`.
6. Record both transitions and results in [2026-09-19-codex-native-lifecycle.md](C:/Users/Jeff/source/repos/agents/superpowers-backplane/tests/scenarios/transcripts/2026-09-19-codex-native-lifecycle.md).
7. After that evidence is committed and integrated, freshly recheck every acceptance criterion before closing #13 with reason `completed`.

This finding concerns the disposable lifecycle fixture for Codex issue #3. It does not approve or reject the product implementation. No files or GitHub data were modified.
````

## Fixture resubmission result

After the rework record was committed and pushed at
`d83fef826778c6fd3367e09bb2fca42c81362cb7`, fresh
`git diff --check` passed. Complete native intake found issue #13 open with
`documentation` and exactly `backplane:active`, no native blocker, and
`updatedAt=2026-09-19T22:23:42Z`. The resubmission comment was recorded at
2026-09-19T22:25:49Z. After another complete intake,
`gh issue edit 13 --repo tvproductions/superpowers-backplane --remove-label
backplane:active --add-label backplane:review` returned `OPEN`,
`documentation`, exactly `backplane:review`, and
`updatedAt=2026-09-19T22:25:51Z`. Issue #3 remained `OPEN` at exactly
`backplane:active` with unchanged `updatedAt=2026-09-19T19:37:32Z`.

The observed fixture sequence is now `review → active → review`, with a
recorded review change request between the first two states. This completes
the review-reversal mechanics and unrelated-label preservation check. Fixture
closure still waits for the evidence to be integrated and freshly verified.