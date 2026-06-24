#!/usr/bin/env python3
"""Pen Test Buddy command-log hook.

PostToolUse(Bash) hook. Appends an audit-trail row to <engagement>/evidence/command-log.md
for every Bash command run inside an engagement workspace. Inert everywhere else.

Hard rules: never block, never raise, always exit 0. The log is a chain-of-custody index,
not a replacement for raw artifacts (those still go to data/raw/).
"""
import sys
import os
import json
import datetime


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)  # may raise -> caught below

    cwd = data.get("cwd") or os.getcwd()

    # Guard: only log inside an engagement workspace.
    is_engagement = os.path.isfile(os.path.join(cwd, "docs", "scope.md")) or os.path.isdir(
        os.path.join(cwd, "data", "knowledge-base")
    )
    if not is_engagement:
        return

    command = (data.get("tool_input") or {}).get("command")
    if not command:
        return

    # Short result summary from the tool response (string or dict, possibly large).
    resp = data.get("tool_response")
    if isinstance(resp, dict):
        resp = resp.get("stdout") or resp.get("output") or resp.get("content") or ""
    result = _cell(str(resp or ""), 80)

    cmd_cell = _cell(command, 200)
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    log = os.path.join(cwd, "evidence", "command-log.md")
    os.makedirs(os.path.dirname(log), exist_ok=True)
    if not os.path.exists(log):
        with open(log, "w") as f:
            f.write(
                "# Command Log\n\n"
                "Automatic chain-of-custody record of every Bash command run in this "
                "engagement workspace (appended by the Pen Test Buddy command-log hook). "
                "Full tool output still belongs in `data/raw/`.\n\n"
                "| UTC time | Command | Result (truncated) |\n"
                "|----------|---------|--------------------|\n"
            )
    with open(log, "a") as f:
        f.write(f"| {ts} | {cmd_cell} | {result} |\n")


def _cell(text, limit):
    """Collapse to one line, escape table pipes, truncate for a markdown cell."""
    text = " ".join(text.split())
    text = text.replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return text


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # never disrupt the session
    sys.exit(0)
