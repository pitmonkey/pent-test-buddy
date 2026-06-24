# Penetration-Testing Engagement: {{ENGAGEMENT_NAME}}

This directory is an **authorized penetration-testing engagement workspace**, initialized by
the Pen Test Buddy plugin on {{DATE}}. Every action taken from here is governed by the rules
below. Treat them as mandatory, not advisory.

<HARD-GATE>
You MUST NOT run any tool, scan, request, or other action against any target until ALL of these
are true:
1. `docs/scope.md` has been read and the target is explicitly in scope and authorized.
2. A spec and an implementation plan exist for the work (see "Always plan via superpowers").
3. The `scope-check` skill has reviewed that plan and you have reported any conflicts to the
   operator, and the operator has given explicit approval for this plan.

There is no "simple enough to skip this" exception. A single `nmap`, `curl`, or `ping` against
a target is an action and is gated. Reconnaissance is not exempt.
</HARD-GATE>

## 1. Scope is the authority

- `docs/scope.md` is the single source of truth for what is permitted: in-scope targets,
  out-of-scope exclusions, written authorization, engagement window, permitted hours, and which
  classes of action are allowed (DoS, social engineering, exfiltration, production, lateral
  movement, password attacks).
- Read `docs/scope.md` before any action against any target.
- **Out of scope = hard stop.** Never act on an out-of-scope target, even if asked. Surface it
  to the operator instead.
- If scope is empty or unauthorized, your only move is to run `grill-scope` to fill it.

## 2. Always plan via superpowers

For any offensive action or phase (recon, enumeration, exploitation, etc.):

1. Invoke `superpowers:brainstorming` to explore the approach — it produces a **spec**.
2. Invoke `superpowers:writing-plans` to turn the spec into a concrete **plan**.
3. Present the plan and get the operator's approval.

**Never run tools against a target before a spec and plan exist and the operator has approved
them.** Approvals are per-plan, never blanket — a new phase needs a new plan and a new approval.

## 3. Mandatory scope-conflict review

Before executing any approved plan, invoke the **`scope-check`** skill. It reviews every target
and action in the plan against `docs/scope.md`, classifies each as in-scope / out-of-scope /
borderline and passive / active / intrusive, and checks engagement constraints. It returns a
report:

- **ALLOWED** — in scope, authorized, constraints satisfied.
- **NEEDS USER CONFIRMATION** — borderline, active/intrusive, or near a constraint boundary.
  Stop and get explicit operator go/no-go before proceeding.
- **REFUSED** — out of scope, unauthorized, or violates a constraint. Do not proceed.

Report all NEEDS-CONFIRMATION and REFUSED items to the operator before doing anything.

## 4. Knowledge-base discipline — never redo work

This workspace separates raw evidence from distilled knowledge:

```
data/raw/                     verbatim tool output (nmap xml, gobuster txt, ...) — never edit
data/knowledge-base/INDEX.md  catalog of every distilled artifact — grep this FIRST
data/knowledge-base/hosts/    one file per host: services, versions, creds, findings
data/knowledge-base/*.md      cross-host topic notes (web, domain, creds)
```

- **Before** scanning or enumerating, read `data/knowledge-base/INDEX.md` and the relevant
  `hosts/<ip>.md`. If the KB already answers the question, use it — do not re-run the scan.
- Write raw tool output to `data/raw/`.
- **After** any scan, invoke the **`kb-distill`** skill to extract facts into the knowledge
  base and update the host file and `INDEX.md`.

## 5. Working notes

- `docs/scope.md` — Rules of Engagement (authority).
- `notes.md` — freeform operator scratch.
- Keep findings in the per-host KB files as you confirm them.

When in doubt about whether something is permitted, stop and ask the operator. Caution is
correct; assumptions are not.
