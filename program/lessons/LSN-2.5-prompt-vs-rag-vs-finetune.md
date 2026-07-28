---
name: LSN-2.5-prompt-vs-rag-vs-finetune
description: Choose prompt vs RAG vs fine-tune for a given client ask, with cost and latency reasoning you can defend in the room.
module: MOD-2
serves: OUT-2.5
duration: 1 h
prework_time: 20
owner: Tyler
status: draft
---

# LSN-2.5 — Prompt vs RAG vs Fine-Tune

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.5 |
| **Duration** | 1 h session + 20 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-2 (quiz) |

## Narrative

The commercial judgment call. The misconception to kill: "train it on our data" is one thing. The capability to install: a two-axis decision framework plus token math, so the escalation prompt → RAG → fine-tune is earned step by step, never assumed. Builds on 2.4 (they know what RAG costs to run because they ran one) and points forward: fine-tuning mechanics (LoRA/PEFT, `generative_ai/04`) are advanced-tier; this hour is about *choosing*, not building.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the decision-framework one-pager (the framework below, as a standalone page) | 15 min | Nothing — used cold in the drill |
| 2 | Pick one real ask from a past or current project and place it on the 2×2 | 5 min | The ask + your quadrant, one line |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The framework | 20 min | talk + discussion | The two axes and the 2×2 (below). Myth-kill: fine-tuning teaches *behavior*, it does not reliably inject *knowledge*. Escalation order: prompt → RAG → fine-tune — each step must be earned by a measured failure of the previous one. Three pre-work placements reviewed aloud. |
| Cost reality: token math | 20 min | worked example | The support-assistant workload (below), computed live on the whiteboard. Participants recompute option B with their own k and chunk size from the 2.4 lab. Latency and ops burden noted alongside dollars. |
| Drill: four client asks | 20 min | drill | Teams of 3; each team gets one ask (below), 3 min to decide, 2 min to defend as if the client is in the room. Debrief traps after each. |

**Timing check:** 20 + 20 + 20 = 60 min = 1 h ✓

**The framework — two axes:**
- **Axis 1 — knowledge vs behavior.** Is the gap in what the model *knows* (your documents, fresh facts) or in how it *behaves* (tone, format, procedure, style)?
- **Axis 2 — changes daily vs changes never.** How fast does the required knowledge or behavior move?

| | Changes often | Static |
|---|---|---|
| **Knowledge** | **RAG** — re-indexing is cheap, retraining is not | Small: **put it in the prompt**. Large: RAG still wins on cost |
| **Behavior** | **System prompt + few-shot** — iterate freely | Prompt first; **fine-tune** when the prompt can't hold it or its length is a cost problem at scale (LoRA — `generative_ai/04`, advanced tier) |

Overlay on everything: cost, latency, and ops burden all rise prompt → RAG → fine-tune.

**Worked cost example.** Workload: internal assistant answering 2,000 questions/day over ~1,200 pages of policy documents (~600k tokens). **Assumed prices for the arithmetic only — not current vendor pricing; check real price sheets at delivery prep:** $3 per 1M input tokens, $15 per 1M output tokens, answers ~500 output tokens.
- **A. Stuff everything into the prompt:** 600k input tokens × 2,000 calls = 1.2B input tokens/day → 1,200 × $3 = **$3,600/day** (~$79k over 22 workdays) — and most context windows can't hold 600k tokens anyway. The shape of the number is the lesson.
- **B. RAG:** ~2,500 input tokens/question (5 chunks × ~400 + question + instructions) × 2,000 = 5M/day → $15; output 500 × 2,000 = 1M/day → $15. **≈ $30/day (~$660/month)**, plus a one-off corpus embedding (negligible at typical embedding prices) and index upkeep. ~120× cheaper per day than A.
- **C. Fine-tune:** assumed one-off training cost in the hundreds-to-low-thousands of dollars plus typically higher per-token serving prices — *and it still can't cite this quarter's policy revision*. You end up adding RAG anyway. Fine-tuning pays when it buys behavior or shorter prompts at very high volume, not knowledge.

**The four client asks (traps in italics, for the owner's debrief notes):**
1. "Our 4,000 pages of equipment maintenance manuals get revised quarterly — we want engineers to ask questions in plain language." *Trap: "fine-tune so it knows the manuals" — quarterly revisions rot the weights. RAG.*
2. "Every customer reply must sound exactly like our brand voice and follow our 6-step escalation script — 50,000 replies a month." *Behavior, changes never: prompt first; fine-tune is defensible at that volume if the style prompt is long and drifting.*
3. "The assistant should know who's staffed on which project — it changes weekly." *Trap: it's barely an LLM problem — RAG or, better, a structured lookup the model calls (tool use, MOD-3).*
4. "Can you train it on our codebase so it stops inventing our internal API names?" *Myth-kill live: fine-tuning won't reliably memorize identifiers. RAG over code and docs, retrieval at generation time.*

## Client Tie-In (Dorel's rule)

This hour is the pre-sales differentiator: on 6MAP the ask arrived garbled ("we want to train the AI on our data"), and the translation gap cost time. The framework is the un-garbling tool — every drill answer is delivered as if the client is in the room, and ask #1 is the construction-site prospect's maintenance-manual scenario almost verbatim.

## Homework

None. The framework one-pager goes into each participant's pre-sales kit; ASM-2 quiz scenarios draw directly from this drill format.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Decision-framework one-pager | build (light — extract the framework + cost example from this plan; module build list item) | program/materials/ — to create |
| LoRA/PEFT notebook — advanced-tier pointer only, not taught here | exists | notebooks/generative_ai/04_GenerativeAI_LoRA_PEFT_FineTuning.ipynb |
| Current vendor price sheets (input/output/embedding per-token) | build (refresh at delivery prep — prices move) | vendor pricing pages — verify at delivery prep |

## Delivery Notes

Not yet delivered. Record here: which trap caught a team, whether the cost math held attention, timing reality. Feeds the MOD-2 retro.
