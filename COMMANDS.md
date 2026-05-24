# AGY Cortex Slash Commands Reference

Welcome to the command reference manual for **AGY Cortex**, the tiered multi-agent orchestration plugin for the **Antigravity CLI**. 

AGY Cortex provides high-signal slash commands directly in the Antigravity TUI interface. These commands give you absolute control over multi-agent triage routing, plan approvals, sandbox executions, and codebase discovery.

---

## Command Index

Here is a summary of all available slash commands in the AGY Cortex ecosystem:

| Command | Category | Purpose | Target Agent / Execution |
| :--- | :--- | :--- | :--- |
| [`/toggle-routing`](#/toggle-routing) | Configuration | Enable/disable multi-agent triage loop | Coordinator (Main Agent) |
| [`/toggle-planning`](#/toggle-planning) | Configuration | Enable/disable implementation plan loops | Coordinator (Main Agent) |
| [`/toggle-parallel`](#/toggle-parallel) | Configuration | Enable/disable isolated parallel work | Coordinator (Main Agent) |
| [`/toggle-mode`](#/toggle-mode) | Configuration | Toggle or set execution mode (Economy/Performance) | Coordinator (Main Agent) |
| [`/status`](#/status) | Info & Diagnostics | Print real-time pipeline status dashboard | Coordinator (Main Agent) |
| [`/question <prompt>`](#/question) | Direct Inquiry | Bypass triage and speak directly to L0 | Coordinator (Main Agent) |
| [`/analyze [path]`](#/analyze) | Discover | Scan codebase structure & build blackboard | L1 Librarian (`librarian.json`) |
| [`/draft <prompt>`](#/draft) | Scaffolding | Generate boilerplates & scaffolds rapidly | L2 Junior Developer (`junior.json`) |
| [`/verify`](#/verify) | Quality Assurance | Execute tests & verification suites | L3.5 Tester (`tester.json`) |
| [`/review`](#/review) | Code Audit | Review git modifications for safety & quality | L4 Senior Developer (`senior.json`) |
| [`/cortex <tier> <prompt>`](#/cortex) | Direct Delegation | Bypass triage router to trigger specific tier | Selected Agent Tier (L1-L5) |
| [`/clean`](#/clean) | Maintenance | Delete active session maps and plan files | Coordinator (Main Agent) |

---

## Detailed Command Reference

### `/toggle-routing`
Toggles the **Hub-and-Spoke Tiered Intelligence Orchestration** on or off.
*   **Aliases:** None
*   **Default State:** `ENABLED` (Active)
*   **Behavior:**
    *   **Enabled:** Standard tasks are parsed by L0 Router and routed down the specialist pipeline.
    *   **Disabled (Bypassed):** Standard tasks are processed directly in the main conversation window by the Coordinator, acting as a standard single-agent executor.

> [!TIP]
> Use `/toggle-routing` when you want to execute quick, simple edits without triggering subagent spawns.

---

### `/toggle-planning`
Enables or disables the **Dynamic Planning Gate** for execution workers.
*   **Aliases:** None
*   **Default State:** `ENABLED` (Active)
*   **Behavior:**
    *   **Enabled:** Complex feature edits halt execution to present a detailed design plan (`.cortex_plan.md`) and await your explicit approval (`/approve`).
    *   **Disabled:** Workers execute code modifications directly without generating design plans or halting.

---

### `/toggle-parallel`
Enables or disables **Isolated Parallel Workspaces**.
*   **Aliases:** None
*   **Default State:** `ENABLED` (Active)
*   **Behavior:**
    *   **Enabled:** Multi-layered tasks are split by the Decomposer, executed in isolated git worktrees concurrently, and merged/validated by the Integrator.
    *   **Disabled:** Multi-layered tasks are executed sequentially in your main workspace.

---

### `/toggle-mode`
Toggles or sets the active **Execution Mode** (Economy or Performance).
*   **Aliases:** `/mode [economy|performance]`
*   **Default State:** `performance`
*   **Syntax:**
    *   `/toggle-mode` or `/mode` (without arguments): Toggles the state between Economy and Performance.
    *   `/mode economy`: Sets the execution directly to Economy Mode.
    *   `/mode performance`: Sets the execution directly to Performance Mode.
*   **Behavior:**
    *   **Economy Mode:** Bypasses Plan subagent generation and the `/approve` confirmation gate. Workers (L2/L3) execute directly with full single-agent autonomy. Medium tasks prioritize **L2 Junior** Flash, and complex strategic logic routes to the direct **L3.5 Pro Engineer** (`gemini-3.1-pro`) worker.
    *   **Performance Mode:** Enables full planning loops (`.cortex_plan.md`) with explicit user approval halts to ensure maximum structural discipline.

---

### `/status`
Displays a real-time status card showing your configuration settings, execution mode, and active blackboard registry status.
*   **Aliases:** `/info`
*   **Example Output:**
    ```text
    ┌────────────────────────────────────────────────────────┐
    │  🧬  AGY CORTEX : PIPELINE SYSTEM STATUS               │
    ├────────────────────────────────────────────────────────┤
    │                                                        │
    │  [Routing]    [ ACTIVE ]                               │
    │  [Planning]   [ ACTIVE ]                               │
    │  [Parallel]   [ ACTIVE ]                               │
    │  [Mode]       [ PERFORMANCE ]                          │
    │  [Blackboard] [ LOADED ]                               │
    │                                                        │
    │  » Blackboard: 12 files, 48 symbols mapped            │
    │  » Plan File: .cortex_plan.md (Absent)                 │
    │                                                        │
    └────────────────────────────────────────────────────────┘
    ```

---

### `/question <prompt>`
Bypasses the entire multi-agent triage loop to directly pose a question to the main Coordinator.
*   **Aliases:** `/q`, `/ask`
*   **Use Cases:** For asking questions, seeking design advice, explaining architectural details, or requesting quick documentation lookups without spinning up Librarian or Architect.

---

### `/analyze [path]`
Triggers **L1 Librarian** to map the folder structure and construct the `.session_map.json` blackboard.
*   **Aliases:** None
*   **Default Path:** `./` (Workspace root)
*   **Behavior:** Populates imports, exports, functions, and file mappings onto the shared blackboard so workers bypass expensive scans.

---

### `/draft <prompt>`
Triggers **L2 Junior Developer** to generate template structures, boilerplate files, or boilerplate logic.
*   **Aliases:** None
*   **Handoff:** Automatically hands off modifications to **L3.5 Tester** to compile, lint, and verify health.

---

### `/verify`
Triggers **L3.5 Tester** to perform a complete codebase validation sweep.
*   **Aliases:** `/test`
*   **Behavior:** Detects your testing framework (e.g. Jest, PyTest, JUnit) and runs the linter and unit tests in the background, outputting a detailed health report.

---

### `/review`
Retrieves workspace modifications (`git diff`) and boots **L4 Senior Developer** under a write-protected sandbox.
*   **Aliases:** None
*   **Behavior:** Outputs a thorough code audit evaluating style consistency, potential bug risks, performance issues, and security vulnerabilities.

---

### `/cortex <tier> <prompt>`
Force-delegates a task directly to a specific specialist subagent, completely bypassing L0 triage router.
*   **Available Tiers:**
    *   `librarian` (L1) — Discovery and file search.
    *   `junior` (L2) — Scaffolding and quick drafts.
    *   `engineer` (L3) — Core feature implementation.
    *   `tester` (L3.5) — Testing and test suite generation.
    *   `pro_engineer` (L3.5 Pro) — Direct high-reasoning execution worker (Economy Mode only).
    *   `senior` (L4) — Sandbox reviews and ADR curation.
    *   `architect` (L5) — Design analysis and strategic pivots.
    *   `decomposer` (Utility) — Concurrent division of tasks.
    *   `integrator` (Utility) — Merging worktree branches.

> [!WARNING]
> Tiers `senior` and `architect` are running under strict **Context Shielding** during manual manual cortex runs. All file-writing or modifying privileges are blocked.

---

### `/clean`
Purges the active shared memory and cached plan files from your workspace directory.
*   **Aliases:** `/reset`
*   **Files Deleted:** `.session_map.json` (blackboard), `.cortex_plan.md` (plan file).

---

## Typical Workflows

### Rapid Scaffold and Verify Loop
1. Draft the DB migrations and API models: `/draft generate mock user schema with fields id, email, role`
2. Instantly verify syntax and compilation: `/verify`

### Clean Re-Scanning
1. Clean previous execution logs and session memory residue: `/clean`
2. Perform a fresh structural code scan: `/analyze`
3. Talk to the main coordinator about the scanned structure: `/question explain the dependencies mapped in our symbol registry`
