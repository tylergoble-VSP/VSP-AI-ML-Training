---
name: LSN-3.5-production-concerns
description: Ask the six production questions — observability, reliability, evals, KPIs, hardware, cost — credibly in a pre-sales or architecture review.
module: MOD-3
serves: OUT-3.4
duration: 1.5 h
prework_time: 30
owner: Tyler + guest (production practitioner, TBD)
status: draft
---

# LSN-3.5 — Production Concerns: The Translation-Gap Lesson

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.4` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | `ASM-3` — mock client conversation + question-bank homework |

## Narrative

This is the lesson Vlad described when he described the whole program: "I know to ask about observability, I know to ask about reliability, whatever KPIs I need to have, hardware requirements, cost." It kills the misconception that production-readiness is a deployment checklist someone else owns — for agents, it's a set of questions the TL must ask before the SOW is signed. The material isn't hypothetical: every dimension is demonstrated on the participants' own instrumented agents from LSN-3.4, whose traces they already know they can't fully explain (that's the pre-work). The take-home is the TL question bank — companion to LSN-1.6's pre-sales bank — which participants carry into LSN-3.6's real cases and ASM-3's mock client conversation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-run your LSN-3.4 agent on its three eval tasks; skim the traces | 15 | Traces open on your machine at session start |
| 2 | Write down two questions about your own agent's behavior that you cannot answer from its logs | 10 | The two questions, written |
| 3 | Skim your LSN-1.6 pre-sales question bank to refresh the format | 5 | — |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Observability | 20 | demo + discussion | Live on two volunteers' LSN-3.4 agents: reconstruct one failed task from traces — every model call, tool call, token count. Then the room's pre-work "questions I can't answer" get sorted: which are observability gaps vs design gaps. Dimension row below. |
| Reliability | 15 | talk + drill | Failure-mode inventory on the lab agents: model timeout mid-task, tool error, loop that never stops, vendor's bad day. For each: retry, fallback, cap, or honest failure? Worst outcome named: the confident wrong answer. |
| Evals | 20 | talk + demo | The LSN-3.4 homework's three-task eval check, scaled up in concept: golden sets, regression on every prompt change, LLM-as-judge and its caveats (validate the judge against human grades or don't trust it). Demo: change one word in a lab agent's system prompt, watch an eval catch the regression. |
| KPIs | 15 | discussion | Bridge agent metrics (task success rate, latency, cost per task) to business metrics (deflection, cycle time). Drill: who defines "success" for a support agent — builder or business owner? Wrong answer cost 6MAP dearly. |
| Hardware & cost | 15 | talk + worked example | API vs self-host: what forces the choice (data residency, air-gap, latency, volume) — usually nothing does. Worked estimate on a lab agent: tokens per task × tasks per month × price, plus the retry/wandering overhead the traces reveal. |
| Assemble the question bank | 5 | drill | Each participant marks the three bank questions they'd be least comfortable asking a client today — that's their homework focus. |

**Timing check:** 20 + 15 + 20 + 15 + 15 + 5 = 90 min = 1.5 h contract. ✓

### The six dimensions (deck skeleton — GAP-4)

| Dimension | What it means for agentic systems | What good looks like |
|---|---|---|
| **Observability** | An agent decides at runtime; without per-step traces (model calls, tool calls, tokens, latency) no single answer can be explained after the fact | Every task has a trace ID; any failure reconstructed step-by-step in minutes without re-running; per-task token/cost accounting; OpenTelemetry-shaped so it survives a platform switch |
| **Reliability** | Failure modes multiply: model timeouts, tool errors, runaway loops, degraded vendor days — and the loop can turn any of them into a confident wrong answer | Retries with backoff at tool and model layers; max-turns and budget caps; a defined degraded mode (fallback model or honest "not now"); no silent-wrong-answer path |
| **Evals** | Prompts and models change under you; evals are the regression suite for behavior you didn't hand-code | Golden task set runs on every prompt/model change and blocks deploys like failing tests; offline suite + sampled production spot-checks; LLM-as-judge only where validated against human grades |
| **KPIs** | Agent metrics mean nothing until mapped to a business metric the client already reports | "Success" defined by the business owner, not the builder; deflection/cycle-time/cost-per-task target written into the SOW; a dashboard the client's exec can read |
| **Hardware** | Mostly the API-vs-self-host question and what forces it: data residency, air-gap, latency floors, volume | The team can name the requirement that forces self-hosting — or state that none does; GPU sizing derived from measured token throughput, not vibes |
| **Cost** | Agents spend tokens in loops — cost is a runtime behavior, not a price sheet | Cost per completed task known and trended; retries/wandering measured as a fraction of spend; levers (caching, model routing, prompt trimming) identified before anyone renegotiates a contract |

### TL question bank (take-home artifact — companion to the LSN-1.6 bank)

**Observability** — 1. "Show me the full trace of one failed task from last week — every model call, tool call, and token count." 2. "When the agent gives a wrong answer, how long until you know which step went wrong?" 3. "What do you log per tool call today, and who looks at it?"
**Reliability** — 4. "The model API times out mid-task: retry, fallback model, or user-facing error — which, and where is that decided?" 5. "What are the max-turns and budget caps per task, and what happens when one is hit?" 6. "The vendor has a degraded day: what does your user see?"
**Evals** — 7. "What runs automatically when someone edits a prompt — would it catch a regression before production?" 8. "How many golden test tasks exist, and who owns keeping them current?" 9. "Where do you use LLM-as-judge, and how was the judge validated against human grades?"
**KPIs** — 10. "What is the task success rate, and who defined 'success' — the builder or the business owner?" 11. "Which business metric moves if this agent works — deflection, cycle time, revenue — and who reports that number today?" 12. "What does one completed task cost end to end, and which direction is it trending?"
**Hardware** — 13. "Is anything self-hosted — and if so, which GPUs, and what's utilization at peak vs idle?" 14. "Does any requirement (data residency, air-gap, latency floor) actually force on-prem inference — or is it preference?" 15. "What breaks first at 10× traffic: quota, rate limits, or budget?"
**Cost** — 16. "What fraction of token spend is retries and agent wandering, and how do you know?" 17. "What cost model was shown to the client — per task, per seat, per month — and on what usage assumption?" 18. "What levers exist before renegotiating the model contract: caching, a smaller routing model, prompt trimming?"

## Client Tie-In (Dorel's rule)

6MAP is the spine: the translation gap this program exists to close was observed there, and the KPI segment names the specific failure — "success" was never defined by the business owner. The in-production meeting-RAG system is the live target: during the observability and KPI segments, two bank questions are asked of it for real, with real answers (or real silence — equally instructive). The construction-site completion prospect grounds the hardware & cost segment: the estimate a client asks for in pre-sales, built live with the worked-example method.

## Homework

Apply the question bank to your own LSN-3.4 agent and identify its **top three production gaps**. Submission references `LSN-3.5`. Grading standard: each gap must (a) cite evidence from your traces, (b) name the bank question that exposed it, (c) propose a one-line remediation. "It has no tests" without trace evidence fails. Feeds `ASM-3` (question-bank homework is part of how OUT-3.4 is verified).

## Materials

| Material | Status | Path / source |
|---|---|---|
| Six-dimension deck (skeleton above) | build (`GAP-4`) | TBD — GAP-4 deliverable, P0 |
| TL question bank as printable handout | build (`GAP-4`) | Drafted in this file; format alongside the LSN-1.6 bank |
| Participants' instrumented agents + traces | exists (prerequisite) | LSN-3.4 lab output — hard dependency |
| Observability in Generative AI — Microsoft Foundry (Microsoft Learn) | exists | [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) |
| Add observability to AgentCore resources (AWS docs) | exists | [docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html) |
| Anthropic — "Building Effective Agents" | exists | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |
| LangSmith evaluation docs | exists | [docs.langchain.com/langsmith/evaluation](https://docs.langchain.com/langsmith/evaluation) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery dependencies: (1) guest production practitioner unconfirmed — target someone who has been paged for an agent in production; (2) two volunteer agents from LSN-3.4 pre-arranged so the observability demo isn't cold-called.
