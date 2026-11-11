---
name: list-builder
description: >
  Build a small company list and people list for a client, using the Clay CLI if
  it is connected, otherwise free public web research. Use when the student says
  "build a list", "find companies", "find prospects", "pull a list from Clay",
  or after new-client.
---

# List builder

A good list comes from good context. This skill reads the client's ICP and turns it into a list of companies and the right people at them.

## Rules

1. Read `clients/<client>/client.md` first. If it is missing, run new-client.
2. One question at a time. Ask before every command.
3. Start small: 10 to 20 companies, at most 2 people per company.
4. Never guess, invent, or pattern match emails or phone numbers. The CSVs have no email or phone columns. If the student wants emails, they enrich in their own Clay account.
5. Respect the Exclusions in client.md.
6. No em dashes or en dashes.

## Step 1: Confirm the list

From client.md, write back a short list plan and ask "Does this look right?":

- Industry, size, countries
- Fit signals to look for
- Job titles (decision maker first)
- What to skip
- How many companies (default 15)

## Step 2: Pick the path

Run `clay whoami`. If it shows a workspace, use the Clay path. If not, ask: "Do you want to connect Clay first (connect-clay skill) or use free web research?"

## Step 3a: Clay path

1. Run `clay searches query-mode reference` and read the grammar before writing a query.
2. Turn the plan into a company query, for example:
   `clay searches query-mode create --query 'select from companies where industry = "Software Development"'`
   Show the query to the student and ask before running it.
3. Run `clay searches query-mode run <searchId>` to get results (JSON). Keep it to one page at first. Free plans get about 50 results per search.
4. Do the same for people at those companies with the job titles from client.md (`select from people ...`).
5. Map the results into the CSV schema below. Set `source` to `clay search`.

## Step 3b: Free web path

1. Search the web for companies that match (directories, "alternatives to" pages, news, association member lists). See `references/research.md`.
2. Check each company's own website. Only keep ones that clearly fit. Write one sentence on why.
3. For people, look at the company's team or about page. If no name is public, add a row with only the target title and `source` = `target title only`.

## Step 4: Score and save

- Score each company 3 (strong fit), 2 (possible), 1 (weak). Drop the 1s unless the list is tiny.
- Save to `clients/<client>/lists/<date>-companies.csv` and `<date>-people.csv` using `references/csv-schema.md`.
- Clean the company file: `python3 .claude/skills/list-builder/scripts/clean_companies.py clients/<client>/lists/<date>-companies.csv`
- Show a short summary: how many companies, how many people, the top 5 and why.

## Step 5: Next

Say: "Next we can turn this list into a campaign with new-campaign." Offer to save to GitHub, and if they set up Supabase, offer connect-supabase to load the CSVs.
