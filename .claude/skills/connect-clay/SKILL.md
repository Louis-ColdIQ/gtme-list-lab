---
name: connect-clay
description: >
  Install the Clay CLI and sign in so Claude can search Clay's company and people
  data from the terminal. Use when the student says "connect Clay", "set up Clay",
  "clay login", or wants list-builder to use Clay.
---

# Connect Clay

Clay is a data tool for finding companies and people. The Clay CLI is a small program that lets Claude talk to the student's own Clay account from the terminal. It is optional. Without it, list-builder uses free web research.

## Rules

1. One step at a time. Ask before every command.
2. The student needs their own Clay account (free is fine to start, sign up at clay.com).
3. Never print or copy tokens. Sign in happens in the browser, there is no key to paste.
4. Tell the student before anything that could use Clay credits.
5. No em dashes or en dashes.

## Step 1: Is it already installed?

```bash
clay --version
```

If it prints a version (for example `1.18.0`), skip to Step 3.

## Step 2: Install

Pick one. Explain it first.

Option A, the Clay plugin for Claude Code (recommended, it also installs Clay's own skills). The student types these at the Claude Code `>` prompt, one at a time:

```
/plugin marketplace add clay-run/agent-plugins
/plugin install clay@clay-plugins
```

Choose "Install for you (user scope)". Then run `/clay:setup`. It installs the `clay` command, signs in, and checks it works.

Option B, with npm (needs Node.js installed):

```bash
npm install -g @clay-run/cli
```

If `clay` is "not found" after installing, the folder `~/.local/bin` may be missing from PATH (Mac/Linux):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Windows: use WSL (Ubuntu) and run everything inside it.

## Step 3: Sign in

```bash
clay login
```

A browser opens. Sign in to Clay, pick the workspace, click Authorize. If no browser opens (remote machine), use:

```bash
clay login --device
```

It prints a link and a code. Open the link on any device, check the code matches, pick the workspace, click Authorize. The code lasts 10 minutes.

## Step 4: Test it

```bash
clay whoami
```

It should show the student's workspace name. Then a tiny search (company search, small):

```bash
clay searches query-mode reference
clay searches query-mode create --query 'select from companies where industry = "Software Development"'
clay searches query-mode run <searchId>
```

The first command prints the query grammar (read it before writing queries). `create` returns a `searchId`, `run` fetches a page of results as JSON.

Free plan limit: about 50 results per search and 100 per 30 days. Keep test searches small.

## Done

Say: "Clay is connected. list-builder will now use Clay for companies and people." To sign out later: `clay logout`.

Source: Clay docs (university.clay.com/docs/clay-api-cli) and github.com/clay-run/agent-plugins. Commands can change, so if one fails, run `clay --help` or `clay <command> --help` and follow that.
