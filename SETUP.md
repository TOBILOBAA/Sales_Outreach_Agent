# Setup Guide — agentic-seller
*For someone who has never used a terminal.*

---

## What you need

| Item | Required? | Cost |
|------|-----------|------|
| Claude.ai subscription | Yes | From $20/month (Pro plan) |
| Claude Code | Yes | Included with your Claude.ai subscription — free to install |
| Bright Data account | Strongly recommended | ~$10/month (free trial available) |
| Notion workspace | Optional | Free |

**Total time to first research:** ~30 minutes

**Note on Claude:** Claude Code is part of Claude.ai — you do NOT need a separate API key. Just subscribe at [claude.ai](https://claude.ai) and Claude Code is included.

---

## Step 1 — Install Claude Code

Claude Code is a command-line tool that runs on your computer. Don't let "command-line" scare you — it's just a text window where you type commands.

**Open your Terminal** (Mac: press `⌘ + Space`, type "Terminal", press Enter)

**Install Node.js first** (if you don't have it):
1. Go to [nodejs.org](https://nodejs.org) and download the LTS version
2. Run the installer — click Next → Next → Install

**Then install Claude Code:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Sign in with your Claude.ai account:**
```bash
claude
```
The first time you run `claude`, it will ask you to log in. Follow the browser prompt — it uses your Claude.ai account (no separate API key needed).

---

## Step 2 — Clone this repo

```bash
git clone https://github.com/YOUR_HANDLE/agentic-seller
cd agentic-seller
```

Don't have git? Download it from [git-scm.com](https://git-scm.com).

---

## Step 3 — Set up Bright Data (strongly recommended)

Bright Data is what makes the research genuinely powerful.

**Without Bright Data (lite mode):** Web search results only — no page content, no LinkedIn profiles, no job posting details.

**With Bright Data (full mode):** Full LinkedIn profiles, company pages, job postings, engineering blogs, Reddit, news articles. This is what separates good research from great research.

1. Sign up at [brightdata.com](https://brightdata.com) (free trial available, then ~$10/month)
2. Get your API token from the dashboard → Settings → API Tokens
3. Copy `.claude/mcp.json.template` to `.claude/mcp.json`:
   ```bash
   cp .claude/mcp.json.template .claude/mcp.json
   ```
4. Open `.claude/mcp.json` in any text editor and replace `YOUR_BRIGHTDATA_API_TOKEN_HERE` with your actual token
5. The `.claude/mcp.json` file is already in `.gitignore` — your API key won't be committed

Full setup details: `mcp-integrations/brightdata-setup.md`

---

## Step 4 — Run Claude and let it onboard you

```bash
claude
```

That's it. Claude will detect that you haven't configured the system yet and ask you 9 questions:

1. Your name and role
2. Your company and what you sell
3. Your ideal customer (ICP)
4. Your qualification framework (MEDDPICC, BANT, SPIN, etc.)
5. Your CRM
6. Other sales tools you use → **Claude will search for MCPs for each one automatically**
7. Whether you have Bright Data → **Claude explains full vs. lite mode**
8. Your top competitors
9. Your verified proof points

**After answering:**
- Claude fills in your personal details in the `CLAUDE.md` file
- Searches for MCP servers for every tool you mentioned
- Offers to connect each one it finds
- Sets up your Notion pipeline if you want it

**You'll see:** "You're set up. Here's what I know about you: [summary]. Ready to research your first account?"

---

## Step 5 — Your first command

```
research [your first target company name]
```

Or: `/prospect-research [company name]`

Claude will run a full research sweep and save the results to `accounts/{company}/research/`.

---

## The 8 skills (what you can do now)

| Command | What it does |
|---------|-------------|
| `research [company]` | Full account research sweep |
| `write outreach for [contact] at [company]` | Personalized LI + InMail + email + cold call |
| `prep me for my call with [company]` | Full meeting brief with discovery questions |
| `just got off a call with [company]` | Capture notes → qualification map → follow-up email |
| `what's the hook for [company]?` | Strongest current signal → one-liner |
| `score my territory` | Ranked signal list weighted by ICP fit |
| `linkedin plan for [company]` | Engagement ladder → warm path |
| `score [company] on ICP` | 5-dimension fit scoring → tier assignment |

---

## Add more integrations (optional)

See `mcp-integrations/` for setup guides for:
- Notion (pipeline, tasks, contacts)
- Apollo (contact enrichment)
- LinkedIn (profile + company data)
- Gong (auto-debrief from call transcripts)
- HubSpot / Salesforce (CRM sync)

Or just run Claude — it will find these automatically during onboarding when you mention the tools you use.

---

## Troubleshooting

**"command not found: claude"** → Node.js or npm isn't in your PATH. Restart your terminal after installing Node.js.

**"API key invalid"** → Make sure you copied the full key starting with `sk-ant-`. Check for extra spaces.

**Research is in lite mode even with Bright Data configured** → Check `.claude/mcp.json` exists (not just the template). Verify the API token is correct.

**Claude doesn't seem to know about your company** → The onboarding didn't complete or placeholders weren't filled. Type "setup" or "onboard me" to re-run the onboarding interview.
