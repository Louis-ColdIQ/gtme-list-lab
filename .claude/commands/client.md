---
description: Start a session by loading one client and all of its context. Run this first, every time.
argument-hint: "[client folder name, optional]"
---

# /client

Use this at the start of every session or new project. It loads the client you are working on so Claude has the full context before doing anything.

## Rules

1. Plain words. Short sentences. No em dashes or en dashes.
2. Read only. Do not create, change, or delete files in this step.
3. Never print API keys, tokens, or passwords, even if you see them.
4. Never do real work in `clients/_template/` or `clients/example-co/`.

## Steps

1. If the student typed a name after `/client` (for example `/client acme`), use `clients/<name>/`. If not, list the folders in `clients/` (skip `_template`) and ask: "Which client are we working on today?" If there are no real clients yet, say so and offer to run the `new-client` skill.
2. If the folder does not exist, say so, show the closest match, and ask. If `client.md` is missing, offer to run `new-client`. Do not guess the ICP or offer.
3. Read in this order:
   - `clients/<name>/client.md` in full
   - `clients/<name>/HANDOFF.md` if it exists
   - the newest file in `clients/<name>/sessions/`
   - the file names in `lists/`, `campaigns/`, `copy/`, and `reports/` (open the newest one in each only if it helps)
4. Give the student a short brief, no more than 10 lines:

```
Client: <name>, <one line on what they sell>
Who we target: <ICP in one line>
Offer: <offer in one line>
Last session: <date and one line, or "first session">
What we have: <N lists, N campaigns, N copy files, N reports>
Next up: <the "Start here next time" line, or the next skill in the usual order>
Open questions: <from HANDOFF.md, or "none">
```

5. Ask: "Want to pick up from there, or work on something else?" Wait for the answer.
6. Remember this client for the rest of the session. Save every output inside `clients/<name>/`. At the end, run `/handoff` for this same client.

## Tell them

"Start every session with /client and end it with /handoff. That is how Claude remembers your client between sessions."
