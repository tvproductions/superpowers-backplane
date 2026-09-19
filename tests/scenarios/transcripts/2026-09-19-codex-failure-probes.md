# Codex Failure Probe Evidence

**Work item:** issue #3. **Status:** in progress; CLI and checkout facts below are observed, while setup-agent decisions still require fresh authenticated sessions.

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
