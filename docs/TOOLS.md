# Tools map

The skills in this kit call the tools of your **[Your Platform] account connector** (one sub-account, read and write) and, for agencies, an optional **super-admin read connector** (many sub-accounts, read only, `sub_account_id` on every call). The names below are the reference names the skills use; if your platform names them differently, map them as described in [WHITE_LABEL.md](WHITE_LABEL.md). Tool names change between versions: before a skill relies on a tool, check that it is in your connector's tool list. If it isn't, say so and use the closest read tool. Never guess a result.

| Area | Reference tool names | Used by |
| --- | --- | --- |
| Setup and profile | `query_custom_values`, `set_custom_value`, `get_business_profile`, `update_business_profile`, `get_business_brief`, `save_business_brief` | get-started, every skill (Step 0) |
| Contacts and CRM | `query_contacts` (search, tags), contact notes and tags, `query_opportunities`, `create_pipeline` | sales-*, ops-*, hr-* |
| Calendar | `list_event_types`, `create_calendar_event_type`, the appointments/bookings read tool | sales-booking-report, sales-call-routing, hr-interview-scheduling |
| Messaging | `list_waba_connections`, `list_waba_templates`, `create_waba_template`, `list_smtp_connections`, `create_email_template`, `get_channel_readiness` | sales-lead-follow-up, sales-event-reminders, finance-collections |
| Automation | `create_workflow`, `update_workflow_steps`, `update_workflow_status`, `validate_workflow_graph`, `query_workflow_templates`, `create_trigger` | marketing-event-funnel, sales-event-reminders |
| Sites and funnels | `create_funnel`, `list_funnels`, `list_funnel_pages`, `create_page`, `get_page_html`, `write_page_html`, `publish_site`, `create_form`, `create_short_link` | organic-marketing, marketing-event-funnel, micro-app-builder |
| Social | `list_instagram_media`, `publish_instagram_post`, `get_instagram_connection_health`, `create_social_flow`, `get_social_flow`, `list_social_flows`, `test_social_flow`, `get_social_flow_logs` | organic-marketing, marketing-performance-report |
| Ads | `ads_get_ad_accounts`, `ads_get_ad_entities`, `get_ad_connection_health`, `list_ad_leads`, `map_lead_form`, `ads_create_*`, `ads_activate_entity`, `ads_library_search` | meta-lead-form-ads, marketing-performance-report |
| Finance | `get_revenue_summary`, `query_transactions`, `get_dashboard_kpis`, finance module (products, payment links, invoices, subscriptions, expenses, reports) | finance-* , ceo-daily-brief |
| Super admin (read only) | `sa_list_agencies`, `sa_get_agency`, `sa_agency_kpis`, `sa_sub_account_kpis`, `sa_finance_overview`, `sa_list_plans`, `sa_rank_agencies_by_revenue` | ceo-daily-brief, sales-booking-report, finance-revenue-report |

## Other connectors the skills use
- **Slack** (or Teams): where reports land. Post to the channel the owner names; never DM customers from here.
- **Email** (Gmail or Outlook): inbox triage, receipts and invoices for finance, candidate mail for HR. Read freely; **draft** replies; send only with an OK.
- **YouTube**: uploads, titles, descriptions, playlists, comments.
- **Google Drive / Docs / Sheets**: trackers and shared reports.
- **GitHub (private repo)**: your private workspace for reports, SOPs and decisions. Never commit credentials or contact lists to it.

## Platform limits worth knowing
- High-risk sends (bulk email, WhatsApp, payment links) can be queued to **AI Suite → Approvals**. A human approves them in the app; an agent can't approve its own queue.
- The lead score field may be read only. Track stages with CRM tags instead (see sales-lead-scoring).
- There may be no inbox-read tool. Don't claim you read a conversation you couldn't open.
