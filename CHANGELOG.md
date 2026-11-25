# Changelog

## 0.3.0 – 2026-11-26

License, white-label and project hygiene.

- License is now MIT for the whole kit (skills, docs and code), so partners can rebrand and resell it. Copies keep the copyright and permission notice; no credit line is required.
- White-label: the skills and docs say `[Your Platform]` instead of a brand name. The tool names stay the same, and docs/WHITE_LABEL.md maps them.
- `.mcp.json` uses the neutral server name `platform-account` and the variable `PLATFORM_MCP_URL`, with a harmless placeholder default when it is unset. `.env.example` is updated to match. If you set `MYAPPZ_MCP_URL` before, rename it.
- The ChatGPT install row is marked as not tested and gives the path that works today.
- The skill count is the same everywhere (33).
- Added CI (`scripts/validate_kit.py`): skill frontmatter, JSON manifests, version consistency, skill count, relative links, and a secret and personal-data scan; external links are checked as warnings.
- Added CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, issue templates and a pull request template.
- The micro-app-builder skill reads PLAYBOOK.md from the Micro App Builder's latest release.

## 0.2.2 – 2026-11-26

Neutral, white-label friendly.

- Removed personal attribution and company bio from the README footer and docs. The author field stays "MyAppz".
- Added docs/WHITE_LABEL.md: what partners rename, what they keep, and the placeholders to use.
- Docs no longer name a specific company as the source of the Grok Bot structure.

## 0.2.1 – 2026-11-25

Public release.

- The micro-app-builder skill and the README now point to the public Micro App Builder playbook (renamed from App Builder Community).
- The README no longer links to any private repository.
- LICENSE is the official CC BY 4.0 text, so GitHub detects it.
- Repository topics, description and homepage set.

## 0.2.0 – 2026-11-25

Five departments, each with a full skill set.

- Marketing: marketing-performance-report, marketing-youtube-publishing, marketing-content-research, marketing-event-funnel (with organic-marketing and meta-lead-form-ads).
- Sales: sales-booking-report, sales-call-routing, sales-lead-scoring, sales-lead-follow-up, sales-event-reminders, sales-pipeline-review.
- Operations (now includes support): ops-customer-onboarding, ops-support-triage, ops-bug-escalation, ops-knowledge-base, ops-agent-handoff (with onboard-a-client).
- Finance: finance-revenue-report, finance-invoicing, finance-collections, finance-expense-report, finance-tax-pack.
- HR: hr-hiring-pipeline, hr-interview-scheduling, hr-staff-onboarding, hr-leave-tracker, hr-offboarding.
- Replaced the 0.1 starter skills sales-follow-up, customer-support, finance-reporting and hr-basics with the skills above.
- CEO and COO skills now coordinate the five departments.
- New docs: TOOLS.md, ROUTINES.md, WHATSAPP_RULES.md.

## 0.1.0 – 2026-11-25

First public-ready layout.

- Installable as a Claude plugin (`.claude-plugin/`), with a SessionStart hook that routes new users to **get-started**.
- Skills moved to `skills/`: get-started, organic-marketing, meta-lead-form-ads, add-proven-playbook, onboard-a-client.
- New generic skills: ceo-daily-brief, coo-daily-rhythm, sales-follow-up, customer-support, finance-reporting, hr-basics, micro-app-builder.
- Docs moved to `docs/` (basics, agent rules, connectors, cloud autopilot, Grok Bot structure).
- `examples/` with fictional sample company data; `template/` for a department workspace.
- Placeholder-only MCP configs for Claude Code and Cursor, `.env.example`, `.gitignore`.
- Company-specific material removed from the kit.
