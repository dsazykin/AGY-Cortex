---
name: toggle-mode
description: "Toggle or set the AGY Cortex execution mode (Economy or Performance)."
---

# Toggle or Set Execution Mode

This skill intercepts the `/mode` or `/toggle-mode` command and dynamically updates the execution mode configuration.

## Critical Instructions:
When this command is triggered by the user:

1. **Read Configuration Immediately**: Retrieve `config.json` by targeting the dynamic global plugin configuration path:
   - **Windows**: `%USERPROFILE%\.gemini\config\plugins\ctx\config.json` (resolve `%USERPROFILE%` dynamically)
   - **macOS/Linux**: `~/.gemini/config/plugins\ctx\config.json` (resolve `~` or `$HOME` dynamically)
   Directly call the `read_file` tool on this global path. Do NOT perform broad directory listings or filesystem scans.
2. **Determine Target Mode**:
   - Extract the optional argument provided with the command (e.g. `/mode economy` or `/mode performance`).
   - If a specific valid argument is passed (`economy` or `performance`), set `execution_mode` directly to that value (case-insensitive).
   - If no argument is provided, toggle the current state of `execution_mode`:
     - If it is currently `"economy"`, set it to `"performance"`.
     - If it is `"performance"` (or missing), set it to `"economy"`.
3. **Save Configuration Immediately**: Write the updated JSON back to the exact path from which it was read using the `replace` or `write_file` tool.
4. **Display Premium Confirmation Card**:
   - Output a beautifully formatted visual card announcing the new state to the user.
   - Do NOT run the triage subagent loop or any standard execution tasks. 
   - Terminate the turn immediately after displaying the confirmation card.

---

### UI Card Design Specification
Use the following high-fidelity visual representations in your confirmation message:

#### If Economy Mode is Set:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX EXECUTION MODE : ECONOMY               │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ ACTIVE ]                                     │
│  Mode:  Single-Agent Economy Execution                 │
│                                                        │
│  » Bypasses separate Planner subagent orchestrations    │
│    and user-approval halts. Worker holds full single-  │
│    agent planning and testing autonomy to save tokens. │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### If Performance Mode is Set:
```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX EXECUTION MODE : PERFORMANCE           │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State: [ ACTIVE ]                                     │
│  Mode:  High-Discipline Multi-Agent Planning           │
│                                                        │
│  » Executes full system planning (.cortex_plan.md)     │
│    via the Planner subagent with user-in-the-loop      │
│    "/approve" gates to guarantee production quality.   │
│                                                        │
└────────────────────────────────────────────────────────┘
```
