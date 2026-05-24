---
name: toggle-routing
description: "Toggle the Hub-and-Spoke Tiered Intelligence Orchestration on or off for the AGY Cortex plugin."
---

# Toggle Model Routing

This skill intercepts the `/toggle-routing` command and dynamically updates the orchestration pipeline configurations.

## Critical Instructions:
When this command is triggered by the user:

1. **Read Configuration Immediately:** Retrieve `config.json` by targeting the dynamic global plugin configuration path based on where your home directory is located:
   - **Windows:** `%USERPROFILE%\.gemini\config\plugins\ctx\config.json` (resolve `%USERPROFILE%` dynamically)
   - **macOS/Linux:** `~/.gemini/config/plugins/ctx/config.json` (resolve `~` or `$HOME` dynamically)
   You MUST only read and modify this global configuration file. Never attempt to read, write, or create a local fallback configuration in the workspace.
   Directly call the `read_file` tool on this global path. Do NOT perform any broad directory listings, grep searches, or filesystem scans.
2. **Toggle the State:**
   - Read the current boolean value of `model_routing_enabled` from the loaded JSON.
   - If it is missing or `false`, update it to `true`.
   - If it is `true`, update it to `false`.
3. **Save Configuration Immediately:** Write the updated JSON back to the exact path from which it was read (using the `replace` or `write_file` tool).
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
