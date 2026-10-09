---
name: pache-frozen-evidence-review
description: "Use when reviewing frozen candidates and test receipts."
---

# Frozen Evidence Review

## When to use
Use before accepting delegated changes, comparing test receipts, or integrating outputs from separate workers.

## Prerequisites and authority
Require authorized source access, an immutable or read-only snapshot, evaluator ownership, and a supported test runtime. Do not read secret files merely to hash them. Reviewers need source and sanitized evidence, not live credentials.

## Procedure
1. Inventory permitted source and all consumed dependency manifests. Filter private paths before opening bytes. Include relevant module/bootstrap code; an incomplete snapshot cannot prove a feature is absent.
2. Preserve the original manifest. Make a separate filtered inventory with explicit exclusions rather than silently editing original pins.
3. Freeze the candidate only after all its writers have exited. Record content hashes, baseline identity, runtime/dependency versions, evaluator hashes, and command inputs.
4. Prove the reviewer can read every required input as the actual review identity. A privileged controller's access is not worker access. If needed, prepare a separate byte-verified read-only copy of approved inputs.
5. Run checks against those exact bytes. Record command, exit status, assertion results, log identity, and scope. Resolve actual imported/autoloaded source paths when the runtime could load another checkout.
6. Distinguish static inspection, fake-transport/unit tests, controller reproduction of maker tests, independently designed checks, and operational proof. Do not relabel one as another.
7. Rehash evaluators and candidate after execution. Any unexplained drift invalidates that receipt. A hash match says “same bytes,” not “correct behavior.”
8. Integrate approved deltas in a fresh single-writer candidate and run interacting tests together. Separate green suites do not prove combined compatibility.

## Acceptance and delivery
Return a narrow signoff tied to candidate and evaluator identities, executed cases, skipped cases, unresolved findings, and evidence classification. Derive totals from machine-readable case entries rather than prose. Keep private full logs restricted and publish only a safe projection.

## Example prompt
“Review this frozen candidate read-only; prove receipt/source alignment and distinguish maker-test reproduction from independent verification.”
