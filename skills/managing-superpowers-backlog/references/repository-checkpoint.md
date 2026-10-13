# Capture, accept, and recover a repository checkpoint

Use for `capture checkpoint`. Read [governance](../../../docs/superpowers-backplane/governance.md),
[format and examples](checkpoint-format.md), [readable rendering](checkpoint-state-template.md),
and the native issue contract. The outputs are `.sp-bp/state.md` and
`.sp-bp/github-state.json`. They record dated product/coverage/evidence state;
an execution scratch ledger or session handoff is not this product checkpoint.
Git, authenticated gh, operational Superpowers, and the host's available native
JSON/file capabilities suffice. No language, helper engine, or extra skill
bundle is prescribed. Follow the project's exact root/worktree and namespace rules.

## Establish capture scope and sources

Record actual repository and selected issue/graph scope, excluded/external
boundaries, Project identity and declared `integrated` or explicitly selected
`issues-only` mode, immutable source commit, relevant approved design/plan and
approval revisions, current issue-owned dispositions/coverage/evaluation pointers,
accepted evidence, and observation start. Establish operation authority before
writes; read-only/simulated requests only assess supplied records.

Use complete native issue intake for each selected issue:

```sh
gh issue view "$sp_bp_issue_number" --repo "$sp_bp_repo" \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url,assignees,milestone
```

Expand selected native parent/child and dependency endpoints through a visited-ID
set, retaining declared external/excluded boundaries. Reuse current issue identities;
never infer an edge from body prose or a code. Retrieve every required connection
page; a CLI array or process exit alone does not prove completeness. Compare totals
where exposed and preserve continuation/terminal evidence. A missing/null connection,
GraphQL errors, inaccessible source, or failed query is partial rather than an empty
successful collection.

Native REST pagination can be retained as page arrays:

```sh
gh api --paginate --slurp "repos/$sp_bp_repo/issues/$sp_bp_issue_number/sub_issues?per_page=100"
gh api --paginate --slurp "repos/$sp_bp_repo/issues/$sp_bp_issue_number/dependencies/blocked_by?per_page=100"
gh api --paginate --slurp "repos/$sp_bp_repo/issues/$sp_bp_issue_number/dependencies/blocking?per_page=100"
```

These are read-only [native hierarchy](https://docs.github.com/en/rest/issues/sub-issues)
and [dependency](https://docs.github.com/en/rest/issues/issue-dependencies) endpoints.
Retain returned page membership and the CLI's completed pagination observation;
when terminal/totals are unproven, report incomplete. Required-field/schema/permission
failures never authorize a fallback to Markdown-derived relationships.

For explicit GraphQL pageInfo, paginate one connection at a time. For example:

```sh
gh api graphql --paginate --slurp \
  -F owner="$sp_bp_owner" -F name="$sp_bp_name" -F number="$sp_bp_issue_number" \
  -f query='query($owner:String!,$name:String!,$number:Int!,$endCursor:String){
    repository(owner:$owner,name:$name){issue(number:$number){
      subIssues(first:100,after:$endCursor){totalCount
        pageInfo{hasNextPage endCursor} nodes{id number url updatedAt}}
    }}
  }'
```

The same inspected Issue connection interface supports `blockedBy`, `blocking`,
and `closedByPullRequestsReferences`; the latter uses PullRequest nodes and
`includeClosedPrs:true` when the required capture includes closed references.
Use separate connection queries, retaining all pages and source identities.
Labels/assignees and native closing PR references also need complete enumeration
when the supplied CLI values do not establish it. Fetch each selected PR's actual
state/review/target/merge/native closing references under the closeout contract.
A PR's native `closingIssuesReferences` is a separately observed connection.
Retain its complete pages and membership under that collection name and the PR
identity; denied membership is `closing_issue_ids: null` with partial metadata,
a field-specific limitation and unavailable graph recheck. Observed empty
membership is [] with an empty terminal page. Do not infer reciprocal membership
from issue-side references. A reference and actual native closed state remain distinct.

For integrated mode, inspect native Project identities, relevant field definitions,
issue-backed items and relevant values. These gh commands have bounded defaults:

```sh
gh project view "$sp_bp_project_number" --owner "$sp_bp_project_owner" --format json
gh project field-list "$sp_bp_project_number" --owner "$sp_bp_project_owner" --format json --limit "$sp_bp_field_limit"
gh project item-list "$sp_bp_project_number" --owner "$sp_bp_project_owner" --format json --limit "$sp_bp_item_limit"
```

Declare the relevant field/item scope; increasing a limit is not proof of full
capture. Verify all pages/totals, or use `gh api graphql --paginate` with native
ProjectV2 `fields`/`items` connections and `$endCursor`. Nested item field-value
connections need their own terminal/totals checks and separate pagination when
truncated. Preserve item/field/option IDs and mappings. For a relevant single-select
value, capture native optionId as FieldValue.option_id and its observed name as
text; resolve against that field's options and recheck both. Text/non-select
projections include option_id=null. Never reconstruct selected identity from a
matching display name; denied selection stays unavailable/partial. Denied access leaves
integrated mode partial; no silently selected issues-only mode or invented values.
Project drafts remain preliminary records, not approved executable issues.

The [gh API manual](https://cli.github.com/manual/gh_api) defines REST Link and
GraphQL `$endCursor` pagination behavior. Verify the target host's current schema,
CLI fields, permissions and results before relying on a query.

## Reconcile and prepare the pair

Preserve relevant approved wording/content, not just URLs. Copy only authorized
claim-supporting evidence into the captured account, or retain committed relative
references and immutable identities. Unavailable/private/redacted required material
has an explicit limitation and prevents a full reconstructability claim.
Do not copy source-manager caches or capture secrets as checkpoint evidence.

Recheck every required issue, native graph, Project, authority and evidence input
used, then record observation end. Compare bodies, relationships and semantic
inputs, not just updatedAt. A relevant changed input makes the candidate stale
until recaptured/reconciled. Editorial equivalence needs available approval and
matching delivery inputs. Unsupported current SATISFIED claims become UNKNOWN;
a known failed check is UNSATISFIED. Preserve raw observed claims/history and
record discrepancies. Refresh Project projections only under their own authority.

Before installing, validate the concrete format/types, unique/ref-resolved IDs,
full declared scope/pagination, approval/evidence availability, source applicability,
shared capture ID, exact JSON-byte SHA-256 and semantic equality of the readable
hierarchy/wording/dispositions/claims/delivery/evidence/limitations. Merely matching
filenames, capture IDs, or digests is insufficient. An explicitly partial/stale
candidate may be kept as a diagnostic in scratch; it does not replace the last
accepted pair as complete/current.

## Transaction receipt and guarded acceptance

Use a unique candidate directory under the validated ignored `.sp-bp/work/`.
Parents and literal output paths must resolve within the authorized worktree,
without links/traversal into protected namespaces. Never invoke an upstream
helper whose direct or indirect default writes to `.superpowers/` or shipped upstream.

The receipt has exact typed fields: `transaction_id`/`capture_id` strings;
`repository_root`/`workspace_root` canonical path strings; `expected_head` commit;
`output_paths` the exact two relative paths; `prior_checkpoint_commit` commit|null;
`prior` two records with `path`, `exists` boolean, `blob`/`mode`/`sha256` and
`index_blob`/`index_mode` strings|null; `candidate` two records with `path`,
`staged_path`, `sha256`, `blob` string|null; `validation` records `{check: string,
result: PASS|FAIL|UNKNOWN, evidence: string}` for format, references, scope,
input-rechecks, evidence, digest and readable semantics; `phase` one of prepared,
installing, accepted, rolled-back, failed; and `accepted_commit` commit|null.
Only actual verified observations populate these fields. Keep the receipt
external to the output pair to avoid self-referential acceptance hashes.

1. **Guard prior state.** Re-establish exact root/worktree identity and inspect
   unfinished receipts. Require outputs absent or byte-equal to the last accepted
   pair, with no staged/unstaged/untracked user changes at either path. Verify the
   prior accepted commit/blobs/modes or recorded absence. Record relevant index
   entries and expected HEAD. Unrelated staged changes prevent an isolated pair
   commit: leave them untouched and reconcile, rather than silently including or
   unstaging them.
2. **Stage and validate.** Create proposed JSON/Markdown and receipt in the unique
   candidate directory; accepted outputs remain untouched. Run every validation
   above and record candidate hashes/validated blob identities when available.
   A prepublication failure preserves the accepted pair and failed candidate;
   it does not install one file as a partial replacement.
3. **Prepare.** Set phase prepared only after all required checks pass. Recheck
   both outputs and index/HEAD still match the recorded prior state. A user edit,
   unexplained index/HEAD change, stale input or missing permission stops publication.
4. **Install under commit authority.** Set phase installing; replace only the two
   literal outputs using native file operations. Verify their exact bytes. Stage
   exactly the pair, e.g. `git add -- .sp-bp/state.md .sp-bp/github-state.json`.
   Inspect the index blobs for both paths against validated candidates and require
   no staged change outside the pair. Do not reset unrelated index entries.
5. **Accept one exact pair commit.** Commit and inspect the actual commit tree,
   parent/range, diff scope and both validated blobs. Local acceptance is the
   successfully created commit containing that pair. A failed hook/commit or
   interruption leaves the transaction unaccepted. An unexpected commit/diff/blob
   is a reconciliation failure, not permission to silently rewrite history.
   Record the verified acceptance SHA in the receipt and set phase accepted.
6. **Verify separate publication.** Only after authorized integration/transport
   is observed does the repository's approved target contain the accepted pair.
   Record that target/reachability evidence separately. Local acceptance is not
   remote integration, another host's arrival, verified delivery, or release.

Git gives a tree containing both blobs; two filesystem replacements and remote
GitHub capture are not atomic. Store the source/verified-delivery identities in
the record and the later storage commit in the receipt/Git history.

## Interrupted publication and recovery

Before a new operation, inspect receipts, HEAD, index and literal output bytes.

- If K1 already contains both validated candidate blobs with the intended parent
  and pair-only scope, verify the acceptance point and finalize its unfinished
  receipt. Never silently roll back an accepted K1.
- Before acceptance, compare each output/index entry with the union of recorded
  prior and candidate identities (including recorded absence), and require
  unchanged unrelated index/files. A differing user edit or unexplained HEAD/index
  change stops automatic recovery and preserves all evidence/files.
- With verified ownership and applicable recovery authority, restore **both** pair
  files **and only their index entries** from the verified prior checkpoint K0.
  A literal-path `git restore --source "$sp_bp_prior_commit" --staged --worktree
  -- .sp-bp/state.md .sp-bp/github-state.json` is one Git interface; re-establish
  the project Git boundary before invoking it. Verify exact prior blobs/hashes/modes,
  preserve unrelated index/files and sentinel, and set phase rolled-back.
- With no prior pair, remove only the two provably transaction-created candidate
  paths and their owned index entries under authority; restore recorded absence.
  Never recursively delete the directory, reset a workspace/index, or remove an
  intervening edit. Recheck unrelated state and mark rolled-back only on success.
- Completing an interrupted candidate requires fresh validation/source/ownership
  guards and publication authority. A prepared receipt or remembered pass is not
  sufficient after an interruption. Partial worktree files are never the accepted
  source; use the validated pair in K0/K1 or report no accepted pair.

Offline or after Project removal, the last accepted checkpoint explains its dated
captured graph/claims and availability limitations. Live eligibility and intended
mutations are unverified. Reconcile current source revisions, graph and evidence
when access returns; do not restore stale state into GitHub. Task fixtures prove
only the actual file/Git behaviors exercised; paper/probe reasoning is separate.

When normalizing native pages, preserve GraphQL endCursor separately from
hasNextPage in Page.cursor_out and Page.has_next_page. Non-null terminal cursors
are valid when hasNextPage=false; continuity applies only to an actual next page.
A denied native collection remains null in its nullable source field, with a
field-specific limitation and incomplete collection metadata (unknown total,
no observed pages). Retain it only as partial diagnostic; never convert it into
observed empty membership or accept it as complete.
