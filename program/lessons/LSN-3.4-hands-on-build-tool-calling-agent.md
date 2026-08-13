---
name: LSN-3.4-hands-on-build-tool-calling-agent
description: Personally build a tool-calling agent — LLM + two tools + loop + stop condition — instrument its traces, break it, and add a max-turns guardrail plus a permission gate.
module: MOD-3
delivery_date: 2026-12-03
serves: OUT-3.3
duration: 1
prework_time: 30
homework_time: 90
owner: Tyler
status: draft
---

# LSN-3.4 — Hands-On: Build a Tool-Calling Agent

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.3` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Three-stage lab — Stage A solo (pre-work) · live hour · Stages B–C solo (homework) |
| **Verified by** | `ASM-3` (artifact — working agent notebook + traces reviewed at the basics final) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Thursday, 3 December 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

**Restructure note (the module's largest):** this was a 2.5 h live lab; the spreadsheet gives it 1 h. Nothing is cut — the lab is now **three staged sections of one notebook**. **Stage A** (pre-work, 30 min): skeleton loop + stub tool round-trips, so nobody spends the live hour on `sys.path`. **Live hour:** unblocking, wiring the two real tools until *everyone's agent makes its first successful real tool call*, reading the trace, and the break-it failure-classification drill. **Stages B–C** (homework, 75 of the 90 min): guardrails (max-turns + permission gate) and the graded third-tool-plus-eval artifact. The solo stages carry explicit self-checkable checkpoints because no instructor is in the room for them.

## Narrative

This session kills the "agents are magic autonomy" misconception by having everyone build one from parts: an LLM, two tool schemas, a while-loop, and a stop condition — and discover that most of what makes it trustworthy is harness, not model. It calls back hard: the tool call is just the LSN-2.2 structured output *acted on*; one of the two tools wraps each participant's own LSN-2.4 RAG pipeline; the anatomy walked in LSN-3.1 is now code they wrote. The instrumentation is the point — the trace log built here is what LSN-3.5's production questions get asked against, and the closing raw-build-vs-framework comparison is the bridge back to LSN-3.2/3.3.

## Pre-work — Stage A (mandatory — no Stage A, no seat)

Stage A is the part of the old live lab that was pure setup and skeleton-reading. It runs solo on the Wednesday evening, and every task has a **checkpoint cell that prints pass/fail** so you know you are ready without asking.

| # | Task | Time | Checkpoint / artifact to bring |
|---|---|---|---|
| A1 | Run the lab's Stage-A cells: the `agent_loop()` skeleton with the stub `echo` tool, until **one tool call round-trips** (call emitted → executed → result appended → model sees it) | 15 | Checkpoint cell prints PASS; the stub trace saved |
| A2 | Confirm your LSN-2.4 retrieval returns chunks for one query; **if it doesn't, load the fallback mini-corpus index** — do this now, not tomorrow | 10 | One retrieved-chunk output (own corpus or fallback) |
| A3 | Skim the lab's §"Safety Considerations" cell and answer in one sentence: "what stops your agent?" | 5 | The sentence, written |

**Pre-work total: 30 min.** **Carried in, not re-charged:** API key provisioning and the repo-root/env smoke test were **LSN-3.1 homework task 2** (10 min, budgeted there) — deliberately front-loaded off this evening, which is the module's second-heaviest. LSN-3.3's homework is also deliberately weekend-due so Wednesday evening has room for Stage A.

## Session Plan

The live hour buys the two things that only work with the room together: **unblocking** and **everyone's agent making its first successful real tool call**. Everything solo-doable is in Stage A or Stages B–C.

| Segment | Time | Method | Detail |
|---|---|---|---|
| Unblock & sync | 10 | lab triage | **Where:** Stage-A checkpoint cells. Hands up for anyone whose A1/A2 checkpoint didn't print PASS; those people get the fallback mini-corpus index and a working neighbor immediately. Then 3 min on screen: `agent_loop()` in `src/llm/tool_calling.py` — the `messages` list, `while iteration < max_iterations`, `parse_tool_call()` → `execute_tool_call()` → result appended back — so the whole room is pointing at the same three lines. **Lab checkpoint:** every participant's stub round-trips one tool call before segment 2 starts. **Likely failure:** `src/` imports fail (repo root not on `sys.path`) or API key not picked up — both should have been caught in Stage A and LSN-3.1 homework; if not, rerun cell 0 and pair the straggler while the instructor fixes offline. |
| Wire the two real tools — **first successful real tool call** | 25 | lab | **Where:** §"Implementation" (extended). The canonical pair: **(a)** `search_docs(query)` — wraps the participant's own LSN-2.4 RAG retrieval, returns top-3 chunks with source ids; **(b)** `calculator(expression)` — safe arithmetic eval, no `eval()` on raw strings. Sketch the real schema together once: `{"name": "search_docs", "description": "Search the meeting-notes corpus; returns the 3 most relevant chunks", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}`. Then straight to the **combined task** — "total the effort estimates in the notes and add a 20% buffer" — which needs both tools; the retrieval-only and calc-only warm-ups move to Stage B. **This segment is the lesson's non-negotiable:** nobody leaves without a real tool call in their own trace. **Lab checkpoint:** everyone's agent completes the combined task with ≥1 `search_docs` and ≥1 `calculator` call visible in the trace log. **Likely failure:** schema mismatch — malformed arguments or a hallucinated tool name; second most likely: RAG index path wrong. **Recovery:** the validate-args wrapper that returns the validation error *to the model as the tool result* (the loop self-corrects — teachable moment, 60 seconds); fallback pre-built index for anyone whose LSN-2.4 index won't load. |
| Read the trace together | 8 | demo | The per-turn log on one volunteer's screen: model text, tool chosen, arguments, result, token counts. One question asked out loud: "where in this log would you look first if the answer were wrong?" This is the hand-off to LSN-3.5 — those traces are tomorrow's material. |
| Break it: a task the tools can't do | 12 | drill | **Where:** §"Validation & Testing" (extended into a failure drill). Ask: "What is the current EUR/USD exchange rate?" then "Email this summary to the team." Watch and classify: hallucinated tool call, loop-until-max-iterations, or a confident answer with no tool call at all. Each participant writes one sentence naming the failure mode their trace shows. **Lab checkpoint:** everyone has a captured failure trace + the mode named — checkpoint question: "at which turn could a human have caught this, and what in the trace tells you?" **Likely failure (meta):** the agent politely refuses and nothing dramatic happens. **Recovery:** the instructor's rigged prompt variant (system prompt that over-encourages tool use) that reliably induces the loop-out, kept ready — at 12 min, deploy it early rather than waiting for a natural failure. |
| Wrap + Stage B/C brief | 5 | talk | **Where:** §"Summary & Key Takeaways". Two minutes mapping the hand-rolled parts to what a framework or cloud gives you — loop → LangGraph's state graph; trace log → LangSmith; permission gate + max-turns → Bedrock Agents guardrails; tool schemas → the same JSON everywhere — with the full mapping already in participants' hands as **LSN-3.3 homework task 3**. Three minutes briefing Stages B and C and their due points. Exit question taken as written homework, not live: "which of the five things you built would you not hand-roll in production, and what would you use instead?" |

**Timing check:** 10 + 25 + 8 + 12 + 5 = 60 min = 1 h — matches the spreadsheet contract.

**What moved out of the live hour (relocated, not cut):** skeleton reading and the stub round-trip → **Stage A pre-work** · retrieval-only and calc-only warm-up tasks → **Stage B** · the whole guardrail segment, max-turns stop reason and permission gate → **Stage B** (homework task 1, with the same checkpoint questions) · the raw-vs-framework mapping discussion → **LSN-3.3 homework task 3** plus the 2-min live summary · the exit question → written, in Stage C.

## Client Tie-In (Dorel's rule)

The `search_docs` tool *is* VSP's in-production meeting-RAG system, promoted from pipeline to agent tool — participants are rebuilding the proof point Vlad cites, then instrumenting it the way production demanded. The trace log is the 6MAP lesson in miniature: the translation gap closes when a TL can answer "what did the agent actually do, turn by turn, and what did it cost?" from their own logs instead of deferring to the AI engineers. LSN-3.5 asks exactly those questions against the traces built here; LSN-3.6 walks the meeting-RAG case end to end with this lab as shared ground truth.

## Homework — Stages B and C

Thursday evening is the module's heaviest: it carries this homework **and** the pre-work for both Friday sessions (the double-header). Tasks 1, 3 and 4 total 50 min and are the only Thursday-night obligation; Stage C floats to the weekend.

| # | Task | Time | Due | Checkpoint / artifact |
|---|---|---|---|---|
| 1 | **Stage B — guardrails.** Run the retrieval-only and calc-only warm-ups you skipped live, then: tighten `max_iterations` 5 → 3 and surface an **explicit stop reason** ("gave up after 3 turns: …") instead of a silent trailing answer; add one **permission gate** — `calculator` auto-runs, `search_docs` (and a mock `send_email` if you add one) needs y/n confirmation *before* execution. Re-run the break-it task. **Doubles as LSN-3.5 pre-work** — this guardrailed agent and its traces are the material for tomorrow's observability demo. Checkpoint questions to answer in writing: "which tools in a client system would you gate, and on what rule?" and the LSN-3.4 exit question ("which of the five things you built would you not hand-roll in production?") | 35 | Fri 4 Dec, session start | Re-run trace showing the gate firing + the loop terminating with an explicit stop reason. **Known traps:** gate placed *after* the tool executes; `input()` hanging the kernel — paste the reference `gated_execute()` cell, or swap `input()` for an `ALLOW_TOOLS` flag |
| 2 | **Stage C — graded artifact** (references `LSN-3.4`; reviewed at `ASM-3`). Add a third tool (`get_date()`, a unit converter, or a second-corpus `search_docs`) and one eval check — three test tasks with known-good answers, asserting the agent's final answer matches each. Submit the notebook + traces for all three eval runs. **Grading standard:** 3/3 eval tasks pass (or you document precisely why one fails and what in the trace shows it); traces included; max-turns and the permission gate still enforced with the third tool present | 40 | Sun 6 Dec | Notebook + three eval traces |
| 3 | Write the **two questions about your own agent's behaviour you cannot answer from its logs**. **Doubles as LSN-3.5 pre-work** — these get sorted live into observability gaps vs design gaps | 5 | Fri 4 Dec | The two questions, written |
| 4 | Skim the **three LSN-3.6 case briefs** (`GAP-5`) and write one triage question per case. **Doubles as LSN-3.6 pre-work** — folded here so the second Friday session needs almost no evening of its own | 10 | Fri 4 Dec | Three triage questions |

**Time accounting:** pre-work 30 min + homework 90 min = 2 h out-of-session budget.

**Cadence note:** three of the four Friday-morning inputs for *both* Friday sessions are paid for out of this lesson's budget — Stage B (LSN-3.5's agent + traces), task 3 (LSN-3.5's unanswerable questions), task 4 (LSN-3.6's case reading). That is what keeps the double-header's own pre-work down to 20 + 15 min.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Guided agent lab notebook — extended with trace-logging, break-it, and guardrail sections; hosted-API path added alongside the existing local-model path (fold into GAP-2 build) | adapt (**GAP-2b**) | `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` |
| **New build requirement from the 2.5 h → 1 h restructure: the notebook must be runnable solo in three staged sections** — Stage A (pre-work), Live, Stages B–C (homework) — each ending in a **self-checkable checkpoint cell that prints PASS/FAIL**, because the guardrail and third-tool work is no longer instructor-supervised. Stage A additionally needs an **unattended-failure path**: the fallback mini-corpus + pre-built index must be loadable from a single cell with no help | build (`GAP-2b`) | Needed **Wed 2 Dec** — Stage A is pre-work, one day earlier than the session |
| Agent-loop helpers — `define_tool_schema()`, `execute_tool_call()`, `agent_loop(max_iterations=5)`, `parse_tool_call()` | exists | `src/llm/tool_calling.py` |
| Each participant's RAG artifact (becomes the `search_docs` tool) | exists after LSN-2.4 | participant-owned, from `LSN-2.4` homework |
| Fallback mini-corpus + pre-built index (for broken LSN-2.4 artifacts) | build (part of `GAP-2b`) | repo — location set at delivery prep. **Now load-bearing at pre-work time:** Stage A2 tells participants to switch to it Wednesday evening rather than discovering the problem in the live hour |
| Pre-work reading: Anthropic, "Building effective agents" | exists | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Rigged system-prompt variant for the break-it drill + reference `gated_execute()` cell | build (part of GAP-2) | lab notebook appendix |
| Supplement — anatomy of a tool and the three-way failure partition (selection / arguments / execution) as the break-it drill and Stage-C rubric | supplement | [`program/sources/SUP-6-agentic-patterns-and-limits.md`](../sources/SUP-6-agentic-patterns-and-limits.md) §3 |

## Delivery Notes

To be filled after each delivery: what landed, what dragged, timing reality. **The single biggest risk in MOD-3:** the 25-min wiring segment hinges on how many participants arrive with Stage A actually passing. Count Stage-A PASS rates before the session (checkpoint output is submittable) — if it drops below ~80%, the live hour becomes a debugging clinic and nobody makes a real tool call. The fallback index is the pressure valve; count how many needed it and feed that to the LSN-2.4 owner. Also record: how many completed Stage B by Friday morning, since LSN-3.5's observability demo has no material without it. Feeds the MOD-3 retro; retro findings that change scope update `program/modules/module-3-agentic-systems.md` first.
