# Agentic Seller — Cowork Plugin

A B2B selling system for AEs, BDRs, and founders. Research accounts, write personalized outreach, prep for calls, and run your territory — without leaving your desktop.

Built for [Claude Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop app. Also works in Claude Code (see the [Claude Code version](../) in the parent folder).

---

## What it does

| You say | What happens |
|---------|-------------|
| `research Acme Corp` | Scans tech stack, finds signals, identifies contacts — builds a research file in minutes |
| `/write-outreach Sarah Chen at Acme Corp` | Reads the research, picks the sharpest hook, writes LinkedIn + InMail + email + cold call — all personalized |
| `/call-prep Acme Corp` | Full meeting brief: agenda, discovery questions, objections, proof points |
| `/call-debrief Acme Corp` | Notes → qualification map → follow-up email → updated account record |
| `/territory-health` | Scores every account against signals this week — tells you where to focus |

---

## Installation

```bash
claude plugins add https://github.com/romiluz13/agentic-seller/tree/main/cowork-plugin
```

Or install from the Claude Cowork plugin marketplace when available.

---

## Setup (5 minutes)

### Step 1 — Fill in your seller profile

Open `seller-context.md` in any text editor and fill in:
- Your name, company, and what you sell (1 line)
- Your ideal customer (industry, size, titles)
- Your qualification framework (MEDDPICC, BANT, etc.)
- Your CRM
- Your verified proof points

Claude reads this file at the start of every session. This is what makes every interaction personalized to you.

### Step 2 — Connect your tools (optional but recommended)

**Bright Data (~$10/month) — makes research genuinely powerful:**

Without it: web search results only.
With it: full LinkedIn profiles, job postings, company pages, engineering blogs.

```bash
export BRIGHTDATA_API_TOKEN=your_token_here
```

Add this to your shell profile (`~/.zshrc` or `~/.bash_profile`) so it persists.
Sign up at [brightdata.com](https://brightdata.com) — free trial available.

**CRM (HubSpot, Notion, or others):**

HubSpot and Notion are pre-configured in `.mcp.json`. Connect via the Cowork MCP settings.
For Salesforce or others: see `CONNECTORS.md` for options.

### Step 3 — Pick a working folder

Run Cowork from a dedicated folder for your sales work. All account files
(`accounts/`, `memory/`) will be created there.

---

## Commands (explicit slash commands)

| Command | What it does |
|---------|-------------|
| `/research <company>` | Full research sweep — tech stack, signals, contacts, FITS score, top 3 hooks |
| `/write-outreach <contact> at <company>` | All 4 channels: LI + InMail + email + cold call |
| `/call-prep <company>` | Full meeting brief — agenda, gaps, questions, objections, proof points |
| `/call-debrief <company>` | Capture notes → qualification map → follow-up email |
| `/territory-health` | Score all accounts by signal strength and ICP tier |

---

## Skills (natural language)

You don't have to use the slash commands. Just talk naturally:

- "Research Stripe before my call tomorrow"
- "What's the hook for Acme Corp?"
- "Write a cold email to the VP Engineering at Notion"
- "I just got off a call with Figma — here are my notes..."
- "What are prospects pushing back on most?"
- "LinkedIn plan for Datadog"
- "Score my territory"

---

## Components

| Component | Count | What they do |
|-----------|-------|-------------|
| **Skills** | 8 | Domain knowledge loaded automatically when relevant |
| **Commands** | 5 | Explicit slash commands for key workflows |
| **Hooks** | 1 | SessionStart: injects seller profile into every session |
| **MCP servers** | 8 | Bright Data, HubSpot, Notion, Apollo, Fireflies, Gmail, Google Calendar, Microsoft 365 |

**Skills:**
- `prospect-research` — account research sweep
- `write-outreach` — personalized outreach across 4 channels
- `discovery-prep` — pre-call meeting brief
- `call-debrief` — post-call capture and follow-up
- `objection-mining` — territory-wide objection library
- `social-selling` — LinkedIn engagement ladder
- `signal-scoring` — territory signal ranking
- `icp-matrix-builder` — 5-dimension ICP scoring

---

## File organization

All output files are created in your working directory:

```
accounts/{company}/
├── account-brief.md          ← Living document. Updated after every touch.
├── research/                 ← Dated research files. Never deleted.
├── discovery/                ← Call notes. One per call.
├── meetings/                 ← Meeting briefs.
└── emails/                   ← Outreach drafts.

memory/
├── account-intel.md          ← Persistent: confirmed contacts, warm intros, gotchas
├── objection-library.md      ← Built by objection-mining. Append only.
├── territory-signals.md      ← Signal scoring snapshot. Overwritten each run.
└── icp-matrix.md             ← ICP tier table. Overwritten monthly.
```

---

## How full mode vs. lite mode works

**Full mode (Bright Data connected):**
- Scrapes full LinkedIn profiles, company pages, job postings, engineering blogs
- Runs 10+ parallel searches per account
- Significantly higher signal quality

**Lite mode (no Bright Data):**
- Uses built-in web search
- Lighter results — still useful for most accounts
- Output notes "⚠️ Lite mode"

You can start in lite mode and add Bright Data later.

---

## Customization

This plugin uses `~~category` placeholders for external tools (see `CONNECTORS.md`).
Replace them with your specific tools using the Cowork plugin customizer:

```
Customize this plugin for my tools
```

Or edit `.mcp.json` directly to add your CRM or other tools.

---

## Claude Code version

This plugin is part of the [agentic-seller](https://github.com/romiluz13/agentic-seller) system.

If you use Claude Code (CLI), the full system is in the parent folder with:
- `CLAUDE.md` — full system configuration with 9-question onboarding
- `.claude/skills/` — all 8 skills auto-discovered by Claude Code
- MCP guides for every integration

**The two versions are fully compatible.** Use whichever interface fits your workflow.
