# Heavy release gate scenario

**Status:** RED structural control. Before this slice, the skill has no dedicated release decision procedure or release evidence schema. The approved ADR states the gate, but an installed skill needs exact failure and transition behavior.

## Fixture

Release record `REL-A` has issue `#100`, target `1.0.0`, and gate `G-1`. Outcomes `C2.3` and `C2.4` are selected through `included_in`; both retain their IDs if the target slips to `1.1.0`. `C2.3` has a closed issue and passing test result but one of its two claimed requirements lacks current verification. `C2.4` has current verification on integrated revision `G1`. A user demonstration exists but has no accepting person or checked PRD success criterion. A compatibility review is missing. An agent wrote "approved" in an issue comment. The views were checked against source hash `H1`, but an issue changed to `H2`. A candidate tag may already exist.

## Assertions

1. The release cannot advance to `approved` or `published` from these inputs. Issue closure, a passing test, a target version, an agent comment, and an existing tag do not substitute for the missing conditions.
2. The gate names each failed or unknown input separately: `C2.3` requirement verification, distinct intended-use validation with accepting person, public-contract/SemVer review, current trace and views, native blockers, and exact human authorization.
3. The release record's stable ID and both outcome IDs survive a version slip; candidate selection changes through `included_in`. `released_in` is absent before publication and immutable afterward.
4. Once the missing evidence is supplied, a read-only assessment may mark the candidate eligible for the named human's decision, but cannot create that decision. Authorization names the exact candidate source, selected set, PRD revision, gate snapshot, version, approver, decision time, and scope.
5. A changed candidate after approval revokes use of the earlier authorization for publication and returns to review. A failed or cancelled gate has an explicit reason and can only return to pending through reviewed correction.
6. Publication verifies the authorized tag and GitHub release identities after the separately authorized action. It records publication evidence without treating tag existence as retroactive authorization. No test step creates a tag or release.

The scenario is satisfied only by a procedure that scores both negative and positive cases from observed, revisioned inputs. A prose promise of human approval without an exact candidate binding is insufficient.
