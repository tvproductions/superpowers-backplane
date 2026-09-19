# Codex Failure Probe Evidence

**Work item:** issue #3. **Status:** in progress; CLI and checkout facts below are observed. Fresh repository-skill hypothetical responses pass after the recorded correction; authenticated native plugin setup remains UNKNOWN.

| Failure input | Observed probe | Expected setup response | Status |
|---|---|---|---|
| Duplicate Backplane plugin | A disposable state installed `superpowers-backplane@superpowers-backplane` and `superpowers-backplane@backplane-duplicate`; `plugin list --json` reported two effective Backplane IDs. | Report conflict and require reconciliation before setup or issue mutation. | Host fact PASS; agent response UNKNOWN |
| Dirty authoritative sibling checkout | A disposable copy retained exact `https://github.com/obra/superpowers.git` origin and commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`; `git status --short` reported only `?? backplane-dirty-probe.txt`. Original upstream stayed clean. | Adoption in place may proceed after required skill checks; an upstream update must refuse the dirty tree. | Host fact PASS; agent response UNKNOWN |
| Lookalike checkout origin | A separate checkout copy retained all four required skills but resolved `origin` to `https://github.com/obra/superpowers-lookalike.git`. | Reject unknown provenance and leave the checkout untouched. | Host fact PASS; agent response UNKNOWN |
| Path collision | The candidate destination `<fixture root>/project` already existed before any managed clone. | Stop before cloning or overwriting it. | Host fact PASS; agent response UNKNOWN |
| Unknown or versionless native upstream | No authoritative versionless native package was available without altering upstream package provenance. | Report compatibility `UNKNOWN` and preserve existing installations. | UNKNOWN |
| Missing `gh` native fields or lifecycle flags | Actual `gh` returned all 15 required issue fields, label add/remove flags, and closure-reason flag. A deficient CLI has not been introduced into a fresh session. | Report compatibility `UNKNOWN` without issue mutation. | UNKNOWN |

Fixture changes were confined to OS-temp directories. Issue #3 remained open at `backplane:active` with `updatedAt=2026-09-19T19:37:32Z` after these probes. No test issue was created or changed.

## Guide quality regression: alternate Backplane selector

- RED: In disposable `sw`, the official Git marketplace was pinned at `8bfba888599568cc8f729ba6f0c030ace8e6377f`, but its plugin was not installed. A separate local marketplace installed the sole effective ID `superpowers-backplane@backplane-duplicate`. The first written update preflight counted one `superpowers-backplane@*` and incorrectly accepted it; proceeding would have added a second effective Backplane installation.
- GREEN: The guide now requires the sole installed Backplane ID to equal `superpowers-backplane@superpowers-backplane` before any marketplace mutation. The same disposable input fails with `Resolve alternate, duplicate, or absent Backplane installations first`; no plugin or issue was changed by the preflight.
- The guide replaced example feature-branch SHAs with explicit 40-character SHA placeholders so a reader must supply reviewed revisions. A positive replay substituted the two published test SHAs only inside a disposable shell and reran all four guide blocks with upstream and sentinel installed. It passed, restored the first marketplace SHA, and left the two unrelated plugin IDs installed.

## Fresh read-only setup behavior — RED

The same session assessed six independent hypothetical failure inputs using repository skills. A, B, D, E, and F gave the expected refusal and recovery. C refused the update but did not state that a dirty authoritative checkout may be adopted in place after compatibility checks. Score C: FAIL. These responses do not prove isolated native plugin discovery.

### Exact prompt

```text
Use managing-superpowers-backlog and every required reference. This is a read-only hypothetical installation assessment; do not inspect or mutate any actual checkout, Codex profile, or GitHub issue. Evaluate each independent case separately. In each case, state the failed check, whether setup may report compatibility, exact recovery, what remains unchanged, and whether any issue mutation is allowed.

A. Two effective Backplane IDs are installed: superpowers-backplane@superpowers-backplane and superpowers-backplane@backplane-duplicate.
B. A native Superpowers package comes from the official documented catalog, but the host exposes neither an installed version nor a resolved revision.
C. A sibling checkout is the exact obra/superpowers origin with all required skills and a known commit, but git status --short shows ?? user-note.txt. Its owner asks to adopt it now and update it to the latest stable release in the same step.
D. A sibling checkout has all required skills but origin https://github.com/obra/superpowers-lookalike.git.
E. A managed-install destination already exists and contains unrelated files.
F. gh issue view on a real issue lacks blockedBy, and gh issue edit --help lacks --remove-label.

In every case an unrelated sentinel plugin, existing upstream files, and a user note have recorded hashes. Preserve those exact bytes. Do not assume any programming-language runtime.```

### Exact RED final response

````text
This assessment uses the installation contract and native GitHub issue contract. Each case fails closed independently. No issue mutation is allowed in any case because setup and compatibility checks never authorize backlog changes.

### A. Duplicate effective Backplane installations

- **Failed check:** Setup requires exactly one effective Backplane installation. Both `superpowers-backplane@superpowers-backplane` and `superpowers-backplane@backplane-duplicate` are effective, so the identity check fails.
- **Compatibility report:** **No.** Setup must report a conflicting duplicate installation, not compatibility.
- **Recovery:** Inspect both package sources and resolved versions. Using the host’s supported plugin manager, remove or disable the duplicate so the sole effective ID is `superpowers-backplane@superpowers-backplane`. Then rerun the complete setup preflight and verify the three required skills in a fresh session.
- **Unchanged:** The canonical Backplane installation is not updated or reinstalled during reconciliation. The sentinel plugin, upstream files, and user note retain their recorded hashes and exact bytes.
- **Issue mutation:** **None allowed.**

### B. Official native package without observable version or revision

- **Failed check:** Native mode requires an observable installed version or resolved tag or commit. Official catalog provenance alone is insufficient when both are unavailable.
- **Compatibility report:** Setup may report **UNKNOWN compatibility**, but may not report the package compatible or adoption complete.
- **Recovery:** Obtain authoritative version or resolved revision evidence from the host’s package manager or catalog metadata. If the host cannot expose it, use the host’s documented path to select an observable, versioned stable package; changing the existing upstream installation requires separate authorization and a recorded rollback point. Then run the complete compatibility preflight and fresh-session skill discovery.
- **Unchanged:** Until that authorized recovery occurs, the native package and all existing upstream content remain untouched. The sentinel plugin, upstream files, and user note retain their exact bytes and hashes.
- **Issue mutation:** **None allowed.**

### C. Authoritative but dirty sibling checkout, with an update requested

- **Failed check:** The authoritative origin, required skills, and known commit pass, but `git status --short` is not empty. `?? user-note.txt` makes the checkout dirty and blocks the proposed update.
- **Compatibility report:** **No for the combined adoption-and-update operation.** Setup must report the dirty-checkout failure and cannot report adoption complete after an update that did not safely occur.
- **Recovery:**
  1. Do not touch `user-note.txt`.
  2. Have the checkout owner preserve it outside the checkout, commit it where appropriate, or otherwise resolve it through an owner-chosen Git workflow.
  3. Require `git status --short` to become empty.
  4. Record the current origin and commit.
  5. Inspect the latest stable release and its compatibility notes.
  6. Report the exact candidate release and obtain explicit authorization for that revision change.
  7. Fetch tags and check out the stable release without discarding local work.
  8. Run the full preflight, five named conformance checks, and fresh-session discovery.

  The owner’s general request to “update to latest stable” does not replace the required candidate-specific report and authorization.
- **Unchanged:** During this failed attempt, the checkout commit, upstream files, and `user-note.txt` remain byte-for-byte unchanged. The sentinel plugin and all recorded hashes also remain unchanged.
- **Issue mutation:** **None allowed.**

### D. Lookalike sibling origin

- **Failed check:** Checkout mode requires the normalized GitHub owner and repository to be exactly `obra/superpowers`. `obra/superpowers-lookalike` fails provenance.
- **Compatibility report:** **No.** Required skills do not compensate for the incorrect origin.
- **Recovery:** Reject the checkout without editing, relocating, or deleting it. Adopt a separately verified official native package, or—if checkout mode is required—clone `obra/superpowers` into a genuinely unused destination, select the latest compatible stable release, and run the full compatibility and discovery checks.
- **Unchanged:** The lookalike checkout remains intact. The sentinel plugin, all existing upstream files, and the user note retain their exact bytes and hashes.
- **Issue mutation:** **None allowed.**

### E. Managed-install destination contains unrelated files

- **Failed check:** Managed checkout mode requires an unused destination. An existing directory containing unrelated files is a path collision.
- **Compatibility report:** **No.** Setup cannot claim compatibility because no safe managed installation has been established.
- **Recovery:** Select a different, verified-unused destination and clone the authoritative repository there with `gh repo clone obra/superpowers <new-destination>`. Select the latest compatible stable release, verify origin, revision, required skills, `gh` capabilities, all five conformance checks, and fresh-session discovery.
- **Unchanged:** Do not merge into, empty, rename, or overwrite the occupied destination. Its unrelated files, the sentinel plugin, existing upstream files, and the user note retain their exact bytes and hashes.
- **Issue mutation:** **None allowed.**

### F. Missing `gh` intake and label-removal capabilities

- **Failed checks:**
  - `gh issue view` does not provide the required `blockedBy` field.
  - `gh issue edit --help` does not expose label removal.
- **Compatibility report:** **No.** Either missing capability is independently incompatible regardless of the displayed `gh` version.
- **Recovery:** Upgrade or replace `gh` through its supported installation channel with a release that exposes the complete required intake fields, label addition and removal, and closure reasons. Authenticate it for the repository in scope, then rerun:
  - the complete real-issue intake query,
  - `gh issue edit --help`,
  - `gh issue close --help`,
  - the named conformance checks,
  - fresh-session skill discovery.
- **Unchanged:** Do not attempt a partial lifecycle transition. All issue labels, issue fields, sentinel plugin data, upstream files, and the user note remain exactly unchanged, with their recorded hashes preserved.
- **Issue mutation:** **None allowed**, including attempts to work around missing label removal with multiple commands.
````

## Fresh read-only setup behavior — GREEN

The installation reference now separates adoption from revision change. The exact same prompt in a fresh session passed all six behavioral cases. Case C explicitly allows conditional adoption of the current authoritative commit while refusing the dirty-tree update. No actual isolated profile setup was run by this hypothetical check.

### Exact GREEN final response

````text
This is a contract assessment only. No checkout, profile, installation, or GitHub issue state was queried or changed. Compatibility requires every preflight and conformance check to pass; installation operations never authorize issue mutation.

### A. Duplicate effective Backplane installations

- **Failed check:** Setup requires exactly one effective Backplane installation. Both `superpowers-backplane@superpowers-backplane` and `superpowers-backplane@backplane-duplicate` match the effective Backplane identity.
- **May setup report compatibility?** **No.** It must report the duplicate installation and fail closed.
- **Exact recovery:** Determine which installation has the reviewed source and revision. Remove or disable the duplicate through Codex’s plugin manager. Then verify:
  1. exactly `superpowers-backplane@superpowers-backplane` remains;
  2. both canonical Backplane skills are visible;
  3. all compatibility checks pass;
  4. a fresh session discovers the three required skills.
- **Unchanged:** The sentinel plugin, upstream Superpowers installation and files, user note, unrelated plugin entries, and all their recorded hashes remain byte-for-byte unchanged.
- **Issue mutation allowed?** **No.**

### B. Official native package without observable version or revision

- **Failed check:** Native package provenance is authoritative, but neither an installed version nor a resolved tag or commit is observable.
- **May setup report compatibility?** **No.** It must report compatibility as **UNKNOWN**, even if the required skills appear operational.
- **Exact recovery:** Use the host’s documented package manager or official catalog to obtain an installation whose version or resolved revision can be recorded. If necessary, reinstall a reviewed stable package from that same official channel with an observable version or immutable revision. Then rerun provenance, fresh-session discovery, `gh` capability checks, and all five conformance checks.
- **Unchanged:** Until that separately authorized package operation occurs, the existing native package, sentinel plugin, upstream files, user note, and recorded hashes remain unchanged.
- **Issue mutation allowed?** **No.**

### C. Authoritative but dirty sibling, with adoption and update requested together

- **Failed check:** `git status --short` is not empty because it reports `?? user-note.txt`. This blocks an upstream revision change.
- **May setup report compatibility?** **Yes, for adoption of the current commit only**, provided provenance, required skills, current-revision compatibility, discovery, `gh`, and conformance checks all pass. It may not report the requested update as compatible, completed, or attempted.
- **Exact recovery:**
  1. Adopt the existing checkout in place at its current known commit.
  2. Refuse and separate the update.
  3. Ask the checkout owner to resolve `user-note.txt` by committing it, moving it outside the checkout, or deliberately removing it.
  4. Confirm `git status --short` is empty.
  5. Inspect the latest stable release and release notes.
  6. Record the current commit and obtain explicit authorization for the specific revision change.
  7. Update without discarding local work, then rerun the full compatibility preflight and five conformance checks.
- **Unchanged:** During this assessment and refused update, `user-note.txt`, every existing upstream file, the sentinel plugin, and every recorded hash remain exactly unchanged. The checkout stays at its current commit.
- **Issue mutation allowed?** **No.**

### D. Lookalike sibling origin

- **Failed check:** The normalized origin owner and repository are not exactly `obra/superpowers`; `obra/superpowers-lookalike` fails authoritative provenance.
- **May setup report compatibility?** **No.** Required skill names or matching files cannot cure failed provenance.
- **Exact recovery:** Do not adopt, update, rewrite, or relocate the lookalike. Install Superpowers through the active harness’s upstream-documented stable native channel, or create a separate sibling checkout whose normalized origin is exactly `obra/superpowers`. Verify its revision, required skills, clean state where an update is involved, fresh-session discovery, and the complete compatibility suite.
- **Unchanged:** The lookalike checkout and all its files, the sentinel plugin, existing authoritative upstream files elsewhere, the user note, and all recorded hashes remain unchanged.
- **Issue mutation allowed?** **No.**

### E. Occupied managed-install destination

- **Failed check:** Managed checkout mode requires an unused destination. A destination containing unrelated files is a path collision.
- **May setup report compatibility?** **No.** Setup cannot claim managed installation or adoption complete.
- **Exact recovery:** Leave the occupied directory untouched and select a new unused destination for the authoritative `obra/superpowers` checkout. Alternatively, its owner may independently relocate the unrelated files; setup must then revalidate that the destination is unused before cloning. After installation, verify provenance, revision, skills, discovery, `gh` capabilities, and conformance.
- **Unchanged:** Every unrelated destination file, the sentinel plugin, existing upstream files, the user note, and their recorded hashes remain byte-for-byte unchanged.
- **Issue mutation allowed?** **No.**

### F. Missing required `gh` capabilities

- **Failed checks:**
  1. Real-issue intake does not return required field `blockedBy`.
  2. `gh issue edit --help` does not expose label removal through `--remove-label`.
- **May setup report compatibility?** **No.** The `gh` capability surface is incompatible regardless of its displayed version.
- **Exact recovery:** Install or select a supported GitHub CLI build/environment that exposes the complete required issue JSON fields and both label addition and removal. Reauthenticate if needed, then rerun:
  1. complete intake against a real issue;
  2. `gh issue edit --help`;
  3. `gh issue close --help` for closure reasons;
  4. all five conformance checks;
  5. fresh-session skill discovery.
- **Unchanged:** The sentinel plugin, upstream files, user note, issue labels/body/state, and all recorded hashes remain unchanged.
- **Issue mutation allowed?** **No.** Missing blocker intake prevents eligibility assessment, and missing label removal prevents the required atomic lifecycle-label transition.

These conclusions follow the [installation contract](C:/Users/Jeff/source/repos/agents/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md), [native issue contract](C:/Users/Jeff/source/repos/agents/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md), and [approved v0.1 adoption specification](C:/Users/Jeff/source/repos/agents/superpowers-backplane/docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md).
````
