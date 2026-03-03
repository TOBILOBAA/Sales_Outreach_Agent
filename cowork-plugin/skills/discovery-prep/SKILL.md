---
name: discovery-prep
description: Builds a complete meeting brief before any sales call. Never walk in blind. Trigger with "prep me for [company]", "meeting prep for [company]", "call prep [company]", "prepare for my call with [company]", "going into a call with [company]", or "what should I know before [company]".
version: 1.0.0
---

# Discovery Prep

**⚠️ DATA RULE:** The worst thing that can happen in a meeting is being surprised.
Pull everything. Find the latest news. Miss nothing.

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

**~~CRM (if connected):**
- Latest account status, open opportunities, stage
- Contact history and relationship depth
- Previous objections documented
- Internal notes from prior touches

**Local files:**
- `accounts/{account}/account-brief.md` → full qualification status
- `accounts/{account}/research/` → most recent research file
- `accounts/{account}/discovery/` → all prior call notes
- `accounts/{account}/meetings/` → prior meeting briefs

**Build this picture before Step 2:**
- What do we know vs. what are we guessing?
- Which qualification elements are confirmed vs. blank?
- What was the goal of the last interaction?

---

## STEP 2 — Fresh External Intel (Last 30 Days)

Search for anything published recently about the company or attendees:

If ~~web research is connected:
```
1. "{Company} news 2026"
2. "{Company} funding announcement 2026"
3. "{Company} engineering hiring 2026"
4. "{Attendee names} LinkedIn blog post conference 2026"
5. "{seller's company} {company industry} case study customer story"
```

If not: use built-in web search with the same queries.

**Goal:** Find at least 1 warm-up talking point from the last 30 days.
Find at least 1 proof point that matches their industry or tech stack.

---

## STEP 3 — Qualification Gap Analysis

Map current knowledge using the qualification framework from seller profile.
Mark each element: ✅ Confirmed | ⬜ Unknown | 🎯 Probe in this meeting | 🚫 Negative signal

Default framework: MEDDPICC

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

**Goal:** Fill at least 3 blank elements.
**Priority:** Confirm Identified Pain first. Everything else depends on it.

---

## STEP 4 — 3 Whys Status

| Why | Status | Evidence |
|-----|--------|----------|
| Why Anything (cost of status quo) | ✅/⬜ | |
| Why Product (capability match) | ✅/⬜ | |
| Why Now (urgency driver) | ✅/⬜ | |

If any Why is ⬜ → it becomes a goal for this meeting.

---

## STEP 5 — Build the Meeting Brief

**Save as:** `accounts/{account}/meetings/{YYYY-MM-DD}-meeting-brief.md`

```markdown
# Meeting Brief — {Company} {Meeting Type}
**Date/Time:** {date and time}
**Type:** Intro / Discovery / Follow-up / AE-led

## Attendees
| Name | Role | Our Side |
|------|------|----------|
| [Their name] | [Title] | [Seller name / AE name] |

## Executive Summary
[1 paragraph: who they are, where we are, top 1-2 signals, meeting goal]

## Hot Signals to Reference (open with one)
1. [Signal 1 — dated, confirmed]
2. [Signal 2]

## Meeting Goals
1. Confirm: [qualification element]
2. Confirm: [qualification element]
3. Establish: [Which Why needs to be built]
4. Close with: [Specific CTA]

## Recommended Agenda
| Time | Topic | Owner |
|------|-------|-------|
| 0:00 | Warm up — reference [hot signal] | Seller |
| 0:03 | Purpose framing | AE |
| 0:08 | Discovery questions | AE |
| 0:25 | Value — 1-2 capabilities matched to pain | AE |
| 0:35 | Proof point (from live search) | AE |
| 0:40 | Objection handling | AE |
| 0:50 | Next step | AE |

## Discovery Questions (mapped to qualification framework)

### Pain (Identified Pain)
- "Walk me through what [their process] looks like today — step by step."
- "What breaks first when [their scale challenge] happens?"
- "What have you tried to solve this? What worked, what didn't?"

### Metrics
- "If you fixed [pain], what would that mean in hours/dollars/time?"

### Economic Buyer
- "Who else gets involved when a decision like this comes up?"

### Decision Process + Paper Process
- "If this conversation goes well, what would next steps look like on your end?"
- "What does procurement/legal look like for something like this?"

### Competition
- "What else are you evaluating? What does your stack look like today?"

### Champion
- "Who on your team would be most involved in evaluating this?"

## Expected Objections
| Objection | Response |
|-----------|----------|
| "We're happy with [current system]" | "What would have to be true for you to consider alternatives?" |
| "No budget right now" | "Is this a timing question or a priority question?" |

## Proof Points Ready
1. **[Customer]** — [metric from live search] — use when: [moment] — Source: [URL]
2. **[Customer]** — [metric] — use when: [moment] — Source: [URL]

## Sales Motion Route + CTA
**Route:** Classic / Sprint / Fast / Unknown
- Classic → "Let's schedule a Technical Workshop."
- Sprint → "Let's lock in a Sprint Zero — 3 hours to scope this."
- Fast → "Let's schedule a kickoff — what's your timeline?"
- Unknown → "Would a 30-min follow-up to go deeper on [topic] make sense?"

## Qualification Gap Analysis
[Copy from Step 3]

## After the Call
→ Run /call-debrief immediately while context is hot.
```

---

## STEP 6 — Day-of Checklist

- [ ] Hot signal to open with: ___
- [ ] First discovery question: ___
- [ ] Economic buyer name to confirm: ___
- [ ] Proof point ready: ___
- [ ] CTA to close with: ___

---

## Quality Gates

- [ ] All existing account files read before web research
- [ ] Fresh external intel checked (at least 1 thing from last 30 days)
- [ ] Qualification gap analysis complete with meeting goals per unknown
- [ ] At least 3 discovery questions per element to fill
- [ ] At least 2 objections prepared with responses
- [ ] At least 1 proof point from live search matched to their profile
- [ ] Sales Motion Route and CTA mapped
- [ ] Meeting brief saved with today's date
