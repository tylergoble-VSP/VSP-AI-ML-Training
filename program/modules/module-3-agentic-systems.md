---
name: module-3-agentic-systems
description: Agentic systems literacy — what agents are, the framework and cloud landscape, a hands-on agent build, production concerns (observability, reliability, evals, cost), and real VSP cases. The lion's share of the program begins here.
---

# MOD-3 — Agentic Systems Literacy

## Module Configuration

| Field | Value |
|---|---|
| **ID** | `MOD-3` |
| **Tier** | Basics |
| **Pillar** | Agentic systems — **the lion's share** ("I do think we will be tasked to do agentic systems" — Vlad) |
| **Week** | 3–4 |
| **Total effort** | ~11 h sessions + ~4 h pre-work/homework |
| **Module owner** | Tyler Goble (guest co-teachers targeted for LSN-3.2/3.3/3.5) |
| **Prerequisite** | `ASM-2` passed |
| **Checkpoint** | `ASM-3` — the basics final |

## Purpose

This is the module the program exists for. Vlad: "The lion's share should be agentic systems. And by that I mean frameworks, harnesses, evaluation frameworks… what GCP offers, what Bedrock offers, what Azure offers. All of this stuff has to be here." At basics level, the bar is fluency, not mastery: know the landscape, build one real agent, and ask the production questions — observability, reliability, evals, KPIs, hardware, cost — that close the 6MAP translation gap. The advanced tier turns this fluency into shipping capability; the expert tier turns it into evaluation-framework and harness depth.

## Outcomes

| ID | After MOD-3 you can… | Serves |
|---|---|---|
| `OUT-3.1` | Explain what an agent is — tools, loops, harnesses — and judge when an agent beats a plain workflow | GOAL-3, GOAL-4 |
| `OUT-3.2` | Map the framework landscape (LangChain, LangGraph, LangSmith, Haystack) and cloud offerings (GCP Vertex, AWS Bedrock, Microsoft Foundry — formerly Azure AI Foundry) to use cases | GOAL-3 |
| `OUT-3.3` | Personally build a tool-calling agent end to end | GOAL-3, GOAL-6 |
| `OUT-3.4` | Ask the production questions: observability, reliability, evals, KPIs, hardware, cost | GOAL-3, GOAL-4 |
| `OUT-3.5` | Walk a real VSP case from client ask → architecture → production concerns, speaking both languages | GOAL-1, GOAL-2, GOAL-3, GOAL-4 |

## Lesson Inventory

| ID | Lesson | Duration | Owner | Format | Material status |
|---|---|---|---|---|---|
| `LSN-3.1` | What is an agent — tools, loops, harnesses | 1.5 h | Tyler | Live | Exists (`generative_ai/06`) |
| `LSN-3.2` | Framework landscape | 1.5 h | Guest / TBD | Live | **BUILD — GAP-2** |
| `LSN-3.3` | Cloud landscape — Vertex, Bedrock, Azure | 1.5 h | Per-cloud owners TBD | Live panel | **BUILD — GAP-3** |
| `LSN-3.4` | **Hands-on: build a tool-calling agent** | 2.5 h | Tyler | Live lab | Extend (`generative_ai/06`) |
| `LSN-3.5` | Production concerns — the translation-gap lesson | 1.5 h | Tyler + guest | Live | **BUILD — GAP-4** |
| `LSN-3.6` | Real VSP cases, end to end | 1 h | Vlad + Dorel + Tyler | Live | **BUILD — GAP-5** |
| — | `ASM-3` — basics final: exam + mock client conversation | 1.5 h | All owners | Live | **BUILD — GAP-6** |

---

### LSN-3.1 — What Is an Agent

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-3.1` |

**Purpose:** Precision about the word "agent": an LLM in a loop with tools and a goal, plus the harness that keeps it honest. Workflow vs agent as an engineering decision (deterministic pipeline when you can, agent when you must). Tool calling from LSN-2.2 becomes the core primitive.

**Pre-work (~30 min):** Read a curated "what is an agent" piece + revisit your LSN-2.2 structured-output homework; think about what it would take to let the model *act* on its output.

**Session outline:**
1. From chatbot to agent: goal, loop, tools, memory, stop condition (25 min)
2. The harness: permissions, guardrails, human-in-the-loop — why production agents are mostly harness (25 min)
3. Workflow vs agent decision drill: five scenarios, pick and defend (25 min)
4. Anatomy walkthrough of a real agent trace — what actually happened turn by turn (15 min)

**Homework:** None (pre-work for the lab).

**Support material:** Exists — `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` (concept sections); curated reading list at lesson-plan time.

---

### LSN-3.2 — Framework Landscape

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Guest co-teacher / TBD (Tyler fallback) | `OUT-3.2` |

**Purpose:** Vlad's list, made navigable: LangChain (components), LangGraph (stateful orchestration), LangSmith (observability/evals), Haystack (pipelines/RAG) — plus where lighter-weight approaches (direct API + tool use) beat frameworks. The outcome is a mental map: given an ask, name the two candidate stacks and the tradeoff.

**Pre-work (~40 min):** One-page framework cards (built as part of GAP-2); skim each framework's own "what is this" page.

**Session outline:**
1. Why frameworks exist: what you'd otherwise hand-roll (15 min)
2. The tour: same toy problem shown in LangChain, LangGraph, Haystack, and raw API — side by side (45 min)
3. Choosing: maturity, lock-in, observability hooks, team skill — the tradeoff table (20 min)
4. When *no* framework is right (10 min)

**Homework:** Match five client scenarios to a stack, one sentence of justification each.

**Support material:** **BUILD (`GAP-2`)** — framework cards + side-by-side demo. Priority build: this and GAP-3/GAP-4 are the program's center of gravity.

---

### LSN-3.3 — Cloud Landscape: Vertex, Bedrock, Microsoft Foundry

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Per-cloud owners (TBD from cohort/guests; panel format) | `OUT-3.2` |

**Purpose:** "What GCP offers, what Bedrock offers, what Azure offers — all of this has to be here" (Vlad). Panel format by design: one owner per cloud, 25 minutes each, same rubric — models available, agent tooling, RAG/knowledge-base offering, eval/observability story, pricing shape, lock-in. This lesson also seeds the advanced tier's per-person cloud ownership model.

**Pre-work (~30 min):** Each participant skims one assigned cloud's AI landing page and brings one "what is this actually?" question.

**Session outline:**
1. The rubric — how to compare clouds without marketing fog (5 min)
2. GCP Vertex AI (25 min) · AWS Bedrock (25 min) · Microsoft Foundry (25 min) — same rubric each
3. Cross-examination: participants' questions (10 min)

**Homework:** None.

**Support material:** **BUILD (`GAP-3`)** — comparison rubric + three per-cloud one-pagers. Recruiting per-cloud owners is part of the build ("maybe somebody knows Azure, maybe somebody knows Bedrock" — Vlad).

---

### LSN-3.4 — Hands-On: Build a Tool-Calling Agent

| Duration | Owner | Serves |
|---|---|---|
| 2.5 h (live lab) | Tyler | `OUT-3.3` |

**Purpose:** Everyone ships an agent: LLM + 2–3 tools + a loop + a stop condition, solving a small real task (e.g., answer questions by searching a doc store *and* calling a calculator — retrieval callback to LSN-2.4). Then instrument it: log every tool call, watch it fail, add one guardrail. The instrumentation is the point — it makes LSN-3.5 concrete.

**Pre-work (~45 min, mandatory):** Working RAG artifact from LSN-2.4 available; read the guided notebook intro; API key provisioned.

**Session outline:**
1. Skeleton: the loop, the tool schema, the stop condition (30 min)
2. Guided build: wire two tools, run the loop, read the traces (60 min)
3. Break it: give it a task the tools can't do; watch the failure modes (25 min)
4. Guardrail: add max-turns + one permission gate; re-run (20 min)
5. Wrap: what you built vs what LangGraph/Bedrock would have given you — bridge to 3.2/3.3 (15 min)

**Homework (artifact, graded):** Add a third tool and one eval check (does the agent's final answer match a known-good answer on 3 test tasks?); submit notebook + traces.

**Support material:** Extend — `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` reworked into a guided lab with tracing + guardrail sections (fold into GAP-2 build effort). Note: the existing notebook and `src/llm/tool_calling.py` run a local HF model; the lab extension adds a hosted-API path alongside it.

---

### LSN-3.5 — Production Concerns: The Translation-Gap Lesson

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler + guest (production practitioner) | `OUT-3.4` |

**Purpose:** The lesson Vlad described when he described the whole program: "I know to ask about observability, I know to ask about reliability, I know to ask about whatever KPIs I need to have, I need to ask about the hardware requirements, cost." Six production dimensions, each with: what it means for agentic systems, what good looks like, and the questions a TL asks in a pre-sales or architecture review.

**Pre-work (~30 min):** Review your instrumented agent traces from LSN-3.4; note two things you couldn't answer about your own agent's behavior.

**Session outline:**
1. Observability: traces, tool-call logs, token accounting — demo on the LSN-3.4 agents (20 min)
2. Reliability: retries, timeouts, fallback models, graceful degradation (15 min)
3. Evals: offline suites, regression on prompt changes, LLM-as-judge caveats (20 min)
4. KPIs: task success rate, deflection, latency, cost per task — tying agent metrics to business metrics (15 min)
5. Hardware & cost: tokens, GPUs, self-host vs API — the estimate a client will ask for (15 min)
6. Build the TL question bank — companion to the LSN-1.6 bank (5 min)

**Homework:** Apply the question bank to your LSN-3.4 agent; identify its top three production gaps.

**Support material:** **BUILD (`GAP-4`)** — six-dimension deck + TL question bank. P0 build.

---

### LSN-3.6 — Real VSP Cases, End to End

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Vlad + Dorel + Tyler | `OUT-3.5` |

**Purpose:** Dorel's rule fully applied: "connect the lesson and the topic to the problem in real life." Two or three real cases — the construction-site completion prospect (vision + ML), 6MAP (the translation-gap origin), the in-production meeting-RAG system — each walked ask → triage (which pillar? which job?) → sketch architecture → production questions. The whole basics tier, exercised on real work.

**Pre-work (~30 min):** Case briefs (anonymized, from Vlad/Dorel).

**Session outline:**
1. Case 1 — construction-site completion: triage and architecture, group-driven (20 min)
2. Case 2 — meeting-RAG in production: what the production questions reveal (20 min)
3. Case 3 — 6MAP: where translation broke and how this cohort would run it now (20 min)

**Homework:** None — final week.

**Support material:** **BUILD (`GAP-5`)** — case briefs require Vlad/Dorel input; request at the July 30 review.

---

## Checkpoint — ASM-3: The Basics Final

| Field | Value |
|---|---|
| **Format** | Written exam (~25 scenario questions across all four modules, 45 min) **+ mock client conversation** (20 min/participant: a realistic ask spanning ML/LLM/agentic; Vlad or Dorel plays the client; rubric-graded) **+ artifact review** (MNIST, RAG, agent — all three submitted and working) |
| **Verifies** | `OUT-3.1`–`OUT-3.5` directly; samples MOD-0/1/2 outcomes for retention |
| **Pass bar** | Exam 80% + conversation rubric "client-ready" + all three artifacts accepted |
| **Gate** | Basics graduation → advanced tier eligibility + hackathon seat |
| **Status** | **BUILD — GAP-6**. Seed from `notebooks/interview/` (GenAI implementation junior/mid/senior + ML Engineer test/answer key) |

## Traceability

| Outcome | Served by | Verified by |
|---|---|---|
| `OUT-3.1` | LSN-3.1 | ASM-3 (exam + conversation) |
| `OUT-3.2` | LSN-3.2, LSN-3.3 | ASM-3 (exam + conversation) |
| `OUT-3.3` | LSN-3.4 | ASM-3 (artifact) |
| `OUT-3.4` | LSN-3.5 | ASM-3 (conversation + question-bank homework) |
| `OUT-3.5` | LSN-3.6 | ASM-3 (conversation) |

## Build List

| ID | Item | Owner | Needed by |
|---|---|---|---|
| `GAP-2` | Framework cards + side-by-side demo + agent lab extension | Tyler + guest TBD | Week 3 |
| `GAP-3` | Cloud comparison rubric + three one-pagers + per-cloud owner recruitment | Tyler (recruiting) | Week 3 |
| `GAP-4` | Production-concerns deck + TL question bank | Tyler + guest | Week 4 |
| `GAP-5` (share) | Case briefs ×3 | Vlad + Dorel | Week 4 |
| `GAP-6` (share) | ASM-3 exam + conversation rubric | Tyler | End of Week 4 |
