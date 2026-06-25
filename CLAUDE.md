# Pen Test Buddy — Repo Guide (for working ON the plugin)

This repo IS the source of the **pent-test-buddy** Claude Code plugin. Editing here changes the
plugin's behavior. It is **not** an engagement workspace — do not run pentests or scaffold
engagement data in this directory.

> Two different `CLAUDE.md` files exist, don't confuse them:
> - **This file** — guides developing the plugin.
> - **`templates/engagement-CLAUDE.md`** — the governed-workflow file the `pentest-init` skill
>   copies into an operator's *engagement* directory. That one is the highest-value artifact;
>   edit it deliberately and never water down its `<HARD-GATE>`.

## What the plugin does

Turns an empty directory into a scope-governed penetration-testing workspace and keeps Claude
inside the Rules of Engagement. Headline idea: a `data/raw/` → `data/knowledge-base/`
distillation pipeline so Claude reads what it already learned instead of re-scanning.

## Layout

```
.claude-plugin/plugin.json      plugin manifest (name, version, author, keywords)
.claude-plugin/marketplace.json single-plugin marketplace for `/plugin marketplace add`
skills/<name>/SKILL.md          one skill per dir; name auto-derives the slash command
hooks/hooks.json                auto-discovered hook config (PostToolUse → Bash)
hooks/command-log.py            the command-log hook implementation
templates/                      files pentest-init copies into an engagement dir
README.md                       operator-facing plugin overview + install
```

Skills (8): `pentest-init`, `grill-scope`, `scope-check`, `kb-distill`, `log-finding`,
`pentest-report`, `cleanup-tracker`, `get-inspired`. Hook (1): command-log.

## Conventions

**Authoring skills** (follow `superpowers:writing-skills`):
- Frontmatter `name` (hyphens, ≤64 chars, matches the dir) + `description`.
- `description` = **triggering conditions only**, no workflow summary — otherwise agents act on
  the description instead of reading the body. Pack it with concrete trigger phrases + the slash
  form.
- Keep bodies tight and imperative. Numbered procedure + a hard **Rules** section.

**Templates & placeholders:**
- `pentest-init` copies `templates/*` into the engagement dir and substitutes `{{ENGAGEMENT_NAME}}`
  and `{{DATE}}` (sed-style). If you add a placeholder, update the copy/fill step in
  `skills/pentest-init/SKILL.md`. Keep template headers in sync where two paths create the same
  file (e.g. `templates/command-log.md` must match the header `hooks/command-log.py` writes
  lazily).
- Init is idempotent: never overwrite an existing `docs/scope.md` or `CLAUDE.md`.

**The command-log hook (`hooks/command-log.py`):**
- PostToolUse/Bash. **Guarded** to engagement dirs only (`docs/scope.md` or `data/knowledge-base/`
  present), else `exit 0`. Must **never block, never raise, always `exit 0`** — it is an audit
  trail, not a gate. Writes two files per command: `evidence/command-log.md` (truncated table,
  escapes `|` for cells) and `evidence/command-log.jsonl` (full untruncated PostToolUse payload +
  a `logged_at` timestamp, one JSON object per line). Only the `.md` has a templated header; the
  `.jsonl` is lazily created with no template.

**Safety posture (this is offensive-security tooling):**
- The whole point is enforcing authorization. Don't weaken the scope gate, the
  superpowers-planning requirement, or the "out-of-scope = hard stop" rule.
- `get-inspired` is read-only and must stay that way: never install/run/copy foreign code.

## Testing changes

No unit suite — skills/templates are prompt artifacts. Validate mechanically:
- JSON parses: `python3 -c "import json;json.load(open('.claude-plugin/plugin.json'))"` (and
  `marketplace.json`, `hooks/hooks.json`).
- Hook compiles + behaves: `python3 -m py_compile hooks/command-log.py`; pipe fake PostToolUse
  JSON in/out of an engagement dir and assert it logs only inside one (both `command-log.md` and
  a valid, untruncated `command-log.jsonl` line) and exits 0 on malformed input.
- Scaffold sim: in a temp dir, `sed`-fill the templates as `pentest-init` describes; assert the
  tree, no leftover `{{...}}`, and idempotent re-run.
- Every new skill: assert `name:`/`description:` frontmatter and that the dir name matches.

## Install (for live testing)

```
/plugin marketplace add /path/to/pent-test-buddy
/plugin install pent-test-buddy
```

Requires the `superpowers` plugin (hard dependency — `pentest-init` stops without it).

## Roadmap

Passive recon subagent, optional shared resource library — not yet built.
