---
description: Search GitHub for public Claude Code skills and, only after you say OK, add one to this project.
---

# /find-skills

Help the student find public Claude Code skills on GitHub (folders with a `SKILL.md`) and, only if they agree, copy one into `.claude/skills/`. Follow the `find-skills` skill if it is available. If not, follow the steps below.

## Rules

1. Ask one question at a time. Plain words. No em dashes or en dashes.
2. Never install or copy a skill until the student says OK.
3. Only name a repo after you have checked it exists, with `gh` or `curl`.
4. Start with trusted collections: https://github.com/anthropics/skills and https://github.com/vercel-labs/agent-skills. Still verify them first.
5. Warn: only install from trusted sources, and read the `SKILL.md` first, because skills can run commands.

## Steps

1. Ask: "What do you want a skill to help you do?"
2. Search. If `gh` works:
   - `gh search code "filename:SKILL.md <topic>" --repo anthropics/skills --limit 10`
   - also `gh search code "filename:SKILL.md <topic>" --limit 10` and `gh search repos "<topic>" --topic claude-skills --sort stars --limit 10`
   If `gh` is missing, send them to:
   - https://github.com/search?q=filename%3ASKILL.md+TOPIC&type=code
   - https://github.com/search?q=topic%3Aclaude-skills+TOPIC&type=repositories
3. Verify each repo exists (`gh api repos/OWNER/REPO` or `curl -sI https://github.com/OWNER/REPO`) and that it has a `SKILL.md`. Skip anything you cannot verify.
4. Show the top 3, each with one plain line, the link, and the star count.
5. Warn them, open the chosen `SKILL.md`, summarise it, and wait for OK.
6. Only then copy the skill folder into `.claude/skills/<name>/`. Tell them to restart or reload Claude Code. Offer to save it to GitHub, and ask before any commit or push.
