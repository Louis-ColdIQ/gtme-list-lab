# CSV schema

One shape for every list, snake_case column names. No emails, no phone numbers.

## Companies (`clients/<client>/lists/<date>-companies.csv`)

```
company_name,domain,linkedin_url,industry,employee_count,location,country,score,tier,source,why_they_fit,list_date
```

- `domain` is the dedupe key. Normalise it: lowercase, no `https://`, no `www.`, no path, no trailing slash.
- `linkedin_url` is the company page, also normalised (no `https://`, no `www.`, no query string, no trailing slash). Blank if you did not find one.
- `score` is 3 (strong fit), 2 (possible), or 1 (weak). `tier` is `fit`, `possible`, or `weak`.
- `source` is where you found the company (for example: `clay search`, `company website`, `alternatives page`, `news article`).
- `why_they_fit` is one short sentence.
- `employee_count` is blank unless a public source states it.

See `examples/companies.example.csv`.

## People (`clients/<client>/lists/<date>-people.csv`)

```
first_name,last_name,full_name,job_title,company_name,company_domain,location,country,tier,source,list_date
```

- `company_domain` must match a `domain` in the company file.
- Name columns may be blank when you only have a target title.
- `source` is `clay search`, `company team page`, `about page`, or `target title only`.
- At most 2 rows per `company_domain`.
- Never add email or phone columns.

See `examples/people.example.csv`.
