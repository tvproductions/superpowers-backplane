# Superpowers Backplane Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap a re-enterable, language-neutral Backplane repository with one tested Superpowers backlog skill and its governing contracts.

**Architecture:** Native GitHub Issues own backlog continuity. A single skill binds that continuity to upstream Superpowers specifications, plans, execution, and completion evidence. Detailed contracts remain in references so the skill stays concise.

**Tech Stack:** Markdown agent skills, GitHub CLI (`gh`), Git, upstream Superpowers

**Spec:** `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md`

## Global Constraints

- Assume upstream Superpowers in every workflow.
- Remain language-neutral; do not assume a project runtime or test framework.
- Require `gh`; do not require GitHub Projects or IssueOps.
- Never add, suggest, or assume pytest.
- Do not create a remote repository or release in this bootstrap.

---

### Task 1: Establish the repository control surface

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `HANDOFF.md`
- Create: `.gitignore`

**Interfaces:**
- Consumes: approved bootstrap design
- Produces: session-entry and dependency rules for future agents

- [x] Record the language-neutral and GitHub-native boundary.
- [x] Record Superpowers as the defining managed dependency.
- [x] Record the re-entry sequence and unresolved publication decisions.

### Task 2: Capture the skill RED baseline

**Files:**
- Create: `tests/scenarios/2026-08-16-native-issue-intake-baseline.md`

**Interfaces:**
- Consumes: a no-skill pressure scenario
- Produces: observed failure modes that the minimal skill must correct

- [x] Run a scenario combining time, authority, and sunk-cost pressure without the skill.
- [x] Record the response's concrete choices and repository-specific leakage.
- [x] Convert observed failures into explicit skill acceptance expectations.

### Task 3: Author the minimal backlog skill

**Files:**
- Create: `skills/managing-superpowers-backlog/SKILL.md`
- Create: `skills/managing-superpowers-backlog/agents/openai.yaml`
- Create: `skills/managing-superpowers-backlog/references/github-issue-contract.md`
- Create: `skills/managing-superpowers-backlog/references/superpowers-binding.md`
- Create: `skills/managing-superpowers-backlog/references/installing-superpowers.md`

**Interfaces:**
- Consumes: native issue contract and observed baseline failures
- Produces: one discoverable skill that surrounds upstream Superpowers with backlog continuity

- [x] Define intake, status, selection, transition, submission, and closure behavior.
- [x] Keep GitHub details and Superpowers binding rules in directly linked references.
- [x] Define sibling and managed Superpowers installation behavior.

### Task 4: Verify and prepare re-entry

**Files:**
- Create: `tests/scenarios/2026-08-16-native-issue-intake-green.md`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: completed skill and reference contracts
- Produces: validation evidence and an honest continuation point

- [x] Run structural skill validation.
- [x] Re-run the pressure scenario with the skill and record results.
- [x] Review the complete scaffold for placeholders, Python assumptions, IssueOps, and required Projects.
- [x] Initialize the local Git repository and install an upstream Superpowers checkout for re-entry.
