**Reject `/agents/superpowers` and leave it untouched.** Its origin is `obra/superpowers-plus`, not the required `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. The deadline and prior work do not override these gates. A dirty, otherwise valid checkout could be adopted after all checks pass, but could not be updated while dirty. [Installation contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md)

The following is the hypothetical sequence; none of these commands has been executed.

1. **Establish the managed installation.** Identify the active harness and read its upstream-documented installation and discovery instructions. Confirm `/agents/upstream-superpowers` is unused, resolves separately from Backplane, and can hold an independent checkout. Use the available destination without renaming or modifying `/agents/superpowers`:

   ```sh
   gh repo clone obra/superpowers /agents/upstream-superpowers
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   git -C /agents/upstream-superpowers status --short
   ```

   Require the canonical root to match the intended destination, the normalized origin owner/repository to be exactly `obra/superpowers`, and the status output to be empty before changing revisions. HTTPS and SSH transports are acceptable.

2. **Select stable explicitly.** Inspect the latest published stable release and its compatibility-impacting notes:

   ```sh
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view --repo obra/superpowers
   ```

   Use the returned stable release tag; do not invent a version or leave the clone on the default branch. Edge was not selected.

   ```sh
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers checkout --detach <stable-release-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Record the source, channel, release tag, and resolved commit. Treat that release as a compatibility candidate until verification passes. The bootstrap commit is an authoring baseline, not a permanent pin.

3. **Run the compatibility preflight.** Require these files in the candidate checkout:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

   Verify the actual harness compatibility boundary; for OpenCode, the documented minimums are V1 1.18.29 and V2 2.0.4. Record `gh --version`, confirm authentication for the repository in scope, and execute the complete required-field intake against a real issue during the actual installation:

   ```sh
   gh auth status
   gh issue view <issue-or-url> --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   gh issue edit --help
   gh issue close --help
   ```

   Require every intake field, label addition/removal support, and closure reasons. Version text alone does not establish capability.

   Run all five named checks: `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation`. Inspect skill metadata, linked-reference existence, and placeholders; run behavioral checks in fresh candidate sessions using the exact mapped scenario prompts, capture responses, and score every expectation. Record candidate identities, Backplane skill hashes, and evidence. Missing evidence, unavailable fields, or any unscored expectation means **unknown compatibility: fail closed**. [Native intake contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md)

4. **Verify independent discovery.** Expose these directories through the active harness’s supported mechanism:

   ```text
   /agents/upstream-superpowers/skills
   <backplane-root>/skills
   ```

   Discovery links are optional; verify their targets before relying on them. Keep upstream and Backplane separately installed. In fresh sessions, confirm the required upstream skills are discoverable and operational, including `superpowers:using-superpowers`, and confirm both `managing-superpowers-backlog` and `managing-superpowers-handoffs`. Conflicting duplicate discovery or missing skills blocks completion.

5. **Preserve update safety.** A later upstream revision change is separate from a Backplane update. Record the current origin/commit, refuse dirty or unknown installations, inspect the candidate stable release and notes, then obtain explicit authorization **before changing the existing upstream revision**. Fetch and check out the authorized stable release; use an edge branch only after explicit edge selection, with fast-forward-only advancement. Never discard local work. Repeat the full preflight, conformance checks, and fresh-session discovery. If compatibility fails, restore the recorded prior revision through a supported, authorized path where possible; otherwise report the unresolved state.

No programming-language runtime, GitHub Project, IssueOps system, or helper engine is required. Keep Backplane artifacts outside shipped upstream and `.superpowers/`. Compatibility records must identify the actual evaluated revisions and limitations; an older pass does not prove a new candidate compatible. [Governance](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers-backplane/governance.md)