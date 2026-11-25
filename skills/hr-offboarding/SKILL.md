---
name: hr-offboarding
description: "Offboard a team member or retire an AI agent safely: list every account, connector, number and key they could use, plan the handover of their work and customers, schedule access removal on the last day, and confirm nothing was left open. Use when someone resigns or leaves, a contractor ends, an agent or routine is retired, or for an access review. Removing access needs an OK for each system."
---

# Offboarding

Work keeps moving and access ends on time. The most common source of leaks is old accounts nobody switched off.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: staff and roles (read; changes with OK), `query_integrations` and the MCP keys list in settings
- Slack or Teams admin, email admin, calendar
- Private workspace: access register, `handoffs/`

## Steps
1. **Access inventory**: every system (CRM, email, chat, ads, social, payment gateway, GitHub, password manager, routines, MCP keys or connections, business numbers). Use the access register; ask the person's manager to confirm.
2. **Handover**: write a handoff with **ops-agent-handoff**: open deals, customers, bookings, routines they own. Reassign each with the manager.
3. **Plan the removal** for the last working day: list each system and what happens (remove, downgrade, transfer ownership). Shared passwords they knew → rotate in the password manager.
4. **On the day, after the OK**: remove or downgrade access, revoke keys and connections, transfer files and calendars, set an email forward or auto-reply.
5. **Confirm**: re-check each system and record the date in the access register. For an agent, also disable its routines.

## Approval rules
- Every removal, revoke or transfer needs an OK naming the system.
- Never copy keys or passwords to check them; revoke and re-issue instead.
- Exit details stay private to the manager and HR.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
🚪 Offboarding — Pat Placeholder, last day Fri 31 Jan
Systems: 11 · removed 0 · planned 11 · keys to revoke 2 · shared passwords to rotate 3
Handover: 4 deals, 9 customers, 2 routines → reassigned [handoff link]
Approve the removal plan?
```

## Done when
- [ ] Inventory confirmed by manager
- [ ] Handover done
- [ ] Every system re-checked after removal
