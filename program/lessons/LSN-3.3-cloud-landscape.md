---
name: LSN-3.3-cloud-landscape
description: Compare GCP Vertex AI, AWS Bedrock, and Microsoft Foundry (Azure) on one rubric and say which fits a given client and why.
module: MOD-3
delivery_date: 2026-12-02
serves: OUT-3.2
duration: 1
prework_time: 20
homework_time: 100
owner: Tyler
status: draft
---

# LSN-3.3 — Cloud Landscape: Vertex, Bedrock, Azure AI Foundry

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.2` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live — one rubric, three clouds, 12 min each (panel if per-cloud owners are recruited) |
| **Verified by** | `ASM-3` — exam + mock client conversation (cloud-fit scenarios) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Wednesday, 2 December 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

**Preserved recruiting note:** the original design was a three-owner panel at 25 min per cloud ("maybe somebody knows Azure, maybe somebody knows Bedrock" — Vlad). At 1 h that panel no longer fits, and the spreadsheet assigns Tyler as presenter. **The per-cloud owner ask stays open and stays valuable** — owners now (a) fill their rubric column and write their one-pager (`GAP-3`), and (b) take a 12-min live slot if available, with Tyler covering any unfilled cloud. This still seeds the advanced tier's per-person cloud ownership model.

## Narrative

Kills the misconception that the three clouds offer the same thing under different names — and its opposite, that you pick "the cloud we know." The naming churn is itself the first lesson: Azure AI Foundry became Microsoft Foundry at Ignite (Nov 2025); AWS's original Bedrock Agents is now "Agents Classic" and closes to new customers on July 30, 2026 — two days after this plan was written — with AgentCore as the successor; Google is folding Vertex AI Agent Builder into "Gemini Enterprise Agent Platform" branding. A TL who compares on a stable rubric survives the churn; one who memorizes product names doesn't. Callback: LSN-3.2's "when no framework is right" criteria pointed here. Setup: seeds the advanced tier's per-person cloud ownership model.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the six-axis rubric below so the compressed 12-min-per-cloud format lands — you must know what row is coming next | 10 | — |
| 2 | Re-read your own cloud question and add one follow-up you'd ask if the first answer is marketing | 10 | Both questions, written — fuels cross-examination |

**Pre-work total: 20 min.** Deliberately thin — Tuesday evening also carries LSN-3.2's homework. **Carried in, not re-charged:** the assigned-cloud landing-page skim and your first "what is this actually?" question were **LSN-3.2 homework task 1** (25 min, budgeted there).

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The rubric | 6 | talk | Tyler frames the six axes below and the anti-marketing rules: every claim dated, every product named as of today, "worst at" is mandatory. Also frames the compression: **headline rows live, full column as homework.** |
| GCP Vertex AI | 12 | talk/panel + live console | **Headline rows only — agent tooling, eval/observability, lock-in** (the three that actually decide a bid), one shown in the real console. Models/RAG/pricing rows are read from the rubric, not walked. Speaker brief below. |
| AWS Bedrock | 12 | talk/panel + live console | Same three rows, same order. |
| Microsoft Foundry (Azure) | 12 | talk/panel + live console | Same three rows, same order. |
| Cross-cloud contrast | 10 | discussion | Put the three columns side by side and name where they genuinely differ vs where they've converged — the move a TL makes in front of a client. **Replaces the per-cloud deep walk that no longer fits.** |
| Cross-examination | 8 | discussion | Participants fire their pre-work questions; the answer "I don't know" is allowed and is also the lesson. |

**Timing check:** 6 + 12 + 12 + 12 + 10 + 8 = 60 min = 1 h — matches the spreadsheet contract.

**What moved, not cut:** the three rubric rows dropped from the live walk (models available, RAG/knowledge base, pricing shape) are covered by **homework tasks 1 and 4** — participants complete their own cloud's full column and price the shared worked example themselves. The "gotcha I learned the hard way" and the worked pricing example move from the speaker's 25 min into the one-pager (`GAP-3`).

### The comparison rubric (owners fill their column; seeded facts current as of 2026-07-28)

| Axis | GCP Vertex AI | AWS Bedrock | Microsoft Foundry (Azure) |
|---|---|---|---|
| **Models available** | Model Garden: 200+ models — Gemini, Anthropic Claude, Llama, Gemma. *Owner: current headliners + regions.* | Multi-vendor catalog: Anthropic Claude, Meta, Mistral, Amazon's own models. *Owner: current headliners + regions.* | Azure OpenAI (GPT family) + broad third-party catalog. *Owner: current catalog size + regions.* |
| **Agent tooling** | Agent Builder = ADK (open-source, code-first; Python/Go/Java/TS) + Agent Engine (managed runtime: Sessions, Memory Bank, Code Execution) + Agent Studio (low-code). | AgentCore: Runtime, Gateway, Memory, Identity, Observability + Code Interpreter & Browser tools; framework-agnostic (runs LangGraph, CrewAI, etc.). Bedrock Agents "Classic" closed to new customers 2026-07-30. | Foundry Agent Service (hosted agents) + Microsoft Agent Framework; runtime, memory, and grounding tooling added through Build 2026. |
| **RAG / knowledge base** | Vertex AI Search; RAG Engine *(owner: verify current naming)*. | Bedrock Knowledge Bases; new Managed Knowledge Base — native connectors (S3, SharePoint, Confluence, Google Drive, OneDrive, web crawler), Smart Parsing, Agentic Retriever. | Azure AI Search integration + Foundry grounding tools *(owner: verify current naming)*. |
| **Eval / observability story** | Agent Engine evaluation services; Cloud Trace/Logging. *Owner: demo one trace.* | AgentCore Observability: built-in metrics per Runtime/Memory/Gateway/tools/Identity; A/B testing of agent versions on live traffic — even for agents running outside AWS. *Owner: demo one trace.* | Four capabilities on one OpenTelemetry pipeline: Trace, Evaluate, Monitor, Optimize; traces LangChain, LangGraph, OpenAI Agents SDK, MS Agent Framework; hosted-agent tracing+evals GA'd mid-2026. *Owner: demo one trace.* |
| **Pricing shape** | Per-token model pricing + Agent Engine compute. *Owner: worked example — 10k-task/month support agent.* | Per-token (on-demand or provisioned throughput) + AgentCore service consumption. *Owner: same worked example.* | Azure OpenAI per-token + agent service compute. *Owner: same worked example.* |
| **Lock-in** | ADK is open source and runs anywhere; Agent Engine/Memory Bank are sticky managed services; branding churn (→ Gemini Enterprise Agent Platform). | Framework-agnostic runtime, but Gateway/Memory/Identity are AWS services; the Agents-Classic sunset proves migration risk is real. | Entra ID / M365 integration is the pull; OTel pipeline is portable; two renames in two years (AI Studio → AI Foundry → Foundry). |

### Speaker brief (hand to each per-cloud owner, or to Tyler for unfilled clouds)

- **Your 12 minutes:** 2 min orientation (what the platform is, one-sentence naming history up to today) → 9 min on **three rows only — agent tooling, eval/observability, lock-in**, in table order → 1 min "the one thing my cloud is worst at."
- **Rules:** rubric rows only, no vendor decks; date every claim ("as of <date>"); show the live console for exactly one row (agent tooling or knowledge base) — one, not several, because the clock is real; name the one thing your cloud is worst at out loud.
- **Moved into your one-pager (no longer live):** the models/RAG/pricing rows, the worked pricing example (10k-task/month support agent — same scenario across all three clouds so numbers stay comparable), and "the gotcha I learned the hard way." Participants price the example themselves as homework task 4, so your worked version is the answer key.
- **Deliverables, one week before session:** your rubric column completed in this file + a one-pager (GAP-3 format) + a 5-min dry run with Tyler.
- **Audience calibration:** senior engineers and TLs who will repeat what you say to clients. If a product was renamed, say both names. If a feature is preview-only, say so.

## Client Tie-In (Dorel's rule)

The cross-cloud contrast segment poses the bid question on the construction-site completion prospect in one minute — vision + agent workload, client has an existing cloud footprint, which cloud do we bid and which rubric rows decided it? — and **homework task 2 is where it gets answered in writing** (the five-minute live exercise does not fit 60 min). Second anchor: the in-production meeting-RAG system — the same memo names what the managed equivalent of our hand-rolled build would be on each cloud and what it would cost us in lock-in, a question each cloud's one-pager must answer on the RAG row.

## Homework

The spreadsheet's 2 h out-of-session budget converts this lesson's former "no homework" into the work that used to happen live: the per-cloud depth is now earned by doing, not watching.

| # | Task | Time | Due | Artifact |
|---|---|---|---|---|
| 1 | Complete **your assigned cloud's full rubric column** — all six axes, every claim dated, including the mandatory "what it's worst at" | 30 | Sun 6 Dec | Filled column (feeds the shared rubric) |
| 2 | Cloud-fit memo: for **the construction-site completion prospect** and **the in-production meeting-RAG system**, name the cloud you'd bid and the **two rubric rows that decided it** | 25 | Sun 6 Dec | Memo, references `LSN-3.3` |
| 3 | Managed-equivalent mapping for the agent you build tomorrow in LSN-3.4: for each hand-rolled part (loop, trace log, tool registry, memory, permission gate), name the managed service on **each** of the three clouds that replaces it — or write "no equivalent" | 25 | Sun 6 Dec | 5×3 table |
| 4 | Price the shared worked example — a 10k-task/month support agent — on your cloud's **public** pricing pages. Show the arithmetic and state every assumption | 20 | Sun 6 Dec | Worked estimate |

**Time accounting:** pre-work 20 min + homework 100 min = 2 h out-of-session budget.

**Cadence note — deliberate:** **nothing here is due the next morning.** Wednesday evening must absorb LSN-3.4's 30-min Stage-A pre-work, which is a hard gate on the Thursday lab, so all four tasks float to the weekend of 5–6 Dec. Task 3 is the exception worth doing early if you have the appetite — it primes the LSN-3.4 wrap segment. The completed rubric and one-pagers feed `ASM-3` cloud-fit scenario questions.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Comparison rubric (above) as fillable handout | build (`GAP-3`) | TBD — GAP-3 deliverable. **New requirement:** must be **self-serve fillable** — homework task 1 has participants completing a column with no facilitator present, so each axis needs a prompt of what a complete answer looks like |
| Per-cloud one-pagers ×3 | build (`GAP-3`) | TBD. **Promoted from handout to primary teaching artifact:** with the live walk cut to three rows per cloud, the one-pagers now carry models/RAG/pricing, the worked pricing example (the answer key for homework task 4), and the "gotcha." Owed one week before session |
| **Per-cloud owner recruitment — now an upgrade, not a blocker** | build (`GAP-3`) | Unfilled as of 2026-08-03; raise at the next curriculum review ("maybe somebody knows Azure, maybe somebody knows Bedrock" — Vlad). Tyler presents any unfilled cloud from the one-pager |
| Managed-equivalent mapping sheet (homework task 3) | build (`GAP-3`) | New — the 5×3 grid (hand-rolled part × cloud), pre-labelled with the five LSN-3.4 parts so the task is fill-in, not invent |
| Vertex AI Agent Builder overview (Google Cloud docs — page now branded "Gemini Enterprise Agent Platform") | exists | [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) |
| "What is Amazon Bedrock AgentCore?" (AWS docs) | exists | [docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) |
| Foundry Agent Service (Microsoft product page) | exists | [azure.microsoft.com/en-us/products/ai-foundry/agent-service](https://azure.microsoft.com/en-us/products/ai-foundry/agent-service) |
| Observability in Generative AI — Microsoft Foundry (Microsoft Learn) | exists | [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery notes: (1) three per-cloud owners still unrecruited — **no longer blocking** (Tyler presents from the one-pagers per the spreadsheet), but recruit anyway; (2) all seeded rubric facts dated 2026-07-28 and must be re-verified at delivery prep — this is the fastest-moving lesson in the program by design; (3) 12 min per cloud is the tightest timing in MOD-3 — run a hard clock and let the cross-cloud contrast segment absorb any spillover, never the console demo.
