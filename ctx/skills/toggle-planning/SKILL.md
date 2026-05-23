---
name: toggle-planning
description: "Toggle the Dynamic Planning Gate and approval loops for the AGY Cortex plugin."
---

# Toggle Planning Mode

This skill intercepts the `/toggle-planning` command and dynamically updates the planning pipeline configuration.

## Critical Instructions:
When this command is triggered by the user:

1. **Read Configuration Immediately:** Retrieve `config.json` by targeting the dynamic global plugin configuration path based on where your home directory is located:
   - **Windows:** `%USERPROFILE%\.gemini\antigravity-cli\plugins\agy-cortex\config.json` (resolve `%USERPROFILE%` dynamically)
   - **macOS/Linux:** `~/.gemini/antigravity-cli/plugins/agy-cortex/config.json` (resolve `~` or `$HOME` dynamically)
   You MUST only read and modify this global configuration file. Never attempt to read, write, or create a local fallback configuration in the workspace.
   Directly call the `read_file` tool on this global path. Do NOT perform any broad directory listings, grep searches, or filesystem scans.
2. **Toggle the State:**
   - Read the current boolean value of `planning_mode_enabled` from the loaded JSON.
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
│  🧬  AGY CORTEX PLANNING PIPELINE : ENABLED            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ ACTIVE ]                                     │
│  Mode:  Dynamic Multi-Agent Technical Planning         │
│                                                        │
│  » The Planner will evaluate your prompt, analyze risks,│
│    and draft a detailed architectural plan for approval│
│    before executing any code modifications.            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### If Disabled:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX PLANNING PIPELINE : DISABLED           │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ BYPASSED ]                                   │
│  Mode:  Direct Strategy & Immediate Implementation     │
│                                                        │
│  » Workers will modify files immediately based on direct│
│    routing triage, bypassing the planning approval gate.│
│                                                        │
└────────────────────────────────────────────────────────┘
```
