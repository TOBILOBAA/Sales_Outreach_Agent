---
name: call-debrief
description: |
  Post-call debrief. Captures notes, maps to qualification framework, flags gaps, drafts follow-up email.
  Use when: just got off a call, have call notes to process, need to capture discovery output,
  want to update qualification status, need a follow-up email, or want to update CRM notes.
  Triggers: debrief, call notes, just got off, post call, call recap, capture notes,
  what happened, update MEDDPICC, follow up email after call, notes from meeting,
  call summary, discovery notes, I just spoke with.
version: 1.0.0
user-invocable: true
---

# Call Debrief

**⚠️ TIMING RULE:** Do this immediately after the call. The best debrief is in the first 15 minutes.
Memory degrades fast. Don't wait.

**⚠️ DATE RULE:** Check `currentDate`. Notes saved as `YYYY-MM-DD-{type}-notes.md`.

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

**Why this matters:** The debrief should highlight what CHANGED, not just what was said.
Compare before vs. after — that's the signal.

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
- "Is there someone internal who's clearly the champion?"
- "What else are they evaluating or already using?"

**Momentum**
- "Did they agree to a next step? What exactly?"
- "Was there a specific objection? How did it go?"
- "Any quote or thing they said that stood out?"

**Objection coaching (AECR check — for every objection mentioned):**
- "What was the exact objection?"
- "Did you acknowledge it before responding, or did you jump to the answer?"
- "What did you say back?"
- "How did they respond — did the objection go away, change, or stay?"
Reference: `references/discovery-frameworks.md` Section 7 (AECR) for in-meeting objections.

---

## STEP 3 — Map to {{QUALIFICATION_FRAMEWORK}}

Map every piece of information to the qualification framework.

**Default: MEDDPICC**

| Letter | Question | Status | Evidence from Call |
|--------|----------|--------|--------------------|
| M — Metrics | What numbers change? | ✅/⬜/🚫 | Direct quote preferred |
| E — Economic Buyer | Who approves budget? | ✅/⬜/🚫 | Name if known |
| D — Decision Criteria | How will they evaluate? | ✅/⬜/🚫 | Criteria mentioned |
| D — Decision Process | Steps to get to yes? | ✅/⬜/🚫 | Process described |
| P — Paper Process | Procurement/Legal/Security? | ✅/⬜/🚫 | Steps mentioned |
| I — Identified Pain | What specific pain? | ✅/⬜/🚫 | Quote from call |
| C — Champion | Who advocates internally? | ✅/⬜/🚫 | Name + evidence |
| C — Competition | What else evaluating or using? | ✅/⬜/🚫 | Competitor(s) named |

**Status key:**
- ✅ Confirmed — we have evidence
- ⬜ Unknown — not yet discussed
- 🚫 Negative — confirmed blocked or won't happen

---

## STEP 3.5 — MEDDPICC Deal Health Score

Score each MEDDPICC element 0–5 based on evidence from THIS call and prior notes.
**Use only confirmed evidence. Never guess.**

| Element | 0 | 1–2 | 3–4 | 5 | Score |
|---------|---|-----|-----|---|-------|
| M — Metrics | Unknown | Mentioned vaguely | Quantified in their words | ROI calculated, agreed | /5 |
| E — Economic Buyer | Unknown | Name known | Name + title + involved | Will be in next meeting | /5 |
| D — Decision Criteria | Unknown | Informal list | Formal criteria shared | We map strongly to all | /5 |
| D — Decision Process | Unknown | Steps described | Timeline confirmed | Milestone dates agreed | /5 |
| P — Paper Process | Unknown | Acknowledged exists | Steps described | Timeline confirmed | /5 |
| I — Identified Pain | Unknown | Surface symptom | Business impact confirmed | Personal impact + urgency | /5 |
| C — Champion | Unknown | Ally identified | Actively helping us | Will broker EB access | /5 |
| C — Competition | Unknown | Mentioned vaguely | Competitors named | Our position understood | /5 |

**Composite Score: ___ / 40**

**Score interpretation:**
- 0–15: Pre-qualification — do not advance stage
- 16–19: Early stage — priority: pain and champion
- 20–27: Active opportunity — work all elements
- 28–34: Strong deal — focus on EB + paper process
- 35–40: Close-ready — confirm final decision criteria

**Red flag triggers (flag ANY of these immediately):**
- Single-threaded (only 1 contact, no champion): ⚠️
- No compelling event (no external urgency driver): ⚠️
- Champion won't/can't broker EB access: ⚠️
- Decision criteria unknown after 2+ discovery calls: ⚠️
- Procurement/legal timeline unknown after verbal yes: ⚠️

**Forecast category assignment:**
- **Commit** (>90%): Score 35+/40 + next step confirmed + paper started
- **Best Case** (>60%): Score 28+/40 + champion active + EB identified
- **Upside** (<60%): Score 20+/40 + discovery complete + Why Anything ✅
- **Not Forecast**: Score < 20/40

**Forecast Category for this deal:** ___

---

## STEP 4 — 3 Whys Assessment

| Why | Status | Evidence |
|-----|--------|----------|
| Why Anything (cost of status quo) | ✅/⬜ | |
| Why {{PRODUCT_NAME}} (capability match) | ✅/⬜ | |
| Why Now (urgency driver) | ✅/⬜ | |

**Analysis:**
- All 3 ⬜ → Very early. Priority: establish pain first.
- Why Anything ✅, others ⬜ → Next meeting: Why {{PRODUCT_NAME}} and Why Now.
- All 3 ✅ → Strong discovery. Flag for AE to advance.
- Why Now ⬜ → Create urgency in follow-up: find an external event (launch date, fiscal year, competitor announcement).

---

## STEP 5 — CRM Update Notes

Output this block formatted for copy-paste into CRM (or sync via CRM MCP if configured):

```
CRM Call Log — {Date}
Call type: {Cold Call / Intro / Discovery / Follow-up}
Duration: {X min}
Attendees: {names + titles}

Summary:
[2-3 sentences: what happened, key finding, next step]

{{QUALIFICATION_FRAMEWORK}} Updates:
- I (Pain): [confirmed/updated to: ...]
- E (Economic Buyer): [identified as: ...]
- C (Champion): [identified as / not yet identified]
- Next Step: [what was agreed]

Stage Recommendation: {Research / Outreach / Engaged / Discovery / Meeting Booked / Qualified}
```

---

## STEP 6 — Save Call Notes

**File path:**
- Discovery/intro/follow-up call → `accounts/{account}/discovery/{YYYY-MM-DD}-{type}-notes.md`
  (types: cold-call, intro, discovery, follow-up)
- AE-led meeting → `accounts/{account}/meetings/{YYYY-MM-DD}-meeting-summary.md`

### Call Notes File Structure

```markdown
# Call Notes — {Company} — {Date}
**Type:** {Cold Call / Intro / Discovery / Follow-up}
**Duration:** {X min}
**Participants:** {Their names + titles} | {{SELLER_NAME}}{, {{AE_NAME}} if present}
**Energy:** {Engaged / Polite / Skeptical / Rushed}

---

**MEDDPICC Score:** ___ / 40 | **Forecast Category:** ___

## What Happened (1-paragraph summary)
[Raw summary before analysis]

## Key Quotes
1. "[Direct quote showing pain or buying signal]"
2. "[Direct quote showing objection or concern]"

## {{QUALIFICATION_FRAMEWORK}} Status (Updated)
[Full table from Step 3]

## 3 Whys Status
[Table from Step 4]

## Gaps to Fill (Next Meeting)
1. [Missing element] → Questions to ask: [...]
2. [Missing element] → Questions to ask: [...]

## Next Step Agreed
[Exactly what was agreed on the call — the literal commitment]

## Deal Health Assessment
- **MEDDPICC Score:** ___ / 40
- **Score trajectory:** ↑ Improving / → Flat / ↓ Declining vs. last call
- **Red flags:** [None / list any triggered]
- **Forecast category:** Commit / Best Case / Upside / Not Forecast
- **Key gap to close next:** [Top 1 element to fill]

## Objections Logged
| Type | Verbatim Quote | Stage | Response Used | Outcome |
|------|---------------|-------|--------------|---------|
| [Timing/Budget/Authority/Trust/Fit/Competition] | "[quote]" | [stage] | [response approach] | [result] |
```

**Note:** The "Objections Logged" section is required — it feeds the `/objection-mining` skill.

---

## STEP 7 — Draft Follow-up Email

Write this while context is hot. Send within 2 hours of the call.

**Subject line options:**
- "Following up: [specific topic discussed]"
- "Next steps from our conversation"
- "[Thing you promised to send]"

**Body:**
```
[Name],

Thanks for the time today.

To recap what we covered:
- [Key finding 1 — reference their exact words if they shared a pain]
- [Key finding 2 — what we agreed to explore]

[If you promised something: "As promised, here is [resource]."]

Based on [specific thing they said], the most relevant thing for your team is [specific capability or case study].

[Proof point in 1 sentence — MUST come from live search, not memory]:
"[Customer] solved [similar pain] and achieved [metric]." — [source URL]

Next step: [Exactly what was agreed]. I'll send a calendar invite for [time if agreed].

[If next step wasn't clear]: "Would [day/time] work for a [X min] call to go deeper on [specific topic]?"

{{SELLER_NAME}}
```

**Rules:**
- Send same day. Ideally within 2 hours.
- Reference at least 1 thing they said specifically (shows you listened)
- One ask only — don't stack multiple CTAs

---

## STEP 8 — Update account-brief.md

Edit `accounts/{account}/account-brief.md`:
1. {{QUALIFICATION_FRAMEWORK}} tracker → fill in newly confirmed elements (with date)
2. "Last Interaction" → today's date + one-sentence summary
3. "Stage" → update if it changed
4. "Key Contacts" → add any new names/titles/info
5. "Top Pain Signal" → update if a clearer pain emerged

---

## STEP 9 — Create CRM Task

Via {{CRM_SYSTEM}} MCP (if configured) or as a paste-ready block:

Create tasks for any commitments made on the call:
- Follow-up email (if not yet sent)
- Resources to send
- Next meeting to schedule
- Research needed for next interaction

Set: account name, due date, priority, assigned to ({{SELLER_NAME}} or {{AE_NAME}}).

---

## Quality Gates

- [ ] Notes saved with today's date in filename
- [ ] {{QUALIFICATION_FRAMEWORK}} table filled with call evidence
- [ ] 3 Whys assessed (all 3 rows)
- [ ] At least 1 direct quote captured
- [ ] Next step documented (or flagged as missing with recovery plan)
- [ ] "## Objections Logged" section present in call notes file
- [ ] Follow-up email drafted and sent (or scheduled same day)
- [ ] account-brief.md updated (qualification status + last interaction)
- [ ] CRM log notes drafted (paste-ready or synced)
- [ ] CRM task created for any commitments made on call
- [ ] MEDDPICC deal score calculated (0–40) and recorded in call notes header
- [ ] Red flags explicitly surfaced to seller (or "None" confirmed)
