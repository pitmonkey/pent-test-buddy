# Pen Test Buddy

A Claude Code plugin that turns an empty directory into a disciplined, scope-governed
penetration-testing workspace — and keeps Claude inside the rules of engagement for the
whole job.

> **Authorized testing only.** This plugin assumes you have written authorization to test
> the targets you put in scope. It is built to *enforce* that authorization, not replace it.

## What it does

- **Scaffolds a structured engagement workspace** (`/pentest-init`) with a `data/raw` →
  `data/knowledge-base` pipeline, a `docs/scope.md`, and a governed `CLAUDE.md` that hard-wires
  the workflow below into every session run from that directory.
- **Intakes the Rules of Engagement** (`/grill-scope`) with a relentless, pentest-specific
  interview that fills out `docs/scope.md` — targets, exclusions, written authorization,
  window, and what classes of action are allowed.
- **Gates planning against scope** (`/scope-check`) — before any plan runs, it reviews the
  planned targets and actions against `docs/scope.md` and reports out-of-scope, borderline, or
  constraint-violating items back to you for an explicit go/no-go.
- **Distills raw output into a knowledge base** (`/kb-distill`) — turns verbatim tool output
  into per-host facts and an index, so Claude reads what it already learned instead of
  re-running equivalent scans.
- **Captures findings and ships a report** (`/log-finding`, `/pentest-report`) — records each
  confirmed finding in a consistent shape, then assembles scope + KB + findings into a
  client-ready report draft.
- **Tracks artifacts and audits every command** (`/cleanup-tracker` + an automatic command-log
  hook) — logs anything dropped on a target for teardown, and records every Bash command run in
  an engagement workspace to `evidence/command-log.md` for chain of custody.
- **Borrows ideas from uninstalled tooling** (`/get-inspired <folder>`) — point Claude at a
  plugin/repo you don't want to install and it mines transferable methods, tools, and workflows
  for the task at hand, without installing, copying, or running any of it.

## The governed workflow

The `CLAUDE.md` written into each engagement directory requires, for any offensive action:

1. `docs/scope.md` is the authority — read it before touching any target.
2. Plan via superpowers: `brainstorming` (→ spec) then `writing-plans` (→ plan). No tools run
   against a target before a spec and plan exist and you have approved them.
3. Run `scope-check` on the plan and report conflicts before executing.
4. Knowledge-base discipline: read the KB first, raw output to `data/raw/`, then `kb-distill`.
5. Approvals are per-plan, never blanket.

## Install

```
/plugin marketplace add /path/to/pent-test-buddy
/plugin install pent-test-buddy
```

Then, in a fresh empty working directory for your engagement:

```
/pentest-init
/grill-scope
```

## Skills

| Skill | Slash command | Purpose |
|-------|---------------|---------|
| `pentest-init`  | `/pentest-init`  | Scaffold the engagement workspace |
| `grill-scope`   | `/grill-scope`   | Relentless pentest scope interview → `docs/scope.md` |
| `scope-check`   | `/scope-check`   | Review a plan against scope, report conflicts |
| `kb-distill`    | `/kb-distill`    | Raw tool output → knowledge-base entry + index |
| `log-finding`   | `/log-finding`   | Record one confirmed finding into `findings/` |
| `pentest-report`| `/pentest-report`| Assemble scope + KB + findings → `report/report.md` |
| `cleanup-tracker`| `/cleanup-tracker`| Track artifacts dropped on targets + teardown checklist |
| `get-inspired`  | `/get-inspired <folder>`| Mine an uninstalled folder for borrowable ideas (no install) |

### Automatic hook

A `PostToolUse` hook logs every Bash command run **inside an engagement workspace** to
`evidence/command-log.md` (chain of custody). It is inert in any non-engagement directory and
never blocks a command.

## Dependencies

**Required:** the `superpowers` plugin. The plan-first workflow uses its `brainstorming`
(→ spec) and `writing-plans` (→ plan) skills, and `/pentest-init` hard-stops if it is not
installed. Install it first:

```
/plugin install superpowers@claude-plugins-official
```

or from source (https://github.com/obra/superpowers):

```
/plugin marketplace add obra/superpowers
/plugin install superpowers
```

## Roadmap

A passive recon subagent and an optional shared resource library are planned but not yet
included.
