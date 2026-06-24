---
name: grill-scope
description: Use when defining or refining the Rules of Engagement / scope for a penetration test — "grill me for scope", "set up scope", "define the engagement", filling out docs/scope.md, or the operator runs /grill-scope. Interrogates the operator relentlessly about targets, authorization, and rules before any testing.
---

# Pen Test Buddy — Grill the Scope

Interview the operator relentlessly, one question at a time, until `docs/scope.md` is complete
and unambiguous. This is the gate that makes every later action safe — do not rush it, do not
fill blanks with assumptions, and do not let the operator hand-wave a "trust me, it's fine".

**Behaves like `claude-dev-skills:grill-me`, tuned for pentest scope.** Walk down each branch of
the scope tree, resolving dependencies one by one. If a question can be answered by reading an
existing file (a contract, an authorization email in the workspace), read it instead of asking.

## Procedure

1. Read the current `docs/scope.md`. If it does not exist, tell the operator to run
   `/pentest-init` first, then stop.
2. Ask questions **one at a time**. After each answer, write it straight into the matching
   section of `docs/scope.md`. Prefer multiple-choice when the answer space is small
   (e.g. "DoS allowed? yes / no").
3. Push back on anything vague. "The internal network" is not a scope — get CIDRs. "Should be
   fine" is not authorization — get a reference.

## Question bank (cover every item)

**Authorization (do this first — everything else is moot without it):**
- Is there written authorization on file? What is the reference (contract / email / ticket)?
- Who authorized it (name + role)? Do they own or control the in-scope systems?

**Targets:**
- Exact in-scope targets: IPs, CIDRs, hostnames, domains, URLs. Enumerate them.
- Exact out-of-scope exclusions: hosts, subnets, third-party/shared services, anything off-limits.
- Any host that is in a listed CIDR but must NOT be touched?

**Window & constraints:**
- Engagement start and end (date/time + timezone).
- Permitted testing hours (24x7? business hours only? avoid a change window?).
- Rate limits or fragile systems to go gently on?

**Allowed action classes (ask each explicitly — default each to NO until confirmed):**
- Denial of service / stress testing? Social engineering? Phishing?
- Data exfiltration? Are production systems in scope?
- Lateral movement? Password / credential attacks? Exploitation (actually gaining access)?

**Contacts / emergency stop:**
- Primary and secondary contacts (name, phone, email).
- How does the client call it off, and what do we do when they do?

## Rules

- **Do not set "Written authorization on file" to YES without a real reference.** No reference,
  it stays NO and the engagement is unauthorized — no testing.
- Treat every unanswered item as a blocker, not a default. Keep grilling until the section is
  filled or the operator explicitly marks it not-applicable.
- When `docs/scope.md` is complete, summarize the scope back to the operator in a few lines and
  ask them to confirm it matches their authorization.
- You are filling scope, not testing. Do not run anything against a target from this skill.
