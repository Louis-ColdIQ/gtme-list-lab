# Client HQ: how this project works

This folder is a small "client HQ". It gives you (Claude) the context you need to do outbound work for one client: who they sell to, what they sell, and how they sound. Good context in, good work out.

## The student

The person you are helping is a beginner. Use plain words and short sentences. Explain what a command does in one sentence before you run it. Ask one question at a time and wait for the answer. Always ask before running a command.

## The golden rule: read the client first

At the start of every session, run `/client` (it does the steps below and gives a short brief). If the student did not run it, do it for them:

1. Find the client folder in `clients/` (ask which one if there is more than one real client).
2. Read `clients/<client>/client.md` in full.
3. If `clients/<client>/HANDOFF.md` exists, read it too, and start from the "Start here next time" line.
4. If `client.md` does not exist yet, run the `new-client` skill first. Do not guess the ICP or offer.

At the end of every session, always run `/handoff` (the `handoff` skill). Do this even if the session was short.

If the student asks how a cold outbound system works, or how Clay, Instantly, APIs, or Supabase fit together, read `context/outbound-system.md` and explain it in plain words. Do not skip ahead and build Level 3 or 4 unless they ask.

`clients/_template/` is the blank template. `clients/example-co/` is a made up example to learn from. Never do real work in either.

## Where things go

```
clients/<client>/
  client.md     who they sell to, the offer, proof, tone, who to skip
  HANDOFF.md    last session notes, so the next session can pick up
  sessions/     one dated note per session
  lists/        companies.csv and people.csv
  campaigns/    campaign briefs
  copy/         email copy
  reports/      simple campaign reports
```

Always save outputs inside the client folder. Never overwrite a file without asking. Add the date to file names, for example `lists/2026-11-11-companies.csv`.

## Skills (in `.claude/skills/`)

| Skill | Use it to |
|---|---|
| connect-github | install Git, sign in to GitHub, save work to GitHub |
| find-skills | search GitHub for public Claude Code skills and add one (optional) |
| new-client | interview the student and write `client.md` |
| offer-builder | tighten the offer in `client.md` and give 3 one-line variants |
| connect-clay | install and sign in to the Clay CLI (optional) |
| list-builder | build a company list and a people list |
| new-campaign | turn `client.md` plus a list into a campaign brief |
| copywriter | write short cold emails from `client.md` and the brief |
| campaign-report | write a simple report from a CSV or pasted campaign numbers |
| connect-supabase | save lists into a free Supabase database (optional) |
| handoff | write a session handoff so the next session can pick up |

Every session starts with `/client` and ends with `/handoff`.

Usual order: connect-github, then optionally find-skills, then new-client, offer-builder, list-builder, new-campaign, copywriter, then `/handoff`. Use `/report` later, once they have numbers from a sending tool. Use the matching skill whenever the student's request fits one.

## Hard rules

- Never guess, invent, or pattern match emails or phone numbers. If the student uses their own Clay account to enrich, that is their call, and it happens inside Clay.
- Never print or save API keys, tokens, or passwords. Secrets go in `.env`, which git ignores.
- No em dashes or en dashes in anything you write. Use commas, full stops, or brackets.
- Keep it free by default. Say clearly before anything that could cost money or credits.
- When work is done, run `/handoff`, then offer to save it to GitHub (commit and push) with the connect-github skill.
