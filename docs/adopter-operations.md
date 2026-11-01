# Adopter operations

Backplane is a companion to independently installed
[Superpowers](https://github.com/obra/superpowers). It is distributed under the
[MIT license](../LICENSE). Git and authenticated GitHub CLI (`gh`) are required,
along with a compatible host and operational upstream Superpowers. It imposes
no runtime, build tool or test runner on a consuming project. The OpenCode
adapter runs in its host's JavaScript runtime.

GitHub Projects are optional presentation. Native issues, hierarchy,
dependencies, closure reasons and Backplane lifecycle labels remain authoritative.
IssueOps is not required or used. Read-only setup, status and selection must
leave GitHub issue state unchanged.

## Select a verified surface

| Host | Available guidance and evidence | Limits |
| --- | --- | --- |
| Codex | [Installation, setup, pinned change/restoration and removal](installing-codex.md); [native acceptance](../tests/scenarios/2026-09-19-codex-installation.md) | Historical Windows evidence, with the exact CLI and source revisions recorded there; replay for changed inputs |
| Claude Code | [Installation, setup, troubleshooting, update, rollback and removal](installing-claude-code.md); [integrated acceptance](../tests/scenarios/2026-10-26-issue-11-satisfaction.md) | Accepted on Claude Code 2.1.311, with separately recorded upstream inputs and immutable Backplane delivery; other versions/platforms need their own evidence |
| OpenCode V1/V2 | [Pinned initial installation and skill loading](installing-opencode.md); [initial-smoke acceptance](../tests/scenarios/2026-11-01-issue-20-satisfaction.md) | Initial native smokes used V1 1.18.31 and V2 2.1.4. Full setup/failure coverage belongs to #21/#23; lifecycle to #22/#24; final acceptance to #12 |

Other harnesses are outside the approved v0.1 contract. OpenCode update,
rollback and uninstall are pending verification; do not extrapolate them from
an initial package load. The contract floors V1 1.18.29 and V2 2.0.4 do not
mean that every later host release has been tested. This is development source;
manifest version `0.1.0` alone does not establish a published release.

## First installation and setup

1. Choose the host guide above. Inspect a reviewed, published full Backplane
   commit at the expected `tvproductions/superpowers-backplane` origin. Use a
   stable release revision when one is available; record the full resolved SHA.
2. Follow that guide's native installation commands. Preserve unrelated plugins
   and record the package ID, source, installed revision and profile. Do not
   create a second effective installation to repair an existing one.
3. Request setup as directed by the guide. The agent follows the canonical
   [installation preflight](../skills/managing-superpowers-backlog/references/installing-superpowers.md).
   Existing compatible upstream is adopted in place. If upstream is absent,
   obtain it only through the active host's current documented stable channel
   in the authorized profile. Do not change an existing upstream installation
   as a side effect.
4. In a fresh session, directly load upstream `using-superpowers` and both
   Backplane skills. Record their separate installation roots, host version,
   upstream source/version or revision, Backplane revision and `gh` capability
   checks. Package installation alone is not completed setup. OpenCode's
   initial discovery smoke remains distinct from full setup acceptance.

The linked guides own executable commands and input prompts. Run their blocks
in order, with the recorded revision/profile substitutions and immediate
verification between blocks. The Claude lifecycle Python blocks share one
session; running each in a separate process loses their state. The repository's
own uv/Python policy applies to its verification tooling, not to adopters.

## Update and rollback

Use the host guide's tested native path. Before changing anything, record the
prior source SHA, installed package inventory, upstream identity and user-file
preservation baseline. Inspect the candidate and check compatibility before
replacement. Preserve a retrievable prior source for rollback.

Codex's documented marketplace ref replacement temporarily affects every plugin
from that marketplace. Inventory those plugin IDs and verify their restoration;
do not remove a shared marketplace as an incidental uninstall step. Claude's
local-directory marketplace loads files in place; editing that checkout does
not prove a hosted package update. Its hosted lifecycle recipe pins the plugin
source SHA separately from the dedicated catalog location.

After update or rollback, verify the exact installed revision and relevant
package files, repeat compatibility checks and perform fresh three-skill loads.
A successful manager exit alone is insufficient. If a candidate fails, inspect
and record the failure state before restoring the recorded prior revision;
verify the restoration rather than assuming it worked. If restoration cannot
be established, report UNKNOWN and the precise remaining check.

## Removal and recovery

Follow Backplane-only removal in the applicable guide. Preserve independent
Superpowers, unrelated plugins and marketplace entries, user-authored files,
repository history and GitHub issues. In a fresh session verify that Backplane
is absent while upstream remains available. Upstream update/removal follows
its own separately authorized channel and compatibility process.

| Failed check | Recovery |
| --- | --- |
| Unknown source or unobservable version/revision | Establish authoritative provenance and observable identity before retrying |
| Duplicate Backplane installations or occupied destination | Inventory the exact sources/paths; reconcile ownership before replacement |
| Dirty authoritative checkout | Preserve changes; adoption without updating may be possible, but do not reset or overwrite it |
| Missing `gh` auth, intake fields, label flags or closure reasons | Repair the specific capability, then repeat preflight without mutating a test issue |
| Host/model authentication unavailable | Authenticate the selected isolated profile through its native flow; never copy credentials or fall back to a normal profile |
| Incompatible host/upstream or missing skill | Use the supported host/channel and repeat fresh-session checks; retain UNKNOWN until observed |
| Failed candidate or incomplete restoration | Preserve failure evidence, restore the recorded prior source through the guide, then verify identity and discovery |

## Authorization and support claims

Inspect package sources and command effects before installing or changing a
profile. Agent permission prompts and host confirmations still apply. Scope
configuration to the intended child process/profile; a changed working directory
alone does not isolate host caches or settings. Never print or copy credentials.

Explicitly starting a work item authorizes its evidence-gated lifecycle workflow;
status or selection alone does not. Re-read current issue scope and revision
before a mutation, preserve unrelated labels, and require integrated acceptance
before completed closure. Project rules control publication, integration,
release and other separate authorization gates. The
[issue contract](../skills/managing-superpowers-backlog/references/github-issue-contract.md)
defines the precise lifecycle conditions.

Historical acceptance retains its original inputs. Changed guide commands,
packages, host versions or upstream inputs require affected checks to be rerun.
See the [#4 execution evidence](../tests/scenarios/2026-11-01-issue-4-license-and-operations.md)
for current replay and hosted-license gaps; this document does not certify
unperformed operations or complete the pending host issues.
