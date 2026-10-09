---
name: pache-bounded-feature-loop
description: "Use when running a bounded maker/checker feature loop."
---

# Bounded Feature Loop

## When to use
Use for one implementable feature or reproducible bug with explicit completion criteria. Do not use an endless “improve everything” loop.

## Prerequisites and authority
Require an exact repository/worktree, clean baseline inventory, permitted paths, supported runtime, isolated fixtures, and an execution owner. Discover actual agent and test capabilities first. If independent workers are unavailable, do sequential implementation and a separate review phase and label the independence limitation.

## Procedure
1. Record a task packet: goal, baseline identity, writable/read-only paths, acceptance cases, forbidden effects, time/concurrency/repair limits, and stop conditions. Suggested starting budget: one maker, one checker, two repairs, twenty minutes; adapt only under explicit authority.
2. Resolve other writers before edits. Use an isolated candidate. Preserve unrelated changes and capture tracked plus untracked baseline files.
3. Freeze approved evaluators outside maker write access. Record hashes and runtime versions. Hashes detect tampering; they do not enforce access control. Use actual filesystem/sandbox boundaries where available.
4. Reproduce the failing case before fixing. Distinguish assertion failure from a setup failure that never reached assertions. Record untouched baseline evidence.
5. Give the maker the minimum complete source and dependency contract. Implement the smallest change, capture actual commands/results, and retain failed attempts.
6. Wait for the maker and descendants to exit before freezing the candidate. Check evaluator integrity, then hand the frozen output to a clean-context checker.
7. Verify behavior, persistence, permissions, error cases, and old consumers relevant to the diff. A build or unit suite alone does not establish a user journey.
8. Send the exact failed assertion and evidence back for a bounded repair. Missing fixtures/access, authority refusals, integrity failures, or exhausted budgets stop the loop. Never reset the budget silently or weaken tests to obtain green.
9. Keep useful partial work in its isolated candidate. Publication, merging, deployment, external sends, and provider spending remain separately authorized effects.

## Acceptance and delivery
Deliver the candidate identity, changed paths, actual gate results and counts, repairs used, remaining blockers, and required decisions. A worker exit or completed batch is not whole-feature acceptance. Use the local [task packet](templates/task-packet.json).

## Example prompt
“Fix this one reproducible bug in an isolated candidate; freeze acceptance tests, allow at most two repairs, and leave publication disabled.”
