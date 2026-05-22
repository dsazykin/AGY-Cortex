---
name: toggle-routing
description: "Toggle the Hub-and-Spoke Tiered Intelligence Orchestration on or off for the AGY Cortex plugin."
---

# Toggle Model Routing

This skill intercepts the `/toggle-routing` command and dynamically updates the orchestration pipeline configurations.

## Critical Instructions:
When this command is triggered by the user:

1. **Locate Configuration:** Locate the plugin configuration file at `agy-cortex/config.json`.
2. **Toggle the State:**
   - Read the existing content of `agy-cortex/config.json`.
   - Read the current boolean value of `model_routing_enabled`.
   - If it is missing or `false`, update it to `true`.
   - If it is `true`, update it to `false`.
3. **Save Configuration:** Write the updated JSON back to `agy-cortex/config.json` immediately.
4. **Display Premium Confirmation Card:**
   - Output a beautifully formatted visual card announcing the new state to the user.
   - Do NOT run the triage subagent loop or any standard execution tasks. 
   - Terminate the turn immediately after displaying the confirmation card.

---

### UI Card Design Specification
Use the following high-fidelity visual representations in your confirmation message:

#### If Enabled:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX ORCHESTRATION PIPELINE : ENABLED        │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ ACTIVE ]                                     │
│  Mode:  Hub-and-Spoke Multi-Agent Triage (L0-L5)       │
│                                                        │
│  » All tasks will be triaged and handled sequentially   │
│    or concurrently by specialist subagents.            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### If Disabled:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX ORCHESTRATION PIPELINE : DISABLED      │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ BYPASSED ]                                   │
│  Mode:  Standard Single-Agent Direct Execution         │
│                                                        │
│  » All tasks will be evaluated and solved directly by  │
│    the primary agent.                                  │
│                                                        │
└────────────────────────────────────────────────────────┘
```
