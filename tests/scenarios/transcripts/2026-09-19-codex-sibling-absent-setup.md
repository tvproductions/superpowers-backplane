# Codex sibling and absent-upstream setup evidence

Disposable fixture: C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287. All fresh sessions used its authenticated state-native CODEX_HOME, not the normal user profile. The sibling consumer at consumer-sibling was a temporary directory with .agents/skills/superpowers junctioned to the separately managed obra/superpowers checkout. The upstream release tested was v6.4.1 / 5bf4e78011075bcfc0dc295f0724994cd123ee71.

## Procedure and score

| Mode | Observed result | Score |
|---|---|---|
| Sibling | Removed only the disposable native upstream plugin; fresh session found the exact sibling origin, commit, clean checkout, four required upstream skills, both installed Backplane skills, full gh intake and lifecycle flags. | PASS for setup and discovery |
| Absent before install | Fresh session found no upstream plugin or skills, found the official catalog entry and stable v6.4.1 route, and reported setup incomplete. | PASS for fail-closed diagnosis |
| Absent after install | codex plugin add superpowers@openai-curated-remote --json installed official 6.4.1; fresh session read four upstream and two Backplane skills from installed caches and passed live gh intake and lifecycle checks. | PASS for stable setup and discovery |
| Restored Git upstream | After the earlier sibling/absent checks, a fresh session read the three installed skill files from separate cache roots. | PASS for restoration discovery |

The official fresh response marked marketplace signature verification and current artifact approval UNKNOWN. Neither is a required Codex setup proof in the approved contract. Official catalog source, package 6.4.1, required skills, separate Backplane installation, and gh capabilities were observed. The official skill hashes reported by that session equal the Git upstream cache hashes for using-superpowers, brainstorming, writing-plans, and writing-skills; the official cache was removed during restoration, so this equality is based on the captured fresh-session hash output. The four behavioral conformance sessions were previously run against the identical current Backplane cache; they were not separately rerun in each upstream mode.

The first official fresh-session command did not start because the temporary directory required --skip-git-repo-check. That command exited 1 before a model session; its finally block restored the Git upstream. The corrected command used that flag and exited 0. No additional login occurred.

The official plugin was removed after the corrected run and superpowers@superpowers-dev was reinstalled. Scoped installed IDs (Backplane, sentinel, Git upstream) matched the pre-mode snapshot. The config, sentinel manifest, Git upstream skill, root user note, and guide user note SHA-256 hashes each matched the snapshot. The official catalog can also list unrelated curated plugins independently of these scoped installations; those entries were not changed by this test. No GitHub issue was mutated.

## Sibling checkout: fresh setup

Session ID: 01a0bbf3-4e97-7253-a259-b0d5fd2ae769

### Exact prompt

Use the installed superpowers-backplane:managing-superpowers-backlog skill and its installing-superpowers reference. Set up Backplane for repository tvproductions/superpowers-backplane using issue #13 only for read-only gh capability intake. This is a disposable consumer fixture. The Backplane plugin is installed. Independently managed upstream Superpowers exists as a sibling checkout exposed at .agents/skills/superpowers. Confirm that no native Superpowers plugin is installed, verify the sibling exact origin and commit, required upstream skills, fresh skill catalog paths, and gh issue fields and lifecycle flags. Report each gate and any UNKNOWN with recovery. Do not install, update, remove, or alter plugins, files, or GitHub issues.

### Exact response

Backplane read-only intake is set up successfully for `tvproductions/superpowers-backplane`, limited to issue #13. No files, plugins, checkouts, or GitHub issues were changed.

| Gate | Result | Evidence |
|---|---|---|
| Backplane plugin | PASS | `superpowers-backplane@superpowers-backplane` enabled, version `0.1.0` |
| Native Superpowers plugin absent | PASS | No enabled `superpowers` plugin entry or cached native package. A `superpowers-dev` marketplace source exists, but no plugin is installed from it |
| Independent sibling checkout | PASS | `.agents/skills/superpowers` is a junction to `C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers`, distinct from Backplane’s plugin root |
| Exact upstream origin | PASS | `https://github.com/obra/superpowers.git` |
| Exact upstream revision | PASS | `5bf4e78011075bcfc0dc295f0724994cd123ee71`, exact tag `v6.4.1` |
| Checkout cleanliness | PASS | `git status --short` returned empty |
| Required upstream skills | PASS | `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills` all exist |
| Fresh catalog discovery | PASS | Current catalog exposes upstream skills through `.agents/skills/superpowers/skills/...` and Backplane skills through the installed `0.1.0` plugin cache |
| GitHub authentication | PASS | Authenticated to `github.com` as `ahuimanu` |
| GitHub CLI capability | PASS | `gh 2.101.0`; label addition/removal and closure reasons are exposed |
| Complete issue intake | PASS | All required JSON fields returned for issue #13 |
| Lifecycle-label catalog | PASS | All six `backplane:*` labels exist with contract-compatible descriptions |
| Read-only preservation | PASS | No mutation command was issued |

Issue #13 lifecycle facts:

- State: `OPEN`; `stateReason` empty.
- Revision: `2026-09-19T22:25:51Z`.
- Leaf: yes—no parent and zero sub-issues.
- Dependencies: zero blockers and zero blocking edges.
- Lifecycle label: exactly one, `backplane:review`.
- Unrelated label preserved: `documentation`.
- Linked closing PRs: none.
- Executable-body headings: complete.
- Artifacts: approved design and plan are cited.
- Captured: yes.
- Covered: yes, based on the issue’s cited approved artifacts.
- Eligible: no—it is in review, not `backplane:ready`.
- Selected: not established by read-only evidence.
- Complete: no; it remains open.

UNKNOWN: full current-revision compatibility conformance. This intake establishes the native issue-intake and discovery gates, but fresh isolated runs of `skill-structure`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation` were not performed. Recovery: run those named scenarios in fresh sessions; lifecycle-transition verification requires separate authorization if it would mutate disposable issue #13.


## Upstream absent: fresh diagnosis before installation

Session ID: 01a0bbf6-43f9-7c60-b546-dd538662540c

### Exact prompt

Use the installed superpowers-backplane:managing-superpowers-backlog skill and its installing-superpowers reference. In this disposable Codex session, Backplane is installed but upstream Superpowers is absent. Check the plugin list and this fresh skill catalog, and use issue #13 in tvproductions/superpowers-backplane only for read-only gh capability intake. Determine the current stable upstream release from the authoritative source and give the exact Codex native plugin installation route and compatibility/discovery gates. Report setup as incomplete until upstream is actually installed. Do not mutate plugins, files, or GitHub issues in this session.

### Exact response

Setup is **incomplete**. Backplane is installed, but upstream Superpowers is not installed or discoverable in this fresh session.

### Findings

- Codex’s plugin catalog contains the official `Superpowers` plugin:
  - ID: `plugins~Plugin_60aea7460bd4819199fd97a9553a5e12`
  - Status: enabled/available
  - Installed: **false**
- The supplied recommended-plugin list does not include Superpowers.
- The fresh skill catalog exposes only Backplane’s two skills; it does not expose upstream `superpowers:using-superpowers`, `brainstorming`, `writing-plans`, or `writing-skills`.
- Backplane is independently present as version `0.1.0`; that does not satisfy its upstream dependency.
- The authoritative upstream release is **Superpowers v6.4.1**, published September 19, 2026. Its Codex manifest also declares version `6.4.1`. [Release](https://github.com/obra/superpowers/releases/tag/v6.4.1) · [Upstream repository](https://github.com/obra/superpowers)

### Exact Codex-native installation route

Upstream’s v6.4.1 README documents the official Codex marketplace route:

- Codex App: open **Plugins** in the sidebar → find **Superpowers** under **Coding** → click `+` → follow the prompts.
- Codex CLI: enter `/plugins` → search for `superpowers` → choose **Install Plugin**.

The catalog entry found above is the correct package; do not copy Superpowers files into Backplane or create an extra checkout merely to emulate plugin installation.

No installation was performed in this session.

### Compatibility and discovery gates

After installation, all of these must pass before setup can be called operational:

1. Record package identity, official marketplace source, installed version, and resolved tag/revision where exposed. If neither version nor revision is observable, compatibility remains unknown.
2. Start a **fresh Codex session** and confirm these upstream skills are discoverable and operational:
   - `superpowers:using-superpowers`
   - `brainstorming`
   - `writing-plans`
   - `writing-skills`
3. Confirm both Backplane skills remain independently discoverable.
4. Verify upstream provenance and reject duplicate, conflicting, or lookalike installations.
5. Verify authenticated `gh` access.
6. Run the complete native issue-intake query against a real issue.
7. Confirm `gh issue edit --help` supports label addition/removal and `gh issue close --help` supports closure reasons.
8. Pass all named Backplane conformance checks:
   - `skill-structure`
   - `native-issue-intake`
   - `language-neutral-verification`
   - `lifecycle-transitions`
   - `superpowers-installation`

Every expectation must pass. Missing captures, unavailable fields, divergent discovery, or unscored results fail closed as unknown compatibility.

### Read-only capability intake

Issue [tvproductions/superpowers-backplane#13](https://github.com/tvproductions/superpowers-backplane/issues/13) successfully returned the complete required field set through `gh 2.101.0`. It is open, has no parent, children, or blockers, and has exactly one lifecycle label, `backplane:review`, while preserving `documentation`.

The CLI also exposes the required label and closure-reason operations. These checks establish the necessary `gh` capability surface only; they do not establish upstream compatibility because Superpowers has not been installed and the fresh-session discovery/conformance gates have not run.

No plugins, files, or GitHub issues were mutated.


## Official stable upstream: fresh setup after installation

Session ID: 01a0bbfe-1f15-72c0-824f-bee7e1edd0cd

### Exact prompt

Read-only setup check for Superpowers Backplane against issue tvproductions/superpowers-backplane#13. From installed plugin caches, verify official Superpowers plugin identity, source, version, required using-superpowers/brainstorming/writing-plans/writing-skills, both Backplane skills, gh auth, all native issue intake fields, and lifecycle flags. Do not install, login, change files, or mutate issues. Report exact evidence and UNKNOWN where unproved.

### Exact response

Read-only setup check passed, with two provenance limits marked `UNKNOWN`. No files, authentication, labels, or issues were changed.

### Superpowers plugin

- Identity: `superpowers`
- Display name: `Superpowers`
- Version: `6.4.1`
- Author: Jesse Vincent / `https://github.com/obra`
- Source: `https://github.com/obra/superpowers`
- Cache channel: `openai-curated-remote`
- Manifest: [plugin.json](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/openai-curated-remote/superpowers/6.4.1/.codex-plugin/plugin.json)
- Manifest SHA-256: `97858971F2670CF7CBBC625D43F9F2568BBC7E362FD1CEBC202A1332A705C364`
- Bundled README explicitly says Codex App/CLI installation is through the official Codex plugin marketplace.
- Backplane’s dependency record identifies stable release `v6.4.1`, published `2026-09-19T00:32:44Z`, resolved commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`.
- End-to-end marketplace signature/cache integrity: **UNKNOWN**. The cache contents and metadata are internally consistent, but no independent signature or remote commit comparison was performed.

Required upstream skills are present and readable:

| Skill | SHA-256 |
|---|---|
| `using-superpowers` | `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA` |
| `brainstorming` | `A32D2255354775AA124855AA7100CF276BEA096FFF4EBB3A0EDF57BE216E6C72` |
| `writing-plans` | `0BC3D36590F7B2C323ED3EC18FF77E9F8ED57AF42F5680A02B11A2D20DE265CF` |
| `writing-skills` | `BBDFE742F853562E643A3D40D64476359D47881E39CEF80A189283FA26D11AB9` |

### Backplane plugin

- Identity: `superpowers-backplane`
- Version: `0.1.0`
- Source: `https://github.com/tvproductions/superpowers-backplane`
- Manifest SHA-256: `BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E`
- Manifest: [plugin.json](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0/plugin.json)

Both required Backplane skills are present and readable:

| Skill | SHA-256 |
|---|---|
| `managing-superpowers-backlog` | `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81` |
| `managing-superpowers-handoffs` | `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE` |

Native issue contract SHA-256: `D6DD8B8C2D1EA5836848FDAC90AECF7002AB865DAE612E94A560EBE7800D3121`.

### GitHub access

- `gh` version: `2.101.0`
- Host: `github.com`
- Account: `ahuimanu`
- Active and authenticated through keyring
- Protocol: HTTPS
- Scopes: `gist`, `read:org`, `repo`, `workflow`
- Authentication validity during this check: verified by successful live issue and label reads.
- Token value was masked and not exposed.

### Issue #13 native intake

Live URL: `https://github.com/tvproductions/superpowers-backplane/issues/13`

All 13 contract-required fields were requested and returned:

| Field | Observed value |
|---|---|
| `number` | `13` |
| `title` | `[verification fixture] Codex Issue #3 lifecycle` |
| `body` | Present; contains Objective, Bounded Scope/Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts |
| `state` | `OPEN` |
| `stateReason` | Empty string; reason semantics **UNKNOWN/not supplied** |
| `issueType` | `null`; no native issue type assigned |
| `labels` | `documentation`, `backplane:review` |
| `parent` | `null` |
| `subIssues` | 0 |
| `subIssuesSummary` | total 0, completed 0, 0% |
| `blockedBy` | 0 |
| `blocking` | 0 |
| `closedByPullRequestsReferences` | Empty |
| `updatedAt` | `2026-09-19T22:25:51Z` |
| `url` | Returned and matches issue #13 |

The body satisfies the executable-leaf heading contract and names approved design and plan artifacts. Whether those artifact contents remain approved/current was not independently evaluated here: **UNKNOWN**.

### Lifecycle evidence

All six required labels exist, with descriptions matching the installed contract:

- `backplane:backlog` — “Captured but not ready for execution”
- `backplane:designing` — “Issue, specification, or plan is being brought to approval”
- `backplane:ready` — “Approved and dependency-ready for execution”
- `backplane:active` — “Superpowers execution is in progress”
- `backplane:blocked` — “Work cannot advance; the reason is recorded in the issue”
- `backplane:review` — “Implementation is submitted and awaiting final review/integration”

Issue #13 is valid on lifecycle-label cardinality: exactly one `backplane:*` label, `backplane:review`, while retaining unrelated label `documentation`.

CLI lifecycle capabilities were also verified from local help:

- `gh issue edit`: `--add-label`, `--remove-label`, native parent/sub-issue and blocking relationship flags.
- `gh issue close --reason`: supports `completed`, `not planned`, and `duplicate`.

A final re-read returned the same `updatedAt` value, state, and labels, confirming this check caused no observable issue mutation.


## Restored independent Git upstream: fresh installed-skill discovery

Session ID: 01a0bbf8-34a9-7670-a613-0502e556b87c

### Exact prompt

In this fresh disposable Codex session after stable upstream installation, inspect the installed plugin IDs and sources, then open the SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs from their installed catalog paths. Report each exact catalog path, package source, upstream version and resolved revision if available. Do not use repository-local junctions or change any plugin, file, or GitHub issue.

### Exact response

Inspected read-only from the installed catalog cache. No repository-local junctions were opened, and nothing was modified.

| Skill | Installed plugin ID | Exact catalog path | Version | Package source | Resolved revision |
|---|---|---|---|---|---|
| `superpowers:using-superpowers` | `superpowers@superpowers-dev` | [SKILL.md](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-dev/superpowers/6.4.1/skills/using-superpowers/SKILL.md) | `6.4.1` (`v6.4.1`) | `https://github.com/obra/superpowers.git` | `5bf4e78011075bcfc0dc295f0724994cd123ee71` |
| `superpowers-backplane:managing-superpowers-backlog` | `superpowers-backplane@superpowers-backplane` | [SKILL.md](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0/skills/managing-superpowers-backlog/SKILL.md) | `0.1.0` | Configured local marketplace source: `\\?\C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\project`; manifest repository: `https://github.com/tvproductions/superpowers-backplane` | Not recorded in installed marketplace metadata |
| `superpowers-backplane:managing-superpowers-handoffs` | `superpowers-backplane@superpowers-backplane` | [SKILL.md](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0/skills/managing-superpowers-handoffs/SKILL.md) | `0.1.0` | Same Backplane package source above | Not recorded in installed marketplace metadata |

Enabled plugin IDs found:

- `superpowers@superpowers-dev`
- `superpowers-backplane@superpowers-backplane`
- `backplane-preservation-sentinel@superpowers-backplane` — catalog version `0.0.1`, from the same configured local marketplace source.

The upstream revision was corroborated by both `.codex-marketplace-install.json` and the marketplace checkout’s read-only `HEAD`; it resolves exactly to tag `v6.4.1`.
