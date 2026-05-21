# AGY Tiered Intel Extension

A sophisticated 5-tier agent architecture for the Antigravity (AGY) CLI, designed to maximize reasoning depth while maintaining extreme context efficiency and operational transparency.

## The 5-Tier Architecture

This extension replaces a single "do-it-all" model with a specialized team of experts, each pinned to the most efficient Gemini model for their specific role.

| Tier | Agent | Model | Primary Responsibility |
| :--- | :--- | :--- | :--- |
| **L0** | **Router** | `gemini-2.5-flash-lite` | Instant triage and task routing. |
| **L1** | **Librarian** | `gemini-2.5-flash-lite` | Codebase exploration, search, and summarization. |
| **L2** | **Junior** | `gemini-3.1-flash` | Boilerplate, minor edits, and simple formatting. |
| **L3** | **Engineer** | `gemini-3.5-flash` | Feature implementation, bug fixes, and testing. |
| **L4** | **Senior** | `gemini-3.1-pro` | Deep debugging, complex refactoring, and peer review. |
| **L5** | **Architect** | `gemini-3.5-pro` | System design, architectural pivots, and strategy. |

---

## How It Operates

### 1. The Triage Flow (L0)
Every new topic begins with the **Router**. It analyzes your prompt and determines the minimum required tier to solve the problem. If you ask a question about the code, it goes to the **Librarian**. If you ask for a feature, it might start with the **Architect**.

### 2. Context Shielding & Tool Proxying
To prevent the "Manager" session from becoming bloated and slow, the extension enforces **Context Shielding**:
- **Strategy Tiers (L4/L5)** are prohibited from writing code directly. They must use `invoke_agent` to delegate to **L2/L3**.
- **Execution Tiers (L2/L3)** handle the "heavy lifting" of file edits and testing.
- **The Librarian (L1)** handles broad searches and returns only concise summaries to the higher tiers.

### 3. The Escalation Chain
The system is designed for self-correction. If a **Junior (L2)** or **Engineer (L3)** fails to resolve a task after 3 attempts (e.g., failing tests or linters), they are mandated to call `submit_result` with an **"escalation"** status. This passes the full context and failure log up to the **Senior (L4)** for a strategic review.

### 4. Full Transparency
With the `stream_internal_dialogue` setting enabled, the internal "thought process" and tool calls of every subagent are streamed directly to your terminal. You can watch the Librarian search the files, the Architect plan the strategy, and the Engineer run the tests in real-time.

---

## 🚀 Installation & Usage

1. **Clone** the repository.
2. **Import to AGY CLI**:
   ```bash
   agy plugin import ./agy-tiered-intel
   ```
3. **Update (if changes are made)**:
   ```bash
   agy plugin import ./agy-tiered-intel --force
   ```
4. **Verify**:
   ```bash
   agy plugin list
   ```


The architecture is now active. You can now use `@router` or any other tier in your `agy` sessions.
