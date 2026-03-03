# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. For example, `~~CRM` might mean Salesforce, HubSpot,
or any other CRM with an MCP server.

The plugin is **tool-agnostic** — it describes workflows in terms of categories
rather than specific products. The `.mcp.json` pre-configures common MCP servers,
but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Web research | `~~web research` | Bright Data | Built-in web search (lite mode — see note) |
| CRM | `~~CRM` | HubSpot, Notion | Salesforce, Pipedrive, Close |
| Contact enrichment | `~~enrichment` | Apollo | Clay, ZoomInfo, Lusha |
| Conversation intelligence | `~~conversation intelligence` | Fireflies | Gong, Chorus, Otter.ai |
| Email | `~~email` | Gmail, Microsoft 365 | — |
| Calendar | `~~calendar` | Google Calendar, Microsoft 365 | — |

## Bright Data setup (~~web research)

Bright Data powers **full mode** — full page scraping, LinkedIn profiles, job
posting content, company pages, engineering blogs. Without it, the plugin falls
back to built-in web search (lighter results, still useful).

To connect Bright Data:
1. Sign up at [brightdata.com](https://brightdata.com) (free trial available)
2. Get your API token from Settings → API Tokens
3. Set the environment variable: `export BRIGHTDATA_API_TOKEN=your_token_here`
   (add this to your shell profile so it persists)

The plugin detects which mode it's in and notes "⚠️ Lite mode" when Bright Data
is not connected.

## CRM setup (~~CRM)

Connect your CRM to log calls, update deals, and create follow-up tasks without
leaving your desktop. HubSpot and Notion are pre-configured in `.mcp.json`.

For Salesforce: add the Salesforce MCP server to `.mcp.json` with your credentials.
See [mcp-integrations/salesforce-setup.md](../mcp-integrations/salesforce-setup.md)
in the Claude Code version of this repo for step-by-step instructions.
