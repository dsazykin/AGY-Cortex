# Project Context & Shared Memory (CONTEXT.md)

## Current Focus
We are implementing core enhancements to the AGY Cortex orchestration plugin. The current milestone is implementing automated quality gates and verification tools to ensure design fidelity.

## Architectural Decision Records (ADRs)

### ADR-001: Automated Intent Alignment Stop Hook
* **Status**: Proposed (Pending L4 Senior Developer approval)
* **Date**: 2026-05-22
* **Context**: Strategy agents (L4 Senior Developer and L5 Lead Architect) formulate architectural designs and plans. Verification of implementation against original design intent is highly manual.
* **Decision**: We introduce an automated `Stop` hook (`intent-alignment-checker`) triggered when the orchestration loop concludes.
  1. The hook identifies if L4 or L5 was active in the conversation.
  2. If active, it collects the total changes made in the session via `git diff HEAD`.
  3. It extracts the original user prompt from `transcript.jsonl`.
  4. It sends both the original prompt and the git diff to a Gemini model to verify intent alignment.
  5. If alignment fails, it blocks the agent's termination and returns `"decision": "continue"`, driving a self-correcting learning loop where the agent is forced back to correct the implementation using the provided feedback.
* **Consequences**: Adds an automated, AI-driven quality gate to strategy execution sessions. Operates transparently and self-corrects without manual user intervention.
