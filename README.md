# AGY Cortex Plugin

A sophisticated, globally installable plugin for the Antigravity (AGY) CLI. AGY Cortex replaces a single "do-it-all" model with a specialized team of expert agents, automatically routing your prompts to the most appropriate tier to maximize reasoning depth while maintaining extreme context efficiency and operational transparency.

## The 5-Tier Architecture

The plugin uses a flat `agents/` directory structure containing distinct agent tiers, each optimized for specific responsibilities. Prompt routing is handled automatically based on the logic defined in the `rules/routing.md` file.

| Tier | Agent | LLM Model | Primary Responsibility |
| :--- | :--- | :--- | :--- |
| **L0** | **Router** | `Gemini 2.5 Flash Lite` | Prompt triage, clarification, and subagent routing. |
| **L1** | **Librarian** | `Gemini 2.5 Flash Lite` | Codebase exploration, search, and summarization. |
| **L2** | **Junior** | `Gemini 3.1 Flash` | Boilerplate, minor edits, and simple formatting. |
| **L3** | **Engineer** | `Gemini 3.5 Flash` | Feature implementation, bug fixes, and testing. |
| **L4** | **Senior** | `Gemini 3.1 Pro` | Deep debugging, complex refactoring, and peer review. |
| **L5** | **Architect** | `Gemini 3.5 Pro` | System design, architectural pivots, and strategy. |

---

## How It Operates

### 1. Automatic Prompt Routing
The plugin evaluates your prompts against the criteria defined in `rules/routing.md`. It automatically determines the required agent tier—from Librarian up to Architect—and seamlessly routes the task to ensure the most efficient problem resolution.

### 2. Context Shielding & Tool Proxying
To prevent session contexts from becoming bloated and slow, the architecture enforces **Context Shielding**:
- **Strategy Tiers (Senior/Architect)** focus on high-level planning and delegate execution.
- **Execution Tiers (Junior/Engineer)** handle the "heavy lifting" of direct file modifications and testing.
- **The Librarian** conducts broad repository searches and returns only concise, relevant summaries.

### 3. The Escalation Chain
The system is built for resilience and self-correction. If an execution agent (like Junior or Engineer) fails to resolve a task after multiple attempts (e.g., repeatedly failing tests or linters), they are mandated to abort and escalate. This escalation process passes the context and failure logs upward for a higher-tier strategic review.

### 4. Opt-In Shared Memory (`CONTEXT.md`)
AGY Cortex supports a powerful, opt-in shared memory tier via `CONTEXT.md`.
By placing a `CONTEXT.md` file at the root of any project, you can define global invariants, architectural decision records (ADRs), and preferred workflows. Every agent in the Cortex is mandated to read this file upon activation, guaranteeing that the entire team remains perfectly aligned with your project's specific guidelines.

---

## Installation & Usage

1. **Clone** the repository.
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

Once installed, the AGY Cortex architecture is active across your environments. Submit your tasks normally, and the intelligent routing will automatically engage the right expert for the job!
