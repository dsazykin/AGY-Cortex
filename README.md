# AGY Cortex Plugin

A sophisticated, globally installable plugin for the Antigravity (AGY) CLI. AGY Cortex replaces a single "do-it-all" model with a specialized team of expert agents, automatically routing your prompts to the most appropriate tier to maximize reasoning depth while maintaining extreme context efficiency and operational transparency.

---

## The 5-Tier Architecture

The plugin uses a flat `agents/` directory structure containing distinct agent tiers, each optimized for specific responsibilities. Prompt routing is handled automatically based on the logic defined in the `rules/routing.md` file.

| Tier | Agent | LLM Model | Primary Responsibility |
| :--- | :--- | :--- | :--- |
| **L0** | **Router** | `Gemini 2.5 Flash Lite` | Prompt triage, clarification, and subagent routing. |
| **L1** | **Librarian** | `Gemini 2.5 Flash Lite` | Codebase exploration, context filtering, and blackboard creation. |
| **L2** | **Junior** | `Gemini 3.1 Flash` | High-output drafting (boilerplates, mock files, migrations) & syntax checks. |
| **L3** | **Engineer** | `Gemini 3.5 Flash` | Full feature implementations, testing sweeps, and integration verification. |
| **L4** | **Senior** | `Gemini 3.1 Pro` | Review, strategic debugging, and automatic ADR curation. |
| **L5** | **Architect** | `Gemini 3.5 Pro` | High-level system design, strategic pivots, and core invariants owner. |
| **Utility** | **Decomposer** | `Gemini 3.1 Pro` | Dependency mapping, task decomposition, and shared API contract planning. |
| **Utility** | **Integrator** | `Gemini 3.5 Flash` | Parallel workspace merging, git conflict reconciliation, and unified verification. |

---

## Advanced Systems & Operational Mechanics

### 1. Two-Tiered Shared Memory & Context Filtering
To solve long-term context window bloat and eliminate API token waste, the plugin establishes a two-tiered memory architecture:
* **Tier 1: Master Focal Registry & ADR Archive**: 
  - `CONTEXT.md` acts as a lightweight focal registry containing the **Active Focal Task**, a high-signal index table of archived ADRs, and active global invariants.
  - Historic Architectural Decision Records (ADRs) are archived locally under `.antigravitycli/adr/adr-XXX.md` to keep `CONTEXT.md` lean.
* **Tier 2: Active Session Blackboard (`.session_map.json`)**: 
  - A temporary runtime file generated at the project root and automatically ignored via `.gitignore` to keep git history pristine.
* **Dynamic L1 Context Filter**: On boot, the L1 Librarian reads `CONTEXT.md`, filters *only* the specific active invariants relevant to the active task, and writes them to the blackboard.
* **Execution Bypass**: L2 and L3 bypass reading `CONTEXT.md` entirely, reading strictly from `.session_map.json` to achieve zero token waste and ultra-fast boot times.
* **Automated Curation**: When a strategic task is closed out, L4 Senior and L5 Architect agents automatically archive details into a new ADR markdown file under `.antigravitycli/adr/` and clear the active task in `CONTEXT.md`.

### 2. The Draft-then-Verify Pipeline
To optimize token usage during heavy generation:
* **L2 Junior** is upgraded to a high-output drafting engine (boilerplates, REST scaffolds, unit test frames) equipped with syntax-checking tools to check for errors before submitting.
* Once L2 succeeds, the orchestrator automatically triggers the pipeline, spawning **L3 Core Engineer** to run full test suites, verify integration, and guarantee complete compatibility.

### 3. Dynamic Re-routing Protocol
If an execution agent (L2/L3) self-assesses that a task's complexity exceeds its technical boundary (e.g. L2 needs deep logical troubleshooting or L3 needs high-level design changes), it aborts and returns `"status": "re-route"`. The Orchestrator immediately intercepts this and triggers a refined triage through the L0 Router.

### 4. Visual Branding Hook
We utilize a system-level hook (`PreInvocation` mapped to `hooks/visual_branding.py`) that handles formatting and prepending agent headers (e.g. `>>> [L3 | ENGINEER | Gemini 3.5 Flash]`) at the system level. Prompts remain 100% focused on logic rather than header formatting.

### 5. Automated Intent Alignment Review (Native Subagent Verification)
To safeguard system design and quality, the Orchestrator implements a native, subagent-driven intent alignment review in Step 5 of the routing loop:
* **Trigger Condition**: Automatically triggers after any Strategy Tier (**L4 Senior** or **L5 Architect**) completes a task and makes modifications.
* **Alignment Analysis**: The Orchestrator automatically captures the working tree modifications via `git diff HEAD` and spawns the **L4 Senior** subagent (`senior.json`) using `invoke_subagent`.
* **Self-Correction**: If L4 identifies any deviations or mismatches, it returns detailed, constructive feedback. The Orchestrator blocks session conclusion, surfaces the feedback, and re-delegates the task back to the execution/strategy agents to self-correct.

### 6. Experimental Parallel Routing & Concurrent Execution (ADR-005)
To maximize throughput for complex tasks containing independent, non-overlapping work vectors (e.g. database schema setup + React visual styling), the plugin introduces a high-performance parallel routing strategy:
*   **Double-Toggle Mechanism (Option A + C)**: Persistent configuration is stored in `config.json` and can be toggled instantly via natural language chat commands (the Orchestrator writes directly to the config file).
*   **The Specialized Decomposer Agent**: Spawns first to perform dependency mapping, set absolute file boundaries for workers, and write a strict, shared API interface contract inside `.session_map.json`.
*   **User-in-the-Loop Confirmation Gate**: The Orchestrator halts and displays the Decomposer's proposed plans, contracts, and boundaries, blocking execution until the user clicks **[Yes, run parallel]**.
*   **Concurrent Isolated Workspaces**: Execution workers are launched concurrently in isolated `share` workspaces backed by git worktrees to completely avoid mid-write file overwrites.
*   **The Specialized Integrator Agent**: Automatically merges the workspaces back, parses and resolves git merge conflict markers manually, and runs test/lint scripts to verify full system compilation.

---

## Installation & Setup Requirements

### Environment Requirements
* **Python**: Python 3.x is required for executing the pre-invocation visual branding hook.

### Installation Steps

1. **Clone** the repository to your local machine.
2. **Validate the plugin structure**:
   ```bash
   agy plugin validate ./agy-cortex
   ```
3. **Install Globally via AGY CLI**:
   ```bash
   agy plugin install ./agy-cortex --global
   ```
4. **Update (if changes are made)**:
   ```bash
   agy plugin install ./agy-cortex --global --force
   ```
5. **Verify**:
   ```bash
   agy plugin list
   ```

Submit your tasks normally, and the intelligent routing will automatically engage the right expert for the job!
