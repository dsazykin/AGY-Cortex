---
name: visualize
description: "Scan repository and construct dynamic Mermaid dependency or workflow charts of workspace files."
---

# Architecture Visualization Engine

This skill intercepts the `/visualize` command and delegate-spawns L1 Librarian / L5 Architect to construct a Mermaid dependency chart.

## Critical Instructions:
When this command is triggered:

1. **Display Active Status Card:** Print a beautifully formatted visualization active status card immediately.
2. **Boot L1 Librarian / L5 Architect:** Spawn `librarian.json` or `architect.json` via `invoke_subagent` instructing it to perform a complete codebase structural scan, identify core file interactions, and generate a dynamic architectural Mermaid diagram.
3. **Wait & Deliver Findings:** Wait for the subagent to report, prepend the correct branding header (`>>> [L5 | ARCHITECT | Gemini 3.5 Pro]` or `>>> [L1 | LIBRARIAN | Gemini 2.5 Flash Lite]`), and output the Mermaid code blocks alongside structural explanations.
4. **Terminate turn.**

---

### UI Card Design Specification
Use the following premium ASCII structure:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : ARCHITECTURE VISUALIZATION            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State:  [ GRAPHING CONTEXT ]                          │
│  Worker: [ L5 | ARCHITECT | Gemini 3.5 Pro ]           │
│                                                        │
│  » Scanning file hierarchy and dependency boundaries...│
│  » Rendering modular dependency graph (Mermaid)...     │
│                                                        │
└────────────────────────────────────────────────────────┘
```
