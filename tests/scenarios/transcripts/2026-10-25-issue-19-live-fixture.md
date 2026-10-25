# Issue 19 live documentation-fixture observations

Operator-approved fixture: https://github.com/tvproductions/superpowers-backplane/issues/34. All cases below are actual fresh Claude sessions with gh restricted to this issue. Before/after snapshots are complete native intake. Local branch/verification claims in model responses remain attributed; the executor's source checks are separately retained. Resume, publication, integration and verified closure are pending, not PASS.

## status

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T16:50:27Z; re-read and reconcile any drift before mutation. Perform only status assessment for #34. Selection alone changes no lifecycle label. Report covered/eligible/selected separately, with no invented priority or approval. The issue-body design and exact paragraph were approved by the operator; the fixture plan is not yet bound. No mutation is authorized in this read-only probe.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01L4hAWwNAJ8dbq8i7xRxhzU",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Read issue 34 status fields from GitHub"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01V1GCcg3cCAUTXdTkUTdjg1",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01JedBS3Kf7XVvMCj1WCZUBQ",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

I used `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog`, and read the skill's native issue contract. This was a status check only. I ran the one `gh issue view 34` command you specified and changed nothing: no GitHub, local file, Git or plugin writes.

## Issue #34: status

**Revision:** `updatedAt` is `2026-10-25T16:50:27Z`, which matches the revision you expected, so nothing has drifted. I made no changes, so I didn't need a second read.

**What GitHub shows:**
- **Title:** "Clarify hosted update verification in the Claude installation guide"
- **Link:** https://github.com/tvproductions/superpowers-backplane/issues/34
- **State:** OPEN, with no close reason set.
- **Labels:** `documentation` and `backplane:backlog`. That is exactly one Backplane lifecycle label, which is valid, and the `documentation` label is unaffected.
- **Hierarchy:** no parent and no sub-issues, so it is a single standalone task.
- **Dependencies:** nothing blocks it and it blocks nothing.
- **Issue type:** none set.
- **Closing pull requests:** none.

**Issue description against the contract:** all seven required headings are present. Acceptance Criteria lists outcomes you can observe, and Verification Seams names the evidence (byte comparison, checks against #19 B/F, intake captures, PowerShell parsing, `git diff --check`). The Superpowers Artifacts section states two things:
- The design authority is the issue description, "subject to operator approval before readiness". You say you have approved it, but no approval is recorded on the issue itself. I didn't read the comments because the contract only requires them when approval evidence is needed for a decision, and this check made none.
- The plan is "to be bound… before readiness". It is not bound, which matches what you said.

## Covered, eligible, selected

| Status | Result | Basis |
|---|---|---|
| **Covered** | Not established | There is no parent issue, and the description has no Backplane Record, Obligation Dispositions or Coverage and Satisfaction sections. No parent issue maps it, so its coverage is UNKNOWN. That is different from being judged uncovered. |
| **Eligible** | **No** | Of the six eligibility conditions, open-leaf, complete-contract and no-blockers are met. Three are not: (a) the lifecycle label is `backplane:backlog`, not `backplane:ready`; (b) no current approved plan uses this revision; (c) design approval is not recorded on the issue. |
| **Selected** | **No** | Nothing was selected, and selecting an issue would not change its label anyway. |
| **Recommended by project policy** | None | There is no priority policy, so I haven't invented a priority or a recommendation. |
| **Complete** | No | The issue is open and nothing has been integrated. |

## Next lifecycle step (not taken)

The allowed path is `backlog → designing → ready`. Moving to `ready` needs a recorded design approval and a plan bound to this issue's link and its `updatedAt` value. Any later change to labels would need your separate authorization and a fresh read of the issue right before it.

## selection

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T16:50:27Z; re-read and reconcile any drift before mutation. Perform only selection assessment for #34. Selection alone changes no lifecycle label. Report covered/eligible/selected separately, with no invented priority or approval. The issue-body design and exact paragraph were approved by the operator; the fixture plan is not yet bound. No mutation is authorized in this read-only probe.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01NZKMt6SfDcm4hz7BoLcDzj",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "View issue 34 details as JSON"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01Wnp69JvavDC5Ec6vdtZ1wM",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01CRiBczEsw7YoTq1vhXW1Yb",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_0154HaXsyyTXrS8J9JjZncS1",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01V6E83qtMd4KKhkrAzPMj3F",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\product-decomposition.md"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

I used the backlog skill to run a read-only selection assessment of #34. The issue isn't eligible, so I didn't select it. Nothing was changed.

**What I read.** I ran the exact `gh issue view 34 …` command you gave, once. I also read the skill's issue contract, plan-binding and product-decomposition references. I made no other gh calls and touched no local files, Git state, plugins or other issues.

**Drift check.** The issue's last update is `2026-10-25T16:50:27Z`, which matches the revision you expected, so there was no drift to reconcile. I didn't re-read before reporting, because that re-read is only required before a mutation.

**Current state of #34**
- It is open, has no parent and no sub-issues, and has no blockers in either direction. No pull requests are linked, and `issueType` is not set.
- Labels: `documentation` and `backplane:backlog`. That is exactly one lifecycle label, which is valid.
- All the required body headings are present: Objective, Bounded Scope (Allowed and Out of Scope), Acceptance Criteria, Verification Seams, and Superpowers Artifacts.

## Covered
**Not established; it is only captured.**
- Coverage means mapping the issue to parent obligations. #34 has no parent, and its body has none of the sections that record coverage (Backplane Record, Obligation Dispositions, Coverage and Satisfaction).
- The body mentions #19 in text, but there is no actual GitHub link between the two issues, and I didn't infer one.
- No accepted evaluation exists, so whether the acceptance criteria are met is **UNKNOWN**.

## Eligible
**No.** The six eligibility checks:

| # | Check | Result |
|---|---|---|
| 1 | Open and an executable leaf | Pass |
| 2 | Body meets the contract | Pass on headings and bounded scope |
| 3 | Design approved | Stated in your prompt, not recorded on the issue. The body still reads "subject to operator approval before readiness". |
| 4 | A current plan uses this revision | **Fail.** The body says the plan is "to be bound", and you confirmed it isn't bound yet. |
| 5 | Blockers resolved | Pass (there are none) |
| 6 | Carries `backplane:ready` | **Fail.** It is `backplane:backlog`. |

## Selected
**No.** The issue fails checks 4 and 6, so it can't be selected, and I didn't select it. Selection on its own wouldn't change a label anyway, and none was changed.

**Priority and recommendation:** none. No project priority policy was given, and I haven't treated #34 as ranked or approved beyond what you stated.

**Next steps, all outside this probe and each needing your authorization:**
1. Move the issue from `backlog` to `designing`.
2. Bind the fixture plan to the issue URL and the current revision, and record the design approval.
3. Move it from `designing` to `ready`.

After that, re-read the issue and run selection again.

## designing

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T16:50:27Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is backlog to designing, for this evidence: The operator approved this exact useful documentation issue and paragraph. The bounded fixture plan is being bound to actual issue 34 under approved issue 19 recovery Task 4. Design preparation has begun; no readiness or publication is claimed.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:backlog --add-label backplane:designing. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01HjEzY3ktXtVTVyZJe5CzJm",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_017LQLqpwaa9twThES7cW5tq",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Fetch complete native state of issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01HLapfEFEG2mGUeWCGW4bwp",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01BM5eurynWeXPkZ8gRYQqod",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012C5uW9KPgvkc254yqJW3yc",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:backlog --add-label backplane:designing",
      "description": "Move issue 34 from backlog to designing"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01TinEkqLnMtWB2tAkYcPfqm",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body \"Lifecycle transition: backplane:backlog -> backplane:designing. Evidence: The operator approved this exact useful documentation issue and paragraph. The bounded fixture plan is being bound to actual issue 34 under approved issue 19 recovery Task 4. Design preparation has begun; no readiness or publication is claimed. Reconciliation: pre-mutation intake matched expected revision updatedAt 2026-10-25T16:50:27Z (no drift); exactly one Backplane label (backplane:backlog) present; unrelated label documentation preserved; no parent, sub-issues, blockers, blocking or closing PRs. Not claimed: approved plan, readiness, integration, verification or closure.\"",
      "description": "Post transition evidence comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01UqbVP5Z5cTK5pR7L9SZP5g",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue 34 has moved from `backplane:backlog` to `backplane:designing`, and a fresh fetch afterwards confirms the change.

**Checks before the change** (I used the installed `superpowers:using-superpowers` and `superpowers-backplane:managing-superpowers-backlog` skills and read their issue-contract and Superpowers-binding references):
- `updatedAt` was `2026-10-25T16:50:27Z`, the revision you expected, so there was no drift to reconcile.
- The issue was open with exactly one Backplane label (`backplane:backlog`) alongside the unrelated `documentation` label.
- The issue body has every required section: Objective, Bounded Scope (Allowed and Out of Scope), Acceptance Criteria, Verification Seams, and Superpowers Artifacts.
- It has no parent, sub-issues, blockers, blocking links or closing PRs.
- Moving from backlog to designing only requires evidence that design work has started, and your evidence supplies that.

**Changes:**
1. I ran `gh issue edit 34 … --remove-label backplane:backlog --add-label backplane:designing` as one command.
2. I posted an evidence comment: https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400484025. It quotes your evidence, records the expected revision and that it matched, notes that the `documentation` label and the empty relationships were kept, and states that the plan is not approved and that readiness, integration, verification and closure are not claimed.

**State after the change:**
- Labels are `documentation` and `backplane:designing`. That is exactly one Backplane label, and the unrelated label has the same ID as before.
- The body and all relationships are unchanged, and the issue is still open.
- The new `updatedAt` is `2026-10-25T16:57:43Z`. Use it as the revision to check against before the next change.

I made no other GitHub calls and did not touch local files, Git state, plugins or any other issue. I did not run `gh label list` because only the listed `gh` calls were allowed. The edit going through, and the label showing up with a matching description, shows that `backplane:designing` already exists in the repository.

## ready

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T16:59:23Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is designing to ready, for this evidence: The issue body now records the operator's explicit approval of this exact fixture and paragraph and the already approved issue 19 recovery Task 4. The reviewed bound plan exists at docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md in the current local fixture branch. Read that plan before deciding readiness. It consumes semantic revision 2026-10-25T16:50:27Z; later changes are only lifecycle/comment/artifact availability, not scope or acceptance. Reconcile this drift explicitly. There are no native blockers. Publication remains separately gated. The independent draft review asks for a content-comparison correction within this existing approved design; do not claim that correction is already implemented.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:designing --add-label backplane:ready. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_013oRzybcUcmncg655k4hpat",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "View issue 34 with native fields"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01LsXfAT9ePmAcGeQ8VLAyvQ",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_017rECaFzyTpadtcYw9EBbPU",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_0166rCsjsWqLGnGtrnZqcRwh",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01U9pYter7CE4kekpAZcj7kF",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\neutral\\docs\\superpowers-backplane\\plans\\2026-10-25-issue-19-lifecycle-fixture.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01ErCR6hVqgaQcrWfB3jRZCE",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\docs\\superpowers-backplane\\plans\\2026-10-25-issue-19-lifecycle-fixture.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_013CytaSv5u7dQstdNZFa2E6",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --comments",
      "description": "Read issue 34 comments to classify revision drift"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01LWkkRKYPVn7kqKZjE96rGx",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-read issue 34 before label transition"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_014KbGN69yDoPzXdeJRYpaJ5",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:designing --add-label backplane:ready",
      "description": "Move issue 34 from designing to ready"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012f1U4ysL1GvgEw4yYsaCo5",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body \"Lifecycle transition: backplane:designing -> backplane:ready. Evidence: the issue body records the operator's explicit approval of this exact fixture body and paragraph, and the already approved issue 19 recovery Task 4 as design authority. The bound plan docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md was read from the local fixture branch test/issue-19-doc-lifecycle (commit 33d4300 per the issue record; the blob hash was not independently recomputed in this session). It records the issue URL, consumed revision 2026-10-25T16:50:27Z, design authority, the acceptance criteria and verification seams as constraints, and the exact checks. No native blockers, parent, sub-issues or closing PRs. Reconciliation: the drift from 2026-10-25T16:50:27Z to 2026-10-25T16:59:23Z consists only of the backlog->designing label change, its comment and the Superpowers Artifacts plan/approval record. Objective, scope, acceptance and the native graph are unchanged, so this is editorial and already covered. The pre-mutation re-read matched 16:59:23Z with exactly one Backplane label; documentation preserved. Pending: the independent draft review requests a content-comparison correction within this approved design (installed version/hash recording vs. comparison with the selected immutable source). That correction is NOT yet implemented. Not claimed: execution start, implementation, publication, integration, verification or closure. Publication remains separately gated.\"",
      "description": "Record readiness evidence comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01DW85FBjGJMPN9SPEq6F88X",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue #34 has moved from `backplane:designing` to `backplane:ready`, and the re-fetched issue confirms it.

**What I checked before the change:**
- **Issue body:** all the required sections are present, and it records your explicit approval of this fixture and paragraph, plus issue #19 recovery Task 4, as the design authority.
- **Plan:** I read `docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md` from the repository root, not the `neutral` working directory. It names the issue URL, consumes revision `2026-10-25T16:50:27Z`, and lists the design authority, the acceptance criteria and verification seams as constraints, and the exact checks. Its review notes already cover the content-comparison point, so the reviewer's requested correction stays within the approved design.
- **Revision drift:** the issue moved from 16:50:27Z to 16:59:23Z. The only changes in that window were the backlog→designing label move, its comment, and the plan/approval note in the Superpowers Artifacts section. The objective, scope, acceptance criteria and relationships did not change, so I treated the drift as editorial.
- **Blockers and labels:** no native blockers, parent, sub-issues or closing PRs. There was exactly one `backplane:*` label before the change, and the re-read just before the edit still matched 16:59:23Z.

**After the change:**
- The open issue has two labels: `documentation`, unchanged, and `backplane:ready` as the only Backplane label.
- The body, the empty relationships and the absence of closing PRs are unchanged. The issue now shows `updatedAt` `2026-10-25T17:00:08Z`.
- The evidence comment is posted: https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400508796. It says the content-comparison correction is **not** implemented yet, and that publication still needs your separate approval.

**Caveats:**
- I couldn't independently check the plan's commit `33d4300` or blob `6b33d68…`, because only `gh` commands were allowed. The commit identity comes from the issue record and the starting git status, and the comment says the hash wasn't recomputed.
- I ran the comment and the final re-fetch at the same time. The re-fetch confirms the label and relationship state; the comment's URL was returned when it posted.

I changed no local files, Git state, plugins or other issues.

## active

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T17:00:08Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is ready to active, for this evidence: All readiness gates were verified in the prior fresh session. The exact approved paragraph task now begins on test/issue-19-doc-lifecycle, with its reviewed plan committed at 33d4300ade509061358effdd6e571356eb94af39. The draft review's real content-comparison correction remains outstanding within the approved design; no clean review or publication is claimed.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:ready --add-label backplane:active. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01Toxy9XkXy77Lx9oRo6ZEig",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "View issue 34 with native relationship fields"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_019yKhdDSTz8hj3DxVG479f3",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01Wi17HesfeRW7TX6HXKSzaR",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01RmT8HYdH1CKCuAkKfnyKX5",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01GQuW6GiGaEap1kKBPM9XYa",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\docs\\superpowers-backplane\\plans\\2026-10-25-issue-19-lifecycle-fixture.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01LKXRccEZ7jxredj3rPWH2f",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-read issue 34 immediately before mutation"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01DteQzvemrEUoaQRwMKaVjw",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:ready --add-label backplane:active",
      "description": "Move issue 34 from ready to active"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_015bS715KSUUdd83SmtaSzV9",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body \"Lifecycle transition: backplane:ready -> backplane:active.\n\nEvidence: All readiness gates were verified in the prior fresh session. The exact approved paragraph task now begins on test/issue-19-doc-lifecycle, with its reviewed plan committed at 33d4300ade509061358effdd6e571356eb94af39. The draft review's real content-comparison correction remains outstanding within the approved design; no clean review or publication is claimed.\n\nReconciliation: Pre-mutation re-read at updatedAt 2026-10-25T17:00:08Z (matched expected). Open leaf; no parent, sub-issues, blockedBy or blocking; exactly one Backplane label (backplane:ready) plus unrelated documentation. Plan docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md binds this issue and consumes semantic revision 2026-10-25T16:50:27Z; the later change is editorial (lifecycle/comment/artifact-link) with objective, scope, acceptance and native graph unchanged. Body and relationships preserved; documentation label retained.\"",
      "description": "Post evidence and reconciliation comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012W3bbdk3cZgyVSHFCqV9Ga",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify the transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue #34 has moved from `backplane:ready` to `backplane:active`, and a fresh read of the issue confirms it.

**Checks before the change:**
- **Revision:** the first read and the re-read just before the edit both showed `updatedAt` `2026-10-25T17:00:08Z`, which matches what you expected. Nothing changed between the two reads.
- **Readiness:** the issue is open and has no parent, sub-issues or blockers in either direction. Its body has every section the issue contract requires (`references/github-issue-contract.md`). It had exactly one Backplane label, `backplane:ready`, plus `documentation`.
- **Plan:** `docs/superpowers-backplane/plans/2026-10-25-issue-19-lifecycle-fixture.md` exists in the local repo. It names #34, the issue body as design authority, and revision `2026-10-25T16:50:27Z`.
- **Revision gap:** the plan was written against `16:50:27Z` and the issue is now at `17:00:08Z`. The issue body says the later changes only touched lifecycle, comments and artifact links. Its objective, scope and acceptance criteria still match the plan, so I treated the gap as editorial.

**Changes made, using only the `gh` calls you allowed:**
1. `gh issue edit 34 … --remove-label backplane:ready --add-label backplane:active`
2. A comment with your evidence text and the checks above: https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400528216

**Fresh read afterwards (`updatedAt` `2026-10-25T17:01:51Z`):**
- The labels are now `documentation` and `backplane:active`, so there is still exactly one Backplane label.
- The issue is still open. The body is byte-identical. Parent, sub-issues, blockers and closing-PR references are all still empty.

**Not checked or claimed:**
- I read the plan file's text but did not confirm it matches commit `33d4300` or blob `6b33d68…`, because only `gh` commands were allowed.
- For the "verified in the prior fresh session" part, I relied on your statement and checked again only what the issue and plan file show.
- The review correction is still outstanding. No clean review, publication or integration is claimed.

I didn't change any local files, Git state, plugins or other issues.

## review

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T17:01:51Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is active to review, for this evidence: The exact approved paragraph and bound plan are committed on test/issue-19-doc-lifecycle; the candidate changes only those two files, and the paragraph bytes plus all four unchanged PowerShell examples passed verification. This is formal submission of that local candidate for the fixture review workflow, not PR publication or merge acceptance. A fresh independent draft review already examined these exact paragraph bytes and identified a real Important content-comparison correction; read .sp-bp/work/issue-19/fixture-review.md, preserve its earlier timing, and record that correction as outstanding. Do not claim a clean review, do not fabricate a later review, and do not publish. The next authorized step is returning review to active to address the actual requested correction.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:active --add-label backplane:review. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_017WM9TXJu6fbj1gamCMvgaX",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01WinvwBcKfhukB39hu5n4rm",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Fetch issue 34 native state"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01BwjQDxe66Qstqecoa57PBQ",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01RU2YTniKXLrNxC2dyQbLH2",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_019DLVqMaHkhxGv6oT4Ux3XA",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\fixture-review.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01Doo8bsobkk9KJ91JaGtZW3",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-read issue 34 before mutation"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_017iMABu2dTWzecqWjyTTHtz",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:active --add-label backplane:review",
      "description": "Transition issue 34 from active to review"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_0184RWxVdguGBNwYCECifNXF",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body \"Lifecycle: backplane:active -> backplane:review (formal submission of local candidate for fixture review workflow; not PR publication or merge acceptance).\n\nReconciliation: re-read at updatedAt 2026-10-25T17:01:51Z, matching the expected revision; no drift. Exactly one Backplane label before transition; documentation label and native graph (no parent, sub-issues, blockers or linked PRs) preserved.\n\nSubmission evidence (operator-attested; this session ran only gh and did not re-run local Git or file verification): the exact approved paragraph and bound plan are committed on test/issue-19-doc-lifecycle; the candidate changes only docs/installing-claude-code.md and the fixture plan; the paragraph bytes and all four unchanged PowerShell examples passed verification.\n\nReview status: an independent read-only draft review (2026-10-25) was obtained BEFORE this transition, against these exact paragraph bytes. No later review has occurred. Outstanding Important finding: the paragraph requires recording source commit, installed version and hashes but does not require them to match the selected immutable source, so an update that leaves the old package installed could pass. Requested correction: require installed commit/version and file hashes to match the selected immutable source for update and rollback; mismatches fail verification. No Critical or Minor findings; no separate plan defect. Verdict: correction required before integration.\n\nThis is not a clean review and not satisfaction evidence. Next authorized step: return backplane:review -> backplane:active to address the requested correction.\"",
      "description": "Post evidence and reconciliation comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01Rmm9nj2wu7ZWmxUH8ugKGu",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue #34 has moved from `backplane:active` to `backplane:review`, and I posted the evidence comment.

**Checks before the change:** I fetched the issue twice. Both reads returned the expected revision `2026-10-25T17:01:51Z`, so there was no drift to reconcile. The issue was OPEN with exactly one Backplane label (`backplane:active`) next to `documentation`, and it had no parent, sub-issues, blockers or linked PRs. The review in `.sp-bp/work/issue-19/fixture-review.md` says "correction required before integration." That blocks integration, not submission, so moving to review was allowed as long as the correction stayed marked outstanding.

**Changes:**
- **Label:** one `gh issue edit` call removed `backplane:active` and added `backplane:review`.
- **Comment:** [issuecomment-6400543221](https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400543221). It records:
  - the revision check;
  - the submission evidence;
  - that the independent draft review happened before this transition and that no later review exists;
  - the outstanding Important correction: installed commit/version and hashes must *match* the selected immutable source for update and rollback, and a mismatch fails verification.

  It says plainly that this is not a clean review and not satisfaction evidence.

**Check after the change:** the re-fetch shows the issue still OPEN, with labels `documentation` and `backplane:review` (exactly one Backplane label). The body and all relationships are unchanged. The new revision is `2026-10-25T17:03:13Z`.

**One limit:** you allowed only `gh` commands, so I did not re-check the local branch, which files changed, or the paragraph and PowerShell results myself. The comment labels those claims as your attestation, not as something this session verified.

I made no local file, Git, plugin or other-issue changes and published nothing. The next authorized step is to move #34 from review back to active and make the requested correction.

## rework

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T17:03:13Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is review to active, for this evidence: The independent read-only fixture reviewer requested this real correction: require installed commit/version and file hashes to match the selected immutable source for update and rollback, and fail verification on mismatch. Its report is .sp-bp/work/issue-19/fixture-review.md. This remains within the operator-approved design and plan. Return the actual reviewed local candidate to active for that correction; preserve documentation and do not publish or close.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:review --add-label backplane:active. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01Y2tyzSiuewR98Kjb6S3JY1",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Fetch native issue 34 state"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_016RghRhebn4tr3tdTPhUyzR",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01TAH3maK721XNWLTcJPcTVJ",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01KEdRyU9bgSubnVuktt9u9F",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01B7Ygwn9fgbNbuswvXMUHGs",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\fixture-review.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01WpSzvjMJzxbbXrEThxF2Vi",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-read issue 34 before mutation"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01QKH3VwMoXxVQXjp7Ahj6TM",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:review --add-label backplane:active",
      "description": "Transition issue 34 from review to active"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012UqAFDPLQyt26keuAGUvAQ",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body \"Lifecycle: backplane:review -> backplane:active (review requested implementation changes).\n\nPre-mutation intake: open, updatedAt 2026-10-25T17:03:13Z (matches expected; no drift), exactly one Backplane label (backplane:review), documentation label present, no parent/sub-issues/blockers/blocking/closing PRs.\n\nEvidence: independent read-only fixture review, local report .sp-bp/work/issue-19/fixture-review.md (2026-10-25). Important finding: the initial paragraph requires recording source commit, installed version and hashes but not that they match the selected immutable source, so a stale install could pass. Requested correction: require installed commit/version and file hashes to match the selected immutable source for update and rollback; mismatches fail verification. No Critical or Minor findings; no defect in the bound plan. Verdict: correction required before integration.\n\nTiming: that review was obtained as a draft contribution review before the native review transition; this record does not claim a later review occurred.\n\nScope: correction stays within the operator-approved issue design and bound plan. Returns the actual reviewed local candidate to active for that correction. Documentation label and all relationships preserved. Not published, not integrated, not closed. Review report does not establish live hosted behavior, integrated-byte arrival or #19 acceptance.\"",
      "description": "Post evidence and reconciliation comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_012Y48XfQKggYNjK4CxGEM94",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue #34 has moved from `backplane:review` back to `backplane:active` so the reviewer's correction can be made. The comment is posted and the issue still has its `documentation` label.

**Checks before the change:**
- **No drift:** both reads, before and just before the edit, showed `updatedAt` at the expected `2026-10-25T17:03:13Z`.
- **Labels:** the issue was open with exactly one Backplane label (`backplane:review`), alongside `documentation`.
- **Relationships:** it had no parent, sub-issues, blockers, blocking links or closing PRs.
- **Transition allowed:** the backlog skill's issue contract allows review → active when a review asks for implementation changes. `.sp-bp/work/issue-19/fixture-review.md` does: it rates as "Important" that the guide paragraph only asks adopters to record the installed commit, version and file hashes, not check them against the source. A stale install could still pass. The report says the paragraph must be corrected before it is integrated.

**Actions:**
1. I ran the `gh issue edit` command you gave, exactly as written.
2. I posted the evidence and reconciliation comment (https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400552658). It records:
   - the intake state before the change;
   - the finding and the requested correction;
   - that the review happened before the issue moved to review, without claiming a later review;
   - that the correction stays within the approved scope;
   - that nothing has been published, integrated or closed.

**Check after the change:** the issue is open, with exactly `documentation` and `backplane:active`. Its body, relationships and closing-PR fields are unchanged, and `updatedAt` is now `2026-10-25T17:04:04Z`.

I made no changes to local files, Git, plugins or any other issue. The guide paragraph itself still has to be corrected.

## blocked

### Exact prompt

```text
This is the operator-authorized live documentation fixture for issue #19. Use actual installed superpowers:using-superpowers and superpowers-backplane:managing-superpowers-backlog skills. Use gh CLI only for GitHub, issue 34 only, repository tvproductions/superpowers-backplane. First run exactly: gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url. Read required installed skill references. Do not mutate local files, Git state, plugins or any other issue. Use no shell chaining, pipelines, redirection or external commands other than the allowed gh calls. Expected current revision is 2026-10-25T17:04:04Z; re-read and reconcile any drift before mutation. The explicitly authorized operation is active to blocked, for this evidence: The useful paragraph is corrected and verified; the real reviewer finding is addressed. Publication and integration were explicitly excluded from the prior authorization and must now be presented separately. The exact local two-file contribution on test/issue-19-doc-lifecycle cannot be published or integrated until the operator approves that concrete package. Resume target: backplane:active. Release condition: explicit operator approval to publish the reviewed fixture branch/PR and integrate it after fresh verification. This is a real authorization dependency, not a fabricated technical failure. Record this blocker before the label edit; do not close issue 34 or issue 19.. If its gates hold, execute exactly: gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:active --add-label backplane:blocked. Preserve documentation and all relationships. Record a concise factual evidence/reconciliation comment using gh issue comment 34 --repo tvproductions/superpowers-backplane --body <quoted text>, then re-fetch the complete native issue and verify the result. If the gates do not hold, stop and explain rather than fabricate evidence. For entering blocked, post the blocker comment BEFORE the label edit. It must state Resume target: backplane:active and the concrete release condition. Then make the one atomic label swap and re-fetch; do not request or infer publication approval.
```

### Observed tool calls

```json
[
  {
    "type": "tool_use",
    "id": "toolu_01JCXn32ASW2jUNqjLJoZfGx",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Fetch native issue 34 state"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01NttQKdhx2V8z1MYy28mP1W",
    "name": "Skill",
    "input": {
      "skill": "superpowers-backplane:managing-superpowers-backlog"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01RysX2G9m7pm4yLUR4JQ6yH",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\github-issue-contract.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_015HeBGroyseubJJds5aLS9q",
    "name": "Read",
    "input": {
      "file_path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog\\references\\superpowers-binding.md"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_011YqjifKiBGYDxQHfRXh33k",
    "name": "Bash",
    "input": {
      "command": "gh issue comment 34 --repo tvproductions/superpowers-backplane --body 'Lifecycle transition: backplane:active -> backplane:blocked (operator-authorized, issue #19 documentation fixture).\n\nReconciliation: re-read native issue at updatedAt 2026-10-25T17:04:04Z (matches expected; no drift). State OPEN; exactly one Backplane label (backplane:active); unrelated label documentation preserved; no parent, sub-issues, blockedBy/blocking edges or closing PRs.\n\nEvidence: the useful paragraph is corrected and verified; the real reviewer finding is addressed.\n\nBlocker: publication and integration were explicitly excluded from the prior authorization and must now be presented separately. The exact local two-file contribution on test/issue-19-doc-lifecycle cannot be published or integrated until the operator approves that concrete package. This is a real authorization dependency, not a technical failure.\n\nResume target: backplane:active\nRelease condition: explicit operator approval to publish the reviewed fixture branch/PR and integrate it after fresh verification.\n\nNo publication approval is requested or inferred here. #34 and #19 remain open.'",
      "description": "Post blocker comment on issue 34"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_0156Y6joJzvs7zD4BUqRpWS6",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 before label edit"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01BqJoaJL5GdbW3KEnc15waw",
    "name": "Bash",
    "input": {
      "command": "gh issue edit 34 --repo tvproductions/superpowers-backplane --remove-label backplane:active --add-label backplane:blocked",
      "description": "Swap issue 34 label active to blocked"
    },
    "caller": {
      "type": "direct"
    }
  },
  {
    "type": "tool_use",
    "id": "toolu_01C8v4sDf9KoEkD5D2eHgGWH",
    "name": "Bash",
    "input": {
      "command": "gh issue view 34 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url",
      "description": "Re-fetch issue 34 to verify transition"
    },
    "caller": {
      "type": "direct"
    }
  }
]
```

### Unedited response

Issue #34 is now in `backplane:blocked`, and the final re-fetch confirms it.

**Gate checks before any change:**
- The issue was open, and `updatedAt` was exactly the expected `2026-10-25T17:04:04Z`.
- It had exactly one Backplane label, `backplane:active`, next to `documentation`.
- It had no parent, sub-issues, blocker links or closing PRs.
- The blocker you gave was concrete: publication and integration are waiting on your approval.

**What I did, in order:**
1. **Blocker comment** (posted before the label edit): https://github.com/tvproductions/superpowers-backplane/issues/34#issuecomment-6400592940. It records:
   - the reconciliation and your evidence;
   - the authorization blocker for the two-file contribution on `test/issue-19-doc-lifecycle`;
   - `Resume target: backplane:active`;
   - the release condition: your explicit approval to publish the reviewed fixture branch/PR and integrate it after fresh verification.
2. **Re-read before the label edit:** `updatedAt` had moved to `17:07:47Z` because of my comment. The body, labels and relationships were unchanged, so it was a minor change caused by the comment, not real drift.
3. **Label swap:** one `gh issue edit` call removed `backplane:active` and added `backplane:blocked`.

**Final state at `updatedAt` `2026-10-25T17:07:58Z`:**
- The issue is still open with no close reason.
- Its labels are exactly `documentation` and `backplane:blocked`, so there is still only one Backplane label.
- The body is unchanged, and there are still no parent, sub-issues, blocker links or closing PRs.

I didn't touch issue #19 or any other issue, local files, Git state or plugins. I haven't asked for or assumed publication approval; that decision stays with you.

## fixture-review.md

# Fresh fixture review

Reviewer: independent `fixture_review` agent, read-only, 2026-10-25.
Review targets: exact approved paragraph, complete B-based before/after guide,
bound fixture plan and approved #19 recovery Task 4.

## Important — recording hashes does not verify installed content

The initial paragraph at `fixture-paragraph.md:3` (proposed guide line 80)
requires recording a source commit, installed version and hashes but does not
require them to match the selected immutable source. An update leaving the old
package installed can satisfy those instructions and still load all three
skills. This conflicts with the fixture's installed-content acceptance criterion
and recovery Review Focus item 1.

Correction requested: require the installed commit/version and file hashes to
match the selected immutable source for update and rollback; mismatches fail
verification.

No Critical or Minor findings. No separate defect in the bound plan. The review
does not establish live hosted behavior, preservation, native lifecycle,
authorization provenance, integrated-byte arrival or final #19 acceptance.

Verdict: correction required before integration. The report was obtained as a
draft contribution review before its native review transition; later lifecycle
records must preserve that timing rather than claim a later review occurred.

## fixture-review-resolution.md

# Fixture review resolution

Same independent review seat, focused confirmation, 2026-10-25.

The Important finding is resolved at guide line 80, local fixture commit
`22c5b8d917a09f275c23d99bd9c9645d6c1d2e35`. The wording explicitly requires
installed commit, version and file hashes to match the selected immutable source;
any mismatch fails verification.

The reviewer accepts the two-file fixture contribution for integration, subject
to operator authorization and integrated-byte checks. No findings remain from
this focused review. This does not establish live lifecycle behavior,
preservation, authorization provenance, integration arrival or final #19 acceptance.
The earlier review's declined-to-judge limits remain unchanged.
