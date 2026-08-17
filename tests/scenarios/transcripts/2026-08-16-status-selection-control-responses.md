# Status and Selection No-Skill Control Responses

The complete outputs captured in this session are reproduced verbatim below.
Each isolated sample received the exact control prompt in
`../2026-08-16-status-selection-refactor.md`. The harness did not expose
durable run identifiers.

## Sample 1

B

`gh issue view 102 --repo example/widgets --json number,title,state,body,labels,assignees,subIssues`

`gh issue list --repo example/widgets --state open --limit 100 --json number,title,state,labels`

## Sample 2

B

`gh issue view 102 --repo example/widgets --json number,title,body,state,labels,assignees,url`

`gh issue list --repo example/widgets --state open --limit 100 --json number,title,body,labels,assignees,url`

## Sample 3

B

`gh issue view 101 --repo OWNER/example-widgets --json number,title,state,labels,body,parent,subIssues,issueType,url`

`gh issue view 102 --repo OWNER/example-widgets --json number,title,state,labels,body,issueType,blockedBy,url`

`gh issue list --repo OWNER/example-widgets --state open --limit 100 --json number,title,labels,issueType,url`

## Sample 4

B

```powershell
gh issue view 101 --repo example/widgets
gh issue view 102 --repo example/widgets
gh issue view 103 --repo example/widgets
gh issue view 104 --repo example/widgets
gh issue list --repo example/widgets --state open
```

## Sample 5

B

`gh issue view 101 --repo OWNER/example-widgets --json number,title,body,state,labels,assignees,subIssues`

`gh issue view 102 --repo OWNER/example-widgets --json number,title,body,state,labels,assignees`

`gh issue list --repo OWNER/example-widgets --state open --limit 100 --json number,title,labels,assignees`

## Manual scoring

All five samples chose B and showed no mutation command. No sample supplied all
required fields:

```text
number,title,body,state,stateReason,issueType,labels,parent,subIssues,
subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

No sample supplied the `backplane:ready` candidate-list shape required by the
contract.
