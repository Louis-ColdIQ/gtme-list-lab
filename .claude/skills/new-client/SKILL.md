---
name: new-client
description: >
  Interview the student about a client (or their own business) and write
  clients/<slug>/client.md. Use when the student says "new client", "set up my
  client", "write my client.md", or when list, campaign, or copy work starts and
  no client.md exists yet.
---

# New client

`client.md` is the context file. Every other skill reads it first, so the better it is, the better the lists and emails get. Your job is to fill it in by interviewing the student.

## Rules

1. One question at a time. Wait for the answer.
2. Plain words. Give a short example answer with each question (use `clients/example-co/client.md` for ideas).
3. Never invent proof, customers, or numbers. If they do not know, write `unknown` and move on.
4. No em dashes or en dashes.

## Steps

1. Ask for the client name and website. Make a slug: lowercase, hyphens, for example `acme-plumbing`.
2. Check `clients/<slug>/` does not exist. If it does, ask whether to update it instead.
3. Copy the template: `clients/_template/client.md` to `clients/<slug>/client.md`, and create `lists/`, `campaigns/`, `copy/` inside it.
4. If they gave a website, offer to read it (free web fetch) and draft the Basics and Offer sections. Show the draft and ask what to fix.
5. Go through the sections in order: ICP, Offer, Proof, Tone, Exclusions. One question per bullet, but skip any bullet already answered.
6. Write the file. Show the finished `client.md` and ask: "Anything wrong or missing?"
7. Tell them: "This file is now Claude's memory for this client. Next we can build a list with list-builder."
8. Offer to save it to GitHub with connect-github (commit and push).
