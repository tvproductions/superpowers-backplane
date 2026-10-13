# Readable checkpoint contract

Render `.sp-bp/state.md` from the validated structured candidate. It is a dated
captured account, not live backlog or execution authority. All claims derive
from [sp-bp-checkpoint/v1](checkpoint-format.md); independently compare the
rendered semantics with the source before acceptance. Use this shape with
observed values; unavailable material stays visible.

```markdown
# Backplane checkpoint

Format: sp-bp-checkpoint/v1
Capture ID: <capture.id>
JSON SHA-256: <digest of exact github-state.json bytes>
Observation window: <capture.started_at> to <capture.finished_at>
Mode / capture status / origin: <mode> / <status> / <origin>
Repository / Project: <identities, or explicit issues-only absence/unavailability>
Source commit: <source.commit; not the future storage commit>
Scope and completeness: <selected/excluded/external graph, pages/totals, rechecks>
Relevant Project projections: <item/field/selected-option identities, display values, availability>

## Product hierarchy and native work

| Issue and title | Code / kind | Native parent / children | Native dependencies | Observed state / lifecycle | Target milestone / PR context |
| --- | --- | --- | --- | --- | --- |

## Approved obligations and dispositions

| Governing statement/key and revision | Owner | Contributions/evidence | Approved disposition and authority | Remaining gap |
| --- | --- | --- | --- | --- |

## Coverage and evaluated satisfaction

| Issue / criterion wording and revision | Requirements and contributions | Current evaluated result / applicability | Verified delivery commit | Evidence / review identities and availability | Remaining work |
| --- | --- | --- | --- | --- | --- |

## Release targets

<Observed milestone grouping and separately observed publication authority;
no inference of release permission from closure, merge, or satisfaction.>

## Authority and evidence availability

<Design/plan/approval and evaluation identities, retained relevant content,
source revisions, semantic reconciliations, historical results and missing material.>

## Limitations and next reconciliation

<Capture gaps/drift, source/projection discrepancies, excluded/external scope,
UNKNOWN evidence, partial/private/redacted material, offline limitations, and
current probes required before any intended live action.>
```

Do not render a raw issue claim as an accepted SATISFIED result when its evidence
is UNKNOWN/stale. Preserve both the observed claim and discrepancy. A deferred
obligation is not delivered. Closed-child progress is not parent satisfaction.
Include actual criterion/requirement wording and governing revisions, not just
IDs or URLs. The accepted storage commit is found through the external receipt
or verified Git tree; do not create a self-referential field.

A partial diagnostic clearly states status and cannot be presented as the
accepted pair. Offline interpretation preserves dated graph/evidence but makes
live eligibility/mutation unverified. Removal from a Project does not erase issue
identity or justify restoring stale native state. Follow the existing handoff
workflow for session continuity; the product pair has a different purpose.
