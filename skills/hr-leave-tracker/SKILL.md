---
name: hr-leave-tracker
description: "Track leave, holidays and availability: record leave requests, check team coverage before approving, keep a shared out-of-office calendar, and post who is out this week so routing, bookings and support stay covered. Use when someone requests leave, asks who is out, plans holidays, or when coverage for sales calls or support is at risk. The manager approves leave."
---

# Leave tracker

Nobody is surprised by an empty seat, and customer-facing work is always covered.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Calendar connector: shared out-of-office calendar
- Private workspace or HR sheet: leave register (balances kept private)
- Slack: weekly who-is-out post
- sales-call-routing and ops-support-triage: coverage changes

## Steps
1. **Request**: person, dates, type (annual, sick, public holiday, other), cover person.
2. **Coverage check**: do the dates clash with other leave in the same role, booked calls they host, or an event? List the clashes.
3. **Send to the manager** with the clash list. The manager approves or declines.
4. **After approval**: add to the out-of-office calendar, update routing (their bookings get a suggested host), and set an out-of-office draft.
5. **Monday post**: who is out this week and who covers.

## Approval rules
- Only the manager approves leave.
- Sick leave reasons and medical details are never posted or committed.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
🌴 Out this week (13–17 Jan)
Alex — Wed–Fri (annual) → cover: Sam for closer calls
Public holiday Thu: support on reduced hours, auto-reply drafted
Clashes: 2 booked calls Wed → suggested hosts in booking report
```

## Done when
- [ ] Clashes checked before approval
- [ ] Calendar and routing updated
- [ ] Monday post sent
