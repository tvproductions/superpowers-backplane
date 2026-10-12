**Reject `/agents/superpowers` and leave it untouched.** `obra/superpowers-plus` is a lookalike origin, and the required `writing-skills` file is missing. The deadline and prior work do not waive these checks. Local changes independently prohibit updating it; an otherwise authoritative, compatible dirty checkout could be adopted without updating.

I read the active inventory’s `using-superpowers`, its Codex reference, `managing-superpowers-backlog`, all three backlog references, and the required governing and conformance documents. The sequence below follows [installing-superpowers.md](/Users/jeff/Documents/Code/superpowers-backplane/.agents/skills/managing-superpowers-backlog/references/installing-superpowers.md). **All commands below are hypothetical and unexecuted.**

1. **Establish the harness and installation identities.**

   Identify the hypothetical harness, version, supported discovery mechanism, and actual Backplane root under `/agents`. Read that harness’s current upstream installation instructions. Confirm one effective Backplane installation and check for an existing authoritative native Superpowers package before requiring a checkout.

   A compatible native package would be adopted in place. For the requested managed-checkout route, use the unused `/agents/upstream-superpowers` destination. Keep upstream independently managed; copy no upstream files into Backplane.

   The scenario does not establish the harness version, package inventory, Backplane revision, or discovery configuration. These remain **unknown**.

2. **Select the stable candidate and obtain authoritative upstream.**

   ```sh
   gh --version
   gh auth status
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   gh release view --repo obra/superpowers
   gh api repos/obra/superpowers/releases/latest \
     --jq '{tag: .tag_name, publishedAt: .published_at, draft: .draft, prerelease: .prerelease, url: .html_url}'
   ```

   Require a published, non-draft, non-prerelease release. Review compatibility-impacting notes. Its actual tag is unknown here; do not substitute a historical baseline or choose the default branch. Edge was not selected.

   ```sh
   test ! -e /agents/upstream-superpowers &&
     test ! -L /agents/upstream-superpowers

   gh repo clone obra/superpowers /agents/upstream-superpowers -- --no-checkout
   ```

   Stop on any failed prerequisite. The no-checkout clone avoids activating the default branch during setup.

3. **Verify provenance, resolve the release, and check out that candidate.**

   ```sh
   git -C /agents/upstream-superpowers rev-parse --show-toplevel
   git -C /agents/upstream-superpowers remote get-url origin
   ```

   Require the canonical root to be exactly `/agents/upstream-superpowers`, separate from Backplane. Normalize the origin and require GitHub owner/repository **exactly `obra/superpowers`**, accepting HTTPS or SSH.

   Set `sp_bp_release_tag` to the verified release tag—not a guessed value—then:

   ```sh
   git -C /agents/upstream-superpowers rev-parse --verify \
     "refs/tags/${sp_bp_release_tag}^{commit}"

   test "$(git -C /agents/upstream-superpowers rev-parse --show-toplevel)" \
     = /agents/upstream-superpowers

   git -C /agents/upstream-superpowers switch --detach \
     "refs/tags/${sp_bp_release_tag}"

   git -C /agents/upstream-superpowers rev-parse HEAD
   git -C /agents/upstream-superpowers status --short
   ```

   Require clean state after this initial checkout. Verify all four files:

   ```sh
   test -f /agents/upstream-superpowers/skills/using-superpowers/SKILL.md
   test -f /agents/upstream-superpowers/skills/brainstorming/SKILL.md
   test -f /agents/upstream-superpowers/skills/writing-plans/SKILL.md
   test -f /agents/upstream-superpowers/skills/writing-skills/SKILL.md
   ```

4. **Run compatibility preflight.**

   In a separately authorized live verification environment, use a designated real issue:

   ```sh
   gh issue view <designated-issue-or-url> --repo <owner/repo> \
     --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

   gh issue edit --help
   gh issue close --help
   ```

   Require every intake field, label addition/removal support, and closure-reason support. Version text alone does not prove compatibility. Installation performs no issue or label mutation.

   Record upstream source, release tag and resolved commit; harness and Backplane identities; `gh` version and capability results; and Backplane skill/reference hashes.

5. **Run every named conformance check without assuming a language runtime.**

   | Check | Required procedure |
   |---|---|
   | `skill-structure` | Inspect YAML delimiters, exact names, descriptions beginning `Use when`, linked references, and absence of placeholders. |
   | `native-issue-intake` | Primary prompt and rubric in `2026-08-16-native-issue-intake-green.md`. |
   | `language-neutral-verification` | Language-neutral variation in that same file. |
   | `lifecycle-transitions` | Prompt and rubric in `2026-08-16-lifecycle-transition-refactor.md`. |
   | `superpowers-installation` | Prompt and rubric in `2026-08-16-superpowers-installation-refactor.md`. |

   For behavioral checks, use fresh manually started sessions with the candidate installations, submit the exact prompts, capture responses, and score every expectation. Historical PASS results do not validate this candidate. Missing captures or unscored expectations mean **unknown compatibility**, which fails closed.

6. **Establish and verify discovery.**

   Expose upstream’s skill directory and Backplane’s canonical root `skills/` independently through the verified harness mechanism. Read the candidate’s current harness instructions first. Preserve unrelated configuration and reconcile conflicting installations.

   Do not assume `/agents/skills` is supported or invent symlink/plugin-manager commands. The scenario lacks the evidence needed to supply those commands.

   In a fresh session, verify operational discovery of upstream `using-superpowers`, `brainstorming`, `writing-plans`, and `writing-skills`, plus both Backplane skills: `managing-superpowers-backlog` and `managing-superpowers-handoffs`. Record the verified identities only after all gates pass. Here, discovery and overall compatibility remain **unknown**.

7. **Keep subsequent updates separately authorized and reversible.**

   Before a later upstream change, record the current origin, tag/commit and discovery configuration; require a clean checkout; inspect the latest stable release and report compatibility impacts; then obtain explicit authorization for that specific revision change.

   After authorization and root/provenance revalidation:

   ```sh
   git -C /agents/upstream-superpowers fetch origin --tags
   ```

   Validate the candidate before replacing the operational installation. Recheck cleanliness immediately before switching to its stable tag, then repeat preflight, all five conformance checks, and fresh-session discovery. If verification fails, restore and verify the recorded prior revision where safely possible; otherwise report unresolved compatibility.

   Never discard local work, silently switch to edge, or update upstream as a side effect of updating Backplane. No project runtime, GitHub Projects, IssueOps, bookkeeping helpers, or `.superpowers/` writes are required.