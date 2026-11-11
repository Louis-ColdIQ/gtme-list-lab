---
name: new-campaign
description: >
  Turn a client's client.md and a list into a simple campaign brief: the angle,
  the segments, and a sequence outline. Use when the student says "new campaign",
  "plan a campaign", "what should we send", or after list-builder.
---

# New campaign

A campaign brief is the plan before the copy. It says who we email, why they should care, and what we send, in what order.

## Rules

1. Read `clients/<client>/client.md` and the latest list in `clients/<client>/lists/` first.
2. One question at a time. Show a draft, then ask what to change.
3. Only use proof that is in client.md. Never invent results.
4. No em dashes or en dashes.

## Steps

1. Ask: "Which list is this campaign for?" (show the files in `lists/`).
2. Pick 1 or 2 segments from the list, for example by job title or a fit signal. Keep it simple.
3. For each segment write:
   - **Who**: titles and company type
   - **Problem**: the one pain they most likely have (from client.md)
   - **Angle**: why now, why us, in one sentence
   - **Offer**: the low risk ask from client.md
   - **Proof**: the best real proof point
4. Sequence outline, 3 emails:
   - Email 1 (day 1): problem plus offer, one question
   - Email 2 (day 3): proof or a short story
   - Email 3 (day 7): short and polite last nudge
5. Write a one line hypothesis: "We think <segment> will reply because <reason>."
6. Save to `clients/<client>/campaigns/<date>-<campaign-name>.md`.
7. Say: "Next, copywriter can write the emails from this brief." Offer to save to GitHub.

## Brief template

```markdown
# Campaign: <name>
Client: <client>  |  List: lists/<file>  |  Date: <date>

## Hypothesis
We think <segment> will reply because <reason>.

## Segment 1
- Who:
- Problem:
- Angle:
- Offer:
- Proof:

## Sequence
1. Day 1:
2. Day 3:
3. Day 7:
```
