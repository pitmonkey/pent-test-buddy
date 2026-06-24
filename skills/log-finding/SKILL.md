---
name: log-finding
description: Use when a vulnerability or issue has been confirmed during a pentest and should be recorded — "log a finding", "record this finding", "add a finding", or the operator runs /log-finding. Captures one finding in a consistent shape that feeds the report.
---

# Pen Test Buddy — Log a Finding

Record ONE confirmed finding into the `findings/` store in a consistent structure so
`pentest-report` can assemble it later. One file per finding. This records an already-confirmed
result — it does not run any test.

## Procedure

1. **Assign an id.** List `findings/F-*.md`, take the highest `F-<NNN>` and increment (zero-padded
   to 3 digits, starting `F-001`). If `findings/` is empty, use `F-001`.

2. **Gather the fields** (ask the operator for anything missing — do not invent severity or
   evidence):
   - `title` — short, specific (e.g. "Unauthenticated RCE in Jenkins script console").
   - `severity` — exactly one of: **Critical / High / Medium / Low / Info**.
   - `cvss` — optional vector/score if known.
   - `target` — affected host(s)/URL(s), concrete.
   - Evidence — the raw artifact path under `data/raw/...` and/or the relevant
     `evidence/command-log.md` time, that proves it.

3. **Write `findings/F-<NNN>-<slug>.md`** (slug = kebab-case of the title):
   ```markdown
   ---
   id: F-<NNN>
   title: <title>
   severity: <Critical|High|Medium|Low|Info>
   cvss: <vector or score, or omit>
   target: <host/url>
   status: open
   date: <YYYY-MM-DD>
   ---

   ## Summary
   <what it is, one paragraph>

   ## Affected
   <targets, endpoints, versions>

   ## Evidence
   <reference data/raw/<file> and/or evidence/command-log.md time — quote the key proof>

   ## Reproduction
   <numbered, exact steps/commands to reproduce>

   ## Impact
   <what an attacker gains; business impact>

   ## Remediation
   <concrete fix / mitigation>

   ## References
   <CVE, advisory, docs — optional>
   ```

4. **Cross-link the KB.** Add a one-line pointer under the host's `## Findings` section in
   `data/knowledge-base/hosts/<ip>.md`: `- F-<NNN> <title> (<severity>)`.

5. **Report** the id, title, and severity, and note that `status: open` until remediation is
   verified or the finding is reported.

## Rules

- Severity must be one of the five values — no ad-hoc labels.
- Every finding needs real evidence pointing at `data/raw/` or the command log. No evidence →
  say so and ask the operator; do not fabricate.
- Do not write secrets/credentials into the finding body in cleartext beyond what is needed to
  prove impact; reference where they are held instead.
