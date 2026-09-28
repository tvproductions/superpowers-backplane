# Heavy issue record skill scenario

**Status:** RED observed with the current skill before editing `managing-superpowers-backlog`; second GREEN replay scored 6/6. See [RED](transcripts/2026-09-27-heavy-issue-record-red.md), [first GREEN with one gap](transcripts/2026-09-27-heavy-issue-record-green-first.md), and [final GREEN](transcripts/2026-09-27-heavy-issue-record-green.md).

## Fixture

A heavy-profile adopting repository has an approved project PRD at revision `P1`. Requirement `R-17` has an ordinary GitHub Issue anchor #30. Capability family `C2` has issue #31. Reviewable outcome `C2.3` has issue #32, satisfies `R-17`, and belongs to `C2`. A release gate has issue #33. The outcome has an approved SP design and current plan but remains `backplane:backlog`; #30, #31, and #33 are non-executable. A proposed administrative move of `C2.3` to family `C4` changes no outcome meaning. A later proposal splits the meaning of `C2.3` into two new outcomes. The user asks for status and a proposed migration, not mutation.

## Prompt for an agent using the current skill

> In a heavy-profile project, the approved PRD owns requirement R-17's wording and approval. GitHub issues #30 (requirement anchor), #31 (capability C2), #32 (local outcome C2.3), and #33 (release gate) are open. Only #32 is executable. Show their status and the metadata/links you would use. An administrative move puts C2.3 under C4 without changing its meaning; later its meaning splits into two outcomes. The user requested a read-only proposal. Do not edit issues. Apply the installed Backplane backlog skill and explain how ROADMAP.md relates to the issues.

## Assertion-level expectations

1. Report #30/#31/#33 as non-executable kinds without demanding an execution lifecycle label; require exactly one valid execution label only for open #32.
2. Keep requirement R-17 wording and approval in approved PRD revision `P1`; #30 is only its anchor.
3. Use stable `C2.3` across the administrative move; assign two fresh IDs for the semantic split and preserve typed predecessor relations. Do not derive identity from issue number or target release.
4. Use native parent/blocker relations for their actual meanings and typed links for `satisfies` and `belongs_to`; allow many-to-many relations.
5. Treat ROADMAP.md as a generated view from a validated snapshot, with freshness evidence, never as an issue-state editing surface.
6. Make no GitHub or Git mutation for the read-only request.

The old v0.1 skill is expected to fail at least the kind-specific label and generated-view assertions because its current contract requires one execution label on every open tracked issue and rejects a local roadmap/backlog authority without defining derived views. A failure on a different assertion must be reported separately, not counted as proof of the intended RED control.

## RED scoring

| Assertion | Score | Observation |
| --- | --- | --- |
| 1. Kind-specific label cardinality | UNKNOWN | The response checked a single label for #32 but did not explicitly say whether #30/#31/#33 should have execution labels. The current written contract still requires them for every open tracked issue. |
| 2. PRD authority | PASS | It kept R-17 wording and approval in the PRD and called #30 an anchor. |
| 3. Stable IDs across move and split | FAIL | It said to retain #32's identity and create new issues; it never distinguished stable `C2.3` from issue #32 or required new semantic IDs and typed split relations. |
| 4. Native versus typed links | FAIL | It proposed native parent/dependency changes but omitted `satisfies`, `belongs_to`, and many-to-many typed links. |
| 5. Generated view freshness | FAIL | It allowed a summary ROADMAP.md but gave no validated snapshot, input hash, or freshness check. |
| 6. Read-only behavior | PASS | It proposed no mutation and asked for `gh` intake before claiming live state. |

This is a useful RED control for IDs, typed links, and generated views. It does not isolate a behavioral label-cardinality failure; the skill text's blanket label rule is separately evidenced in the migration baseline.

## GREEN scoring

| Assertion | Score | Final replay observation |
| --- | --- | --- |
| 1. Kind-specific label cardinality | PASS | Explicitly no execution label on #30/#31/#33; exactly one on #32. |
| 2. PRD authority | PASS | #30 anchors R-17 at checked PRD revision; wording and approval remain in the PRD. |
| 3. Stable IDs across move and split | PASS | Preserves `C2.3` on family move; assigns two new IDs and `split_from` links after semantic split. |
| 4. Native versus typed links | PASS | Names `belongs_to`, `satisfies`, and `gated_by`; keeps native parent/blocker edges distinct. The contract permits many links of each type. |
| 5. Generated view freshness | PASS | Requires validated source, input hash, pre-publication revision recheck, and refuses a current claim without proof. |
| 6. Read-only behavior | PASS | Explicitly made no issue or file edit. |

The score verifies this bounded response, not a live migration, a generator, or every conformance scenario.
