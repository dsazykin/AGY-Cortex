---
name: toggle-parallel
description: "Toggle the experimental parallel agent routing on or off for the AGY Cortex plugin."
---

# Toggle Parallel Routing

This skill intercepts the `/toggle-parallel` command and dynamically updates the parallel execution configurations.

## Critical Instructions:
When this command is triggered by the user:

1. **Read Configuration Immediately:** Retrieve `config.json` by targeting the dynamic global plugin configuration path based on where your home directory is located:
   - **Windows:** `%USERPROFILE%\.gemini\antigravity-cli\plugins\agy-cortex\config.json` (resolve `%USERPROFILE%` dynamically)
   - **macOS/Linux:** `~/.gemini/antigravity-cli/plugins/agy-cortex/config.json` (resolve `~` or `$HOME` dynamically)
   You MUST only read and modify this global configuration file. Never attempt to read, write, or create a local fallback configuration in the workspace.
   Directly call the `read_file` tool on this global path. Do NOT perform any broad directory listings, grep searches, or filesystem scans.
2. **Toggle the State:**
   - Read the current boolean value of `experimental_parallel_routing` from the loaded JSON.
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
