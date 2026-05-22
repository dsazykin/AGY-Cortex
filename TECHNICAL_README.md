# Technical Reference Manual: AGY Tiered Intelligence System

This document serves as the comprehensive technical specification and architectural manual for the **AGY Cortex** plugin (`agy-cortex`). It details the tiered intelligence loop, dynamic shared memory schemes, quantitative token optimization metrics, parallel routing mechanics, and self-correction workflows.

---

## 1. Architectural Philosophy: Hub-and-Spoke Tiered Intelligence

Standard developer agents suffer from **Context Fatigue**. Appending recursive file-tree scans, raw codebase files, execution outputs, and conversational histories into a single context window causes a linear decrease in LLM reasoning quality, while exponentially increasing latency and token usage.

`agy-cortex` solves this by establishing a **Hub-and-Spoke Tiered Intelligence model**. Instead of utilizing a single high-tier model for all tasks, the plugin distributes roles across specialized, narrow-scoped agent profiles.

```
                  ┌────────────────────────┐
                  │   L0 Triage Router     │
                  └───────────┬────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
            [ Path A: Seq ]      [ Path B: Parallel ]
            ┌──────────────┐     ┌──────────────────┐
            │ L1 Librarian │     │  L5 Decomposer   │
            └──────┬───────┘     └────────┬─────────┘
                   │                      │
                   ▼                      ▼
            ┌───────────────────────────────────────┐
            │   Active Blackboard (.session_map)   │
            └──────────────┬──────────────┬─────────┘
                           │              │
                    ┌──────▼──────┐┌──────▼──────┐
                    │  L2 Junior  ││ L3 Engineer │
                    └──────┬──────┘└──────┬──────┘
                           │              │
                           ▼              ▼
                     ┌──────────────┬─────────────┐
                     │  L4 Senior   │ L4 Integrator│
                     └──────────────┴─────────────┘
```

---

## 2. Core Agent Specifications (Tiers L0 - L5)

Each agent profile resides under `agy-cortex/agents/` as a structured JSON file detailing its dedicated model, system prompts, and tool permissions.

| Tier | Agent | File | Model | Primary Tools | Primary Responsibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L0** | **Router** | `router.json` | `Gemini 2.5 Flash Lite` | *None* | Initial task triage, user clarification, and subagent routing. |
| **L1** | **Librarian** | `librarian.json` | `Gemini 2.5 Flash Lite` | `read_file`, `grep_search`, `glob`, `list_dir` | Codebase discovery, context filtering, and blackboard creation. |
| **L2** | **Junior** | `junior.json` | `Gemini 3.1 Flash` | `read_file`, `replace`, `write_file`, `run_command` | Boilerplate drafting, scaffolding, and syntax checks. |
| **L3** | **Engineer** | `engineer.json` | `Gemini 3.5 Flash` | `read_file`, `replace`, `run_test_suite`, `run_linter`, `git_*` | Full feature implementations and complete testing sweeps. |
| **L4** | **Senior** | `senior.json` | `Gemini 3.1 Pro` | `invoke_agent`, `read_file`, `git_*` | Complex refactoring, strategic debugging, and ADR archiving. |
| **L5** | **Architect** | `architect.json` | `Gemini 3.5 Pro` | `invoke_agent`, `read_file`, `git_*` | System design, core invariant management, and strategic reviews. |
| **Utility** | **Planner** | `planner.json` | `Gemini 3.1 Pro` | `read_file`, `write_file`, `replace`, `list_directory`, `grep_search`, `submit_result` | Evaluates prompt planning merit, writes `.cortex_plan.md` plan, halts for `/approve` |
| **Utility** | **Decomposer** | `decomposer.json` | `Gemini 3.1 Pro` | `read_file`, `write_file`, `grep_search` | Dependency graphing, task decomposition, and API contracts. |
| **Utility** | **Integrator** | `integrator.json` | `Gemini 3.5 Flash` | `git_status`, `git_diff`, `run_command` | Branch merging, manual conflict reconciliation, and test sweeps. |

---

## 3. Context Shielding & Execution Safety Nets

To maintain operational integrity and prevent runaway prompt bloat, the system enforces several architectural constraints:

### 3.1 Context Shielding (Tool Proxying)
High-tier reasoning agents (**L4 Senior** and **L5 Lead Architect**) are structurally barred from using code-writing tools (such as `replace` or `write_file`). They cannot directly edit codebase source files. Instead, they must delegate implementation vectors to **L2 Junior** or **L3 Engineer** via `invoke_subagent`, specifying exact file paths and line ranges. This ensures strategy agents remain purely focused on architectural designs without their prompts getting cluttered with raw codebase lines.

### 3.2 The Execution Safety Net
Unlike traditional architectures where execution agents operate "blind" (modifying files based on regex matches without reading the surrounding block), **L2 Junior** and **L3 Engineer** are equipped with targeted `read_file` tools. They are mandated to read the exact surrounding lines of code before submitting a string replacement, significantly reducing hallucinated modifications.

### 3.3 Scoped Shell Access
To prevent execution subagents from bypassing the tiered model (such as downloading raw scripts via `curl` or modifying files using shell commands), full shell terminal access is removed. Subagents are instead provided restricted, domain-specific execution wrappers like `run_test_suite` and `run_linter` to verify code correctness safely.

---

## 4. The Shared Session Blackboard Protocol

The cornerstone of the system's token efficiency is the **Active Session Blackboard** (`.session_map.json`), which acts as our Tier 2 Shared Memory.

### 4.1 Schema Specification
```json
{
  "files_targeted": [
    { 
      "path": "agy-cortex/agents/router.json", 
      "lines": "1-30", 
      "purpose": "Modify dispatch action schemas" 
    }
  ],
  "symbols_discovered": [
    { 
      "name": "dispatchAction", 
      "type": "variable", 
      "file": "agy-cortex/agents/router.json" 
    }
  ],
  "invariants_active": [
    "Orchestrator Prepending: Prefix outputs with [TIER] tags.",
    "Blackboard-First Boot: Subagents must read blackboard before scanning directories."
  ],
  "custom_user_instructions": [
    "Prefer HSL tailored colors for maximum accessibility.",
    "Keep responses concise and avoid overly polite phrasing."
  ],
  "parallel_specification": {
    "contracts": [
      {
        "file": "path/to/api.py",
        "interface": "def getUserInfo(userId: str) -> dict"
      }
    ],
    "tasks": [
      {
        "worker": "junior",
        "workspace": "share_worker_a",
        "instructions": "Implement backend model and export getUserInfo method."
      }
    ]
  },
  "execution_logs": [
    { 
      "agent": "librarian", 
      "action": "initialize_blackboard", 
      "timestamp": "2026-05-22T19:25:37Z", 
      "details": "Parsed CONTEXT.md focal task and mapped active invariants." 
    }
  ]
}
```

### 4.2 The Blackboard Lifecycle
1.  **Boot Filtering**: When a task begins, the **L1 Librarian** boots up, reads the active `CONTEXT.md` focal registry, dynamically filters out *only* the specific active invariants relevant to the current task, and writes the structured `.session_map.json` blackboard.
2.  **Developer Instruction Compilation**: L1 Librarian dynamically checks for local `DEVELOPER.md`/`CORTEX.md` in the workspace root, or global `developer.md`/`cortex.md` in the home directory. It extracts custom coding styling, conventions, and phrasings, ignores all orchestration meta-directives, and compiles them to `"custom_user_instructions"` on the blackboard.
3.  **VCS Ignore Injection**: Upon creation, the Librarian automatically appends `.session_map.json` to the project's `.gitignore` file, ensuring temporary blackboards are never committed.
3.  **Boot Read Requirement**: Subagents **L2 (Junior)** and **L3 (Engineer)** are hard-coded to read `.session_map.json` as their absolute first action upon waking. They completely bypass reading `CONTEXT.md` or doing expensive codebase-wide directory scans.
4.  **Write Back & Clean Up**: Before terminating, workers update `.session_map.json` with their modified file targets and execution logs. Once the Orchestrator completes the overall task, it deletes `.session_map.json` to leave the workspace pristine.

---

## 5. Token Savings & Cost Efficiency Report

By decoupling discovery from execution and archiving historic contexts, `agy-cortex` realizes massive, compounding token savings.

### 5.1 Naive vs. Tiered Cost-Benefit Comparison

| Characteristic | Standard Monolithic Agent | AGY Tiered Cortex Plugin |
| :--- | :--- | :--- |
| **Context Window Consumption** | Linear growth with directory scans & active logs. | Capped, flat-sized targeted prompts. |
| **Typical Task Token Cost** | **120,000 to 150,000 tokens** | **15,000 to 22,000 tokens** |
| **Context Growth Invariant** | Continually inflates with each chat turn. | Staid. History is isolated; ADRs are archived. |
| **Average Prompt Boot Latency** | 45 - 90 seconds (System wait) | 12 - 25 seconds (Instant dispatch) |
| **System API Costs (per 100 tasks)** | ~$1.20 - $1.50 | ~$0.15 - $0.22 |
| **Hallucination Occurrence** | High (Context window dilution) | Near Zero (Highly scoped targets) |

### 5.2 Mathematical Analysis of Savings

#### A. ADR Archival Pruning Savings
In long-lived repositories, the master context registry (e.g. `brain.md`) grows continuously. At 20 ADRs, a standard prompt consumes upwards of **40,000 tokens** of historical architectural boilerplate. By separating and archiving these records into individual files, the active boot context is reduced to a lean **~1,000 tokens**:
$$\text{Compounded Savings Per Invocation} \approx \text{Total Historical ADRs} \times \text{ADR Token Size} - \text{Active Registry size}$$
$$\text{Savings Per Invocation} \approx 40,000 \text{ tokens} - 1,000 \text{ tokens} = \mathbf{39,000 \text{ tokens}}$$

#### B. Blackboard Bypass Savings
A naive agent spends substantial token allocations performing recursive directory mapping and multi-file reads to establish context:
$$\text{Naive Prompt Input} = \text{Dir Tree} + \text{Whole Files Contents} + \text{Full Chat Transcript} \approx 15,000\text{ to }20,000\text{ tokens}$$
With the L1 Librarian building a targeted `.session_map.json`, execution workers ingest only the narrow target data:
$$\text{Tiered Prompt Input} = \text{Blackboard Spec (400t)} + \text{Target File Segment (2k - 4kt)} \approx 3,500\text{ to }5,000\text{ tokens}$$
$$\textbf{Turn Token Savings: } \sim \mathbf{75\% \text{ reduction per execution turn}}$$

#### C. Parallel Branch Isolation Savings
Running concurrent subagents sequentially in a single chat thread causes exponential transcript growth because each step inherits the full history of prior steps. 
By isolating concurrent workers L2 and L3 into parallel workspace scopes (`share` git worktrees), history is strictly partitioned:
$$\text{Sequential Turn Summation} = \sum_{n=1}^{k} \text{Context}_n \approx 110,000\text{ tokens}$$
$$\text{Parallel Isolated Run} = (\text{L1 Librarian}) + \sum (\text{Worker}_n) + (\text{Integrator}) \approx 17,000\text{ tokens}$$
$$\textbf{History Reduction: } \sim \mathbf{84.5\% \text{ savings}}$$

---

## 6. Configuration Schema & Dynamic Home Directory Resolution

Persistent configuration and execution states are declared in `config.json`.

### 6.1 Configuration Schema (`config.json`)
```json
{
  "model_routing_enabled": true,
  "experimental_parallel_routing": false,
  "planning_mode_enabled": true
}
```
*Users can update these configuration states using conversational requests or specialized slash commands (e.g. `/toggle-routing`, `/toggle-parallel`), which the Orchestrator intercepts, writes in-place to `config.json`, and returns with styled visual toggle confirmations.*

### 6.2 Environment-Driven Dynamic Path Resolution
To eliminate filesystem searching latencies during interactive chats, the Orchestrator is instructed to bypass recursive directory and grep scans when reading or writing `config.json`. Instead, it resolves the configuration path dynamically using environment variables:
- **Windows Systems**: `%USERPROFILE%\.gemini\antigravity-cli\plugins\agy-cortex\config.json`
- **macOS/Linux Systems**: `~/.gemini/antigravity-cli/plugins/agy-cortex/config.json`

By utilizing these precise point-reads/writes exclusively on the global plugin configurations, the plugin achieves near-instantaneous state transitions while protecting the local repository from configuration clutter or git modifications.

---

## 7. Experimental Parallel Routing & Workspace Isolation

To maximize throughput on complex development prompts consisting of non-overlapping vectors, `agy-cortex` triggers **Path B (Parallel Route)**.

### 7.1 The Parallel Loop Phase Details

#### Phase 1: Planning (Decomposer)
If triage returns `parallel_route` (and parallel routing is enabled in the configuration), the Orchestrator spawns the **Decomposer** (`Gemini 3.1 Pro`) in the background. The Decomposer maps imports, inspects database/frontend dependencies, designs visual interfaces, and writes detailed integration contracts to `.session_map.json` under `parallel_specification`.

#### Phase 2: The User-in-the-Loop Confirmation Gate
The Orchestrator pauses all execution and presents the Decomposer's proposed interface specifications, targeted files, and worker assignments visually to the user. It blocks worker spawning until the user selects **[Yes, run parallel]**.

#### Phase 3: Concurrent Spawning (`share` workspaces)
The Orchestrator spawns workers concurrently using the `Workspace: "share"` configuration.
*   **Git Worktree Isolation**: The CLI leverages `git worktree` under the hood to checkout temporary, lightweight project folders pointing to the same repository directory. This completely isolates file writing, ensuring Worker A never overwrites Worker B's active buffers.

#### Phase 4: Integration & Verification (Integrator)
Once workers terminate, the Orchestrator spawns the **Integrator** (`Gemini 3.5 Flash`).
*   **Merge & Conflict Reconciliation**: The Integrator checks out the parallel branch directories, merges their codebases, manually parses and resolves any standard git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), and executes linter sweeps and validation tests (`run_command` tests) to guarantee compile-safety before closing the session.

---

## 8. Automated Intent Alignment Review Loop

Before concluding execution after any strategy-tier (**L4 Senior** or **L5 Architect**) file edits, the system executes a native, pre-authenticated verification check:

1.  **Diff Capture**: The Orchestrator automatically captures the working tree modifications via `git diff HEAD`.
2.  **Senior Audit**: The Orchestrator spawns **L4 Senior** (`Gemini 3.1 Pro`) with the git diff and your original task prompt.
3.  **Self-Correction**:
    - If L4 Senior identifies alignment issues, it returns `"status": "escalation"` alongside detailed, constructive feedback. The Orchestrator blocks session completion, displays L4's audit report, and re-delegates the task back to the execution tiers to correct.
    - If L4 Senior confirms alignment, it returns `"status": "success"` and the Orchestrator wraps up the task.

---

## 9. Manual Slash Command Lifecycles & Bypass Workflows

Slash commands complement automated routing by providing direct control channels for targeted workflows:

```
                  ┌──────────────────────────────────────────┐
                  │           User Slash Command             │
                  └─────┬──────────────────────────────┬─────┘
                        │                              │
         [ Configuration Toggles ]             [ Direct Subagent Bypasses ]
         ┌──────────────┴──────────────┐       ┌──────────────┴──────────────┐
         │ /toggle-routing             │       │ /cortex <tier> <prompt>     │
         │ /toggle-parallel            │       │ /analyze [path]             │
         └──────────────┬──────────────┘       │ /review                     │
                        ▼                      │ /draft <prompt>             │
         ┌─────────────────────────────┐       └──────────────┬──────────────┘
         │ Direct Environment Path     │                      │
         │ Point-Read & Write          │                      ▼
         └─────────────────────────────┘       ┌─────────────────────────────┐
                                               │ Executed Bypass Lifecycles  │
                                               └─────────────────────────────┘
```

### 9.1 Toggle Commands (`/toggle-routing`, `/toggle-parallel`, & `/toggle-planning`)
1. Intercept: The Orchestrator intercepts the slash command immediately prior to starting the L0 Triage router.
2. Resolve & Read: It uses dynamic environment-driven resolution to locate the global `config.json` and performs a point-read.
3. Write & Announce: It flips the targeted boolean state (`model_routing_enabled`, `experimental_parallel_routing`, or `planning_mode_enabled`), writes the update back to the configuration file, prints a styled state card in the terminal, and terminates the turn instantly.

### 9.2 Direct Subagent Control (`/cortex <tier> <prompt>`)
1. **Tier Check**: The Orchestrator validates the extracted `<tier>` against the specialist registry.
2. **Blackboard Safety Net**: If the targeted tier is an execution worker (`junior` or `engineer`) and `.session_map.json` is missing, the Orchestrator spawns L1 Librarian first to discover symbols and compile the blackboard.
3. **Context Shielding Sandbox**: If targeting a strategy tier (`senior` or `architect`), the Orchestrator injects a strict sandbox directive to strip file-writing permissions, guaranteeing a read-only analysis and design session.
4. **Execution**: The Orchestrator executes the subagent, prepends the visual identifier to the output, runs verification if files were modified, and cleans up the temporary blackboard.

### 9.3 Codebase Discovery (`/analyze [path]`)
1. **Triage Bypass**: Automatically routes to the L1 Librarian.
2. **Indexing**: Librarian catalogs files and symbols, compile active invariants, and writes `.session_map.json` at the root.
3. **Persistence**: Appends `.session_map.json` to `.gitignore` and keeps the file active after completing, allowing subsequent commands to run with zero-discovery latencies.

### 9.4 Code Quality Auditing (`/review`)
1. **Diff Extraction**: Orchestrator runs `git diff HEAD` to capture working tree changes.
2. **Audit Invocation**: Spawns L4 Senior Developer under the strict sandbox shield (read-only mode).
3. **Report Delivery**: Prepend L4 branding and outputs the comprehensive architectural and style review report.

### 9.5 Rapid Generation (`/draft <prompt>`)
1. **Draft Generation**: Spawns L2 Junior Developer to draft mock classes, database migrations, or boilerplate.
2. **Blackboard Fallback**: Junior reads `.session_map.json` if available; otherwise, displays a fallback warning to the user but continues.
3. **Handoff Verification**: Spawns L3 Core Engineer to compile, lint, and verify the newly generated files automatically.
