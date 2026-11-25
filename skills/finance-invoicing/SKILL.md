---
name: finance-invoicing
description: "Prepare invoices, quotations, payment links, credit notes and receipts from a won deal, a plan change or a manual request, with correct product, price, tax and due date. Use when asked to invoice a client, send a quote, create a payment link, issue a credit note or receipt, or bill a new customer. Drafts only; creating or sending anything a customer sees needs an OK."
---

# Invoicing

Accurate billing documents, prepared fast, never sent without a human check.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Account connector: finance module (products, payment links, invoices, quotations, credit notes), `query_contacts`, `query_opportunities`
- Email connector: draft the cover email
- Private workspace: `finance/price-list.md` (your own prices; keep real pricing private)

## Steps
1. **Source**: the won deal, signed quote or request. Confirm customer, billing entity, product or plan, quantity, price, discount, tax rate and due date. Anything missing → ask.
2. **Price check**: price must match the price list or a written owner approval for the discount. Flag any mismatch.
3. **Tax**: apply the account's tax settings; show tax separately. If the customer gave a tax ID, check its format, not its validity.
4. **Draft** the document in the finance module (draft status) or as a preview table. For a payment link, use a connected gateway product; links made outside the platform may not track.
5. **Cover email** draft: what it is for, amount, due date, how to pay, who to contact.
6. **Ask for the OK** with the preview. After the OK, issue and send, then log a CRM note and tag `invoice-sent`.

## Approval rules
- Never issue, send or void an invoice, or create a live payment link, without an OK for that document.
- Discounts and refunds only with the owner's written approval.
- Never put card numbers, bank logins or gateway keys anywhere.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
Preview:

```
🧾 Draft invoice — Acme Studio
Growth plan × 1 · ₹12,000 · GST 18% ₹2,160 · Total ₹14,160
Due: 31 Jan · Pay by: payment link (draft) · Price check: matches list
Approve to issue and send?
```

## Done when
- [ ] Price and tax checked
- [ ] Draft previewed
- [ ] Issued and logged only after OK
