# agentic-seller

## Your AI co-pilot for B2B sales. Built by a seller, for sellers.

Account research that takes 2 hours → done in 8 minutes.<br>
Generic outreach that gets ignored → personalized messages built from real signals.<br>
Walking into discovery calls blind → full brief ready in 2 minutes.

This is not a chatbot. It's an **always-on selling system** that knows your company, your ICP, your methodology, and your territory — and gets smarter every call.

---

## Who this is for

You are an **AE, BDR, SDR, AM, or founder doing sales**.

You spend too much time on things that shouldn't take that long:
- Researching an account before reaching out
- Writing the same outreach in slightly different ways
- Preparing for a discovery call at 11pm
- Capturing notes after a call while trying to remember what was said
- Figuring out which accounts in your territory are actually worth chasing this week

This system handles all of that.

---

## What it actually does

Once you set it up (30 minutes, no coding), you talk to it like a colleague:

**Before reaching out to an account:**
> `research Acme Corp`

It scans their tech stack, finds the engineer who just published a blog post about the exact problem you solve, checks for recent funding, identifies who to target first, and tells you the three strongest hooks — with sources. Saves 2+ hours.

**When you need to write outreach:**
> `write outreach for Sarah Chen, VP Engineering at Acme Corp`

It reads the research it just did, picks the sharpest signal, and drafts a LinkedIn connection, InMail, cold email, and cold call script — all in one go. Personalized to her role and their specific situation. Never generic.

**The morning before a big discovery call:**
> `prep me for my call with Acme Corp`

It pulls everything it knows about the account, finds anything published in the last 30 days, identifies which qualification gaps to fill, and builds a full meeting brief — agenda, discovery questions, expected objections, proof points ready to pull.

**Right after a call:**
> `just got off a call with Acme Corp`

Dump your raw notes. It extracts the qualification map, flags what's still missing, drafts the follow-up email, and updates the account record. Done in under 5 minutes.

**When you want to know where to focus:**
> `territory health`

It scans all your accounts, scores the signals by how well each account fits your ICP, and gives you a ranked list: who to call today, who to warm up, who to deprioritize.

---

## What it costs

| What | Cost |
|------|------|
| **Claude Code** | Included with Claude.ai subscription |
| **Claude.ai subscription** | From $20/month (Pro) — enough to get started |
| **Bright Data** | ~$10/month — free trial available |

**Bright Data** is what makes research genuinely powerful. Without it: web search results only. With it: full LinkedIn profiles, job postings, company pages, engineering blogs, news. Most serious sellers connect it. You can start without it and add it later.

**Total: ~$30/month.** Less than one lunch.

---

## Setup — 30 minutes, no coding required

Full step-by-step: **[SETUP.md](SETUP.md)**

The short version:
1. Get [Claude Code](https://claude.ai/code) — it's included with your Claude.ai subscription
2. Clone this repo: `git clone https://github.com/romiluz13/agentic-seller`
3. Add your Bright Data key (see `mcp-integrations/brightdata-setup.md`)
4. Run `claude` from the folder — it onboards you automatically

**The onboarding experience:**
Claude asks you 9 questions — your name, company, what you sell, your ICP, your CRM, which sales tools you use. It then:
- Fills in your personal configuration
- Searches for AI integrations for every tool you already use (Gong, Salesforce, HubSpot, Apollo...)
- Sets up your pipeline in Notion if you want it
- Tells you what's connected and what's not yet available

> "You're set up. Ready to research your first account? Just say: research [company name]"

---

## The 8 skills

Everything runs by typing in plain English. No commands to memorize.

| What you say | What it does |
|---|---|
| "research [company]" | Scans tech stack, finds signals, identifies contacts, builds the research file. 8 min vs 2 hours. |
| "write outreach for [name] at [company]" | Reads the research, picks the sharpest hook, writes LinkedIn + InMail + email + cold call script — all personalized. |
| "prep me for my call with [company]" | Builds a full meeting brief: what we know, what we're missing, discovery questions, objections to expect, proof points to pull. |
| "just got off a call with [company]" | Notes → qualification map → follow-up email → updated account record. While it's still fresh. |
| "what are they pushing back on" | Scans all your call notes, finds the objection patterns, builds a response library ranked by what actually works. |
| "linkedin plan for [company]" | Maps the warm path before you cold outreach — who to engage, what to comment on, how to become familiar before you pitch. |
| "territory health" | Scans every account, scores the signals against your ICP, tells you exactly where to focus this week. |
| "score [company] on ICP" | 5-dimension fit scoring — tells you if this account is worth your time or not, and why. |

---

## Works with your existing tools

Claude finds integrations automatically during onboarding. It searches for each tool you mention and tells you what it found.

| Your tool | What it adds |
|-----------|-------------|
| **Bright Data** | Full web research — LinkedIn, job boards, news, company pages. The difference between shallow and deep research. |
| **Gong** | Pull call transcripts directly. Say "debrief my last call with [company]" — no notes needed. |
| **Salesforce** | Look up accounts, log activities, update deal stages without opening Salesforce. |
| **HubSpot** | Same as Salesforce — reads and writes your CRM. |
| **Apollo** | Contact search and enrichment directly from your research. |
| **Notion** | Pipeline, tasks, and contacts if you don't have a CRM or want a free option. |
| **LinkedIn** | Profile and company data at scale. |

---

## Works for any seller, any methodology

- **Roles:** AE, BDR, SDR, AM, CSM, RevOps, founder doing sales
- **Qualification frameworks:** MEDDPICC (default), BANT, SPIN, SPICED, Challenger, custom
- **CRM:** Salesforce, HubSpot, Notion, Pipedrive, or none
- **Company size:** Startup with 5 reps or enterprise team of 200

During setup, it asks which framework you use and configures itself accordingly. Switch frameworks in one sentence.

---

## See a real example

`examples/acme-corp/` shows exactly what the output looks like:
- The research file after running "research Acme Corp"
- The account brief after a discovery call

---

## Built by a seller

This was built by an SDR who got tired of doing the same manual work every day and decided to engineer a way out.

It's based on the same system used in production — generalized so any seller at any company can use it.

Open source. No SaaS. No subscription to this repo. Clone it and own it.

---

> *"Non-technical teams across sales, marketing, legal, and operations gain the ability to automate workflows and build tools with little or no engineering intervention."*
> — Anthropic 2026 Agentic Coding Trends Report
