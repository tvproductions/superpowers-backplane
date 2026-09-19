# Native Installed-plugin Discovery and Setup — Issue #3

Date: 2026-09-19. The disposable `state-native` profile was already authenticated using ChatGPT when these checks ran. No additional login was started. Codex CLI 0.155.1 loaded Backplane from its local package cache and upstream Superpowers 6.4.1 from the separate authoritative Git package cache. The working directory was the disposable fixture root, outside the repository and its `.agents/skills` junctions.

These discovery and setup sessions preceded the disposable cache refresh of `installing-superpowers.md` from SHA-256 `5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF` to current `50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D`. They prove native catalog identity and readable SKILL.md files, which did not change; their setup response alone is not current-branch conformance evidence. The four current-cache behavioral runs are recorded separately in `2026-09-19-codex-installed-plugin-conformance.md`.

The first fresh `--sandbox read-only` session listed all three skills in its catalog, but a PowerShell file read was blocked by execution policy. That first session alone does not prove operational discovery. A second fresh session with `--approve-for-me` completed direct reads of all three installed SKILL.md files from cache paths. A third fresh session performed read-only native setup checks and correctly withheld full compatibility until the four behavioral conformance scenarios were scored separately. The exact prompt and final response for each session follow.

## Fresh catalog discovery

Session ID: 01a0bbcd-1495-77b0-b63e-889d81591d12

### Exact prompt

`````text
Read your available skills catalog for this fresh session. Report whether superpowers:using-superpowers, managing-superpowers-backlog, and managing-superpowers-handoffs are available. For each, report the skill path from the catalog. Do not use repository-local junctions as evidence. Do not change files or GitHub issues.
`````

### Exact final response

`````text
All three are available in this session’s skills catalog:

| Skill | Catalog path |
|---|---|
| `superpowers:using-superpowers` | `r2/using-superpowers/SKILL.md` |
| `superpowers-backplane:managing-superpowers-backlog` | `r1/managing-superpowers-backlog/SKILL.md` |
| `superpowers-backplane:managing-superpowers-handoffs` | `r1/managing-superpowers-handoffs/SKILL.md` |

Catalog roots:

- `r1` = `C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0/skills`
- `r2` = `C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-dev/superpowers/6.4.1/skills`

This reports catalog availability; reading `using-superpowers/SKILL.md` was blocked by execution policy. No repository-local junctions were used, and no files or GitHub issues were changed.
`````

## Fresh installed-skill reads

Session ID: 01a0bbce-0fd4-7f12-a150-df8177696dd0

### Exact prompt

`````text
In this fresh session, open and read the SKILL.md files for the installed superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs skills from their plugin cache paths in your available-skills catalog. For each, report its exact name and the first instruction heading after frontmatter. Report any access failure exactly. Do not use project-local junctions and do not change files, plugin state, or GitHub issues.
`````

### Exact final response

`````text
All three files were read successfully from their catalog plugin cache paths.

| Exact catalog name | Frontmatter `name` | First heading after frontmatter |
|---|---|---|
| `superpowers:using-superpowers` | `using-superpowers` | `## The Rule` |
| `superpowers-backplane:managing-superpowers-backlog` | `managing-superpowers-backlog` | `# Managing the Superpowers Backlog` |
| `superpowers-backplane:managing-superpowers-handoffs` | `managing-superpowers-handoffs` | `# Managing Superpowers Handoffs` |

No access failures. No project-local junctions used; no files, plugin state, or GitHub issues changed.
`````

## Native package setup preflight

Session ID: 01a0bbce-e6aa-7b80-8553-20473c8dec42

### Exact prompt

`````text
Set up Superpowers Backplane in this Codex session for https://github.com/tvproductions/superpowers-backplane, using issue #13 only for read-only gh compatibility intake. The installed native upstream package superpowers@superpowers-dev is the candidate to adopt. Follow the installed Backplane backlog skill and its installation reference. Check exact Backplane package identity, authoritative upstream source and observed version, required upstream skills, gh authentication and full native issue fields and lifecycle flags, and fresh-session discovery. Report PASS, FAIL, or UNKNOWN for each gate with source paths and recovery for any missing gate. Do not install, update, remove, or alter plugins, files, or GitHub issues.
`````

### Exact final response

`````text
**Read-only preflight completed; overall adoption is UNKNOWN and remains incomplete.** The native candidate passes identity, provenance, discovery, and `gh` capability checks. Fresh behavioral conformance evidence is missing. No plugins, files, or GitHub issues were changed.

Source-path aliases below:

- **B:** [installed Backplane package](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0)
- **U:** [installed upstream package](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-dev/superpowers/6.4.1)
- **Config:** [active configuration](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/config.toml)

| Gate | Result | Evidence / recovery |
|---|---|---|
| Exact Backplane identity | **PASS** | `superpowers-backplane@superpowers-backplane`, version `0.1.0`; enabled in Config. `B/plugin.json` names `https://github.com/tvproductions/superpowers-backplane`. Marketplace source is the local `project` directory; this establishes development-package identity, not a verified release revision. |
| Independent installations; no effective conflict | **PASS** | Config and this session’s catalog expose one Backplane package and one upstream package, in separate cache roots. The preservation sentinel is a distinct plugin. |
| Authoritative upstream source | **PASS** | `superpowers@superpowers-dev` comes from `https://github.com/obra/superpowers.git`. Config, `U/.agents/plugins/marketplace.json`, and marketplace installation metadata agree. This satisfies Backplane’s authoritative Git-package route. |
| Observed upstream version/revision | **PASS** | `U/.codex-plugin/plugin.json`: `6.4.1`. Installed HEAD: `5bf4e78011075bcfc0dc295f0724994cd123ee71`; GitHub’s annotated `v6.4.1` tag resolves to that commit. |
| Required upstream skills | **PASS** | All four are catalog-discovered and readable at `U/skills/{using-superpowers,brainstorming,writing-plans,writing-skills}/SKILL.md`. |
| Harness and fresh-session discovery | **PASS** | This fresh session exposes both Backplane skills and all four required upstream skills. Existing [fresh-session read transcript](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/native-skill-read-run.txt) also records successful native-cache reads under Codex `0.155.1`. |
| Git and authenticated `gh` | **PASS** | Git `2.55.0.windows.3`; `gh` `2.101.0`; `gh auth status` succeeds as `ahuimanu`, and repository intake succeeds. |
| Full native issue intake | **PASS** | The exact query from `B/skills/managing-superpowers-backlog/references/github-issue-contract.md` returned all **15 required fields** for [issue #13](https://github.com/tvproductions/superpowers-backplane/issues/13), including native relationships and closure references. |
| Lifecycle flags | **PASS** | `gh issue edit --help` exposes `--add-label` and `--remove-label`; `gh issue close --help` exposes `--reason` with `completed` and `not planned`. |
| Repository lifecycle labels | **PASS** | `gh label list` returned all six labels with appropriate descriptions. #13 has exactly one lifecycle label: `backplane:review`, plus `documentation`. |
| `skill-structure` | **PASS** | Both `B/skills/*/SKILL.md` files have valid delimiters, exact names, descriptions beginning “Use when,” existing directly referenced files, and no detected placeholders. |
| `native-issue-intake` behavioral conformance | **UNKNOWN** | No fresh, scored candidate run. Recovery: execute the primary prompt in `B/tests/scenarios/2026-08-16-native-issue-intake-green.md`. |
| `language-neutral-verification` | **UNKNOWN** | Recovery: execute and score that same file’s language-neutral variation in a fresh candidate session. |
| `lifecycle-transitions` | **UNKNOWN** | Recovery: execute and score `B/tests/scenarios/2026-08-16-lifecycle-transition-refactor.md` hypothetically, without issue mutations. |
| `superpowers-installation` | **UNKNOWN** | Recovery: execute and score `B/tests/scenarios/2026-08-16-superpowers-installation-refactor.md` hypothetically, without installation changes. |

Current upstream [Codex installation documentation](https://github.com/obra/superpowers/blob/v6.4.1/README.md#codex-cli) documents the official marketplace. The installed candidate independently meets Backplane’s accepted authoritative `obra/superpowers` Git-source route; its cache’s local Git remote is not a provenance failure.

Issue #13 remained `OPEN`, with no parent, children, blockers, blocking edges, or closing PR references. `issueType` is explicitly `null`. Its `updatedAt` remained **`2026-09-19T22:25:51Z`** on reread. It was used only for compatibility intake.

Observed Backplane skill SHA-256 values:

```text
backlog:  739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81
handoffs: A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE
```

The installed [installation reference](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0/skills/managing-superpowers-backlog/references/installing-superpowers.md) says “candidate revisions require fresh execution” and “an unscored result is unknown compatibility and fails closed.” Existing bootstrap transcripts use a different upstream revision and skill hashes. Therefore, the package is a verified adoption candidate, but full compatibility is not yet established.
`````
