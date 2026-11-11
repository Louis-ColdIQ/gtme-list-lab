---
description: Write a simple campaign report from a CSV or pasted numbers, with 3 next actions.
---

# /report

Turn the student's campaign numbers into a short report. Follow the `campaign-report` skill if it is available. If not, follow the steps below.

## Rules

1. Read `clients/<client>/client.md` first. Ask which client if it is not obvious.
2. One question at a time. Plain words. No em dashes or en dashes.
3. Only use numbers they give you. Never invent counts.
4. Out of office is not a real reply. Count people who actually wrote back.
5. Never ask them to paste API keys.

## Steps

1. Confirm the client, the campaign name, and the date range.
2. Ask them to point to a CSV export or paste totals: sent, bounced, replies, positive replies, meetings.
3. Calculate sent, bounce rate, reply rate, positive replies, and meetings. Show the working.
4. Write `clients/<client>/reports/YYYY-MM-DD.md` with the numbers, a short read of what they suggest, and 3 plain next actions.
5. Show the report, ask if it looks right, then offer to save it to GitHub. Ask before any commit or push.
