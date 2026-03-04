# agentic-seller

## The AI selling system that actually does the work.

You say one thing. It does ten.

> `research Acme Corp`

In the next 8 minutes it runs 12 parallel searches, scrapes their engineering blog, finds the Stack Overflow question from their backend engineer complaining about Elasticsearch sync lag, cross-references 4 open job postings that mention the same pain, identifies the VP Engineering as your best entry point, scores the account 84/100 on your ICP, picks the Sprint sales motion, and delivers three outreach hooks — each one tied to a specific signal with a source URL.

That's not a summary. That's a complete account brief, ready to act on.

---

## Then it chains.

You say:

> `write outreach for Sarah Chen, VP Engineering at Acme Corp`

It doesn't ask you anything. It reads the research file it just built, picks the strongest hook (the Elasticsearch blog post, not the funding round — because Sarah's an engineering leader), maps to her persona, finds a live proof point from your company's case study page that matches her stack, and drafts a LinkedIn connection request, InMail, cold email, and cold call script — all in one pass. The LinkedIn request is 287 characters. The subject line is a question about her specific pain. No product name. No "I'm reaching out."

---

## Then it remembers.

Three weeks later, before your discovery call:

> `prep me for my call with Acme Corp`

It reads everything — the research file, the outreach file, your prior call notes — without you briefing it again. It pulls anything published about Acme in the last 30 days, maps what you still don't know about their buying process against MEDDPICC, and builds a full meeting brief: agenda, targeted discovery questions for each gap, two objections to expect with prepared responses, and two proof points from live search that match their profile.

You walk in knowing more than their own sales team knows about the deal.

---

## Then it learns.

After 10 calls across your territory:

> `what are they pushing back on`

It scans every call notes file you've saved, pulls every objection logged, classifies them by type (Timing / Budget / Authority / Trust / Fit / Competition), calculates win rates, and builds a response library ranked by what actually works. Not generic sales advice. Your patterns, from your calls, in your market.

---

## Every Monday morning:

> `territory health`

It scores every account against your ICP on 5 dimensions, scans for fresh signals (who raised money over the weekend, who hired a new CTO, who published a blog post about the pain you solve), weights the scores by ICP tier, and surfaces a ranked action list: who to call today, who to warm up on LinkedIn this week, who to deprioritize.

You start Monday knowing exactly where to spend your energy.

---

## This is not a chatbot.

Chatbots answer questions. This system takes goals and executes them — across multiple steps, multiple data sources, and your full territory — and gets smarter the more you use it.

It knows your company, your ICP, your qualification methodology, and every account you've ever touched. It runs on live data, not pre-training. Every research file, every call note, every proof point feeds the next interaction.

---

## Who it's for

**AE, BDR, SDR, AM, CSM, RevOps, or founder doing sales.**

Specifically if you:
- Spend 2+ hours researching an account before reaching out
- Write the same outreach in slightly different ways for each contact
- Prep for discovery calls the night before by piecing together LinkedIn + Google + your CRM
- Lose track of what you said you'd follow up on after a call
- Don't know which accounts in your territory are actually worth chasing this week

---

## Two ways to run it

### Claude Code (terminal, full power)

For sellers comfortable with a terminal, or willing to learn one command.

**Setup:** Clone the repo → run `claude` → answer 9 questions → running in 30 minutes.

Claude onboards you through a 9-question interview: your name, company, what you sell, your ICP, qualification framework, CRM, sales tools. It then:
- Fills in your personal configuration
- Searches for AI integrations for every tool you mention (Gong, Salesforce, HubSpot, Apollo...)
- Connects each one it finds
- Tells you what's connected and what's not yet available

```bash
git clone https://github.com/romiluz13/agentic-seller
cd agentic-seller
claude
```

Full setup guide: **[SETUP.md](SETUP.md)**

---

### Claude Cowork (desktop app, no terminal needed)

Anthropic's Claude Cowork is a desktop app that gives you the same agentic AI without ever touching a terminal. Install the plugin, fill in your seller profile, and you're running.

**Setup:** Install the plugin → fill in `cowork-plugin/seller-context.md` → done.

```bash
claude plugins add https://github.com/romiluz13/agentic-seller/tree/main/cowork-plugin
```

Or find it in the Claude Cowork plugin marketplace.

Requires: Claude.ai paid subscription + [Claude Desktop app](https://claude.ai/download) for macOS.

Both interfaces run the **same 8 skills** on the **same methodology**. Use whichever fits your workflow.

---

## What it costs

| What | Cost |
|------|------|
| **Claude.ai subscription** | From $20/month — Claude Code and Cowork are both included |
| **Bright Data** | ~$10/month — free trial available |

**Bright Data** is what makes research genuinely powerful.

| Without Bright Data (lite mode) | With Bright Data (full mode) |
|--------------------------------|------------------------------|
| Web search results | Full page scraping |
| Company overview | LinkedIn profiles, scraped |
| News headlines | Job postings with full text |
| Basic leadership names | Engineering blogs, forums, Stack Overflow |

Most serious sellers connect it. You can start without it and add it later.

**Total: ~$30/month.** Less than a SaaS tool you'd forget to cancel.

---

## The 8 skills

Everything runs in plain English. No commands to memorize.

| What you say | What it does |
|---|---|
| `research [company]` | 12 parallel searches + page scraping → tech stack confirmed, pain signals cited, contacts ranked, FITS score, 3 outreach hooks ready |
| `write outreach for [name] at [company]` | Reads research file → live proof point search → all 4 variants: LI connection (≤300 chars) + InMail + email + cold call script. Banned phrases checked. |
| `prep me for my call with [company]` | Reads all prior files + pulls last 30 days of news → MEDDPICC gap analysis → full meeting brief with agenda, discovery questions, objections, proof points |
| `just got off a call with [company]` | Notes → qualification map → 3 Whys status → follow-up email drafted → account-brief updated → CRM tasks created |
| `what are they pushing back on` | Scans all call notes → classifies objections by type → win rates → response library ranked by what works |
| `linkedin plan for [company]` | Warm path mapping → 4-week engagement ladder → day-by-day comment + share + DM plan before first cold outreach |
| `territory health` | ICP scoring on 5 dimensions → signal scan per account → weighted priority queue → ranked action list for this week |
| `score [company] on ICP` | 5-dimension scoring (Firmographic / Technical / Timing / Decision Capacity / Value Match) → tier assignment → recommended pursuit strategy |

---

## Skill chains (what makes it agentic)

The skills feed each other. You don't manage this — it happens automatically.

**Research → Outreach:**
When you ask for outreach, it reads the research file from your last scan. The hooks, tech stack, and pain signals flow directly into the message. If no research file exists, it runs research first.

**Call debrief → Objection library:**
Every call notes file includes an `## Objections Logged` section. When you run objection mining, it scans every call note across your entire territory and builds the pattern library automatically.

**ICP scoring → Signal weighting:**
Signal scoring multiplies each signal by the account's ICP tier. A funding round at a Tier 1 account scores 29. The same signal at a Tier 4 account scores 9. Your territory rank is always ICP-weighted.

---

## Works with your existing tools

| Tool | What it adds |
|------|-------------|
| **Bright Data** | Full web research — scrapes LinkedIn, job boards, news, company pages, engineering blogs, forums |
| **Gong / Fireflies** | Pull call transcripts directly. Say "debrief my last call with [company]" — no notes needed |
| **Salesforce** | Look up accounts, log calls, update deal stages, create follow-up tasks — without opening Salesforce |
| **HubSpot** | Reads and writes your CRM — contacts, deals, activities, notes |
| **Apollo** | Contact search and enrichment built into your research workflow |
| **Notion** | Full pipeline, tasks, and contacts if you want a free CRM option |
| **Gmail / Calendar** | Pull meeting context before calls, create email drafts from debrief |

---

## Works for any seller, any methodology

- **Roles:** AE, BDR, SDR, AM, CSM, RevOps, founder doing sales
- **Qualification:** MEDDPICC (default), MEDDIC, BANT, SPIN, SPICED, Challenger, custom
- **CRM:** Salesforce, HubSpot, Notion, Pipedrive, or none
- **Company size:** Individual contributor or full sales team

During setup, it asks which methodology you use and configures itself accordingly.
Switch frameworks in one sentence: "we use SPICED, not MEDDPICC."

---

## See a real example

`examples/acme-corp/` shows exactly what the output looks like:
- The full research file after running "research Acme Corp" — FITS score 84/100, 3 confirmed pain signals, 3 ready-to-use hooks
- The account brief after a discovery call — MEDDPICC status, 3 Whys, Sprint route, next actions

---

## Built by a seller

This was built by an SDR who got tired of doing the same manual work every day and decided to engineer a way out.

It's based on the same system used in production — generalized so any seller at any company can use it.

Open source. No SaaS. No subscription to this repo. Clone it, fill in your details, and it's yours.

---

> *"Non-technical teams across sales, marketing, legal, and operations gain the ability to automate workflows and build tools with little or no engineering intervention."*
> — Anthropic 2026 Agentic Coding Trends Report
