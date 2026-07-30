---
name: LSN-2.1-how-llms-actually-work
description: Explain how an LLM works — tokens, training vs inference, context windows, why it hallucinates — to a colleague or client without hand-waving.
module: MOD-2
serves: OUT-2.1
duration: 1.5 h
prework_time: 45
owner: Tyler
status: draft
---

# LSN-2.1 — How LLMs Actually Work

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.1 |
| **Duration** | 1.5 h session + 45 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-2 (quiz) |

## Narrative

Kill the magic. Participants arrive as fluent ChatGPT consumers who cannot say what a token is or why the model confidently invents things. The session installs one honest mental model — next-token prediction scaled up, shaped by pretraining → fine-tuning → RLHF (RL callback to LSN-1.5) — and reframes hallucination as a structural property of that mechanism, not a bug to be patched. Everything downstream depends on this: prompting (2.2), retrieval as grounding (2.3/2.4), and the honest client conversation (2.6).

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch Andrej Karpathy, ["Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g) (YouTube) — the opening segment on what an LLM is / next-word prediction, and the hallucination segment (timestamps on the segment list) | ~20 min | One sentence: the thing that most changed your mental model |
| 2 | Watch Andrej Karpathy, ["Deep Dive into LLMs like ChatGPT"](https://www.youtube.com/watch?v=7xTGNNLPyMI) (YouTube, 3 h 31 m) — the tokenization segment only (timestamp on the segment list) | ~10 min | Nothing — feeds task 3 |
| 3 | Tokenize two sentences in the [OpenAI tokenizer playground](https://platform.openai.com/tokenizer): one plain-English sentence, one containing code or a rare/technical word. Count the tokens vs the words | ~15 min | Screenshot of both tokenizations |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Tokens: what the model actually sees | 20 min | demo + discussion | Review 3–4 participant screenshots on screen. Tokens ≠ words: whitespace, subwords, code, non-English text. Why letter-counting questions fail. Cost and context are denominated in tokens — first commercial hook. |
| Next-token prediction scaled up | 25 min | talk | One arc: pretraining (internet-scale next-token) → supervised fine-tuning (demonstrations) → RLHF (preference ranking; RL callback to LSN-1.5 — reward signal shaping a policy). Base model vs assistant model. Temperature: why the same prompt varies. |
| Context window = working memory | 20 min | talk + demo | What fits, what falls out, what was never there (your data, anything after training cutoff). Demo: bury an instruction early in a very long paste and watch it get ignored. Design consequences: chunking and retrieval — setup for 2.3/2.4. |
| Why it hallucinates — and why that's structural | 25 min | demo + discussion | Live demo (prompt below). The model emits plausible continuations; there is no truth oracle inside. What mitigates (grounding, citations, "say you don't know" instructions, evals) vs what doesn't (asking "are you sure?"). The single most important thing to explain to a client. |

**Timing check:** 20 + 25 + 20 + 25 = 90 min = 1.5 h ✓

**Live "confident wrong answer" demo — concrete prompt.** Run cold, no system prompt:
> "Provide the full citation — authors, journal, year, and DOI — for the 2019 paper 'Hierarchical Attention Networks for Insurance Claim Triage'."

The paper does not exist; models typically fabricate a plausible citation with real-sounding authors and a well-formed DOI. Fallback if the model hedges: "What parameters does the `getClaimStatus` endpoint of the Veridian Insurance public REST API accept?" (fictional company — the model will often invent a parameter list). Rehearse both at delivery prep; keep a saved transcript as backup if the live model refuses.

## Client Tie-In (Dorel's rule)

The construction-site prospect's first question in pre-sales is some form of "so it can answer anything about our manuals?" The engineer who can explain — in two sentences, without hand-waving — why a raw LLM will confidently invent a torque spec, and why grounding it in the client's own documents (the way our in-production meeting-RAG system does) changes that, is the one the client trusts. This lesson builds exactly that explanation.

## Homework

None — LSN-2.2 carries heavy pre-work instead. Bring your tokenizer screenshot forward; it reappears in the cost math of LSN-2.5.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Karpathy — "Intro to Large Language Models" (video) | exists | [youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g) (segment timestamps chosen at delivery prep) |
| Karpathy — "Deep Dive into LLMs like ChatGPT" (video, 3 h 31 m) | exists | [youtube.com/watch?v=7xTGNNLPyMI](https://www.youtube.com/watch?v=7xTGNNLPyMI) (segment timestamps chosen at delivery prep) |
| Karpathy segment list (one page, with timestamps) | build (lesson-plan work, module build list) | program/materials/ — to create |
| "LLM in five pictures" deck | build (lesson-plan work, module build list) | program/materials/ — to create |
| OpenAI tokenizer playground | exists | [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) |
| Stanford GenAI companion decks | pending | Tyler pulling via academic contacts |

## Delivery Notes

Not yet delivered. Record here: which pre-work segment landed, whether the fabricated-citation demo fired on the first try, and timing reality per segment. Feeds the MOD-2 retro.
