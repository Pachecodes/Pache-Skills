---
name: pache-safe-recurring-automation
description: "Use when designing bounded recurring agent automation."
---

# Safe Recurring Automation

## When to use
Use for recurring signals, fixed-time reports, event handling, or finite goal-driven work. Prefer a normal one-shot task when no recurrence or measurable stop exists.

## Prerequisites and authority
Discover an available scheduler/event transport, process ownership, state storage, and current tool permissions. Installing this document creates no scheduler. Starting or persisting a job needs explicit opt-in.

## Procedure
1. Classify the trigger: fixed time for reports, events for incoming work, interval for sources lacking events, finite goal for active implementation. Prefer event subscriptions when reliable events exist.
2. Define mission, exact scope, permitted reads/writes, done condition, verification rubric, cadence, shared deadline, concurrency, retry budget, notification policy, and owner.
3. Store state outside conversation context. Include attempt/event IDs, candidate identity, last accepted receipt, current phase, outstanding blocker, and next action. Deduplicate events before effects.
4. Separate maker, checker, and controller custody. A verification-only watcher may observe stalled work but cannot recover it without recovery authority.
5. For event transports, register before sampling current state to avoid a missed-event race. Reconcile each callback against the exact process/attempt; completion notifications trigger inspection, not acceptance.
6. Treat an ambiguous launch timeout as unknown. Inspect tracked process state, descendants, workspace activity, and late receipts before another launch. Never create a competing writer because stdout is absent.
7. Enforce a common budget across phases. At safe checkpoints stop on blockers or expiry. Do not abruptly kill a deployment or migration at a deadline and then assume external state is clean.
8. Update both durable state and effective scheduled instructions when scope changes. Read back the exact stored job and its destination/enabled state before claiming supervision reflects the change.
9. Notify only on meaningful state changes, failures, required decisions, or final acceptance. A no-op is valid. Repeated polling is not progress.

## Acceptance and delivery
Verify one harmless trigger-to-state-to-report cycle, deduplication, deadline handling, and owned-child cleanup before unattended use. Label configured, active, paused, and accepted separately. Do not persist a job beyond the session unless requested.

## Example prompt
“Design a read-only event-driven build watcher with a shared deadline, durable deduplication, and notifications only when the verdict changes; do not start it.”
