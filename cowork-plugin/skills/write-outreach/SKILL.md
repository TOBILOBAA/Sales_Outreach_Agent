---
name: write-outreach
description: Drafts hyper-personalized outreach across all 4 channels. Always reads research file first. Never generic. Trigger with "write outreach for [contact] at [company]", "cold email to [name]", "LinkedIn message for [contact]", "cold call script for [company]", or "outreach for [contact]".
version: 1.0.0
---

# Write Outreach

**⚠️ DATA RULE:** Do NOT write a single message without first reading the account's research file.
Every message must reference at least one research-confirmed signal. Generic = deleted.

**⚠️ BANNED:** Check `references/banned-phrases.md`. Any banned phrase → rewrite from scratch.

**⚠️ METRICS RULE:** Never invent numbers. Only use verified proof points from `references/proof-points.md`
or a live search. Find the most specific match to this account first.

---

## STEP 0 — Gather Context

Ask if not provided:
1. Contact name + title + company
2. Channels needed: LI connection / InMail / Email / Cold Call (default: all 4)
3. Any specific angle to focus on?

---

## STEP 1 — Check ~~CRM / DNC

If ~~CRM is connected:
- Search for this contact — existing relationship or AE ownership?
- Check for any "do not contact" flags

**🛑 STOP if contact is AE-owned or flagged.** Tell seller: "This contact is owned/flagged. Coordinate before reaching out."

---

## STEP 2 — Read Research File

Find and read the most recent research file in `accounts/{account}/research/`.

Extract:
- **Tech Stack** → what they're running
- **Pain Signals** → confirmed, cited pains
- **Top 3 Outreach Hooks** → ready-to-use angles
- **Leadership Contacts** → this contact's role + relevance
- **Sales Motion Route** hypothesis
- **Value Driver** for their profile

If no research file exists → run `/research` first, then return here.

---

## STEP 2.5 — Live Proof Point Search

Run before writing. Never default to the first proof point you remember.

Priority order (most specific wins):
1. Scrape the seller's company case study page — filter by prospect's industry and use case
2. Web search: "[seller's company] [prospect industry] case study" and "[seller's company] [their tech stack] migration"
3. Check ~~CRM for internal proof points
4. Fall back to `references/proof-points.md` only if no live match

---

## STEP 3 — Select the Hook

Hook selection priority:
1. **Personal signal:** Did they publish a blog post, speak at a conference, post on LinkedIn?
2. **Company signal:** Recent product launch, funding, job posting, news (from research file)
3. **Technical signal:** A specific tool they use that has a known pain
4. **Role signal:** What does someone in this title care about most? (from references/buyer-personas.md)

Never use a signal you haven't confirmed from research or live data.

---

## STEP 4 — Map to Framework

Before writing, confirm:
- **Sales Motion Route:** Classic / Sprint / Fast
- **Value Driver:** Make Money / Save Money / Go Fast / Be Safe
- **Pain:** 1 specific confirmed pain (not a guess)
- **Proof Point:** 1 relevant customer from live search or proof-points.md
- **3 Whys status:** Why Anything confirmed? Why Product confirmed? Why Now confirmed?
  If Why Now is ⬜ → urgency must come from the hook

---

## STEP 5 — Write All Variants

### A) LinkedIn Connection Request (≤300 chars — count every character)

Pattern:
```
[Name], [hot signal in 1 clause]. [pain as question or curiosity hook]. [1 proof point]. Worth connecting?
```

Exec contacts: aim for ≤200 chars.

---

### B) LinkedIn InMail (≤500 words, target 200–300)

**Subject line:** Pain hypothesis as a question. Never: product name, "introduction", "checking in".

**Body:**
1. Hook (1 sentence — reference the research signal)
2. Pain statement (what's the friction for their role, 2 sentences)
3. Evidence (2–3 bullets: what peers at their stage did + metric)
4. CTA (one ask: 15–20 min call with the AE or seller)

---

### C) Cold Email (≤400 words, target 200–250)

**Subject:** `[quantified pain] at [company]?` or `[hook signal as question]?`
Never: product name, "checking in", "following up".

**Body:**
```
[Name],

[1 sentence: reference the signal — why you're writing NOW]

[Pain sentence: what breaks for them right now, in their language]

Two things relevant to [Company]:
1. [Specific insight/finding from research]
2. [Proof point: Customer + metric + why it's relevant]

[Seller's name] works with [their type of] teams.
Would a 20-min call this week make sense?

[Seller name + title + contact]
```

Optional P.S.: `"P.S. [Specific thing from research that shows you paid attention]."`

---

### D) Cold Call Script

Build from `references/cold-call-framework.md`:
- Pattern interrupt → Bridge (specific signal) → Pain + outcome → Soft ask
- AAA objection handling for likely objections for their role
- Voicemail variant (20-30 sec max)

---

## STEP 6 — Save, Update, Create CRM Tasks

**Save file:** `accounts/{account}/emails/{YYYY-MM-DD}-{contact-name}-outreach.md`
**Update:** `accounts/{account}/account-brief.md` → add to outreach log section

**Create 2 tasks** via ~~CRM (or output as paste-ready block):

Task 1 — Day 1 Send:
```
"Send outreach — {Contact} @ {Company} (Day 1: LI + Email)"
Due: Today | Priority: High | Notes: File path + LI URL
```

Task 2 — Day 3 Call:
```
"Call — {Contact} @ {Company} (Day 3 follow-up)"
Due: Today + 3 days | Notes: Cold call script in outreach file
```

---

## Quality Gates

- [ ] ~~CRM/DNC checked
- [ ] Research file read — at least 1 confirmed signal used
- [ ] Live proof point searched — most specific match found
- [ ] LI connection ≤300 chars (counted)
- [ ] Email subject does NOT mention product name or "checking in"
- [ ] Cold call has pattern-interrupt opener (not "How are you?")
- [ ] At least 1 proof point with metric and source
- [ ] No banned phrases (checked against references/banned-phrases.md)
- [ ] Sales Motion Route and Value Driver mapped
- [ ] Output file saved
- [ ] 2 CRM tasks created or output as paste-ready block
