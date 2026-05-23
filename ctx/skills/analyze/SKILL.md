---
name: analyze
description: "Run L1 Librarian codebase discovery on the workspace or a specified subdirectory."
---

# Codebase Analysis & Blackboard Initialization

This skill intercepts the `/analyze [path]` command and triggers L1 Librarian to run codebase discovery.

## Critical Instructions:
When this command is triggered by the user:

1. **Parse Target Path**:
   - Extract the target path if provided (e.g. `/analyze agy-cortex` -> path: `agy-cortex`).
   - If no path is provided, default to the entire active repository root (`./`).

2. **Boot L1 Librarian**:
   - Spawn the **L1 Librarian** (`librarian.json`) via `invoke_subagent`.
   - Pass an instruction prompt telling L1 Librarian to scan the workspace or specified directory path, find its structure/symbols, initialize the structured `.session_map.json` blackboard, and append it to `.gitignore` if not already present.
   - Example Librarian prompt: `Please run an exhaustive directory scan and codebase analysis of the workspace (target path: '<path>'), document key files and structures, and compile a structured .session_map.json blackboard at the repository root.`

3. **Display Premium Card & Outputs**:
   - Prior to booting, output a premium ASCII status card.
   - Once L1 Librarian finishes and reports back, print its final findings, structural outline, and symbol map beautifully to the user.

---

### UI Card Design Specification
Use the following premium ASCII outline layout during analysis:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : CODEBASE DISCOVERY IN PROGRESS       │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State:  [ ACTIVE DISCOVERY ]                         │
│  Worker: [ L1 LIBRARIAN ]                              │
│  Target: [ <path> ]                                    │
│                                                        │
│  » Scanning symbols, directories, and invariants.      │
│  » Initializing dynamic .session_map.json blackboard.  │
│                                                        │
└────────────────────────────────────────────────────────┘
```
