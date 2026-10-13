**Reject `/agents/superpowers` and leave it untouched.** Its origin identifies `obra/superpowers-plus`, not the required `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. Deadline pressure and prior effort do not waive these gates. Dirtiness alone would permit adoption of an otherwise compatible authoritative checkout, but would prohibit its update.

Under the candidate’s [installation contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md), I would apply this sequence. These are hypothetical actions; none was executed.

1. **Establish the installation boundary.** Identify the active harness and its supported skill-discovery mechanism. Confirm `/agents/upstream-superpowers` remains unused and resolves separately from Backplane’s root. Keep the rejected checkout and its local changes intact.

2. **Select stable and obtain authoritative upstream.**

   ```sh
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view <returned-stable-tag> --repo obra/superpowers
   gh repo clone obra/superpowers /agents/upstream-superpowers
   ```

   Review the release notes for compatibility changes. Select the latest published stable release as the initial candidate; edge was not authorized. Cloning the repository’s default HEAD does not establish the selected installation revision.

3. **Verify and resolve the managed checkout.**

   ```sh
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   git -C /agents/upstream-superpowers status --short
   ```

   Require the exact intended root, normalized GitHub owner/repository `obra/superpowers`, and an empty status before revision changes. Then:

   ```sh
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers checkout --detach <returned-stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Record the origin, stable tag, resolved commit, and observation time. Require all four files:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

4. **Run compatibility preflight.** Record `gh --version`, verify `gh auth status`, and test the complete intake against a real issue in the repository in scope:

   ```sh
   gh issue view <issue-or-url> --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   gh issue edit --help
   gh issue close --help
   ```

   Require every intake field, label addition/removal support, and closure-reason support. Version text alone is insufficient. Apply applicable host compatibility requirements; the reference identifies OpenCode V1’s minimum as 1.18.29 and V2’s as 2.0.4.

5. **Expose independent skills and verify discovery.** Use the harness’s documented mechanism to expose upstream’s `skills/` and Backplane’s authored `skills/` separately. Discovery links are optional; verify their targets if used. In a fresh session, verify operational upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus both Backplane skills. Require discovery of `superpowers:using-superpowers` and `managing-superpowers-backlog`. Do not place Backplane artifacts inside upstream or `.superpowers/`.

6. **Run all five named conformance checks.** Inspect YAML delimiters, exact names, descriptions beginning `Use when`, linked-reference existence, and placeholders for `skill-structure`. For the behavioral checks, use fresh candidate sessions and the exact mapped prompts:

   - `native-issue-intake`: native-intake scenario, primary prompt.
   - `language-neutral-verification`: same scenario, language-neutral variation.
   - `lifecycle-transitions`: lifecycle-transition scenario.
   - `superpowers-installation`: installation scenario.

   Capture responses and score every expectation. Record upstream and Backplane revisions, Backplane skill hashes, harness scope, capability results, and limitations. Missing evidence or any unscored expectation means **unknown compatibility; fail closed**. Bootstrap evidence is not a permanent pin or proof for this candidate.

7. **Protect later updates.** Treat upstream updates separately from Backplane updates. Before each upstream revision change, record the current identity, refuse dirty or unknown installations, inspect stable release notes, report the candidate, and obtain explicit authorization. Fetch and select the authorized stable release; use the default branch only after explicit edge selection. Repeat compatibility, conformance, and fresh-session discovery checks. On failure, restore the recorded prior version where supported or report the unresolved state.

This requires Git, authenticated `gh`, and a skill-capable harness—no programming-language runtime, GitHub Projects, or IssueOps.