---
name: sales-call-routing
description: "Suggest the right host for each sales call by role: a technical or conversion closer for informed or high-value leads, the default host for first-time walkthroughs, and the follow-up owner for no-shows and payments. Researches the lead in the CRM first. Use when a booking has no host, when asked who should take a call, to prepare a call brief, or to balance load across the sales team. Suggestions only; never reassigns."
---

# Call routing

Puts every booked call in front of the person most likely to convert it, with a 5-line brief so they walk in prepared.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `query_contacts` (tags, notes, source), `query_opportunities` (stage, value), the bookings read tool, `list_event_types`
- Private workspace: `team-and-routing.md` (roles, not personal data)

## Steps
1. **Read the routing table** in the private workspace. It lists roles, not phone numbers, for example:

   | Role | Takes | Fictional example |
   | --- | --- | --- |
   | Closer | informed, agency or high-value leads; technical questions | Alex Example |
   | Guide (default) | first-time walkthroughs, new to the product | Sam Sample |
   | Follow-up owner | no-shows, reschedules, payment collection | Pat Placeholder |
   | Escalation | anything the above can't answer | the COO |

2. **Research the lead:** company, source (ad, organic, referral), tags, deal stage, past calls and no-shows, booking notes and answers.
3. **Pick a role** with a one-line reason ("runs an agency, asked about white-label pricing → Closer"). If two rules conflict, pick the higher-value one and say so.
4. **Check load:** if that host already has 3+ calls in the same 2 hours, suggest the next best.
5. **Write the call brief** (below) and add it to the booking report or the host's thread.

## Approval rules
- Suggest only. Changing the host on a calendar needs the host or the owner to do it, or an explicit OK naming the booking.
- Briefs stay internal; never send them to the lead.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Per booking:

```
Call brief — Strategy call, Thu 15:00 IST
Lead: Jamie, Acme Studio (agency, 6 staff) · source: webinar
Stage: warm · tags: evt-asl-attended, wants-whitelabel
History: 1 no-show (Jan 9), replied on WhatsApp Jan 12
Suggested host: Closer — asked about pricing for clients
Goal: agree on plan and next step
```

## Done when
- [ ] Every unassigned booking has a suggestion and a reason
- [ ] Briefs use CRM facts only
