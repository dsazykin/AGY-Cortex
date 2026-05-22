---
name: review
description: "Spawn L4 Senior Developer to review active git diff modifications."
---

# Code Review & Integrity Audit

This skill intercepts the `/review` command to perform a high-fidelity review of all modified code blocks.

## Critical Instructions:
When this command is triggered by the user:

1. **Obtain Git Diff**:
   - Run a `git diff` or `git status` check to identify modified files.
   - If there are no modifications detected on the active branch, output a styled card informing the user that the workspace is clean and terminate immediately.

2. **Boot L4 Senior Developer**:
   - Spawn the **L4 Senior Developer** (`senior.json`) via `invoke_subagent`.
   - Pass the active git diff as context, along with a strict review instruction.
   - Ensure safety shielding: Instruct L4 Senior that they are strictly sandboxed and forbidden from writing or replacing files during this review.
   - Example prompt for L4 Senior:
     `CRITICAL: You are running in direct manual mode via the /review command. You are strictly forbidden from modifying any files or calling any file-writing or file-replacing tools (such as write_file or replace).
     
     Your task is to review the following active git diff for logic bugs, styling alignment, performance issues, and architectural consistency:
     
     <git_diff>
     
     Please provide a beautifully styled, high-fidelity code review, referencing file lines and highlighting any potential problems.`

3. **Display Premium Card**:
   - Output the premium review status card before handing off.
   - Once L4 Senior completes, output its structured review report cleanly.

---

### UI Card Design Specification
Use the following premium ASCII outline layout during reviews:

```text
┌────────────────────────────────────────────────────────┐
│  🧬  AGY CORTEX : ACTIVE CODE AUDIT IN PROGRESS        │
├────────────────────────────────────────────────────────┤
│                                                        │
│  State:  [ AUDITING ACTIVE DIFF ]                      │
│  Worker: [ L4 SENIOR DEVELOPER ]                       │
│  Target: [ ACTIVE MODIFICATIONS ]                      │
│                                                        │
│  » Running git diff analysis and inspecting files...    │
│  » Verification for logic, style, and architectural alignment.│
│                                                        │
└────────────────────────────────────────────────────────┘
```
