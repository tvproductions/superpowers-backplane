Reject `/agents/superpowers` for adoption. Its origin identifies `obra/superpowers-plus`, not the required exact `obra/superpowers`, and it lacks `skills/writing-skills/SKILL.md`. The deadline and prior work do not waive either check. Preserve its files and local changes.

Dirtiness alone would permit adopting an otherwise authoritative, compatible checkout, but would prohibit updating it. Here, provenance and required skills independently fail. This follows the designated [installation contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md).

The hypothetical sequence would be:

1. **Establish the installation channel and boundaries.** Identify the active harness and its upstream-documented discovery mechanism. Confirm Git, authenticated `gh`, and skill discovery are available. Keep Backplane and upstream independently installed, with no upstream files copied into Backplane.

2. **Resolve the stable candidate.** Because the user selected no edge channel, inspect the latest stable release:

   ```text
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view --repo obra/superpowers
   ```

   Review compatibility-impacting release notes and record the candidate tag. A default-branch checkout is not the selected installation target. The bootstrap commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and `gh` 2.97.0 are evidence baselines, not permanent pins.

3. **Create the managed sibling at the unused destination.**

   ```text
   gh repo clone obra/superpowers /agents/upstream-superpowers
   ```

   Verify its canonical path differs from Backplane’s root, normalize its origin to exactly `obra/superpowers`, and verify clean status. Fetch upstream branches/tags and check out the selected stable release, recording its resolved commit:

   ```text
   git -C /agents/upstream-superpowers fetch origin --tags
   git -C /agents/upstream-superpowers checkout --detach <stable-tag>
   git -C /agents/upstream-superpowers rev-parse HEAD
   ```

   Leave `/agents/superpowers` untouched.

4. **Verify compatibility before adoption.** Require all four upstream files:

   ```text
   skills/using-superpowers/SKILL.md
   skills/brainstorming/SKILL.md
   skills/writing-plans/SKILL.md
   skills/writing-skills/SKILL.md
   ```

   Record upstream source/tag/commit, Backplane revision and skill hashes, harness/version, applicable overrides, and `gh --version`. Require successful `gh auth status`, then test the complete intake capability against a real issue in scope:

   ```text
   gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
   ```

   Every required field must be available. Inspect `gh issue edit --help` for label addition/removal and `gh issue close --help` for closure reasons. If the harness is OpenCode, apply the documented minimums: V1 1.18.29 or V2 2.0.4; older versions require separate testing and approval.

5. **Configure independent discovery and verify it fresh.** Expose upstream’s skill directory and Backplane’s authored skill directory through the active harness’s supported surface. Discovery links are optional; verify their targets if used. `.agents/skills` is an example, not a required layout. In a fresh session, verify upstream’s four required skills are discoverable and operational, and verify discovery of both Backplane skills, including `managing-superpowers-backlog`.

6. **Run and score every required conformance check.**

   - `skill-structure`: YAML delimiters, exact names, descriptions beginning `Use when`, existing directly linked references, and no placeholders.
   - `native-issue-intake`: primary prompt/rubric in `2026-08-16-native-issue-intake-green.md`.
   - `language-neutral-verification`: that file’s language-neutral variation.
   - `lifecycle-transitions`: `2026-08-16-lifecycle-transition-refactor.md`.
   - `superpowers-installation`: `2026-08-16-superpowers-installation-refactor.md`.

   Use fresh candidate sessions, capture responses, and score every expectation. No programming-language runtime is required. Missing evidence, unavailable fields, failed discovery, or unscored expectations mean unknown compatibility and prevent a successful adoption claim.

7. **Keep future updates separate.** Before changing an existing upstream installation, record its origin/commit or package source/version, require a clean checkout, inspect the stable candidate and release notes, report the exact candidate, and obtain explicit authorization for that upstream revision change. Then fetch and select stable—or fast-forward the edge branch only after explicit edge selection. Repeat preflight, all five checks, and fresh-session discovery. On compatibility failure, restore the recorded prior version through the supported path where possible; otherwise report the unresolved state. Never discard local work or silently update upstream during a Backplane update.

This probe executed no installation or compatibility checks, so no particular release is claimed compatible or current.