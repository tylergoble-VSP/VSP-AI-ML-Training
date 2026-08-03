---
name: module-2-llm-literacy
description: LLM literacy — how LLMs actually work, deliberate prompting, embeddings, a hands-on RAG build, prompt-vs-RAG-vs-fine-tune judgment, and honest client expectations.
---

# MOD-2 — LLM Literacy

## Module Configuration

| Field | Value |
|---|---|
| **ID** | `MOD-2` |
| **Tier** | Basics |
| **Pillar** | LLM |
| **Schedule** | 19 Oct – 23 Nov 2026 — six weekly Monday sessions (program spreadsheet, locked 2026-08-03) |
| **Per lesson** | 1 h live + 4 h out-of-session (pre-work + homework combined) |
| **Total effort** | 6 h live + 24 h out-of-session = **30 h** — the program's heaviest module by design: the spreadsheet gives MOD-2 double the out-of-session budget of the other modules, weighting LLM fundamentals hardest |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC — spreadsheet says "Mazilu?") |
| **Module owner** | Tyler Goble |
| **Prerequisite** | `ASM-1` passed |
| **Checkpoint** | `ASM-2` — **not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Nov 23–27, after LSN-2.6** |

## Purpose

GOAL-2: "talk to the customer about LLM-based solutions and look intelligent." The module takes participants from consumer-level ChatGPT familiarity to practitioner-level understanding: what a token is, why context windows matter, what embeddings buy you, how RAG actually works (they build one), and — commercially decisive — when to prompt vs RAG vs fine-tune and what to honestly promise a client. RAG is a basics-level topic by Vlad's explicit call; graph-RAG variants are deferred to advanced.

The Karpathy "build an LLM from scratch" series is this module's spirit reference — "I don't want that, but I want the spirit of that" (Vlad): mechanics shown honestly, curated to fit.

## Outcomes

| ID | After MOD-2 you can… | Serves |
|---|---|---|
| `OUT-2.1` | Explain how an LLM works — tokens, training vs inference, why it hallucinates — without hand-waving | GOAL-2, GOAL-4 |
| `OUT-2.2` | Prompt deliberately: system prompts, few-shot, chain-of-thought, structured outputs | GOAL-2, GOAL-6 |
| `OUT-2.3` | Explain embeddings and vector search, and identify where they fit in a solution | GOAL-2, GOAL-4 |
| `OUT-2.4` | Sketch and defend a RAG architecture on a whiteboard; you have personally built one | GOAL-2, GOAL-3, GOAL-6 |
| `OUT-2.5` | Choose prompt vs RAG vs fine-tune for a given ask, with cost/latency reasoning | GOAL-2, GOAL-4 |
| `OUT-2.6` | State LLM limitations honestly and set client expectations that survive production | GOAL-2, GOAL-4 |

## Lesson Inventory

All six lessons run the same spreadsheet contract: **1 h live + 4 h out-of-session**, presenter Tyler, reviewer Vlad, guinea pig Mazilu (TBC).

| ID | Lesson | Date (Monday) | Duration | Format | Material status |
|---|---|---|---|---|---|
| `LSN-2.1` | How LLMs actually work | 19 Oct 2026 | 1 h live + 4 h out | Live | Curate (Karpathy + Stanford) |
| `LSN-2.2` | Prompting as engineering | 26 Oct 2026 | 1 h live + 4 h out | Live lab | Exists (`generative_ai/05`, `06` excerpts) |
| `LSN-2.3` | Embeddings & vector search | 2 Nov 2026 | 1 h live + 4 h out | Live lab | Exists (`foundations/10`) |
| `LSN-2.4` | **Hands-on: build a RAG** | 9 Nov 2026 | 1 h live + 4 h out | Live lab | Adapt (**GAP-9**, scope changed — see build list) |
| `LSN-2.5` | Prompt vs RAG vs fine-tune | 16 Nov 2026 | 1 h live + 4 h out | Live | Exists partially (`generative_ai/04` as pointer) |
| `LSN-2.6` | Limitations & what to promise a client | 23 Nov 2026 | 1 h live + 4 h out | Live | **BUILD — GAP-7** (scope grown — see build list) |
| — | `ASM-2` — quiz + whiteboard exercise | *unscheduled* | 0.5 h | Live | **BUILD — GAP-6** |

**Spreadsheet title aliases** (spreadsheet wording ≠ repo wording; same lesson, no renumbering): "Embeddings and Vector Search" = LSN-2.3 (`&` in repo); "Hands on Build a RAG" = LSN-2.4 ("Hands-On: Build a RAG"); "Prompt vs RAG vs Fine Tune" = LSN-2.5 (hyphenated in repo); **"Limitations of Large Language Models" = LSN-2.6 ("Limitations & What to Promise a Client")** — the repo title names the commercial half, which is where the hour actually spends its time.

---

### LSN-2.1 — How LLMs Actually Work

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 19 Oct 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.1` |

**Purpose:** Kill the magic. Tokens, next-token prediction, pretraining vs fine-tuning vs RLHF (RL callback to LSN-1.5), inference and why it costs money, context windows as working memory. Hallucination as a *structural* property, not a bug — the single most important thing to explain to a client.

**Pre-work (120 min, mandatory):** Karpathy ["Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g) in full (60 min) + the tokenization/inference chapters of ["Deep Dive into LLMs like ChatGPT"](https://www.youtube.com/watch?v=7xTGNNLPyMI) (40 min) + a four-sentence tokenizer-playground exercise with token counts and a cost estimate (20 min). The 4 h budget makes the full 1 h talk assignable rather than excerpted — on-mission, since this is the module's spirit reference.

**Session outline (60 min):**
1. Tokens: what the model actually sees — two participant screenshots on screen (10 min)
2. Next-token prediction scaled up: pretraining → fine-tuning → RLHF in one arc (20 min)
3. Context window = working memory: what falls out, and what that means for solution design (10 min)
4. Why it hallucinates and why that's structural; live demo of a confident wrong answer (20 min)

**Homework (120 min):** Karpathy Deep Dive post-training + hallucination/working-memory chapters (50 min); the "lost in the middle" position experiment, relocated out of the live hour (30 min); a self-run hallucination hunt in your own domain testing which mitigations actually work (25 min); write and rehearse the two-sentence client explanation (15 min).

**Support material:** Curate — Karpathy series segment list + one-page "LLM in five pictures" deck (light build, part of lesson-plan work). Stanford GenAI course as companion (Tyler pulling decks via academic contacts).

---

### LSN-2.2 — Prompting as Engineering

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 26 Oct 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.2` |

**Purpose:** From "typing questions" to engineering: system prompts, few-shot examples, chain-of-thought, structured outputs (JSON), and why the same prompt gives different answers (stochastic — LSN-0.4 callback). This is also the module's on-ramp to tool use, which MOD-3 runs with.

**Pre-work (110 min):** Run the 5 provided prompts and note the surprises (30 min); read *and run* the chain-of-thought notebook sections — CoT theory relocated out of the live hour (45 min); a self-consistency mini-experiment, five runs and a majority vote (20 min); read the tool-calling intro, the MOD-3 bridge relocated from the live close (15 min).

**Session outline (60 min):**
1. Anatomy of a prompt: system vs user, and who controls what (10 min)
2. Few-shot and chain-of-thought: pre-work debrief on a real extraction task (15 min)
3. Structured outputs: getting JSON you can build on — live lab from `generative_ai/05` (20 min)
4. Failure gallery: prompts that break, and the client conversation about non-determinism (15 min)

**Homework (130 min, artifact graded):** Build a prompt that reliably extracts structured fields from a messy document — now **5** consecutive runs, schema-first (60 min); harden it against format drift with validate-and-retry on a longer input (30 min); a few-shot-bleed test with neutral placeholder examples (25 min); write the client sentence on non-determinism (15 min).

**Support material:** Exists — `notebooks/generative_ai/05_GenerativeAI_ChainOfThought_Reasoning.ipynb` + tool-calling teaser from `06`.

---

### LSN-2.3 — Embeddings & Vector Search

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 2 Nov 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.3` |

**Purpose:** The bridge between "LLMs know things" and "LLMs can use *your* things." Text → vectors, similarity as distance, and vector search as the retrieval half of RAG. Clustering callback to LSN-1.1 (embeddings are what make clustering text possible).

**Pre-work (95 min):** Read the `foundations/10_Embedding_Models.ipynb` intro sections (25 min); run setup so the sentence-transformers model is **cached before the room** — this pre-empts the Wi-Fi stall in 2.4's runbook (30 min); compute cosine similarity by hand on two 3-d vectors (15 min); read the "where embeddings show up" catalogue, relocated out of the live hour (20 min); name a document set you'd want semantic search over (5 min).

**Session outline (60 min):**
1. Text as coordinates: the map metaphor, similar things near each other (12 min)
2. Live lab: embed 50 sentences, query nearest neighbors, inspect hits and the scripted polarity miss (30 min)
3. Where embeddings show up: search, dedup, clustering, recommendation — and RAG next lesson (10 min)
4. Client framing: "semantic search over your documents" without overpromising (8 min)

**Homework (145 min):** k-means cluster recovery, relocated from the live lab's final checkpoint (35 min); embed your **own** 30–50 sentences and run hit/miss/polarity queries (45 min); sentence-level vs paragraph-level re-embedding, which previews 2.4's chunking decision (30 min); two-model ranking comparison (20 min); the client-framing pitch written out (15 min). The 2.3 notebook must run end-to-end before 2.4 — weekly cadence gives the week to do it.

**Support material:** Exists — `notebooks/foundations/10_Embedding_Models.ipynb`.

---

### LSN-2.4 — Hands-On: Build a RAG

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 9 Nov 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.4` |

**Purpose:** RAG is basics by Vlad's explicit call — "RAG is here somewhere… it's in basic." Everyone builds the canonical pipeline: chunk → embed → store → retrieve → augment → answer, against a corpus that feels like client work. They leave able to draw this on a whiteboard because they've built it.

**Restructure note (2 h → 1 h):** the solo build stages move to pre-work; the live hour keeps only what needs a room — **unblocking**, getting the pipeline answering end-to-end for *everyone*, and the three scripted failure demos. The build itself does not shrink; it moves.

**Pre-work (150 min, mandatory):** LSN-2.3 notebook running; read the guided notebook's four intro sections (25 min); corpus pack downloaded and verified (15 min); then **four solo build stages with self-verifying checkpoints** — chunk (25 min), embed (25 min), index + smoke query with the header-stripping fix if boilerplate dominates (35 min), `retrieve(query, k)` returning (chunk, score) pairs (25 min). PASS/FAIL summary posted to the pre-session thread so Tyler knows who to unblock.

**Session outline (60 min):**
1. The architecture on one slide: why retrieval fixes (some) hallucination; cold-call the six stages (8 min)
2. Unblock and green-light: every pre-work pipeline verified live, recovery assets deployed (17 min)
3. Augment and answer together: top-k into the prompt, grounding instruction before/after (15 min)
4. Where it breaks: bad chunks, stale corpus, questions the corpus can't answer — three scripted demos (15 min)
5. Whiteboard rehearsal: one volunteer draws the pipeline cold — ASM-2 rehearsal (5 min)

**Homework (90 min, artifact graded):** the k × chunk-size × grounding-instruction grid, relocated from the live hour (45 min); re-point the pipeline at a different small corpus and submit notebook + one paragraph on retrieval quality (45 min).

**Support material:** Adapt (**GAP-9**) — `notebooks/generative_ai/07_GenerativeAI_Retrieval_Augmented_Generation.ipynb` reworked with a VSP-shaped corpus (e.g., anonymized meeting notes — the "RAG for meetings" system Vlad referenced is the in-house proof point).

---

### LSN-2.5 — Prompt vs RAG vs Fine-Tune

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 16 Nov 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.5` |

**Purpose:** The commercial judgment call. A decision framework: prompt when knowledge fits in context; RAG when knowledge is yours and changes; fine-tune when it's about *behavior*, not knowledge. Cost and latency as first-class factors — this is a pre-sales differentiator.

**Pre-work (80 min):** Decision-framework one-pager (15 min); place one real ask on the 2×2 (5 min); recompute the worked cost example against **current published vendor prices** for two models, so the room runs on live numbers (30 min); read the LoRA/PEFT notebook intro only — enough to know what you're declining, not to build it (30 min).

**Session outline (60 min — unchanged, already on contract):**
1. The framework, with the "changes daily vs changes never" axis and the knowledge-vs-behavior axis (20 min)
2. Cost reality: token math for each approach on a concrete workload (20 min)
3. Drill: four client asks, teams pick an approach and defend it (20 min)

**Homework (160 min):** a one-page decision memo on a real prospect ask, graded (60 min); build a reusable prompt-vs-RAG cost calculator validated against the lesson's worked example (40 min); run the four client asks past an LLM and grade *its* recommendations against the framework (25 min); rehearse a 3-minute spoken defense (20 min); file the one-pager and calculator into your pre-sales kit and self-check OUT-2.1–2.5 (15 min).

**Support material:** Partial — decision framework one-pager to write (folded into lesson-plan work); `generative_ai/04_LoRA_PEFT` as the advanced-tier pointer.

---

### LSN-2.6 — Limitations & What to Promise a Client

*(Spreadsheet title: "Limitations of Large Language Models".)*

| Date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 23 Nov 2026 | 1 h live + 4 h out-of-session | Tyler | `OUT-2.6` |

**Purpose:** The honesty lesson. Hallucination, prompt injection at awareness level, data privacy, evals as "how you know it works" (expanded in MOD-3), and the sentence patterns that set survivable expectations. Directly serves the translation gap: engineers who can say what an LLM *can't* do are the ones clients trust.

**Pre-work (90 min):** the two post-mortems (30 min); a third case on indirect prompt injection and a privacy/data-boundary one-pager — both new to the GAP-7 pack (35 min); run one hidden-instruction injection test yourself, because recognition is this lesson's stated job (25 min).

**Session outline (60 min — unchanged, already on contract):**
1. Failure taxonomy: hallucination, staleness, injection, privacy leaks — one real example each (25 min)
2. "How do you know it works?" — evals at a glance, promising *measured* quality not vibes (20 min)
3. Drill: rewrite three overpromising statements into survivable ones (15 min)

**Homework (150 min):** build a **20-question golden eval set** against your LSN-2.4 corpus (15 answerable, 5 deliberately unanswerable), run it, and report the score — this turns "measured quality, not vibes" from a slogan into a number you own (60 min); rewrite five overpromising statements from your own past decks (30 min); two timed cold ASM-2 whiteboard rehearsals (30 min); module self-check across OUT-2.1–2.6 (30 min).

**Support material:** **BUILD (`GAP-7`)** — failure post-mortem pack (now four cases, not two) + expectation-setting patterns + golden-question eval template.

---

## Checkpoint — ASM-2

| Field | Value |
|---|---|
| **Format** | Async quiz (~15 scenario questions) **+ whiteboard exercise**: sketch a RAG architecture for a given client scenario and defend two design choices (10 min/participant) |
| **Verifies** | `OUT-2.1`–`OUT-2.3`, `OUT-2.5`, `OUT-2.6` (quiz); `OUT-2.4` (whiteboard + LSN-2.4 artifact) |
| **Pass bar** | Quiz 80% + whiteboard rubric "client-ready" |
| **Gate** | Must pass to start `MOD-3` |
| **Scheduling** | **Not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Nov 23–27, after LSN-2.6.** The LSN-2.6 homework already contains two timed whiteboard rehearsals, so the slot only needs the 0.5 h assessment itself |
| **Status** | **BUILD — GAP-6** |

## Traceability

| Outcome | Served by | Verified by |
|---|---|---|
| `OUT-2.1` | LSN-2.1 | ASM-2 (quiz) |
| `OUT-2.2` | LSN-2.2 | ASM-2 (quiz + artifact) |
| `OUT-2.3` | LSN-2.3 | ASM-2 (quiz) |
| `OUT-2.4` | LSN-2.4 | ASM-2 (whiteboard + artifact) |
| `OUT-2.5` | LSN-2.5 | ASM-2 (quiz) |
| `OUT-2.6` | LSN-2.6 | ASM-2 (quiz) |

## Build List

Needed-by dates are **pre-work ship dates**, not session dates: with a 4 h out-of-session budget, participants start a week before the room.

| ID | Item | Owner | Needed by |
|---|---|---|---|
| `GAP-9` | RAG lab with VSP-shaped corpus (adapt `generative_ai/07`) — **scope changed by the 2 h → 1 h cut:** the chunk/embed/index/retrieve stages are now **solo pre-work**, so the notebook needs self-verifying PASS/FAIL checkpoint cells, inline recovery assets (`chunks.json`, `embeddings.npy`, shared model cache) and a troubleshooting appendix that works without an instructor in the room. Same content, higher build bar | Tyler | **2 Nov 2026** (a week before the 9 Nov session — pre-work now contains the build) |
| `GAP-7` | Limitations lesson: failure pack + expectation patterns — **scope grown:** post-mortem pack goes from two cases to four (adds indirect prompt injection + a privacy/data-boundary case), plus a golden-question eval template for the new 60-min eval homework | Tyler | **16 Nov 2026** |
| `GAP-6` (share) | ASM-2 quiz + whiteboard rubric | Tyler | End of Nov 2026 (slot TBC — not on the spreadsheet) |
| — | Karpathy segment list + "LLM in five pictures" + decision one-pager + "where embeddings show up" catalogue (new — relocated out of LSN-2.3's live hour) | Tyler | 12 Oct 2026 onward (lesson-plan work, LSN-2.1/2.3/2.5) |
