---
name: avantic-approaches
description: Use for an outside-the-box, self-challenging gap audit of a pentest engagement that fans out to parallel subagents — "avantic approaches", "gap analysis", "audit our approach", "what controls/evidence/decisions are missing", "challenge our conclusions", "objectives vs activities", "what other avenues could we explore", "new attack paths across all phases", or /avantic-approaches. Review only; runs no actions; not scope-constrained but flags out-of-scope.
---

# Pen Test Buddy — Avantic Approaches (Fan-Out Gap Audit)

Fan out to parallel read-only subagents, mine the whole engagement workspace, and return a
critical, self-challenging audit: where the approach has gaps, and what other avenues exist
across the full pentest lifecycle. Get outside the box on *approach*; stay ruthless on *fact*.

**This is a REVIEW ONLY.** This skill — and every subagent it dispatches — runs no scan, tool,
command, or action against any target, and proposes none for execution. It is not constrained by
`docs/scope.md` when surfacing ideas, but every item is clearly flagged when it is likely out of
scope. Pursuing anything surfaced here goes through the normal plan → `scope-check` → operator
approval flow, separately.

Complementary to `what-have-we-missed` (quick creative next-moves): this is the heavier,
epistemically-disciplined audit pass.

## Procedure

1. **Require an engagement, read-only.** Read `docs/scope.md`. If it is missing, stop and point
   to `/pentest-init` + `/grill-scope`. State up front that this run is a review only and will
   take no action against any target.

2. **Fan out by analytic lens** (per `superpowers:dispatching-parallel-agents`). Dispatch up to
   **5 read-only `Explore` subagents in parallel**, one per lens. Open every subagent prompt with
   the hard contract (template below), then give it its lens:
   - **L1 — Objectives vs activities vs artifacts.** Compare stated objectives (`docs/scope.md`,
     `notes.md`, engagement README/`CLAUDE.md`) against what was *planned* and what was
     *completed* (`evidence/command-log.md`/`.jsonl`, `findings/*`, `data/knowledge-base/`, a
     listing of `data/raw/`). Where do objectives have no matching activity or artifact?
   - **L2 — Missing controls.** Safety / process / coverage controls absent or unproven: untested
     attack surfaces, skipped scope-checks, cleanup gaps, broken or missing evidence chain, no
     rollback.
   - **L3 — Missing evidence.** Claims, findings, or assumptions not backed by an artifact in
     `data/raw/` or the command log; conclusions resting on memory rather than record.
   - **L4 — Missing decisions / unexplored approaches.** Decisions deferred or never made;
     outside-the-box approaches the engagement never considered (creative, *not* scope-limited).
   - **L5 — Avenues to explore across the full lifecycle (generative).** New attack avenues for
     every phase — recon, enumeration, vuln analysis, exploitation, post-exploitation, exfil,
     reporting. Concretely: services discovered but never enumerated, surfaces with exploit
     potential, OSS components (by name/version in the KB) whose source could be pulled and
     reviewed for bugs, credential/hash reuse, chaining/pivot/lateral paths, persistence and
     exfil options. Ground each in a KB/finding/log fact where possible; outside-the-box where
     not. Proposed ideas only.

3. **Synthesize + self-challenge (main thread).** Merge the returns, de-dupe, then run an
   explicit **devil's-advocate pass**: for each item ask "what evidence would overturn this?" and
   downgrade or drop weakly-supported items. **Use conservative reasoning when evidence
   conflicts** — prefer the cautious reading and say which it is and why.

4. **Tag every item epistemically** — keep these distinct, never blur them:
   - `[evidence]` — cites a specific file / host / log line.
   - `[inference]` — reasoned from evidence, stated as inference.
   - `[speculation]` — outside-the-box, unproven.

5. **Flag scope without being bound by it.** Mark each item `in-scope` or `likely-out-of-scope`
   (with why + what authorization it would need). Out-of-scope items are *surfaced, never
   actioned*.

6. **Return this structure (to chat):**
   - **CONTRACT** — one line: review only; no action taken or proposed for execution.
   - **OBJECTIVES vs ACTIVITIES vs ARTIFACTS** — L1 summary/table.
   - **MISSING CONTROLS / MISSING EVIDENCE / MISSING DECISIONS** — L2–L4.
   - **AVENUES TO EXPLORE — by lifecycle phase** — L5, grouped recon → enum → vuln → exploit →
     post-exploit → exfil → reporting. Each: **what** · **grounded in** (cite, or marked
     speculation) · **why it could pay off**.
   - **CHALLENGES TO OUR OWN CONCLUSIONS** — the devil's-advocate results.

   Every item carries its `[evidence|inference|speculation]` tag and its scope flag.

7. **Offer to persist.** Offer to save the review to `docs/reviews/<YYYY-MM-DD>.md` (create
   `docs/reviews/` if needed; append a timestamped block if the file exists). Frontmatter:
   `date`, `generated-from: avantic-approaches`. This save is the **only** write the skill makes,
   and only on operator confirmation.

## Subagent prompt — hard-contract opener (use verbatim, fill `<LENS>`)

> You are a READ-ONLY reviewer in a penetration-testing workspace. This is a REVIEW ONLY. You
> MUST NOT run any scan, tool, command, or action against any target, and MUST NOT propose
> actions for execution. Read files only. Your sole job is gap analysis through this lens:
> `<LENS>`. Tag every finding `[evidence]` / `[inference]` / `[speculation]` and cite the file
> for evidence. Use conservative reasoning when evidence conflicts. Flag anything likely out of
> scope per `docs/scope.md` — but do not let scope limit what you surface. Challenge your own
> conclusions. Return a terse list and take no other action.

## Rules

- **Review only.** This skill and every subagent it dispatches run **no** scans/tools/actions
  against any target and propose none for execution. The subagent contract above is mandatory —
  never omit it from a dispatch.
- Not bound by scope for *analysis*, but every item is scope-flagged; out-of-scope = surface,
  never act. This advisory split does not grant approval — `scope-check` does that.
- Keep `[evidence]` / `[inference]` / `[speculation]` distinct; conservative reading wins ties;
  self-challenge is mandatory, not optional.
- Ground every claim in a workspace file; never fabricate hosts, services, findings, or
  credentials. Outside-the-box ideas are allowed but must be tagged `[speculation]`.
- The only write is the optional `docs/reviews/` save, on operator confirmation. Otherwise
  read-only throughout.
