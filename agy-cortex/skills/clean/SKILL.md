---
name: clean
description: "Purge active session states (.session_map.json and .cortex_plan.md) from the workspace to restore a pristine state."
---

# Purge Active Pipeline States

This skill intercepts the `/clean` command and deletes active blackboard and plan files.

## Critical Instructions:
When this command is triggered:

1. **Delete States:**
   - Detect and delete `.session_map.json` from workspace root.
   - Detect and delete `.cortex_plan.md` from workspace root.
2. **Display Confirmation Card:** Show a beautifully formatted premium purge confirmation ASCII card.
3. **Terminate turn immediately.**

---

### UI Card Design Specification
Use the following premium ASCII structure:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : ACTIVE PIPELINE PURGED               │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Files Cleaned:                                        │
│  » .session_map.json                                   │
│  » .cortex_plan.md                                     │
│                                                        │
│  State: [ READY / PRISTINE ]                           │
│                                                        │
└────────────────────────────────────────────────────────┘
```
