# Superpowers v7.0.0 local compatibility

## Inventory and authorization

On 2026-10-11 the operator requested bringing project dependencies up to speed.
The initial Backplane worktree was clean on
`plan/issue-19-claude-lifecycle-draft`. This maintenance leaves that branch in
place and does not execute its issue #19 plan or mutate GitHub backlog state.

The only project-managed versioned dependency is the independent, ignored
`.agents/superpowers` checkout. The tracked tree has no runtime manifests,
lockfiles, CI action pins, container bases, hooks, or bundled executable tools.
Backplane's plugin metadata version `0.1.0` identifies Backplane itself, not a
dependency. The plugin schema URL is unchanged. Git, GitHub CLI, and the agent
harness are unpinned machine prerequisites; their global installations are
outside this project dependency refresh. Host version floors remain unchanged.

## Candidate and source review

- Previous: stable `v6.4.1`, `5bf4e78011075bcfc0dc295f0724994cd123ee71`.
- Candidate: stable `v7.0.0`, `bb92a77741419a4ab5f06e711a283343f1ada0c3`.
- Official release published: `2026-10-10T00:28:58Z`.
- Source: `https://github.com/obra/superpowers.git`.
- Release: <https://github.com/obra/superpowers/releases/tag/v7.0.0>.
- Observed prerequisites: Git `2.55.0.windows.5`, `gh` `2.102.0`, Codex CLI
  `0.162.1`. No machine tool was upgraded.

`gh api repos/obra/superpowers/releases/latest` identified the candidate.
The release notes and `git diff v6.4.1 v7.0.0` were reviewed, including the full
candidate brainstorming skill and writing-plans changes. Brainstorming now
sizes work and uses a builder check; plans favor exact decisions over redundant
implementation bodies. Neither changes Backplane's native issue authority,
revision reconciliation, evidence gates, or project-owned verification rules.
Windows hook and execution bookkeeping fixes are also included. No Backplane
skill edit was necessary. No optional upstream runtime or test tool was installed.

The upstream checkout had exact authoritative origin and no local changes before
`git -C .agents/superpowers fetch origin tag v7.0.0` and
`git -C .agents/superpowers checkout --detach v7.0.0`. Required upstream skill
paths remained present. The checkout is clean after the update. The previous
tag remains available for rollback; no rollback was needed.

## Preflight

- Authenticated `gh auth status` succeeded.
- `gh issue view 2 --repo tvproductions/superpowers-backplane --json
  number,title,body,state,stateReason,issueType,labels,parent,subIssues,
  subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`
  returned all 15 current contract fields, including nullable issue type.
- `gh issue edit --help` exposes `--add-label` and `--remove-label`.
- `gh issue close --help` exposes closure `--reason`.
- Both authored skills have expected YAML names and descriptions beginning
  `Use when`; all directly linked references exist; the scoped placeholder
  scan found no `TBD`, `TODO`, `FIXME`, or `PLACEHOLDER`.

## Fresh conformance

Each behavioral prompt was extracted verbatim from its mapped scenario's text
block and sent to a separate ephemeral read-only `codex exec` session. A probe
preamble required reading the candidate upstream entry skill first and prohibited
mutations or agent spawning. Responses were captured with `--output-last-message`.
Every session exited zero. Scores below come from reading the captured responses
against every expectation in the original rubric, not from process exit status.

| Required check | Result | Captured response |
|---|---|---|
| skill-structure | PASS, both skills | Structural preflight above |
| native-issue-intake | PASS, 6/6 | [Response](transcripts/2026-10-11-v7-native-issue-intake.md) |
| language-neutral-verification | PASS, 5/5 | [Response](transcripts/2026-10-11-v7-language-neutral.md) |
| lifecycle-transitions | PASS, all 6 acceptance expectations | [Response](transcripts/2026-10-11-v7-lifecycle.md) |
| superpowers-installation | PASS, 6/6 | [Response](transcripts/2026-10-11-v7-installation.md) |

Intake refuses blocked and unreconciled execution, retrieves the native graph,
preserves layered authority, and requires integrated verification for closure.
The language-neutral probe uses only `cargo test --workspace`. Lifecycle repair
preserves `security`, restores review before rework, records the blocked resume
target, and revalidates gates. Installation rejects lookalike and incomplete
upstream, defaults to authoritative stable installation, and fails closed on
unknown compatibility.

A fifth fresh session confirmed active inventory discovery, read all three
entry skills, resolved discovery junctions, and observed the candidate HEAD:
[Discovery response](transcripts/2026-10-11-v7-discovery.md). Its observation that
the dependency records still named the previous release was accurate during the
probe; those records were synchronized only after scoring passed.

Backlog skill SHA-256 values tested:

| File | SHA-256 |
|---|---|
| SKILL.md | `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81` |
| references/github-issue-contract.md | `D6DD8B8C2D1EA5836848FDAC90AECF7002AB865DAE612E94A560EBE7800D3121` |
| references/superpowers-binding.md | `703435E24308513482DA2CA7148DE383B14305E3063ABFF08372B0E36EF7E6D6` |
| references/installing-superpowers.md | `50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D` |

## Result and boundary

All five required Backplane compatibility checks plus fresh local Codex discovery
passed. The managed upstream dependency matches the latest stable release
observed on 2026-10-11. This verifies the development checkout and local Codex
discovery, not independent Claude Code or OpenCode installations. There is no
owning package manager providing an outdated or vulnerability command here;
this report makes no comprehensive vulnerability-audit claim.

Only dependency records and compatibility evidence changed in tracked Backplane
content. No skills, manifests, host support floors, or project purpose changed.
No commit, push, publication, release, or GitHub mutation was performed.
