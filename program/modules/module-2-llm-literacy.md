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
| **Week** | 2–3 |
| **Total effort** | ~9 h sessions + ~3.5 h pre-work/homework |
| **Module owner** | Tyler Goble |
| **Prerequisite** | `ASM-1` passed |
| **Checkpoint** | `ASM-2` |

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

| ID | Lesson | Duration | Owner | Format | Material status |
|---|---|---|---|---|---|
| `LSN-2.1` | How LLMs actually work | 1.5 h | Tyler | Live | Curate (Karpathy + Stanford) |
| `LSN-2.2` | Prompting as engineering | 1.5 h | Tyler | Live lab | Exists (`generative_ai/05`, `06` excerpts) |
| `LSN-2.3` | Embeddings & vector search | 1.5 h | Tyler | Live lab | Exists (`foundations/10`) |
| `LSN-2.4` | **Hands-on: build a RAG** | 2 h | Tyler | Live lab | Adapt (**GAP-9**) |
| `LSN-2.5` | Prompt vs RAG vs fine-tune | 1 h | Tyler | Live | Exists partially (`generative_ai/04` as pointer) |
| `LSN-2.6` | Limitations & what to promise a client | 1 h | Tyler | Live | **BUILD — GAP-7** |
| — | `ASM-2` — quiz + whiteboard exercise | 0.5 h | Tyler | Live | **BUILD — GAP-6** |

---

### LSN-2.1 — How LLMs Actually Work

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-2.1` |

**Purpose:** Kill the magic. Tokens, next-token prediction, pretraining vs fine-tuning vs RLHF (RL callback to LSN-1.5), inference and why it costs money, context windows as working memory. Hallucination as a *structural* property, not a bug — the single most important thing to explain to a client.

**Pre-work (~45 min, mandatory):** Curated Karpathy excerpts (specific segments listed in the lesson plan, ~30 min total) + tokenize two sentences in an online tokenizer playground; bring a screenshot.

**Session outline:**
1. Tokens: what the model actually sees — participants' tokenizer screenshots reviewed (20 min)
2. Next-token prediction scaled up: pretraining → fine-tuning → RLHF in one arc (25 min)
3. Context window = working memory: what falls out, and what that means for solution design (20 min)
4. Why it hallucinates and why that's structural; live demo of a confident wrong answer (25 min)

**Homework:** None (heavy pre-work for 2.2).

**Support material:** Curate — Karpathy series segment list + one-page "LLM in five pictures" deck (light build, part of lesson-plan work). Stanford GenAI course as companion (Tyler pulling decks via academic contacts).

---

### LSN-2.2 — Prompting as Engineering

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-2.2` |

**Purpose:** From "typing questions" to engineering: system prompts, few-shot examples, chain-of-thought, structured outputs (JSON), and why the same prompt gives different answers (stochastic — LSN-0.4 callback). This is also the module's on-ramp to tool use, which MOD-3 runs with.

**Pre-work (~30 min):** Run 5 provided prompts against any LLM; note where outputs surprised you.

**Session outline:**
1. Anatomy of a prompt: system vs user, and who controls what (15 min)
2. Few-shot and chain-of-thought: demo on a real extraction task (25 min)
3. Structured outputs: getting JSON you can build on — live lab from `generative_ai/05` (30 min)
4. Failure gallery: prompts that break, and the client conversation about non-determinism (20 min)

**Homework (artifact):** Build a prompt that reliably extracts structured fields from a messy document; submit prompt + 3 outputs.

**Support material:** Exists — `notebooks/generative_ai/05_ChainOfThought_Reasoning.ipynb` + tool-calling teaser from `06`.

---

### LSN-2.3 — Embeddings & Vector Search

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-2.3` |

**Purpose:** The bridge between "LLMs know things" and "LLMs can use *your* things." Text → vectors, similarity as distance, and vector search as the retrieval half of RAG. Clustering callback to LSN-1.1 (embeddings are what make clustering text possible).

**Pre-work (~20 min):** Read the intro of `foundations/10_Embedding_Models.ipynb`.

**Session outline:**
1. Text as coordinates: the map metaphor, similar things near each other (20 min)
2. Live lab: embed 50 sentences, query nearest neighbors, inspect hits and misses (40 min)
3. Where embeddings show up: search, dedup, clustering, recommendation — and RAG next lesson (20 min)
4. Client framing: "semantic search over your documents" without overpromising (10 min)

**Homework:** None (pre-work for the RAG lab instead).

**Support material:** Exists — `notebooks/foundations/10_Embedding_Models.ipynb`.

---

### LSN-2.4 — Hands-On: Build a RAG

| Duration | Owner | Serves |
|---|---|---|
| 2 h (live lab) | Tyler | `OUT-2.4` |

**Purpose:** RAG is basics by Vlad's explicit call — "RAG is here somewhere… it's in basic." Everyone builds the canonical pipeline: chunk → embed → store → retrieve → augment → answer, against a corpus that feels like client work. They leave able to draw this on a whiteboard because they've built it.

**Pre-work (~45 min, mandatory):** LSN-2.3 lab completed; read the guided notebook intro; corpus downloaded.

**Session outline:**
1. The architecture on one slide: why retrieval fixes (some) hallucination (15 min)
2. Guided build: chunking → embeddings → vector store → retrieval (50 min)
3. Augment and answer: watch quality change with k, chunk size, prompt (30 min)
4. Where it breaks: bad chunks, stale corpus, questions the corpus can't answer — honest failure modes (25 min)

**Homework (artifact, graded):** Point the pipeline at a different small corpus; submit notebook + one paragraph on retrieval quality.

**Support material:** Adapt (**GAP-9**) — `notebooks/generative_ai/07_Retrieval_Augmented_Generation.ipynb` reworked with a VSP-shaped corpus (e.g., anonymized meeting notes — the "RAG for meetings" system Vlad referenced is the in-house proof point).

---

### LSN-2.5 — Prompt vs RAG vs Fine-Tune

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-2.5` |

**Purpose:** The commercial judgment call. A decision framework: prompt when knowledge fits in context; RAG when knowledge is yours and changes; fine-tune when it's about *behavior*, not knowledge. Cost and latency as first-class factors — this is a pre-sales differentiator.

**Pre-work (~20 min):** One-page decision-framework read.

**Session outline:**
1. The framework, with the "changes daily vs changes never" axis and the knowledge-vs-behavior axis (20 min)
2. Cost reality: token math for each approach on a concrete workload (20 min)
3. Drill: four client asks, teams pick an approach and defend it (20 min)

**Homework:** None.

**Support material:** Partial — decision framework one-pager to write (folded into lesson-plan work); `generative_ai/04_LoRA_PEFT` as the advanced-tier pointer.

---

### LSN-2.6 — Limitations & What to Promise a Client

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-2.6` |

**Purpose:** The honesty lesson. Hallucination, prompt injection at awareness level, data privacy, evals as "how you know it works" (expanded in MOD-3), and the sentence patterns that set survivable expectations. Directly serves the translation gap: engineers who can say what an LLM *can't* do are the ones clients trust.

**Pre-work (~30 min):** Read two short post-mortems of public LLM failures (curated).

**Session outline:**
1. Failure taxonomy: hallucination, staleness, injection, privacy leaks — one real example each (25 min)
2. "How do you know it works?" — evals at a glance, promising *measured* quality not vibes (20 min)
3. Drill: rewrite three overpromising statements into survivable ones (15 min)

**Homework:** None — checkpoint week.

**Support material:** **BUILD (`GAP-7`)** — failure post-mortem pack + expectation-setting patterns.

---

## Checkpoint — ASM-2

| Field | Value |
|---|---|
| **Format** | Async quiz (~15 scenario questions) **+ whiteboard exercise**: sketch a RAG architecture for a given client scenario and defend two design choices (10 min/participant) |
| **Verifies** | `OUT-2.1`–`OUT-2.3`, `OUT-2.5`, `OUT-2.6` (quiz); `OUT-2.4` (whiteboard + LSN-2.4 artifact) |
| **Pass bar** | Quiz 80% + whiteboard rubric "client-ready" |
| **Gate** | Must pass to start `MOD-3` |
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

| ID | Item | Owner | Needed by |
|---|---|---|---|
| `GAP-9` | RAG lab with VSP-shaped corpus (adapt `generative_ai/07`) | Tyler | Week 3 |
| `GAP-7` | Limitations lesson: failure pack + expectation patterns | Tyler | Week 3 |
| `GAP-6` (share) | ASM-2 quiz + whiteboard rubric | Tyler | End of Week 3 |
| — | Karpathy segment list + "LLM in five pictures" + decision one-pager | Tyler | Week 2 (lesson-plan work, LSN-2.1/2.5) |
