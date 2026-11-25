# For AI agents

You are helping a business run its departments with this kit. It is a set of skills, not code to build.

## Read first
1. [docs/AGENT_RULES.md](docs/AGENT_RULES.md): rules for every skill (clickable links, approvals, facts only, connector order).
2. [docs/CONNECTORS.md](docs/CONNECTORS.md): which connector to use for what.
3. [docs/grok-bot-structure.md](docs/grok-bot-structure.md): the CEO, COO and five department agents, and which skills each uses.
4. [docs/TOOLS.md](docs/TOOLS.md), [docs/ROUTINES.md](docs/ROUTINES.md) and [docs/WHATSAPP_RULES.md](docs/WHATSAPP_RULES.md): tool names, scheduled runs and WhatsApp rules.

## Before any skill
- Check the platform account connector is present: `get_business_profile` must return the user's business. If it is missing, tell the user to add their account's connection link in **their agent's connector settings** (not in chat), and stop.
- Check setup: `query_custom_values` with search `agentic_kit_setup`. If missing, run [skills/get-started](skills/get-started/SKILL.md) first.

## Pick the skill
Skill names start with their department: `marketing-`, `sales-`, `ops-`, `finance-`, `hr-` (plus organic-marketing, meta-lead-form-ads and onboard-a-client). The CEO and COO skills coordinate across them.
Each folder in [skills/](skills) has a `SKILL.md` whose `description` says when to use it. Read the whole `SKILL.md`, then its `references/` only when a step points to them.

## Never
- Send, post, spend, launch ads, refund or delete without the user's explicit yes for that action.
- Ask for or store passwords, API keys, tokens or one-time codes.
- Write the user's private data (SOPs, reports, customer data, IDs) into this repo. It goes in the user's own private workspace (layout: [template/](template)).
- Invent numbers, URLs, claims or testimonials.
- Commit passwords, keys, tokens, login links, contact details or customer data to any repo, private ones included.

## Editing this repo
- Skills follow the Agent Skills format: `skills/<name>/SKILL.md` with YAML frontmatter `name` (matches the folder, lowercase and hyphens) and `description` (what it does and when to use it).
- Keep the kit white-label and generic: no real client, staff or account names, emails, phone numbers, IDs or prices. Before every commit, scan the diff for them. Sample data goes in `examples/` and must be clearly fake.
- For every change, bump the version in `.claude-plugin/plugin.json` and `marketplace.json` and add a `CHANGELOG.md` line (minor for a new skill, patch for fixes). Run `python3 scripts/validate_kit.py` before you commit; CI runs it on every push and pull request.
