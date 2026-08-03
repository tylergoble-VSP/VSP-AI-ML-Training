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
| **Schedule** | **Mon 30 Nov – Fri 4 Dec 2026** — one lesson per day, **double-header Fri 4 Dec** (LSN-3.5 then LSN-3.6) (program spreadsheet, locked 2026-08-03) |
| **Per lesson** | 1 h live + 2 h out-of-session (pre-work + homework combined) |
| **Total effort** | 6 h live + 12 h out-of-session = **18 h** — compressed into a single week, which makes it the program's heaviest week (see the cadence arithmetic below) |
| **Presenter (all six)** | Tyler Goble — per the program spreadsheet; guest co-teacher / per-cloud-owner ambitions preserved as open recruiting notes per lesson |
| **Reviewer (all six)** | Vlad |
| **Guinea pig (all six)** | Mazilu (TBC — spreadsheet reads "Mazilu?") |
| **Prerequisite** | `ASM-2` passed |
| **Checkpoint** | `ASM-3` — the basics final (**not on the program spreadsheet** — needs a calendar slot, see below) |
| **Followed by** | Phase-4 capstone, Dec 14–17 2026 — "Build an Agentic Harness that Scores Leads" (`module-4-capstone.md`) |
| **Canonical dates** | `program/SCHEDULE.md` — this spec must not drift from it |

## Cadence and evening-stacking arithmetic — flag for the next review call

Per-lesson dates and pre-work/homework splits are in the Lesson Inventory below; canonical dates live in `program/SCHEDULE.md`. A daily cadence means each evening carries **lesson N's homework and lesson N+1's pre-work**, and the **Thu 3 Dec evening feeds the Friday double-header** — LSN-3.5 *and* LSN-3.6 pre-work both land on top of LSN-3.4's homework. Mitigations built into the lesson plans:

1. **Pre-work held to 15–30 min** module-wide; LSN-3.6's case-brief reading is folded into LSN-3.4's homework so its own pre-work is 15 min.
2. **Homework chains forward** — lesson N's homework deliberately produces the artifact lesson N+1 needs, so an evening carries one task, not two. Chains: 3.1 hw → 3.2 pre-work (framework cards) · 3.2 hw → 3.3 pre-work (cloud landing page) · 3.4 hw Stage B → 3.5 pre-work (guardrailed agent + traces) · 3.4 hw → 3.6 pre-work (case briefs). LSN-3.1's homework also front-loads API-key/env setup off Thursday.
3. **Every homework task carries an explicit `Due` column** in its lesson plan — either the next session (needed the following morning) or Sun 6 Dec (graded artifact, floats past the delivery week). This is what decouples the 2 h *budget* from the evening *load*.

Resulting **mandatory** evening load: Mon 60 min · Tue 45 min · Wed 30 min · Thu 85 min. **The remainder — ≈8 h of graded artifact work — necessarily spills past Fri 4 Dec.** Honest arithmetic: 12 h of out-of-session work does not fit into five working evenings alongside a full work day. It is scheduled for Dec 5–6 and realistically spreads into Dec 7–11 (the proposed `ASM-3` week). **Decision needed:** accept the spill, cut the per-lesson out-of-session budget below 2 h, or spread MOD-3 across two weeks.

## Purpose

This is the module the program exists for. Vlad: "The lion's share should be agentic systems. And by that I mean frameworks, harnesses, evaluation frameworks… what GCP offers, what Bedrock offers, what Azure offers. All of this stuff has to be here." At basics level, the bar is fluency, not mastery: know the landscape, build one real agent, and ask the production questions — observability, reliability, evals, KPIs, hardware, cost — that close the 6MAP translation gap. The advanced tier turns this fluency into shipping capability; the expert tier turns it into evaluation-framework and harness depth. MOD-3 is the **last taught module of the basics tier, not the end of the program**: `ASM-3` gates basics graduation, and the **Phase-4 capstone (Dec 14–17, "Build an Agentic Harness that Scores Leads")** is where this fluency is exercised as delivery.

## Outcomes

| ID | After MOD-3 you can… | Serves |
|---|---|---|
| `OUT-3.1` | Explain what an agent is — tools, loops, harnesses — and judge when an agent beats a plain workflow | GOAL-3, GOAL-4 |
| `OUT-3.2` | Map the framework landscape (LangChain, LangGraph, LangSmith, Haystack) and cloud offerings (GCP Vertex, AWS Bedrock, Microsoft Foundry — formerly Azure AI Foundry) to use cases | GOAL-3 |
| `OUT-3.3` | Personally build a tool-calling agent end to end | GOAL-3, GOAL-6 |
| `OUT-3.4` | Ask the production questions: observability, reliability, evals, KPIs, hardware, cost | GOAL-3, GOAL-4 |
| `OUT-3.5` | Walk a real VSP case from client ask → architecture → production concerns, speaking both languages | GOAL-1, GOAL-2, GOAL-3, GOAL-4 |

## Lesson Inventory

| ID | Lesson | Date | Live | Out-of-session (pre-work + hw) | Presenter | Format | Material status |
|---|---|---|---|---|---|---|---|
| `LSN-3.1` | What is an agent — tools, loops, harnesses | Mon 30 Nov 2026 | 1 h | 2 h (25 + 95 min) | Tyler | Live | Exists (`generative_ai/06`) |
| `LSN-3.2` | Framework landscape | Tue 1 Dec 2026 | 1 h | 2 h (20 + 100 min) | Tyler | Live | **BUILD — GAP-2** |
| `LSN-3.3` | Cloud landscape — Vertex, Bedrock, Foundry | Wed 2 Dec 2026 | 1 h | 2 h (20 + 100 min) | Tyler | Live (panel if owners recruited) | **BUILD — GAP-3** |
| `LSN-3.4` | **Hands-on: build a tool-calling agent** | Thu 3 Dec 2026 | 1 h | 2 h (30 + 90 min) | Tyler | Live lab + solo stages | Extend (`generative_ai/06`) |
| `LSN-3.5` | Production concerns — the translation-gap lesson | Fri 4 Dec 2026 | 1 h | 2 h (20 + 100 min) | Tyler | Live | **BUILD — GAP-4** |
| `LSN-3.6` | Real VSP cases, end to end | Fri 4 Dec 2026 — **double-header, 2nd session** | 1 h | 2 h (15 + 105 min) | Tyler | Live | **BUILD — GAP-5** |
| — | `ASM-3` — basics final: exam + mock client conversation | **unscheduled** *(not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Dec 7–11, between MOD-3 and the Dec 14–17 capstone)* | 1.5 h | — | Tyler | Live | **BUILD — GAP-6** |

**Presenter-role discrepancy (flag for the next review call):** earlier plans assigned a guest co-teacher to LSN-3.2, per-cloud owners to LSN-3.3, a production practitioner to LSN-3.5, and Vlad + Dorel to LSN-3.6. The spreadsheet puts **Tyler** on all six, so Tyler is recorded as the responsible presenter. The guest/co-owner intentions are **preserved as open recruiting asks** — they now upgrade a session rather than gate it:

| Lesson | Original intent | Preserved as |
|---|---|---|
| `LSN-3.2` | Guest co-teacher (framework practitioner) | Recruit for the side-by-side tour; lesson ships without one |
| `LSN-3.3` | Three per-cloud owners, panel, 25 min each | The 25-min panel no longer fits 1 h. Owners now contribute the **rubric column + one-pager** (GAP-3) and take a 12-min live slot if available. Still seeds the advanced tier's per-person cloud ownership |
| `LSN-3.5` | Guest production practitioner (someone paged for an agent in production) | Recruit for the observability or reliability segment, not a co-teach |
| `LSN-3.6` | Vlad + Dorel facilitating, in character as the client | Ask stays open — their in-character presence is what makes the session real. **`GAP-5` still hard-depends on Vlad/Dorel for the case briefs; Tyler cannot substitute, because no case fact may be invented** |

---

### LSN-3.1 — What Is an Agent

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Mon 30 Nov 2026 | 1 h | 2 h (25 min pre-work + 95 min homework) | Tyler | `OUT-3.1` |

**Purpose:** Precision about the word "agent": an LLM in a loop with tools and a goal, plus the harness that keeps it honest. Workflow vs agent as an engineering decision (deterministic pipeline when you can, agent when you must). Tool calling from LSN-2.2 becomes the core primitive.

**Pre-work (25 min):** Read a curated "what is an agent" piece + revisit your LSN-2.2 structured-output homework; note what it would take to let the model *act* on its output.

**Session outline (60 min):**
1. From chatbot to agent: goal, loop, tools, memory, stop condition (18 min)
2. The harness: permissions, guardrails, human-in-the-loop — why production agents are mostly harness (15 min)
3. Workflow vs agent decision drill: three scenarios live, pick and defend (18 min)
4. Anatomy walkthrough of a real agent trace — what actually happened turn by turn (9 min)

**Homework (95 min):** Framework cards read + one line each (**doubles as LSN-3.2 pre-work**, 30) · API key + repo env smoke test, front-loaded off the Thursday lab (10) · notebook-06 trace annotation against the six-part definition (30) · workflow-vs-agent memo on the two drill scenarios cut from the live session (25). First two due Tue 1 Dec; the rest by Sun 6 Dec.

**Support material:** Exists — `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` (concept sections); curated reading list at lesson-plan time.

---

### LSN-3.2 — Framework Landscape

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Tue 1 Dec 2026 | 1 h | 2 h (20 min pre-work + 100 min homework) | Tyler (guest co-teacher still an open recruiting ask — see Lesson Inventory) | `OUT-3.2` |

**Purpose:** Vlad's list, made navigable: LangChain (components), LangGraph (stateful orchestration), LangSmith (observability/evals), Haystack (pipelines/RAG) — plus where lighter-weight approaches (direct API + tool use) beat frameworks. The outcome is a mental map: given an ask, name the two candidate stacks and the tradeoff.

**Pre-work (20 min):** Skim the "what is this" page of the two frameworks your LSN-3.1 homework left least clear; mark plumbing-vs-logic in your LSN-2.4 RAG code. *The GAP-2 framework cards are read as LSN-3.1 homework — budgeted there, not here.*

**Session outline (60 min):**
1. Why frameworks exist: what you'd otherwise hand-roll (8 min)
2. The tour: same toy problem in raw API and LangGraph — the two poles, side by side (27 min)
3. Choosing: maturity, lock-in, observability hooks, team skill — the tradeoff table (15 min)
4. When *no* framework is right (10 min)

**Homework (100 min):** Assigned-cloud landing-page skim + question (**doubles as LSN-3.3 pre-work**, 25) · match five client scenarios to a stack naming the deciding axis (35) · meeting-RAG retro-fit memo (20) · self-study the two implementations cut from the live tour — LangChain 1.0 `create_agent` and Haystack 2.x — noting where the loop and state live (20). First task due Wed 2 Dec; the rest by Sun 6 Dec.

**Support material:** **BUILD (`GAP-2`)** — framework cards + side-by-side demo. Priority build: this and GAP-3/GAP-4 are the program's center of gravity. **Restructure note:** the demo must now be *self-study-readable* — the LangChain and Haystack implementations are homework, not live walkthrough, so they need commentary cells a participant can follow alone.

---

### LSN-3.3 — Cloud Landscape: Vertex, Bedrock, Microsoft Foundry

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Wed 2 Dec 2026 | 1 h | 2 h (20 min pre-work + 100 min homework) | Tyler (per-cloud owners still an open recruiting ask — "maybe somebody knows Azure, maybe somebody knows Bedrock", Vlad — see Lesson Inventory) | `OUT-3.2` |

**Purpose:** "What GCP offers, what Bedrock offers, what Azure offers — all of this has to be here" (Vlad). One rubric across three clouds — models available, agent tooling, RAG/knowledge-base offering, eval/observability story, pricing shape, lock-in. The deep per-cloud walk moves out of the live hour into the take-home rubric.

**Pre-work (20 min):** Read the six-axis rubric so the compressed format lands; sharpen your assigned-cloud question. *The landing-page skim is LSN-3.2 homework — budgeted there.*

**Session outline (60 min):**
1. The rubric — how to compare clouds without marketing fog (6 min)
2. GCP Vertex AI (12 min) · AWS Bedrock (12 min) · Microsoft Foundry (12 min) — same rubric each, headline rows only
3. Cross-cloud contrast: the three rows where they actually differ (10 min)
4. Cross-examination: participants' questions (8 min)

**Homework (100 min):** Complete your assigned cloud's rubric column incl. "worst at" (30) · cloud-fit memo on the construction-site prospect and the meeting-RAG system (25) · managed-equivalent mapping for the agent you build tomorrow (25) · price the 10k-task/month worked example on public pricing (20). All due Sun 6 Dec — **nothing here is due next morning**, deliberately, so Wednesday evening can absorb LSN-3.4's 30-min Stage-A pre-work.

**Support material:** **BUILD (`GAP-3`)** — comparison rubric + three per-cloud one-pagers. **Restructure note:** with per-cloud depth moved to homework, the one-pagers are now the *primary* teaching artifact rather than a handout, and the rubric must be self-serve fillable.

---

### LSN-3.4 — Hands-On: Build a Tool-Calling Agent

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Thu 3 Dec 2026 | 1 h | 2 h (30 min pre-work + 90 min homework) | Tyler | `OUT-3.3` |

**Restructure (the big one):** the lab was a 2.5 h live session; the spreadsheet gives it 1 h. It is now a **three-stage lab** — Stage A solo (pre-work: skeleton + stub tool round-trips), the **live hour** (unblock, wire the two real tools, everyone's first successful real tool call, break-it drill), Stage B/C solo (homework: guardrails, third tool, eval check). Nothing was cut; the solo stages carry explicit checkpoints so the live hour can start from a known state.

**Purpose:** Everyone ships an agent: LLM + 2–3 tools + a loop + a stop condition, solving a small real task (e.g., answer questions by searching a doc store *and* calling a calculator — retrieval callback to LSN-2.4). Then instrument it: log every tool call, watch it fail, add one guardrail. The instrumentation is the point — it makes LSN-3.5 concrete.

**Pre-work — Stage A (30 min, mandatory, checkpointed):** run the skeleton `agent_loop()` with a stub `echo` tool until one tool call round-trips (15) · confirm your LSN-2.4 retrieval returns chunks, or load the fallback index (10) · one sentence: "what stops your agent?" (5). *API key + env were done as LSN-3.1 homework — front-loaded off this evening.*

**Session outline (60 min):**
1. Unblock & sync: Stage-A triage, fallback index for anyone broken (10 min)
2. Wire the two real tools — everyone's agent makes its **first successful real tool call** on the combined task (25 min)
3. Read the trace together, turn by turn (8 min)
4. Break it: a task the tools can't do; classify the failure mode (12 min)
5. Wrap: raw build vs LangGraph/Bedrock + Stage B/C brief (5 min)

**Homework (90 min):** **Stage B** — max-turns stop reason + one permission gate, re-run the break-it task, keep traces (**doubles as LSN-3.5 pre-work**, 35, due Fri morning) · two questions you can't answer from your logs (5, due Fri) · skim the three LSN-3.6 case briefs (**doubles as LSN-3.6 pre-work**, 10, due Fri) · **Stage C, graded artifact** — third tool + eval check on three known-good tasks, submit notebook + traces (40, due Sun 6 Dec).

**Support material:** Extend — `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` reworked into a guided lab with tracing + guardrail sections (fold into GAP-2 build effort). Note: the existing notebook and `src/llm/tool_calling.py` run a local HF model; the lab extension adds a hosted-API path alongside it. **Restructure note — new build requirement:** the notebook must now be **runnable solo in three staged sections** (Stage A pre-work, live section, Stage B/C homework), each with a self-checkable checkpoint cell that prints pass/fail, because the guardrail and third-tool work is no longer instructor-supervised. Stage A also needs an unattended-failure path (fallback mini-corpus + pre-built index reachable without help).

---

### LSN-3.5 — Production Concerns: The Translation-Gap Lesson

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Fri 4 Dec 2026 (first of two sessions) | 1 h | 2 h (20 min pre-work + 100 min homework) | Tyler (guest production practitioner still an open recruiting ask — see Lesson Inventory) | `OUT-3.4` |

**Purpose:** The lesson Vlad described when he described the whole program: "I know to ask about observability, I know to ask about reliability, I know to ask about whatever KPIs I need to have, I need to ask about the hardware requirements, cost." Six production dimensions, each with: what it means for agentic systems, what good looks like, and the questions a TL asks in a pre-sales or architecture review.

**Pre-work (20 min):** Re-run your Stage-B guardrailed agent on its three eval tasks, traces open (12); skim your LSN-1.6 pre-sales bank for format (8). *Your instrumented agent and the two "questions I can't answer" arrive from LSN-3.4 homework — budgeted there.*

**Session outline (60 min):**
1. Observability: traces, tool-call logs, token accounting — demo on the LSN-3.4 agents (14 min)
2. Reliability: retries, timeouts, fallback models, graceful degradation (10 min)
3. Evals: offline suites, regression on prompt changes, LLM-as-judge caveats (13 min)
4. KPIs: task success rate, deflection, latency, cost per task — agent metrics to business metrics (10 min)
5. Hardware & cost: tokens, GPUs, self-host vs API — the estimate a client will ask for (10 min)
6. Hand over the TL question bank — companion to the LSN-1.6 bank (3 min)

**Homework (100 min, all due Sun 6 Dec):** Apply the question bank to your own agent — top three production gaps with trace evidence (graded, 40) · cost per completed task + retry/wandering fraction from your traces, projected to 10k tasks/month (25) · add one eval regression and show it catching a one-word prompt change (20) · the three bank questions you'd least like to ask a client, with the answer you'd want to hear (15).

**Support material:** **BUILD (`GAP-4`)** — six-dimension deck + TL question bank. P0 build. **Restructure note:** the worked cost example and the eval-regression demo move from live walkthrough to homework, so both need a step-by-step worksheet (inputs, formula, worked sample) rather than slides alone.

---

### LSN-3.6 — Real VSP Cases, End to End

| Date | Live | Out-of-session | Presenter | Serves |
|---|---|---|---|---|
| Fri 4 Dec 2026 (second of two sessions — **double-header with LSN-3.5**) | 1 h | 2 h (15 min pre-work + 105 min homework) | Tyler (Vlad + Dorel in-character facilitation still an open recruiting ask; Vlad is reviewer, Dorel is not on the spreadsheet — see Lesson Inventory) | `OUT-3.5` |

**Purpose:** Dorel's rule fully applied: "connect the lesson and the topic to the problem in real life." Two or three real cases — the construction-site completion prospect (vision + ML), 6MAP (the translation-gap origin), the in-production meeting-RAG system — each walked ask → triage (which pillar? which job?) → sketch architecture → production questions. The whole basics tier, exercised on real work.

**Pre-work (15 min — deliberately minimal; this is the second session of a double-header and its evening is the module's heaviest):** bring one written triage question per case and both question banks. *The case briefs themselves are read as LSN-3.4 homework — budgeted there.*

**Session outline (60 min):**
1. Case 1 — construction-site completion: triage and architecture, group-driven (20 min)
2. Case 2 — meeting-RAG in production: what the production questions reveal (20 min)
3. Case 3 — 6MAP: where translation broke and how this cohort would run it now (20 min)

**Homework (105 min, all due Sun 6 Dec):** One-page pre-sales brief walking one case ask → triage → architecture → top five production questions (45) · paired mock client conversation on a case you did *not* write up, 15 min each way — the `ASM-3` rehearsal (30) · read the Phase-4 capstone brief and name which MOD-3 artifacts you carry in (15) · re-rate yourself against `OUT-3.1`–`OUT-3.5` versus your LSN-0.1 baseline (15). This is no longer "final week" homework: it is `ASM-3` and capstone on-ramp.

**Support material:** **BUILD (`GAP-5`)** — case briefs require Vlad/Dorel input; request at the next review call. **Untouchable rule:** no invented case facts. If a brief cannot be sourced from Vlad/Dorel or `meetings/2026-07-28-ml-discussion/transcript.md`, the case runs shorter rather than fuller. **Restructure note:** the briefs are now *pre-read as LSN-3.4 homework*, so they must stand alone at ~1 page with no facilitator preamble.

---

## Checkpoint — ASM-3: The Basics Final

**Not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Dec 7–11, between MOD-3 and the Dec 14–17 capstone.** That slot also absorbs the ≈8 h out-of-session tail from the MOD-3 delivery week (see the evening-stacking arithmetic above), so it should be a light-touch week other than the assessment itself.

| Field | Value |
|---|---|
| **Proposed date** | Week of Dec 7–11 2026 — **unscheduled**, not on the spreadsheet |
| **Format** | Written exam (~25 scenario questions across all four modules, 45 min) **+ mock client conversation** (20 min/participant: a realistic ask spanning ML/LLM/agentic; Vlad or Dorel plays the client; rubric-graded) **+ artifact review** (MNIST, RAG, agent — all three submitted and working) |
| **Verifies** | `OUT-3.1`–`OUT-3.5` directly; samples MOD-0/1/2 outcomes for retention |
| **Pass bar** | Exam 80% + conversation rubric "client-ready" + all three artifacts accepted |
| **Gate** | Basics graduation → seat at the **Phase-4 capstone (Dec 14–17, "Build an Agentic Harness that Scores Leads")** + advanced tier eligibility. MOD-3 ends the taught basics tier; the capstone ends the program |
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
| `GAP-2` | Framework cards + **self-study-readable** side-by-side demo (LangChain/Haystack now homework) | Tyler (+ guest if recruited) | Mon 30 Nov (cards are LSN-3.1 homework) |
| `GAP-2b` | Agent lab extension — **three staged sections with self-checkable checkpoint cells** + unattended Stage-A fallback index | Tyler | Wed 2 Dec (Stage A is LSN-3.4 pre-work) |
| `GAP-3` | Cloud rubric (self-serve fillable) + three one-pagers as **primary** teaching artifact + per-cloud owner recruitment | Tyler (recruiting) | Tue 1 Dec (landing-page assignment is LSN-3.2 homework) |
| `GAP-4` | Production-concerns deck + TL question bank + **cost/eval-regression worksheets** for homework | Tyler (+ guest if recruited) | Fri 4 Dec |
| `GAP-5` (share) | Case briefs ×3 — must **stand alone as pre-read**; no invented facts | Vlad + Dorel | Thu 3 Dec (pre-read is LSN-3.4 homework) |
| `GAP-6` (share) | ASM-3 exam + conversation rubric | Tyler | Once ASM-3 is calendared (proposed Dec 7–11) |
