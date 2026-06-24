# {{ENGAGEMENT_NAME}} — Engagement Workspace

Initialized by Pen Test Buddy on {{DATE}}. This is an **authorized penetration-testing
workspace**. Read `CLAUDE.md` for the governed workflow Claude follows here.

## Layout

```
docs/
  scope.md                 Rules of Engagement — the authority for what is permitted
  inspiration/             distilled notes from get-inspired (borrowed ideas, no install)
data/
  raw/                     verbatim tool output (nmap xml, gobuster txt, ...) — never edited
  knowledge-base/
    INDEX.md               catalog of every distilled artifact — read this first
    hosts/                 one markdown file per host (services, creds, finding pointers)
    *.md                   cross-host topic notes (web, domain, creds)
findings/                  one file per confirmed finding (log-finding)
report/                    report.md client deliverable (pentest-report)
evidence/
  command-log.md           automatic audit trail of every Bash command
cleanup/
  cleanup-log.md           artifacts dropped on targets + teardown status
CLAUDE.md                  governed-workflow rules loaded automatically by Claude Code
notes.md                   freeform scratch
```

## Getting started

1. `/grill-scope` — fill out `docs/scope.md` (targets, authorization, rules). Do this first.
2. Confirm written authorization is on file before any testing.
3. Plan each phase with Claude (it will use the superpowers brainstorm → plan workflow), let
   `scope-check` review it, then execute.
4. After each scan, `/kb-distill` turns raw output into reusable knowledge-base facts.
5. Confirmed a vuln? `/log-finding`. Dropped something on a target? `/cleanup-tracker`.
6. At the end, `/pentest-report` assembles the deliverable.

Optional: `/get-inspired <folder>` mines an uninstalled plugin/repo for ideas to use in
planning — borrowed approaches still pass through `scope-check` before use.

Stuck or wrapping up a phase? `/what-have-we-missed` reads the whole workspace and suggests
next moves (in scope) plus out-of-scope options worth knowing about.

Need a capability you don't have? `/find-skills <capability>` searches GitHub for an existing
skill or subagent and recommends one — you decide whether to install it.

## Ground rules

- Nothing runs against a target that is not explicitly in scope and authorized in `scope.md`.
- Every plan is reviewed against scope before execution; out-of-scope is a hard stop.
- Raw evidence stays in `data/raw/`; distilled, reusable facts live in `data/knowledge-base/`.
- Every Bash command is logged to `evidence/command-log.md` automatically.
- The engagement is not clean until every `cleanup/cleanup-log.md` item is removed.
