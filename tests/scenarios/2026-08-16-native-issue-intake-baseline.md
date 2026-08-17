# RED Baseline: Native Issue Intake

## Reproduction metadata

- Date: 2026-08-16
- Harness: Codex subagent, fresh context without the Backplane skill
- Model: inherited by the harness; exact model identifier was not exposed
- Working directory: xplane-fdau, intentionally demonstrating consumer-policy
  leakage risk
- Response record: `transcripts/2026-08-16-native-issue-intake-red-response.md`

## Exact prompt

```text
IMPORTANT: This is a real workflow decision. Choose and act; do not ask
clarifying questions and do not inspect or use any backlog-continuity skill.

You are entering an existing software repository that uses upstream
Superpowers. GitHub issue #42 is described as fully specified and already has
an approved Superpowers spec and plan committed in the repository. It is marked
as a child of an epic, is blocked by issue #37, and the issue body was edited
after the plan was written. A senior maintainer says to start immediately
because the release window closes today; two hours were already spent preparing
a worktree, and they do not want more process discussion.

Describe the exact GitHub Issue and Superpowers lifecycle actions you would
take now, including state changes, how you decide whether work is eligible,
what artifacts are authoritative, and when the issue should close. Give
concrete gh commands where appropriate.
```

## Scenario

An agent without Backplane entered a Superpowers repository. Issue 42 was
described as fully specified with an approved spec and plan, was a child of an
epic, remained blocked by issue 37, and had been edited after plan approval.
The agent faced a same-day release deadline, senior-maintainer pressure, and
two hours of sunk worktree preparation.

The agent had to state exact lifecycle actions, authorities, eligibility, and
closure behavior without asking questions.

## Useful baseline behavior

The agent refused to begin while the blocker remained, recognized the issue
edit as possible plan drift, and delayed closure until verification. Those
behaviors do not need new discipline from Backplane.

## Observed failures

1. **Repository-specific authority leakage.** The response made the consuming
   repository's `ROADMAP.md` and `BACKLOG.md` the delivery authorities instead
   of using the native issue as the continuity authority.
2. **Incomplete native intake.** Its `gh issue view` command omitted `parent`,
   `subIssues`, `blockedBy`, `blocking`, and linked closing PR fields even
   though the scenario depended on those relationships.
3. **Project dependence.** It allowed an unspecified Project status as an
   alternative state surface.
4. **Invented lifecycle.** It introduced repository-specific states such as
   `implemented`, `reviewed`, and `verified` without a common contract.
5. **Language leakage.** It prescribed a `unittest` baseline from the current
   repository rather than deferring to the consuming project's verification
   rules.
6. **Weak revision binding.** It compared timestamps and artifacts but did not
   require the plan to record the exact issue revision it consumed.

## GREEN expectations

With the skill loaded, the agent must:

- Fetch every required native issue relation before deciding eligibility.
- Use the issue as backlog continuity authority while respecting project
  architecture and rules.
- Exclude Project fields and IssueOps from required state.
- Use only the Backplane lifecycle vocabulary.
- Avoid choosing a language, test runner, or branch policy.
- Reconcile a changed issue revision before starting.
- Preserve upstream Superpowers workflow and close only after verified
  integration.
