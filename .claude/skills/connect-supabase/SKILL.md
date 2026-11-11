---
name: connect-supabase
description: >
  Optional. Set up a free Supabase project as the "company brain" and load the
  company and people CSVs into it. Use when the student says "set up Supabase",
  "save my list to a database", or "connect Supabase".
---

# Connect Supabase (optional)

GitHub keeps the files (the instructions and context). Supabase keeps the data: every company and person you ever found, in one place, so nothing gets lost between lists. Think of it as the company brain.

Keep this light. No code is needed, everything happens in the Supabase website.

## Rules

1. One step at a time. Wait for the student.
2. Never ask them to paste keys or passwords into the chat. If they want Claude to read the database later, keys go in `.env` (git ignores it).
3. No em dashes or en dashes.

## Steps

1. Go to supabase.com and sign up (free plan, GitHub sign in works).
2. Click New project. Name it `client-hq`. Pick a region close to them. Save the database password somewhere safe (not in this repo).
3. Open SQL Editor, click New query, paste this, click Run:

```sql
create table companies (
  id bigint generated always as identity primary key,
  client text,
  company_name text,
  domain text,
  linkedin_url text,
  industry text,
  employee_count text,
  location text,
  country text,
  score int,
  tier text,
  source text,
  why_they_fit text,
  list_date date,
  unique (client, domain)
);

create table people (
  id bigint generated always as identity primary key,
  client text,
  first_name text,
  last_name text,
  full_name text,
  job_title text,
  company_name text,
  company_domain text,
  location text,
  country text,
  tier text,
  source text,
  list_date date
);
```

4. Before importing, add a `client` column to each CSV with the client slug. Claude can do this: ask first, then write copies named `*-supabase.csv` in the same `lists/` folder.
5. Open Table Editor, pick `companies`, click Insert, then Import data from CSV, and pick the companies file. Do the same for `people`.
6. Check the row counts match the CSVs.

Say: "Your list now lives in Supabase. Next time, Claude can check it so you never research the same company twice."
