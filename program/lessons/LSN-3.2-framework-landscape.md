---
name: LSN-3.2-framework-landscape
description: Given a client ask, name the two candidate agent stacks (LangChain, LangGraph, Haystack, or no framework) and state the deciding tradeoff.
module: MOD-3
serves: OUT-3.2
duration: 1.5 h
prework_time: 40
owner: Guest co-teacher / TBD (Tyler fallback)
status: draft
---

# LSN-3.2 — Framework Landscape

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.2` |
| **Duration** | 1.5 h session + 40 min pre-work |
| **Format** | Live |
| **Verified by** | `ASM-3` — exam + mock client conversation (framework-choice scenarios) |

## Narrative

Kills two misconceptions: that "LangChain" is one thing (in 2026 it's a stack — LangChain 1.0's `create_agent` running on the LangGraph runtime, with LangSmith as the framework-agnostic observability/eval platform), and that framework choice is a religion rather than an engineering tradeoff. Participants watch one toy problem solved four ways — raw API, LangChain, LangGraph, Haystack — so the differences are visible in code, not slides. Callbacks: the agent loop anatomy from LSN-3.1 and the RAG plumbing pain from LSN-2.4. Setups: LSN-3.4's lab builds this same toy problem raw, so participants can judge firsthand what a framework would have bought them; LSN-3.3 extends the map to cloud-native stacks.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the four one-page framework cards (GAP-2 deliverable) | 20 | One sentence per framework — "what it is" in your own words |
| 2 | Skim each framework's own "what is this" page (links in Materials) | 15 | One "what is this actually?" question |
| 3 | Re-open your LSN-2.4 RAG homework; mark which code was plumbing vs logic | 5 | List of 2–3 plumbing pain points |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Why frameworks exist | 15 | talk | What you otherwise hand-roll: the loop, tool schemas, retries, state, tracing. Collect participants' LSN-2.4 plumbing pain points on the board — frameworks exist to absorb exactly that list. |
| The tour: one problem, four stacks | 45 | demo | **Toy problem (fixed, same as the LSN-3.4 lab):** "According to the project docs, what was Q2 infra spend, and what does that annualize to?" — agent must search a 10-document store, then call a calculator tool, then answer with a citation. Shown in: (1) raw API tool-use loop (~80 lines — where's the loop, where's state); (2) LangChain 1.0 `create_agent` (~15 lines — middleware for human-in-the-loop shown); (3) LangGraph (explicit graph + checkpointer — kill it mid-run, restart, it resumes); (4) Haystack 2.x pipeline with an Agent component (typed components, explicit connections). Checkpoint per stack: code size, where the loop lives, where state lives, what the trace looks like. |
| Choosing: the tradeoff table | 20 | discussion | Walk the table below axis by axis; for each axis, name the client situation where it dominates. |
| When *no* framework is right | 10 | drill | Criteria below; two rapid scenarios, room votes framework-or-not and defends. |

**Timing check:** 15 + 45 + 20 + 10 = 90 min = 1.5 h contract. ✓

### The tradeoff table (delivered as a handout; filled live)

| Axis | Raw API (no framework) | LangChain 1.0 | LangGraph 1.0 | Haystack 2.x |
|---|---|---|---|---|
| **Maturity** | As mature as the vendor SDK; everything above it is yours | 1.0 GA Oct 2025; huge integration surface; hazard: the web is littered with stale pre-1.0 tutorials | 1.0 GA Oct 2025; the runtime under LangChain agents; production-proven | 2.x since 2024 (near-total rewrite); stable, slower-moving, Apache-2.0 |
| **Lock-in** | Only the model vendor's SDK shape | Portable across model providers; gravitational pull toward LangSmith (commercial) | Graph/checkpointer APIs are ecosystem-specific; OSS core self-hostable; LangGraph Platform is commercial | OSS core; commercial pull is deepset's Haystack Enterprise Platform |
| **Observability hooks** | Whatever you log yourself | First-class LangSmith tracing (LangSmith itself is framework-agnostic: Python/TS/Go/Java SDKs) | Same LangSmith story + checkpoint history is inspectable | Component-level tracing; OpenTelemetry-based integrations |
| **State management** | Hand-rolled (a message list, if that) | Handled by the LangGraph runtime underneath; middleware for HITL, summarization | The differentiator: durable checkpointing, time-travel replay, survives restarts | Pipelines are the unit; cyclic graphs allow agent loops; state less central |
| **Team skill** | Needs your strongest engineers; nothing to google | Easiest ramp; most tutorials (many stale) | Steeper: think in graphs and state reducers; pays off on complex flows | Natural for teams already shipping RAG pipelines; Pythonic, typed |

### When no framework is right (criteria)

- Single model provider, ≤3 tools, one loop, no resume-after-crash requirement — a raw tool-use loop is under 100 lines and fully auditable.
- Hard latency or audit constraints where every abstraction layer must be defended line-by-line.
- Delivery window shorter than the team's framework learning curve — the framework becomes the risk.
- The harness requirements (permissions, approval gates) are so client-specific you'd fight the framework's opinions.
- The client's mandated cloud already covers the need natively (Bedrock AgentCore, Vertex Agent Engine, Foundry Agent Service) — bridge to LSN-3.3.

## Client Tie-In (Dorel's rule)

The in-production meeting-RAG system is the grounding case: segment 3 closes with a five-minute retro-fit — "if we rebuilt it today, which stack and why?" (defensible answers: Haystack, LangChain, or raw API — the argument matters more than the pick). The 6MAP translation gap frames the stakes: the pre-sales moment when a client architect asks "why LangGraph and not just Bedrock?" is exactly the conversation this lesson makes survivable.

## Homework

Match each of these five client scenarios to a stack (or "no framework") with one sentence naming the deciding axis from the tradeoff table. Submissions reference `LSN-3.2`. Grading: pick defensible + axis correctly identified; several scenarios have two defensible answers — the justification is what's graded.

1. A logistics client wants a support agent over ~40k shipping documents; their team ships Python daily and demands eval regression before every prompt change.
2. An insurance client needs multi-step claims triage with human approval before any payout action, state that survives process restarts, and audit-grade replay of every decision.
3. A startup prospect wants a working demo agent in two weeks: one model provider, three tools, no compliance constraints, demo dies after the pitch.
4. An enterprise client is all-in on AWS; security forbids third-party observability SaaS; agents must run inside their VPC with IAM-governed tool access.
5. A client's data team already runs Haystack RAG pipelines in production and wants to add one agentic search step without a platform migration.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Framework cards ×4 (LangChain, LangGraph, LangSmith+observability, Haystack) | build (`GAP-2`) | TBD — GAP-2 deliverable |
| Side-by-side demo: one toy problem, four implementations | build (`GAP-2`) | TBD — GAP-2 deliverable; shares tools with the LSN-3.4 lab notebook |
| "LangChain & LangGraph 1.0" announcement (LangChain blog) | exists | https://blog.langchain.com/langchain-langgraph-1dot0/ |
| LangGraph product/docs page | exists | https://www.langchain.com/langgraph |
| "What is Haystack?" (deepset) | exists | https://haystack.deepset.ai/overview/intro |
| LangSmith observability & evals docs | verify | LangChain — LangSmith documentation (verify at delivery prep) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery dependency: guest co-teacher unconfirmed (Tyler fallback per module spec). Landscape facts current as of 2026-07-28 — re-verify version claims at delivery prep; this space renames itself quarterly.
