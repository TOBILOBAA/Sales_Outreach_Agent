---
description: Score your territory — surface where to focus this week
allowed-tools: Read, Write, WebSearch
---

Read your seller profile: @${CLAUDE_PLUGIN_ROOT}/seller-context.md

Run a territory health check.

Follow the icp-matrix-builder and signal-scoring skills in sequence:

Step 1 — ICP Tiers:
- Load memory/icp-matrix.md. If it does not exist: score all accounts in the accounts/ folder on 5 dimensions first (Firmographic / Technical / Timing / Decision Capacity / Value Match, 0–20 each) then assign tiers (Tier 1: 80+, Tier 2: 60–79, Tier 3: 40–59, Tier 4: <40).

Step 2 — Signal Scan:
- For all Tier 1 and Tier 2 accounts: search for fresh buying signals (funding, hiring, product launches, leadership changes, conference talks, engineering blog posts).
- If ~~web research is connected: run live searches per account.
- If not: check existing research files and use built-in web search.

Step 3 — Score and Rank:
- Score each signal: funding round = 22, leadership change = 20, hiring surge = 18, product launch = 18, job posting mentioning pain = 13, engineering blog post = 14.
- Apply ICP tier multiplier: Tier 1 × 1.3, Tier 2 × 1.0, Tier 3 × 0.7, Tier 4 × 0.4.
- Build priority queue (score 18+) and watch list (score 12–17).

Deliver:
- Priority queue with recommended action per account
- Watch list
- Territory health metrics (total accounts, active signals, hot signals)
- Top 3 focus recommendations for this week — specific, not generic

Save to: memory/territory-signals.md (overwrite — this is a current-state snapshot)
