Reject `/agents/superpowers`: its origin identifies `obra/superpowers-plus`, not the required `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. The deadline and prior work do not waive those checks. Preserve it unchanged. Local changes alone would allow adoption of an otherwise authoritative, compatible checkout, but would prohibit updating it. These distinctions come from the designated [installation contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md).

I would apply this sequence in an actual authorized installation:

1. **Establish the harness and installation boundary.** Confirm one effective Backplane installation, with both canonical Backplane skills visible. Read the selected upstream release’s installation instructions for that harness. Use its supported discovery mechanism; do not assume `/agents/skills` is supported merely because it is convenient.

2. **Create an independent managed checkout.** Confirm `/agents/upstream-superpowers` is unused and separate from Backplane. Clone the authoritative repository, leaving the rejected checkout intact:

   ```sh
   gh repo clone obra/superpowers /agents/upstream-superpowers -- --no-checkout
   ```

   Verify the new checkout’s canonical root and normalize its origin to exactly `obra/superpowers`.

3. **Resolve the stable channel.** Inspect the current stable release:

   ```sh
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   ```

   Review that release’s compatibility-impacting notes. Fetch its tag and check out the resolved stable release:

   ```sh
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers checkout --detach <stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Record the source, stable channel, tag, publication time, and resolved commit outside upstream. The default branch requires an explicit edge selection. Historical baseline revisions are diagnostic evidence, not permanent pins or proof of today’s latest release.

4. **Check upstream completeness.** Require all four files:

   - `skills/using-superpowers/SKILL.md`
   - `skills/brainstorming/SKILL.md`
   - `skills/writing-plans/SKILL.md`
   - `skills/writing-skills/SKILL.md`

5. **Run the compatibility preflight.** Verify `gh auth status`, record `gh --version`, and query an actual in-scope issue using the complete required intake:

   ```sh
   gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Confirm `gh issue edit --help` supports label addition/removal and `gh issue close --help` supports closure reasons. Version text cannot substitute for these capabilities.

   Run all five named checks: `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation`. Record candidate revisions, Backplane skill hashes, captured responses, and every scored expectation. Missing or unscored evidence leaves compatibility **unknown**.

6. **Verify independent discovery.** Expose upstream and Backplane separately through the harness’s supported mechanism. In fresh sessions, confirm the four required upstream skills are operational and both `managing-superpowers-backlog` and `managing-superpowers-handoffs` are discoverable. Reconcile conflicting installations before claiming setup complete.

7. **Keep future updates separate and reversible.** Before each upstream revision change, record the prior origin, tag/commit, discovery configuration, and rollback target; require an empty `git status --short`. Inspect the stable candidate and report compatibility implications, then obtain explicit authorization for that update. Backplane installation authorization does not authorize later upstream revision changes. Fetch and select the approved release, repeat preflight, all five checks, and fresh discovery. If verification fails, restore and verify the prior revision where possible; otherwise report the unresolved state.

Keep upstream independently updateable, with its authoritative remote intact. Store Backplane records outside upstream, preserve unrelated files and installations, and make no GitHub lifecycle changes during setup. Git, authenticated `gh`, and harness-native capabilities suffice; no programming-language runtime is prescribed.

This probe performed only permitted source reads. No live release lookup, installation, compatibility execution, or mutation occurred, so no particular stable version or successful installation is claimed.