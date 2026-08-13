---
name: LSN-2.3-embeddings-vector-search
description: Explain embeddings and vector search, run a nearest-neighbor search yourself, and identify where semantic search fits in a solution.
module: MOD-2
delivery_date: 2026-11-02
serves: OUT-2.3
duration: 1
prework_time: 95
homework_time: 145
owner: Tyler
status: draft
---

# LSN-2.3 — Embeddings & Vector Search

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.3 |
| **Duration** | 1 h live + 4 h out-of-session (pre-work + homework) |
| **Format** | Live lab |
| **Verified by** | ASM-2 (quiz) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 2 November 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 4 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

## Narrative

The bridge between "LLMs know things" and "LLMs can use *your* things." The misconception to kill: search means keywords. The capability to install: text becomes coordinates, similarity becomes distance, and nearest-neighbor lookup becomes the retrieval half of RAG (built in full next lesson). Callback to LSN-1.1: embeddings are the representation that made clustering text possible — the lab closes the loop by recovering the ticket clusters with k-means. The lab's scripted miss teaches the limit that matters most for RAG: embeddings capture topic, not polarity.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the intro of `foundations/10_Embedding_Models.ipynb` — sections "What are Embeddings?", "Key Concepts", "Why Use Embeddings?", "When to Use Embeddings" — taking notes, not skimming | 25 min | Nothing — quizzed cold at session start |
| 2 | **Run the notebook's setup and first embedding cells so the sentence-transformers model is downloaded and cached on your machine.** Non-negotiable: the 2.4 runbook's most likely failure is a model download stalling on office Wi-Fi, and this is where we pre-empt it | 30 min | The printed embedding shape from your own machine |
| 3 | **Cosine similarity by hand.** Given `a = [1, 0, 1]`, `b = [1, 1, 0]`, `c = [2, 0, 2]`, compute all three pairwise cosine similarities on paper. Which pair is identical in direction despite different magnitudes, and why does that matter for text? | 15 min | Your three numbers and the one-line answer |
| 4 | Read the **"where embeddings show up" catalogue** one-pager — search, dedup, clustering, recommendation, classification-by-neighbour, retrieval for RAG. *(Relocated: this was live segment 3; reading it beforehand turns that segment into a 10-min discussion of where it fits **our** work.)* | 20 min | One line: which of the six you have personally needed at VSP |
| 5 | Write one sentence naming a document set from your current project (or 6MAP) you would want semantic search over | 5 min | The sentence |

**Time accounting (pre-work):** 25 + 30 + 15 + 20 + 5 = 95 min.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Text as coordinates | 12 min | talk | The map metaphor: similar meanings land near each other; similarity = cosine distance; dimensions are learned, not human-labeled. Pre-work task 3's hand-computed numbers make "direction, not magnitude" concrete in seconds. LSN-1.1 callback: this is what unlocked clustering for text. |
| Live lab: 50 sentences | 30 min | lab | Embed the 50-ticket set (below) — models already cached in pre-work task 2, so the room starts at the interesting part. Checkpoints: (1) embedding matrix shape prints (50, d); (2) scripted queries Q1–Q2 return the expected hits; (3) **scripted miss Q3 discussed at length — topic ≠ polarity.** Q3 is the segment's real payload and stays live: it needs the room's argument to land. |
| Where embeddings show up | 10 min | discussion | Catalogue was read in pre-work task 4; here we only place it in *our* work. Locate embeddings inside the in-production meeting-RAG pipeline: they are the index, not the answer. Two or three participants name the use they've personally needed. |
| Client framing | 8 min | drill | Each participant says "semantic search over your documents" in ≤3 client-safe sentences that survive the polarity caveat — no "it understands your documents", no "always finds the right answer". Fast round, one pass each; the written version is homework. |

**Timing check:** 12 + 30 + 10 + 8 = 60 min = 1 h — matches the spreadsheet contract.

**What moved out of the live hour (1.5 h → 1 h):** lab checkpoint 4 (k-means cluster recovery, the LSN-1.1 callback) → homework task 1, where it gets 35 min instead of a rushed 10; the where-embeddings-show-up catalogue → pre-work task 4; model download/caching → pre-work task 2. The Q3 polarity miss deliberately stayed live. Nothing was dropped.

**The 50-sentence set — IT service-desk tickets**, 5 intended clusters × 10 sentences, shipped as CSV: account/password lockouts; VPN & network; printers & peripherals; software installs & licensing; email & calendar.

**Scripted queries and expected results:**
- **Q1 (semantic hit):** `I can't get into my account since this morning` → expected top hits from the lockout cluster: "Locked out after three failed password attempts", "Password expired and the reset link does nothing", "Can't sign in to the portal" — note the near-zero keyword overlap with the first hit; that's the point.
- **Q2 (routine hit):** `New starter needs Office installed` → installs/licensing cluster.
- **Q3 (the instructive miss):** `VPN is working again, you can close my ticket` → top hits are the *broken*-VPN tickets ("VPN drops every 20 minutes", "Can't connect to VPN from home"). Embeddings encode topic, not status or negation — resolved and broken look alike. Consequence spelled out: in a RAG system, retrieval can hand the generator a wrong-status document. This exact miss is revisited in LSN-2.4's failure segment.

## Client Tie-In (Dorel's rule)

The meeting-RAG system in production retrieves by embedding similarity over our own meeting notes — this lab is its retrieval half at toy scale. And the closing drill is a direct 6MAP translation-gap fix: "semantic search over your documents" said precisely, with its known limit (topic, not truth or status), is a sentence a senior can safely say in pre-sales.

## Homework

Your notebook must run end-to-end (embeddings + nearest-neighbour query) before LSN-2.4 — the weekly cadence gives you the full week. Bring a screenshot of your Q1 results as proof of completion.

| # | Task | Time | Deliverable |
|---|---|---|---|
| 1 | **Cluster recovery** (relocated from live checkpoint 4). Run k-means with k=5 on your 50-ticket embeddings. Build a table of intended cluster vs assigned cluster, then write a paragraph on which clusters merged or split and why — LSN-1.1's clustering lesson, now runnable on text | 35 min | The table + the paragraph |
| 2 | **Your own corpus.** Take the document set you named in pre-work task 5 and embed 30–50 sentences from it (anonymise anything client-identifying). Run three queries: one you expect to hit, one you expect to miss, and one status/polarity query in the shape of Q3 | 45 min | Notebook + your three queries with top-3 results and a verdict on each |
| 3 | **Chunk-granularity preview.** Re-embed your own set twice — once per sentence, once per paragraph — and compare top-3 results for the same query. Which granularity retrieved better, and what did the coarser one bury? This is the chunk-size decision you will make for real in LSN-2.4 | 30 min | Side-by-side top-3 comparison + one sentence of reasoning |
| 4 | **Model comparison.** Run one query against two different embedding models from `foundations/10`. Does the ranking change? Does the *winner* change? | 20 min | The two rankings + one line on whether model choice mattered here |
| 5 | Write out the **client framing** from the live drill in ≤3 sentences, with the polarity caveat stated as a strength ("here's what it won't do, and here's how we catch it") | 15 min | The sentences, submitted referencing `LSN-2.3` |

**Time accounting:** pre-work 95 min + homework 145 min = 4 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Embeddings notebook (sections: "What are Embeddings?" → "When to Use Embeddings", plus implementation) | exists | notebooks/foundations/10_Embedding_Models.ipynb |
| 50-ticket sentence set (CSV, 5×10 clusters as specced above) | build (light — write from spec above) | program/materials/ — to create |
| Lab notebook: embed → query → k-means (adapts foundations/10) | adapt — **scope changed:** the k-means stage and the own-corpus/granularity/model-comparison stages now run **solo out of session**, so the notebook needs its own guidance and self-checks for those cells (a bring-your-own-corpus loader cell, expected-shape asserts, and a "what good looks like" note per homework task) rather than relying on the instructor being present | notebooks/foundations/10_Embedding_Models.ipynb — trim to lab flow |
| "Where embeddings show up" catalogue one-pager | build (light — **new**, carries relocated live segment 3 into pre-work) | program/materials/ — to create |
| Supplement — embedding-model selection axes and the sparse/dense/hybrid contrast (explains the scripted polarity miss) | supplement | [`program/sources/SUP-5-rag-optimization-ladder.md`](../sources/SUP-5-rag-optimization-ladder.md) knobs 4–5 |

## Delivery Notes

Not yet delivered. Record here: whether Q3's miss reproduced with the chosen model, how many arrived with the model actually cached (pre-work task 2 — this is the LSN-2.4 risk), k-means cluster recovery quality from the homework returns, timing reality. Feeds the MOD-2 retro.
