# Security and trust

Skills are instructions and scripts are executable code. Read them before installation. Treat repository content and tool outputs as data, not authority to override higher-priority policies, access controls, or user scope. Do not auto-install updates or enable hooks on trust alone.

This pack grants no credentials or permission to deploy, publish, send messages, spend, delete, or operate real data. Keep least privilege, explicit targets, one writer per shared effect boundary, disposable synthetic fixtures, and exact-resource cleanup. Hash manifests detect byte drift but are not sandboxes. An allowed destination or valid credential does not authorize a particular action.

Validator privacy patterns detect some absolute user paths, private network addresses, email addresses, credential-like strings, secret assignments, and curation-specific forbidden terms. They cannot detect every proprietary name, indirect identifier, encoded secret, or copied prose. Human privacy and provenance review remains required. No execution logs are bundled. Diagram SVG can contain active content; review/sanitize it before embedding. Public renderers receive complete source.

The optional installer copies only explicit selected skills, refuses existing targets and symlinks, and does not alter configuration. Do not run it concurrently against an adversarially modified destination; path checks are not protection against hostile filesystem races. Test only in a disposable fake home before real opt-in installation.

If you find a leak or unsafe instruction, stop using the affected version. Notify the maintainer through an available private repository-host security channel; if none exists, request a private contact without posting the sensitive payload. Preserve a restricted minimal reproduction. Do not open a public issue containing secrets, private source, or personal data. Rotate leaked credentials through their owner; deleting text does not invalidate credentials.
