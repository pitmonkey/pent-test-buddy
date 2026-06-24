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
| `pentest-init` | `/pentest-init` | Scaffold the engagement workspace |
| `grill-scope`  | `/grill-scope`  | Relentless pentest scope interview → `docs/scope.md` |
| `scope-check`  | `/scope-check`  | Review a plan against scope, report conflicts |
| `kb-distill`   | `/kb-distill`   | Raw tool output → knowledge-base entry + index |

## Dependencies

Uses the `superpowers` plugin's `brainstorming` and `writing-plans` skills for the plan-first
workflow. Install superpowers alongside this plugin for the full experience.

## Roadmap

Report generation, a passive recon subagent, and an optional shared resource library are
planned but not yet included.
