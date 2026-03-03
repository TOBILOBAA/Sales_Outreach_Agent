---
name: social-selling
description: LinkedIn engagement ladder and weekly social plan for warming up accounts before cold outreach. Trigger with "LinkedIn plan for [company]", "social selling plan for [company]", "warm path for [company]", "engagement plan for [company]", or "weekly social plan".
version: 1.0.0
---

# Social Selling

**Purpose:** Warm up accounts before cold outreach. Turn strangers into familiar faces.
The engagement ladder runs 2–4 weeks before the first direct message.

**Rule:** Every engagement must reference something real and relevant from research.
Generic likes get ignored. Specific, thoughtful engagement gets remembered.

---

## STEP 0 — Confirm Scope

1. **Single account:** "LinkedIn plan for [company]"
   → Build engagement ladder for 1–3 target contacts at that account
2. **Weekly territory plan:** "Social selling plan for this week"
   → Identify top 3–5 accounts for social engagement and plan actions

---

## STEP 1 — Research Warm Signal Sources

For each target account, read:
- `accounts/{account}/research/` → most recent research file
- `accounts/{account}/account-brief.md` → contacts and relationship status

Look specifically for:
- **Published content:** Blog posts, LinkedIn articles, conference talks
- **Recent company news:** Product launches, funding, hiring announcements
- **Community involvement:** Speakers at events, open source contributors, podcast guests
- **Mutual connections:** People in common network (if LinkedIn is connected)

These are the raw material for authentic engagement.

---

## STEP 2 — Engagement Ladder

For each target contact, build a 2–4 week sequence:

| Week | Action | Why |
|------|--------|-----|
| Week 1 | **Follow + Like** a recent post | Appears in notifications — zero friction |
| Week 1-2 | **Comment** on a specific post | Visible to their network + shows you read it |
| Week 2 | **Share/repost** with a relevant comment | Highest signal — you amplified their work |
| Week 3 | **Warm DM** (1–2 sentences, reference the content) | Now you're familiar, not cold |
| Week 3-4 | **Connection request** (after DM or engagement) | Much higher accept rate |
| Week 4+ | **InMail or Email** (after connecting) | Now genuinely warm |

**Comment quality rules:**
- Bad: "Great post!" (ignored)
- Bad: "Interesting perspective!" (ignored)
- Good: "[Specific thing they said] — we saw the same pattern at [comparable context]. The part about [specific point] is especially relevant given [current industry trend]."
- Good: Add something they didn't mention: "One thing I'd add is [related insight from research]."

---

## STEP 3 — Content-Based Conversation Starters

For each warm signal found in research, draft a conversation starter:

```
Signal: [Blog post / Conference talk / Product launch / Hiring announcement]
Contact: [Name + Title]
Engagement action: [Like / Comment / Share / DM]
Message draft:
  "[Name], [reference their specific content + what stood out].
  [1 sentence connecting it to a relevant trend or question].
  [Optional: soft question or observation — NOT a pitch]"

Do NOT include: product mentions, "I noticed you..." opener, any ask
```

---

## STEP 4 — Warm Path Mapping

Identify the shortest path to this contact beyond direct outreach:

1. **Mutual connections** — someone who knows both of you
2. **Community overlap** — same Slack groups, industry forums, event attendance
3. **Content engagement** — they commented on your content, or vice versa
4. **Event path** — attending the same upcoming conference or webinar
5. **Referral** — someone you know can make an introduction

Document each path found in `accounts/{account}/account-brief.md` → Key Contacts section.

---

## STEP 5 — Weekly Territory Social Plan

```markdown
# Social Selling Plan — Week of {YYYY-MM-DD}

## This Week's Focus Accounts
[Prioritized by ICP tier + warm signal recency]

| Account | Target Contact | Tier | Signal | Planned Action | Timing |
|---------|---------------|------|--------|----------------|--------|

## Day-by-Day Actions
Monday: [Account — Action — Content to engage with]
Tuesday: [Account — Action]
Wednesday: [Account — Action]
Thursday: [Account — Action]
Friday: [Account — Action — Review responses, plan follows]

## Warm Up Progress
| Account | Contact | Last Engagement | Next Step | Target Cold Outreach Date |
|---------|---------|----------------|-----------|--------------------------|
```

---

## STEP 6 — Save Output

**Single account plan:** `accounts/{account}/emails/{YYYY-MM-DD}-social-plan.md`
**Weekly territory plan:** `memory/territory-signals.md` → append social plan section

---

## Quality Gates

- [ ] All engagement actions reference specific research-confirmed content
- [ ] No product pitch in any engagement message
- [ ] Ladder respects timing (don't rush from like to DM in 1 day)
- [ ] Warm paths documented in account-brief.md
- [ ] Weekly plan is ICP-tier-weighted (Tier 1 accounts get more attention)
- [ ] Output file saved with today's date
