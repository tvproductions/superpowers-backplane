# Superpowers Binding

## Boundary

Backplane supplies the outer product-continuity loop. Upstream Superpowers
supplies design and implementation discipline. Do not fork, weaken, or reorder
Superpowers skills inside Backplane.

```text
GitHub issue continuity
  -> superpowers:brainstorming when design is required
  -> approved issue design or docs/superpowers/specs artifact
  -> superpowers:writing-plans
  -> Superpowers execution and TDD
  -> Superpowers review and verification
  -> integration, evidence, and GitHub closure
```

## Design authority decision

Use a human-approved issue body as design authority when the work is bounded,
the issue contract is complete, and implementation does not introduce an
architectural, cross-cutting, or breaking decision.

Require a reviewed local specification under `docs/superpowers/specs/` when
the work changes architecture, spans multiple independently reviewable
subsystems, introduces a breaking contract, or requires design reasoning that
would be obscured in an issue body.

Do not repeat blank-slate brainstorming for decisions already approved in the
issue. Do use brainstorming to resolve missing or newly changed design.

## Plan binding

Each executable issue binds to one current Superpowers plan. The plan header or
constraints must record:

- Issue URL.
- Issue `updatedAt` revision consumed.
- Design authority: issue body or specification path.
- Acceptance criteria and verification seams as hard constraints.
- Exact project-owned verification commands.

The plan is execution authority, not the backlog master. A checked task records
plan progress only.

## Execution transitions

- Move `backplane:ready` to `backplane:active` when execution actually begins.
- Move any open state to `backplane:blocked` when a concrete unresolved
  condition stops progress; record its prior valid state as the resume target
  plus the required release evidence.
- Move active work to `backplane:review` when implementation, relevant review,
  and worktree verification support submission.
- Keep review open through requested changes and integration.
- Return review to `backplane:active` when review requests implementation
  changes.
- Close completed only after the integrated target passes fresh verification.

Project instructions decide worktree placement, branch strategy, test tools,
release rules, and deployment authority. Backplane must read those rules and
must not supply defaults that conflict with them.

## Evidence

Prefer native and committed evidence:

- Native issue relationships for hierarchy and blockers.
- Committed specification and plan paths for design/execution.
- Commits and review records for implementation.
- Linked PR and merge state for integration.
- Fresh command output or durable attestation for verification.

Comments explain state that these surfaces do not already express. They are not
a substitute for missing verification.
