---
name: ops-knowledge-base
description: "Keep the team knowledge base current: FAQ, how-to answers, known issues and workarounds, a do-not-promise list, training video index and the escalation map by role. Use when a new question comes up twice, a feature ships or changes, a bug is fixed, someone asks where to find something, or to review docs for gaps and contradictions. Writes to the private workspace only."
---

# Knowledge base

One trusted place the support, sales and onboarding agents read before they answer anyone.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Private workspace (GitHub private repo or Drive): `knowledge/` folder
- Slack: announce changes to the team
- Product docs and release notes (read)

## Steps
1. **Structure** (create if missing):
   - `knowledge/faq.md`: question, short answer, steps, link;
   - `knowledge/known-issues.md`: the bug log from ops-bug-escalation;
   - `knowledge/do-not-promise.md`: features under development, things only the owner can confirm (pricing, dates, refunds);
   - `knowledge/training-index.md`: video or doc title, topic, link, order;
   - `knowledge/escalation.md`: topic → role → channel (roles only; no personal phone numbers).
2. **Add** an FAQ entry when a question is asked twice. Use the customer's wording as the question.
3. **Every fact has a source** (doc, video, release note, owner decision with date). Mark unsourced items **TBD – needs confirmation**.
4. **On change** (release, fix, decision): update every affected entry, then post a 3-line "what changed" note.
5. **Monthly review:** find contradictions, stale entries (older than 90 days with no check) and gaps; list them for the owner.

## Approval rules
- No passwords, keys, login links, customer contact details or customer data in the knowledge base. Use a password manager for credentials.
- Pricing and policy entries change only with the owner's OK.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Change note:

```
📚 KB updated — 16 Jan
+ FAQ: "Why is my WhatsApp template rejected?" [link]
~ Known issue S3 domain blank page → fixed, verified
TBD: 2 entries need owner confirmation [links]
```

## Done when
- [ ] Every entry has a source or TBD
- [ ] Change note posted
- [ ] No sensitive data added
