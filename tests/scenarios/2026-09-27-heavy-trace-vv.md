# Heavy trace and V&V scenario

**Status:** The corrected baseline behavioral response was already mostly sound; the structural negative control proved the exact evidence contract absent. After implementation, the structural check passed and the read-only behavioral replay passed 6/6. See [GREEN verbatim response](transcripts/2026-09-27-heavy-trace-vv-green.md).

## Fixture and prompt

An approved PRD revision `P1` defines requirements `R-1` and `R-2`. Outcome `C2.3` claims both through `satisfies`. Outcome `C2.4` also claims `R-2`, so links are many-to-many. Concrete behavior examples `E-1` and `E-2` were agreed for `R-1` and `R-2`, and test definitions `T-1` and `T-2` point to them. Integrated revision `G1` has passing verification evidence `V-1` for `R-1` through `C2.3`, but no result for `R-2`. The PRD then changes `R-2` in approved revision `P2`. Old `R-2` evidence from `P1` on `C2.4` remains historical. A pilot user review `U-1` has not happened. The user asks for a read-only trace and whether `C2.3` and a candidate release can be called verified/validated.

> Build a forward and reverse trace for approved requirements R-1 and R-2 and outcomes C2.3 and C2.4. C2.3 explicitly claims both R-1 and R-2; C2.4 also claims R-2. R-2 changed from PRD P1 to approved P2. C2.3 has passing integrated G1 evidence only for R-1, while C2.4 has old P1 evidence for R-2. Behavior examples E-1/E-2 and test definitions T-1/T-2 exist, but no pilot user review U-1 has occurred. State which links and evidence are current, stale, missing, or unknown; whether C2.3 is verified; whether the release is validated; and what exact revision, method, result, integrated-source, and accepting-person fields the evidence records would need. Do not edit issues or documents.

## Assertions

1. The trace shows R-1 -> C2.3, R-2 -> C2.3 and C2.4, and reverse outcome -> requirement links without treating one row as the only owner.
2. `E-1/E-2` and `T-1/T-2` are definition links, not passing results. `V-1` is tied to R-1, C2.3, P1, and integrated G1; no result is invented for R-2.
3. R-2's P1 evidence remains historical but is stale for P2 until impact analysis and current verification; changing an approved requirement does not erase old records.
4. C2.3 is not verified while any claimed governing requirement lacks current evidence; a closed issue or passing result for R-1 alone cannot substitute.
5. The release is not validated without distinct intended-use evidence against PRD users and success criteria with an accepting person; verification and validation are separate.
6. The response is read-only and names the exact missing probes rather than assigning PASS to unknown links or evidence.

The current heavy issue-record reference can represent `satisfies`, `exemplified_by`, `tested_by`, `verified_by`, and `validated_by`, but does not yet define evidence currency, forward/reverse reconciliation, or the release validation decision. The RED response should expose at least one of those missing rules before implementation.

## Observed controls and scoring

The first prompt accidentally omitted the stated C2.3 → R-2 claim, so its response was not a valid many-to-many control. The corrected prompt produced a sound provisional trace and refused premature verification/validation even before the new reference. That behavioral response did **not** establish a RED failure; it showed general agent reasoning can cover the case without a reusable contract. The assertion-level negative control was structural: `heavy-trace-and-evidence.md` did not exist, and `heavy-issue-record.md` had no exact evidence schema. Both were observed before writing the new reference. Afterward, the new example parsed as JSON with all 11 required fields.

| Assertion | GREEN score | Evidence |
| --- | --- | --- |
| 1. Many-to-many forward/reverse trace | PASS | R-1 → C2.3; R-2 → C2.3/C2.4 and both reverse paths. |
| 2. Definitions versus results | PASS | E/T links unknown and not counted as passing; G1's coverage limited to R-1 and exact fields requested. |
| 3. P1/P2 history and staleness | PASS | Old C2.4 P1 evidence retained; P2 current proof missing; reviewed impact path named. |
| 4. Outcome verified gate | PASS | C2.3 not verified while R-2 and own acceptance lack current evidence. |
| 5. Distinct validation | PASS | U-1 absent; release not validated; intended-use fields and accepting person named. |
| 6. Read-only, unknowns | PASS | No mutation; missing URLs/revisions classified unknown rather than current. |

This validates the bounded response and schema example. It does not prove a live trace engine or release gate.
