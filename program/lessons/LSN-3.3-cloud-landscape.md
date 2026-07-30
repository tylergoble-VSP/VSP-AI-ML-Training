---
name: LSN-3.3-cloud-landscape
description: Compare GCP Vertex AI, AWS Bedrock, and Microsoft Foundry (Azure) on one rubric and say which fits a given client and why.
module: MOD-3
serves: OUT-3.2
duration: 1.5 h
prework_time: 30
owner: Per-cloud owners TBD (panel; Tyler moderates)
status: draft
---

# LSN-3.3 — Cloud Landscape: Vertex, Bedrock, Azure AI Foundry

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.2` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live panel — one owner per cloud, 25 min each, identical rubric |
| **Verified by** | `ASM-3` — exam + mock client conversation (cloud-fit scenarios) |

## Narrative

Kills the misconception that the three clouds offer the same thing under different names — and its opposite, that you pick "the cloud we know." The naming churn is itself the first lesson: Azure AI Foundry became Microsoft Foundry at Ignite (Nov 2025); AWS's original Bedrock Agents is now "Agents Classic" and closes to new customers on July 30, 2026 — two days after this plan was written — with AgentCore as the successor; Google is folding Vertex AI Agent Builder into "Gemini Enterprise Agent Platform" branding. A TL who compares on a stable rubric survives the churn; one who memorizes product names doesn't. Callback: LSN-3.2's "when no framework is right" criteria pointed here. Setup: seeds the advanced tier's per-person cloud ownership model.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Skim your assigned cloud's AI landing page (assignment by Marius; links in Materials) | 25 | — |
| 2 | Write one "what is this actually?" question about a product name on that page | 5 | The question, written — fuels cross-examination |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The rubric | 5 | talk | Tyler frames the six axes below and the anti-marketing rules: every claim dated, every product named as of today, "worst at" is mandatory. |
| GCP Vertex AI | 25 | panel + live console | Owner walks their rubric column row by row (speaker brief below); at least one row shown in the real console. |
| AWS Bedrock | 25 | panel + live console | Same rubric, same order. |
| Microsoft Foundry (Azure) | 25 | panel + live console | Same rubric, same order. |
| Cross-examination | 10 | discussion | Participants fire their pre-work questions; panel answers or says "I don't know" — which is also the lesson. |

**Timing check:** 5 + 25 + 25 + 25 + 10 = 90 min = 1.5 h contract. ✓

### The comparison rubric (owners fill their column; seeded facts current as of 2026-07-28)

| Axis | GCP Vertex AI | AWS Bedrock | Microsoft Foundry (Azure) |
|---|---|---|---|
| **Models available** | Model Garden: 200+ models — Gemini, Anthropic Claude, Llama, Gemma. *Owner: current headliners + regions.* | Multi-vendor catalog: Anthropic Claude, Meta, Mistral, Amazon's own models. *Owner: current headliners + regions.* | Azure OpenAI (GPT family) + broad third-party catalog. *Owner: current catalog size + regions.* |
| **Agent tooling** | Agent Builder = ADK (open-source, code-first; Python/Go/Java/TS) + Agent Engine (managed runtime: Sessions, Memory Bank, Code Execution) + Agent Studio (low-code). | AgentCore: Runtime, Gateway, Memory, Identity, Observability + Code Interpreter & Browser tools; framework-agnostic (runs LangGraph, CrewAI, etc.). Bedrock Agents "Classic" closed to new customers 2026-07-30. | Foundry Agent Service (hosted agents) + Microsoft Agent Framework; runtime, memory, and grounding tooling added through Build 2026. |
| **RAG / knowledge base** | Vertex AI Search; RAG Engine *(owner: verify current naming)*. | Bedrock Knowledge Bases; new Managed Knowledge Base — native connectors (S3, SharePoint, Confluence, Google Drive, OneDrive, web crawler), Smart Parsing, Agentic Retriever. | Azure AI Search integration + Foundry grounding tools *(owner: verify current naming)*. |
| **Eval / observability story** | Agent Engine evaluation services; Cloud Trace/Logging. *Owner: demo one trace.* | AgentCore Observability: built-in metrics per Runtime/Memory/Gateway/tools/Identity; A/B testing of agent versions on live traffic — even for agents running outside AWS. *Owner: demo one trace.* | Four capabilities on one OpenTelemetry pipeline: Trace, Evaluate, Monitor, Optimize; traces LangChain, LangGraph, OpenAI Agents SDK, MS Agent Framework; hosted-agent tracing+evals GA'd mid-2026. *Owner: demo one trace.* |
| **Pricing shape** | Per-token model pricing + Agent Engine compute. *Owner: worked example — 10k-task/month support agent.* | Per-token (on-demand or provisioned throughput) + AgentCore service consumption. *Owner: same worked example.* | Azure OpenAI per-token + agent service compute. *Owner: same worked example.* |
| **Lock-in** | ADK is open source and runs anywhere; Agent Engine/Memory Bank are sticky managed services; branding churn (→ Gemini Enterprise Agent Platform). | Framework-agnostic runtime, but Gateway/Memory/Identity are AWS services; the Agents-Classic sunset proves migration risk is real. | Entra ID / M365 integration is the pull; OTel pipeline is portable; two renames in two years (AI Studio → AI Foundry → Foundry). |

### Speaker brief (hand to each per-cloud owner)

- **Your 25 minutes:** 3 min orientation (what the platform is, one-sentence naming history up to today) → 17 min rubric walk, one row at a time, in table order → 5 min "the gotcha I learned the hard way" + spillover questions.
- **Rules:** rubric rows only, no vendor decks; date every claim ("as of <date>"); show the live console for at least one row (agent tooling or knowledge base); bring one worked pricing example (10k-task/month support agent — all three owners use the same scenario so numbers are comparable); name the one thing your cloud is worst at.
- **Deliverables, one week before session:** your rubric column completed in this file + a one-pager (GAP-3 format) + a 10-min dry run with Tyler.
- **Audience calibration:** senior engineers and TLs who will repeat what you say to clients. If a product was renamed, say both names. If a feature is preview-only, say so.

## Client Tie-In (Dorel's rule)

Cross-examination closes with a five-minute bid exercise on the construction-site completion prospect: vision + agent workload, client has an existing cloud footprint — which cloud do we bid and which rubric rows decided it? Second anchor: the in-production meeting-RAG system — each owner points at the rubric's RAG row and states what the managed equivalent of our hand-rolled build would be on their cloud, and what it would cost us in lock-in.

## Homework

None (per module spec — final rubric becomes the take-home reference). The completed rubric and one-pagers feed `ASM-3` cloud-fit scenario questions.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Comparison rubric (above) as fillable handout | build (`GAP-3`) | TBD — GAP-3 deliverable |
| Per-cloud one-pagers ×3 | build (`GAP-3`) | TBD — owed by per-cloud owners one week before session |
| **Per-cloud owner recruitment — open dependency** | build (`GAP-3`) | Unfilled as of 2026-07-28; raise at July 30 curriculum review ("maybe somebody knows Azure, maybe somebody knows Bedrock" — Vlad) |
| Vertex AI Agent Builder overview (Google Cloud docs — page now branded "Gemini Enterprise Agent Platform") | exists | [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) |
| "What is Amazon Bedrock AgentCore?" (AWS docs) | exists | [docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) |
| Foundry Agent Service (Microsoft product page) | exists | [azure.microsoft.com/en-us/products/ai-foundry/agent-service](https://azure.microsoft.com/en-us/products/ai-foundry/agent-service) |
| Observability in Generative AI — Microsoft Foundry (Microsoft Learn) | exists | [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) |

## Delivery Notes

*To be filled after delivery.* Pre-delivery dependencies: (1) three per-cloud owners unrecruited — blocking; (2) all seeded rubric facts dated 2026-07-28 and must be re-verified at delivery prep — this is the fastest-moving lesson in the program by design.
