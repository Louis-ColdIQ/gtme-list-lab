---
name: offer-builder
description: >
  Interview the student and write a tight, Mafia Offer style offer into the
  Offer section of clients/<client>/client.md, plus 3 one-line variants. Use
  after new-client and before list-builder, or when the student says "mafia
  offer", "build my offer", "make the offer stronger", or types /offer.
---

# Offer builder

A Mafia Offer is an offer so good the buyer feels stupid saying no. The product does not need to change. The offer does: a clear dream outcome, a specific result, a timeframe, a way to take the risk off the buyer, and a small first step. A strong offer with average copy beats a weak offer with perfect copy.

This skill tightens the `## Offer` section in `client.md`. Run it after `new-client` and before `list-builder`. Later skills (list, campaign, copy) will read what you write here.

## Rules

1. Read `clients/<client>/client.md` first. Ask which client if it is not obvious. If there is no `client.md`, run `new-client` first.
2. One question at a time. Wait for the answer. Give a short made up example with each question (coffee shop, staff scheduling, and similar is fine).
3. Never invent proof, customers, numbers, or guarantees. If they do not have one, write `unknown` and say so.
4. Do not put a price in the outreach offer. Price belongs on a call, not in a cold email.
5. The smaller the first ask, the easier it is to reply. A free, fast, no-call first step beats "book a 30 minute demo".
6. No em dashes or en dashes.

## What to collect

Ask only the questions that `client.md` does not already answer clearly. If an answer is vague, ask once more with an example.

1. **What do they actually sell?** The product or service, in plain words.
2. **Who is the buyer?** Job title and company type.
3. **Dream outcome.** What does that buyer want to be true when this works?
4. **Specific result and timeframe.** Not "more sales". A number and a window, for example "3 extra bookings in 30 days". If they do not have a number, help them pick an honest, modest one, or write `unknown`.
5. **What can they give away or guarantee without it hurting?** A free audit, a sample, a short teardown, a trial you set up for them, or a simple guarantee. This is usually what makes the offer feel safe. If they cannot think of anything, say so: most weak offers are weak because there is nothing to give and the buyer takes all the risk.
6. **How little does the buyer have to do?** Keep the first step small (a yes or no, a reply, a 10 minute setup).
7. **What real proof do they have?** A customer, a result, years in the work, or a relevant project. Never invent this.

## The offer is ready when

Check these out loud and name any that fail:

1. Specific result plus a timeframe (or an honest `unknown`).
2. The buyer can picture the steps. No black box.
3. Real proof, even a small one.
4. Risk sits with the seller (a free first step, a trial, or a guarantee).
5. The first ask is small and relevant to this buyer, not a generic pitch.

## Steps

1. Confirm the client folder and read `client.md`.
2. Interview with the questions above, one at a time.
3. Draft the `## Offer` section (replace the existing one, keep the rest of the file). Use this shape:

```markdown
## Offer
- The main problem they solve:
- Dream outcome:
- Specific result and timeframe:
- Risk reversal or guarantee:
- What the buyer has to do (keep this small):
- The offer for cold outreach (one sentence):
- Offer variants:
  1. <outcome plus timeframe plus the safe first step>
  2. <proof led, still a small ask>
  3. <shortest version, one line, easy to paste into an email>
```

4. Show the draft and the 3 one-line variants. Ask: "Which variant is the main one, and what should we change?"
5. Write the section into `client.md`. Remind them this is now the offer that list-builder, new-campaign, and copywriter will use.
6. Offer to save it to GitHub with connect-github (commit and push).
