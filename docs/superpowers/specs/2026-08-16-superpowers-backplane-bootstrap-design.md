# Superpowers Backplane Bootstrap Design

**Status:** Approved bootstrap direction

## Purpose

Superpowers produces durable specifications and implementation plans but does
not connect those artifacts into a persistent product arc. Projects therefore
invent incompatible roadmap files, backlog schemas, status rules, and skills.

Superpowers Backplane provides that missing backlog-level continuity. It is a
companion fitted to Superpowers, not a replacement for it and not a generic
project-management system.

## Commitments

- Assume upstream Superpowers in every workflow.
- Remain agnostic to project language, runtime, build system, test framework,
  and branch policy.
- Require GitHub CLI (`gh`) and use native GitHub Issues as the continuity
  backplane.
- Never require GitHub Projects.
- Never introduce IssueOps.
- Never add, suggest, or assume pytest.
- Keep project rules in each consuming project's normal control documents.
- Keep Superpowers independently identifiable and updateable when Backplane
  obtains it.

## Authority model

Authority is layered rather than duplicated:

1. Project architecture and rules govern product and repository constraints.
2. A GitHub issue governs backlog identity, objective, bounded scope,
   acceptance criteria, verification seams, hierarchy, dependencies, and
   backlog lifecycle.
3. An approved Superpowers specification governs design when a separate design
   artifact is warranted. A complete, human-approved issue may itself be the
   design authority for bounded work.
4. A Superpowers plan governs execution of one bounded work item and records
   the issue revision it consumed.
5. Commits, reviews, verification output, and a merged pull request provide
   completion evidence.

No local roadmap or backlog document may silently become a second mutable
master for fields governed by the issue.

## Native GitHub model

Use GitHub's native structures directly:

- Repository plus issue number or URL is the stable work-item identity.
- Parent and sub-issue relationships form product arcs and decomposition.
- Blocking relationships encode execution dependencies.
- Native issue types classify work where available.
- Exactly one Backplane lifecycle label records the open issue's workflow
  state.
- Linked pull requests and GitHub closure relationships connect delivery
  evidence.
- GitHub open/closed state records whether work remains live; closure reason
  distinguishes completed from not-planned outcomes.

GitHub Projects may visualize issues but never carry required Backplane state.

## Lifecycle

The portable lifecycle vocabulary is:

| Label | Meaning |
|---|---|
| `backplane:backlog` | Captured but not ready for execution |
| `backplane:designing` | Issue, specification, or plan is being brought to approval |
| `backplane:ready` | Approved and dependency-ready for execution |
| `backplane:active` | Superpowers execution is in progress |
| `backplane:blocked` | Work cannot advance; the reason is recorded in the issue |
| `backplane:review` | Implementation is submitted and awaiting final review/integration |

A completed issue is closed with reason `completed`; a rejected or abandoned
item is closed with reason `not planned`. Closed issues do not carry a
`backplane:done` label.

Transitions must follow evidence. A deadline, prepared worktree, open pull
request, or checked plan box does not independently prove a transition.

## Issue contract

Executable leaf issues contain the following headings:

```markdown
## Objective

## Bounded Scope

### Allowed

### Out of Scope

## Acceptance Criteria

## Verification Seams

## Superpowers Artifacts
```

Parentage and dependencies remain native relationships rather than duplicated
body text. The artifact section links the approved design authority and plan;
it may state that the approved issue body is the design authority.

## Intake and eligibility

Intake retrieves at least `number`, `title`, `body`, `state`, `stateReason`,
`issueType`, `labels`, `parent`, `subIssues`, `blockedBy`, `blocking`,
`closedByPullRequestsReferences`, `updatedAt`, and `url` through `gh`.

An issue is eligible only when it is open, is an executable leaf, satisfies the
issue contract, has approved design authority and a plan, has no unresolved
native blocker, and carries `backplane:ready`. Selection is explicit; a list of
eligible issues is not an invented priority order.

`updatedAt` is a conservative change detector, not proof of semantic change.
If it differs from the revision recorded by the plan, reconcile the current
issue body against the design and plan before execution.

## Superpowers binding

Backplane does not alter the upstream Superpowers sequence. It supplies the
outer continuity surrounding it:

```text
issue intake
  -> brainstorming/spec when required
  -> writing-plans
  -> execution and TDD
  -> review and verification
  -> integration and issue closure
```

The issue tracks the product arc. The specification records approved design.
The plan records temporary execution authority. Plan checkboxes are progress
signals, not backlog completion evidence.

## Installation and dependency model

Backplane is a separate checkout installed through the skill-discovery surface
supported by the active agent harness. It supports:

- **Sibling mode:** detect and adopt an existing compatible Superpowers
  checkout beside Backplane.
- **Managed mode:** obtain upstream `obra/superpowers` when absent and expose
  both projects' skills.

Managed Superpowers remains an independent Git checkout with its upstream
remote intact. Backplane records the resolved upstream revision for diagnosis
but favors new compatible releases instead of creating an indefinite pin. The
default channel is the latest stable upstream release; the upstream default
branch is an explicit edge-channel choice. Updates must refuse to overwrite
local changes and must report compatibility before changing the checkout.

## Bootstrap scope

The bootstrap creates normative specifications, one reusable skill, reference
contracts, conformance scenarios, and a re-entry handoff. It does not create a
standalone executable, GitHub Action, GitHub Project, remote repository, or
release.
