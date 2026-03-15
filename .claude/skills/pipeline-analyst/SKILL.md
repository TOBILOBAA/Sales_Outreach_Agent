---
name: pipeline-analyst
description: |
  Reviews full pipeline, assigns forecast categories by MEDDPICC score, calculates coverage and velocity.
  Use when: doing a pipeline review, preparing a forecast, checking territory health, or finding at-risk deals.
  Triggers: pipeline review, forecast review, pipeline health, deal health check, commit list, best case list,
  forecast, coverage analysis, what's my number, pipeline at risk, inspect pipeline, weekly forecast.
version: 1.0.0
user-invocable: true
---

# Pipeline Analyst

**DATA RULE:** Forecast categories assigned by criteria — not gut feel. Read all files before scoring.

**DATE RULE:** Check `currentDate`. Output overwrites `memory/pipeline-forecast.md` each run.

---

## STEP 0 — Confirm Scope

Ask if not provided:
1. Full pipeline review or specific stage?
2. What's the quota target for this period? (needed for coverage calculation)
3. What's the period? (this month / this quarter / this half)

---

## STEP 1 — Load All Active Accounts

Read all files:
1. All `accounts/*/account-brief.md` files → stage, MEDDPICC score, last interaction, champion, EB
2. Most recent discovery notes per account → to validate scores and surface red flags

**Inventory every active account:**
| Account | Stage | MEDDPICC Score | Champion | EB Named | Last Touch | Next Step |
|---------|-------|---------------|---------|---------|-----------|----------|
| [name] | | /40 | ✅/⬜ | ✅/⬜ | [date] | [action] |

---

## STEP 2 — Assign Forecast Categories

Assign categories based ONLY on evidence from files. Never on optimism.

| Category | Criteria (ALL must be true) |
|----------|---------------------------|
| **Commit** (>90%) | Score 35+/40 AND next step confirmed with date AND paper/procurement started |
| **Best Case** (>60%) | Score 28+/40 AND champion actively engaged AND EB identified by name |
| **Upside** (<60%) | Score 20+/40 AND discovery complete AND Why Anything confirmed |
| **Not Forecast** | Score < 20/40 OR Why Anything still unknown |

**Forecast Summary:**

| Category | Accounts | Total ACV | Weighted Value |
|----------|----------|-----------|---------------|
| Commit | | $__ | $__ (x1.0) |
| Best Case | | $__ | $__ (x0.6) |
| Upside | | $__ | $__ (x0.3) |
| **Total Forecast** | | $__ | $__ |

---

## STEP 3 — Pipeline Velocity

Formula: **(Qualified Opps x Average Deal Size x Win Rate) / Average Sales Cycle Length**

Fill in from account-briefs and seller context:
- Qualified opportunities (score 20+/40): ___
- Average deal size: $___
- Estimated win rate: ___%
- Average sales cycle length: ___ days

**Pipeline Velocity: $___ / day**

Use to project: "At current velocity, you're on track for $[X] by [date]."

---

## STEP 4 — Coverage Analysis

Coverage ratio = Total pipeline value / Quota target

| Ratio | Status | Interpretation |
|-------|--------|---------------|
| 3x+ | Healthy | Enough to hit quota with normal attrition |
| 2-3x | Adequate | Manageable — watch for deals going dark |
| 1-2x | Thin | Need to add pipeline immediately |
| < 1x | Critical | Cannot hit quota from current pipeline |

**Your coverage: [X]x — [Status]**

---

## STEP 5 — Surface At-Risk Deals

Flag any deal where ANY of the following is true:
- Last meaningful touch > 14 days ago
- MEDDPICC score stuck (same score 2+ reviews)
- Single-threaded (no champion or champion unresponsive)
- No confirmed next step with date
- Red flag triggered (from call-debrief STEP 3.5)

**At-Risk Deals:**

| Account | Risk Signal | Last Touch | Recommended Action |
|---------|------------|-----------|-------------------|
| [name] | [specific signal] | [date] | [specific recovery action] |

---

## STEP 6 — Top 3 Focus Deals

Identify the 3 deals most worth investing time in THIS week:
- Highest score in Commit/Best Case with an actionable next step
- At-risk deals that can be recovered with 1 focused action
- Deals close to a scoring threshold that could upgrade category

| Priority | Account | Category | Why Focus Now | This Week's Action |
|----------|---------|----------|--------------|-------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## STEP 7 — Save Pipeline Forecast

**Overwrite:** `memory/pipeline-forecast.md` (same pattern as territory-signals.md)

### pipeline-forecast.md structure:

```
# Pipeline Forecast — {Date}

## Forecast Summary
[Table from Step 2]

## Coverage Analysis
Coverage ratio: [X]x — [Status]
Quota: $___
Pipeline: $___

## Pipeline Velocity
$___ / day — projected $[X] by [date]

## At-Risk Deals
[Table from Step 5]

## Top 3 Focus Deals This Week
[Table from Step 6]

## Full Pipeline Inventory
[Table from Step 1]
```

---

## Quality Gates

- [ ] All active account-briefs read (not just the ones you remember)
- [ ] MEDDPICC scores sourced from actual call notes or account-briefs — never estimated
- [ ] Forecast categories assigned by criteria (not gut feel)
- [ ] Coverage ratio calculated with actual quota target
- [ ] At-risk deals have specific recovery actions (not "follow up")
- [ ] Pipeline velocity calculated
- [ ] Saved to memory/pipeline-forecast.md with today's date
