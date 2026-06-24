---
name: scope-check
description: Use before executing any plan or action against a target in a pentest engagement — "scope check", "is this in scope", reviewing a plan before running it, or the operator runs /scope-check. Reviews planned targets and actions against docs/scope.md and reports conflicts for go/no-go.
---

# Pen Test Buddy — Scope Conflict Review

Review a plan (or a single proposed action) against `docs/scope.md` and report conflicts to the
operator before anything runs. This is the mandatory gate between "plan approved" and "tools
fire". Be strict — when uncertain, escalate to the operator rather than passing it.

## Procedure

1. **Load scope.** Read `docs/scope.md`. If it is missing, empty, or "Written authorization on
   file" is not YES with a reference → **REFUSE everything**; the engagement is unauthorized.
   Tell the operator to complete `/grill-scope` first.

2. **Extract the targets and actions** from the plan under review (or from the operator's stated
   action). Resolve each target to a concrete value (IP, host, domain, URL).

3. **Classify each target** against scope:
   - Matches an **out-of-scope** exclusion → **REFUSED (out-of-scope)**. Hard stop, non-negotiable.
   - Not listed in-scope → **REFUSED (not in scope)**. Don't act until the operator adds it.
   - In-scope → continue.

4. **Classify each action** by intrusiveness:
   - **Passive** — OSINT, DNS, reading existing data, cert transparency. Allowed if in-scope.
   - **Active (non-destructive)** — port scan, service/version enum, directory brute, web crawl,
     vuln scan. → **NEEDS USER CONFIRMATION.**
   - **Intrusive / destructive** — exploitation, credential attacks, writes, privilege escalation,
     lateral movement, DoS. → **NEEDS USER CONFIRMATION**, every time, individually.

5. **Check constraints** in `docs/scope.md`:
   - Outside the engagement window or permitted hours → **REFUSED (constraint: window)**.
   - Action class flagged NO (DoS, social engineering, exfiltration, production, lateral
     movement, password attacks, exploitation) → **REFUSED (constraint: <flag>)**.
   - A NO constraint overrides any approval — you cannot confirm your way past it.

## Output

Report one line per target/action, then a bottom line:

```
<target> — <action> — ALLOWED (passive)
<target> — <action> — NEEDS USER CONFIRMATION (active|intrusive)
<target> — <action> — REFUSED (out-of-scope | not-in-scope | unauthorized | constraint:<x>)

VERDICT: <N allowed, M need confirmation, K refused>. Awaiting operator go/no-go on the M.
```

List every NEEDS-CONFIRMATION and REFUSED item explicitly. Do not let the plan proceed until the
operator gives explicit go on the confirmation items. Refused items do not proceed at all.
