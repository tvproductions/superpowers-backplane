# Install Superpowers Backplane in Claude Code

Backplane is a companion to [upstream Superpowers](https://github.com/obra/superpowers). Install the two Claude Code plugins independently. Backplane supplies the backlog and handoff skills; upstream supplies `superpowers:using-superpowers` and the development workflow.

## Requirements

- Claude Code with native plugin support, Git, and authenticated GitHub CLI (`gh`).
- A reviewed, published 40-character Backplane commit. Use a stable release commit when one exists. Do not use moving `main` as the selected installation revision.
- An existing issue in the GitHub repository where you intend to use Backplane. Setup uses it for read-only native issue intake; it never changes that issue just to check compatibility.
- An authenticated Claude Code session for the fresh discovery check.

## Clone and inspect the reviewed Backplane revision

Run this PowerShell block from an unused parent directory. Enter the exact reviewed commit from the Backplane pull request or release. The script refuses an occupied checkout path, an unexpected GitHub origin, and an unpublished revision.

```powershell
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI authentication is required' }
$backplaneRevision = Read-Host 'Reviewed 40-character Backplane commit'
if ($backplaneRevision -cnotmatch '^[0-9a-f]{40}$') { throw 'Use a full lowercase commit SHA' }
$backplaneCheckout = Join-Path (Get-Location) 'superpowers-backplane'
if (Test-Path -LiteralPath $backplaneCheckout) { throw "Checkout path already exists: $backplaneCheckout" }
gh repo clone tvproductions/superpowers-backplane $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Backplane clone failed' }
git -C $backplaneCheckout checkout --detach $backplaneRevision
if ($LASTEXITCODE -ne 0) { throw 'Reviewed revision is not in the clone' }
$origin = git -C $backplaneCheckout remote get-url origin
if ($LASTEXITCODE -ne 0 -or -not $origin) { throw 'Backplane origin is unavailable' }
$origin = $origin.Trim()
$acceptedOrigins = @(
  'https://github.com/tvproductions/superpowers-backplane',
  'https://github.com/tvproductions/superpowers-backplane.git',
  'git@github.com:tvproductions/superpowers-backplane',
  'git@github.com:tvproductions/superpowers-backplane.git',
  'ssh://git@github.com/tvproductions/superpowers-backplane',
  'ssh://git@github.com/tvproductions/superpowers-backplane.git'
)
if ($origin -notin $acceptedOrigins) { throw "Unexpected Backplane origin: $origin" }
$resolvedRevision = git -C $backplaneCheckout rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $resolvedRevision.Trim() -ne $backplaneRevision) { throw 'Checkout is at the wrong revision' }
$publishedRevision = gh api "repos/tvproductions/superpowers-backplane/commits/$backplaneRevision" --jq .sha
if ($LASTEXITCODE -ne 0 -or $publishedRevision.Trim() -ne $backplaneRevision) { throw 'Revision is not published at the expected origin' }
$dirty = git -C $backplaneCheckout status --porcelain
if ($LASTEXITCODE -ne 0 -or $dirty) { throw 'Reviewed checkout is not clean' }
$claudeManifest = Get-Content -LiteralPath (Join-Path $backplaneCheckout '.claude-plugin/plugin.json') -Raw | ConvertFrom-Json
$marketplace = Get-Content -LiteralPath (Join-Path $backplaneCheckout '.claude-plugin/marketplace.json') -Raw | ConvertFrom-Json
if ($claudeManifest.name -ne 'superpowers-backplane' -or $marketplace.name -ne 'superpowers-backplane' -or
    $marketplace.plugins.Count -ne 1 -or $marketplace.plugins[0].name -ne 'superpowers-backplane' -or
    $marketplace.plugins[0].source -ne './' -or $marketplace.plugins[0].version -ne $claudeManifest.version) {
  throw 'Claude package identity or root source is unexpected'
}
foreach ($skill in @('managing-superpowers-backlog', 'managing-superpowers-handoffs')) {
  if (-not (Test-Path -LiteralPath (Join-Path $backplaneCheckout "skills/$skill/SKILL.md"))) {
    throw "Canonical skill is missing: $skill"
  }
}
claude plugin validate --strict $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Claude package validation failed' }
```

Inspect both Claude manifests and the two root `skills/*/SKILL.md` files in that checkout before installing. Record `$backplaneRevision` and the checkout path. The marketplace source `./` resolves to the repository root, so Claude Code uses the canonical skill folders there.

## Install the Backplane plugin

First inspect `claude plugin marketplace list` and `claude plugin list`. If Backplane is already configured, resolve its source and version before adding another copy. For a clean installation, run:

```powershell
claude plugin marketplace add $backplaneCheckout
if ($LASTEXITCODE -ne 0) { throw 'Backplane marketplace registration failed' }
claude plugin install superpowers-backplane@superpowers-backplane --scope user
if ($LASTEXITCODE -ne 0) { throw 'Backplane plugin installation failed' }
claude plugin list
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect installed plugins' }
```

A marketplace added from a local directory loads its relative-path plugin in place. Keep this checkout at the recorded revision until a separately verified update; changing its files changes the effective plugin. Installing Backplane alone does not run setup.

## Check the target issue and request setup

Provide an existing issue number in the target repository. This command checks read-only access and the complete native issue fields Backplane needs. Replace the prompts with the real repository and issue; do not use a production issue as mutation test data.

```powershell
$targetRepo = Read-Host 'Target GitHub owner/repo'
$targetIssue = Read-Host 'Existing issue number in that repository'
gh issue view $targetIssue --repo $targetRepo --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
if ($LASTEXITCODE -ne 0) { throw 'Cannot read the target issue with complete native fields' }
gh issue edit --help
gh issue close --help
```

Check that the edit help exposes label addition and removal and the close help exposes a closure reason. A displayed `gh` version alone does not establish compatibility.

Start a new Claude Code session. Tell Claude the target repository and existing issue number, then send this exact request:

> Set up Superpowers Backplane in this Claude Code session.

The setup agent follows the [Backplane installation and compatibility reference](../skills/managing-superpowers-backlog/references/installing-superpowers.md). It must find exactly one effective Backplane plugin and both canonical skills, then adopt a separate operational upstream Superpowers plugin with an authoritative source and observable version or revision. If upstream is absent, use [upstream Superpowers' current Claude Code installation channel](https://github.com/obra/superpowers#claude-code) and its compatible stable release. Do not replace or update an existing upstream installation as a side effect.

The response must identify the Backplane plugin and revision, independent upstream package and source/version or commit, authenticated `gh` with complete read-only intake of the target issue and label/closure capabilities, and the three skill identities. If any result cannot be established, report `UNKNOWN` with the failed check and a recovery action. Setup must not change GitHub issue state.

Start another fresh Claude Code session. In `/help`, inspect Custom commands for `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. Invoke each with a harmless read-only request and verify that the two packages remain separate. Package installation or a model's unverified statement alone is not discovery evidence.

## Later lifecycle work

Pinned update, rollback, and Backplane-only uninstall instructions are pending verification in [issue #19](https://github.com/tvproductions/superpowers-backplane/issues/19). Follow upstream Superpowers' own installation and update channel for upstream changes; Backplane does not manage that package.
