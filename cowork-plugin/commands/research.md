---
description: Research an account — signals, tech stack, contacts, hooks
argument-hint: <company name>
allowed-tools: Read, Write, WebSearch
---

Read your seller profile: @${CLAUDE_PLUGIN_ROOT}/seller-context.md

Run a full research sweep on: $ARGUMENTS

Follow the prospect-research skill. Deliver a complete research file covering:
- Company overview (size, stage, what they do, HQ)
- Tech stack confirmed from sources — not assumed
- Leadership contacts with relevance to the seller's solution
- Pain signals cited from live research
- FITS score: Firmographic / Intent / Timing / Solution Match (0–25 each)
- Top 3 outreach hooks — specific, ready to use, one per key contact

Research mode:
- If ~~web research is connected: scrape full pages, job postings, LinkedIn company page, engineering blogs
- If not: use built-in web search and note "⚠️ Lite mode — search results only, no page scraping"

Save to: accounts/{company-name}/research/YYYY-MM-DD-initial-research.md
Create: accounts/{company-name}/account-brief.md skeleton if it does not exist
