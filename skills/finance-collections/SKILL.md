---
name: finance-collections
description: "Collections: list overdue invoices, failed subscription payments and unpaid payment links by age, draft polite reminders on a fixed ladder, hand hard cases to the follow-up owner, and report what was collected. Use when asked who owes money, to chase payments, for an overdue or outstanding report, failed renewals, or to reduce churn from failed payments. Drafts only; every reminder needs an OK."
---

# Collections

Gets paid on time without damaging the relationship.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: finance module (invoices, subscriptions, transactions), `query_transactions`, `query_contacts`, `list_waba_templates`
- Email connector: drafts
- Slack: the weekly collections list

## Steps
1. **Pull** overdue invoices, failed or past-due subscriptions and unpaid payment links. Group by age: 1–7, 8–15, 16–30, 30+ days.
2. **Check** for a payment in the last 48 hours or a note about a dispute before chasing anyone.
3. **Reminder ladder** (default):

   | Age | Message |
   | --- | --- |
   | due date | friendly heads-up with the link |
   | +3 days | reminder, offer help |
   | +7 days | second reminder, ask if anything is wrong |
   | +15 days | call by the follow-up owner |
   | +30 days | owner decides: pause service, plan or write-off |

4. **Draft** each reminder (email, or an approved WhatsApp template) with amount, invoice number and link.
5. **Queue** for approval; after send, log a CRM note `collections-<step>`.
6. **Weekly report**: collected this week, still overdue by bucket, at-risk accounts.

## Approval rules
- Every reminder needs a human OK. Never threaten, never mention penalties not in the contract.
- Pausing service or writing off debt is the owner's decision only.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
💸 Collections — week of 13 Jan
Overdue: ₹62k (9 invoices) · 1–7d ₹20k · 8–15d ₹22k · 30+ ₹20k
Collected this week: ₹38k
Reminders ready to approve: 6 [list]
Needs owner decision: 1 account 30+ days
```

## Done when
- [ ] Recent payments checked first
- [ ] Ladder step correct per invoice
- [ ] Nothing sent without OK
