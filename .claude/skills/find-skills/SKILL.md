---
name: find-skills
description: >
  Help a beginner search GitHub for public Claude Code skills (folders
  with a SKILL.md) and, only after they say OK, copy one into
  .claude/skills/. Use when the student says "find skills", "search for
  skills", "get a skill from GitHub", "install a skill", or types
  /find-skills.
---

# Find skills

You are helping a beginner find extra Claude Code skills on GitHub and, only if they agree, add one to this project. A skill is a folder with a `SKILL.md` file. Claude reads that file and follows it.

## Rules

1. Ask one question at a time. Wait for the answer.
2. Plain English. Short sentences. No em dashes or en dashes.
3. Never install, copy, or download a skill until the student says OK.
4. Only name a repo after you have checked it exists, with `gh` or `curl`. If the check fails, do not recommend it.
5. Prefer well known, trusted collections. Start with https://github.com/anthropics/skills (official public Agent Skills, skills live under `skills/`). Another official collection is https://github.com/vercel-labs/agent-skills. Still verify they exist before you name them.
6. Warn before any install: only add skills from sources they trust, and read the `SKILL.md` first, because a skill can tell Claude to run commands.
7. Never copy secrets, `.env` files, or credentials. Only copy the skill folder.
8. Ask before running any command.

## Step 1: Ask what they want

Ask: "What do you want a skill to help you do?"

Use their words as the search topic. Keep it to a few words, for example "pdf", "slides", or "web testing".

## Step 2: Search GitHub

Check whether `gh` works: `gh --version` and `gh auth status`. You can search public code without being signed in sometimes, but a login helps.

If `gh` works, search in this order:

1. Inside a known collection, for example:
   `gh search code "filename:SKILL.md <topic>" --repo anthropics/skills --limit 10`
   You can run the same search against `vercel-labs/agent-skills`.
2. Across GitHub:
   `gh search code "filename:SKILL.md <topic>" --limit 10`
   If that returns nothing, it is often a search limit, not a missing skill. Fall back to step 1 and to repo search.
3. Repos tagged for skills:
   `gh search repos "<topic>" --topic claude-skills --sort stars --limit 10`

If `gh` is missing or the search fails, do not invent results. Send them to these GitHub website searches (replace TOPIC with their words, no spaces encoded as `+`):

- Code: https://github.com/search?q=filename%3ASKILL.md+TOPIC&type=code
- Repos: https://github.com/search?q=topic%3Aclaude-skills+TOPIC&type=repositories
- Official collection: https://github.com/anthropics/skills/tree/main/skills

You can also open a collection and look for a folder whose name matches the topic, with a `SKILL.md` inside it.

## Step 3: Verify, then show the top 3

For each candidate, before you show it:

1. Confirm the repo exists and is public:
   `gh api repos/OWNER/REPO --jq "{name: .full_name, url: .html_url, stars: .stargazers_count, private: .private}"`
   If `gh` is missing: `curl -sI https://github.com/OWNER/REPO` and check for `HTTP` 200.
2. Confirm there is a `SKILL.md` (get the exact folder path).
3. Skip anything private, anything you could not verify, and anything that looks like malware, credentials, or a joke at the student's expense.

Show at most 3 options. For each one, one plain line plus the link and the star count, for example:

1. pdf: extract and fill PDF files. https://github.com/anthropics/skills/tree/main/skills/pdf (repo anthropics/skills, N stars)

If you found nothing solid, say so, and offer to try a different topic. Do not pad the list with unverified repos.

## Step 4: Warn, then wait for OK

After the list, say this in plain words:

"Only install a skill from a source you trust. I will open the SKILL.md first so we can read what it does. Skills can tell me to run commands on your computer. I will not copy anything until you say OK."

Ask which one they want (1, 2, 3, or none). If they pick one, fetch and show the `SKILL.md` (the first 80 lines is enough if it is long). Summarise in 2 or 3 short sentences: what it does, and whether it runs commands or needs API keys.

Then ask: "Do you want me to copy this skill into .claude/skills/ now?"

If they say no, stop. Leave the project as it is.

## Step 5: Copy the skill, only after OK

Copy only the folder that contains that `SKILL.md` into `.claude/skills/<name>/`, where `<name>` is a short lowercase folder name (the skill's `name` field, or the folder name). If that folder already exists, stop and ask before overwriting.

A simple way, after they say OK:

```bash
git clone --depth 1 https://github.com/OWNER/REPO.git /tmp/find-skills-src
```

Then copy the skill folder (adjust the path to match the repo):

```bash
mkdir -p .claude/skills
cp -r /tmp/find-skills-src/skills/<name> .claude/skills/<name>
```

Remove the temp clone when you are done (`rm -rf /tmp/find-skills-src`). If `git clone` is heavy, you may download just the skill folder with `gh api` instead. Do not use a package you have not checked.

After the copy:

1. Confirm `.claude/skills/<name>/SKILL.md` exists.
2. Tell them to restart Claude Code, or reload skills, so it can see the new skill.
3. Offer to save the change to GitHub with the connect-github skill. Ask before any commit or push.
4. Tell them they can type `/<name>` or ask to "run the <name> skill" next.

## If something goes wrong

- Search returned nothing: try a broader topic, or browse https://github.com/anthropics/skills/tree/main/skills together.
- Repo or SKILL.md could not be verified: skip it and say why.
- They are not sure they trust it: do not install. Offer to keep looking.
