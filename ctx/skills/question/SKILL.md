---
name: question
description: "Directly ask the primary Coordinator agent a question, bypassing the multi-agent orchestration pipeline entirely."
---

# Direct Coordinator Inquiry

This skill intercepts the `/question` command (or `/q`, `/ask`) and routes the query directly to the main Coordinator agent for an immediate response without engaging subagents or toggling routing states.

## Critical Instructions:
When this command is triggered by the user:

1. **Bypass Triage Immediately:** Do not run the router subagent, planning phase, or sequential/parallel worker chain.
2. **Display Premium Bypassed Card:** Output the beautifully formatted visual card below before responding to the user's inquiry.
3. **Execute Direct Evaluation:** Answer the user's prompt directly using the primary coordinator's context and capabilities.

---

### UI Card Design Specification
Use the following premium ASCII representation to announce the direct channel:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : DIRECT COORDINATOR INQUIRY          │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ BYPASSING ORCHESTRATION ]                    │
│  Target: Standard Single-Agent Direct Execution        │
│                                                        │
│  » Processing query directly via the primary agent.   │
│                                                        │
└────────────────────────────────────────────────────────┘
```
