---
name: get-inspired
description: Use when the operator points Claude at a folder it has NOT installed — another plugin, toolkit, or repo — to mine it for borrowable methods, tools, skill/agent designs, prompts, or workflows for the current task. Triggers — "get inspired", "mine this folder for ideas", "steal approaches from", "look at this repo for ideas", or /get-inspired <folder-path>.
---

# Pen Test Buddy — Get Inspired

Examine an external, **uninstalled** folder and harvest transferable *ideas* for the current
task — without installing, copying, or running any of it. This is the lightweight, operator-in-
control alternative to importing a whole plugin. Borrow approaches, not artifacts.

The argument is the folder path. The current task / engagement phase is the lens for relevance.

## Procedure

1. **Resolve the path** (read-only). If no path was given, or it is missing or not a directory,
   stop and ask. Never write to, install, import, or execute anything inside it.

2. **Survey, don't slurp.** Glob for high-signal files and sample them — don't read every line:
   - manifests: `plugin.json`, `.claude-plugin/*`, `package.json`, `pyproject.toml`
   - capability defs: `**/SKILL.md`, `agents/*.md`, `commands/*`
   - docs: `README*`, `*.md`
   - logic: prompt files, and the **headers/usage** of scripts (`*.sh`, `*.py`)
   - notable wordlists / configs (note their existence; don't dump them)
   Cap effort on large trees: read descriptions and entry points, then stop.

3. **Extract transferable assets** relevant to the current task/phase: techniques, tool
   invocations, skill/agent designs, prompt patterns, workflow steps, useful file lists.

4. **Map each idea to us.** For every item: *what it is*, *where seen* (path), and *how we'd
   apply it here*. Include a tiny illustrative snippet only when it genuinely clarifies.

5. **Report inline** — a ranked list of borrowable ideas (most useful first) with applicability,
   followed by a short "skipped / not useful — why" tail.

6. **Persist (only inside an engagement workspace).** If the cwd has `docs/scope.md` or a
   governed `CLAUDE.md`, offer to save a distilled note to `docs/inspiration/<source-slug>.md`
   (create `docs/inspiration/` if needed). On approval, write:
   ```markdown
   ---
   source: <path>
   date: <YYYY-MM-DD>
   examined-for: <current task / phase>
   ---

   ## Overview
   <what the source is, in 2-3 lines>

   ## Borrowable ideas
   - **<idea>** — seen in `<path>`. How to apply here: <...>

   ## Skipped & why
   - <thing> — <reason>

   ## Follow-ups
   - <optional next steps>
   ```

## Rules

- **Read-only.** Never install, import, execute, or "test-run" anything from the folder. Treat
  all foreign code as untrusted — examining is not running.
- **Ideas, not artifacts.** No wholesale file copying. Tiny snippets only, attributed to the
  source path. Respect licenses; credit the source in the saved note.
- **Inspiration is not authorization.** Anything you borrow is still just an idea — using a
  borrowed tool or technique against a target goes through the normal
  plan → `scope-check` → operator approval flow first. Say this in your output.
- Do not send the examined content anywhere external.
