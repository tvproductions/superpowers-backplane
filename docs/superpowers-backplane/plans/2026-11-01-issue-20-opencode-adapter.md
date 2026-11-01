# Issue #20 OpenCode Adapter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Status:** Draft for operator review; implementation has not started.

**Revision:** 2026-11-01 plan-review corrections: explicit lifecycle gates, pinned host/command contracts, and fail-closed receipt tests. The commands below are planned verification, not successful native runs.

**Goal:** Deliver one native OpenCode V1/V2 package and a pinned-install guide, with independent installed-package discovery evidence for both variants.

**Architecture:** A single root JavaScript entry point exposes the V1 plugin function/server contract and V2 id/setup contract. Both register the canonical root skills; neither bootstraps Superpowers or manages upstream. Read skill metadata/content at runtime from that tree rather than shipping authored copies.

**Tech Stack:** Markdown, OpenCode's JavaScript runtime, native Git/gh; uv-managed Python 3.14 for Backplane verification orchestration.

**Spec:** `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`.

## Global Constraints

- Issue: https://github.com/tvproductions/superpowers-backplane/issues/20; consumed `updatedAt`: `2026-09-20T01:30:13Z`. Reconcile fresh full intake before execution or lifecycle mutation.
- V1 minimum 1.18.29; V2 minimum 2.0.4. Test both variants separately; basic smoke acceptance does not establish every version above either floor.
- One package entry point, canonical `skills/`, no duplicated authored skills, independent upstream and no competing bootstrap. Preserve existing Codex and Claude metadata.
- Host runtime only; no consumer runtime requirement, GitHub Projects requirement, IssueOps, dependency manager, or new Backplane executable.
- Scope ends at basic package/install/discovery smoke. #21–#24 own setup, failures and lifecycle; #12 owns final acceptance.
- Fixtures, isolated profiles, briefs and execution ledger belong under ignored `.sp-bp/work/issue-20/`. Record containment, source identities and protected-state snapshots before use. Never copy credentials or use a normal profile as a fallback.
- Do not write `.superpowers/` or upstream installations. No publication, release, or completed closure is authorized by this plan.

## Review Focus

- V1 loader export scanning must not perform V2 registration. If V1 calls `setup` with a V1-shaped context, it must return without side effects; test that call explicitly.
- V2 replayed transforms must register current canonical paths/content without mutating unrelated skills; test callback replay and unrelated entries.
- Paths containing spaces and Windows drive letters must resolve from the package, independently of process cwd; test both.
- A Git-installed package must include every referenced skill contract and documentation dependency; compare its installed inventory with source.
- Missing host/authentication or unknown upstream provenance yields UNKNOWN, never PASS; test the receipt's incomplete-result classification.

### Task 1: Verify host contracts and establish isolated execution

**Files:** Create `.sp-bp/work/issue-20/execution.md` and `.sp-bp/work/issue-20/host-smoke.py`; later create `tests/scenarios/2026-11-01-issue-20-opencode-adapter.md` and `.json` for portable evidence. The helper is verification orchestration, not a shipped executable; retain its screened source and command receipt with the tracked evidence.

**Interfaces:** Consumes approved contracts and native issue intake; produces selected host identities, exact adapter interface and protected fixture identities.

- [ ] Run complete #20 intake using the exact command in Lifecycle gates below; reconcile body/graph against the recorded revision. If it is still backlog, enter designing only while actually preparing the plan. Do not reset an issue already in a later valid state.
- [ ] Establish a registered isolated worktree sharing this repository's Git directory. Record canonical path, branch, starting SHA and registration before project mutations. Leave other registered worktrees untouched.
- [ ] Use the pinned hosts, adapter exports, isolation environment and argument vectors in Native verification contract below. Confirm installed `--version` and `--help` match those contracts before inference. A mismatch stops the affected smoke at UNKNOWN and requires a documented plan correction; do not substitute another host or invent flags.
- [ ] Implement the fixture runner's `prepare`, `preflight`, `smoke` and `verify` operations specified below. Provision only the missing V1 release binary; read the existing V2 binary without modifying its installation. Verify all paths before any launch, including help/version commands. Use child-scoped paths and verified existing authentication only where natively supported; otherwise require separate isolated-profile login. No credential copying or normal-profile fallback.
- [ ] Record baseline canonical skill and Codex/Claude metadata hashes, Git/gh capability, independent upstream source/revision and unrelated profile sentinels. Keep raw secret-bearing captures ignored and screen derived evidence.
- [ ] After plan approval, record its tracked blob/containing commit, design references and semantic issue revision in #20's artifact section under the separate planning-update authority supplied by the operator's request to work on #20. Preserve the rest of the body and graph; do not publish a local-only commit URL. Pass the ready gate, then enter active immediately before the first approved execution task.

### Task 2: Implement and verify the shared adapter

**Files:** Create `package.json`, `index.js`, `tests/opencode-adapter.test.mjs`.

**Interfaces:** Export `BackplanePlugin = async (ctx) => ({ config: async (config) => ... })` for V1 and default `{ id: "superpowers-backplane", server: BackplanePlugin, setup: async (ctx) => ... }`. V1 config preserves existing `skills.paths` and adds the package's canonical absolute `skills/` path once. V2 `setup` preloads both canonical files, strips frontmatter from the body, and calls `ctx.skill.transform` with a synchronous callback adding `{ id, name, description, path, content }` for each. `id` is the canonical skill directory name and `path` names its absolute `SKILL.md`. V1-shaped contexts cause V2 setup to return without registration; it must not require session hooks, since this adapter has no bootstrap.

- [ ] Write named runtime tests: `v1_preserves_paths_and_registers_once`, `v1_context_does_not_activate_v2`, `v2_registers_exact_canonical_payloads`, `v2_replay_preserves_unrelated_skills`, and `paths_resolve_from_package_with_spaces_and_different_cwd`. Assert the two exact skill IDs, parsed name/description, body excluding frontmatter, absolute installed file paths, unchanged sentinel entries and absence of session/bootstrap/GitHub calls. On Windows, assert a real drive-letter package path round-trips through URL-to-path conversion.
- [ ] Run `node --test tests/opencode-adapter.test.mjs` with the existing Node binary (observed v26.13.0). Use a dynamic import inside the test and assert that loading succeeds so the missing entry point produces an assertion-level RED result. Node tests are development evidence; native OpenCode smoke remains the host-runtime proof.
- [ ] Implement the smallest adapter satisfying both verified native contracts. Avoid SDK runtime dependencies unless required by tested host loading. Set package identity `superpowers-backplane`, ESM mode, version equal to existing manifests, and one `index.js` main/export.
- [ ] Read canonical metadata without hardcoded skill bodies. Load file contents before registering replayable V2 transforms. Surface malformed/missing canonical files as a specific load error without partial unrelated-state edits.
- [ ] Add and observe failing tests for malformed/missing skill files, then implement error handling and rerun the full runtime test file to PASS. Verify package inventory includes skill references, root docs referenced by them, and license once #4 lands; no cache or `.sp-bp` material belongs in the package.

### Task 3: Guide and two installed-package smoke runs

**Files:** Create `docs/installing-opencode.md`; modify `README.md` to link it; complete the Task 1 evidence pair.

**Interfaces:** Consumes tested adapter and selected host contracts; produces reproducible initial install and exact smoke scores, with later lifecycle coverage explicitly pending.

- [ ] Document V1 `plugin` and V2 `plugins` configuration, prerequisites, separately installed Superpowers, immutable full-SHA Git package source, fresh-session verification and preservation checks. Mark setup/update/rollback/uninstall acceptance under their owning leaves. Do not present local development configuration as native package acceptance.
- [ ] Write `test_issue20_receipt.py` under `.sp-bp/work/issue-20/` using standard-library unittest. Use the Receipt contract below: test missing auth, missing host identity, unknown upstream provenance, source-tree discovery instead of installed discovery, absent skill-load evidence, and missing preservation evidence. Each incomplete case must be UNKNOWN; each observed failure must be FAIL; only a fully populated verified case may be PASS. Observe failing assertions before implementing `classify_smoke(record)` in the fixture runner.
- [ ] Run `uv run --no-project python -m unittest discover -s .sp-bp/work/issue-20 -p test_issue20_receipt.py -v`; expect all negative controls and the complete-case positive control to pass. Keep fixture source/evidence separate from product code.
- [ ] Install the fixture-local immutable commit through each host's native Git-package resolver using the exact source/config contract below. Verify no hardlinks or alternates in locally cloned repositories. A resolver that rejects the local Git source is FAIL for that attempted seam; hosted acceptance stays UNKNOWN pending explicit publication. Never count a local-directory substitution as Git-package acceptance.
- [ ] Run the exact fresh-session prompt and argument vectors below through the fixture runner. Check each required skill's successful native load and installed path/hash; record host, package and upstream identities and gh capability separately for V1 and V2. A model's unsupported narrative assertion is insufficient discovery evidence.
- [ ] Replay guide commands and compare unrelated plugins, user sentinels, upstream and project refs immediately before/after each operation. Require both smoke scores PASS; an unavailable model or host remains UNKNOWN.
- [ ] Run `node --test tests/opencode-adapter.test.mjs`, the receipt unittest command above, and `uv run --no-project python .sp-bp/work/issue-20/host-smoke.py verify`. The last command must check all package/guide links and installed inventory, source/metadata preservation, JSON schema/score consistency, and both native smoke records. Run `uv run --no-project ruff check .sp-bp/work/issue-20`, `uv run --no-project ruff format --check .sp-bp/work/issue-20`, `uv run --no-project ty check .sp-bp/work/issue-20`, and `git diff --check`. Compile any new Python guide examples and parse any new PowerShell examples. Missing evidence prevents a passing final gate.
- [ ] Obtain fresh whole-change review, fix Important/Critical findings, rerun affected checks and pass the active-to-review gate below before submission. Use branch finishing; record exact product and evidence-storage SHAs separately. Integration, publication and issue closure remain distinct decisions and gates.

## Lifecycle gates

Before each authorized mutation, run:

```text
gh issue view 20 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read the current plan and its issue semantics again when `updatedAt` changes. A planning label or artifact-pointer edit is not a scope change; changed criteria, new unresolved blockers or invalid label cardinality stop the intended transition. Capture observations before/after each operation; preserve unrelated labels and the native graph.

| Gate | Preconditions and action |
| --- | --- |
| backlog → designing | Actual planning has begun under the operator's instruction. Atomically remove backlog/add designing. |
| designing → ready | Operator approved this exact plan; design remains approved; approved plan has a tracked blob and an honest artifact pointer; #20 remains an open executable leaf with no unresolved blockers. Atomically remove designing/add ready. |
| ready → active | Re-read and revalidate eligibility immediately before the first approved execution task. Atomically remove ready/add active; capture the consumed revision in the execution ledger. |
| active → review | Implementation, both native smoke results, full applicable quality gate and independent review pass. Submission requires its own authority; the present request to revise the plan is not submission authority. If absent, leave active and present the review package. |
| blocked/resume | For a concrete impediment during authorized execution, record the exact failed probe, release condition and `Resume target: backplane:active`; atomically replace active with blocked. Revalidate the target's gates before restoring active. |

For an authorized transition, use one command, substituting only the verified source/target pair:

```text
gh issue edit 20 --repo tvproductions/superpowers-backplane --remove-label backplane:<source> --add-label backplane:<target>
```

Re-fetch full intake and require one expected lifecycle label, unchanged unrelated labels and unchanged semantics/graph. No transition is performed while merely revising or reviewing this draft. Publication, integration choice and completed closure retain their separate authority.

## Native verification contract

### Pinned hosts and adapter API

| Variant | Selected host | Source identity | Launch contract |
| --- | --- | --- | --- |
| V1 | 1.18.31 | `anomalyco/opencode` tag commit `014614d35b397775e5d397a490fc72368c894ec2` | Private in-process `run`; omit attach/continue/session flags. |
| V2 | 2.1.4 | tag commit `68bc26b7da1990ce10ffecfbc1e09eb13aa5d824` | `run --standalone`; never use the account-wide background service. |

These are selected smoke versions above the approved floors, not new minimums or a claim of universal version coverage. Current Windows V2 package metadata is `@opencode/cli` 2.1.4; its executable is `C:/Users/Jeff/AppData/Roaming/npm/node_modules/@opencode/cli/bin/opencode.exe`. Record its hash and invoke it read-only with the child environment. On this Windows x64 host, provision V1 only after fixture ownership checks with:

```text
gh release download v1.18.31 --repo anomalyco/opencode --pattern opencode-windows-x64.zip --dir <verified-area>/hosts/v1
```

Require archive SHA-256 `0ecd7ffc7f26390ce7799e7bcd409e4f11c410144308a6a5b0fcdce63d871006`, observed in release metadata on 2026-11-01. Extract with Python `zipfile` only after validating every entry's containment, and require the resulting executable to report 1.18.31. Never overwrite an occupied unknown destination. A different OS/architecture needs its own verified official asset and explicit plan amendment; do not execute a guessed binary.

The adapter interface in Task 2 is fixed for this plan. Verify the selected loaders accept it during preflight; any contradiction requires revision before implementation, not a second adapter or weakened tests. V2 callbacks receive an editor and use `add` with `id`, `name`, `description`, `path`, `content`; preload canonical file data and keep callbacks synchronous/replayable. V1 appends the absolute canonical directory through `config.skills.paths` without replacing existing configuration.

### Child environment and fixture location

Let `AREA` be the canonically verified ignored `.sp-bp/work/issue-20/` in the standalone repository and `P` be `AREA/profiles/v1` or `AREA/profiles/v2`. The Python runner constructs a child environment dictionary; it does not set parent-shell/system variables or repurpose a shell variable named HOME. Override the child's home-related variables only to isolate the host:

| Child variable | Value |
| --- | --- |
| `HOME`, `USERPROFILE`, `OPENCODE_TEST_HOME` | `P/home` |
| `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, `XDG_CACHE_HOME`, `XDG_STATE_HOME` | `P/config`, `P/data`, `P/cache`, `P/state`, respectively |
| `APPDATA`, `LOCALAPPDATA` | `P/roaming`, `P/local`, respectively |
| `TMPDIR`, `TMP`, `TEMP` | `P/tmp` |
| `OPENCODE_CONFIG_DIR` | `P/config/opencode` |
| V1 only: `OPENCODE_DISABLE_PROJECT_CONFIG`, `OPENCODE_DISABLE_AUTOUPDATE` | `true` |

Strip inherited `OPENCODE_*` values before applying the explicit allowlist above; do not inherit attach/server/config-content/database pointers. Preserve only deliberately selected authentication through an existing host-supported mechanism, never by copying credential files. Do not print secret-bearing environment values.

Run **both** hosts with `cwd=P/config/opencode`, their isolated global-config directory, with fixture `opencode.json` there. V2 2.1.4's versioned config discovery skips the ancestor walk when cwd canonically equals that directory; this prevents the repository's `opencode.jsonc` and `.agents/skills` from supplying false discovery. Keep the child home `.agents`, `.claude` and `.opencode` directories empty. For Windows also set child `ProgramData=P/programdata` to contain V2 system configuration. Inspect effective sources before inference; if any normal-profile, project-source or unapproved machine policy/plugin is active, stop at UNKNOWN rather than overriding policy or claiming isolation.

Before adding Backplane, the same isolated profile must discover the verified independent upstream and an unrelated sentinel, and must not discover either Backplane skill. Configure upstream using its recorded read-only sibling directory and verify its Git origin, clean revision and installed skill path. This is the compatible-preinstalled-upstream smoke case; acquisition/setup modes remain outside #20.

### Source installation and exact command vectors

Commit the candidate in the isolated worktree, record full `CANDIDATE_SHA`, then make a contained fixture mirror with `git clone --no-hardlinks --bare <verified-worktree> <AREA>/sources/backplane.git`. Verify its root, origin, candidate object, refs and absence of alternates before subsequent mutations. Construct `PACKAGE_SPEC` as `git+<Path(mirror).as_uri()>#<CANDIDATE_SHA>`; this is a **Git package** target, not a configured local directory. Use the same form for a pinned installed sentinel if a package sentinel is needed. Preserve these distinctions in receipts.

Write the fixture config with the runner's JSON encoder:

```json
{"plugin": ["<VERIFIED_UPSTREAM_DIRECTORY>", "<SENTINEL_TARGET>", "<PACKAGE_SPEC>"]}
```

For V2 the only change is `plugin` → `plugins`, plus global `"update": "disable"`. Include no Backplane `skills` path or discovery symlink. Native startup resolves the package. The eventual public guide uses `git+https://github.com/tvproductions/superpowers-backplane.git#<published-full-SHA>` only after that SHA exists remotely; this local fixture is not hosted transport evidence.

The runner uses `subprocess.run` argument lists, explicit UTF-8 capture, bounded timeouts and the child environment/cwd above. `V1_EXE` and `V2_EXE` are the verified absolute binary paths; `MODEL` is the explicitly recorded authenticated provider/model supported by that host, never an implicit fallback. Each command is a separate invocation:

```text
[V1_EXE, "--version"]
[V1_EXE, "run", "--help"]
[V1_EXE, "debug", "paths"]
[V1_EXE, "debug", "config"]
[V1_EXE, "debug", "skill"]
[V1_EXE, "run", "--format", "json", "--model", MODEL, PROMPT]
[V2_EXE, "--version"]
[V2_EXE, "run", "--help"]
[V2_EXE, "debug", "paths"]
[V2_EXE, "api", "GET", "/api/config", "--standalone", "--header", "x-opencode-directory:<P/config/opencode>"]
[V2_EXE, "api", "GET", "/api/plugin", "--standalone", "--header", "x-opencode-directory:<P/config/opencode>"]
[V2_EXE, "api", "GET", "/api/skill", "--standalone", "--header", "x-opencode-directory:<P/config/opencode>"]
[V2_EXE, "run", "--standalone", "--format", "json", "--model", MODEL, PROMPT]
```

`PROMPT` is fixed: `Use the native skill tool to load using-superpowers, managing-superpowers-backlog, and managing-superpowers-handoffs. Report each tool result and its source path. Do not query GitHub, mutate any issue or file, run setup, or delegate. Stop after reporting discovery.` Fresh sessions use no continuation/session identifiers. The bootstrap may load using-superpowers already; require its actual source evidence rather than inventing a redundant tool load. Capture the native skill calls/results for both Backplane skills. A handoff prerequisite refusal during this discovery-only prompt is not permission to query or change GitHub.

V2 API responses must identify the fixture location; require Backplane active at the candidate source and exact three skill paths. V1 debug inventory and native load results must supply equivalent file identities. Resolve Backplane paths under the **host-installed package cache**, compare hashes with the candidate Git blobs, and reject the development worktree, fixture mirror or repository-discovery paths. Compare upstream paths against its separately verified installation and preserve the unrelated sentinel.

The runner interface is:

```text
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py prepare
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py preflight --variant v1
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py preflight --variant v2
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py smoke --variant v1 --candidate <CANDIDATE_SHA> --model <authenticated-provider/model>
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py smoke --variant v2 --candidate <CANDIDATE_SHA> --model <authenticated-provider/model>
uv run --no-project python .sp-bp/work/issue-20/host-smoke.py verify
```

`prepare` validates containment/ownership and builds only the declared fixtures; `preflight` runs the non-inference commands, checks source isolation and auth availability, and produces a screened record; `smoke` runs one fresh prompt after successful preflight; `verify` validates both records plus inventory/links/preservation and exits nonzero for any FAIL or UNKNOWN. Help/command-shape checks are prerequisites, not claims that these planned native commands already passed. If a pinned command is unavailable, retain its failure and revise the plan before proceeding.

## Receipt contract and negative controls

`classify_smoke(record)` returns `FAIL` when any observed check is false, otherwise `UNKNOWN` if any required check/evidence is absent or unverified, otherwise `PASS`. This ordering prevents missing fields from hiding a known failure. Required record fields:

- `variant`, `host_version`, `host_source_sha`, `host_executable_sha256`, `candidate_sha`, `package_spec`, `installed_package_root`, `upstream_origin`, `upstream_revision`, `upstream_skill_path`, `model`, `session_id` and command exit codes;
- `auth_verified`, `source_isolated`, `gh_capabilities_verified`, `package_inventory_matches`, `protected_state_unchanged`, each as `true`, `false` or `null`;
- `skills`: exactly the required three identities, each with canonical source path, SHA-256, successful native discovery/load evidence and its capture digest;
- immutable capture references and before/after sentinel/upstream/metadata/ref snapshots. Keep raw streams ignored; persist screened evidence and fixture helper sources for portability.

Standard-library unittest cases must assert: the complete record is PASS; deleting each required field yields UNKNOWN; null authentication/provenance/load/preservation evidence yields UNKNOWN; a development-tree path yields FAIL; a failed native skill call yields FAIL; a failing preservation comparison remains FAIL even if authentication is missing; and a nonzero/timeout command never yields PASS. Use `subTest` to cover each required field. These are scoring tests, not expanded host setup/failure acceptance under #21/#23.

## Initial reconnaissance

The revision resolved the selected host tags with `gh api` and read their primary sources without launching or installing a host. V1 global/flag/config-path and run-command definitions confirm the XDG roots, `OPENCODE_TEST_HOME`, project-config switch and JSON run flags. V2 global-roots/config-discovery and CLI command definitions confirm the isolated-global-directory ancestor-walk exception, child ProgramData lookup, and `api`/`run` standalone support. V2 `debug config` has no standalone flag, so the contract uses `api GET /api/config --standalone` instead. Immutable source anchors:

- https://github.com/anomalyco/opencode/blob/014614d35b397775e5d397a490fc72368c894ec2/packages/core/src/global.ts
- https://github.com/anomalyco/opencode/blob/014614d35b397775e5d397a490fc72368c894ec2/packages/core/src/flag/flag.ts
- https://github.com/anomalyco/opencode/blob/014614d35b397775e5d397a490fc72368c894ec2/packages/opencode/src/config/paths.ts
- https://github.com/anomalyco/opencode/blob/014614d35b397775e5d397a490fc72368c894ec2/packages/opencode/src/cli/cmd/run.ts
- https://github.com/anomalyco/opencode/blob/68bc26b7da1990ce10ffecfbc1e09eb13aa5d824/packages/util/src/global-roots.ts
- https://github.com/anomalyco/opencode/blob/68bc26b7da1990ce10ffecfbc1e09eb13aa5d824/packages/core/src/config/discovery.ts
- https://github.com/anomalyco/opencode/blob/68bc26b7da1990ce10ffecfbc1e09eb13aa5d824/packages/cli/src/commands/commands.ts

The V1 release archive exists with the recorded digest. V2 2.1.4 has a resolved source tag and existing local package, but `gh release view v2.1.4` returned no release; do not invent a matching downloadable release archive. Initial guesses for versioned global/flag file locations returned 404; the source-tree lookup above resolved their actual paths. None of these source inspections establishes successful installed-package acceptance.

On 2026-11-01, current official V2 migration documentation explicitly describes one default export with `server()` and `setup()` for V1/V2. V2 server documentation describes synchronous `skill.transform` callbacks; V1 documentation retains singular `plugin`. Sources:

- https://opencode.ai/v2/docs/build/plugins/migrate-v1
- https://opencode.ai/v2/docs/build/plugins/server
- https://opencode.ai/v2/docs/plugins
- https://opencode.ai/docs/plugins/

The local upstream 7.0.1 implementation was read for API corroboration only; it stays read-only and is not copied. An initial normal-profile `opencode --version` attempted to open its log and failed with EPERM in the sandbox. Do not repeat that probe against the normal profile; future probes must use child-scoped disposable paths.
