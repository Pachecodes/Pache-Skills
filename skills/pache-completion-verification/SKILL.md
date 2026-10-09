---
name: pache-completion-verification
description: "Use when verifying worker completion or external effects."
---

# Completion Verification

## When to use
Use when a worker reports done, a command times out, a scheduled callback arrives, or a write to an external system is reported successful.

## Prerequisites and authority
Require the exact task/attempt identity, target, current authority, and readback capability. This skill grants no permission to write or retry. When target readback is unavailable, report the effect as unverified.

## Procedure
1. Enumerate every acceptance criterion and effect claimed. Separate requested assignments, observed activity, submitted artifacts, reviewed artifacts, and accepted behavior.
2. Inspect current tracked/native process ownership and descendants. A callback or exit code alone is not a substantive handoff. “Waiting for workers” is an interim state.
3. Read the actual final artifact, changed paths, evaluator results, and candidate identity. Match receipts to the exact output under review.
4. For an authorized external write, read back the exact resource by stable identity with an allowlisted field projection. Check intended fields, ownership/environment, version, and status. Do not infer provider defaults.
5. After a timeout or uncertain response, reconcile before retry. A request may have succeeded; repeating a non-idempotent effect can duplicate it. Use provider-supported idempotency only when its actual contract is established.
6. Keep distinct verdicts for source review, branch publication, runtime identity, infrastructure health, feature activation, and user-visible acceptance. Healthy processes or a successful push do not prove the intended code is running.
7. Preserve partial truth. Accepted individual gates can coexist with a failed or interrupted whole mission. Retain earlier failures as historical evidence; supersede only the current status when fresh proof warrants it.
8. Clean up only owned temporary resources and verify absence through exact-resource readback. Avoid broad process kills or wildcard resource removal.

## Acceptance and delivery
Use PASS, FAIL, BLOCKED, and NOT TESTED per criterion. Include what changed, what was read back, what remains unknown, and the next required decision. Do not claim all done until all named criteria are closed. Reproduction of worker tests is useful but is not independently designed verification.

## Example prompt
“Check this worker's claimed completion and reconcile the exact target after its timed-out write; do not retry or make new changes.”
