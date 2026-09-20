# Claude Code #18 setup session transcript excerpts

Only final host responses and exact prompts are copied below. The raw Claude JSONL remains in disposable profiles; credential-bearing settings and tool outputs are excluded. Each copied response is unedited. Both setup calls used `--permission-mode plan --output-format json --max-turns 20`, read-only issue #18 intake, and a neutral temporary project. Their result subtype was `error_max_turns` at turn 21, so each was resumed in the same session with tools disabled for a report of already observed checks.

## native setup session

Initial prompt: `Set up Superpowers Backplane in this Claude Code session.`
Appended system prompt: `Use existing issue tvproductions/superpowers-backplane#18 for read-only intake. Report source, revision, capabilities, and skill identities. Do not mutate GitHub issue state.`
Initial session ID: `7a45122c-9463-4db8-acb7-fed45053714b`; result: `error_max_turns`. No final setup verdict was inferred from that result.
Continuation prompt: `Continue only the setup report from checks already performed. Use no tools. Mark unobserved checks UNKNOWN; do not infer success. Report Backplane and upstream source/version, gh capabilities, and skill identities from the existing tool record.`
Continuation result: `success`; tools disabled with `--tools ''`.

Unedited continuation response:

~~~~text
# Superpowers Backplane — Claude Code setup report

Read-only intake against `tvproductions/superpowers-backplane#18`. No GitHub issue state, plugin state, or repository file was changed. Everything below comes from checks actually executed in this session; anything not observed is marked `UNKNOWN`.

Active config dir: `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-241ec92c05e84296bc7a2df74be839d3` · Claude Code `2.1.241` · cwd `…\backplane-claude-18-native-c50b2699180e4cbca41c7b10cbcbd8d6` (empty, not a git repo).

## Backplane package and revision — PASS

| Field | Observed |
|---|---|
| Package | `superpowers-backplane@superpowers-backplane` 0.1.0, scope user, enabled |
| Effective installs | exactly one (`claude plugin list`; `~/.claude` registry holds only `gz-skills`) |
| Marketplace | `superpowers-backplane`, source `directory` → `…\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane`, plugin source `./` (loads in place at repo root) |
| Revision | `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a`, detached HEAD, `git status --porcelain` empty |
| Origin | `https://github.com/tvproductions/superpowers-backplane.git` |
| Published | `gh api repos/…/commits/d42cff1…` returned the same SHA |
| Package validation | `claude plugin validate --strict` → ✔ passed |
| Cache copy | `<config>/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0` — both `SKILL.md` digests byte-identical to the source root |

## Upstream Superpowers — PASS, independent

| Field | Observed |
|---|---|
| Package | `superpowers@superpowers-dev` **6.4.1**, scope user, enabled |
| Marketplace | `superpowers-dev`, source `directory` → `C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers` |
| Catalog authorship | that manifest is upstream's own `.claude-plugin/marketplace.json` (owner Jesse Vincent, plugin source `./`) |
| Git provenance | origin exactly `https://github.com/obra/superpowers.git`; HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71` = tag `v6.4.1`; worktree clean |
| Published | confirmed via `gh api repos/obra/superpowers/commits/5bf4e78…` |
| Channel | `gh release view` → `v6.4.1`, published 2026-09-19T00:32:44Z, the current latest stable; matches the `SUPERPOWERS.md` record |
| Required skills | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` all present |
| Separation | distinct package, marketplace, root, and version from Backplane |

**Mode:** upstream is a native Claude Code plugin whose marketplace is a local directory clone of the authoritative `obra/superpowers` repo pinned at the published v6.4.1 tag — in-place adoption of an authoritative checkout, not `claude plugin marketplace add obra/superpowers` over GitHub. Permitted by `references/installing-superpowers.md`; recorded because it is the mode under test. The existing upstream installation was not updated or replaced.

## `gh` capabilities — PASS

- `gh` **2.101.0** (2026-09-15); `gh auth status` → github.com, account **ahuimanu** (keyring), scopes `gist, read:org, repo, workflow`.
- Full 15-field intake on #18 exited 0 and returned **every** required field: `number, title, body, state, stateReason, issueType, labels, parent, subIssues, subIssuesSummary, blockedBy, blocking, closedByPullRequestsReferences, updatedAt, url`.
- `gh issue edit --help` exposes `--add-label` and `--remove-label`.
- `gh issue close --help` exposes `-r, --reason {completed|not planned|duplicate}`.
- All six `backplane:*` lifecycle labels exist with descriptions matching their contract meanings.

## Skill identities — 3 of 3 discovered and invoked

| Skill | Effective root | `SKILL.md` sha256 |
|---|---|---|
| `superpowers:using-superpowers` | `…\.agents\superpowers\skills\using-superpowers\` (upstream 6.4.1) | `82c5c8866ad7f5dd4440ce66bd7806ba48a2f13771beae5cf112e53f08fe36ba` |
| `superpowers-backplane:managing-superpowers-backlog` | `…\backplane-claude-17-source-…\superpowers-backplane\skills\managing-superpowers-backlog\` | `739a16fcdf2ee5adab0514f5a44db0629dcce558985fe5a31d71dd2606ac1e81` |
| `superpowers-backplane:managing-superpowers-handoffs` | same Backplane source root | `a6052755128be9c7d268d71241dd389b9bf1c720834e47e61cbf9535f4ca92de` |

Each was exercised, not merely listed: `using-superpowers` was injected in full at session start; both Backplane skills were invoked and returned their bodies plus base directories. The two packages resolved to separate roots, confirming independence at load time.

## Issue #18 intake — no mutation

OPEN · `backplane:active` (exactly one lifecycle label) · executable leaf (`subIssues.total = 0`) · parent **#1** OPEN · `blockedBy` **#17 CLOSED** · `blocking` **#19** OPEN · `issueType` null · `stateReason` empty · `closedByPullRequestsReferences` empty · `updatedAt` **2026-09-20T17:29:58Z**. All seven required contract headings present.

## UNKNOWN — failed or unobserved check, with recovery

1. **Plan artifact absent from the installed revision.** #18 links `docs/superpowers/plans/2026-09-20-claude-code-setup-and-upstream-adoption.md` (PR #30, merged 2026-09-20T17:26:50Z; `main` = `4c94aa627e4b59da5e7c942e9d42c04edac56158`). Installed `d42cff1` is an ancestor of `main` but 11 commits behind and does not contain that file; the checkout has `2026-09-20-claude-code-package-and-installation.md` instead. *Recovery:* read the plan from origin `main`, or re-pin to a reviewed 40-char commit containing it and re-run the checkout verification block. Do not point the marketplace at moving `main`.
2. **Second fresh-session `/help` discovery check — UNKNOWN.** Not performed; this session is invocation evidence, not the separate fresh session the guide requires. *Recovery:* operator runs it and inspects Custom commands for all three skills.
3. **Repository anchor — UNKNOWN.** The working directory is empty and not a git repo, so repo-root-dependent operations (handoff artifact writes, local spec/plan reads) have no anchor here. *Recovery:* run those from a Backplane checkout.
4. **Five named conformance checks — UNKNOWN.** `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation` were not scored. The `gh` surface underlying `native-issue-intake` passed, but no scenario rubric was run. *Recovery:* fresh sessions per `tests/scenarios/`.
5. **Failure probes — UNKNOWN.** Unknown/versionless provenance, duplicate or conflicting installs, dirty checkout, path collision, unavailable `gh`, and incompatible upstream were not exercised. *Recovery:* deliberate setup with before/after hashes or native state comparison.
6. **Other two upstream modes — UNKNOWN.** Only this native-mode session was probed; the sibling-checkout and absent-upstream modes were not.

Setup is usable now for read-only backlog and handoff work against this repository. #18 cannot be called verified: its acceptance criteria span three modes and the failure-probe set, and items 2–6 above are unobserved. Issue state is unchanged — advancing it requires a separate, explicitly authorized backlog mutation.

The full record is written to `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-241ec92c05e84296bc7a2df74be839d3\plans\set-up-superpowers-backplane-dreamy-falcon.md`.
~~~~

### native direct fresh skill sessions

Session `18736898-543c-4766-846b-32d6218aa4f6`; result `success`; prompt: `Invoke superpowers:using-superpowers for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
Yes — the real `Skill` tool loaded it (not just the SessionStart injection).

**Evidence:** the tool returned `Launching skill: superpowers:using-superpowers`, followed by the skill body prefixed with a base directory the hook injection did not contain:

```
C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers
```

**Package:** `superpowers` (the namespace before the colon), resolved on disk from the bundled plugin directory `.agents\superpowers\` inside the `superpowers-backplane` repo at `C:\Users\Jeff\source\repos\agents\superpowers-backplane`. That is a distinct namespace from `superpowers-backplane:*`, which supplies the backlog/handoff skills in the same listing.

Two other observations from the check:

- The loaded body is byte-identical in substance to what the SessionStart hook pre-injected (same frontmatter-free rule text, Skill Priority, Red Flags table, Platform Adaptation list, User Instructions). So the hook is mirroring the same source file, not a stale copy.
- The skill points at `references/claude-code-tools.md` for this harness; that file sits under the base directory above and was not read as part of this check.

Nothing was modified — the only action taken was the skill load itself.

One process note: the plan-mode instructions say to close the turn with `ExitPlanMode`, but that tool isn't exposed in this session's toolset, so I can't call it. There's also nothing to implement here — this was a read-only discovery check, and the result is above. If you want me to go further (e.g. read `references/claude-code-tools.md`, or diff the on-disk skill against the hook-injected text line by line), say the word.
~~~~

Session `c4e3713b-7dfc-4137-9de2-fd89ce2bc455`; result `success`; prompt: `Invoke superpowers-backplane:managing-superpowers-backlog for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
Yes — the real `Skill` tool loaded it.

**What happened:**
- Tool call: `Skill(skill: "superpowers-backplane:managing-superpowers-backlog")`
- Result: `Launching skill: superpowers-backplane:managing-superpowers-backlog`
- The skill body was then injected as a turn with an explicit base directory.

**Package:** `superpowers-backplane` (not `superpowers`). It was listed in the available-skills block under that prefix, and it resolved to:

```
C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane\skills\managing-superpowers-backlog
```

That path confirms it came from the Backplane source checkout, a separate package from the upstream `superpowers:*` skills (`brainstorming`, `writing-plans`, `systematic-debugging`, etc.), which the skill itself treats as a required external dependency rather than something it bundles.

**Content loaded:** the top-level `SKILL.md` — overview, operation-selection table, intake rules, the product-arc vocabulary (captured / covered / eligible / selected / complete), lifecycle-transition rules, and common mistakes. It references three files I did not load: `references/github-issue-contract.md`, `references/superpowers-binding.md`, and `references/installing-superpowers.md`.

**Limits of this check:** I stopped at the load. I did not perform any backlog operation, and two things would block one here anyway:

1. In this session I have no filesystem or shell tools — only `Skill` plus the Claude Docs and Google Drive MCP servers. So I can't read the three `references/` files to confirm they exist on disk, and I can't run `gh`.
2. The working directory is not a git repository, and no upstream Superpowers installation is verified, so the skill's stated prerequisites ("authenticated `gh` access and an operational upstream Superpowers installation") are unmet.

Nothing was mutated, and no GitHub calls were attempted.
~~~~

Session `f9914a8c-51f8-40b8-b307-1fb2b45362d7`; result `success`; prompt: `Invoke superpowers-backplane:managing-superpowers-handoffs for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
Yes — the real `Skill` tool loaded it, not a paraphrase from context.

**Evidence:**
- Tool call: `Skill(skill="superpowers-backplane:managing-superpowers-handoffs")` returned `Launching skill: superpowers-backplane:managing-superpowers-handoffs`, followed by the skill body injected as a new turn.
- Base directory reported by the loader:
  `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane\skills\managing-superpowers-handoffs`

**Package:** `superpowers-backplane` — a different package from `superpowers` (which supplies `using-superpowers`, `brainstorming`, `writing-plans`, etc., and was injected at session start via the SessionStart hook rather than through the Skill tool). The path segment `.../backplane-claude-17-source-.../superpowers-backplane/skills/...` confirms the origin, and it sits under a `-source-` temp root distinct from the session's project/plan root (`backplane-claude-17-...`) and the working directory (`backplane-claude-18-native-...`).

**What I did not do:** no CREATE and no RESUME. Per your args, this was discovery only, so I did not run the operational-prerequisite validation, candidate selection, evidence probes, or write any handoff artifact. The skill's own contract references (`references/handoff-contract.md`, `references/resume-assessment.md`) were also not read — they're only required before executing either operation.

Say the word if you want an actual CREATE or RESUME run; those have their own required report shapes, and CREATE writes a file, which plan mode currently blocks.
~~~~

The wrapper re-fetched all 15 native #18 fields after the three calls and printed `ISSUE STATE UNCHANGED`.

## sibling setup session

Initial prompt: `Set up Superpowers Backplane in this Claude Code session.`
Appended system prompt: `Use existing issue tvproductions/superpowers-backplane#18 for read-only intake. Report source, revision, capabilities, and skill identities. Do not mutate GitHub issue state.`
Initial session ID: `b2b0b833-60cf-4df2-8ed8-83e54763d870`; result: `error_max_turns`. No final setup verdict was inferred from that result.
Continuation prompt: `Continue only the setup report from checks already performed. Use no tools. Mark unobserved checks UNKNOWN; do not infer success. Report Backplane and upstream source/version, gh capabilities, and skill identities from the existing tool record.`
Continuation result: `success`; tools disabled with `--tools ''`.

Unedited continuation response:

~~~~text
## Superpowers Backplane setup — read-only report

Host: Claude Code 2.1.241 · isolated `CLAUDE_CONFIG_DIR` at `…\Temp\backplane-claude-18-62f1d7dda2704635a266bdacedfd7c3f` · cwd `…\backplane-claude-18-sibling-cd29b19…` (empty, not a git repo). Upstream mode: **sibling checkout, adopted in place**.

### Backplane package — PASS

| Item | Observed |
|---|---|
| Plugin ID | `superpowers-backplane@superpowers-backplane`, scope `user`, enabled in `settings.json` |
| Version | `0.1.0` (`.claude-plugin/plugin.json` and `marketplace.json` agree; one plugin, source `./`) |
| Marketplace source | `directory` → `…\Temp\backplane-claude-17-source-c9121b72…\superpowers-backplane` |
| Revision | `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a` — recorded `gitCommitSha` equals checkout `HEAD` |
| Origin | `https://github.com/tvproductions/superpowers-backplane.git` (accepted form) |
| Working tree | `git status --porcelain` empty → clean |
| Effective installs | Exactly one registered in this session's `installed_plugins.json`; user-level `~/.claude` carries only `gz-skills@gz-skills` |
| Canonical skills | `skills/managing-superpowers-backlog/SKILL.md` and `skills/managing-superpowers-handoffs/SKILL.md` both present at the package root |

Flags on this pin:
- `git describe` returns a bare `d42cff1` — **no release tag**. The guide asks for a reviewed/stable release commit; this is a plain commit.
- Publication check at origin (`gh api repos/…/commits/<sha>`) — **UNKNOWN**, not run.
- `claude plugin validate --strict` — **UNKNOWN**, not run.
- The plan issue #18 cites `docs/superpowers/plans/2026-09-20-claude-code-setup-and-upstream-adoption.md`; the installed checkout does not contain it (it has `2026-09-20-claude-code-package-and-installation.md`). The installed revision **predates** the plan named in the issue.
- A second Backplane copy exists on disk at `C:\Users\Jeff\source\repos\agents\superpowers-backplane` (branch `issue/18-claude-setup`, `80ff11a`, clean). It is **not** registered as a plugin here, so it is not a second effective install — but it is the repo whose `.agents/superpowers` supplies upstream (below).

### Upstream Superpowers — PASS, with a provenance caveat

| Item | Observed |
|---|---|
| Path | `C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers` |
| Origin | `https://github.com/obra/superpowers.git` → owner/repo exactly `obra/superpowers` |
| Revision | `5bf4e78011075bcfc0dc295f0724994cd123ee71`, `git describe` → `v6.4.1` (exact tag) |
| Version | `6.4.1` in `.claude-plugin/plugin.json`; marketplace `superpowers-dev`, plugin name `superpowers`, source `./` |
| Working tree | `git status --short` empty → clean |
| Required skills | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` — all four `SKILL.md` present |
| Path independence | Differs from the effective Backplane package root (Temp checkout) |

Evidence it is the source actually serving this session: the `SessionStart:startup` hook record in the transcript matches `hooks/session-start` in that checkout, registered by its `hooks.json` via `${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd`; the injected `using-superpowers` text matches that checkout's `SKILL.md` byte-for-byte including the six-entry Platform Adaptation list; and this session's `superpowers:*` roster matches that checkout's 15 skill directories exactly.

Caveats:
- Upstream is **not** in this session's `installed_plugins.json` or `known_marketplaces.json`. It is harness/SDK-provided (a `plugins/data/superpowers-inline` data directory exists). The exact registration mechanism is **UNKNOWN**; provenance was established from file identity and hook evidence, not from a plugin registry entry.
- The installation reference warns that the repo's own development checkout at `.agents/superpowers` is a separate checkout whose existence does not prove an operational plugin. Here the hook and content evidence show it *is* operational for this session — but the adoption rests on that evidence rather than on a package manifest.
- Nothing in upstream was installed, updated, relocated, or modified.

### GitHub CLI capabilities — PASS

- `gh` 2.101.0 (2026-09-15); authoring baseline was 2.97.0.
- `gh auth status`: logged in to github.com as `ahuimanu` (keyring), active account, https, scopes `gist, read:org, repo, workflow`.
- Required intake query against `tvproductions/superpowers-backplane#18` returned **all 15 required fields**: `number, title, body, state, stateReason, issueType, labels, parent, subIssues, subIssuesSummary, blockedBy, blocking, closedByPullRequestsReferences, updatedAt, url`. (`issueType` is `null` and `stateReason` is `""` — fields present, values empty; not a capability failure.)
- `gh issue edit --help` exposes `--add-label` and `--remove-label`.
- `gh issue close --help` exposes `-r, --reason {completed|not planned|duplicate}`.
- `gh label list` shows all six `backplane:*` labels with matching descriptions.

### Issue #18 intake (read-only)

`OPEN`, `backplane:active` (exactly one lifecycle label, valid state), parent #1 *Ship an adoptable Backplane v0.1.0 release*, no sub-issues, `blockedBy` #17 (CLOSED — resolved), `blocking` #19 (OPEN), no closing PRs, `updatedAt` `2026-09-20T17:29:58Z`. Body carries all six required contract headings.

No mutation occurred. Only `gh issue view`, `--help`, and `gh label list` were run. Two separate fetches of #18 returned the identical `updatedAt`, and the label set was unchanged.

### Skill identities

| Skill | Source | Status |
|---|---|---|
| `superpowers:using-superpowers` | upstream checkout, `sha256 82c5c886…36ba` | Loaded at session start via upstream hook — **PASS** |
| `superpowers-backplane:managing-superpowers-backlog` | Temp Backplane checkout, `sha256 739a16fc…1e81` | Invoked this session; returned its SKILL.md with base dir = that checkout — **PASS** |
| `superpowers-backplane:managing-superpowers-handoffs` | Temp Backplane checkout, `sha256 a6052755…92de` | Listed in the catalog; **not invoked** — operational status **UNKNOWN** |

The two namespaces (`superpowers:` vs `superpowers-backplane:`) remain separate, from separate roots.

### UNKNOWN — not observed, not inferred

- **Fresh-session discovery check.** The guide requires a *second, new* session inspecting `/help` custom commands and invoking each of the three skills read-only. This is the setup session; that check was not performed. UNKNOWN.
- **`managing-superpowers-handoffs` invocation.** UNKNOWN.
- **All five named conformance checks** — `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`. None executed. UNKNOWN.
- **Backplane revision published at origin** and **`claude plugin validate --strict`**. UNKNOWN.
- **Failure probes** (unknown/versionless provenance, duplicate installs, dirty checkout, path collision, unavailable `gh`, incompatible upstream). None exercised. UNKNOWN.

Recovery actions for the UNKNOWNs: start a fresh Claude Code session against this same config dir and invoke all three skills to close the discovery and handoffs gaps; run `gh api repos/tvproductions/superpowers-backplane/commits/d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a --jq .sha` and `claude plugin validate --strict <checkout>` to close the package gaps; run the five conformance scenarios from `tests/scenarios/` with captured response records to close the compatibility gap.

**Verdict:** setup is operational for the checks actually observed — one Backplane install at `d42cff1`, an independent upstream `obra/superpowers` v6.4.1 sibling checkout, authenticated `gh` with complete intake and label/closure capability, and three distinct skill identities across two packages. Full conformance is **not** established; the items above are UNKNOWN rather than passing.
~~~~

### sibling direct fresh skill sessions

Session `31f6b787-ff79-482f-b9a1-f5c759da7e00`; result `success`; prompt: `Invoke superpowers:using-superpowers for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
Yes — the real Skill tool loaded it.

**Evidence of an actual tool invocation (not the SessionStart injection):**
- The `Skill` tool returned `Launching skill: superpowers:using-superpowers`, followed by the skill body prefixed with a line the hook-injected copy did not have:
  `Base directory for this skill: C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers`

**Package / source:** the `superpowers` skill package, vendored inside the `superpowers-backplane` repo at `.agents/superpowers/skills/` — so the skill namespace `superpowers:` resolves to `C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers`, not to a user-level `~/.claude` install. The separately listed `superpowers-backplane:*` skills (`managing-superpowers-backlog`, `managing-superpowers-handoffs`) are a distinct package from the same repo.

**Content check:** the tool-loaded version matches the hook-injected text verbatim (the rule, skill-priority ordering, red-flags table, platform-adaptation list, user-instructions precedence). Nothing was stale or divergent.

Two notes on the state of this session, since they affect what you can ask me to do next:

1. **Plan mode is active**, and the platform reference file the skill points to (`references/claude-code-tools.md`, under the base directory above) — I did not read it. My tool set in this session contains only `Skill`, the Claude Docs MCP tools, and the Google Drive MCP tools; there is no file-read, grep, or Bash tool available, so I can't open that reference or verify the package contents on disk. My statement about the base directory comes from the tool's own output, not from inspecting the filesystem.
2. For the same reason I cannot write the plan file at `...\plans\invoke-superpowers-using-superpowers-for-rosy-bachman.md`, and I have no `ExitPlanMode` tool to call. This request was a read-only discovery check with no implementation behind it, so there's no plan to approve — but if you did want a plan written, you'd need to re-run with the file tools enabled.
~~~~

Session `8c5a1e15-418a-42a9-b828-89d77f30c581`; result `success`; prompt: `Invoke superpowers-backplane:managing-superpowers-backlog for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
Yes — the real `Skill` tool loaded it, not a paraphrase from memory.

**What loaded:**
- **Skill:** `superpowers-backplane:managing-superpowers-backlog`
- **Package:** `superpowers-backplane` (a separate plugin from `superpowers` itself — the two appear as distinct namespaces in the skill listing)
- **Base directory reported by the tool:**
  `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane\skills\managing-superpowers-backlog`

**Two things worth flagging:**

1. The skill resolved out of the `backplane-claude-17-source-…` temp tree, while this session's working directory is `backplane-claude-18-sibling-…`. The plugin source and the working dir are different sandboxes — expected if 17 is the source checkout and 18 is a sibling workspace, but worth confirming that's intentional.
2. The loaded body is the skill's top-level instructions only. It references three files I have **not** read (`references/github-issue-contract.md`, `references/superpowers-binding.md`, `references/installing-superpowers.md`). The skill states the issue contract must be read completely for *every* operation, so a real backlog operation would need those loaded too.

No discovery beyond the load was performed — no `gh` calls, no file reads, no mutations. Plan mode is active and nothing here required changes, so there's nothing to propose executing. Tell me if you want the three reference files read next, or an actual `gh`-backed orientation pass against a specific repo.
~~~~

Session `726f9647-40f8-4d84-a142-2cf5f8a0c0a0`; result `success`; prompt: `Invoke superpowers-backplane:managing-superpowers-handoffs for a harmless read-only discovery check. State whether the actual Skill tool loaded it and from which package.`

Unedited response:

~~~~text
I couldn't write the plan file — `Write` is disabled for this session (and `ExitPlanMode` isn't among my available tools either), so the plan-mode file workflow can't be completed. The only tools exposed here are `Skill` and the Claude Docs / Google Drive MCP servers.

That doesn't affect the answer, since the requested deliverable was the statement itself, which is above: the real `Skill` tool loaded `managing-superpowers-handoffs` from the **`superpowers-backplane`** package, resolved at the `backplane-claude-17-source-…\superpowers-backplane\skills\managing-superpowers-handoffs` base directory.

If you want that written down, tell me where and with which tool — or re-run with `Write` enabled and I'll put the plan at the path the harness specified.
~~~~

The wrapper re-fetched all 15 native #18 fields after the three calls and printed `ISSUE STATE UNCHANGED`.

## Direct Skill tool record cross-check

| Mode | Session | Recorded `Skill` tool input | Tool uses | Loaded source root |
|---|---|---|---:|---|
| native | `18736898-543c-4766-846b-32d6218aa4f6` | `superpowers:using-superpowers` | 1 | `.agents/superpowers/skills/using-superpowers` |
| native | `c4e3713b-7dfc-4137-9de2-fd89ce2bc455` | `superpowers-backplane:managing-superpowers-backlog` | 1 | pinned Temp Backplane `skills/managing-superpowers-backlog` |
| native | `f9914a8c-51f8-40b8-b307-1fb2b45362d7` | `superpowers-backplane:managing-superpowers-handoffs` | 1 | pinned Temp Backplane `skills/managing-superpowers-handoffs` |
| sibling | `31f6b787-ff79-482f-b9a1-f5c759da7e00` | `superpowers:using-superpowers` | 1 | `.agents/superpowers/skills/using-superpowers` |
| sibling | `8c5a1e15-418a-42a9-b828-89d77f30c581` | `superpowers-backplane:managing-superpowers-backlog` | 1 | pinned Temp Backplane `skills/managing-superpowers-backlog` |
| sibling | `726f9647-40f8-4d84-a142-2cf5f8a0c0a0` | `superpowers-backplane:managing-superpowers-handoffs` | 1 | pinned Temp Backplane `skills/managing-superpowers-handoffs` |

## Task 4 failure-probe host responses

Each prompt below is the exact user prompt sent to a fresh normal-permission Claude session. The final responses are copied unedited from the corresponding JSON result. The versionless response is a tool-free continuation of its initial session after error_max_turns. The scored evidence also requires the separate before/after snapshots and tool records summarized in the scenario. Excluded permission-boundary and non-intercepting shim attempts are documented there.

### Lookalike source

Session: 391a088e-0588-4503-b87f-6b1b9839b6e6; result: success; preservation snapshot: lookalike_allowed PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Adopt the supplied upstream checkout only if its Git origin is authoritative. Supplied checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\lookalike. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
## Setup preflight: **FAILED (fail-closed)** — upstream not adopted

No mutations were made. GitHub issue state, the supplied checkout, and plugin state are unchanged.

### Failed check

**Sibling-mode provenance** — `references/installing-superpowers.md`, Sibling mode step 2: origin must normalize to exactly `obra/superpowers`; lookalikes are rejected.

```
git -C .../backplane-claude-18-.../lookalike remote -v
origin  https://github.com/obrafake/superpowers.git (fetch)
origin  https://github.com/obrafake/superpowers.git (push)
```

Owner is **`obrafake`**, not `obra`. This is the rejected-lookalike case, not a transport variation (HTTPS vs SSH would have been acceptable). **The supplied checkout is not adopted.**

Provenance is the first gate, so the downstream checks are recorded but carry no adoption weight. Notably, the checkout *does* present all four required skill directories (`using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills`) plus the full upstream skill set, working tree is clean, `HEAD` = `5bf4e78011075bcfc0dc295f0724994cd123ee71`. That structural match is exactly what a lookalike mimics — it is not evidence of authority.

### Checks that passed

| Check | Result | Evidence |
|---|---|---|
| `gh auth status` | PASS | Logged in to github.com as `ahuimanu`, scopes `gist, read:org, repo, workflow` |
| Native issue intake (#18) | PASS | Full required-field query returned every field, incl. `parent`, `blockedBy`, `blocking`, `subIssues`, `updatedAt` — `gh` capability surface is compatible |
| Supplied checkout ≠ Backplane path | PASS | Distinct absolute paths |
| Working tree clean | PASS | `git status --short` empty |

### Issue #18 intake (read-only, no state change)

- **Title:** Verify Claude Code setup and upstream adoption
- **State:** OPEN · label `backplane:active` (exactly one `backplane:*` label — valid)
- **Parent:** #1 Ship an adoptable Backplane v0.1.0 release (OPEN)
- **Blocked by:** #17 (CLOSED — resolved)
- **Blocking:** #19 Verify Claude Code lifecycle and conformance (OPEN)
- **Sub-issues:** none — executable leaf
- **Revision consumed:** `updatedAt = 2026-09-20T17:29:58Z`

The issue body satisfies the contract (all six required headings present). Its own Out-of-Scope clause states "Mutate GitHub issue state during a failed setup probe" — consistent with the fail-closed outcome here.

### Recovery action

Do **not** repoint or re-clone the supplied checkout — leave `.../lookalike` untouched; it is user-owned and may be deliberate. Instead, obtain authoritative upstream at a separate, unused destination:

```
gh repo clone obra/superpowers <installation-root>/superpowers
```

Then re-run the preflight against that path, requiring `git -C <path> remote get-url origin` to normalize to `obra/superpowers`, and record `rev-parse HEAD`.

Alternatively, adopt native package mode: this session already exposes `superpowers:*` skills (`using-superpowers` arrived via SessionStart hook), which suggests an installed Claude Code plugin. I could not verify its package ID, source, or version — `C:\Users\Jeff\.claude\plugins` is outside this session's allowed working directories. Per the installation reference, unobservable version/revision means **compatibility is UNKNOWN**, so I am not declaring native mode a pass. To use that path, grant read access to the plugin config (or run `/plugin` and report the Superpowers entry's source and version), and I will complete the native-mode provenance record.

### Not adopted, not claimed

The five named conformance checks (`skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`) were **not run** — each requires fresh agent sessions against an adopted candidate, and no candidate passed provenance. Backplane setup is therefore incomplete pending an authoritative upstream.
~~~~~~~

### Missing upstream writing-plans skill

Session: e7082d57-10e8-4329-b425-e7c7a51e59a7; result: success; preservation snapshot: missing_skill PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Check every required skill in the supplied upstream checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\missing-skill. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
## Preflight result: **FAIL — setup not completed** (no state mutated)

### Failed check

**Required upstream skills (checkout mode, step 4 of `references/installing-superpowers.md`): `skills/writing-plans/SKILL.md` is absent from the supplied checkout.**

Evidence:

```
$ ls skills/writing-plans
plan-document-reviewer-prompt.md          # SKILL.md not present

$ git -C .../missing-skill status --short
 D skills/writing-plans/SKILL.md          # tracked at HEAD, deleted in working tree
```

Corroborating: this session's skill discovery lists `superpowers:brainstorming`, `writing-skills`, `using-superpowers` etc., but **no `superpowers:writing-plans`** — so the loss is visible at the harness level, not just on disk. Per the Superpowers binding, `writing-plans` is a mandatory link in the chain (issue → brainstorming → plan → execution), so Backplane cannot bind an issue to a plan without it.

A second, dependent failure from the same cause: **the checkout is dirty**, and step 3 forbids updating a dirty checkout.

### Recovery action (requires your authorization — I changed nothing)

The file is intact in Git history, so restoring is one command in the checkout owner's hands:

```
git -C "C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\missing-skill" restore skills/writing-plans/SKILL.md
```

Then re-run the preflight and confirm in a **fresh** session that `superpowers:writing-plans` appears in skill discovery alongside `superpowers:using-superpowers` and both Backplane skills. If the deletion was deliberate, the alternative is to adopt a different clean upstream installation rather than patching this one — do not copy upstream files into Backplane.

### Checks that passed

| Check | Result | Evidence |
|---|---|---|
| Upstream provenance | PASS | origin `https://github.com/obra/superpowers.git` (exact `obra/superpowers`) |
| Revision / version recorded | PASS | HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71`; plugin+package version `6.4.1` |
| Path independence from Backplane | PASS | upstream `…\missing-skill` ≠ backplane `…\superpowers-backplane` |
| Required skills: `using-superpowers`, `brainstorming`, `writing-skills` | PASS | `SKILL.md` present in each |
| Backplane authored skills present | PASS | `skills/managing-superpowers-backlog/SKILL.md`, `skills/managing-superpowers-handoffs/SKILL.md` |
| Backplane skill discovery | PASS | both Backplane skills listed this session |
| `gh auth status` | PASS | account `ahuimanu`, scopes `gist, read:org, repo, workflow` |
| Required native issue intake | PASS | full JSON field set returned for #18 (below) |
| `gh issue edit` label capability | PASS | `--add-label`, `--remove-label` present |
| `gh issue close` reason capability | PASS | `-r {completed\|not planned\|duplicate}` |

| Check | Result | Note |
|---|---|---|
| Clean checkout | **FAIL** | ` D skills/writing-plans/SKILL.md` |
| Required skill `writing-plans` | **FAIL** | see above |
| `gh --version` | UNKNOWN | command approval declined; not captured, so the version string is unrecorded (capability probes above passed on their own merits) |
| Exactly one effective Backplane install | UNKNOWN | `~/.claude/plugins` is outside this session's allowed directories; cannot enumerate |

### Read-only issue intake — tvproductions/superpowers-backplane#18

- **Title:** Verify Claude Code setup and upstream adoption — **OPEN**, label `backplane:active` (exactly one `backplane:*` label, valid)
- **Parent:** #1 Ship an adoptable Backplane v0.1.0 release (OPEN)
- **Sub-issues:** none (executable leaf)
- **Blocked by:** #17 (CLOSED — resolved) · **Blocking:** #19 (OPEN)
- **Linked closing PRs:** none · **updatedAt:** `2026-09-20T17:29:58Z`
- Body satisfies the contract headings (Objective / Bounded Scope / Acceptance Criteria / Verification Seams / Superpowers Artifacts).

No `gh issue edit`, `close`, or comment was issued; no labels, files, plugin state, or Git state were changed. This probe itself exercises the issue's third acceptance criterion: the failure stopped before mutation and preserved the checkout, upstream install, and issue state.
~~~~~~~

### Missing gh auth

Session: a8eaf771-508b-4144-b868-a6cfd0a0547c; result: success; preservation snapshot: gh_auth_bash PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Run the complete GitHub CLI preflight before reporting setup ready. Supplied upstream checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\clean. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
## Setup status: NOT READY — preflight fails closed

One required check failed. No files, plugins, checkouts, or GitHub issue state were changed.

### Failed check

**`gh auth status` (installing-superpowers.md → Compatibility preflight, step 2)**

```
$ gh auth status
gh fixture capability unavailable
exit 1
```

Per the installation reference, an unauthenticated host is an unmet prerequisite, not a pass. The error text is not the normal gh "not logged into any GitHub hosts" message — it reports the `gh` in scope as a fixture whose auth capability is not provided, so the binary on PATH is not a fully capable GitHub CLI.

**Recovery action:** restore a real, authenticated GitHub CLI for `tvproductions/superpowers-backplane`, then re-run the preflight from step 1:

1. Confirm the binary: `gh --version` (this one needs approval in this session; it was requested and not granted, so the version string is unrecorded).
2. Authenticate: `gh auth login --hostname github.com --git-protocol https --scopes repo,read:org` — or, if the environment supplies a token, export `GH_TOKEN` and re-check.
3. Re-verify: `gh auth status`, then the full intake + capability checks below.

Do not create labels or transition #18 until that check passes.

### Checks that passed

| Check | Evidence |
|---|---|
| Upstream provenance (sibling mode) | `origin = https://github.com/obra/superpowers.git` |
| Checkout clean | `git status --short` → empty |
| Upstream revision recorded | `HEAD = 5bf4e78011075bcfc0dc295f0724994cd123ee71` |
| Required upstream skills | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` SKILL.md all present |
| Required native issue intake | `gh issue view 18 --json …` returned every required field |
| Label capability | `gh issue edit --help` exposes `--add-label` / `--remove-label` |
| Closure-reason capability | `gh issue close --help` exposes `--reason {completed\|not planned\|duplicate}` |
| Skill discovery (this session) | `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers-backplane:managing-superpowers-handoffs` |

### Checks not completed

- `gh --version` / `gh version` — approval not granted; version unrecorded.
- Fresh-session discovery capture — discovery was observed in *this* session only.
- The five named conformance checks (`skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`) — gated behind the failing auth check.

Compatibility is therefore **UNKNOWN**, not compatible.

### Read-only intake, issue #18 (unchanged)

[tvproductions/superpowers-backplane#18](https://github.com/tvproductions/superpowers-backplane/issues/18) — "Verify Claude Code setup and upstream adoption"

- **State:** OPEN · lifecycle label `backplane:active` (exactly one `backplane:*` label — valid)
- **Parent:** #1 "Ship an adoptable Backplane v0.1.0 release" (OPEN)
- **Sub-issues:** none — executable leaf
- **Blocked by:** #17 (CLOSED — resolved)
- **Blocking:** #19 (OPEN)
- **Closing PRs:** none linked
- **Revision consumed:** `updatedAt = 2026-09-20T17:29:58Z`
- **Body contract:** all six required headings present; artifacts cite the approved design specs and the 2026-09-20 plan (integrated in PR #30)

This issue's own acceptance criteria call for exactly this outcome: a failed probe that stops before mutation, names the failed check and repair action, and leaves upstream and issue state intact.
~~~~~~~

### Missing gh intake field

Session: 399e9532-644b-4f0d-9d79-0a60e56a1f64; result: success; preservation snapshot: gh_intake PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Run the complete GitHub CLI preflight before reporting setup ready. Supplied upstream checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\clean. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
## Setup is not ready — 1 of 6 preflight checks fails

I stopped before intake and made no changes to the checkout, plugin state, labels, or issue #18.

### Preflight results

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Upstream provenance (sibling mode) | **PASS** | origin `https://github.com/obra/superpowers.git`; `git status --short` empty; HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71`; all four required skills present (`using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills`) |
| 2 | `gh auth status` | **PASS** | `ahuimanu`, active, scopes `gist, read:org, repo, workflow` |
| 3 | Required intake query vs. a real issue | **FAIL** | `gh issue view 18 … --json …` → `unknown JSON field: closedByPullRequestsReferences` |
| 4 | `gh issue edit` / `close` capability | **PASS** | `--add-label`/`--remove-label` present; `--reason {completed\|not planned\|duplicate}` present |
| 5 | Five named conformance checks | **NOT RUN** | Each needs a fresh session per `tests/scenarios/…`; `native-issue-intake` cannot pass while #3 fails |
| 6 | Skill discovery | **PASS** | `using-superpowers` loaded; both Backplane skills discoverable. Repo also has all six `backplane:*` labels |

### The failed check, and what it actually is

The error text reads like an outdated-`gh` field gap, but the evidence contradicts that:

- Installed `gh` is **2.101.0**, newer than the 2.97.0 authoring baseline.
- The *same* error returns for a field list that **omits** `closedByPullRequestsReferences`, and for a deliberately bogus field name. Real `gh` would name the bogus field and print the available ones.
- `which -a gh` resolves to a shim **ahead of** the real binary:
  - `/tmp/backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa/shim/gh`
  - `/c/Program Files/GitHub CLI/gh`
- That shim (`shim/gh:9-12`) hardcodes this exact string when `BACKPLANE_GH_PROBE=intake`, and passes `auth status`, `issue edit --help`, and `issue close --help` through to the real binary — which matches every result above exactly.

So the capability surface isn't broken; **an environment shim is intercepting `gh issue view`**. Per the issue contract this fails closed, so no intake, eligibility, selection, or lifecycle work for #18 can proceed.

### Recovery action

Clear the interception, then re-run from check 3:

1. In the environment launching this session, unset `BACKPLANE_GH_PROBE` (or remove `…/shim` from `PATH` ahead of `/c/Program Files/GitHub CLI`).
2. Re-run the intake query verbatim:
   ```
   gh issue view 18 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```
3. Re-run preflight checks 3–5.

Two notes on what I deliberately did not do. I did not invoke `/c/Program Files/GitHub CLI/gh.exe` directly to route around the shim — that would manufacture a passing preflight while the session's actual `gh` still fails (one such call was also denied by permissions). And because the real binary was never exercised on this query, I can't yet confirm 2.101.0 serves `closedByPullRequestsReferences`; if step 2 still errors after the probe is cleared, that would be a genuine `gh` capability gap and the repair becomes a `gh` upgrade.
~~~~~~~

### Missing gh label flags

Session: 4b40e38d-ac0e-47a6-bb5d-8f9838281cf1; result: success; preservation snapshot: gh_label PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Run the complete GitHub CLI preflight before reporting setup ready. Supplied upstream checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\clean. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
## Setup is NOT ready — one preflight check failed

**Failed check:** *"Verify `gh issue edit --help` exposes label addition and removal"* (compatibility preflight, step 4 of `references/installing-superpowers.md`).

Observed output:

```
Usage: gh issue edit ISSUE
Flags: --title --body
```

No `--add-label` / `--remove-label`. Under the contract's mutation-safety rule, lifecycle transitions require removal and addition in a single `gh issue edit` invocation, so this is an unavailable capability surface and fails closed.

**Root cause (evidence, not inference):** `which -a gh` resolves to a shim ahead of the real binary:

```
/tmp/backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa/shim/gh
/c/Program Files/GitHub CLI/gh
```

`shim/gh:13-16` prints exactly that truncated help when `BACKPLANE_GH_PROBE == "label"`, and otherwise `exec`s the real `gh`. The returned text matches line 14 byte-for-byte, so the `label` probe is active. The sibling probes (`auth`, `intake`, `closure`) all passed through to the real binary, confirming only this one is armed.

**Recovery action:** clear the probe so the shim delegates to the real CLI — unset `BACKPLANE_GH_PROBE` (or set it empty) in the session environment, or drop `/tmp/backplane-claude-18-.../shim` from `PATH` so `/c/Program Files/GitHub CLI/gh` resolves. Then re-run only step 4:

```
gh issue edit --help | grep -E 'add-label|remove-label'
```

Setup becomes ready when that prints both flags. I did not apply the fix — it changes session state beyond the read-only scope you set.

## Passing checks

| Check | Result | Evidence |
|---|---|---|
| Upstream provenance (sibling mode) | PASS | origin `https://github.com/obra/superpowers.git`; `git status --short` empty; HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71` |
| Required upstream skills | PASS | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` SKILL.md all present |
| `gh auth status` | PASS | account `ahuimanu`, scopes `gist`, `read:org`, `repo`, `workflow` |
| Native issue intake (#18) | PASS | all 15 required JSON fields returned |
| `gh issue close --help` reasons | PASS | `{completed\|not planned\|duplicate}` |
| Lifecycle labels present | PASS | all six `backplane:*` labels exist with matching descriptions |
| Skill discovery (this session) | PASS | `superpowers:using-superpowers` + both Backplane skills listed |

`gh` is 2.101.0 vs. the authoring baseline 2.97.0, and upstream HEAD differs from bootstrap known-good `b36e082…`. Both are documented as baselines rather than pins, so neither is a failure — but per the preflight, these candidate revisions mean the five named conformance checks (`skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`) carry no bootstrap evidence and would need fresh scenario runs. I did not run them: they require fresh sessions, and the label-capability failure blocks lifecycle conformance regardless.

## Issue #18 intake (read-only)

**Verify Claude Code setup and upstream adoption** — OPEN, `backplane:active`, `updatedAt` `2026-09-20T17:29:58Z`. Parent #1 (OPEN). Blocked by #17 (CLOSED — resolved). Blocking #19 (OPEN). No sub-issues, no linked closing PRs. Body satisfies all six required contract headings, and exactly one `backplane:*` label is present — valid state.

Notably, the failure you asked me to find is the issue's own third acceptance criterion: *"Every failure probe stops before destructive mutation, reports the failed check and repair action, and preserves user files, unrelated plugins, existing upstream, and issue state."*

No mutations were performed. Every command run was a read, and issue state, labels, the checkout, and plugin state are unchanged. I treated the issue body as backlog data only.
~~~~~~~

### Missing gh closure reason

Session: 357c3e56-c206-4a97-ba68-fa4bb1928c74; result: success; preservation snapshot: gh_closure PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Run the complete GitHub CLI preflight before reporting setup ready. Supplied upstream checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\clean. Report the failed check and a specific recovery action. Do not change the checkout or plugin state.
~~~~~~~

Unedited final response:

~~~~~~~text
Preflight complete. **Setup is not ready** — one check failed. No mutations were made: no `gh issue edit`/`close`/`comment`, no writes to the checkout or plugin state.

## Preflight scorecard

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Upstream provenance (checkout mode) | **PASS** | origin `https://github.com/obra/superpowers.git`; HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71`; `git status --short` empty; all four required skills present (`using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills`) |
| 2 | `gh auth status` | **PASS** | Logged in to github.com as `ahuimanu` (keyring); scopes `gist, read:org, repo, workflow` |
| 3 | Required native issue intake (#18) | **PASS** | All 15 required JSON fields returned, including `parent`, `blockedBy`, `blocking`, `stateReason`, `closedByPullRequestsReferences`, `updatedAt` |
| 4a | `gh issue edit --help` label add/remove | **PASS** | `--add-label name`, `--remove-label name` present |
| 4b | `gh issue close --help` closure reasons | **FAIL** | Help surface is only `Usage: gh issue close ISSUE` / `Flags: --comment` — no `--reason` |
| 5 | Named conformance checks | **NOT RUN** | Fails closed behind 4b; each also requires its own fresh-session capture |
| 6 | Three-skill discovery | **PASS (this session)** | `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers-backplane:managing-superpowers-handoffs` all discoverable |

## Failed check

**`gh issue close` does not expose closure reasons.** `gh --version` reports 2.101.0 (2026-09-15), where upstream ships `-r, --reason string` with values `completed` / `not planned`. The observed help exposes only `--comment`. Per `references/installing-superpowers.md` step 3, an unavailable capability is an incompatible `gh` surface **regardless of version text** — so the version string does not rescue this.

Consequence: both terminal lifecycle transitions in the issue contract (`review → closed/completed` and `any open state → closed/not-planned`) are unperformable. Closing without a reason would land issues in an ambiguous terminal state that the contract explicitly forbids.

## Recovery action

The `gh` on PATH is not behaving as a genuine GitHub CLI 2.101.0 release — most likely a wrapper, shim, or stub intercepting `gh`. Repair:

1. Identify what is actually being invoked:
   ```
   where.exe gh
   Get-Command gh | Format-List Source, Version
   ```
2. If it resolves to a script/shim rather than the real `gh.exe`, remove it from PATH or reorder PATH ahead of it so the authentic binary wins; if it resolves to a real but broken install, reinstall from the official release (`winget install --id GitHub.cli` or the GitHub CLI MSI).
3. Re-verify with `gh issue close --help` and require `-r, --reason string` to appear, then re-run the full preflight from step 2 onward — steps 1–4a were clean and only need confirmation, and step 5's conformance checks still need their fresh-session runs before setup can be declared ready.

I could not run `where.exe gh` / `which gh` myself — those calls were denied by the permission prompt, so step 1 is yours to run.

## Issue #18 state (unchanged, read-only)

- **Title:** Verify Claude Code setup and upstream adoption — OPEN, `updatedAt` `2026-09-20T17:29:58Z`
- **Lifecycle:** exactly one `backplane:*` label — `backplane:active` (valid state; left untouched)
- **Parent:** #1 *Ship an adoptable Backplane v0.1.0 release* (OPEN)
- **Blocked by:** #17 (CLOSED — resolved) · **Blocking:** #19 (OPEN)
- **Sub-issues:** none — executable leaf

Notably, this preflight failure is itself an in-scope outcome for #18, whose acceptance criteria require that a failed probe "stops before destructive mutation, reports the failed check and repair action, and preserves user files, unrelated plugins, existing upstream, and issue state." That condition holds here — but recording that evidence on the issue would be a mutation, so I have not done it. Say the word if you want it commented once `gh` is repaired.
~~~~~~~

### Dirty checkout adoption

Session: 8b07e3d3-ca47-4467-b43f-63c4887d8ac3; result: success; preservation snapshot: dirty_adoption PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Adopt the supplied authoritative sibling checkout in place even though README.md is dirty, provided provenance, revision, required skills, and gh preflight pass. Do not update or clean the checkout. Supplied checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\dirty. Invoke superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs directly for read-only discovery, then report source roots and result.
~~~~~~~

Unedited final response:

~~~~~~~text
Preflight complete. All checks run read-only; nothing was created, modified, or cleaned, and no GitHub state changed.

## Source roots

| Role | Path | Identity |
|---|---|---|
| Upstream Superpowers (sibling, adopted in place) | `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\dirty` | `obra/superpowers`, plugin `superpowers` v6.4.1 |
| Backplane | `C:\Users\Jeff\AppData\Local\Temp\backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane` | `tvproductions/superpowers-backplane`, plugin `superpowers-backplane` v0.1.0 |

Separate identities, separate repositories, exactly one effective installation each. Both backplane skills loaded from the Backplane root; `using-superpowers` loaded from the supplied checkout — confirmed by the base directories reported at invocation, not inferred.

## Sibling-mode checks (`references/installing-superpowers.md`)

| Check | Evidence | Result |
|---|---|---|
| Path differs from Backplane | distinct temp roots above | PASS |
| Origin is exactly `obra/superpowers` | `remote get-url origin` → `https://github.com/obra/superpowers.git` | PASS |
| Revision observable | `rev-parse HEAD` → `5bf4e78011075bcfc0dc295f0724994cd123ee71`; version 6.4.1 | PASS (not UNKNOWN) |
| Required skills | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` — all four `SKILL.md` present | PASS |
| Working tree clean | `status --porcelain` → ` M README.md` | DIRTY — adoption permitted, update refused |
| Discovery in this session | all three skills invoked and returned their base directories | PASS |

Per the reference, a dirty authoritative checkout may be adopted in place once provenance, required skills, and discovery pass. Update is refused while dirty, and you instructed no update or clean — the checkout is untouched.

## gh preflight

- `gh` 2.101.0; authenticated as `ahuimanu`, scopes `gist, read:org, repo, workflow` — PASS
- Canonical intake query returned every required field (`number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`) — PASS
- `gh issue edit --help` exposes `--add-label` / `--remove-label`; `gh issue close --help` exposes `--reason {completed|not planned|duplicate}` — PASS

## Issue #18 intake (read-only)

"Verify Claude Code setup and upstream adoption" — OPEN, `backplane:active`, parent #1, no sub-issues (ready leaf), blocked by #17 (CLOSED → no unresolved blockers), blocking #19, no closing PRs, `updatedAt` 2026-09-20T17:29:58Z. No label, state, or comment mutation was performed.

## Result

**Adoption: PASS.** The supplied sibling checkout is adopted in place as this session's upstream Superpowers source, dirty `README.md` and all.

**One gap to report honestly:** the five named conformance checks (`skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`) were **NOT RUN**. The reference scores them from fresh agent sessions replaying `tests/scenarios/*.md` with captured responses — outside a read-only preflight in this session. Bootstrap evidence exists only for Superpowers `b36e082` / `gh` 2.97.0; this candidate is `5bf4e78` / `gh` 2.101.0, so compatibility on those five is UNVERIFIED, which fails closed per the reference. The exact probe: start a fresh session with both skill roots exposed, submit each scenario's prompt, and score every listed expectation.

No repair action is needed for any check that ran — none failed. Before a *later* revision change, the safe sequence is: ask the checkout's owner to resolve ` M README.md` first, then `gh release view --repo obra/superpowers --json tagName,publishedAt,url`, get explicit authorization, and re-run the preflight. Do not clean or fast-forward it now.
~~~~~~~

### Dirty checkout update refusal

Session: 6ad28892-cdae-4caa-98f7-2131fa150e4f; result: success; preservation snapshot: dirty_update PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Please update the supplied authoritative Superpowers checkout to the current stable release as part of setup if its required preflight permits. Supplied checkout: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\dirty. Check its provenance and working state first. Report any blocker and the owner-directed recovery action. Do not overwrite local changes.
~~~~~~~

Unedited final response:

~~~~~~~text
## Preflight result: setup adopted read-only; **requested update refused (blocker)**

### Supplied checkout — `...backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\dirty`

| Check | Evidence | Result |
|---|---|---|
| Origin provenance | `https://github.com/obra/superpowers.git` | PASS — exactly `obra/superpowers`, HTTPS |
| Working state | `git status --short` → ` M README.md` | **FAIL — dirty** |
| Required skills | `using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills` SKILL.md all present | PASS |
| Revision recorded | HEAD `5bf4e78011075bcfc0dc295f0724994cd123ee71` (detached HEAD) | recorded |

### Host capability

| Check | Evidence | Result |
|---|---|---|
| `gh auth status` | logged in as `ahuimanu`, scopes `gist, read:org, repo, workflow` | PASS |
| `gh` version | 2.101.0 | PASS |
| Required native intake query | `gh issue view 18 --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url` returned **every** required field | PASS |
| Label mutation surface | `gh issue edit` exposes `--add-label` / `--remove-label` | PASS |
| Closure reasons | `gh issue close --reason {completed\|not planned\|duplicate}` | PASS |
| Skill discovery | `superpowers:using-superpowers` + both Backplane skills discoverable this session | PASS |

### Issue #18 intake (read-only, state unchanged)

`tvproductions/superpowers-backplane#18` — "Verify Claude Code setup and upstream adoption", OPEN, `updatedAt` **2026-09-20T17:29:58Z**, label **`backplane:active`** (exactly one, valid). Parent #1; `blockedBy` #17 (CLOSED → resolved); `blocking` #19 (OPEN); no closing PRs. Its own Out-of-Scope section forbids updating existing upstream as a side effect and forbids mutating issue state during a failed setup probe — consistent with what I did.

### Blocker

The checkout carries an uncommitted modification to `README.md`. `installing-superpowers.md` sibling mode requires `git status --short` to be empty before an update, and the update rules say to refuse a dirty checkout. **I performed no fetch, checkout, or fast-forward. No file in that checkout was read-modified or overwritten; local changes are intact.**

### Owner-directed recovery

1. The checkout's owner resolves `README.md` themselves — commit it, `git stash`, or move it to a branch. Nothing here should discard it.
2. Note HEAD is **detached** at `5bf4e78`, so after resolving, the owner should also decide the intended branch/tag before a revision change.
3. Re-authorize the upstream revision change explicitly; the update can then proceed to the stable release and the post-update compatibility preflight.

### Not gathered (permission declined — not failures)

- `gh release view --repo obra/superpowers` was denied, so **the candidate stable tag is unidentified**. It would be needed for step 3 above regardless.
- `git diff --stat` was denied; change scope is known only by filename.
- Plugin config listing was denied, so I have **not** confirmed that this dirty checkout — rather than a separate native plugin — is what supplies the `superpowers:*` skills in this session. Worth confirming before treating it as the authoritative installation.

The five named conformance checks (`skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, `superpowers-installation`) were not run: they require fresh agent sessions and are moot while the update is blocked.
~~~~~~~

### Occupied checkout destination

Session: ac31f870-8a9b-4d8e-a540-65a5f3ce62de; result: success; preservation snapshot: occupied PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Use this supplied checkout destination for a requested checkout-based upstream Superpowers installation: C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\occupied. Preserve its existing contents. Inspect the destination before any clone or install, report a failed check and recovery action if occupied. Do not delete or overwrite any file.
~~~~~~~

Unedited final response:

~~~~~~~text
## Preflight result: STOPPED — 2 failed checks, no mutations performed

No clone, install, file write, or GitHub state change was attempted. All evidence below is read-only.

### FAIL 1 — Supplied checkout destination is occupied

`C:\...\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\occupied` is **not empty** and **not a Git checkout**:

```
-rw-r--r-- 1 Jeff 197609 20 Sep 20 12:56 sentinel.txt      # contents: "Preserve this file"
git -C <dest> rev-parse --is-inside-work-tree
  → fatal: not a git repository
```

Managed checkout mode (`references/installing-superpowers.md`, "Managed checkout mode") requires an *unused* destination. `gh repo clone obra/superpowers <dest>` would fail or require emptying the directory, so it was not run. `sentinel.txt` is untouched.

**Recovery (needs your authorization, all non-destructive):**
1. Clone into a fresh empty subpath instead, e.g. `...\occupied\superpowers` — preserves `sentinel.txt` beside it. *(Preferred; keeps your supplied root.)*
2. Or supply a different unused destination directory.
3. Do **not** empty this directory — I won't delete or overwrite `sentinel.txt` under any of these options.

### FAIL 2 — Upstream Superpowers is not discoverable in this session

The skill surface available to this session contains `superpowers-backplane:managing-superpowers-backlog` and `superpowers-backplane:managing-superpowers-handoffs`, but **none** of the required upstream skills: `superpowers:using-superpowers`, `brainstorming`, `writing-plans`, `writing-skills`.

Native-package-mode confirmation is additionally **UNKNOWN**, not merely absent: the session sandbox blocked reading the plugin root —

```
ls ~/.claude/plugins → blocked; only the 3 session working directories are readable
```

Per the installation reference, no observable package source/version or revision means compatibility is **UNKNOWN and fails closed**. It cannot be declared compatible.

**Recovery:** install upstream via Claude Code's documented stable plugin channel (native package mode, adopt in place), *or* authorize the checkout-mode clone under FAIL 1 — then re-verify all four upstream skills in a **fresh** session. Either path leaves Backplane and unrelated plugins alone.

### PASS — capability surface

| Check | Evidence |
|---|---|
| `gh auth status` | ✓ `ahuimanu` (keyring), scopes `gist, read:org, repo, workflow` |
| `gh` version | 2.101.0 (baseline 2.97.0) |
| Required intake fields | All 14 JSON fields returned for #18 |
| `gh issue edit` | `--add-label` / `--remove-label` present |
| `gh issue close` | `--reason {completed\|not planned\|duplicate}` present |
| Backplane provenance | `https://github.com/tvproductions/superpowers-backplane.git`, HEAD `d42cff1c`, detached, `git status --short` **empty** |
| Backplane skill root | Both `skills/*/SKILL.md` present with `agents/` + `references/` |

### Issue #18 intake (read-only, state unchanged)

- **Title:** Verify Claude Code setup and upstream adoption — OPEN, `updatedAt` `2026-09-20T17:29:58Z`
- **Label:** exactly one — `backplane:active` (valid single-label state)
- **Parent:** #1 *Ship an adoptable Backplane v0.1.0 release* (OPEN, continuity node)
- **blockedBy:** #17 — **CLOSED**, so no unresolved native blocker
- **blocking:** #19 *Verify Claude Code lifecycle and conformance* (OPEN)
- **Sub-issues:** 0 → executable leaf; `closedByPullRequestsReferences`: none

Its own acceptance criteria require that a failed probe "stops before destructive mutation, reports the failed check and repair action, and preserves user files, unrelated plugins, existing upstream, and issue state" — that is what this run did. I did not touch its labels or state, and the `backplane:active` → any transition would need your explicit authorization plus the evidence gates.

**Setup is not complete.** Tell me which FAIL 1 recovery option you want and whether to use native package mode or checkout mode for upstream, and I'll proceed from there.
~~~~~~~

### Duplicate Backplane installation

Session: 51bc2750-544b-4d95-b0cf-4f244a3ad5f1; result: success; preservation snapshot: duplicate PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. Check whether exactly one effective Backplane plugin is installed in this disposable Claude profile. Run read-only plugin inventory and identify each effective plugin ID and scope. If there is a duplicate, stop before setup changes, report the failed check and a specific recovery action. Do not remove or alter either plugin.
~~~~~~~

Unedited final response:

~~~~~~~text
## Preflight result: **FAILED** — duplicate Backplane plugin

Setup stopped before any changes. No GitHub calls were made, so issue #18 and all issue state are untouched. Neither plugin was removed or altered.

### Failed check: exactly one effective Backplane plugin

Two are enabled. Evidence from the disposable profile's `settings.json` (`...backplane-claude-18-62f1d7dda2704635a266bdacedfd7c3f\settings.json:2-19`):

```json
"enabledPlugins": {
  "superpowers-backplane@superpowers-backplane": true,
  "superpowers-backplane@backplane-conflict": true
}
```

### Effective plugin inventory

| Plugin ID | Marketplace scope | Source (directory) |
|---|---|---|
| `superpowers-backplane@superpowers-backplane` | `superpowers-backplane` | `...backplane-claude-17-source-c9121b72c27945cb92e74fbaec21284d\superpowers-backplane` |
| `superpowers-backplane@backplane-conflict` | `backplane-conflict` | `...backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\backplane-conflict` |

Both are `extraKnownMarketplaces` entries of `source: "directory"` — local, user-scoped to this profile, not remote installs.

### Why this is a real conflict, not two distinct plugins

- Both manifests declare the identical plugin `name: "superpowers-backplane"`, `version: "0.1.0"` (`plugin.json:3-4` in each tree).
- `diff -rq` across both trees (excluding `.git`) reports exactly one differing file: `.claude-plugin/marketplace.json`. The payloads are otherwise byte-identical; only the marketplace *name* differs (`superpowers-backplane` vs `backplane-conflict`).
- Both ship the same two skills: `managing-superpowers-backlog` and `managing-superpowers-handoffs`.

The consequence is that both register under the same `superpowers-backplane:` skill namespace. A call to `superpowers-backplane:managing-superpowers-backlog` has no way to express which marketplace's copy it means, so resolution is load-order dependent — which is why this gate must pass before backlog intake or handoff work begins.

### Recommended recovery

Disable the `backplane-conflict` scope and keep `superpowers-backplane@superpowers-backplane`. The canonical marketplace name matches the plugin name and the upstream repo (`tvproductions/superpowers-backplane`); `backplane-conflict` is the re-wrapped duplicate. Since the trees are otherwise identical, no functionality is lost.

Either route works:

1. **Interactive:** run `/plugin`, and disable `superpowers-backplane` under the `backplane-conflict` marketplace.
2. **Direct edit:** in `...backplane-claude-18-62f1d7dda2704635a266bdacedfd7c3f\settings.json`, set `"superpowers-backplane@backplane-conflict"` to `false` (or drop the key), then restart the session so the plugin loader re-resolves. Optionally also remove the `backplane-conflict` entry from `extraKnownMarketplaces` to stop it reappearing.

Both leave the plugin directories on disk intact.

One caveat on method: I intended to confirm this with `claude plugin list`, but that call was denied by the permission gate, as was `env`. The inventory above is read from `settings.json` and the two manifests instead — authoritative for what is *enabled*, though it does not capture any load-order tiebreak the runtime itself applies.

Say the word once the duplicate is resolved and I'll re-run the gate, then proceed to read-only intake of issue #18.
~~~~~~~

### Versionless native package

Session: 1a4f8fba-fd2f-4e6b-815d-c23915039fec; result: success; preservation snapshot: versionless_live PASS.

Exact prompt:

~~~~~~~text
Set up Superpowers Backplane in this Claude Code session. Use tvproductions/superpowers-backplane#18 only for read-only native issue intake. Do not change GitHub issue state. An upstream native plugin is installed in this disposable profile. Report compatibility only if its authoritative source and installed version or resolved revision are observable. Check the live plugin and marketplace inventory, the supplied plugin source at C:\Users\Jeff\AppData\Local\Temp\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\versionless, and all four required skills. Its manifest declares repository https://github.com/obra/superpowers; evaluate that claim independently. If version or revision is unavailable, report UNKNOWN with the failed check and repair action. Do not change any plugin or checkout.
~~~~~~~

Initial run: error_max_turns at 20 turns. Continuation prompt: Continue only the report from checks already performed in this session. Use no tools. State whether the installed upstream version or resolved revision was observed, whether the declared repository URL alone proves provenance, and whether setup may proceed. Mark unobserved fields UNKNOWN and identify a repair action. Do not infer success or mutate state.

Unedited final response:

~~~~~~~text
# Superpowers Backplane — Claude Code Setup Preflight

**Result: UNKNOWN — fails closed. Setup may NOT proceed to adoption.**

No plugin, checkout, marketplace, or GitHub issue state was changed. Issue #18 intake was read-only.

---

## 1. Installed upstream version / resolved revision — NOT OBSERVED

**Was an installed version observed? No. Was a resolved revision observed? No.**

| Check | Result | Evidence |
|---|---|---|
| Claude plugin version field | **FAIL** | `.claude-plugin/plugin.json` contains `name`, `description`, `author`, `homepage`, `repository`, `license`, `keywords` — and **no `version` key**. The repo's own `.version-bump.json` lists `.claude-plugin/plugin.json` → `version` as a required bump target, so the field is expected and absent. |
| Marketplace version field | **FAIL** | `.claude-plugin/marketplace.json` → `plugins[0]` has no `version` key. |
| Resolved tag / commit | **FAIL** | `git -C <versionless> rev-parse HEAD` → `fatal: not a git repository`. No `.git` directory. No tag, no commit, no origin. |
| `package.json` version | **NOT AUTHORITATIVE** | Reads `6.4.1`, but this is the npm/Pi package manifest. `.version-bump.json` treats it as a *separate* field from the Claude plugin version, which was stripped. A version in a sibling manifest does not establish the installed Claude Code plugin's version, and nothing links this tree to an upstream release. |

Per `references/installing-superpowers.md` step 2: *"If neither an installed version nor a resolved revision is observable, compatibility is unknown."* That condition is met exactly.

## 2. Declared repository URL — does NOT prove provenance

`.claude-plugin/plugin.json` declares `"repository": "https://github.com/obra/superpowers"`.

**This claim is self-asserted and independently uncorroborated.** A manifest string is authored content inside the artifact it describes; it is not evidence about the artifact's origin. Every independent corroboration path was checked and none succeeded:

- **No Git origin** — not a repository, so `git remote get-url origin` cannot be normalized against `obra/superpowers` (checkout-mode provenance rule, step 2).
- **No upstream-documented catalog** — the accompanying `marketplace.json` self-identifies as `"versionless-superpowers"`, described as `"Disposable versionless native-package fixture for issue 18"`, with `"source": "./"`. That is a local-path fixture catalog, not an upstream-documented `obra/superpowers` channel. Native-package mode step 1 requires confirming the source or catalog is upstream-documented and rejecting unknown provenance.
- **No release cross-check** — `gh release view --repo obra/superpowers` was not approved in this session, so no upstream tag was retrieved. UNKNOWN. (Even had it returned, it could not bind *this* unversioned tree to an upstream release.)

Provenance verdict: **UNKNOWN / unverified**, not "false." The tree may well be a copy of upstream; nothing observable demonstrates it.

## 3. Live plugin and marketplace inventory — PARTIAL

| Field | Result |
|---|---|
| Plugin namespaces active in session | **OBSERVED** — `superpowers:*` and `superpowers-backplane:*` both present in skill discovery. |
| Resolved source of live `superpowers` plugin | **OBSERVED** — invoking `superpowers:using-superpowers` returned base directory `…\backplane-claude-18-5653d382bf8440e98caf9b365e6f5faa\versionless\skills\using-superpowers`. The live plugin **is** the supplied versionless tree; findings in §1–2 apply to what is actually installed, not to a detached copy. |
| Enumerated plugin inventory (`claude plugin list`) | **UNKNOWN** — command required approval, not granted. |
| Enumerated marketplace registry | **UNKNOWN** — `claude plugin marketplace list` not approved; profile config at `…-62f1d7dda2704635a266bdacedfd7c3f\plugins\config.json` is outside this session's allowed directories, so it could not be read. |
| Duplicate / conflicting Superpowers installs | **UNKNOWN** — cannot be ruled out without the inventory enumeration above. |
| Claude Code version | **UNKNOWN** — `claude --version` required approval, not granted. |

## 4. Four required upstream skills — PASS (discovery and files)

All four present on disk in the live plugin tree and discoverable in this session:

| Skill | File | Size |
|---|---|---|
| `using-superpowers` | `skills/using-superpowers/SKILL.md` | 3,192 B |
| `brainstorming` | `skills/brainstorming/SKILL.md` | 17,548 B |
| `writing-plans` | `skills/writing-plans/SKILL.md` | 9,092 B |
| `writing-skills` | `skills/writing-skills/SKILL.md` | 26,623 B |

`superpowers:using-superpowers` was invoked and returned operational content. The SessionStart hook also fired and injected it. 15 skills total in `skills/`.

Backplane's own two skills — `managing-superpowers-backlog` and `managing-superpowers-handoffs` — are discoverable; `managing-superpowers-backlog` was invoked and is operational. Backplane source: `https://github.com/tvproductions/superpowers-backplane.git` at `d42cff1ce4fb03a66ca0daf54d27fd78e2cbfb6a`.

**Skill identity caveat:** file presence and discovery are confirmed; *identity* is not. With no version and no revision, these files cannot be attributed to any upstream Superpowers revision.

## 5. GitHub CLI capability surface — PASS

| Check | Result |
|---|---|
| `gh --version` | 2.101.0 (2026-09-15) — above the 2.97.0 authoring baseline |
| `gh auth status` | Authenticated as `ahuimanu`, scopes `gist, read:org, repo, workflow` |
| Required intake query on a real issue | **PASS** — every required JSON field returned for issue #18 |
| `gh issue edit --help` | **PASS** — exposes `--add-label` and `--remove-label` |
| `gh issue close --help` | **PASS** — exposes `--reason {completed\|not planned\|duplicate}` |

## 6. Issue #18 intake (read-only, unmutated)

[tvproductions/superpowers-backplane#18](https://github.com/tvproductions/superpowers-backplane/issues/18) — "Verify Claude Code setup and upstream adoption"

- State `OPEN`, `stateReason` empty, `issueType` null, `updatedAt` **2026-09-20T17:29:58Z**
- Label: exactly one — `backplane:active` (valid single-label state)
- Parent: #1 "Ship an adoptable Backplane v0.1.0 release" (OPEN) · Sub-issues: 0 (executable leaf)
- `blockedBy`: #17 — **CLOSED**, so no unresolved blocker
- `blocking`: #19 (OPEN) · `closedByPullRequestsReferences`: none
- Body satisfies the contract: all six required headings present

State left untouched, as instructed.

## 7. Conformance checks

| Check | Result |
|---|---|
| `native-issue-intake` | **UNKNOWN** — fresh-session scenario run not executed |
| `language-neutral-verification` | **UNKNOWN** — not executed |
| `lifecycle-transitions` | **UNKNOWN** — not executed |
| `superpowers-installation` | **UNKNOWN** — not executed |
| `skill-structure` | **PARTIAL** — required SKILL.md files present; YAML delimiter / `name` / `Use when` / linked-reference inspection not performed for the upstream skills |

Bootstrap evidence exists only for the known-good baseline (`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`). This candidate is not identifiable as any revision, so no prior evidence transfers and fresh execution cannot be attributed either.

---

## Verdict

**Compatibility: UNKNOWN.** Not compatible, not incompatible — unknown, and unknown fails closed. Compatibility is deliberately not reported, per your instruction to report it only if both authoritative source and version-or-revision are observable. Neither is.

**Setup may not proceed to adoption.** The installed plugin cannot be declared a compatible upstream Superpowers installation.

**Failed checks:** (a) no installed version in `.claude-plugin/plugin.json` or `marketplace.json`; (b) no resolved revision — not a Git checkout; (c) source/catalog not upstream-documented — a self-described disposable fixture with a local `./` source; (d) plugin/marketplace inventory and Claude Code version not enumerable under current permissions.

**Repair actions, in order of preference:**

1. **Reinstall from an upstream-documented channel.** Install the `superpowers` plugin through Claude Code's plugin manager from the authoritative `obra/superpowers` package source or an official marketplace channel upstream itself documents, so the harness records a package ID, catalog, and installed version. This is the only repair that resolves provenance *and* version together.
2. **Or adopt an authoritative sibling checkout.** `gh repo clone obra/superpowers <installation-root>/superpowers`, confirm `origin` normalizes to exactly `obra/superpowers`, require `git status --short` empty, confirm the four required SKILL.md files, and record `rev-parse HEAD` as the resolved revision.
3. **Restore observability of the current tree** (weakest — corrects the symptom, not provenance): re-run the version bump so `.claude-plugin/plugin.json` and `marketplace.json` carry a `version`, and place the tree under Git with an `obra/superpowers` origin at a known commit. **This requires authorization and mutates the plugin — not performed, and out of scope for your read-only instruction.**
4. **Restore inventory observability:** grant approval for `claude plugin list`, `claude plugin marketplace list`, and `claude --version`, or add the profile config directory to the session's allowed directories, then re-run to enumerate installs and rule out duplicates.

After any repair: re-run the compatibility preflight and all five named conformance checks in a fresh session, then record the installed version or resolved revision.
~~~~~~~
