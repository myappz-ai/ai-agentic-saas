---
name: finance-expense-report
description: "Expense report: gather receipts and bills from email and the finance module, categorise by vendor and category, spot duplicates, renewals and unusual charges, compare with budget, and list subscriptions nobody uses. Use for a monthly expense report, \"what are we spending on\", software subscriptions, budget vs actual, or preparing expenses for the accountant. Read only; adding or changing expense records needs an OK."
---

# Expense report

Shows where the money goes each month and what can be cut.

## Step 0 – Setup check
Call the account connector's `query_custom_values` with search `agentic_kit_setup`. If the account isn't connected or the value is missing, run the **get-started** skill first. Tool names below are the reference names (see the mapping in [docs/WHITE_LABEL.md](../../docs/WHITE_LABEL.md)); confirm them in your [Your Platform] connector's tool list ([docs/TOOLS.md](../../docs/TOOLS.md)).

## Tools and connectors
- Email connector: search receipts and invoices (read)
- Account connector: finance module expenses, vendors, categories; `query_transactions`
- Private workspace: `finance/budget.md`, `finance/vendors.md`

## Steps
1. **Collect** the month's receipts: email search (receipt, invoice, payment received, subscription renewed) plus expenses already in the finance module.
2. **Extract** date, vendor, amount, currency, tax, category. Convert currencies at the stated rate and say which rate.
3. **Clean**: merge duplicates (same vendor, amount, date ±1 day); mark missing receipts.
4. **Compare** with budget by category; flag anything 20% over.
5. **Subscriptions**: list recurring charges with last-use evidence if available; mark "check if still needed".
6. **Propose** records to add to the finance module (draft list). Add them only after the OK.

## Approval rules
- Read only until the OK to add records.
- Never store card numbers or bank details; show the last 4 digits at most.
- Cancelling a subscription is the owner's decision.
- Always give exact, clickable links (see `docs/AGENT_RULES.md`). Facts only, from tools you actually called.
- Never ask for, paste or store passwords, API keys, tokens or one-time codes.

## Output
```
🧮 Expenses — January
Total ₹1.42L (budget ₹1.30L, +9%)
Software ₹58k (+24% ⚠) · Ads ₹55k · Contractors ₹24k · Other ₹5k
Duplicates: 1 · Missing receipts: 3
Check if still needed: 2 tools, ₹4.2k/month
```
Plus a CSV `reports/YYYY-MM/YYYY-MM-expenses.csv` in the private workspace.

## Done when
- [ ] Every expense categorised
- [ ] Duplicates and missing receipts listed
- [ ] Nothing written without OK
