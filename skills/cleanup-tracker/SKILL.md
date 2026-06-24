---
name: cleanup-tracker
description: Use when something has been dropped on a target during a pentest (uploaded file, shell, created account, persistence, config change) or when tearing down at engagement end — "track cleanup", "log artifact", "cleanup checklist", "what needs removing", or the operator runs /cleanup-tracker. Tracks artifacts left on targets and their removal.
---

# Pen Test Buddy — Cleanup / Artifact Tracker

Track everything left on a target so nothing is forgotten at teardown. Two modes.

## Mode A — Record an artifact (when something is dropped on a target)

Invoke this the moment an artifact is placed on a target — do not defer it. Append a row to
`cleanup/cleanup-log.md` (create with header if missing):

```
| <YYYY-MM-DD HH:MMZ> | <host/target> | <type> | <location/path> | <how to remove> | active |
```

- **type** — one of: uploaded-file, shell/implant, account, persistence, config-change, other.
- **location** — exact path / account name / registry key / cron entry, etc.
- **how to remove** — the exact command or steps to undo it.
- **status** — starts `active`.

## Mode B — Teardown checklist (at phase/engagement end)

1. Read `cleanup/cleanup-log.md`.
2. Present every row with `status: active` as a checklist, grouped by host, each with its
   removal step.
3. As the operator confirms each is removed, set that row's status to `removed` and stamp the
   time.
4. Report what remains `active`. **The engagement is not clean until zero `active` items
   remain.** Surface any outstanding items prominently.

## Rules

- Log on drop, not at the end — memory is not chain of custody.
- Never delete rows; flip `active` → `removed` so the log is a complete record for the report.
- Record exact removal steps when you log, while you still remember them.
