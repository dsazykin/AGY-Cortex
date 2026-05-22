---
name: toggle-parallel
description: "Toggle the experimental parallel agent routing on or off for the AGY Cortex plugin."
---

# Toggle Parallel Routing

This skill intercepts the `/toggle-parallel` command and dynamically updates the parallel execution configurations.

## Critical Instructions:
When this command is triggered by the user:

1. **Locate Configuration:** Locate the plugin configuration file at `agy-cortex/config.json`.
2. **Toggle the State:**
   - Read the existing content of `agy-cortex/config.json`.
   - Read the current boolean value of `experimental_parallel_routing`.
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
│  🧬  AGY CORTEX PARALLEL ROUTING : ENABLED             │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ ACTIVE ]                                     │
│  Mode:  Experimental Parallel Subagent Branching       │
│                                                        │
│  » Non-overlapping tasks will be decomposed and run    │
│    concurrently in isolated workspaces.                 │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### If Disabled:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX PARALLEL ROUTING : DISABLED            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ INACTIVE ]                                   │
│  Mode:  Standard Sequential Task Execution             │
│                                                        │
│  » All tasks will run sequentially through single-tier │
│    delegation flows.                                   │
│                                                        │
└────────────────────────────────────────────────────────┘
```
