# Build a small prospect list with Claude Code

This is the take-home from the GTME Clay Cohort live session. You will use Claude Code and two small skills to get GitHub working, then build a short, clean company list.

Time: about 45 minutes.

## What you'll have at the end

- A GitHub account, and this project folder on your computer
- `outputs/companies.csv`: 15 companies that fit a tight ICP
- `outputs/people.csv`: 1 or 2 target titles at each company
- `outputs/notes.md`: a few lines on how you chose the list

The files have no emails and no phone numbers. Finding those is a later step, with a proper data tool. Today is about picking the right companies and the right titles.

## What you need

- Claude Code already installed and logged in
- About 45 minutes
- A free GitHub account, or 5 minutes to make one. The first skill walks you through it.

You do not need API keys or paid data tools.

## How to start

1. Open Claude Code. A new empty folder, or your home folder, is fine.
2. Copy everything between the lines below and paste it as one message:

```
Clone https://github.com/Louis-ColdIQ/gtme-list-lab into a new folder on my computer, then open that folder as the project. I am a beginner. First run the connect-github skill and help me get Git and GitHub working. Then run the list-builder skill and walk me through building a small prospect list. Ask one question at a time, explain each step in plain words, and wait for me before running a command. Use only free public web research. Never collect, guess, or write emails or phone numbers. Save the list as CSVs in outputs/.
```

3. Press Enter and answer the questions as they come.

Once the folder is open, you can also type `/connect-github` and then `/list-builder` if those appear in the slash menu.

If you already cloned this repo and opened it in Claude Code, paste this instead:

```
Run the connect-github skill, then the list-builder skill. Start my take-home, or continue it if I already started.
```

## The steps

1. Git and GitHub (about 10 minutes). Install Git if you need it, make or sign in to a GitHub account, and get this project onto your computer.
2. Pick a tight ICP, or use the default one the skill offers: industry, country, company size, and 2 or 3 titles.
3. Find 15 companies from public sources. Company websites, public directories, "alternatives to" pages, and news are all fair game. The skill helps you search.
4. Clean the list: normalise each domain, drop duplicates, and keep at most 2 titles per company.
5. Save the CSVs and write a short note.
6. Spot-check 3 companies yourself before you submit.

## The default ICP

If you do not want to invent one, use this:

B2B customer support or helpdesk software companies, 20 to 200 people, United States or United Kingdom. Titles: Head of Marketing, Head of Growth.

You can change it. Keep it narrow. Fifteen companies that really fit are better than fifty that sort of fit.

## What to submit

Upload these three files to the Circle space, in the session thread (change this if your instructor gives you a different place):

- `outputs/companies.csv`
- `outputs/people.csv`
- `outputs/notes.md`

## If you get stuck

Ask Claude Code "where am I?" or "explain that again." If a command fails, paste the error and ask it to fix the problem with you, one step at a time. You can also post in the Circle space.

## Rules

- No emails or phone numbers in any file
- No paid data tools and no API keys
- Do not commit a `.env` file
- If something asks you to skip a security warning you do not understand, stop and ask in Circle
