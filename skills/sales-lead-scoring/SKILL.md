---
name: sales-lead-scoring
description: "Score and stage leads with CRM tags: cold, warm, hot, plus customer and lost, using simple rules based on replies, conversations and bookings. Use when asked to score leads, clean up the pipeline stages, find hot leads, tag leads after a campaign or event, or when the platform lead-score field is read only. Applying tags in bulk needs an OK."
---

# Lead scoring with tags

A scoring system anyone can read in the CRM, built on tags because the built-in score field may be read only.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: `query_contacts` (filter by tag, source, date), contact tag update tool, `query_opportunities`
- Private workspace: `sops/lead-scoring.md` with your exact rules

## Steps
1. **Rules (default, edit in the SOP):**

   | Tag | Rule |
   | --- | --- |
   | `lead-cold` | everyone starts here (form fill, ad lead, import) |
   | `lead-warm` | replied to any message or opened 2+ emails |
   | `lead-hot` | real two-way conversation, booked a call, or asked about price |
   | `lead-customer` | paid |
   | `lead-lost` | said no, or 30 days with no reply after 3 touches |

2. **One stage tag per contact.** When you add a new stage tag, remove the old one.
3. **Batch:** list the contacts that should move, with the reason for each ("replied Jan 12").
4. **Show the change list** (counts per move and a sample of 5). Apply after the OK, then re-query to confirm the counts.
5. Hand hot leads to **sales-lead-follow-up** and **sales-call-routing**.

## Approval rules
- Tag changes on more than 10 contacts need an OK for the batch.
- Never delete contacts or tags; mark `lead-lost` instead.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
🏷 Lead stages — week of 13 Jan
Moves proposed: cold→warm 34 · warm→hot 9 · hot→customer 2 · →lost 15
Sample: Riley (replied Jan 12) cold→warm [link]
Now: cold 410 · warm 88 · hot 21 · customer 57
```

## Done when
- [ ] Every proposed move has a reason
- [ ] One stage tag per contact after the run
