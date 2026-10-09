# Compatibility

[Back to README](../README.md#guides-and-evidence)

## Capabilities, not universal tool names

| Runtime | How to adapt |
| --- | --- |
| Hermes | Use the installed skill loader or explicitly read SKILL.md; map file/process/delegation/verification steps to enabled tools. Home/profile selection is installation-specific. |
| Claude Code | Use the installed release's supported skill discovery or explicitly read SKILL.md; inspect current help/docs for scope and permission options before using them. |
| Codex | Use the installed release's supported skill discovery or explicitly read SKILL.md; inspect current help/docs for sandbox and worker support. |

All three can use the documents as instructions when file reading is available. Automatic discovery and invocation syntax depend on release and configuration; they were not tested in this pack. No particular subagent, browser, scheduler, mobile tool, or API is universally available. Missing capabilities produce a precise blocker. Never simulate unavailable execution or call a sequential self-review independent review.
