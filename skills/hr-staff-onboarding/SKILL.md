---
name: hr-staff-onboarding
description: "Onboard a new team member or a new AI agent: day-one checklist, accounts and roles with least privilege, separate business number and browser profile per agent, training plan, a buddy, first-week goals and a 30-60-90 day check-in. Use when someone joins, a new agent is set up for a department, or to check onboarding progress. Account invites and access changes need an OK."
---

# Staff onboarding

New people and agents are useful in week one and only have the access they need.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: staff and roles in settings (invite only with OK)
- Slack or Teams: invite to the right channels
- Private workspace: `hr/onboarding-checklist.md`, `handoffs/` (see ops-agent-handoff), training index
- Calendar: first-week meetings

## Steps
1. **Before day one**: role, manager, buddy, start date, tools needed. Write the access list: which systems, which role, which accounts. Least privilege first.
2. **Accounts**: send invites through each tool's own invite flow (never share a login). For an AI agent: its own email or inbox, its own business number and browser profile, connectors scoped to what it needs.
3. **Day one**: welcome note, team intro, the company overview, the role's handoff doc, the rules (approvals, privacy, never promise).
4. **Training plan**: the core training videos in order, one small task per day, with the buddy checking.
5. **First-week goals**: 3 concrete outcomes.
6. **Check-ins** at day 7, 30, 60, 90: what's going well, blockers, access still right?

## Approval rules
- Granting access, adding staff or connecting accounts needs an OK for each system.
- Passwords and recovery codes go in a password manager, never in chat, docs or git.
- Personal details (ID documents, bank, address) go to the HR system, not the repo.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Checklist per person:

```
🎒 Onboarding — Sam Sample, Support (day 2)
☑ Email ☑ Slack channels ☐ CRM role (waiting OK) ☑ Buddy: Pat
Training: video 2 of 6 · Task: answer 3 FAQ tickets (drafts)
Check-in: day 7 — Fri 24 Jan
```

## Done when
- [ ] Access list approved before invites
- [ ] Handoff doc read
- [ ] Check-ins scheduled
