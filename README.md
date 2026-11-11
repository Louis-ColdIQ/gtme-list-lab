# GTME Client HQ (starter)

A starter "client HQ" for doing outbound with Claude Code. The idea is simple: **context in, good work out.** You write down who your client is once (`client.md`), and every skill reads it before building a list, a campaign, or an email.

- **Claude Code** does the work, using the skills in `.claude/skills/`.
- **GitHub** saves your HQ (context, lists, copy) so nothing gets lost.
- **Supabase** (optional) is the company brain for your data.
- **Clay** (optional) gives Claude real company and people data through the Clay CLI.

## 5 minute setup

1. Install Claude Code (needs a paid Claude plan). Mac/Linux terminal:
   `curl -fsSL https://claude.ai/install.sh | bash`
   Then run `claude` and sign in.
2. Paste the prompt below into Claude Code. It clones this repo and walks you through the rest.
3. Optional: connect Clay with the `connect-clay` skill (needs a Clay account, free is fine).

## The paste prompt

```
Clone https://github.com/Louis-ColdIQ/gtme-list-lab into a new folder on my computer, then open that folder as the project and read CLAUDE.md. I am a beginner. Run these skills in order: connect-github, then new-client to write my client.md, then list-builder (use Clay if I have connected it with connect-clay, otherwise free public web research), then new-campaign, then copywriter. Ask one question at a time, explain each step in plain words, and wait for my OK before running any command. Never guess or invent emails or phone numbers. Save everything in my client's folder.
```

(Also in `PROMPT.txt`.)

## What is inside

```
CLAUDE.md                 how the HQ works (Claude reads this first)
clients/
  _template/client.md     blank client file
  example-co/client.md    a made up example to learn from
.claude/skills/
  connect-github/         install Git, sign in, save your work
  new-client/             interview you and write client.md
  connect-clay/           install and sign in to the Clay CLI
  list-builder/           company and people lists (Clay or free web)
  new-campaign/           campaign brief: angle, segments, sequence
  copywriter/             short, plain cold emails
  connect-supabase/       optional database for your lists
examples/                 sample CSVs and a list plan
outputs/                  scratch space
```

## The flow

1. **connect-github**: Git works and the HQ is on your computer.
2. **new-client**: Claude interviews you and writes `clients/<you>/client.md`.
3. **list-builder**: 10 to 20 companies and up to 2 people each, saved as CSVs.
4. **new-campaign**: a short brief with the angle and a 3 email sequence.
5. **copywriter**: the emails, under 80 words each.
6. Save to GitHub. Optional: load the lists into Supabase.

## Your homework

Run the paste prompt for a real client (or your own business). Finish with a `client.md`, one list, one campaign brief, and 3 emails, pushed to your own GitHub.

## Ground rules

- Never guess emails or phone numbers. If you want contact data, enrich in your own Clay account.
- Never commit API keys. Secrets go in `.env`, which is ignored.
- Start small. A good list of 15 beats a bad list of 1,000.
