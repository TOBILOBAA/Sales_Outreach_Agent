---
description: Build a full meeting brief before any sales call
argument-hint: <company name>
allowed-tools: Read, Write, WebSearch
---

Read your seller profile: @${CLAUDE_PLUGIN_ROOT}/seller-context.md

Prep me for my call with: $ARGUMENTS

Follow the discovery-prep skill:

1. Read all existing account files: account-brief.md, research files, prior call notes, meeting briefs.
2. Pull fresh external intel — anything published about the company or attendees in the last 30 days.
3. Run a gap analysis on the qualification framework from the seller profile. Mark each element: ✅ Confirmed | ⬜ Unknown | 🎯 Probe in this meeting | 🚫 Negative signal.
4. Check 3 Whys status: Why Anything / Why Product / Why Now. Each ⬜ becomes a meeting goal.
5. Find at least 1 proof point from live search matched to their industry and profile.

If ~~CRM is connected: pull account history, open opportunities, last 10 activities, and any internal notes.
If ~~conversation intelligence is connected: find prior call recordings or transcripts for this account.
If ~~calendar is connected: pull meeting attendees and any description from the calendar invite.

Deliver:
- Executive summary (who they are, where we are, top signals, meeting goal)
- Recommended agenda with time blocks
- Discovery questions mapped to each unknown qualification element
- Top 2 objections with prepared responses
- 2 proof points from live search (with sources)
- Day-of checklist

Save to: accounts/{company}/meetings/YYYY-MM-DD-meeting-brief.md
