# Claude instructions for this repo

Follow [AGENTS.md](AGENTS.md). It applies to Claude Code, Claude Desktop and claude.ai alike.

Short version:
- Run **get-started** before any other skill when `agentic_kit_setup` is missing in the account.
- Agents prepare, humans approve: no sends, spend or deletes without an explicit yes.
- Always end with exact, clickable links to what you built or changed (`docs/AGENT_RULES.md`).
- Never commit secrets or a user's private data to this repo. `.mcp.json` reads the connection link from the `PLATFORM_MCP_URL` environment variable and falls back to a harmless placeholder when it is unset (`.env.example`).
