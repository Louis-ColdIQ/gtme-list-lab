---
name: handoff
description: >
  End a session by writing or updating clients/<client>/HANDOFF.md and a dated
  note in clients/<client>/sessions/. Use when the student says "handoff",
  "wrap up", "end the session", "we're done", types /handoff, or when a
  session of client work is finishing.
---

# Handoff

A handoff is a short note for the next session. It is how context carries over. Write it at the end of every session, even a short one.

## Rules

1. Plain words. Short sentences. No em dashes or en dashes.
2. Ask which client folder if it is not obvious.
3. Never invent work that did not happen. If something is unclear, put it under Open questions.
4. Do not include API keys, tokens, passwords, or personal emails.
5. Ask before creating or overwriting files, then ask before any git commit or push.

## Steps

1. Confirm the client folder (`clients/<slug>/`).
2. Skim `client.md` and today's files so the note is accurate.
3. Write or overwrite `clients/<slug>/HANDOFF.md` with this shape:

```markdown
# Handoff: <client name>
Updated: YYYY-MM-DD

## What we did
- ...

## Files created or changed
- path: one line on what changed

## Decisions
- ...

## What's next (top 3)
1. ...
2. ...
3. ...

## Open questions
- ...

## Start here next time
One or two sentences on the first thing to do.
```

4. Create `clients/<slug>/sessions/` if needed. Append a short entry to `clients/<slug>/sessions/YYYY-MM-DD.md` (create the file if it is new). Use today's date. If there is already an entry for today, add a new section rather than deleting the old one. Keep the dated note short: what we did, and what's next.
5. Show the student `HANDOFF.md` and ask: "Does this look right?"
6. Offer to save it to GitHub. Suggest a plain commit message like `Add session handoff for <slug>`. Ask before running commit or push.

## Tell them

"Next session, Claude will read client.md and this HANDOFF.md first, then pick up from the Start here line."
