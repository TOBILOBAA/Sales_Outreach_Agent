---
description: Write personalized outreach for a contact — all 4 channels
argument-hint: <contact name> at <company>
allowed-tools: Read, Write, WebSearch
---

Read your seller profile: @${CLAUDE_PLUGIN_ROOT}/seller-context.md

Write outreach for: $ARGUMENTS

Follow the write-outreach skill:

1. Check ~~CRM for existing relationship or AE ownership. Stop if contact is owned or flagged.
2. Read the most recent research file for this account. If none exists: run /research first.
3. Search for a live proof point matching their industry and use case before writing.
4. Select the strongest hook: personal signal > company signal > technical signal > role signal.
5. Draft all 4 variants:
   - LinkedIn connection request (≤300 characters — count every character)
   - LinkedIn InMail (≤500 words, subject = pain hypothesis as a question)
   - Cold email (≤400 words, subject = quantified pain at company?)
   - Cold call script (pattern interrupt → bridge → pain + outcome → soft ask)
6. Check every draft against references/banned-phrases.md. Rewrite from scratch if any banned phrase appears.

Save to: accounts/{company}/emails/YYYY-MM-DD-{contact}-outreach.md
Create 2 CRM tasks via ~~CRM (or output as paste-ready block if not connected):
- Task 1: Day 1 — send LI + email
- Task 2: Day 3 — follow-up call
