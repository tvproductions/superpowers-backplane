# Status and Selection Skill-Enabled Responses

The complete outputs captured in this session are reproduced verbatim below.
Each isolated sample received the exact skill-enabled prompt in
`../2026-08-16-status-selection-refactor.md`. The harness did not expose
durable run identifiers.

## Sample 1

B

```text
gh issue view 102 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 103 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue list --repo example/widgets --state open --label backplane:ready --json number,title,labels,parent,subIssues,blockedBy,updatedAt,url
```

## Sample 2

B

```text
gh issue list --repo <owner/repo> --state open --label backplane:ready --json number,title,labels,parent,subIssues,blockedBy,updatedAt,url
gh issue view 101 --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 102 --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 103 --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 104 --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

## Sample 3

B

```text
gh issue view 102 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue view 103 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
gh issue list --repo example/widgets --state open --label backplane:ready --json number,title,labels,parent,subIssues,blockedBy,updatedAt,url
```

## Sample 4

B

```text
gh issue view 102 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

gh issue list --repo example/widgets --state open --label backplane:ready --json number,title,labels,parent,subIssues,blockedBy,updatedAt,url
```

## Sample 5

B

```text
gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

gh issue list --repo <owner/repo> --state open --label backplane:ready --json number,title,labels,parent,subIssues,blockedBy,updatedAt,url
```

## Manual scoring

All five samples chose B and showed no mutation command. Every sample supplied
the complete native issue-view field list and the `backplane:ready`
candidate-list command shape.
