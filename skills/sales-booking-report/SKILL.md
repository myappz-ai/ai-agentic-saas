---
name: sales-booking-report
description: "Booking and show-up report across one or many accounts: what needs action now (bookings with no host, past meetings still marked booked, no-shows and cancellations to follow up), suggested hosts, and a 30-day table of bookings, show-ups, no-shows and cancellations. Use for the morning or evening booking report, \"who is on my calendar\", show-up rate, calendar hygiene, or a daily sales update to Slack. Read only."
---

# Booking report

The twice-a-day sales heartbeat. Tells the team exactly which bookings need a human, in a format they can act on in one minute.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector (one account) or super-admin read connector (many, pass `sub_account_id`): `list_event_types`, the appointments/bookings read tool, `query_contacts`, `query_opportunities`
- Slack: the sales channel the owner names
- Private workspace: `reports/YYYY-MM/`

## Steps
1. **Scope.** Accounts to cover (from `accounts.md` in the private workspace) and the window: today and tomorrow for action, last 30 days for the table. Times in the owner's zone.
2. **Pull bookings** per account and event type. For each: time, event type, status, assigned host, contact.
3. **Needs action:**
   - booking with **no host** → add a host suggestion from **sales-call-routing**;
   - meeting time has passed but status is still **booked** → host must mark show-up or no-show today;
   - **no-show** or **cancelled** in the last 48 hours → follow-up owner (see sales-lead-follow-up);
   - event types with **no staff** assigned.
4. **30-day table** per account: bookings, showed, no-show, cancelled, not updated, show-up %.
5. **Per-account sections**: today's and tomorrow's bookings with host and a one-line note from the CRM (stage, tags, last call).
6. Save and post. Close with the time of the next update.

## Approval rules
- Read only. Never reassign hosts, change booking status or message contacts from this skill.
- In Slack, refer to contacts by first name and booking link only; never post phone numbers or emails.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Slack message (same text saved as `reports/YYYY-MM/YYYY-MM-DD-morning.md` or `-evening.md`):

```
📅 Bookings — Thu 16 Jan, 10:00 IST
Needs action (4)
• No host: Strategy call 15:00 — Jamie (Acme Studio) → suggest: Closer [link]
• Past, not updated: Demo 09:30 yesterday — host Sam [link]
• No-show: Consult 18:00 yesterday — Riley → follow-up owner: Pat [link]
30 days | Booked | Showed | No-show | Cancelled | Not updated | Show-up %
Acme Studio | 42 | 28 | 8 | 4 | 2 | 67%
Next update: 17:30 IST
```

## Done when
- [ ] Every booking in the window checked
- [ ] Needs action listed first, each with a link
- [ ] Report saved and posted
