# Tiered Intel Orchestration Rules

This extension implements a 5-tier intelligence hierarchy. The goal is to maximize reasoning quality while minimizing token usage and context bloat.

## The Escalation Chain

- **L0: Router** (Triage) -> Invoked on the first prompt of a new topic.
- **L1: Librarian** (Discovery) -> Handles search, indexing, and summaries.
- **L2: Junior** (Simple Execution) -> Handles boilerplate and minor fixes.
- **L3: Engineer** (Primary Execution) -> Handles core features and testing.
- **L4: Senior** (Strategy/Review) -> Handles deep debugging and escalation review.
- **L5: Architect** (Design/Pivot) -> Handles high-level strategy and system design.

## Tool Proxying & Context Shielding

- **L4/L5** are restricted from editing files directly. They must delegate implementation to **L2/L3**, providing exact file paths, line ranges, and invariant variable/type names.
- **L4/L5** should prefer summaries from **L1** for broad context, but may use `read_file` for critical technical nuance.
- **L2/L3** must read files before editing to ensure precision.
- **L3** uses scoped tools for tests/linting to prevent architectural bypass.

## Protocols

### Context Payload Protocol
When invoking a subagent via `invoke_agent`, provide a specific prompt with:
1. The immediate goal.
2. **Precise File Context:** Exact file paths, line ranges, and invariant variable/type/signature names to prevent "Telephone Game" context loss.
3. A concise summary of relevant context.
Do NOT pass the entire session history.

### Return & Escalation Protocol (via `submit_result`)
All subagents (L1-L3) must conclude their task by calling `submit_result`.
- **Status: "success"** -> Task completed. Include `files_modified`, `tests_run`, and a `message` summary.
- **Status: "escalation"** -> Task failed or too complex. Include a detailed `message` explaining the roadblock for the higher tier.
- **Threshold**: L2/L3 must escalate after 3 consecutive failures.
- **Hard Global Loop Limit:** A single task block may only bounce between Strategy (L4/L5) and Execution (L2/L3) twice. If a second escalation occurs, Strategy must abort, compile a detailed blocker summary, and surface it directly to the human user to avoid infinite loops.

### Transparency Protocol
All subagents must articulate their reasoning step-by-step. With `stream_internal_dialogue` enabled, this reasoning is streamed to the user's terminal. Tool execution outputs must be visually collapsed in the CLI UI to avoid terminal noise.
