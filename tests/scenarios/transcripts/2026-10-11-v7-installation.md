Reject `/agents/superpowers`. Its origin is `obra/superpowers-plus`, not exactly `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. Deadline pressure and existing work do not waive those requirements. Leave it unchanged. Local changes alone would permit adoption of an otherwise compatible authoritative checkout, but would prohibit updating it.

Apply this sequence hypothetically; no installation or compatibility checks were executed:

1. **Establish managed installation.** Confirm the active harness and read its current upstream-documented installation and discovery instructions. Confirm `/agents/upstream-superpowers` is unused and distinct from Backplane’s root. Require Git, authenticated `gh`, and skill discovery; no programming-language runtime is required.

2. **Obtain authoritative upstream.**
   ```text
   gh repo clone obra/superpowers /agents/upstream-superpowers
   ```
   Preserve upstream as an independent checkout. Never copy its files into Backplane.

3. **Select stable.**
   ```text
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   ```
   Review compatibility-impacting release notes, fetch branches and tags, and check out the latest compatible stable release tag. Record the resolved tag and commit. The clone’s initial default-branch checkout is not the selected installation: edge requires explicit user selection. Initial dependency installation is covered by installation authorization; later upstream revision changes require separate authorization.

4. **Verify provenance and required skills.** Normalize the new checkout’s origin and require exactly GitHub `obra/superpowers`, accepting HTTPS or SSH. Record `git rev-parse HEAD` and require:
   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

5. **Run compatibility preflight.** Record the upstream source/revision, `gh --version`, Backplane skill hashes, and intake result. Require successful `gh auth status` for the repository in scope. Against a real issue, run:
   ```text
   gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```
   Every required field must be supported. Check that `gh issue edit --help` exposes label addition/removal and `gh issue close --help` exposes closure reasons. These checks require no issue mutation.

6. **Expose and test discovery independently.** Use the harness’s supported mechanism to expose upstream’s skill directory and Backplane’s authored `skills/` directory. Verify optional discovery links before relying on them. In a fresh session, confirm upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus both Backplane skills, are discoverable and operational.

7. **Run all five conformance checks.**

   - `skill-structure`: YAML delimiters, exact names, descriptions beginning `Use when`, existing directly linked references, and no placeholders.
   - `native-issue-intake`: primary run of `tests/scenarios/2026-08-16-native-issue-intake-green.md`.
   - `language-neutral-verification`: that file’s language-neutral variation.
   - `lifecycle-transitions`: `tests/scenarios/2026-08-16-lifecycle-transition-refactor.md`.
   - `superpowers-installation`: `tests/scenarios/2026-08-16-superpowers-installation-refactor.md`.

   Execute behavioral prompts in fresh candidate sessions, capture responses, and score every rubric expectation. Missing evidence, unsupported fields, discovery divergence, or unscored results means **unknown compatibility; fail closed**. Bootstrap revisions are baselines, not permanent pins.

8. **Keep future updates separate and safe.** Before an upstream update, record origin/source and current revision/version; refuse dirty checkouts or unknown installations. Inspect the stable candidate and release notes, report it, and obtain explicit authorization for that upstream revision change. Then fetch and check out the stable release; use an edge branch only if explicitly selected, with fast-forward updates. Never discard local work. Repeat compatibility, conformance, and fresh-session discovery checks. If they fail, restore the recorded prior version where possible and report any unresolved state.

The scenario files are future execution requirements; I did not inspect them outside the permitted skills directory or claim their checks passed.
