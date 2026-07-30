---
name: LSN-3.4-hands-on-build-tool-calling-agent
description: Personally build a tool-calling agent — LLM + two tools + loop + stop condition — instrument its traces, break it, and add a max-turns guardrail plus a permission gate.
module: MOD-3
serves: OUT-3.3
duration: 2.5
prework_time: 45
owner: Tyler
status: draft
---

# LSN-3.4 — Hands-On: Build a Tool-Calling Agent

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.3` |
| **Duration** | 2.5 h session + 45 min pre-work |
| **Format** | Live lab |
| **Verified by** | `ASM-3` (artifact — working agent notebook + traces reviewed at the basics final) |

## Narrative

This session kills the "agents are magic autonomy" misconception by having everyone build one from parts: an LLM, two tool schemas, a while-loop, and a stop condition — and discover that most of what makes it trustworthy is harness, not model. It calls back hard: the tool call is just the LSN-2.2 structured output *acted on*; one of the two tools wraps each participant's own LSN-2.4 RAG pipeline; the anatomy walked in LSN-3.1 is now code they wrote. The instrumentation is the point — the trace log built here is what LSN-3.5's production questions get asked against, and the closing raw-build-vs-framework comparison is the bridge back to LSN-3.2/3.3.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Confirm your LSN-2.4 RAG artifact still runs end to end: execute one retrieval query against your corpus and keep the output | 20 | Your RAG notebook + one retrieved-chunk output |
| 2 | Read the guided agent lab intro cells (§"What are LLM Agents?", §"Theory & Mechanics" — What is Tool Calling / Agent Architecture / Safety Considerations) | 15 | One-sentence written answer to: "what stops your agent?" |
| 3 | API key provisioned per the lab's setup cell; run the smoke test until it returns a completion | 10 | Screenshot of the successful smoke-test output |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Skeleton: loop, tool schema, stop condition | 30 | talk + lab | **Where:** lab notebook §"Theory & Mechanics" → §"Implementation" skeleton (from `06_GenerativeAI_Tool_Calling_Agents.ipynb`), reading `agent_loop()` in `src/llm/tool_calling.py` on screen: the `messages` list, `while iteration < max_iterations`, `parse_tool_call()` → `execute_tool_call()` → result appended back. Sketch a real schema together: `{"name": "search_docs", "description": "Search the meeting-notes corpus; returns the 3 most relevant chunks", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}`. Run the skeleton with a stub `echo` tool. **Lab checkpoint:** everyone can point at the loop, the schema, and the stop condition in their own notebook, and the stub round-trips one tool call. **Likely failure:** environment — `src/` imports fail (repo root not on `sys.path`) or API key not picked up. **Recovery:** rerun cell 0 (`ensure_repo_root_on_sys_path()` + key smoke test); `.env` template on the shared drive; stragglers pair with a working neighbor while the instructor fixes offline. |
| Guided build: wire two tools, run the loop, read the traces | 60 | lab | **Where:** §"Implementation" (extended). The canonical pair: **(a)** `search_docs(query)` — wraps the participant's own LSN-2.4 RAG retrieval, returns top-3 chunks with source ids; **(b)** `calculator(expression)` — safe arithmetic eval, no `eval()` on raw strings. Three graded tasks, run in order: retrieval-only ("what did the meeting decide about the rollout?"), calc-only ("what is 12.5% of 1,840?"), combined ("total the effort estimates in the notes and add a 20% buffer"). Then read the traces: the per-turn log — model text, tool chosen, arguments, result, token counts. **Lab checkpoint:** everyone's agent completes the combined task with ≥1 `search_docs` and ≥1 `calculator` call visible in the trace log. **Likely failure:** schema mismatch — malformed arguments or a hallucinated tool name from the model; second most likely: RAG index path wrong on the participant's machine. **Recovery:** the validate-args wrapper that returns the validation error *to the model as the tool result* (the loop self-corrects — teachable moment); repo fallback mini-corpus with a pre-built index for anyone whose LSN-2.4 index won't load. |
| Break it: a task the tools can't do | 25 | drill | **Where:** §"Validation & Testing" (extended into a failure drill). Ask: "What is the current EUR/USD exchange rate?" then "Email this summary to the team." Watch and classify: hallucinated tool call, loop-until-max-iterations, or a confident answer with no tool call at all. Each participant writes one sentence naming the failure mode their trace shows. **Lab checkpoint:** everyone has a captured failure trace + the mode named — checkpoint question: "at which turn could a human have caught this, and what in the trace tells you?" **Likely failure (meta):** the agent politely refuses and nothing dramatic happens. **Recovery:** the instructor's rigged prompt variant (system prompt that over-encourages tool use) that reliably induces the loop-out, kept ready. |
| Guardrail: max-turns + one permission gate | 20 | lab | **Where:** §"Safety Considerations" (extended into code). Tighten `max_iterations` from 5 to 3 and surface an explicit stop reason ("gave up after 3 turns: …") instead of a silent trailing answer; add one permission gate — `calculator` auto-runs, `search_docs` (and the mock `send_email` if added) requires a y/n confirmation before execution. Re-run the break-it task. **Lab checkpoint:** the re-run shows the gate firing and the loop terminating with an explicit stop reason — checkpoint question: "which tools in a client system would you gate, and on what rule?" **Likely failure:** gate placed *after* the tool executes, or `input()` hanging the notebook kernel. **Recovery:** reference `gated_execute()` cell to paste; swap `input()` for an `ALLOW_TOOLS` boolean flag if the kernel misbehaves. |
| Wrap: raw build vs LangGraph / Bedrock | 15 | talk + discussion | **Where:** §"Summary & Key Takeaways". Map each hand-rolled part to what a framework or cloud gives you: the loop → LangGraph's state graph; the trace log → LangSmith; the permission gate + max-turns → Bedrock Agents guardrails; the tool schemas → the same JSON everywhere. Bridge to LSN-3.2/3.3: "you now know what the frameworks are *for*, because you built the naive version." **Lab checkpoint:** exit question, one per person — "which of the five things you built today would you not hand-roll in production, and what would you use instead?" |

**Timing check:** 30 + 60 + 25 + 20 + 15 = 150 min = 2.5 h — matches the contract duration.

## Client Tie-In (Dorel's rule)

The `search_docs` tool *is* VSP's in-production meeting-RAG system, promoted from pipeline to agent tool — participants are rebuilding the proof point Vlad cites, then instrumenting it the way production demanded. The trace log is the 6MAP lesson in miniature: the translation gap closes when a TL can answer "what did the agent actually do, turn by turn, and what did it cost?" from their own logs instead of deferring to the AI engineers. LSN-3.5 asks exactly those questions against the traces built here; LSN-3.6 walks the meeting-RAG case end to end with this lab as shared ground truth.

## Homework

**Artifact (graded, references LSN-3.4; reviewed at ASM-3):** Add a third tool (suggested: `get_date()`, a unit converter, or a second-corpus `search_docs`) and one eval check — three test tasks with known-good answers, asserting the agent's final answer matches each. Submit the notebook + the traces for all three eval runs. **Grading standard:** agent passes 3/3 eval tasks (or documents precisely why one fails and what in the trace shows it); traces included; max-turns and the permission gate still enforced with the third tool present.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Guided agent lab notebook — extended with trace-logging, break-it, and guardrail sections; hosted-API path added alongside the existing local-model path (fold into GAP-2 build) | adapt (**GAP-2** share) | `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` |
| Agent-loop helpers — `define_tool_schema()`, `execute_tool_call()`, `agent_loop(max_iterations=5)`, `parse_tool_call()` | exists | `src/llm/tool_calling.py` |
| Each participant's RAG artifact (becomes the `search_docs` tool) | exists after LSN-2.4 | participant-owned, from `LSN-2.4` homework |
| Fallback mini-corpus + pre-built index (for broken LSN-2.4 artifacts) | build (part of GAP-2) | repo — location set at delivery prep |
| Pre-work reading: Anthropic, "Building effective agents" | exists | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Rigged system-prompt variant for the break-it drill + reference `gated_execute()` cell | build (part of GAP-2) | lab notebook appendix |

## Delivery Notes

To be filled after each delivery: what landed, what dragged, timing reality (the 60-min wiring segment hinges on how many LSN-2.4 artifacts arrive broken — the fallback index is the pressure valve; count how many needed it and feed that to the LSN-2.4 owner). Feeds the MOD-3 retro; retro findings that change scope update `program/modules/module-3-agentic-systems.md` first.
