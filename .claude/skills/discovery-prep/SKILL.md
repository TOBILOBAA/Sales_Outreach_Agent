---
name: discovery-prep
description: |
  Builds a complete meeting brief before any discovery, intro, or follow-up call. Never walk in blind.
  Use when: preparing for a discovery call, intro meeting, follow-up, or AE-led meeting.
  Includes: exec summary, agenda, qualification gap analysis, key questions, objections, proof points.
  Triggers: prep, meeting prep, discovery prep, prepare for, call prep, before meeting,
  discovery call, intro meeting, meeting brief, what should I know, going into a call, prep me.
version: 1.0.0
user-invocable: true
---

# Discovery Prep

**⚠️ DATA RULE:** The worst thing that can happen in a meeting is being surprised.
Pull everything. Find the latest news. Miss nothing.

**⚠️ DATE RULE:** Check `currentDate`. Output file named `YYYY-MM-DD-meeting-brief.md`.
Don't use training knowledge for "latest news" — always pull live data.

---

## STEP 0 — Confirm Meeting Details

Ask if not provided:
1. Account name + type of meeting (intro / discovery / follow-up / AE-led)
2. Date and time
3. Who's on the call (their side + your side)
4. How did this meeting get booked? What's the context?

---

## STEP 1 — Internal Knowledge Refresh

Check all existing intel before going to the web:

**CRM (if MCP configured):**
- Latest account status, open opportunities, stage
- Contact history and relationship depth
- Previous objections documented
- Internal notes from AE or previous touches

**Local files:**
- `accounts/{account}/account-brief.md` → full qualification status
- `accounts/{account}/research/` → most recent research file
- `accounts/{account}/discovery/` → all prior call notes
- `accounts/{account}/meetings/` → prior meeting briefs

**Build picture before Step 2:**
- What do we know vs. what are we guessing?
- Which {{QUALIFICATION_FRAMEWORK}} elements are confirmed vs. blank?
- What was the goal of the last interaction?

---

## STEP 2 — Fresh External Intel (Last 30 Days)

Search for anything published recently about the company or attendees:

**Full mode (Bright Data):**
```
mcp__brightdata__search_engine:
1. "{Company} news 2026"
2. "{Company} funding announcement 2026"
3. "{Company} engineering hiring 2026"
4. "{Attendee names} LinkedIn blog post conference 2026"
5. "{{COMPANY_NAME}} {Company industry} case study customer story"
6. "{{COMPANY_NAME}} {their tech stack} replaced migration customer"
```

**Lite mode (WebSearch):**
```
Same queries via WebSearch tool
```

**Goal:** Find at least 1 warm-up talking point from the last 30 days.
Find at least 1 proof point that specifically matches their industry or tech stack.

---

## STEP 2.5 — Draft Upfront Contract Opener

Before building the agenda, draft the upfront contract for this specific call.
Reference: `references/discovery-frameworks.md` Section 4.

**Template (fill in before the call):**
> "[Name], I want to make sure this is a good use of your time.
> I'll spend [X minutes] understanding [their specific situation based on research].
> Then I'll share [specific thing: 1-2 examples / a capability / how similar companies solved this].
> At the end, either this makes sense to explore — and we'll agree on a next step — or it doesn't, and we'll both know that. Either outcome is fine.
> Does that work?"

**Fill in before the call:**
- Their specific situation: ___
- What you'll share: ___
- Proposed next step if it goes well: ___

---

## STEP 3 — {{QUALIFICATION_FRAMEWORK}} Gap Analysis

Map current knowledge. Mark each element:
✅ Confirmed | ⬜ Unknown | 🎯 Probe in this meeting | 🚫 Negative signal

**Default: MEDDPICC**

| Letter | Question | Status | What We Know | Goal for This Meeting |
|--------|----------|--------|--------------|----------------------|
| M — Metrics | What numbers change if they fix this? | | | |
| E — Economic Buyer | Who approves budget? On the call? | | | |
| D — Decision Criteria | How will they evaluate options? | | | |
| D — Decision Process | What steps to get to yes? Timeline? | | | |
| P — Paper Process | Procurement/legal/security steps? | | | |
| I — Identified Pain | What specific pain in their words? | | | |
| C — Champion | Who advocates internally? | | | |
| C — Competition | What else are they evaluating? | | | |

**Goal for this meeting:** Fill at least 3 blank elements.
**Priority:** Confirm I (Identified Pain) first. Everything else depends on it.

---

## STEP 4 — 3 Whys Status

| Why | Status | Evidence |
|-----|--------|----------|
| Why Anything (cost of status quo) | ✅/⬜ | |
| Why {{PRODUCT_NAME}} (capability match) | ✅/⬜ | |
| Why Now (urgency driver) | ✅/⬜ | |

If any Why is ⬜ → it becomes a goal for this meeting.

---

## STEP 5 — Build the Meeting Brief

**Save as:** `accounts/{account}/meetings/{YYYY-MM-DD}-meeting-brief.md`

```markdown
# Meeting Brief — {Company} {Meeting Type}
**Date/Time:** {date and time}
**Duration:** {duration}
**Type:** Intro / Discovery / Follow-up / AE-led

## Attendees
| Name | Role | Our Side |
|------|------|----------|
| [Their name] | [Title] | {{SELLER_NAME}} / {{AE_NAME}} |

## Executive Summary
[1 paragraph: who they are, where we are in the cycle, top 1-2 signals, meeting goal]

## Hot Signals to Reference (open with one)
1. [Signal 1 — dated, confirmed from research]
2. [Signal 2]

## Meeting Goals
1. Confirm: [{{QUALIFICATION_FRAMEWORK}} element]
2. Confirm: [{{QUALIFICATION_FRAMEWORK}} element]
3. Establish: [Which Why needs to be built]
4. Close with: [Specific CTA]

## Recommended Agenda
| Time | Topic | Owner |
|------|-------|-------|
| 0:00 | Warm up — reference [hot signal] | {{SELLER_NAME}} |
| 0:03 | Purpose framing: "Here's why we asked for this time…" | {{AE_NAME}} |
| 0:08 | Discovery (see questions below) | {{AE_NAME}} |
| 0:25 | Value — 1-2 specific capabilities matched to their pain | {{AE_NAME}} |
| 0:35 | Proof point: [Customer story from live search] | {{AE_NAME}} |
| 0:40 | Objection handling | {{AE_NAME}} |
| 0:50 | Next step | {{AE_NAME}} |

## Discovery Questions ({{QUALIFICATION_FRAMEWORK}}-mapped)

### Pain (I — Identified Pain)
- "Walk me through what [their process] looks like today — step by step."
- "What breaks first when [their scale challenge] happens?"
- "What have you tried to solve this? What worked, what didn't?"

**SPIN Implication questions** (ask after they confirm a problem):
- "If [problem] keeps happening, what does that mean for [their team / their metric]?"
- "What's the downstream impact on [adjacent process] when this breaks?"
- "How often does this happen — and what does each occurrence cost?"

**Sandler Level 2 (business impact) — ask after Level 1 surface pain:**
- "What does that mean for the business? Revenue, cost, or risk?"
- "Is this something leadership has noticed? How does it come up?"

**Sandler Level 3 (personal/emotional) — only with rapport, only with champion:**
- "How does this affect you personally when it happens?"
- "What would it mean for you and your team if this was solved by [their timeline]?"

**60/40 check:** If you've asked 3 questions in a row and they've given short answers, stop and say:
> "I've been asking a lot — what's your reaction so far? What matters most to you here?"

### Metrics (M)
- "If you fixed [pain], what would that mean in hours/dollars/time?"
- "How are you measuring success for [project]?"

### Economic Buyer (E)
- "When a decision like this comes up, who else gets involved?"
- "Who would ultimately sign off on something like this?"

### Decision Process (D) + Paper Process (P)
- "If this conversation goes well, what would next steps look like on your end?"
- "Is there a timeline you're working toward?"
- "What does procurement/legal look like for something like this?"

### Competition (C)
- "What else are you evaluating? What does your stack look like today?"

### Champion (C)
- "Who on your team would be most involved in evaluating this?"

## Expected Objections

| Objection | Response |
|-----------|----------|
| "We're happy with [current system]" | "What would have to be true for you to consider alternatives?" |
| "No budget right now" | "Understood — is this a timing question or a priority question?" |
| "We're evaluating X" | "What's your evaluation criteria? We'd love to make sure {{PRODUCT_NAME}} is in the mix." |
| [Add objections from research/prior calls] | |

## Competitive Prep

*Reference: `references/competitive-positioning.md` + `knowledge/competitive/` battlecards*

| Competitor | Zone | FIA Position | Landmine Question |
|-----------|------|-------------|------------------|
| [Name] | Winning / Battling / Losing | [FIA reframe in 1 sentence] | [1 question that surfaces their weakness] |

**If no competitor in play:** Leave this section blank. Do not invent a competitor.

## Proof Points Ready

**Source priority:** Live search (company case studies page) → CRM proof points → references/proof-points.md

1. **[Customer]** — [metric from live search] — use when: [moment in conversation] — Source: [URL]
2. **[Customer]** — [metric] — use when: [moment] — Source: [URL]

## Sales Motion Route + CTA
**Route:** Classic / Sprint / Fast / Unknown
**Proposed CTA:**
- Classic → "Let's schedule a Technical Workshop with our solutions team."
- Sprint → "Let's lock in a Sprint Zero — 3 hours to scope this properly."
- Fast → "Let's schedule a kickoff — what's your timeline?"
- Unknown → "Would a 30-min follow-up to go deeper on [topic] make sense?"

## {{QUALIFICATION_FRAMEWORK}} Pre-Meeting Status
[Copy gap analysis table from Step 3]

## After the Call
→ Run `/call-debrief` immediately while context is hot.
```

---

## STEP 6 — Day-of Checklist

Print or pin before the call:
- [ ] Hot signal to open with: ___
- [ ] First discovery question: ___
- [ ] Economic buyer name to confirm: ___
- [ ] Proof point ready: ___
- [ ] CTA to close with: ___
- [ ] Next step to propose: ___

---

## Quality Gates

- [ ] All existing account files read before searching the web
- [ ] Fresh external intel checked (at least 1 thing from last 30 days)
- [ ] {{QUALIFICATION_FRAMEWORK}} gap analysis complete with goals for each unknown
- [ ] At least 3 discovery questions per element you need to fill
- [ ] At least 2 objections prepared with responses
- [ ] At least 1 proof point from live search matched to their profile
- [ ] Sales Motion Route and CTA mapped
- [ ] Meeting brief saved to `meetings/` with today's date
- [ ] Upfront contract drafted (Step 2.5 template filled in)
- [ ] At least 2 implication/impact questions in the discovery question set
