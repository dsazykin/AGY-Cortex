---
name: verify
description: "Spawn L3.5 Tester in the background to execute verification sweeps, run tests, and check codebase health."
---

# Workspace Verification Sweep

This skill intercepts the `/verify` command and delegate-spawns L3.5 Tester to run comprehensive test suites and validations.

## Critical Instructions:
When this command is triggered:

1. **Display Active Status Card:** Print a beautifully formatted verification active status card immediately.
2. **Boot L3.5 Tester:** Spawn `tester.json` via `invoke_subagent` instructing it to perform a thorough build, lint, and test validation check on the current workspace.
3. **Wait & Deliver Findings:** Wait for the subagent to report, prepend the `L3.5` tester branding header (`>>> [L3.5 | TESTER | Gemini 3.5 Flash]`), and output the final test report.
4. **Terminate turn.**

---

### UI Card Design Specification
Use the following premium ASCII structure:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : ACTIVE VERIFICATION SWEEP            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State:  [ EXECUTING TESTS ]                           │
│  Worker: [ L3.5 | TESTER | Gemini 3.5 Flash ]          │
│                                                        │
│  » Scanning workspace for test folders and files...    │
│  » Running linters and executing unit test suites...   │
│                                                        │
└────────────────────────────────────────────────────────┘
```
