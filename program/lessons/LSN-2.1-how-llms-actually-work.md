---
name: LSN-2.1-how-llms-actually-work
description: Explain how an LLM works — tokens, training vs inference, context windows, why it hallucinates — to a colleague or client without hand-waving.
module: MOD-2
delivery_date: 2026-10-19
serves: OUT-2.1
duration: 1
prework_time: 120
homework_time: 120
owner: Tyler
status: draft
---

# LSN-2.1 — How LLMs Actually Work

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.1 |
| **Duration** | 1 h live + 4 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | ASM-2 (quiz) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 19 October 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 4 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

## Narrative

Kill the magic. Participants arrive as fluent ChatGPT consumers who cannot say what a token is or why the model confidently invents things. The session installs one honest mental model — next-token prediction scaled up, shaped by pretraining → fine-tuning → RLHF (RL callback to LSN-1.5) — and reframes hallucination as a structural property of that mechanism, not a bug to be patched. Everything downstream depends on this: prompting (2.2), retrieval as grounding (2.3/2.4), and the honest client conversation (2.6).

## Pre-work (mandatory — no pre-work, no seat)

The 4 h out-of-session budget makes the Karpathy talks assignable in substance rather than in excerpts — this is the module's declared spirit reference, so watching it properly *is* the curriculum, not a reading-list gesture. Chapter names below are the videos' own chapter titles; exact timestamps go on the segment list at delivery prep.

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch Andrej Karpathy, ["Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **in full** (the whole ~1 h talk, including the LLM-security closing on jailbreaks and prompt injection, which seeds LSN-2.6) | 60 min | Three bullets: the thing that most changed your mental model, one thing you didn't believe, one question for the room |
| 2 | Watch Andrej Karpathy, ["Deep Dive into LLMs like ChatGPT"](https://www.youtube.com/watch?v=7xTGNNLPyMI) (3 h 31 m) — chapters **"tokenization"**, **"neural net I/O"**, **"neural net internals"**, **"inference"** | 40 min | Nothing — feeds task 3 and session segments 1–2 |
| 3 | Tokenize **four** strings in the [OpenAI tokenizer playground](https://platform.openai.com/tokenizer): one plain-English sentence, one with code, one with a rare/technical word (e.g. a drug name or a part number), one in a non-Latin script. Record tokens vs words for each, then price 1,000 calls carrying all four at $3 / 1M input tokens | 20 min | Screenshots + your four token counts + the dollar figure |

**Time accounting (pre-work):** 60 + 40 + 20 = 120 min.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Tokens: what the model actually sees | 10 min | demo + discussion | Two participant screenshots on screen — chosen in advance for contrast (non-Latin script vs code). Tokens ≠ words; why letter-counting questions fail. Their own dollar figure from pre-work task 3 read out: cost and context are denominated in tokens. The rest of the token taxonomy was covered in pre-work; do not re-teach it. |
| Next-token prediction scaled up | 20 min | talk | One arc: pretraining (internet-scale next-token) → supervised fine-tuning (demonstrations) → RLHF (preference ranking; RL callback to LSN-1.5 — reward signal shaping a policy). Base model vs assistant model. Temperature: why the same prompt varies. |
| Context window = working memory | 10 min | talk + demo | What fits, what falls out, what was never there (your data, anything after training cutoff). One quick demo: an instruction buried early in a long paste gets ignored. Design consequences: chunking and retrieval — setup for 2.3/2.4. The systematic position experiment is theirs to run in homework. |
| Why it hallucinates — and why that's structural | 20 min | demo + discussion | Live demo (prompt below). The model emits plausible continuations; there is no truth oracle inside. What mitigates (grounding, citations, "say you don't know" instructions, evals) vs what doesn't (asking "are you sure?"). The single most important thing to explain to a client. |

**Timing check:** 10 + 20 + 10 + 20 = 60 min = 1 h — matches the spreadsheet contract.

**What moved out of the live hour (1.5 h → 1 h):** the full token taxonomy (whitespace/subwords/code/non-English) now lands in pre-work tasks 2–3, where participants generate it themselves; the context-window investigation shrinks to one demo, with the position sweep relocated to homework task 2. Nothing was dropped.

**Live "confident wrong answer" demo — concrete prompt.** Run cold, no system prompt:
> "Provide the full citation — authors, journal, year, and DOI — for the 2019 paper 'Hierarchical Attention Networks for Insurance Claim Triage'."

The paper does not exist; models typically fabricate a plausible citation with real-sounding authors and a well-formed DOI. Fallback if the model hedges: "What parameters does the `getClaimStatus` endpoint of the Veridian Insurance public REST API accept?" (fictional company — the model will often invent a parameter list). Rehearse both at delivery prep; keep a saved transcript as backup if the live model refuses.

## Client Tie-In (Dorel's rule)

The construction-site prospect's first question in pre-sales is some form of "so it can answer anything about our manuals?" The engineer who can explain — in two sentences, without hand-waving — why a raw LLM will confidently invent a torque spec, and why grounding it in the client's own documents (the way our in-production meeting-RAG system does) changes that, is the one the client trusts. This lesson builds exactly that explanation.

## Homework

| # | Task | Time | Deliverable |
|---|---|---|---|
| 1 | Finish the **Deep Dive** arc: chapters **"pretraining to post-training"**, **"post-training data (conversations)"**, **"hallucinations, tool use, knowledge/working memory"**, **"models need tokens to think"**. This is the honest-mechanics core of the module's spirit reference and it directly reinforces session segments 2 and 4 | 50 min | Half a page: how post-training turns a document-completer into an assistant, and why Karpathy calls context "working memory" |
| 2 | **Lost-in-the-middle experiment** (relocated from the live hour). Take a long document (~8–10k words). Plant one specific instruction — e.g. "end your answer with the word ORANGE" — at the start, the middle, and the end. Run each position twice, then repeat all three at roughly half the document length. Log obeyed/ignored | 30 min | A 6-row results table + one sentence on what this implies for chunk placement in RAG |
| 3 | **Hallucination hunt in your own domain.** Get a confident wrong answer about something you can verify (a real API's parameters, a standard's clause number, a competitor's pricing tier). Then try three mitigations on the same question: (a) "say you don't know if you're unsure", (b) paste the real source into context, (c) ask "are you sure?" Record which changed the answer and which only changed the tone | 25 min | The fabricated answer + a 3-row mitigation table with your verdict on (c) |
| 4 | Write the **two-sentence client explanation** of why a raw LLM will confidently invent a torque spec, and why grounding it in the client's own documents changes that. Say it out loud twice; cut every hedge that doesn't earn its place | 15 min | The two sentences, submitted referencing `LSN-2.1` |

Carry your tokenizer screenshots and dollar figure forward — they reappear in the cost math of LSN-2.5. Homework tasks 3 and 4 are the raw material for LSN-2.6's expectation-setting drill.

**Time accounting:** pre-work 120 min + homework 120 min = 4 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Karpathy — "Intro to Large Language Models" (video, ~1 h, assigned in full) | exists | [youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g) |
| Karpathy — "Deep Dive into LLMs like ChatGPT" (video, 3 h 31 m) | exists | [youtube.com/watch?v=7xTGNNLPyMI](https://www.youtube.com/watch?v=7xTGNNLPyMI) (chapter timestamps confirmed at delivery prep) |
| Karpathy segment list (one page, with timestamps) | build (lesson-plan work, module build list) — **scope grown:** must now cover the pre-work chapter set *and* the homework chapter set (~90 min of assigned Deep Dive across both), not a 30-min excerpt list | program/materials/ — to create |
| Long-document pack for the lost-in-the-middle experiment (or instructions for sourcing one) | build (light — new, supports relocated homework task 2) | program/materials/ — to create |
| "LLM in five pictures" deck | build (lesson-plan work, module build list) | program/materials/ — to create |
| OpenAI tokenizer playground | exists | [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) |
| Stanford GenAI companion decks | pending | Tyler pulling via academic contacts |

## Delivery Notes

Not yet delivered. Record here: which pre-work segment landed, whether the fabricated-citation demo fired on the first try, and timing reality per segment. Feeds the MOD-2 retro.
