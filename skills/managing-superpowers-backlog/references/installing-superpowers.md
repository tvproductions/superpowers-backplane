# Installing Backplane With Superpowers

## Dependency rule

Backplane always assumes upstream Superpowers. Installation must either adopt a
compatible sibling checkout or obtain upstream Superpowers for the user.

Keep Superpowers as a separate Git checkout whose remote identifies the
authoritative `obra/superpowers` repository. Do not copy its tracked files into
Backplane or vendor them under a harness-specific skill directory.

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

Do not rewrite or relocate a valid user-managed checkout merely to match an
example layout.

## Managed mode

When Superpowers is absent, require an unused destination and obtain the
authoritative repository:

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

Use the latest published upstream GitHub release as the default stable channel.
Use the upstream default branch only when the user explicitly selects the edge
channel.

Before an update:

1. Refuse to update a dirty Superpowers checkout.
2. Fetch upstream branches and tags.
3. Inspect the latest stable release with
   `gh release view --repo obra/superpowers --json tagName,publishedAt,url`.
4. Report compatibility-impacting release notes and the proposed revision.
5. Obtain explicit authorization for the revision change.
6. For stable, check out the published release. For edge, fast-forward only
   along the upstream default branch. Never discard local work.
7. Run the compatibility preflight and Backplane conformance checks.
8. Record the resolved revision for diagnosis, not as an unreviewed permanent
   pin.

If compatibility cannot be established, leave the checkout unchanged.

## Compatibility preflight

Backplane is known-good at bootstrap against Superpowers commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and `gh` 2.97.0. These identify
the authoring baseline, not permanent pins.

Before adoption or update:

1. Verify the authoritative origin and required Superpowers skill files above.
2. Verify `gh auth status` succeeds for the GitHub repository in scope.
3. Run the required intake query from `github-issue-contract.md` against a
   real issue. Failure to return any required JSON field is an incompatible
   `gh` capability surface, regardless of version text.
4. Verify `gh issue edit --help` exposes label addition and removal, and
   `gh issue close --help` exposes closure reasons.
5. Run the named conformance checks: `skill-structure`,
   `native-issue-intake`, `language-neutral-verification`,
   `lifecycle-transitions`, and `superpowers-installation`.
6. Confirm both skills are discoverable in a fresh agent session.

Run the checks without assuming a programming-language runtime:

1. Record the candidate Superpowers commit, `gh --version`, required-field
   intake result, and Backplane skill-file hashes.
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
