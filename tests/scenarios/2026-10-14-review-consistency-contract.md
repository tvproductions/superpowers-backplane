# Issue31 review consistency application

Version: `issue31-review-consistency/v1`. This adds focused coverage for the
four confirmed PR33 comments. It does not edit earlier frozen contracts.

The exact prompt is stored in the integrated-verification run manifest. The
prompt was fixed before the fresh baseline invocation; this rubric records its
five required outcomes before source corrections or candidate capture.

| Assertion | Required outcome |
| --- | --- |
| R1 | Different recheck kinds may share a tracker id under an explicit documented composite identity. |
| R2 | An identical `(kind, id)` recheck pair is rejected as a duplicate. |
| R3 | After evaluation-pointer edits, the numbered closeout sequence requires a fresh full issue/graph read immediately before closure; acceptance drift prevents the closing write until reconciled and revalidated. |
| R4 | The partial example's unavailable E1 observation renders as unavailable, without a contradictory unchanged explanation. |
| R5 | The stale example's changed issue observation renders as changed, without a contradictory unchanged explanation. |

Score each applied outcome PASS/FAIL/UNKNOWN against the full captured response
and inspected source. A baseline that identifies a source gap is retained as
such; do not convert a correct gap diagnosis into a false behavioral failure.
Record fixture, prompt, source, response and process identities. This is
read-only application evidence, not live closure or production capture.
