---
name: kb-distill
description: Use after running a scan or enumeration in a pentest engagement, when new raw tool output exists in data/raw/ — "distill this", "update the knowledge base", "process the nmap output", or the operator runs /kb-distill. Turns verbatim tool output into reusable per-host facts and an index so scans are not repeated.
---

# Pen Test Buddy — Distill Raw Output Into the Knowledge Base

Convert a raw tool artifact into structured, reusable knowledge so Claude reads facts instead of
re-running scans. Raw evidence is never edited; the knowledge base is the distilled layer.

## Procedure

1. **Pick the source.** Identify the raw artifact in `data/raw/` to distill (the operator names
   it, or use the most recent un-indexed file). If the artifact is not yet in `data/raw/`, move
   the verbatim output there first — raw output always lives in `data/raw/`, untouched.

2. **Extract facts.** Parse the artifact for:
   - Hosts / IPs and hostnames.
   - Open ports, services, and version strings.
   - Web paths, endpoints, technologies, interesting headers.
   - Credentials, tokens, or secrets discovered.
   - Findings / vulnerabilities and their evidence.

3. **Update per-host files.** For each host, append or update
   `data/knowledge-base/hosts/<ip>.md` (create it if missing). Keep a stable structure per host:
   ```
   # <ip>  (<hostnames>)
   ## Services
   | Port | Proto | Service | Version | Notes |
   ## Web
   ## Credentials
   ## Findings
   ## Notes
   ```
   Merge new facts in; do not duplicate rows that already exist. Note the source raw file next to
   facts so they are traceable.

4. **Update cross-host topic notes** where relevant — e.g. `data/knowledge-base/web.md`,
   `domain.md`, `credentials.md` — for facts that span hosts.

5. **Add an index row.** Append one row to `data/knowledge-base/INDEX.md`:
   ```
   | <YYYY-MM-DD> | <what it is> | data/raw/<file> | <host(s)> | <one-line summary> |
   ```

6. **Report** what was distilled: hosts touched, new findings, and anything that warrants a
   follow-up action (which still goes through plan → scope-check before running).

## Rules

- Never edit files in `data/raw/` — they are the evidence of record.
- Distill facts, not noise: capture what changes future decisions, drop boilerplate.
- Distilling is not testing. Any follow-up scan this suggests must go through the normal
  plan → `scope-check` → approval flow before it runs.
