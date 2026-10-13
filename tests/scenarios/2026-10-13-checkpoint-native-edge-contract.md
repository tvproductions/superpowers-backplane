# Checkpoint native-edge fix contract

Version checkpoint-native-edges/v1. Frozen before the review fix; original governance-probes/v1 and governance-freshness/v1 remain unchanged.

Source fixtures are 2026-10-13-checkpoint-native-edge-fixtures.json. Each contains a supplied checkpoint source and immutable raw native labels observations. Baseline uses the unchanged pre-fix typed record; candidate may project observed hasNextPage into a new exact field while retaining all supplied cursor identities/membership. Native source inputs, intended results and scoring do not change between arms.

1. A complete nonempty two-page labels connection has native first hasNextPage=true/endCursor=cursor-L1 and final hasNextPage=false/endCursor=cursor-L2. Both native cursor identities and all members must be preserved. Expected: structurally/semantically acceptable invented capture; non-null terminal endCursor must not make it partial.
2. Labels are denied. The source retains labels:null, partial capture, unknown expected total, no observed label pages, unavailable input recheck and specific limitation. Expected: conforming partial diagnostic; no invented empty successful collection or complete acceptance.

Pre-change validation must reproduce both representational failures with the actual source records. After one fix pass, validate both cases and original18 outcomes plus incomplete page/continuity/complete-null negatives. Retain complete input/output/errors/schema/validator identities; no live source, publication or general production-validator proof is claimed.

