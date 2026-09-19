# Installing Backplane With Superpowers

## Dependency rule

Backplane always assumes upstream Superpowers. Each supported harness needs an
operational, independent upstream installation. Adopt a compatible existing
native plugin or sibling Git checkout. If upstream is absent, obtain it through
the harness's upstream-documented installation channel. Never copy upstream
files into Backplane or require a second checkout solely because a native
plugin does not expose one.

Backplane's authored skills live at
`<backplane-root>/skills/managing-superpowers-backlog/SKILL.md` and
`<backplane-root>/skills/managing-superpowers-handoffs/SKILL.md`. A harness
discovery directory such as `.agents/skills` contains optional links; it is
not the Backplane package's skill root. Verify a link exists before using that
directory as a discovery source.

## Native package mode

Read the current upstream Superpowers installation instructions for the active
harness before using its plugin manager. Upstream may be installed from an
authoritative `obra/superpowers` Git package source or an official marketplace
channel that upstream itself documents. A package cache need not be a Git
checkout.

1. Verify the active harness and package identity. Confirm the source or
   catalog is upstream-documented; reject lookalikes, unknown provenance, and
   conflicting duplicate installations.
2. Record the package ID, source or catalog, installed version, and resolved
   tag or commit when the harness exposes one. If neither an installed version
   nor a resolved revision is observable, compatibility is unknown.
3. Confirm in a fresh session that the upstream `using-superpowers`,
   `brainstorming`, `writing-plans`, and `writing-skills` skills are
   discoverable and operational.
4. Adopt a compatible package in place. Do not clone or relocate upstream
   solely to satisfy checkout-mode rules. If upstream is absent, install it
   through that harness's documented stable channel and preserve host prompts
   and permissions.
5. Check the host compatibility boundary in the v0.1 adoption specification.
   OpenCode V1 starts at 1.18.29 and V2 at 2.0.4; an older version is reported
   unsupported until separately tested and approved.

The repository's own development checkout at `.agents/superpowers` remains a
separate checkout. Its existence does not prove another harness has an
operational native plugin.

## Sibling mode

When a Superpowers checkout already exists:

1. Resolve its absolute path and require it to differ from Backplane's path.
2. Normalize `git -C <path> remote get-url origin` and require the GitHub owner
   and repository to be exactly `obra/superpowers`; accept HTTPS or SSH
   transport but reject lookalikes.
3. Require `git -C <path> status --short` to be empty before an update.
4. Require `skills/using-superpowers/SKILL.md`,
   `skills/brainstorming/SKILL.md`, `skills/writing-plans/SKILL.md`, and
   `skills/writing-skills/SKILL.md`.
5. Record `git -C <path> rev-parse HEAD` for diagnosis.
6. Expose the Superpowers and Backplane skill directories independently
   through the active harness's supported discovery mechanism.
7. Verify from a fresh agent session that both `superpowers:using-superpowers`
   and `managing-superpowers-backlog` appear in skill discovery.

An authoritative sibling checkout with local changes may be adopted in place
after provenance, required skills, compatibility, and discovery checks pass.
Report adoption separately from a requested update. Refuse the update while the
checkout is dirty; leave its files unchanged and ask its owner to resolve the
local changes before any separately authorized revision change.

Do not rewrite or relocate a valid user-managed checkout merely to match an
example layout.

## Managed checkout mode

When a checkout is required and no compatible one exists, require an unused
destination and obtain the authoritative repository:

```text
gh repo clone obra/superpowers <installation-root>/superpowers
```

Place Backplane beside it when practical:

```text
<installation-root>/
  superpowers/
  superpowers-backplane/
  skills/                    harness discovery links or junctions
```

Use the active harness's supported discovery surface. `.agents/skills` is a
valid cross-runtime example, not a protocol requirement.

## Channels and updates

Use the latest compatible stable upstream release available through the selected
channel by default.
Use the upstream default branch only after an explicit edge-channel selection.
An upstream update is separate from a Backplane update.

Before changing an existing upstream installation:

1. Record its package source and version or checkout origin and commit. Refuse
   to update a dirty checkout or overwrite an unknown installation.
2. Inspect the latest stable release with
   `gh release view --repo obra/superpowers --json tagName,publishedAt,url`
   and review compatibility-impacting release notes.
3. Report the candidate version and obtain explicit authorization for this
   upstream revision change.
4. In native package mode, update only the Superpowers plugin through the
   active harness's documented manager, preserving Backplane and unrelated
   plugins. Record the prior package source and version for rollback.
5. In checkout mode, fetch upstream branches and tags; check out the stable
   release or fast-forward along the selected edge branch. Never discard local
   work.
6. Run the compatibility preflight and all Backplane conformance checks.
   Verify required skills again in a fresh session, then record the installed
   version or resolved revision.

If compatibility fails, restore the recorded prior version through the
harness's supported path where possible; otherwise report the unresolved
state. Never claim a failed candidate is compatible or silently mutate the
independent upstream installation.

## Compatibility preflight

Backplane is known-good at bootstrap against Superpowers commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and `gh` 2.97.0. These identify
the authoring baseline, not permanent pins.

Before adoption or update:

1. Verify mode-specific upstream provenance: its upstream-documented package
   source and observable version or revision in native mode, or its exact
   `obra/superpowers` Git origin and required skill files in checkout mode.
2. Verify `gh auth status` succeeds for the GitHub repository in scope.
3. Run the required intake query from `github-issue-contract.md` against a
   real issue. Failure to return any required JSON field is an incompatible
   `gh` capability surface, regardless of version text.
4. Verify `gh issue edit --help` exposes label addition and removal, and
   `gh issue close --help` exposes closure reasons.
5. Run the named conformance checks: `skill-structure`,
   `native-issue-intake`, `language-neutral-verification`,
   `lifecycle-transitions`, and `superpowers-installation`.
6. Confirm `using-superpowers` and both Backplane skills are discoverable in a
   fresh agent session.

Run the checks without assuming a programming-language runtime:

1. Record the candidate Superpowers source and version or commit,
   `gh --version`, required-field intake result, and Backplane skill hashes.
2. For `skill-structure`, inspect `SKILL.md` for YAML delimiters, the exact
   `name` and a `description` beginning with `Use when`; verify every directly
   linked reference exists and no placeholder remains. A harness-native skill
   validator may supplement this checklist but is not a hard dependency.
3. For each behavioral check, start a fresh agent session with the candidate
   Superpowers and Backplane skill, submit the exact prompt in the mapped file,
   capture a response record, and score every listed expectation:

| Check | Scenario and rubric |
|---|---|
| `native-issue-intake` | `tests/scenarios/2026-08-16-native-issue-intake-green.md`, primary run |
| `language-neutral-verification` | same file, language-neutral variation |
| `lifecycle-transitions` | `tests/scenarios/2026-08-16-lifecycle-transition-refactor.md` |
| `superpowers-installation` | `tests/scenarios/2026-08-16-superpowers-installation-refactor.md` |

Every expectation must pass. Missing capture, unavailable fields, divergent
skill discovery, or an unscored result is unknown compatibility and fails
closed. Bootstrap evidence exists for all five named checks against the
known-good revisions above; candidate revisions require fresh execution.

## Hard dependencies

- GitHub CLI (`gh`), authenticated for the repositories in scope.
- Git, as required by Superpowers development workflows.
- An agent harness capable of discovering skills.

Do not require a programming language runtime, GitHub Projects, or IssueOps.
