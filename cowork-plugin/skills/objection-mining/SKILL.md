---
name: objection-mining
description: Aggregates objections from call notes across territory and builds a living response library. Trigger with "what are they pushing back on", "objection library", "log this objection", "what objections am I seeing", "objection patterns", or "update my objection library".
version: 1.0.0
---

# Objection Mining

**Purpose:** Turn individual objections from every call into a territory-wide pattern library.
Every call is a data point. This skill connects them.

**Input:** `## Objections Logged` sections in all `accounts/*/discovery/` files.
**Output:** `memory/objection-library.md` — append only, never overwrite.

---

## STEP 0 — Confirm Scope

1. **Single account:** "Log the objection from my last call with [company]"
   → Read most recent `discovery/` file for that account only
2. **Territory sweep:** "Update my objection library" or "What are they pushing back on?"
   → Scan all `accounts/*/discovery/` files

---

## STEP 1 — Scan Call Notes Files

Read all files matching `accounts/*/discovery/*.md`.

For each file, look for the `## Objections Logged` section:

```
## Objections Logged
| Type | Verbatim Quote | Stage | Response Used | Outcome |
```

If no section found → skip it. If found → extract all rows.

**Types:** Timing / Budget / Authority / Trust / Fit / Competition

---

## STEP 2 — Parse and Classify

For each objection row:
1. Confirm or correct the Type classification
2. Note the Stage (what deal stage was this raised at?)
3. Note the Response Used and Outcome
4. Check if new or a variant of an existing one

| Type | Description | Example |
|------|-------------|---------|
| Timing | "Not now" | "We're heads-down until Q3" |
| Budget | Cost or prioritization block | "No budget allocated this year" |
| Authority | Needs escalation | "I'd need to check with my manager" |
| Trust | Skepticism | "We've heard this before and it didn't deliver" |
| Fit | Genuine mismatch concern | "We're too small / too big for this" |
| Competition | Evaluating an alternative | "We're already evaluating [competitor]" |

---

## STEP 3 — Aggregate into Library

Read `memory/objection-library.md` (create if doesn't exist).

For each objection:
- Find the matching entry or create a new one
- Increment count
- Add the new verbatim quote
- Update win/loss pattern if outcome is known

**Library format:**

```markdown
# Objection Library
*Last updated: YYYY-MM-DD | {N} objections tracked | {N} accounts*

---

## Timing Objections
**Count:** {N} | **Win rate:** {N}% | **Most common stage:** {stage}

### Most Common Responses (by win rate)
1. [Response that worked — with example]
2. [Second best response]

### Verbatim Quotes (latest 5)
- "[Quote]" — {Company}, {Stage}, {Date}

---

## Budget Objections
[Same structure]

## Authority Objections
[Same structure]

## Trust Objections
[Same structure]

## Fit Objections
[Same structure]

## Competition Objections
[Same structure]

---

## Top 5 Objections by Frequency

| Rank | Objection | Type | Count | Win Rate | Best Response |
|------|-----------|------|-------|----------|--------------|
| 1 | | | | | |
```

---

## STEP 4 — Generate Response Templates

For any objection type where Count ≥ 3 AND no "Best Response" is documented:

Generate a template using the AAA framework:
```
Type: [Timing/Budget/Authority/Trust/Fit/Competition]
Pattern: "[Common version of this objection]"

AAA Response:
- Acknowledge: "[Validate without agreeing]"
- Ask: "[Reframe question to understand root cause]"
- Advance: "[Earn the next 30 seconds]"

Outcome goal: [What constitutes a win for this objection]
```

---

## STEP 5 — Save

**Append to** `memory/objection-library.md` — never overwrite the full file.

---

## Quality Gates

- [ ] All `discovery/` files scanned for `## Objections Logged` sections
- [ ] Each objection type-classified correctly
- [ ] Frequency counts updated
- [ ] Win rate updated where outcome is known
- [ ] Response templates generated for types with 3+ examples and no template
- [ ] `memory/objection-library.md` updated (append only)
- [ ] Top 5 frequency table updated
