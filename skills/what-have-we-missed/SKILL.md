---
name: what-have-we-missed
description: Use when the operator wants a step-back review of an engagement to surface overlooked opportunities, gaps, and next moves — "what have we missed", "what are we missing", "any gaps", "brainstorm next moves", "lines of effort", or /what-have-we-missed. On-demand, run at any point.
---

# Pen Test Buddy — What Have We Missed?

Step back, read the whole engagement workspace, and surface next moves that have not been taken.
Get creative on *approach* while staying anchored to what is actually on disk. This is analysis
only — it runs no scans.

## Procedure

1. **Require an engagement.** Read `docs/scope.md`. If it is missing, stop and point to
   `/pentest-init` + `/grill-scope`. Read-only throughout.

2. **Walk the workspace and build the picture** (read, do not act):
   - `docs/scope.md` — what is in/out of scope and the constraints.
   - `data/knowledge-base/INDEX.md`, `hosts/*`, topic notes — what is known.
   - `findings/*` — what is confirmed.
   - `evidence/command-log.md` — what has actually been run (the "done" list).
   - `cleanup/cleanup-log.md`, `notes.md`, `docs/inspiration/*`, and a listing of `data/raw/`.

3. **Hunt for gaps and openings:** untouched in-scope targets, services discovered but never
   enumerated, credentials/hashes found but never reused, findings with an unexplored
   exploitation or chaining path, web surfaces not crawled, pivot/lateral opportunities implied
   by the data, stale leads parked in `notes.md`.

4. **Stay grounded.** Every suggestion cites the host / finding / file it is built on. Do not
   invent hosts, services, or credentials. Label anything speculative as a **hypothesis**.
   Creative on approach, truthful on facts.

5. **Return exactly two sections:**

   ### In scope — lines of effort we could pursue
   For each idea: **what** · **grounded in** (cite the host/finding/file) · **next action**.
   Every item's targets and actions fall within `docs/scope.md`.

   ### Likely out of scope — options nonetheless
   Ambitious ideas that exceed current authorization, sub-split:
   - **Would need scope expansion / extra authorization** — what to ask the client for.
   - **Blocked by a current RoE constraint** — name the blocker (DoS, social engineering,
     exfiltration, production, lateral movement, …) and why it is off-limits now.

6. **Offer to persist.** Offer to save both sections to `docs/ideas/<YYYY-MM-DD>.md` (create
   `docs/ideas/` if needed; if the file exists, append a timestamped block). Frontmatter:
   `date`, `generated-from: what-have-we-missed`.

## Rules

- Read-only. Runs **no** scans or tools against any target.
- Anything proposed is just an idea. Pursuing it goes through the normal
  plan → `scope-check` → operator approval flow. The in/out-of-scope split here mirrors the
  `scope-check` logic but is advisory — it does **not** grant approval.
- Ground every claim in a workspace file. Never fabricate hosts, services, or findings; mark
  guesses as hypotheses.
