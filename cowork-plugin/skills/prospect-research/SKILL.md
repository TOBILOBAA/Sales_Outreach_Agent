---
name: prospect-research
description: Full account research sweep using live data. Trigger with "research [company]", "deep scan [company]", "what's the hook for [company]", "who should I target at [company]", "add account [company]", or "tell me about [company]".
version: 1.0.0
---

# Prospect Research

**⚠️ DATA RULE:** Never trust pre-training knowledge for current company state. Always pull live data.
Pre-training is stale. Internal knowledge first → web research second → synthesize third.

---

## STEP 0 — Confirm Account and Goal

Before any research:
1. Confirm the account name (exact spelling — becomes the folder path in kebab-case)
2. Initial research or a refresh?
3. Check if `accounts/{account-name}/` already exists

If no folder exists → create the structure now:
```
accounts/{account-name}/
├── account-brief.md
├── research/
├── discovery/
├── meetings/
└── emails/
```

---

## STEP 1 — Internal Knowledge First

Check what already exists before going to the web:

**~~CRM (if connected):**
- Search for existing relationship, open opportunities, past interactions
- Pull any contact records

**Local files:**
- `accounts/{account}/` — prior research files, call notes, meeting briefs
- `knowledge/competitive/` — relevant battlecards
- `knowledge/personas/` — ICP persona guides

---

## STEP 2 — Web Research

**Detect mode:** Is ~~web research (Bright Data) connected?

### FULL MODE (~~web research connected)

Run these searches in parallel:
```
1. "{Company} tech stack {seller's solution category} 2025 2026"
2. "{Company} engineering hiring jobs 2026"
3. "{Company} news funding announcement 2026"
4. "{Company} CTO VP Engineering Chief Architect"
5. "{Company} {solution category} challenge problem pain"
6. "{Company} AI machine learning 2026"
7. "{seller's company} {company industry} case study customer"
8. "{Company} engineering blog AI machine learning 2026"
9. "{Company} hiring AI engineer vector LLM RAG embedding 2026"
10. "{Company} {CTO or VP name} blog post LinkedIn article 2026"
```

Then scrape for depth:
- Company website → About, Engineering, Careers pages
- Recent blog posts (prioritize AI/engineering content)
- Press releases from last 90 days
- LinkedIn company page (if accessible)

### LITE MODE (no ~~web research — built-in web search)

```
1. "{Company} tech stack 2026"
2. "{Company} CTO VP Engineering LinkedIn"
3. "{Company} news funding 2026"
4. "{Company} {solution category} use case"
5. "{Company} engineering blog AI"
```

Note in output: "⚠️ Lite mode — search results only, no page scraping. Lower signal quality."

**Key signals to find:**
- [ ] Confirmed tech stack (not assumed)
- [ ] Engineering headcount and growth trajectory
- [ ] AI/ML initiatives
- [ ] Recent funding, product launches, leadership changes
- [ ] Engineering leadership names + any recent changes
- [ ] People publishing about relevant topics
- [ ] Job postings mentioning specific tools → reveals architecture decisions

---

## STEP 3 — FITS Scoring

Score the account before writing the research file:

| Dimension | Score (0–25) | What to assess |
|-----------|-------------|----------------|
| **F — Firmographic Fit** | /25 | Industry, company size, stage, headcount match the ICP from seller profile |
| **I — Intent Signals** | /25 | Active hiring, product launch, funding, leadership change, competitor eval |
| **T — Timing** | /25 | Urgency window — is there a forcing function? |
| **S — Solution Match** | /25 | Is their confirmed pain solvable by the seller's product? |

**Tiers:** 80+ = Tier 1 (prioritize) | 60–79 = Tier 2 | 40–59 = Tier 3 | <40 = Tier 4

---

## STEP 4 — Synthesize and Save

**Output path:** `accounts/{account-name}/research/{YYYY-MM-DD}-initial-research.md`

### Required sections (write-outreach reads these):

```markdown
# {Company} — Research
**Date:** {YYYY-MM-DD} | **Mode:** Full / Lite

---

## Key Signals
[Fresh, time-sensitive findings. Lead with most recent.]

## Company Overview
[2-3 sentences: what they do, size, stage, HQ]

## Tech Stack (Confirmed)
| System | Technology | Source |
|--------|-----------|--------|

## Leadership Contacts
| Name | Title | Relevance | Source |
|------|-------|-----------|--------|

## People Publishing About Relevant Topics
| Name | Title | Topic | Link | Why It Matters |
|------|-------|-------|------|----------------|

## Job Postings (Architecture Intelligence)
| Role | Tools Mentioned | Posted | Implication |
|------|----------------|--------|-------------|

## Pain Signals (Research-Confirmed)
1. [Pain] → Source: [URL]

## Sales Opportunity Analysis
**FITS Score:** /100 | **ICP Tier:** 1/2/3/4
**Sales Motion Route:** Classic / Sprint / Fast / Unknown
**Value Driver:** Make Money / Save Money / Go Fast / Be Safe
**Why Anything:** [What breaks if they do nothing?]
**Why Product:** [Which capability matches their pain?]
**Why Now:** [What external event creates urgency?]

## Top 3 Outreach Hooks
1. [Specific person + specific signal + specific angle. Ready to use.]
2.
3.

## Recommended First Contact
**Who:** [Name + title]
**Channel:** LI / Email / Cold Call
**Hook:** [One-liner]

## Sources
- [URL or document with description]
```

---

## STEP 5 — Update account-brief.md

After saving the research file:
- Add/update FITS score and ICP tier
- Add any new confirmed contacts
- Update "Last Updated" date
- Update "Top Pain Signal" and "Top Hook" fields

---

## Quality Gates

- [ ] Internal knowledge checked before web research
- [ ] At least 5 queries run (full mode: 10+)
- [ ] Tech stack confirmed from source — not assumed
- [ ] At least 1 pain signal cited with source URL
- [ ] FITS score calculated with reasoning per dimension
- [ ] Sales motion route stated with reasoning
- [ ] All required chain interface sections present
- [ ] account-brief.md updated
- [ ] No invented metrics
