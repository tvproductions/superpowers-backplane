# Structured checkpoint format

`sp-bp-checkpoint/v1` is a dated captured account, not live eligibility or a
mutable offline backlog. All fields below are required, including explicit
nulls/empty arrays for known absence. Unavailable is distinct from observed
absence and carries a limitation. Reject unknown format versions/fields until
reconciled rather than silently dropping source data. Use host-native JSON
parsing/validation; no language, helper engine, or schema library is mandatory.

## Primitive types and object definitions

`ID` and `Revision` are nonempty strings. Tracker IDs are namespaced strings,
never numeric identity substitutes; native numbers remain positive integers.
`Commit` is a resolved immutable Git object ID, not a moving ref. `SHA256` is
64 lowercase hex characters. `Time` is an ISO-8601 UTC string. `Availability`
is `available`, `unavailable`, or `redacted`; missing/redacted required material
prevents complete reconstructability. Arrays contain their named type, with
no duplicate IDs/links. Objects have exactly the listed fields.

| Top-level field | Type and required contents |
| --- | --- |
| `format` | Literal `sp-bp-checkpoint/v1` |
| `capture` | Capture |
| `repository` | Repository |
| `project` | Project or null; null is observed no-Project in explicit issues-only mode, not denied integrated capture |
| `source` | `{commit: Commit}`; source observation identity, not the eventual storage commit |
| `scope` | Scope |
| `issues` | Issue[]; full normalized native records for selected captured issues |
| `pull_requests` | PullRequest[] |
| `authorities` | Authority[] |
| `requirements` | Requirement[] |
| `criteria` | Criterion[] |
| `dispositions` | Disposition[] |
| `coverage` | Coverage[] |
| `evaluations` | Evaluation[] |
| `evidence` | Evidence[] |
| `limitations` | string[]; whole-capture limitations |

| Object | Exact fields and types |
| --- | --- |
| Capture | `id: ID`, `started_at: Time`, `finished_at: Time`, `mode: integrated\|issues-only`, `status: complete\|partial\|stale\|invalid`, `origin: live-capture\|supplied-records\|invented-fixture`, `rechecks: Recheck[]` |
| Recheck | `kind: issue\|project\|graph\|authority\|evidence\|delivery`, `id: ID`, `initial_revision: Revision\|null`, `final_revision: Revision\|null`, `result: unchanged\|reconciled\|changed\|unavailable`, `approval_ids: ID[]`, `details: string` |
| Repository | `id: ID` (owner/name), `url: string`, `owner: string`, `name: string` |
| Scope | `issue_ids: ID[]`, `excluded_ids: ID[]`, `external_records: External[]`, `collections: Collection[]`, `complete: boolean` |
| External | `id: ID`, `url: string\|null`, `owner: string\|null`, `reason: string`, `availability: Availability` |
| Collection | `name: string`, `owner_id: ID`, `expected_total: nonnegative integer\|null`, `pages: Page[]`, `complete: boolean` |
| Page | `cursor_in: string\|null`, `cursor_out: string\|null`, `has_next_page: boolean`, `record_ids: ID[]`; preserve observed native cursors and continuation separately |
| Project | `id: ID`, `url: string\|null`, `owner: string`, `number: positive integer`, `availability: Availability`, `field_definitions: Field[]\|null`, `items: Item[]\|null`, `limitations: string[]` |
| Field | `id: ID`, `name: string`, `type: string`, `options: Option[]`; capture only declared relevant fields, explicitly delimiting scope |
| Option | `id: ID`, `name: string` |
| Item | `id: ID`, `content_id: ID\|null`, `content_kind: issue\|pull-request\|draft`, `title: string\|null`, `updated_at: Time\|null`, `fields: FieldValue[]\|null` |
| FieldValue | `field_id: ID`, `text: string\|null`, `option_id: ID\|null`, `availability: Availability`; retain observed selected-option identity separately from its text projection |
| Label | `id: ID\|null`, `name: string`, `description: string\|null`, `color: string\|null` |
| IssueType | `id: ID\|null`, `name: string`, `description: string\|null`, `color: string\|null` |
| Milestone | `id: ID`, `number: positive integer`, `title: string`, `url: string`, `due_at: Time\|null` |
| BackplaneRecord | `code: string`, `namespace: string`, `kind: capability\|outcome\|gate\|external-boundary`, `authority_ids: ID[]` |
| Issue | `id: ID`, `number: positive integer`, `url: string`, `title: string`, `body: string\|null`, `state: OPEN\|CLOSED\|null`, `state_reason: string\|null`, `issue_type: IssueType\|null`, `labels: Label[]\|null`, `assignees: string[]\|null`, `milestone: Milestone\|null`, `updated_at: Time\|null`, `parent_id: ID\|null`, `child_ids: ID[]\|null`, `sub_issues_summary: Summary\|null`, `blocked_by_ids: ID[]\|null`, `blocking_ids: ID[]\|null`, `closing_pr_ids: ID[]\|null`, `backplane_record: BackplaneRecord\|null`, `accepted_evaluation_ids: ID[]`, `limitations: string[]` |
| Summary | `total: nonnegative integer`, `completed: nonnegative integer`, `percent_completed: number 0..100`; native closure progress is not satisfaction |
| PullRequest | `id: ID`, `number: positive integer`, `url: string`, `title: string\|null`, `body: string\|null`, `state: OPEN\|CLOSED\|MERGED\|null`, `base_ref: string\|null`, `head_ref: string\|null`, `merged_at: Time\|null`, `merge_commit: Commit\|null`, `review_status: accepted\|changes-requested\|pending\|unknown`, `closing_issue_ids: ID[]\|null`, `closure_intent: contribution\|closing\|unspecified`, `updated_at: Time\|null`, `limitations: string[]` |
| Authority | `id: ID`, `kind: issue-body\|specification\|plan\|approval\|project-instructions`, `locator: string`, `revision: Revision\|null`, `content: string\|null`, `availability: Availability`, `approver: string\|null`, `approved_scope: string\|null`, `approval_ids: ID[]`, `limitations: string[]` |
| Requirement | `id: ID`, `key: string`, `text: string`, `authority_id: ID`, `authority_revision: Revision` |
| Criterion | `id: ID`, `issue_id: ID`, `key: string`, `text: string`, `authority_id: ID`, `authority_revision: Revision`, `delivery_commit: Commit\|null`, `requirement_ids: ID[]` |
| Disposition | `id: ID`, `parent_issue_id: ID`, `requirement_ids: ID[]`, `child_issue_ids: ID[]`, `evidence_ids: ID[]`, `disposition: covered\|deferred\|excluded\|unresolved`, `owner: string\|null`, `approval_ids: ID[]`, `note: string` |
| Coverage | `id: ID`, `issue_id: ID`, `criterion_id: ID`, `requirement_ids: ID[]`, `contribution_issue_ids: ID[]`, `pr_ids: ID[]`, `combined_result_owner: string\|null`, `scope: string` |
| Evaluation | `id: ID`, `criterion_id: ID`, `requirement_ids: ID[]`, `verified_commit: Commit\|null`, `method: string`, `observed_result: string`, `result: SATISFIED\|UNSATISFIED\|UNKNOWN`, `observed_at: Time\|null`, `evidence_ids: ID[]`, `review_approval_ids: ID[]`, `applicability: current\|historical\|unreconciled`, `remaining_contributions: string[]`, `limitations: string[]` |
| Evidence | `id: ID`, `kind: verification\|review\|approval\|other`, `locator: string`, `revision: Revision\|null`, `sha256: SHA256\|null`, `availability: Availability`, `content: string\|null`, `verified_commit: Commit\|null`, `limitations: string[]` |

For unavailable nullable scalar or native collection fields, retain null with
specific limitations. A nullable native collection is null when not observed,
not an empty successful collection. Record its Scope collection as complete=false,
expected_total=null and pages=[]; capture status is partial. Known empty native
collections use [] with complete=true, total=0 and an observed empty terminal
page. Unknown mandatory identities cannot be invented to manufacture a valid
record; retain the failed raw diagnostic until a conforming record is available. A Project denied in integrated
mode retains its known identity and unavailable material with partial status.
Raw issue/PR bodies preserve observed claims, including discrepancies; evaluated
results and applicability express their supported interpretation separately.

## Referential, semantic, and complete-status constraints

1. IDs are unique in each object collection. Every reference resolves to the
   appropriate typed collection, or for native graph/PR endpoints an explicitly
   declared excluded/external tracker identity. Scope issue IDs exactly identify
   captured issue records. Never silently omit a scoped node. Code+namespace
   pairs are unique; preserve an approved alias migration in authority records.
2. Native parent/child and blocked-by/blocking edges agree when both endpoints
   are captured. Capture native closing references and observed issue/PR state
   separately; a closing keyword alone does not populate the native arrays.
   Sub-issue totals match full child enumeration; closure counts do not imply
   accepted obligations. Missing source records limit the claim.
3. Requirement/criterion authority revisions match their available approved
   authority records, or explicit accepted semantic reconciliation is captured.
   Current accepted evaluation pointers resolve to that issue's criteria.
   Coverage references its own issue/criterion and preserves many-to-many scope.
   Dispositions account for captured approved parent obligations; shared scope
   has contribution boundaries and a combined-result owner. Deferred/excluded
   entries need available approval and never count as satisfied delivery.
4. A current SATISFIED evaluation matches the criterion's requirement set and
   current applicable delivery commit, has available immutable verification and
   required review/approval, and has no unmet contributions or limitations that
   invalidate its claim. A known failed applicable check is UNSATISFIED; missing
   acceptance/evidence is UNKNOWN. Historical evidence is retained and cannot
   support a mismatching current claim. Body/mirror conflicts remain disclosed.
5. Capture times are ordered. Each required issue/graph/authority/evidence and
   integrated Project source is rechecked. Unchanged means matching observed
   identities; reconciled needs available semantic approval. A relevant changed
   input is stale; unavailable input is partial. Timestamps alone do not prove
   stable relationships or semantic equivalence.
6. A complete capture has complete declared scope and all required collection
   pages. Cursor continuity, explicit terminal pagination, totals where available, and
   declared membership are checked. Every required native graph, PR, relevant
   label/assignee and Project field/item collection is accounted for. Permission,
   network, schema, missing-page, or required evidence-availability gaps prevent
   complete reconstructability. Integrated mode requires an available captured
   Project and consistent projections; issues-only is explicitly selected.
7. A capture may completely record UNKNOWN satisfaction when checks were never
   performed and the absence is known; complete capture is not successful
   delivery. A partial/stale/invalid diagnostic never replaces a previously
   accepted pair as complete/current.
8. `state.md` and JSON share capture ID. Markdown names SHA-256 of the exact
   JSON bytes, and every readable hierarchy/criterion/disposition/result,
   delivery/evidence identity and limitation agrees with the JSON. A matching
   digest alone does not establish semantic agreement. Acceptance/storage
   commit is recorded outside the pair; source/evaluation commits stay distinct.

## Examples

[Complete invented example](checkpoint-complete-example.json) contains one
fully captured issue with a fixture-supported accepted evaluation, separate
source and verified-delivery commits, full declared native pagination, and
explicit issues-only mode. Its URI-like fixture evidence is embedded data,
not live verification or a repository product snapshot.
[Partial example](checkpoint-partial-example.json) preserves unavailable
required evidence and a missing graph page; [stale example](checkpoint-stale-example.json)
records changed source revision. They are diagnostics, not accepted replacements.

Use [capture/recovery](repository-checkpoint.md) and the
[readable contract](checkpoint-state-template.md). Example validity cannot
supply a real capture's approval, access, complete graph, or fresh evidence.

## Native pagination mapping and unavailable collections

For GraphQL, Page.cursor_in is the actual supplied after cursor (null initially),
Page.cursor_out is the returned pageInfo.endCursor, and Page.has_next_page is
pageInfo.hasNextPage. A nonempty final page commonly retains a non-null endCursor
while has_next_page=false; preserve both. Do not treat every non-null endCursor
as a missing page or discard it to imply termination. The next page exists only
when has_next_page=true, and then its cursor_in must equal the prior cursor_out.
The final observed page must have has_next_page=false for complete capture.
For REST, retain the observed page/next-Link identity and set has_next_page from
whether a next Link exists; a terminal next Link is null. Totals and membership
must still match; a terminal boolean alone is not proof of full scope.

Nullable native arrays permit denied-source diagnostics, including issue labels,
assignees, child/dependency/closing references, relevant Project definitions/items,
PR closing-issue references, and nested item values. Null requires an explicit field-specific limitation,
unavailable input observation, corresponding incomplete Scope collection and
partial status. Do not infer reciprocal edges, zero totals, eligibility, or
complete capture from null. Complete status requires all in-scope collections
observed, with available arrays, full membership and terminal/totals evidence.

For a PR's unavailable `closing_issue_ids`, use collection name
`closingIssuesReferences` with `owner_id` equal to the PR identity. Retain null,
a PR field-specific limitation, and an unavailable graph recheck for
`<PR identity>:closingIssuesReferences`; the collection has unknown total,
no observed pages, and complete=false. Capture status is partial. Observed empty
PR closing membership uses [] and an observed empty terminal collection, as for
issue-side closing references. Never infer one side from an unavailable other.

## Relevant Project value normalization

For `SINGLE_SELECT`, retain the observed native optionId in `option_id`, using
the same identity as the matching Field.options entry, and its observed name in
`text`. An available set value requires that option identity to resolve within
its own field and the name to agree; never infer the selection ID from text.
Recheck definitions and selected values together. An observed unset value uses
null for both fields. For a text projection or other non-single-select field,
`option_id` is null. Every FieldValue includes the slot.

An unavailable value uses availability=unavailable (or redacted), text=null
and option_id=null, with its specific limitation and incomplete input/collection
observations. It prevents complete capture; it is not observed unset membership.
The readable account retains selected identities alongside display values when
relevant to the captured projection, and discloses unavailable values.

These are pre-integration corrections to the unpublished v1 contract. Existing
pre-correction fixtures remain historical at their recorded source identities;
regenerate candidates against the current exact field set. No production pair
is migrated by these reference edits.
