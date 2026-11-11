---
name: campaign-report
description: >
  Turn pasted or exported campaign numbers into a short report with sent,
  bounce rate, reply rate, positive replies, meetings, and 3 next actions.
  Use when the student says "report", "how did the campaign do", "campaign
  numbers", or types /report. Works from a CSV or from numbers they paste.
---

# Campaign report

A simple report from numbers the student already has. They export a CSV from their sending tool, or paste a few totals. You do the sums, write a short markdown file, and suggest 3 next actions. This is a beginner report, not a live dashboard.

## Rules

1. Read `clients/<client>/client.md` first. Ask which client if it is not obvious.
2. One question at a time. Plain words. No em dashes or en dashes.
3. Only use numbers the student gives you. Never invent sent, bounce, reply, or meeting counts.
4. If a number is missing, write `unknown` and skip that rate.
5. Out of office is not a real reply. Count only messages a person actually wrote. If the student is not sure, keep replies and positive replies separate and say the reply number may include automatic messages.
6. Never ask them to paste API keys. This skill reads a file or pasted numbers, nothing else.

## What to collect

Ask which campaign (or date range) this is for, then ask for numbers in one of these ways:

- A CSV they exported from their sending tool, saved under the client folder (for example `clients/<client>/reports/raw.csv`).
- Or they paste totals: sent, bounced, replies, positive replies, meetings.

If they give a CSV, look for columns that mean sent, bounced, replies, positive or interested, and meetings. Column names vary by tool, so confirm your mapping with them before you calculate. If a row is a person, count people, not repeated events, when you can.

## How to calculate

- **Sent:** total emails sent.
- **Bounce rate:** bounced / sent, as a percentage to 1 decimal place. (If sent is 0, write `unknown`.)
- **Reply rate:** replies / sent, as a percentage to 1 decimal place. Replies here means people who wrote back.
- **Positive replies:** people who asked a next step (a call, the price, more details) or agreed to one.
- **Meetings:** meetings booked.

Show the working in one short line each, so they can see how you got the rate.

## Steps

1. Confirm the client folder.
2. Ask for the campaign name and the date range, then for a CSV path or pasted totals.
3. Confirm which columns or totals you will use. Then calculate.
4. Draft 3 plain next actions from the numbers. Keep them generic and useful, for example:
   - Bounce rate over about 3%: check domain setup and list quality before sending more.
   - Reply rate is low: review the offer in `client.md` and whether the list matches the ICP.
   - Replies exist but few are positive: tighten the offer and the ask in the first email.
   - Positive replies but few meetings: follow up the interested people first, and make the next step clearer.
   - Volume is still small: do not change everything yet, send a bit more and report again.
5. Create `clients/<client>/reports/` if needed. Save to `clients/<client>/reports/YYYY-MM-DD.md` (use today's date, or the last day of the range they gave). If that file already exists, ask before overwriting, or add a new section.
6. Show the report and ask: "Does this look right?"
7. Offer to save it to GitHub with connect-github (commit and push).

## Report template

```markdown
# Campaign report
Client: <client>  |  Campaign: <name>  |  Dates: <range>  |  Report date: YYYY-MM-DD

## Numbers
- Sent:
- Bounced:  (bounce rate: )
- Replies:  (reply rate: )
- Positive replies:
- Meetings:

## How I counted
- One or two lines on the source (CSV or pasted totals) and any missing numbers.

## What this suggests
- Two or three short observations, in plain words.

## Next actions
1.
2.
3.
```
