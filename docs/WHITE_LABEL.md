# White-label guide

You can run this kit under your own brand. The kit already uses placeholders: `[Your Platform]` for the SaaS platform and `[Your Brand]` for your company. Replace them, rename the identifiers below, and keep the pieces that make it work.

## Placeholders

| Placeholder | Replace with |
|---|---|
| `[Your Platform]` | the name of your SaaS platform (the account your agent connects to) |
| `[Your Brand]` | your company or agency name |
| `https://your-account-connection-link.example/mcp` | nothing: each user puts their real link in their agent's connector settings or in `PLATFORM_MCP_URL` |

## Tool name mapping

The skills call MCP tools by name. The reference names in [TOOLS.md](TOOLS.md) (for example `query_custom_values`, `get_business_profile`, `query_contacts`, `create_workflow`, `get_revenue_summary`) are the tool names of the MyAppz platform connector, which this kit was written against. Keep them if your platform is MyAppz-based. If your platform names a tool differently:

1. Add a column to the table in `TOOLS.md` with your platform's name for each tool.
2. Replace the name in the skills that list it (the "Used by" column tells you which).
3. Keep `agentic_kit_setup` as the setup marker, or rename it everywhere (`get-started`, every skill's Step 0 and `hooks/session-start.md`).

## Rename these identifiers

| Where | What | Notes |
|---|---|---|
| `.claude-plugin/plugin.json` | `name`, `displayName`, `author`, `homepage`, `repository` | |
| `.claude-plugin/marketplace.json` | `name` (now `myappz-ai-agentic-saas`), `owner` | The marketplace name is part of the install command (`ai-agentic-saas@<marketplace name>`), so it stays as is in this repo. Change it in your fork and update the README. |
| `.mcp.json`, `.cursor/mcp.json` | server name `platform-account`, variable `PLATFORM_MCP_URL` | Neutral already; rename only if you want your brand there. |
| `README.md` | title, badges, install commands (repository path), Related and footer lines | |
| GitHub | repository owner and name in every `github.com/...` link | Search for the current owner name. |

## Make it local

- Currency, tax and compliance: the finance skills use example amounts and mention GST. Replace them with your market's currency and tax terms.
- Working hours, holidays, time zone and languages: set them in your business profile, not in the skills.
- Channels: if you do not use WhatsApp or Meta ads, delete those skills and their rows in the README table.

## Keep these

- The approval rules in `AGENTS.md` and `docs/AGENT_RULES.md`: agents prepare, a person approves anything that sends, spends or deletes.
- No secrets in the repo. Connection links live in your agent's connector settings or in environment variables.
- Your own records (SOPs, reports, decisions, client data) belong in your private workspace, never in a public fork.
- The `LICENSE` file. The kit is MIT licensed: you may rebrand, change and sell it, as long as copies keep the copyright and permission notice. No public credit line is required.

## Check before you publish

1. Search the repo for the old brand, real names, phone numbers, IDs and links.
2. Run `python3 scripts/validate_kit.py` (frontmatter, manifests, versions, links, secrets and personal data).
3. Bump the version in `plugin.json` and `marketplace.json`, the README badge and the CHANGELOG.
