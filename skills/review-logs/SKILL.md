---
name: review-logs
description: Use to get a compressed overview of an engagement's audit logs — "review the logs", "summarise the command log", "what have we run", "log overview", "audit recap", "what did we do / what happened", "reconstruct the engagement", or the operator runs /review-logs. Reads evidence/command-log + cleanup-log and emits a caveman-compressed digest plus an inferred storyline of the engagement's activities.
---

# Pen Test Buddy — Review the Audit Logs

Read this engagement's audit trail and emit one super-compressed, caveman-style overview of what
was run and what was left behind — plus an inferred storyline of the engagement. Read-only: this
skill summarises, it never runs, edits, or writes anything.

## Procedure

1. **Guard.** Confirm this is an engagement workspace — `docs/scope.md` or `data/knowledge-base/`
   present (same guard the command-log hook uses, `hooks/command-log.py:27`). If neither exists,
   say so and stop: there is no engagement audit trail here.

2. **Load sources.**
   - `evidence/command-log.jsonl` — **primary** (full, untruncated). Parse line by line; each
     line is the full PostToolUse payload + a `logged_at` stamp. Pull `tool_input.command`,
     `logged_at`, and a short result from `tool_response.stdout` / `output` / `content`.
   - If `.jsonl` is absent, fall back to the truncated `evidence/command-log.md` table and **note
     the fallback** (results are truncated there).
   - `cleanup/cleanup-log.md` — read if present.
   - If a source is empty or missing, say which and continue with the rest.

3. **Compress the command log:**
   - Totals + time span: command count, first→last `logged_at`.
   - Commands grouped/deduped by tool/intent (e.g. `nmap×4`, `gobuster×2`, `curl×7`), target
     where derivable.
   - Per-target rollup: which hosts / URLs were touched.
   - Notable rows: errors / non-zero exits, creds or secrets touched, anything destructive —
     flag, don't expand.

4. **Compress the cleanup log:** active vs removed counts, and an explicit list of any `active`
   artifacts. These are teardown debt — surface them prominently.

5. **Reconstruct the engagement flow (inferred).** Walk the command log in chronological order
   (`logged_at`) and infer the *story* — phase, target, outcome — purely from log evidence.
   Classify command clusters into pentest phases by the tools/args used:
   - **recon/OSINT** — whois, dig/host/dnsenum, theHarvester, passive lookups.
   - **enum/scan** — nmap, masscan, gobuster/ffuf, nikto, enum4linux, smbclient.
   - **vuln analysis** — searchsploit, version probes.
   - **exploitation** — msfconsole, sqlmap, hydra/credential attacks, manual curl/payloads.
   - **post-exploit / persistence** — shells, account creation, uploads — cross-reference
     `cleanup-log.md` `active` rows.
   - **exfil / loot** — data pulls, dumps.

   Infer **outcome** from adjacent evidence: non-zero/error results or repeated retries →
   "failed/blocked"; a matching cleanup-log artifact → "succeeded, dropped X"; a pivot back to
   recon after a failed exploit → call it out ("re-recon after failed exploit"). Produce a short
   ordered storyline, e.g.: *recon on 10.0.0.5 → port/web scan → tried Jenkins RCE (failed) →
   more web enum → found upload bypass → uploaded webshell (cleanup: active) → enumerated
   internal hosts*.

   **Label it as inference.** This is reconstructed from logs, not ground truth — note gaps
   (manual actions that left no Bash command won't appear).

6. **Emit one caveman-compressed digest to chat** (no file). Sections, in order:
   - **FLOW** — the inferred storyline (step 5). The headline. Mark `[inferred]`.
   - **RAN** — command tally / grouped counts.
   - **TARGETS** — host/URL rollup.
   - **FLAGS** — errors, secrets touched, destructive ops.
   - **CLEANUP** — active vs removed; list every `active` item.

   Max signal, min tokens.

## Rules

- **Read-only.** Never edit or delete the logs, never write a file. Pure summary.
- Prefer `.jsonl` (full record) over `.md` (truncated). Note when falling back.
- Never re-run anything the log mentions. Any follow-up goes through plan → `scope-check` first.
- Don't print raw secrets in cleartext — reference where they live (mirror `log-finding`).
- The flow is an inference from logs, not the engagement's ground truth. Always label it so.
- If both logs are empty/absent, say there is nothing to review; do not invent activity.
