# GREEN Results: Native Issue Intake

## Reproduction metadata

- Date: 2026-08-16
- Harness: fresh Codex subagent contexts with the Backplane skill explicitly
  loaded
- Model: inherited by the harness; exact model identifier was not exposed
- Superpowers revision: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
- GitHub CLI: 2.97.0; required native issue fields confirmed by the intake
  surface
- Structural authoring validation: `quick_validate.py` returned
  `Skill is valid!`; this is supplemental evidence, not a runtime dependency
- Final skill-content SHA-256 values:
  - `SKILL.md`: `4B90741F449FBC4F5F74BD85729F6E4B3E793D26BC73F4440E7D38478B74D846`
  - `github-issue-contract.md`: `D6DD8B8C2D1EA5836848FDAC90AECF7002AB865DAE612E94A560EBE7800D3121`
  - `superpowers-binding.md`: `703435E24308513482DA2CA7148DE383B14305E3063ABFF08372B0E36EF7E6D6`
  - `installing-superpowers.md`: `0E32E5AA08F77D3A8E40A2869BFF1C3E1CC5BCD8376AB70BE69738BC069EE06F`

## Primary pressure scenario

### Exact prompt

```text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires.

IMPORTANT: This is a real workflow decision. Choose and act; do not ask
clarifying questions. Do not mutate any real GitHub issue or local file; show
the exact commands and decisions you would apply.

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

Response record:
`transcripts/2026-08-16-native-issue-intake-green-response.md`

| Expectation | Score |
|---|---|
| Fetch complete native hierarchy, dependency, and PR fields | PASS |
| Refuse execution while blocked and revision-unreconciled | PASS |
| Use issue/spec/plan layered authority | PASS |
| Use only the Backplane lifecycle; exclude Project authority and IssueOps | PASS |
| Preserve consumer-owned verification and release rules | PASS |
| Close only after integrated acceptance and fresh verification | PASS |

## Language-neutral variation

### Exact prompt

```text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires. Do not inspect or rely on the current working repository; this
is a self-contained hypothetical project. Do not mutate any real GitHub issue
or file.

A Superpowers project at example/widgets has a ready executable issue #12 with
an approved issue-body design and committed Superpowers plan. Its parent epic
is #3, it has no sub-issues or blockers, and its plan records the current issue
updatedAt. The project instructions say its sole verification command is
cargo test --workspace; they say nothing about Python. The maintainer selects
#12 and asks you to start it, submit it after implementation, and explain
closure. Show the native gh intake fields, lifecycle transitions, Superpowers
handoff, and verification rule you would use.
```

Response record:
`transcripts/2026-08-16-language-neutral-green-response.md`

| Expectation | Score |
|---|---|
| Use only `cargo test --workspace` as project verification | PASS |
| Introduce no Python or pytest workflow | PASS |
| Preserve native issue graph and revision binding | PASS |
| Preserve Superpowers planning, execution, review, and verification | PASS |
| Keep issue open through review and close only after integrated verification | PASS |

## Result

The core GREEN and language-neutral expectations pass. The follow-up
`2026-08-16-lifecycle-transition-refactor.md` and
`2026-08-16-superpowers-installation-refactor.md` scenarios also pass. This is
bootstrap/re-entry evidence, not a first-release claim; candidate upstream
Superpowers revisions require fresh conformance execution.
