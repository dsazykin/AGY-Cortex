---
name: cortex
description: "Directly invoke a specific AGY Cortex agent tier, bypassing L0 Router triage."
---

# Direct Cortex Agent Routing

This skill intercepts the `/cortex <tier> <prompt>` slash command and executes a direct bypass routing mechanism, bypassing the L0 Router triage.

## Valid Tiers:
- `librarian` (L1): Explores the codebase, updates files/symbols, and builds the Blackboard.
- `junior` (L2): High-output code drafting, templates, boilerplates, migrations.
- `engineer` (L3): Core logic implementation, refactoring, advanced coding.
- `senior` (L4): Deep debugging, architectural review, strategy audit.
- `architect` (L5): Strategic direction, high-level invariants, structural layout.
- `decomposer` (Utility): Task planning, contract writing, parallel partition setup.
- `integrator` (Utility): Merge reconciliation, linting, conflict resolution, test suites.

## Critical Invariants & Rules:

1. **Tier Validation**:
   - Verify the chosen `<tier>` matches one of the valid tiers listed above.
   - If the tier is invalid, output a styled warning card with the allowed tiers and terminate the turn immediately.

2. **Memory Preservation Check**:
   - If the user targets `junior` or `engineer` but `.session_map.json` is missing from the repository root, you MUST run **L1 Librarian** (`librarian.json`) first to build the blackboard.
   - Specifically, boot L1 Librarian, wait for it to generate `.session_map.json` and update `.gitignore`, and only *then* invoke the targeted worker subagent (`junior` or `engineer`), forwarding the original request.

3. **Context / Safety Shielding Check**:
   - If the user targets `senior` (`senior.json`) or `architect` (`architect.json`), you MUST inject a strict sandbox directive in their invocation prompt:
     `CRITICAL: You are running in direct manual mode via the /cortex command. You are strictly forbidden from modifying any files or calling any file-writing or file-replacing tools (such as write_file or replace). Your task is strictly analysis, review, or design. If any changes are needed, you must describe them instead of executing them.`

4. **Visual Branding Output**:
   - Prior to calling the subagent, output a high-fidelity visual bypass transition card.

---

### UI Card Design Specification
Use the following premium ASCII outline layout in your status transition:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : DIRECT ORCHESTRATION BYPASS          │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Target Tier:  [ <tier_name> ]                         │
│  State:        [ DIRECT DELEGATION ]                   │
│  Status:       [ BYPASSING L0 ROUTER ]                 │
│                                                        │
│  » Directly routing task prompt to target worker       │
│    subagent...                                         │
│                                                        │
└────────────────────────────────────────────────────────┘
```
