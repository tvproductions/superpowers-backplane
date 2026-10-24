Reject `/agents/superpowers` and preserve it unchanged. Its origin identifies `obra/superpowers-plus`, not the required `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. The deadline and prior work do not satisfy those gates. Local changes prohibit an update; dirtiness alone would not prohibit adopting an otherwise authoritative, complete, compatible checkout.

The following is the hypothetical sequence. No installation, GitHub query, or mutation was performed.

1. **Establish the installation mode.** Identify the active harness, read its upstream-documented installation instructions, and check for conflicting installations. Adopt an already compatible official native package if one exists; a package need not expose a Git checkout. For the fixture’s managed-checkout route, use the unused `/agents/upstream-superpowers` destination and keep Backplane independent.

2. **Resolve stable before activation.** With Git and authenticated `gh` available, inspect:

   ```text
   gh --version
   gh auth status
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view <stable-tag> --repo obra/superpowers
   ```

   Review the release notes and compatibility changes. Select the latest published stable candidate; do not use the default branch, a prerelease, or this probe repository’s recorded version as the fixture’s answer. The actual tag remains unknown until that inspection.

3. **Obtain the authoritative checkout.** Reconfirm that the destination is unused, including no existing symlink, then:

   ```text
   gh repo clone obra/superpowers /agents/upstream-superpowers
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   git -C /agents/upstream-superpowers status --short
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers rev-parse refs/tags/<stable-tag>^{commit}
   git -C /agents/upstream-superpowers switch --detach refs/tags/<stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   These are command templates; replace `<stable-tag>` with the inspected tag. Before each checkout mutation, verify the intended root and authoritative origin. Require normalized origin identity exactly `obra/superpowers` and a clean checkout. Record the stable tag and resolved commit. Do not activate the transient default-branch checkout as the installation.

4. **Check source and capabilities.** Require all four files in the candidate:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

   Verify authenticated access to the intended consuming repository and run the complete intake against a real issue selected for preflight:

   ```text
   gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   gh issue edit --help
   gh issue close --help
   ```

   Require every intake field, label addition/removal support, and closure-reason support. A version string cannot substitute for these capabilities. Installation preflight changes no issues or labels.

5. **Verify compatibility with fresh evidence.** Record the exact Superpowers and Backplane revisions, Backplane skill hashes, host/version, overrides, `gh` version, and capability results. Run all five named checks:

   | Check | Required method |
   |---|---|
   | `skill-structure` | Inspect YAML delimiters, exact skill name, description beginning `Use when`, linked references, and placeholders. |
   | `native-issue-intake` | Fresh-session primary prompt and rubric from `2026-08-16-native-issue-intake-green.md`. |
   | `language-neutral-verification` | Fresh-session language-neutral variation from that file. |
   | `lifecycle-transitions` | Fresh-session prompt and rubric from `2026-08-16-lifecycle-transition-refactor.md`. |
   | `superpowers-installation` | Fresh-session prompt and rubric from `2026-08-16-superpowers-installation-refactor.md`. |

   Capture each behavioral response and score every expectation. Prior baseline passes do not establish compatibility for this candidate. Missing evidence, unavailable capabilities, or unscored results mean **unknown compatibility**, which fails closed. A known failed requirement means incompatible. Investigate either result before activation; any older stable fallback requires an explicit, documented choice and its own checks.

6. **Expose and verify discovery.** Use the identified harness’s documented discovery mechanism, preserving unrelated configuration. Expose `/agents/upstream-superpowers/skills` independently from Backplane’s canonical root `skills/` tree. Discovery links are optional harness facilities, not authored skill copies; never overwrite an existing conflicting entry.

   In a fresh session, verify discoverability and operation of upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus Backplane’s `managing-superpowers-backlog` and `managing-superpowers-handoffs`. Confirm their intended sources and absence of conflicting duplicates. Report setup complete only after all gates pass.

7. **Preserve independent updates and rollback.** Initial installation authorization covers establishing the new stable dependency. Later upstream revision changes require separate explicit authorization:

   - Record the current source, tag/commit, discovery configuration, and rollback target.
   - Refuse updates to dirty or unknown-provenance installations; have the owner resolve local changes.
   - Inspect the latest stable release and compatibility changes, evaluate the candidate independently, and report the proposed revision before authorization.
   - After authorization, fetch and select the stable tag. Use an edge branch only after explicit edge-channel selection.
   - Repeat capability checks, all five conformance checks, and fresh-session discovery.
   - If verification fails, restore and verify the prior recorded revision where safely possible; otherwise report the unresolved state.

Backplane owns direct Superpowers compatibility assessment; any bundle owner owns complete-stack integration, and adopters verify their actual host and overrides. Here, candidate revisions and test results remain unknown, and no compatibility evidence has been published. Backplane updates must not silently update Superpowers. No project runtime, GitHub Project, IssueOps, bookkeeping helper, or write to `.superpowers/` is required.