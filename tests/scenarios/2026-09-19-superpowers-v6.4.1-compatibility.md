# Superpowers v6.4.1 local compatibility

## Candidate

- Date: 2026-09-19.
- Target: this repository's ignored `.agents/superpowers` checkout and local Codex discovery.
- Previous stable release: `v6.3.0` at `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
- Current stable release: `v6.4.1` at `5bf4e78011075bcfc0dc295f0724994cd123ee71`, published `2026-09-19T00:32:44Z`.
- Source: `https://github.com/obra/superpowers.git`; the checkout was clean before and after switching tags.
- `gh` 2.101.0 authenticated; a complete 15-field native intake query against Backplane issue #2 succeeded.
- `gh issue edit --help` exposes label addition and removal; `gh issue close --help` exposes closure reasons.

Release changes relevant to Backplane: brainstorming and plan approval gates, native inline plan execution, and OpenCode 2.0 support. This report verifies the local Codex installation only.

## Structural preflight

Both Backplane skills have valid frontmatter with the expected `name` and a `description` beginning `Use when`. Every directly linked reference exists. The scoped placeholder scan found no `TBD`, `TODO`, `FIXME`, or `PLACEHOLDER`. The candidate contains `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`.

Backlog skill SHA-256 values used by the fresh probes:

| File | SHA-256 |
|---|---|
| `SKILL.md` | `4B90741F449FBC4F5F74BD85729F6E4B3E793D26BC73F4440E7D38478B74D846` |
| `references/github-issue-contract.md` | `D6DD8B8C2D1EA5836848FDAC90AECF7002AB865DAE612E94A560EBE7800D3121` |
| `references/superpowers-binding.md` | `703435E24308513482DA2CA7148DE383B14305E3063ABFF08372B0E36EF7E6D6` |
| `references/installing-superpowers.md` | `0E32E5AA08F77D3A8E40A2869BFF1C3E1CC5BCD8376AB70BE69738BC069EE06F` |

## Fresh-session checks

Each behavioral check used its exact scenario prompt in a separate ephemeral, read-only `codex exec` session. Responses are saved under `transcripts/`.

| Required check | Score | Response |
|---|---|---|
| `skill-structure` | PASS | Structural preflight above |
| `native-issue-intake` | PASS, 6/6 expectations | `transcripts/2026-09-19-v6.4.1-native-issue-intake.md` |
| `language-neutral-verification` | PASS, 5/5 expectations | `transcripts/2026-09-19-v6.4.1-language-neutral.md` |
| `lifecycle-transitions` | PASS, 5/5 expectations | `transcripts/2026-09-19-v6.4.1-lifecycle.md` |
| `superpowers-installation` | PASS, 6/6 expectations | `transcripts/2026-09-19-v6.4.1-installation.md` |

The intake response refused blocked and unreconciled execution, fetched the complete native graph, separated issue/spec/plan authority, and required integrated acceptance and fresh verification for closure. The language-neutral response used only `cargo test --workspace`. The lifecycle response repaired duplicate labels, preserved `security`, and recorded and revalidated the blocked resume target. The installation response rejected the unsafe sibling, selected the authoritative stable source, and required compatibility and discovery checks.

A separate fresh Codex session discovered `superpowers:using-superpowers`, `managing-superpowers-backlog`, and `managing-superpowers-handoffs`; see `transcripts/2026-09-19-v6.4.1-discovery.md`. The ignored local handoff-skill junction was missing and was added before that probe.

## Result and boundary

All five required Backplane compatibility checks and local Codex discovery passed for this stable update. `SUPERPOWERS.md` records the observed revision for diagnosis. Issue #2 still requires independent Codex, Claude Code, and OpenCode adoption verification before v0.1 harness support can be claimed.
