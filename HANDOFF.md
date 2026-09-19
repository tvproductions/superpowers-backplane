# Handoff

## Current state

The standalone local repository is at
`C:\Users\Jeff\source\repos\agents\superpowers-backplane` on `main`. Before
Git mutation, continue to require `git rev-parse --show-toplevel` to resolve
exactly to that Backplane root.

The initial design is approved in principle:

- Everything assumes and is fitted to upstream Superpowers.
- Native GitHub Issues provide backlog continuity.
- GitHub CLI (`gh`) is a hard dependency.
- GitHub Projects are optional visualization only and never authoritative;
  IssueOps is not used.
- The project is language-neutral and must never assume pytest.
- Backplane can adopt a sibling Superpowers checkout or obtain one for the
  user while preserving upstream provenance and updateability.

The first skill and its reference contracts have passed the bootstrap
pressure scenarios plus a five-control/five-skill read-only status and
selection micro-test. The no-skill arm supplied complete native intake in 0/5
samples; the skill-enabled arm supplied it in 5/5 while both arms refused to
invent priority or mutate state. The verbatim response records are under
`tests/scenarios/transcripts/`.

Stable upstream Superpowers `v6.4.1` is installed at
`.agents/superpowers` at commit
`5bf4e78011075bcfc0dc295f0724994cd123ee71`. Discovery junctions expose
upstream Superpowers, `managing-superpowers-backlog`, and
`managing-superpowers-handoffs` under `.agents/skills`. The local update and
fresh Codex conformance evidence are recorded in
`tests/scenarios/2026-09-19-superpowers-v6.4.1-compatibility.md`.
The repository is published publicly at
`https://github.com/tvproductions/superpowers-backplane`, and `main` tracks
`origin/main`. GitHub CLI authentication was verified for `ahuimanu` with
keyring-stored credentials. The repository-local Git identity uses GitHub's
noreply address. Re-check `gh auth status` before real backlog operations.

## Re-entry sequence

1. Read `AGENTS.md`.
2. Read the bootstrap design and plan linked there.
3. Read `SUPERPOWERS.md` and confirm that the installed checkout matches it.
4. Confirm that the Git top-level directory is exactly this repository root.
5. Inspect `skills/managing-superpowers-backlog/`.
6. Review the RED/GREEN/REFACTOR evidence in `tests/scenarios/`.
7. Confirm `gh auth status` succeeds before any real backlog operation.
8. Confirm `origin` resolves exactly to
   `https://github.com/tvproductions/superpowers-backplane.git` before any
   real backlog operation or push.

## Next design decisions

- Final installation surfaces for Codex, Claude Code, and other Superpowers
  harnesses.
- Whether v1 should mutate labels or remain read-only until an explicit start
  or transition request.
- Whether deterministic helpers are needed after field experience; v1 does
  not assume a standalone Backplane executable.
