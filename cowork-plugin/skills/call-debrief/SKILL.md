---
name: call-debrief
description: Post-call debrief. Captures notes, maps to qualification framework, drafts follow-up email. Trigger with "just got off a call with [company]", "debrief [company]", "call notes for [company]", "I just spoke with [name]", "post call [company]", or "update qualification for [company]".
version: 1.0.0
---

# Call Debrief

**⚠️ TIMING RULE:** Do this immediately after the call. The best debrief is in the first 15 minutes.
Memory degrades fast. Don't wait.

---

## STEP 0 — Confirm Context

Ask if not provided:
1. Which account + which contact(s) were on the call?
2. Call type: cold call / intro / discovery / follow-up / AE-led
3. How long did it last?
4. Do you have notes, or should I ask you questions to capture them?

If no notes → run the verbal download guide in Step 2.

---

## STEP 1 — Read Prior Context

Before capturing notes, read what we knew BEFORE the call:
1. `accounts/{account}/account-brief.md` → current qualification status
2. `accounts/{account}/meetings/{last-brief}.md` → what were we trying to learn?
3. `accounts/{account}/discovery/` → any prior call notes

**Why this matters:** The debrief highlights what CHANGED, not just what was said.

---

## STEP 2 — Capture Notes (verbal download mode)

If seller is giving notes verbally, guide them through these in order:

**Quick Context**
- "What happened — in one sentence?"
- "Who spoke the most — them or you?"
- "What was the energy? Engaged / polite / skeptical / rushed?"

**Pain Discovery (most important)**
- "Did they describe any specific problem or frustration?"
- "What does the current process look like? What breaks?"
- "Did they use words like 'pain', 'frustration', 'annoying', 'broken'?"
- "What have they tried before? What didn't work?"

**Qualification Elements**
- "Did anyone mention budget, cost, or cost reduction?"
- "Who else needs to be involved in a decision like this?"
- "What criteria will they use to evaluate options?"
- "Is there a timeline or upcoming deadline?"
- "Who's the internal champion?"
- "What else are they evaluating or already using?"

**Momentum**
- "Did they agree to a next step? What exactly?"
- "Any specific objection? How did it go?"
- "Any quote or thing they said that stood out?"

---

## STEP 3 — Map to Qualification Framework

Use the framework from seller profile.

Default: MEDDPICC

| Letter | Question | Status | Evidence from Call |
|--------|----------|--------|--------------------|
| M — Metrics | What numbers change? | ✅/⬜/🚫 | Direct quote preferred |
| E — Economic Buyer | Who approves budget? | ✅/⬜/🚫 | Name if known |
| D — Decision Criteria | How will they evaluate? | ✅/⬜/🚫 | Criteria mentioned |
| D — Decision Process | Steps to get to yes? | ✅/⬜/🚫 | Process described |
| P — Paper Process | Procurement/Legal/Security? | ✅/⬜/🚫 | Steps mentioned |
| I — Identified Pain | What specific pain? | ✅/⬜/🚫 | Quote from call |
| C — Champion | Who advocates internally? | ✅/⬜/🚫 | Name + evidence |
| C — Competition | What else evaluating? | ✅/⬜/🚫 | Competitor(s) named |

---

## STEP 4 — 3 Whys Assessment

| Why | Status | Evidence |
|-----|--------|----------|
| Why Anything (cost of status quo) | ✅/⬜ | |
| Why Product (capability match) | ✅/⬜ | |
| Why Now (urgency driver) | ✅/⬜ | |

Analysis:
- All 3 ⬜ → Very early. Priority: establish pain first.
- Why Anything ✅, others ⬜ → Next meeting: Why Product and Why Now.
- All 3 ✅ → Strong discovery. Advance to next stage.
- Why Now ⬜ → Create urgency in follow-up: find an external event.

---

## STEP 5 — CRM Update Notes

Output for copy-paste into ~~CRM (or sync via CRM if connected):

```
CRM Call Log — {Date}
Call type: {type} | Duration: {X min} | Attendees: {names + titles}

Summary:
[2-3 sentences: what happened, key finding, next step]

Qualification Updates:
- Pain (I): [confirmed/updated to: ...]
- Economic Buyer (E): [identified as: ...]
- Champion (C): [identified as / not yet identified]
- Next Step: [what was agreed]

Stage Recommendation: {Research / Outreach / Engaged / Discovery / Qualified}
```

---

## STEP 6 — Save Call Notes

**File path:**
- Discovery/intro/follow-up → `accounts/{account}/discovery/{YYYY-MM-DD}-{type}-notes.md`
- AE-led meeting → `accounts/{account}/meetings/{YYYY-MM-DD}-meeting-summary.md`

```markdown
# Call Notes — {Company} — {Date}
**Type:** {Cold Call / Intro / Discovery / Follow-up}
**Duration:** {X min}
**Participants:** {Their names + titles} | {Seller / AE if present}
**Energy:** {Engaged / Polite / Skeptical / Rushed}

---

## What Happened (1-paragraph summary)

## Key Quotes
1. "[Direct quote showing pain or buying signal]"
2. "[Direct quote showing objection or concern]"

## Qualification Status (Updated)
[Full table from Step 3]

## 3 Whys Status
[Table from Step 4]

## Gaps to Fill (Next Meeting)
1. [Missing element] → Questions to ask: [...]

## Next Step Agreed
[Exactly what was agreed — the literal commitment]

## Objections Logged
| Type | Verbatim Quote | Stage | Response Used | Outcome |
|------|---------------|-------|--------------|---------|
| [Timing/Budget/Authority/Trust/Fit/Competition] | "[quote]" | [stage] | [response] | [result] |
```

**Note:** The `## Objections Logged` section is required — it feeds the objection-mining skill.

---

## STEP 7 — Draft Follow-up Email

Write while context is hot. Send within 2 hours.

**Subject:** "Following up: [specific topic]" or "Next steps from our conversation"

**Body:**
```
[Name],

Thanks for the time today.

To recap what we covered:
- [Key finding 1 — reference their exact words if they shared a pain]
- [What we agreed to explore]

Based on [specific thing they said], the most relevant thing for your team is [specific capability or case study].

[Proof point — from live search, not memory]:
"[Customer] solved [similar pain] and achieved [metric]." — [source URL]

Next step: [Exactly what was agreed].

[Seller name]
```

Rules:
- Send same day, ideally within 2 hours
- Reference at least 1 thing they said specifically
- One ask only — don't stack multiple CTAs

---

## STEP 8 — Update account-brief.md

1. Qualification tracker → fill in newly confirmed elements (with date)
2. "Last Interaction" → today's date + one-sentence summary
3. "Stage" → update if it changed
4. "Key Contacts" → add any new names/titles

---

## Quality Gates

- [ ] Notes saved with today's date in filename
- [ ] Qualification table filled with call evidence
- [ ] 3 Whys assessed
- [ ] At least 1 direct quote captured
- [ ] Next step documented (or flagged as missing with recovery plan)
- [ ] `## Objections Logged` section present in call notes file
- [ ] Follow-up email drafted and sent (or scheduled same day)
- [ ] account-brief.md updated
- [ ] CRM log notes drafted or synced
