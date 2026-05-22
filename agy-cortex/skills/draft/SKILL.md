---
name: draft
description: "Directly invoke L2 Junior Developer to generate boilerplate, templates, or migrations."
---

# Code Drafting & Scaffolding

This skill intercepts the `/draft <prompt>` command to quickly generate templates, boilerplates, or migration scripts using L2 Junior Developer.

## Critical Instructions:
When this command is triggered by the user:

1. **Verify Session Map**:
   - Check if `.session_map.json` is present at the repository root.
   - If `.session_map.json` is missing, print a highly visible warning indicating that no active discovery session exists and details might be less aligned, but proceed anyway.

2. **Boot L2 Junior Developer**:
   - Spawn the **L2 Junior Developer** (`junior.json`) via `invoke_subagent`.
   - Forward the user's prompt, instructing them to consume `.session_map.json` if present and draft/create the requested template, boilerplate, or migration files.
   - If files are modified, ensure that a standard L3 (Core Engineer) verification step is triggered at the end of the execution block to double-check syntax/compilation.

3. **Display Premium Card**:
   - Output the premium draft status card.
   - Deliver the junior developer's drafted files and reports cleanly to the user.

---

### UI Card Design Specification
Use the following premium ASCII outline layout during drafts:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : RAPID CODE DRAFTING ACTIVE           │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State:  [ BOOTSTRAPPING SCAFFOLDING ]                 │
│  Worker: [ L2 JUNIOR DEVELOPER ]                       │
│  Task:   [ DIRECT CODE DRAFT ]                         │
│                                                        │
│  » Spawning junior worker for templating/boilerplate...│
│  » Preserving blackboard session if active.            │
│                                                        │
└────────────────────────────────────────────────────────┘
```
