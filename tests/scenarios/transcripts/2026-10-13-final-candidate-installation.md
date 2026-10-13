Reject `/agents/superpowers` and leave it unchanged. `obra/superpowers-plus` is not the required `obra/superpowers` identity, and `writing-skills` is missing. The deadline and prior work do not waive those checks. Dirt alone can permit adoption of an otherwise authoritative, compatible checkout, but it prevents updating it.

I would apply this sequence. Commands below are hypothetical; none were executed.

1. **Establish the installation boundary.** Identify the active harness and its upstream-documented checkout installation and discovery mechanism. Keep Backplane and Superpowers independently identifiable. With Backplane at `/agents/superpowers-backplane`, confirm `/agents/upstream-superpowers` is unused, including absence of a dangling symlink. Require Git, authenticated `gh`, and skill discovery.

2. **Select stable and obtain authoritative upstream.**

   ```sh
   gh auth status
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view <returned-stable-tag> --repo obra/superpowers
   gh repo clone obra/superpowers /agents/upstream-superpowers
   ```

   Review compatibility-impacting release notes. Use the latest published stable release as the candidate because edge was not selected. Do not run from the clone’s default branch merely because cloning initially checked it out.

3. **Verify the clone, then select the release.**

   ```sh
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   git -C /agents/upstream-superpowers status --short
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Require the resolved root to be the new destination and distinct from Backplane. Normalize HTTPS or SSH origin syntax and require exactly GitHub owner/repository `obra/superpowers`. Require an empty status and record the initial commit before proceeding.

   ```sh
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers checkout --detach refs/tags/<returned-stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Record the selected tag and resolved commit. Require these files at that revision:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

4. **Expose both installations independently.** Use the active harness’s supported discovery surface, pointing to `/agents/upstream-superpowers/skills` and Backplane’s authored skills under `/agents/superpowers-backplane/skills`. `/agents/skills` may contain links or junctions if the harness supports that layout; it is not a required protocol. Preserve existing discovery entries, reject conflicting duplicates, and never copy Backplane artifacts into upstream.

   In a fresh session, verify discovery and operation of upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus both Backplane skills, `managing-superpowers-backlog` and `managing-superpowers-handoffs`.

5. **Establish compatibility with the actual installed tuple.**

   ```sh
   gh --version
   gh auth status
   gh issue view <real-issue-or-url> --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   gh issue edit --help
   gh issue close --help
   ```

   Require all 15 intake fields, label addition/removal capability, and closure reasons. Record upstream source/tag/commit, harness scope, `gh` version, intake evidence, and Backplane skill hashes.

   Run all five named conformance checks:

   - `skill-structure`: inspect YAML delimiters, exact names, descriptions beginning `Use when`, linked-reference existence, and absence of placeholders.
   - `native-issue-intake`: primary prompt and rubric in `2026-08-16-native-issue-intake-green.md`.
   - `language-neutral-verification`: its language-neutral variation.
   - `lifecycle-transitions`: `2026-08-16-lifecycle-transition-refactor.md`.
   - `superpowers-installation`: `2026-08-16-superpowers-installation-refactor.md`.

   Execute behavioral probes in fresh sessions with the candidate installed skills, capture responses, and score every expectation. Historical bootstrap passes and version numbers do not establish this candidate’s compatibility. Missing evidence, fields, discovery, or scoring means **unknown compatibility: fail closed**. Adopt only after every gate passes; do not silently substitute another release.

6. **Keep subsequent updates separately authorized.** Before any later upstream revision change, record the exact origin, installed tag/commit, and rollback identity; recheck provenance and cleanliness. Refuse updates to dirty or unknown installations. Inspect the latest stable release and notes, report the candidate, and obtain explicit authorization for that upstream revision change. Then fetch and select the authorized stable tag; follow an upstream branch only after explicit edge selection.

   Repeat compatibility checks and fresh-session discovery, then record the result. If compatibility fails, restore the recorded prior revision where safely possible or report the unresolved state. Preserve local work, Backplane, and unrelated installations.

This sequence requires no programming-language runtime, GitHub Project, or IssueOps system.