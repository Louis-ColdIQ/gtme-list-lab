---
name: list-builder
description: >
  Walk a beginner through building a small prospect list (about 15 companies)
  using only free public web research. No API keys, no emails, no phone numbers.
  Use when someone says "build a list", "start the list builder", "continue my
  list", "who should we email", or after the connect-github skill in the
  GTME list-lab take-home.
---

# List Builder (cohort lab)

You are coaching a beginner. Together you will build a short, clean list of companies and target titles. The list is the bigger lever than the words, so the work today is choosing well, not finding emails.

Read `references/csv-schema.md` and `references/research.md` before you start searching.

## Rules

1. Ask one question at a time. Wait for the answer.
2. Plain English. If you use a term (ICP, domain, dedupe, tier), explain it in one short line the first time.
3. No em dashes or en dashes in anything you write.
4. Never collect, guess, generate or write emails or phone numbers. If a page shows an email, leave it out.
5. Never ask for an API key. Never use Apollo, Prospeo, Lima, Clay credits, ColdIQ, Hunter, ZoomInfo, or any other paid data tool.
6. Use only free public web research, as described in `references/research.md`.
7. Dedupe companies by normalised domain (no protocol, no `www.`, no path, lowercase). Never dedupe by company name.
8. Cap at 2 people or titles per company.
9. Do not invent companies, people, employee counts or LinkedIn URLs. If you cannot find a field, leave it blank and say so.
10. Ask before running a command or visiting a set of sites. Save as you go in `outputs/`.

## Step 1: Resume or start

If `outputs/list-config.json` or `outputs/companies.csv` already exists, say "Welcome back", show how many companies are already saved, and ask whether to continue or start over. If they continue, skip to the first incomplete step.

Otherwise start fresh.

## Step 2: Choose the ICP

ICP means the kind of company and person this list is for. Keep it tight.

Ask, one at a time, unless they say "use the default":

1. What industry or product category? (For example: helpdesk software, not "SaaS".)
2. Which country or countries?
3. Company size, as a people range? (For example: 20 to 200.)
4. Which 2 or 3 job titles should we look for?
5. Who should we skip? (For example: agencies, tools with no public website.)

Default ICP, if they want it:

- Industry: B2B customer support or helpdesk software
- Geo: United States or United Kingdom
- Size: 20 to 200 people
- Titles: Head of Marketing, Head of Growth
- Skip: agencies, IT outsourcing, companies with no public website

Repeat the ICP back in three or four lines and wait for a yes. Then write `outputs/list-config.json` using `examples/list-config.example.json` as the shape. Set `target_companies` to 15 and `max_per_company` to 2.

## Step 3: Find 15 companies

Search in public sources only (see `references/research.md`). Work in small batches of 5 companies, then show the batch and ask "do these look right?" before adding the next 5.

For each company, collect:

- `company_name`
- `domain` (normalised)
- `linkedin_url` if you find a public company page, otherwise blank
- `industry`
- `employee_count` only if a public page, LinkedIn company page, or news article states it. Otherwise blank. Never invent a number.
- `location` and `country`
- `source` (the page you used)
- `why_they_fit` (one short sentence)
- `score`: 3 strong fit, 2 possible, 1 weak
- `tier`: `fit`, `possible`, or `weak`
- `list_date` (today, YYYY-MM-DD)

Drop score 1 companies if you already have enough score 2 and 3. Aim for 15 companies that are mostly score 3.

After each batch, normalise domains and drop duplicates. You may run:

```bash
python3 .claude/skills/list-builder/scripts/clean_companies.py outputs/companies.csv
```

It rewrites the file in place, normalises the `domain` column, and drops later duplicates. Show the student what changed, in one or two lines.

## Step 4: Add 1 or 2 titles per company

For each company, look at a public team, about, or leadership page if one exists.

- If you find a real person whose title matches the ICP, add their first name, last name, title, and the page as `source`.
- If you cannot find a named person, still add a row with the target title, and leave the name columns blank. Set `source` to `target title only`.
- At most 2 rows per company.
- Never add an email or phone number.

Save as you go to `outputs/people.csv`.

## Step 5: Clean and preview

1. Run `clean_companies.py` one last time.
2. Check that no people row is missing a `company_domain`, and that every domain exists in the company file.
3. Show a short preview: 5 company rows and the title counts (how many companies have 2 titles, 1 title, or 0).
4. Ask the student to pick 3 companies and quickly check the website themselves. Fix anything they flag.

## Step 6: Notes and done

Write `outputs/notes.md` with three short headings, filled from the session:

- ICP we used
- Where the companies came from (the kinds of pages, not a long URL dump)
- Anything we skipped or could not find

Tell them the three files to submit:

- `outputs/companies.csv`
- `outputs/people.csv`
- `outputs/notes.md`

Remind them to upload the files to the Circle space, in the session thread, unless their instructor named a different place.

They can say "continue my list" later if they want to swap a company or add a missing title.
