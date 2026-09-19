# Install Superpowers Backplane in Codex

Backplane is a companion to [upstream Superpowers](https://github.com/obra/superpowers). Install the two plugins independently. Backplane supplies the backlog and handoff skills; upstream supplies `superpowers:using-superpowers` and its development workflow.

## Requirements

- Codex with plugin marketplace support, Git, and authenticated GitHub CLI (`gh`).
- A reviewed checkout of `tvproductions/superpowers-backplane` at a published commit. Use a stable release revision when one exists. A moving `main` branch is not the default install source.
- An issue in the GitHub repository where you intend to use Backplane, so setup can check the complete native issue fields and `gh` lifecycle commands.

## Install the Backplane package

Run these PowerShell commands **from the reviewed Backplane checkout**. Inspect its `plugin.json`, `.agents/plugins/marketplace.json`, and both root `skills/*/SKILL.md` files before installing. The origin and remote commit checks prevent a consuming project's `HEAD` or an unpublished local commit from becoming the marketplace ref.

```powershell
gh auth status
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI authentication is required' }
$backplaneRoot = git rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0 -or -not $backplaneRoot) { throw 'Run this from the Backplane checkout' }
$backplaneRoot = $backplaneRoot.Trim()
$origin = git -C $backplaneRoot remote get-url origin
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
$backplaneRevision = git -C $backplaneRoot rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or -not $backplaneRevision) { throw 'Backplane commit is unavailable' }
$backplaneRevision = $backplaneRevision.Trim()
$publishedRevision = gh api "repos/tvproductions/superpowers-backplane/commits/$backplaneRevision" --jq .sha
if ($LASTEXITCODE -ne 0 -or $publishedRevision -ne $backplaneRevision) { throw 'Backplane commit is not published at the expected origin' }
$installed = codex plugin list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect existing plugins' }
if (@($installed.installed | Where-Object { $_.pluginId -like 'superpowers-backplane@*' }).Count -gt 0) { throw 'Backplane is already installed; inspect it before changing versions' }
$registered = codex plugin marketplace list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect existing marketplaces' }
if (@($registered.marketplaces | Where-Object name -eq 'superpowers-backplane').Count -gt 0) { throw 'Backplane marketplace is already configured; inspect it before changing refs' }
codex plugin marketplace add tvproductions/superpowers-backplane --ref $backplaneRevision
if ($LASTEXITCODE -ne 0) { throw 'Backplane marketplace registration failed' }
codex plugin add superpowers-backplane@superpowers-backplane
if ($LASTEXITCODE -ne 0) { throw 'Backplane plugin installation failed' }
codex plugin list --json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect installed plugins' }
```

Record `$backplaneRevision` for a later rollback. If Backplane is already installed or a marketplace with that name is configured, inspect its source and version before changing it; do not add a conflicting second installation. Package installation alone does not run setup.

## Request setup in a new Codex session

Ask Codex: `Set up Superpowers Backplane in this Codex session.` The setup agent follows the [Backplane installation and compatibility reference](../skills/managing-superpowers-backlog/references/installing-superpowers.md) before any backlog operation.

Setup checks exactly one effective Backplane plugin and both canonical Backplane skills. It finds an operational, independent Superpowers installation, verifies its authoritative source and observable version or revision, and adopts it in place. A compatible sibling Git checkout is also valid. If upstream is absent, follow [Superpowers' current Codex installation instructions](https://github.com/obra/superpowers#installation) and select the latest compatible stable release through that channel. Do not update or replace an existing upstream installation as a side effect. A later upstream update follows `SUPERPOWERS.md` and requires its own preflight and authorization.

Setup also runs `gh auth status`, verifies the complete native issue intake fields on a real issue in the target repository, and checks that `gh issue edit --help` supports label add/remove and `gh issue close --help` supports closure reasons. A displayed CLI version alone does not prove compatibility.

Start another fresh Codex session and confirm discovery of `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs` from the two separate installations. The setup response should report the Backplane package ID and revision, upstream package source and version or checkout origin and commit, `gh` capability result, and the three discovered skill identities. If any source, version, capability, or fresh-session result cannot be proved, report `UNKNOWN` with the failed check and recovery action; do not report adoption complete or change any GitHub issue state.

## Change or restore a pinned Backplane revision

Use a reviewed, published Backplane commit for each revision. Record the installed revision and the complete list of plugins from the Backplane marketplace before changing it. Codex CLI 0.155.1 requires removing and re-adding a Git marketplace to change its `--ref`; that temporarily makes every plugin from that marketplace unavailable. Keep the prior revision available for restoration. Do not use this procedure for an unknown or local marketplace source.

Run the following in PowerShell after replacing the two SHA placeholders with the reviewed prior and candidate commits. This preflight checks the current Git checkout, marketplace source, existing plugin IDs, and candidate availability before changing Codex state:

```powershell
$priorRevision = '<recorded-prior-40-character-commit-sha>'
$candidateRevision = '<reviewed-candidate-40-character-commit-sha>'
if ($priorRevision -notmatch '^[0-9a-f]{40}$' -or $candidateRevision -notmatch '^[0-9a-f]{40}$') { throw 'Use full reviewed commit SHAs' }
$marketplaces = codex plugin marketplace list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect marketplaces' }
$market = @($marketplaces.marketplaces | Where-Object name -eq 'superpowers-backplane')
if ($market.Count -ne 1) { throw 'Expected one Backplane marketplace' }
if ($market[0].marketplaceSource.sourceType -ne 'git' -or
    $market[0].marketplaceSource.source -ne 'https://github.com/tvproductions/superpowers-backplane.git') {
  throw 'Unexpected Backplane marketplace source'
}
$resolvedPrior = (git -C $market[0].root rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $resolvedPrior -ne $priorRevision) { throw 'Recorded prior revision does not match the installed marketplace' }
$before = codex plugin list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect installed plugins' }
$backplanePlugins = @($before.installed | Where-Object { $_.pluginId -like 'superpowers-backplane@*' })
if ($backplanePlugins.Count -ne 1 -or $backplanePlugins[0].pluginId -ne 'superpowers-backplane@superpowers-backplane') { throw 'Resolve alternate, duplicate, or absent Backplane installations first' }
$beforeIds = @($before.installed | Where-Object marketplaceName -eq 'superpowers-backplane' | ForEach-Object pluginId | Sort-Object)
$publishedCandidate = gh api "repos/tvproductions/superpowers-backplane/commits/$candidateRevision" --jq .sha
if ($LASTEXITCODE -ne 0 -or $publishedCandidate -ne $candidateRevision) { throw 'Candidate revision is not published at the expected origin' }
```

After inspecting the candidate package and its compatibility, change only the Backplane marketplace and reinstall its selected plugin:

```powershell
codex plugin marketplace remove superpowers-backplane
if ($LASTEXITCODE -ne 0) { throw 'Could not remove the prior Backplane marketplace' }
codex plugin marketplace add tvproductions/superpowers-backplane --ref $candidateRevision
if ($LASTEXITCODE -ne 0) { throw 'Candidate registration failed; restore the prior revision below' }
codex plugin add superpowers-backplane@superpowers-backplane
if ($LASTEXITCODE -ne 0) { throw 'Candidate installation failed; restore the prior revision below' }
$marketplaces = codex plugin marketplace list --json | ConvertFrom-Json
$market = @($marketplaces.marketplaces | Where-Object name -eq 'superpowers-backplane')
if ($LASTEXITCODE -ne 0 -or $market.Count -ne 1) { throw 'Candidate marketplace is missing' }
$resolvedCandidate = (git -C $market[0].root rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $resolvedCandidate -ne $candidateRevision) { throw 'Candidate checkout is at the wrong commit' }
$after = codex plugin list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect candidate plugins' }
$afterIds = @($after.installed | Where-Object marketplaceName -eq 'superpowers-backplane' | ForEach-Object pluginId | Sort-Object)
if (@($after.installed | Where-Object { $_.pluginId -like 'superpowers-backplane@*' }).Count -ne 1) { throw 'Candidate left a duplicate or absent Backplane installation' }
if (@(Compare-Object $beforeIds $afterIds).Count -ne 0) { throw 'A plugin from the marketplace was lost or added unexpectedly' }
```

Start a **new Codex session** and verify discovery of `superpowers:using-superpowers`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers-backplane:managing-superpowers-handoffs`. Run the setup compatibility preflight again and compare the package files with the reviewed candidate. If any check fails, restore the prior revision with the recorded SHA:

```powershell
$priorRevision = '<recorded-prior-40-character-commit-sha>'
if ($priorRevision -notmatch '^[0-9a-f]{40}$') { throw 'Use the full recorded prior commit SHA' }
$marketplaces = codex plugin marketplace list --json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect marketplaces before restoration' }
if (@($marketplaces.marketplaces | Where-Object name -eq 'superpowers-backplane').Count -gt 0) {
  codex plugin marketplace remove superpowers-backplane
  if ($LASTEXITCODE -ne 0) { throw 'Could not remove the candidate marketplace' }
}
codex plugin marketplace add tvproductions/superpowers-backplane --ref $priorRevision
if ($LASTEXITCODE -ne 0) { throw 'Could not restore the prior marketplace' }
codex plugin add superpowers-backplane@superpowers-backplane
if ($LASTEXITCODE -ne 0) { throw 'Could not restore the prior plugin' }
$marketplaces = codex plugin marketplace list --json | ConvertFrom-Json
$market = @($marketplaces.marketplaces | Where-Object name -eq 'superpowers-backplane')
if ($LASTEXITCODE -ne 0 -or $market.Count -ne 1) { throw 'Restored marketplace is missing' }
$resolvedPrior = (git -C $market[0].root rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $resolvedPrior -ne $priorRevision) { throw 'Restored checkout is at the wrong commit' }
codex plugin list --json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect restored plugins' }
```

Check the recorded plugin IDs again and repeat the three-skill fresh-session check after restoration. An upstream Superpowers update remains a separate operation.

To remove only Backplane while preserving its marketplace and unrelated installations:

```powershell
codex plugin remove superpowers-backplane@superpowers-backplane
if ($LASTEXITCODE -ne 0) { throw 'Backplane removal failed' }
codex plugin list --json
if ($LASTEXITCODE -ne 0) { throw 'Could not inspect installed plugins after removal' }
```
