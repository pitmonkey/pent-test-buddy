---
name: find-skills
description: Use when the operator wants to discover an existing Claude skill or subagent for a capability — "find a skill for X", "is there a skill/subagent that does X", "search github for a skill", "who's good at X", or /find-skills <capability>. Searches GitHub and recommends; does not install.
---

# Pen Test Buddy — Find Skills

Search GitHub for existing skills and subagents that are good at a given capability, verify them,
and recommend. **Discovery only** — this finds and recommends; it never installs or runs anything.
It is the remote-discovery counterpart to `get-inspired` (which mines a local folder).

The argument is the capability/topic (e.g. `azure graph api`). Use the current task as the lens.

## Procedure

1. **Take the capability.** If no topic was given, ask for one.

2. **Search GitHub — `gh` preferred** (authenticated `gh` avoids rate limits):
   ```bash
   gh search code --filename SKILL.md "<topic>" --limit 20
   gh search code "<distinctive term>" --filename SKILL.md --limit 20   # e.g. graph.microsoft.com
   gh search code --filename "*.md" "<topic>" "subagent" --limit 15     # subagents
   gh search repos "<topic> claude skill OR subagent" --limit 15
   ```
   A concrete API host / CLI name / keyword as the "distinctive term" cuts noise hard. Also scan
   known catalogs: `VoltAgent/awesome-claude-code-subagents`, `VoltAgent/awesome-agent-skills`,
   `MicrosoftDocs/Agent-Skills`, and vendor plugin repos. Use `WebSearch` to surface
   catalog/marketplace repos that code search misses.

3. **Verify each candidate is real, not just a mention.** It must have skill/agent frontmatter
   (`name:` + `description:`). Fetch and check:
   ```bash
   gh api repos/<owner>/<repo>/contents/<path> --jq .content | base64 -d | head -40
   ```
   (or `raw.githubusercontent.com`). Skim for substance — real endpoints/commands, not a stub.

4. **Rank** on: maintained (official org / stars / recent commits) · real frontmatter · substance
   · license · fit. Note caveats: non-English, narrow scope, stale, no license.

5. **Report — top pick + adaptive split:**

   ### Top pick
   The single best "just good at `<topic>`" skill or subagent — `owner/repo` · path · one-line
   why · caveat.

   ### By angle (adaptive)
   - **Security topic** → a **Defensive** pick and an **Offensive** pick.
   - **Otherwise** → **Official / maintained** vs **Lightweight / community**.
   - Omit a bucket if nothing real fills it — say so, don't pad.

   Each entry: `owner/repo` · path · skill-or-subagent · one-line capability · caveat.

6. **Handoff line.** Say how to adopt: `/plugin marketplace add` + `/plugin install` (an operator
   action — Claude cannot run `/plugin`), **or** clone a copy and run `/get-inspired` on it to
   borrow ideas. Nothing is auto-adopted.

7. **Persist (in-engagement only).** If the cwd has `docs/scope.md` or a governed `CLAUDE.md`,
   offer to save to `docs/skills-found/<topic-slug>.md` (create the dir lazily). Frontmatter:
   `topic, date`; body = top pick + buckets + source links.

## Rules

- **Discovery only.** Never `/plugin install` (Claude can't) and never clone-and-execute a found
  repo to "try it". Recommending is not adopting.
- **Verify before recommending.** Real frontmatter + an actual look at the content; flag caveats
  (language, license, maintenance, scope) rather than burying them. No hallucinated repos — every
  pick is a URL that was actually fetched.
- End web-derived findings with the **source links** used.
- Anything later adopted still runs under the normal engagement rules
  (plan → `scope-check` → approval) before use against a target.

## Dependency / fallback

Prefers the authenticated `gh` CLI. If `gh` is missing or unauthenticated, fall back to
`WebSearch` + `WebFetch` against `github.com/search` and `raw.githubusercontent.com`. State which
path you used.
