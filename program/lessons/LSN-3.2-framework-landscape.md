---
name: LSN-3.2-framework-landscape
description: Given a client ask, name the two candidate agent stacks (LangChain, LangGraph, Haystack, or no framework) and state the deciding tradeoff.
module: MOD-3
delivery_date: 2026-12-01
serves: OUT-3.2
duration: 1
prework_time: 20
homework_time: 100
owner: Tyler
status: draft
---

# LSN-3.2 — Framework Landscape

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.2` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | `ASM-3` — exam + mock client conversation (framework-choice scenarios) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Tuesday, 1 December 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

**Preserved recruiting note:** a guest co-teacher (framework practitioner) was the original owner of this lesson. The spreadsheet assigns Tyler, who is now the responsible presenter — the guest ask stays open as an upgrade to the side-by-side tour, not a dependency.

## Narrative

Kills two misconceptions: that "LangChain" is one thing (in 2026 it's a stack — LangChain 1.0's `create_agent` running on the LangGraph runtime, with LangSmith as the framework-agnostic observability/eval platform), and that framework choice is a religion rather than an engineering tradeoff. Participants watch one toy problem solved four ways — raw API, LangChain, LangGraph, Haystack — so the differences are visible in code, not slides. Callbacks: the agent loop anatomy from LSN-3.1 and the RAG plumbing pain from LSN-2.4. Setups: LSN-3.4's lab builds this same toy problem raw, so participants can judge firsthand what a framework would have bought them; LSN-3.3 extends the map to cloud-native stacks.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Skim the "what is this" page of the **two frameworks your LSN-3.1 homework left least clear** (links in Materials) | 12 | Your one "what is this actually?" question, sharpened |
| 2 | Re-open your LSN-2.4 RAG homework; mark which code was plumbing vs logic | 8 | List of 2–3 plumbing pain points |

**Pre-work total: 20 min.** Deliberately thin — Monday evening also carries LSN-3.1's homework. **Carried in, not re-charged:** the four GAP-2 framework cards and your one-sentence-per-framework summaries were **LSN-3.1 homework task 1** (30 min, budgeted there). Bring them; you are not reading them twice.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Why frameworks exist | 8 | talk | What you otherwise hand-roll: the loop, tool schemas, retries, state, tracing. Collect participants' LSN-2.4 plumbing pain points on the board — frameworks exist to absorb exactly that list. |
| The tour: one problem, **the two poles** | 27 | demo | **Toy problem (fixed, same as the LSN-3.4 lab):** "According to the project docs, what was Q2 infra spend, and what does that annualize to?" — agent must search a 10-document store, then call a calculator tool, then answer with a citation. Live: **(1) raw API tool-use loop** (~80 lines — where's the loop, where's state) and **(4) LangGraph** (explicit graph + checkpointer — kill it mid-run, restart, it resumes). The two poles make the axis visible; **LangChain 1.0 `create_agent` and Haystack 2.x move to homework task 4** as annotated self-study, with their headline numbers quoted live (~15 lines for `create_agent`; typed components + explicit connections for Haystack). Checkpoint per stack: code size, where the loop lives, where state lives, what the trace looks like. |
| Choosing: the tradeoff table | 15 | discussion | Walk the table below axis by axis; for each axis, name the client situation where it dominates. All four columns are walked — the table is the artifact that covers the two stacks not demoed live. |
| When *no* framework is right | 10 | drill | Criteria below; two rapid scenarios, room votes framework-or-not and defends. |

**Timing check:** 8 + 27 + 15 + 10 = 60 min = 1 h — matches the spreadsheet contract.

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

The in-production meeting-RAG system is the grounding case: segment 3 closes by *posing* the retro-fit — "if we rebuilt it today, which stack and why?" — in one minute, and the answer is written up as **homework task 3** (defensible answers: Haystack, LangChain, or raw API — the argument matters more than the pick). At 15 min the segment can no longer host the five-minute discussion, so the thinking moves out of the room and comes back graded. The 6MAP translation gap frames the stakes: the pre-sales moment when a client architect asks "why LangGraph and not just Bedrock?" is exactly the conversation this lesson makes survivable.

## Homework

| # | Task | Time | Due | Artifact |
|---|---|---|---|---|
| 1 | **Doubles as LSN-3.3 pre-work.** Skim your assigned cloud's AI landing page (assignment by Marius) and write one "what is this actually?" question about a product name on it | 25 | Wed 2 Dec, session start | The written question |
| 2 | The five-scenario stack match below — one sentence per scenario naming the deciding axis | 35 | Sun 6 Dec | Five matches + justifications |
| 3 | Meeting-RAG retro-fit memo (~200 words): if we rebuilt it today, which stack, and which axis of the tradeoff table decided it? | 20 | Sun 6 Dec | Memo |
| 4 | Self-study the **two implementations cut from the live tour** — LangChain 1.0 `create_agent` and Haystack 2.x — in the GAP-2 demo notebook. For each, write where the loop lives, where state lives, and what the trace looks like | 20 | Sun 6 Dec | Six one-liners (3 per stack) |

**Time accounting:** pre-work 20 min + homework 100 min = 2 h out-of-session budget.

**Cadence note:** task 1 (25 min) is the only Tuesday-evening obligation — and it is LSN-3.3's pre-work, budgeted here and not charged again there. Tasks 2–4 float to the weekend of 5–6 Dec.

**Task 2 — the five scenarios.** Match each to a stack (or "no framework") with one sentence naming the deciding axis from the tradeoff table. Submissions reference `LSN-3.2`. Grading: pick defensible + axis correctly identified; several scenarios have two defensible answers — the justification is what's graded.

1. A logistics client wants a support agent over ~40k shipping documents; their team ships Python daily and demands eval regression before every prompt change.
2. An insurance client needs multi-step claims triage with human approval before any payout action, state that survives process restarts, and audit-grade replay of every decision.
3. A startup prospect wants a working demo agent in two weeks: one model provider, three tools, no compliance constraints, demo dies after the pitch.
4. An enterprise client is all-in on AWS; security forbids third-party observability SaaS; agents must run inside their VPC with IAM-governed tool access.
5. A client's data team already runs Haystack RAG pipelines in production and wants to add one agentic search step without a platform migration.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Framework cards ×4 (LangChain, LangGraph, LangSmith+observability, Haystack) | build (`GAP-2`) | TBD — GAP-2 deliverable. **Deadline pulled forward to Mon 30 Nov:** the cards are now read as LSN-3.1 homework, not as this lesson's pre-work |
| Side-by-side demo: one toy problem, four implementations | build (`GAP-2`) | TBD — GAP-2 deliverable; shares tools with the LSN-3.4 lab notebook. **New requirement from the restructure:** the LangChain and Haystack implementations are now *homework self-study*, so they need annotated commentary cells (where the loop lives / where state lives / what the trace looks like) that a participant can follow with no instructor present. The raw-API and LangGraph implementations remain the live demo |
| "LangChain & LangGraph 1.0" announcement (LangChain blog) | exists | [langchain.com/blog/langchain-langgraph-1dot0](https://www.langchain.com/blog/langchain-langgraph-1dot0) |
| LangGraph product/docs page | exists | [langchain.com/langgraph](https://www.langchain.com/langgraph) |
| "What is Haystack?" (deepset) | exists | [haystack.deepset.ai/overview/intro](https://haystack.deepset.ai/overview/intro) |
| LangSmith observability & evals docs | exists | [LangSmith observability docs](https://docs.langchain.com/langsmith/observability) · [LangSmith evaluation docs](https://docs.langchain.com/langsmith/evaluation) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery notes: (1) presenter is Tyler per the spreadsheet — a guest co-teacher remains a nice-to-have, no longer a dependency; (2) landscape facts current as of 2026-07-28 — re-verify version claims at delivery prep; this space renames itself quarterly; (3) the 27-min two-pole tour is the timing risk — if the LangGraph kill-and-resume demo overruns, cut it to a recorded clip rather than dropping the raw-API comparison.
