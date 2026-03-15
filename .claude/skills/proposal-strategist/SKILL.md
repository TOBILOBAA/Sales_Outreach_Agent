---
name: proposal-strategist
description: |
  Builds a three-act proposal narrative with win themes and executive summary from discovery notes.
  Use when: deal is qualified (MEDDPICC 20+) and seller needs to write a formal proposal or business case.
  Triggers: proposal, write proposal, build proposal, proposal narrative, executive summary, business case,
  win themes, three-act proposal, proposal strategy, proposal draft, write the business case.
version: 1.0.0
user-invocable: true
---

# Proposal Strategist

**READINESS GATE:** Do not build a proposal until the deal is qualified. Check before proceeding.

**DATA RULE:** Every claim must trace back to a confirmed discovery quote or verified proof point. Never invent metrics.

**DATE RULE:** Check `currentDate`. Output saved as `YYYY-MM-DD-proposal-draft.md`.

---

## STEP 0 — Readiness Gate

Before building anything, confirm ALL of these are true:

| Gate | Requirement | Status |
|------|-------------|--------|
| MEDDPICC Score | 20+ (active opportunity minimum) | Confirmed / Not yet |
| Identified Pain | Confirmed with at least 1 direct quote | Confirmed / Not yet |
| Economic Buyer | Named — who will approve or sign | Confirmed / Not yet |
| Decision Criteria | At least 2-3 criteria articulated by buyer | Confirmed / Not yet |

**If any gate is not met — STOP.**
Tell the seller: "This deal isn't ready for a proposal yet. The gap is [missing element]. Run `/discovery-prep` to fill it before the next call."

---

## STEP 1 — Load Deal Context

Read all available files:
1. `accounts/{account}/account-brief.md` → full MEDDPICC status, EB, champion, decision criteria
2. `accounts/{account}/discovery/` → all call notes (pain quotes, metrics they mentioned, language they used)
3. `accounts/{account}/meetings/` → meeting briefs and summaries
4. `accounts/{account}/research/` → company overview, tech stack, competitive context
5. `.claude/skills/write-outreach/references/proof-points.md` → verified proof points to match

**Extract from the files:**
- 3-5 confirmed pains in the buyer's exact words (direct quotes)
- Decision criteria as they stated them
- Metrics they care about (their numbers, not yours)
- Economic Buyer's name + role + what they care about
- Competitors in the deal (if any)

---

## STEP 2 — Define Win Themes

Build 3-5 win themes. Each theme is:
**[Buyer's confirmed pain] + [Your specific capability] + [Proof metric]**

And each theme must map to at least one confirmed decision criterion.

| Win Theme | Buyer Pain (quote) | Your Capability | Proof Metric | Decision Criterion |
|-----------|-------------------|-----------------|-------------|-------------------|
| 1 | "[direct quote]" | [specific feature/approach] | [verified metric] | [their criterion] |
| 2 | "[direct quote]" | [specific feature/approach] | [verified metric] | [their criterion] |
| 3 | "[direct quote]" | [specific feature/approach] | [verified metric] | [their criterion] |

**Rule:** If you can't find a direct quote for a theme, that theme is not confirmed. Remove it.

---

## STEP 3 — Build the Three-Act Narrative

### Act I — Understanding Their Situation
Mirror their world back to them. Zero product mentions.

Structure:
1. Where they are today (their current state — use their language from discovery)
2. What's breaking (the specific pain — use their direct quotes)
3. What they've tried (prior solutions that didn't work)
4. The cost of continuing this way (implication — their numbers or close estimates)

**Quality gate:** Re-read Act I. If {{PRODUCT_NAME}} appears anywhere — remove it. Act I is 100% about them.

---

### Act II — The Solution
Map capabilities to confirmed pains. One section per win theme.

Structure per win theme:
1. **Recap the pain** (1 sentence — their words)
2. **The specific capability** that addresses it (feature/approach in plain language)
3. **How it works** (1-2 sentences — concrete, not vague)
4. **Proof** (1 customer example that mirrors their situation — source URL or proof-points.md ref)

**Quality gate:** Every capability in Act II must map to a confirmed pain from Act I. No orphaned features.

---

### Act III — The Transformed State
Show the specific, quantified future using their own metrics.

Structure:
1. **[Their metric] changes from [current state] to [future state]** — because of [specific capability]
2. **What becomes possible** that isn't possible today (use their future state language from discovery)
3. **Timeline to value** — when do they start seeing results?

**Quality gate:** Act III must use THEIR metrics (from discovery) not generic industry benchmarks.

---

### Executive Summary (1 page, 5 sentences)

Write exactly 5 sentences:
1. **Situation:** "[Company] is dealing with [specific pain in their words]."
2. **Cost of nothing:** "Left unaddressed, this means [implication — their words or verified estimate]."
3. **What we do:** "{{PRODUCT_NAME}} [specific capability] so that [specific outcome]."
4. **Proof:** "[Customer] solved a similar challenge and achieved [metric] in [timeframe]."
5. **Next step:** "We recommend [specific next step] by [date] to [achieve their goal]."

**Quality gate:** Read the executive summary aloud. It must stand alone in 90 seconds and make sense to someone who wasn't on any discovery call.

---

## STEP 4 — Save Proposal Draft

**Save as:** `accounts/{account}/meetings/YYYY-MM-DD-proposal-draft.md`

### Proposal file structure:

```
# Proposal Draft — {Company}
Prepared: {date}
For: {Economic Buyer name + title}
Prepared by: {{SELLER_NAME}} / {{AE_NAME}}

---

## Executive Summary
[5-sentence structure from Step 3]

---

## Understanding Your Situation (Act I)
[Act I content]

---

## The Solution (Act II)

### Win Theme 1: [theme title]
[Content]

### Win Theme 2: [theme title]
[Content]

### Win Theme 3: [theme title]
[Content]

---

## What Changes (Act III)
[Act III content]

---

## Win Themes Summary
[Table from Step 2]

---

## Recommended Next Step
[Specific CTA with proposed date]
```

---

## Quality Gates

- [ ] MEDDPICC 20+ confirmed before starting
- [ ] Pain confirmed with at least 1 direct quote from discovery
- [ ] Win themes map to confirmed decision criteria
- [ ] Act I contains no product mentions
- [ ] Act II capabilities map to confirmed pains (no orphaned features)
- [ ] Act III uses buyer's own metrics from discovery (not generic benchmarks)
- [ ] Executive summary stands alone in 90 seconds
- [ ] Saved with today's date in meetings/ folder
