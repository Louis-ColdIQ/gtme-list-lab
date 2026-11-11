---
name: copywriter
description: >
  Write short, plain cold emails from client.md and a campaign brief. Use when
  the student says "write the emails", "write copy", "cold email", "review my
  email", or after new-campaign.
---

# Copywriter

The copy is only as good as the context. Read the client and the brief, then write emails that sound like a person.

## Rules for every email

- Read `clients/<client>/client.md` and the brief in `campaigns/` first. Match the Tone section.
- Under 80 words in the body. Short sentences. Plain words.
- One idea per email and one ask, ending with a simple question.
- Subject line: 2 to 4 words, lowercase is fine, no hype, no spammy words (free!!!, guarantee, act now).
- Start with them, not us. No "I hope this finds you well". No "My name is".
- Use a variable like `{{first_name}}` and `{{company_name}}` so each email is personal.
- Only real proof from client.md. Never invent numbers or customers.
- No em dashes or en dashes. No exclamation marks.

## Steps

1. Ask which brief to write for (list files in `campaigns/`).
2. Write the 3 emails from the brief's sequence. For email 1, write 2 versions (A and B) with different first lines.
3. Check each email against the rules above. Count the words. Fix anything that breaks a rule.
4. Show the emails and ask: "Which version do you like, and what should change?"
5. Save to `clients/<client>/copy/<date>-<campaign-name>.md`.
6. Offer to save to GitHub.

## Example (Example Co)

Subject: rota on sundays

Hi {{first_name}},

Saw {{company_name}} is hiring baristas. When the team grows, the rota usually lives in a group chat and shifts get missed.

ShiftPal builds the week's rota in about 15 minutes. We set it up for you in one call, free for 30 days.

Worth a look for {{company_name}}?

Sam
