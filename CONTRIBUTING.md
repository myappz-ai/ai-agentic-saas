# Contributing

Thanks for improving the kit. People and AI agents both read it, so clear and short beats long.

## Ground rules

- No passwords, keys, tokens, connection links, real names, phone numbers, emails, account IDs, prices of real deals or client data. Use placeholders such as `[Your Platform]`, `[Your Brand]` and `[Client]`, and clearly fake sample data in `examples/`.
- Agents prepare, people approve. A skill must never send, post, spend, refund or delete without an explicit yes.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report security problems privately (see [SECURITY.md](SECURITY.md)).

## Add or change a skill

1. Create `skills/<name>/SKILL.md`. The folder name is lowercase with hyphens and starts with the department (`marketing-`, `sales-`, `ops-`, `finance-`, `hr-`).
2. Frontmatter: `name` (same as the folder) and `description` (what it does and when to use it, under 1024 characters). Put the description in double quotes if it contains a colon.
3. Start with the Step 0 setup check, then Tools and connectors, Steps, what needs approval and what it hands back. Copy the shape of an existing skill.
4. Use the reference tool names from [docs/TOOLS.md](docs/TOOLS.md). Long material goes in `skills/<name>/references/`.
5. Add the skill to the README table and update the skill count in the README and `plugin.json`.

## Before you open a pull request

1. Run `pip install pyyaml` once, then `python3 scripts/validate_kit.py`. CI runs the same check on every push and pull request.
2. Bump the version in `.claude-plugin/plugin.json`, both places in `.claude-plugin/marketplace.json` and the README badge (minor for a new skill, patch for fixes), and add a `CHANGELOG.md` entry.
3. Describe the real situation that showed the change was needed.

By contributing you agree that your contribution is licensed under the MIT License of this repository.
