# WhatsApp rules

Read before any skill touches WhatsApp. These come from running it in production.

1. **Never use a personal number.** Each agent or channel gets its own business number and its own browser profile.
2. **First touch is an approved template** from the official WhatsApp Business (WABA) number. No cold first messages from WhatsApp Web.
3. **Every WABA send waits for a human OK**, usually in **AI Suite → Approvals**. One-to-one replies included.
4. **Event or broadcast sends are held** until the owner says go, even when the template is approved. Don't over-message: one reminder sequence per event, nothing extra.
5. **WABA numbers can't join existing groups.** Plan group support around that.
6. **Linked devices drop after about 14 days offline.** Check the connection before a campaign (`get_channel_readiness`, `list_waba_connections`).
7. **Opt-outs win.** Anyone who says stop is tagged `wa-opt-out` and never messaged again.
8. Keep numbers, connection IDs and template IDs out of git. Refer to them by label ("main business number") and look them up live.
