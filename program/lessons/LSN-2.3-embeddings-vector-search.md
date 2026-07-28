---
name: LSN-2.3-embeddings-vector-search
description: Explain embeddings and vector search, run a nearest-neighbor search yourself, and identify where semantic search fits in a solution.
module: MOD-2
serves: OUT-2.3
duration: 1.5 h
prework_time: 20
owner: Tyler
status: draft
---

# LSN-2.3 — Embeddings & Vector Search

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.3 |
| **Duration** | 1.5 h session + 20 min pre-work |
| **Format** | Live lab |
| **Verified by** | ASM-2 (quiz) |

## Narrative

The bridge between "LLMs know things" and "LLMs can use *your* things." The misconception to kill: search means keywords. The capability to install: text becomes coordinates, similarity becomes distance, and nearest-neighbor lookup becomes the retrieval half of RAG (built in full next lesson). Callback to LSN-1.1: embeddings are the representation that made clustering text possible — the lab closes the loop by recovering the ticket clusters with k-means. The lab's scripted miss teaches the limit that matters most for RAG: embeddings capture topic, not polarity.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the intro of `foundations/10_Embedding_Models.ipynb` — sections "What are Embeddings?", "Key Concepts", "Why Use Embeddings?", "When to Use Embeddings" | 15 min | Nothing — quizzed cold at session start |
| 2 | Write one sentence naming a document set from your current project (or 6MAP) you would want semantic search over | 5 min | The sentence |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Text as coordinates | 20 min | talk | The map metaphor: similar meanings land near each other; similarity = cosine distance; dimensions are learned, not human-labeled. LSN-1.1 callback: this is what unlocked clustering for text. Cold-check three pre-work sentences aloud. |
| Live lab: 50 sentences | 40 min | lab | Embed the 50-ticket set (below) with a local sentence-transformers model. Checkpoints: (1) embedding matrix shape prints (50, d); (2) scripted queries Q1–Q2 return the expected hits; (3) scripted miss Q3 discussed — topic ≠ polarity; (4) k-means with k=5 recovers the five ticket clusters (LSN-1.1 callback made runnable). |
| Where embeddings show up | 20 min | talk + discussion | Search, dedup, clustering, recommendation, classification-by-neighbor — and retrieval for RAG, next lesson. Locate embeddings inside the in-production meeting-RAG pipeline: they are the index, not the answer. |
| Client framing | 10 min | drill | Each participant says "semantic search over your documents" in ≤3 client-safe sentences that survive the polarity caveat — no "it understands your documents", no "always finds the right answer". |

**Timing check:** 20 + 40 + 20 + 10 = 90 min = 1.5 h ✓

**The 50-sentence set — IT service-desk tickets**, 5 intended clusters × 10 sentences, shipped as CSV: account/password lockouts; VPN & network; printers & peripherals; software installs & licensing; email & calendar.

**Scripted queries and expected results:**
- **Q1 (semantic hit):** `I can't get into my account since this morning` → expected top hits from the lockout cluster: "Locked out after three failed password attempts", "Password expired and the reset link does nothing", "Can't sign in to the portal" — note the near-zero keyword overlap with the first hit; that's the point.
- **Q2 (routine hit):** `New starter needs Office installed` → installs/licensing cluster.
- **Q3 (the instructive miss):** `VPN is working again, you can close my ticket` → top hits are the *broken*-VPN tickets ("VPN drops every 20 minutes", "Can't connect to VPN from home"). Embeddings encode topic, not status or negation — resolved and broken look alike. Consequence spelled out: in a RAG system, retrieval can hand the generator a wrong-status document. This exact miss is revisited in LSN-2.4's failure segment.

## Client Tie-In (Dorel's rule)

The meeting-RAG system in production retrieves by embedding similarity over our own meeting notes — this lab is its retrieval half at toy scale. And the closing drill is a direct 6MAP translation-gap fix: "semantic search over your documents" said precisely, with its known limit (topic, not truth or status), is a sentence a senior can safely say in pre-sales.

## Homework

None — this lab **is** the pre-work for LSN-2.4: your notebook must run end-to-end (embeddings + nearest-neighbor query) before the RAG session. Bring a screenshot of your Q1 results as proof of completion.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Embeddings notebook (sections: "What are Embeddings?" → "When to Use Embeddings", plus implementation) | exists | notebooks/foundations/10_Embedding_Models.ipynb |
| 50-ticket sentence set (CSV, 5×10 clusters as specced above) | build (light — write from spec above) | program/materials/ — to create |
| Lab notebook: embed → query → k-means (adapts foundations/10) | adapt | notebooks/foundations/10_Embedding_Models.ipynb — trim to lab flow |

## Delivery Notes

Not yet delivered. Record here: whether Q3's miss reproduced with the chosen model, k-means cluster recovery quality, timing reality. Feeds the MOD-2 retro.
