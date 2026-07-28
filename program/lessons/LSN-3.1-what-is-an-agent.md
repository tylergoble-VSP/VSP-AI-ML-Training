---
name: LSN-3.1-what-is-an-agent
description: Define an agent precisely (LLM + goal + loop + tools + memory + stop condition), explain why production agents are mostly harness, and judge workflow-vs-agent on a real client ask.
module: MOD-3
serves: OUT-3.1
duration: 1.5
prework_time: 30
owner: Tyler
status: draft
---

# LSN-3.1 — What Is an Agent

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.1` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-3 (exam + conversation) |

## Narrative

"Agent" is the most abused word in the field, and this cohort will be selling against people who abuse it. This session kills the vagueness: an agent is an LLM with a goal, run in a loop, with tools, memory, and a stop condition — and in production, the thing you actually engineer is the **harness** around it (permissions, guardrails, human-in-the-loop). It connects backward to LSN-2.2 — structured output was the model *describing* an action; an agent is a harness *executing* it and feeding the result back — and forward to LSN-3.4, where everyone builds this exact loop by hand. The lasting capability: workflow-vs-agent as an engineering decision you can defend to a client, not a fashion choice.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read Anthropic's "Building Effective Agents" (see Materials) | 15 | One sentence: where does the piece draw the workflow/agent line? |
| 2 | Revisit your LSN-2.2 structured-output homework | 10 | The homework artifact, open and runnable |
| 3 | Think: what would it take to let the model *act* on its output? | 5 | One bullet listing what's missing (execution? feedback? permission?) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| From chatbot to agent | 25 | talk + whiteboard | Build the six-part definition live: **LLM + goal + loop + tools + memory + stop condition**. Start from a participant's LSN-2.2 artifact: the model already emits a structured action — what turns that into an agent? Execute it, append the result, ask again. Loop = repeated inference over a growing transcript; memory = that transcript; stop = "no tool call emitted" or a budget. Leans on notebook 06 sections "What are LLM Agents?" and "Key Concepts". |
| The harness | 25 | talk + discussion | Why production agents are **mostly harness**: the model is one component; the engineering is around it. Cover: tool allowlists and schema validation; permission gates on side-effecting tools (read freely, write with approval); max-turns and token budgets; audit logs of every tool call; human-in-the-loop escalation paths. Leans on notebook 06 "Safety Considerations". Discussion prompt: which of these does your current project already have for *ordinary* services? (Most — that's the point: harness thinking is delivery thinking.) |
| Workflow vs agent decision drill | 25 | drill | Five scenarios below — for each, the room picks **deterministic pipeline** or **agent** and defends it (~4 min each), then 5 min synthesis: *if you can draw the flowchart before you run it, build the flowchart; reach for an agent only when the next step depends on what the last step revealed.* Agents buy adaptability and cost predictability — the harness is how you buy the predictability back. |
| Anatomy of a real agent trace | 15 | demo walkthrough | Turn-by-turn read of the meeting-assistant trace below: user ask → tool call → tool result → next decision → permission gate → stop. Every turn is the same shape (context in, decision out). Closes with: "in LSN-3.4 you build this loop yourself." |

**Timing check:** 25 + 25 + 25 + 15 = **90 min** = 1.5 h contract duration. ✓

### The five-scenario decision drill

| # | Scenario | Right call | The tell |
|---|---|---|---|
| D1 | **Construction-site completion** (real VSP prospect — Dorel): client sends a photo/video of a site, wants "is it done?" | Deterministic workflow around a vision model (trained classifier, or multimodal-LLM checklist step) | One decision, fixed steps, no runtime tool choice. An *AI ask* is not automatically an *agent ask* — this is ML-pillar triage (LSN-1.1). |
| D2 | Nightly client-status report: pull metrics from three known APIs, LLM writes the summary, email it | Deterministic pipeline with one LLM step | Identical steps every run; failures need retries, not reasoning. |
| D3 | Meeting-knowledge assistant: "what did we commit to for client X, and is the follow-up scheduled?" — may need meeting search, calendar check, maybe drafting an invite | Agent | Step two depends on what step one returned; the tool sequence varies per request and can't be pre-drawn. |
| D4 | Invoice intake: extract fields from a known vendor set's PDFs into the ERP; flag mismatches for a human | Pipeline (OCR/LLM extraction step + validation rules + exception queue) | Known output schema, enumerable failure modes; in finance, determinism is a *feature*. |
| D5 | Incident triage assistant: "why did last night's deploy fail?" — read logs, query metrics, inspect diffs, decide where to look next | Agent (with a tight harness: read-only tools, turn budget) | The search space can't be enumerated in advance; each result changes the next question. |

### Trace anatomy — the walkthrough script

One real request through a meeting-assistant agent (the shape of VSP's in-production meeting-RAG system, agent-ified):

- **Turn 0 — user ask:** "What did we commit to in the Acme kickoff, and did we schedule the follow-up?" Harness prepends the system prompt: goal, tool schemas, max 6 turns.
- **Turn 1 — tool call:** Model decides it needs the meeting record → emits `search_meetings(query="Acme kickoff commitments")`. Harness validates the call against the schema, executes it, appends the **tool result**: three transcript chunks with dates and owners.
- **Turn 2 — next decision:** Model reads the chunks: two commitments found, one is "follow-up call in two weeks." It cannot answer the second half from memory → emits `calendar_search(attendees="Acme", range="next 30 days")`. Result: **no event found**.
- **Turn 3 — the gate:** Model proposes `create_event(...)`. The harness stops it: `create_event` is side-effecting and sits behind a permission gate → execution pauses, human is asked. Human declines ("just tell me"). The decline is appended as the tool result. *This turn is where production risk lives — point at it.*
- **Turn 4 — stop:** Model emits a final answer, no tool call: both commitments listed with sources, follow-up **not** scheduled, offer to draft the invite. No tool call = stop condition met; loop ends at turn 4 of a 6-turn budget.

What to point at: the loop is literally repeated inference; tool results are just appended text; "memory" is the transcript; the goal came from the user, the stop condition and gate came from the harness.

## Client Tie-In (Dorel's rule)

Drill scenario D1 is the real construction-site completion prospect Dorel raised in the July 28 meeting ("taking a picture or a video of a construction site and decide if it is done or not"). The teachable moment: the prospect sounds like an agent ask because it's an AI ask — the triage move is to recognize a single vision-classification decision and *not* sell a loop. The trace walkthrough is grounded in VSP's in-production meeting-RAG system, extended with tools. LSN-3.6 revisits both cases end to end.

## Homework

None — this session **is** pre-work for the LSN-3.4 lab. Keep your drill answers; D3 is roughly the agent you will build. Confirm your API key is provisioned (LSN-3.4 pre-work requirement).

## Materials

| Material | Status | Path / source |
|---|---|---|
| Concept sections: agent definition, architecture, safety | exists | `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` (markdown sections; note: module spec cites `06_Tool_Calling_Agents.ipynb` — same notebook, filename drift) |
| Pre-work reading | exists | Anthropic — "Building Effective Agents" (verify link at delivery prep) |
| Optional deeper read | exists | Lilian Weng — "LLM Powered Autonomous Agents" blog post (verify link at delivery prep) |
| Decision-drill scenario sheet | exists | This file, Session Plan section |
| Trace walkthrough script | exists | This file; optional live run from notebook 06 "Implementation" section |

## Delivery Notes

None yet — first delivery scheduled Week 3. Fill after delivery: what landed, what dragged, timing reality. Feeds the module retro.
