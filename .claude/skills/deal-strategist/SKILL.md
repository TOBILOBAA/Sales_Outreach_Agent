---
name: deal-strategist
description: |
  Diagnoses stuck deals and builds a 3-move recovery strategy using MEDDPICC scoring and targeted frameworks.
  Use when: deal is stalled, competitive threat identified, single-threaded, or process has stopped.
  Triggers: deal strategy, deal review, stuck deal, advance this deal, competitive play, challenger approach,
  deal health, how do I win this, competitive strategy, how to advance, deal blocked, reframe strategy.
version: 1.0.0
user-invocable: true
---

# Deal Strategist

**DATA RULE:** Strategy must be grounded in actual deal state — not assumptions. Read the files first.

**DATE RULE:** Check `currentDate`. Output saved as `YYYY-MM-DD-deal-strategy.md`.

---

## STEP 0 — Confirm Deal Context

Ask if not provided:
1. Which account?
2. Current stage (Research / Outreach / Discovery / Meeting Booked / Qualified)
3. What's the problem? (e.g., "they went dark", "competitor entered", "stuck after verbal yes")
4. When was the last meaningful interaction?

---

## STEP 1 — Load Deal State

Read all available files in order:
1. `accounts/{account}/account-brief.md` → current MEDDPICC status + 3 Whys + stage
2. `accounts/{account}/discovery/` → most recent call notes (look for MEDDPICC score + red flags)
3. `accounts/{account}/meetings/` → most recent meeting brief or summary
4. `memory/account-intel.md` → confirmed contacts, warm intros, relationship history

**Build the deal snapshot:**
- Current MEDDPICC Score: ___ / 40
- Champion: confirmed / suspected / none
- Economic Buyer: named / not reached / unknown
- Compelling event: exists / unclear / none identified
- Competitor: in play / not mentioned / unknown
- Last meaningful interaction: [date + what happened]

---

## STEP 2 — Diagnose Deal Problem

Identify ONE primary problem type (the root cause, not just the symptom):

| Problem Type | Signals | Framework to deploy |
|-------------|---------|-------------------|
| **Complacent buyer** | No urgency, "we're fine", scores low on Why Anything | Challenger — Rational Drowning + Emotional Impact |
| **Competitive threat** | Competitor named, decision criteria shifting, going dark | FIA + Landmine questions |
| **Single-threaded** | Only 1 contact, champion won't broker EB, no internal movement | Champion coaching plan |
| **Process stall** | Verbal yes but nothing moving, procurement/legal silent, "waiting on" | Pattern interrupt re-engagement |

**State the diagnosis explicitly:**
> "This is a [Problem Type] situation because [2-3 specific signals from the files]."

---

## STEP 3 — Build Strategy by Problem Type

### If Complacent Buyer — Challenger Play
Reference: `.claude/skills/write-outreach/references/challenger-messaging.md`

1. **Identify the reframe:** What does this buyer not realize about their problem?
2. **Find the rational drowning data:** What's the cost of inaction? (use verified proof points only)
3. **Map the emotional impact:** What does this mean for their team / career / competitive position?
4. **Draft the reframe message:** Use Steps 2-4 of the Challenger sequence

Output: A reframe message + talking points for the next interaction.

---

### If Competitive Threat — FIA Play
Reference: `.claude/skills/discovery-prep/references/competitive-positioning.md` + `knowledge/competitive/{competitor}.md`

1. **Identify the zone:** Winning / Battling / Losing
2. **FIA response:** Fact (acknowledge) → Impact (ask about their use case) → Act (reframe to your strength)
3. **Select 1-2 landmine questions** relevant to this specific competitor and deal
4. **Identify the winning criterion** the buyer has confirmed that favors you

Output: FIA positioning + landmine questions + next conversation approach.

---

### If Single-Threaded — Champion Coaching Plan

1. **Assess the champion:** Do they believe? Can they articulate the value? Will they carry it internally?
2. **Identify the gap:** Is the champion unwilling, unable, or just not yet asked to broker access?
3. **Build the ask:** What specifically are you asking them to do? (intro to EB, internal memo, stakeholder map)
4. **Create a 1-pager they can use internally:** Problem statement (in their words) + value in their metrics + proposed next step

Output: Champion coaching script + 1-pager outline for internal use.

---

### If Process Stall — Pattern Interrupt Re-engagement

1. **Find a new signal:** Fresh news, funding, hire, competitive move, regulatory change — anything that creates a new reason to reach out
2. **New value angle:** Something you haven't shared yet (proof point, case study, relevant benchmark)
3. **Reframe the urgency:** What external event could create a new compelling reason to move?
4. **Pattern interrupt message:** Not "just checking in" — a new signal + a new question

Output: Re-engagement message with new hook + a reframed Why Now argument.

---

## STEP 4 — Build 3 Next Moves

Output exactly 3 moves. Each must be:
- **Specific** (not "follow up" — exact message / action / conversation)
- **Ownable** (who does it: seller, AE, or champion)
- **Dated** (proposed date — not "soon")
- **Measurable** (what does success look like for this move)

| Move | Action | Owner | Date | Success Measure |
|------|--------|-------|------|----------------|
| 1 | [Specific action] | [Seller / AE / Champion] | [Date] | [What changes if this works] |
| 2 | [Specific action] | [Seller / AE / Champion] | [Date] | [What changes if this works] |
| 3 | [Specific action] | [Seller / AE / Champion] | [Date] | [What changes if this works] |

---

## STEP 5 — Save and Update

**Save strategy as:** `accounts/{account}/meetings/YYYY-MM-DD-deal-strategy.md`

**Update account-brief.md:**
- Stage: update if changed
- Deal health: add MEDDPICC score if new
- Next action: update to Move 1

---

## Quality Gates

- [ ] Deal state loaded from actual files (not assumptions)
- [ ] MEDDPICC score sourced from call notes or account-brief (not estimated)
- [ ] Problem type diagnosed with 2+ specific signals cited
- [ ] Correct framework loaded for the diagnosed problem type
- [ ] 3 next moves are specific, ownable, and dated
- [ ] Strategy saved with today's date
- [ ] account-brief.md updated with new next action
