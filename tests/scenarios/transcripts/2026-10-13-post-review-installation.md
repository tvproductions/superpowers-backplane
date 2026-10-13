Reject `/agents/superpowers` and leave it unchanged. Its origin is `obra/superpowers-plus`, not the required exact `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. The deadline and prior work do not waive those gates. Local changes independently prohibit an update; dirtiness alone would not prevent adopting an otherwise authoritative, complete, compatible checkout.

Using the designated candidate’s [installation contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md), I would apply this sequence. These are proposed operations only; no live verification was performed.

1. **Establish the managed destination and harness.** Confirm `/agents/upstream-superpowers` is unused and distinct from Backplane’s installation path. Identify the active harness and read its upstream-documented installation/discovery instructions. Keep upstream independently identifiable and updateable.

2. **Select stable, then install the authoritative repository.**

   ```sh
   gh auth status
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view <stable-tag> --repo obra/superpowers
   gh repo clone obra/superpowers /agents/upstream-superpowers
   ```

   Review the release notes and confirm `<stable-tag>` identifies the latest published stable release. No edge channel was selected, so do not use the default branch as the installed revision. Before switching the new checkout, verify its exact root, origin and clean status:

   ```sh
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   git -C /agents/upstream-superpowers status --short
   git -C /agents/upstream-superpowers checkout --detach refs/tags/<stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Require the root to resolve to the intended destination and normalize the origin to exactly GitHub owner/repository `obra/superpowers`. Record the tag and resolved commit.

3. **Verify the required upstream files.** Require all four:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

   Apply the host compatibility boundary too. For OpenCode, the documented minimums are V1 `1.18.29` and V2 `2.0.4`; older versions remain unsupported without separate testing and approval.

4. **Verify actual `gh` capabilities.**

   ```sh
   gh --version
   gh auth status
   gh issue view <real-issue> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   gh issue edit --help
   gh issue close --help
   ```

   Require the complete intake field surface, label addition/removal support, and closure reasons. Version text alone does not prove compatibility. These checks need no issue mutation.

5. **Configure discovery independently.** Expose `/agents/upstream-superpowers/skills` and Backplane’s authored `skills` directory through the active harness’s supported mechanism. Discovery links or junctions belong on that supported surface; do not copy upstream into Backplane or place Backplane artifacts inside upstream.

   In a fresh session, verify discovery and operation of upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus both Backplane skills: `managing-superpowers-backlog` and `managing-superpowers-handoffs`.

6. **Complete compatibility conformance before acceptance.** Record exact Superpowers and Backplane revisions, Backplane skill hashes, `gh` version, intake results, and harness scope. Run:

   - `skill-structure`: YAML delimiters, exact names, descriptions beginning `Use when`, existing directly linked references, and no unresolved placeholders.
   - `native-issue-intake`: the primary prompt/rubric in `2026-08-16-native-issue-intake-green.md`.
   - `language-neutral-verification`: that file’s language-neutral variation.
   - `lifecycle-transitions`: `2026-08-16-lifecycle-transition-refactor.md`.
   - `superpowers-installation`: `2026-08-16-superpowers-installation-refactor.md`.

   For each behavioral check, use a fresh session, submit the exact mapped prompt, capture its response, and score every expectation. Every expectation must pass. Missing captures, unavailable fields, failed discovery, or unscored results mean **unknown compatibility and fail closed**. The bootstrap baseline is historical evidence, not a permanent pin or proof for this candidate.

7. **Keep later updates separately authorized.** Before any upstream revision change, record its origin, current commit/version and rollback identity; refuse dirty or unknown installations. Inspect the latest stable release and notes, report the candidate, and obtain explicit authorization for that upstream revision change. Then fetch branches/tags, select the authorized stable tag—or explicitly selected edge branch—and repeat the full preflight, conformance and fresh-session discovery checks.

   If compatibility fails, restore the recorded prior revision through a supported, safe path where possible; otherwise report the unresolved state. Never discard local work or silently change upstream during a Backplane update.

Git, authenticated `gh`, and a skill-capable harness suffice. No programming-language runtime, GitHub Project, or IssueOps system is required.