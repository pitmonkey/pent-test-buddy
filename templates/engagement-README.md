# {{ENGAGEMENT_NAME}} — Engagement Workspace

Initialized by Pen Test Buddy on {{DATE}}. This is an **authorized penetration-testing
workspace**. Read `CLAUDE.md` for the governed workflow Claude follows here.

## Layout

```
docs/
  scope.md                 Rules of Engagement — the authority for what is permitted
data/
  raw/                     verbatim tool output (nmap xml, gobuster txt, ...) — never edited
  knowledge-base/
    INDEX.md               catalog of every distilled artifact — read this first
    hosts/                 one markdown file per host (services, creds, findings)
    *.md                   cross-host topic notes (web, domain, creds)
CLAUDE.md                  governed-workflow rules loaded automatically by Claude Code
notes.md                   freeform scratch
```

## Getting started

1. `/grill-scope` — fill out `docs/scope.md` (targets, authorization, rules). Do this first.
2. Confirm written authorization is on file before any testing.
3. Plan each phase with Claude (it will use the superpowers brainstorm → plan workflow), let
   `scope-check` review it, then execute.
4. After each scan, `/kb-distill` turns raw output into reusable knowledge-base facts.

## Ground rules

- Nothing runs against a target that is not explicitly in scope and authorized in `scope.md`.
- Every plan is reviewed against scope before execution; out-of-scope is a hard stop.
- Raw evidence stays in `data/raw/`; distilled, reusable facts live in `data/knowledge-base/`.
