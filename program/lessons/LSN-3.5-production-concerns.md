---
name: LSN-3.5-production-concerns
description: Ask the six production questions — observability, reliability, evals, KPIs, hardware, cost — credibly in a pre-sales or architecture review.
module: MOD-3
delivery_date: 2026-12-04
serves: OUT-3.4
duration: 1
prework_time: 20
homework_time: 100
owner: Tyler
status: draft
---

# LSN-3.5 — Production Concerns: The Translation-Gap Lesson

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.4` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | `ASM-3` — mock client conversation + question-bank homework |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Friday, 4 December 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |
| **Note** | Double-header: LSN-3.5 and LSN-3.6 both run Friday, 4 December |

**Preserved recruiting note:** a guest production practitioner — ideally someone who has been paged for an agent in production — was the original co-owner here. The spreadsheet assigns Tyler as presenter. The ask stays open, but at 1 h the guest's realistic contribution is one segment (observability or reliability), not a co-teach.

## Narrative

This is the lesson Vlad described when he described the whole program: "I know to ask about observability, I know to ask about reliability, whatever KPIs I need to have, hardware requirements, cost." It kills the misconception that production-readiness is a deployment checklist someone else owns — for agents, it's a set of questions the TL must ask before the SOW is signed. The material isn't hypothetical: every dimension is demonstrated on the participants' own instrumented agents from LSN-3.4, whose traces they already know they can't fully explain (that's the pre-work). The take-home is the TL question bank — companion to LSN-1.6's pre-sales bank — which participants carry into LSN-3.6's real cases and ASM-3's mock client conversation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-run your **Stage-B guardrailed agent** once — the combined task plus the break-it task — and leave the traces open | 12 | Traces open on your machine at session start |
| 2 | Skim your LSN-1.6 pre-sales question bank to refresh the format | 8 | — |

**Pre-work total: 20 min.** Deliberately thin — Thursday evening carries LSN-3.4's homework *and* the pre-work for both Friday sessions. **Carried in, not re-charged:** the guardrailed agent itself is **LSN-3.4 homework task 1 / Stage B** (35 min) and the **two questions you cannot answer from your logs** are **LSN-3.4 homework task 3** (5 min) — both budgeted there. Bring the questions; they get sorted live in segment 1.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Observability | 14 | demo + discussion | Live on **one** pre-arranged volunteer's Stage-B agent (not two — the clock): reconstruct one failed task from traces, every model call, tool call, token count. Then the room's "questions I can't answer" (LSN-3.4 homework task 3) get sorted fast: observability gap or design gap? Dimension row below. |
| Reliability | 10 | talk + drill | Failure-mode inventory on the lab agents: model timeout mid-task, tool error, loop that never stops, vendor's bad day. For each: retry, fallback, cap, or honest failure? Worst outcome named: the confident wrong answer. |
| Evals | 13 | talk + demo | The LSN-3.4 Stage-C eval check, scaled up in concept: golden sets, regression on every prompt change, LLM-as-judge and its caveats (validate the judge against human grades or don't trust it). Demo: change one word in a lab agent's system prompt, watch an eval catch the regression — **shown once, fast; participants reproduce it themselves as homework task 3.** |
| KPIs | 10 | discussion | Bridge agent metrics (task success rate, latency, cost per task) to business metrics (deflection, cycle time). Drill: who defines "success" for a support agent — builder or business owner? Wrong answer cost 6MAP dearly. |
| Hardware & cost | 10 | talk + worked example | API vs self-host: what forces the choice (data residency, air-gap, latency, volume) — usually nothing does. The estimate method demonstrated on one lab agent — tokens per task × tasks per month × price, plus the retry/wandering overhead the traces reveal — then **each participant runs the full estimate on their own agent as homework task 2.** |
| Hand over the question bank | 3 | drill | Each participant marks the three bank questions they'd be least comfortable asking a client today — that's homework task 4's focus. |

**Timing check:** 14 + 10 + 13 + 10 + 10 + 3 = 60 min = 1 h — matches the spreadsheet contract.

**What moved, not cut:** the second volunteer's observability walkthrough → the room now watches one and each participant does their own in homework task 1 · the full worked cost estimate → homework task 2 (live is method-only) · reproducing the eval regression → homework task 3 · the bank-question self-assessment write-up → homework task 4.

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

| # | Task | Time | Due | Artifact |
|---|---|---|---|---|
| 1 | **Graded.** Apply the question bank to your own LSN-3.4 agent and identify its **top three production gaps**. Each gap must (a) cite evidence from your traces, (b) name the bank question that exposed it, (c) propose a one-line remediation. "It has no tests" without trace evidence fails | 40 | Sun 6 Dec | Write-up, references `LSN-3.5` |
| 2 | Cost model on your own agent, using the worked method from segment 5: compute **cost per completed task** and the **fraction of token spend that is retries and wandering**, both derived from your traces, then project to 10k tasks/month | 25 | Sun 6 Dec | Worked estimate + the trace numbers it came from |
| 3 | Reproduce the eval regression yourself: change one word in your agent's system prompt, run your Stage-C eval, and report whether it caught the change. One paragraph on what the answer says about your suite | 20 | Sun 6 Dec | Before/after eval output + paragraph |
| 4 | The three bank questions you'd be **least** comfortable asking a client — for each, write the answer you would want to hear, so you know what you're listening for | 15 | Sun 6 Dec | Three questions + three model answers |

**Time accounting:** pre-work 20 min + homework 100 min = 2 h out-of-session budget.

**Cadence note:** nothing here is due the next morning — MOD-3's last live session is the same day, so all four tasks land on the weekend of 5–6 Dec. Feeds `ASM-3` (question-bank homework is part of how `OUT-3.4` is verified) and, via task 2, the Phase-4 capstone's cost story.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Six-dimension deck (skeleton above) | build (`GAP-4`) | TBD — GAP-4 deliverable, P0 |
| TL question bank as printable handout | build (`GAP-4`) | Drafted in this file; format alongside the LSN-1.6 bank. **Now needed by Fri 4 Dec morning** — LSN-3.6 runs the same day and depends on it |
| **Cost-model worksheet** (homework task 2) and **eval-regression worksheet** (homework task 3) | build (`GAP-4`) | New requirement from the restructure: the worked cost example and the regression demo moved from live walkthrough to solo homework, so each needs inputs, formula and a worked sample a participant can follow alone — slides are not enough |
| Participants' instrumented agents + traces | exists (prerequisite) | LSN-3.4 **Stage B** output — hard dependency, and Stage B is now homework done the night before. If Stage-B completion is low, segment 1 has no material: check submissions Friday morning |
| Observability in Generative AI — Microsoft Foundry (Microsoft Learn) | exists | [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) |
| Add observability to AgentCore resources (AWS docs) | exists | [docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html) |
| Anthropic — "Building Effective Agents" | exists | [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) |
| LangSmith evaluation docs | exists | [docs.langchain.com/langsmith/evaluation](https://docs.langchain.com/langsmith/evaluation) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery notes: (1) guest production practitioner unconfirmed — **no longer blocking** (Tyler presents per the spreadsheet); target someone who has been paged for an agent in production and give them one segment; (2) **one** volunteer agent pre-arranged Thursday night — confirm their Stage B actually completed, because a cold-called broken agent burns the 14-min segment; (3) this is the first half of a double-header — check room/calendar for the LSN-3.6 hand-off and take a real break between the two hours.
