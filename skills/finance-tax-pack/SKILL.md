---
name: finance-tax-pack
description: "Monthly or quarterly tax and accounts pack for the accountant: sales and tax collected by rate, purchases and input tax, refunds and credit notes, invoice number gaps, and a checklist of missing documents. Use when asked to prepare GST or VAT data, month-end close, documents for the accountant or auditor, or to check invoices before filing. Prepares data only; never files returns."
---

# Tax pack

A clean, checked bundle the accountant can file from, with problems found before they cost money.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: finance module reports (tax, revenue, refund, outstanding), invoices and credit notes, `query_transactions`
- finance-expense-report output for purchases
- Private workspace or Drive folder the accountant can read

## Steps
1. **Period** and tax regime (from the account settings).
2. **Sales**: invoices issued, taxable value and tax by rate, split by customer type if your regime needs it (business vs consumer, in-state vs out-of-state).
3. **Adjustments**: credit notes, refunds, cancelled invoices.
4. **Purchases**: from the expense report, with tax shown on each bill.
5. **Checks**: invoice number gaps or duplicates, missing customer tax IDs on business invoices, totals that don't match collected payments, documents missing.
6. **Pack**: summary sheet plus CSV exports, in a folder shared only with the accountant.

## Approval rules
- Never file, pay tax or sign anything. The accountant and the owner do that.
- Share the pack only with the people the owner names.
- Tax IDs and bank details stay in the private workspace, never in Slack.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
📑 Tax pack — January
Taxable sales ₹4.1L · Tax ₹73.8k (18%) · Credit notes 2
Purchases with tax ₹98k · Input tax ₹17.6k
Checks: ☑ numbering · ⚠ 2 business invoices without tax ID · ☑ totals match
Folder: [private link]
```

## Done when
- [ ] All checks run
- [ ] Issues listed for the accountant
- [ ] Pack shared only as told
