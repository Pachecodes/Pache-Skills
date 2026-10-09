---
name: pache-agent-integration-preflight
description: "Use when auditing an agent-facing IDE integration."
---

# Agent Integration Preflight

## When to use
Use when attaching an IDE, desktop frontend, or companion device to an existing agent runtime.

## Prerequisites and authority
Know the authoritative runtime/profile, current configuration owner, installed versions, and intended integration. Inspection is distinct from permission to install, pair devices, or change settings.

## Procedure
1. Map boundaries: shared configuration/skills does not imply the same active conversation; another host is a separate runtime unless intentionally synchronized.
2. Inspect current vendor documentation and implementation for launch mechanisms, config writes, bypass flags, telemetry, diagnostics, relays, mobile transport, license, and update channel.
3. Check existing installation, executable resolution, processes, version, and plugins before installing. Prefer an authorized signed/maintained distribution. Do not overwrite unrelated plugins.
4. Keep manual permissions by default. Read the effective launch arguments, not merely the UI label. Telemetry and remote diagnostics require explicit policy for private source.
5. For application-owned settings, stop the owner cleanly, preserve a backup, change only documented fields, relaunch, and read back after startup. Never race a live renderer writing the same store.
6. Test attachment using a non-sensitive repository. Verify actual profile/runtime selection, lifecycle/status events, and the correspondence between displayed diffs and real repository state.
7. Pair a companion device separately through human authentication/approval. Never put pairing tokens in chat. Read back the intended host/device mapping. Describe actual mobile capabilities rather than assuming a full editor.
8. Preserve durable review/approval boundaries even when the frontend can stage or commit directly.

## Acceptance and delivery
Report installed/CLI versions, effective runtime/profile, permission mode, telemetry policy, preserved plugins, harmless session evidence, settings readback, and any human pairing step. Connected badges are hints, not end-to-end proof.

## Example prompt
“Audit this IDE's attachment to my existing runtime read-only; verify identity and permission boundaries without installing or pairing anything.”
