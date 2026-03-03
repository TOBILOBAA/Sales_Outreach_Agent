---
description: Capture call notes, map to qualification, draft follow-up email
argument-hint: <company name>
allowed-tools: Read, Write, WebSearch
---

Read your seller profile: @${CLAUDE_PLUGIN_ROOT}/seller-context.md

I just got off a call with: $ARGUMENTS

Follow the call-debrief skill. Do this immediately — memory degrades fast.

1. Read what we knew BEFORE the call: account-brief.md, last meeting brief, prior call notes. Debrief highlights what CHANGED, not just what was said.
2. If no notes provided: guide me through a verbal download (quick context → pain discovery → qualification elements → momentum).
3. Map everything to the qualification framework from the seller profile. Mark status: ✅ Confirmed | ⬜ Unknown | 🚫 Negative.
4. Assess 3 Whys: Why Anything / Why Product / Why Now.
5. Draft follow-up email — send same day, ideally within 2 hours.
6. Update account-brief.md with new qualification status, last interaction date, and stage.

If ~~CRM is connected: log the call activity and create tasks for any commitments made.
If not: output a formatted CRM block ready to paste.

Save call notes to: accounts/{company}/discovery/YYYY-MM-DD-{type}-notes.md
Note: include "## Objections Logged" section — required for objection-mining skill.
