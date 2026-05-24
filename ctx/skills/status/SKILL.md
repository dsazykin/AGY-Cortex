---
name: status
description: "View the current status, active toggles, and blackboard mapping details of the AGY Cortex framework."
---

# Operational Pipeline Status Dashboard

This skill intercepts the `/status` command and displays a highly detailed operational status card.

## Critical Instructions:
When this command is triggered:

1. **Read Configurations & States:**
   - Retrieve `config.json` via global path resolving.
   - Attempt to read `.session_map.json` in workspace root.
2. **Determine Active Modes:**
   - Detect routing enabled (`model_routing_enabled`).
   - Detect parallel enabled (`experimental_parallel_routing`).
   - Detect planning enabled (`planning_mode_enabled`).
   - Determine if the blackboard is loaded or empty.
3. **Display Visual Card:** Show a beautifully aligned premium status ASCII card.
4. **Terminate turn immediately.**

---

### UI Card Design Specification
Use the following premium ASCII structure:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : PIPELINE SYSTEM STATUS               │
├────────────────────────────────────────────────────────┤
│                                                        │
│  [Routing]    [ ACTIVE/BYPASSED ]                      │
│  [Planning]   [ ACTIVE/BYPASSED ]                      │
│  [Parallel]   [ ACTIVE/BYPASSED ]                      │
│  [Mode]       [ ECONOMY/PERFORMANCE ]                  │
│  [Blackboard] [ LOADED/EMPTY ]                         │
│                                                        │
│  » Blackboard details are shown here...                │
│                                                        │
└────────────────────────────────────────────────────────┘
```
