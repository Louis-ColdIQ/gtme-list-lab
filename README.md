# GTME Client HQ (starter)

A starter "client HQ" for doing outbound with Claude Code. The idea is simple: **context in, good work out.** You write down who your client is once (`client.md`), and every skill reads it before building a list, a campaign, or an email. Start every session with `/client` to load your client and its context, and end it with `/handoff`, so the next session can pick up where you left off.

- **Claude Code** does the work, using the skills in `.claude/skills/`.
- **GitHub** saves your HQ (context, lists, copy) so nothing gets lost.
- **Supabase** (optional) is the company brain for your data.
- **Clay** (optional) gives Claude real company and people data through the Clay CLI.

For the bigger picture (ICP, Clay, Instantly, APIs, reporting, and a Level 1 to 4 roadmap), read `context/outbound-system.md`.

## 5 minute setup

1. Install Claude Code (needs a paid Claude plan). Mac/Linux terminal:
   `curl -fsSL https://claude.ai/install.sh | bash`
   Then run `claude` and sign in.
2. Paste the prompt below into Claude Code. It clones this repo and walks you through the rest.
3. Optional: connect Clay with the `connect-clay` skill (needs a Clay account, free is fine).

## The paste prompt

```
Clone https://github.com/Louis-ColdIQ/gtme-list-lab into a new folder on my computer, then open that folder as the project and read CLAUDE.md. I am a beginner. Run these skills in order: connect-github, then new-client to write my client.md, then offer-builder, then list-builder (use Clay if I have connected it with connect-clay, otherwise free public web research), then new-campaign, then copywriter. Ask one question at a time, explain each step in plain words, and wait for my OK before running any command. Never guess or invent emails or phone numbers. Save everything in my client's folder. At the end, run /handoff.
```

(Also in `PROMPT.txt`.)

## What is inside

```
CLAUDE.md                 how the HQ works (Claude reads this first)
context/outbound-system.md  how a cold outbound system fits together
clients/
  _template/client.md     blank client file
  example-co/client.md    a made up example to learn from
.claude/commands/
  client.md               type /client at the start of every session to load a client
  find-skills.md          type /find-skills to search GitHub for extra skills
  offer.md                type /offer to tighten the offer in client.md
  report.md               type /report to write a simple campaign report
  handoff.md              type /handoff at the end of every session
.claude/skills/
  connect-github/         install Git, sign in, save your work
  find-skills/            search GitHub for public skills and add one
  new-client/             interview you and write client.md
  offer-builder/          tight offer plus 3 one-line variants
  connect-clay/           install and sign in to the Clay CLI
  list-builder/           company and people lists (Clay or free web)
  new-campaign/           campaign brief: angle, segments, sequence
  copywriter/             short, plain cold emails
  campaign-report/        simple report from a CSV or pasted numbers
  connect-supabase/       optional database for your lists
  handoff/                write a session handoff for next time
examples/                 sample CSVs and a list plan
outputs/                  scratch space
```

## The flow

1. **connect-github**: Git works and the HQ is on your computer.
2. **/find-skills** (optional): search GitHub for extra public skills and add one you trust.
3. **new-client**: Claude interviews you and writes `clients/<you>/client.md`.
4. **offer-builder**: tighten the offer (dream outcome, result, timeframe, a safe first step) and pick from 3 one-line variants.
5. **list-builder**: 10 to 20 companies and up to 2 people each, saved as CSVs.
6. **new-campaign**: a short brief with the angle and a 3 email sequence.
7. **copywriter**: the emails, under 80 words each.
8. **/handoff**: write `HANDOFF.md` so the next session can pick up.
9. Save to GitHub. Optional: load the lists into Supabase.
10. Later, **/report**: paste or export campaign numbers for a simple report.

Coming back for another session? Type **/client** first. It loads `client.md`, your last `HANDOFF.md` and your files, gives you a short brief, and asks where to pick up.

## Your homework

Run the paste prompt for a real client (or your own business). Finish with a `client.md` (including a tight offer), one list, one campaign brief, 3 emails, and a `/handoff`, pushed to your own GitHub.

## Ground rules

- Never guess emails or phone numbers. If you want contact data, enrich in your own Clay account.
- Never commit API keys. Secrets go in `.env`, which is ignored.
- Start small. A good list of 15 beats a bad list of 1,000.
