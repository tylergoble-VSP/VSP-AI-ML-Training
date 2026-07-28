---
name: LSN-2.4-hands-on-build-a-rag
description: Build the canonical RAG pipeline end-to-end against a VSP-shaped corpus; sketch and defend the architecture on a whiteboard afterward.
module: MOD-2
serves: OUT-2.4
duration: 2 h
prework_time: 45
owner: Tyler
status: draft
---

# LSN-2.4 — Hands-On: Build a RAG

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.4 |
| **Duration** | 2 h session + 45 min pre-work |
| **Format** | Live lab |
| **Verified by** | ASM-2 (whiteboard + artifact) |

## Narrative

RAG is basics by Vlad's explicit call ("RAG is here somewhere… it's in basic"). Everyone builds the canonical pipeline — chunk → embed → store → retrieve → augment → answer — with their own hands, against a corpus that feels like client work: anonymized meeting notes, because the in-production meeting-RAG system is our in-house proof point. Builds directly on LSN-2.3 (the retrieval half is already in their notebook). They leave able to draw and defend this on a whiteboard because they built it and watched it break.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | LSN-2.3 lab notebook complete and running (embed + nearest-neighbor query) | — (done in 2.3) | Screenshot of your Q1 query results |
| 2 | Read the guided notebook intro — sections "What is RAG?", "RAG Pipeline", "Document Chunking Strategies", "Retrieval Methods" | 25 min | Nothing — quizzed cold at session start |
| 3 | Download the meeting-notes corpus pack; run the setup cell; confirm `len(docs) == 12` prints | 20 min | The printed confirmation in your notebook |

**Corpus (GAP-9):** 12 anonymized VSP-style meeting notes (clients → "Client A/B", people → roles). Contents engineered for the lab: kickoffs, status calls, action items with owners, and one architecture decision that is **reversed in a later meeting** — deliberately, for the staleness demo in segment 4. ~40 pages → ~150 chunks at default settings.

## Session Plan

Runbook format — each lab segment lists checkpoint state, likely failure, and recovery.

| Segment | Time | Method | Detail |
|---|---|---|---|
| The architecture on one slide | 15 min | talk | Chunk → embed → store → retrieve → augment → answer. Why retrieval fixes *some* hallucination: the model generates from evidence in context instead of from its weights. What it doesn't fix (segment 4). **Checkpoint:** cold-call two people to name the six stages unprompted. |
| Guided build: chunk → embed → store → retrieve | 50 min | lab | **CP1 (+10 min):** corpus chunked — ~150 chunks at size 500 / overlap 50. *Likely failure:* path/encoding errors, missing deps. *Recovery:* pre-baked `chunks.json` in the lab repo — load it and keep moving. **CP2 (+25):** all chunks embedded locally (same sentence-transformers model as 2.3); matrix shape prints. *Likely failure:* model download stalls on office Wi-Fi. *Recovery:* model cache shared in pre-work; else load the pre-computed `embeddings.npy`. **CP3 (+40):** index built; smoke query "Who owns the follow-up on the Client A pilot?" returns the action-item chunk in top-3. *Likely failure:* every query returns the same attendee-list/header chunk — boilerplate dominates similarity. *Recovery:* strip headers, re-chunk, re-embed — say out loud that this **is** the lesson: retrieval quality is a data-cleaning problem. **CP4 (+50):** everyone's `retrieve(query, k)` returns (chunk, score) pairs — all green before moving on. |
| Augment and answer | 30 min | lab | Wire top-k chunks into the prompt. Grid: k ∈ {1, 3, 8} × chunk size {200, 500, 1000} × prompt with/without "Answer only from the provided context; if the answer is not there, say so." **Checkpoint:** a filled comparison table for one question. *Likely failure A:* model answers from world knowledge, ignoring context → *recovery:* add the grounding instruction, show the before/after diff. *Likely failure B:* k=8 × 1000-char chunks degrades or overflows — the context window is working memory (LSN-2.1 callback) → *recovery:* drop k, note the trade-off in the table. |
| Where it breaks — honest failure modes | 25 min | demo + discussion | Three scripted breaks: **(a) bad chunks** — a mid-sentence split produces a garbage citation; **(b) stale corpus** — ask about the reversed architecture decision with and without the later meeting's doc in the index: confident, outdated answer vs corrected answer; **(c) unanswerable question** — the corpus can't answer; watch retrieval + confabulation blend, then fix with the "say so" instruction. Revisit 2.3's polarity miss as a retrieval hazard. Close: one volunteer draws the pipeline cold on the whiteboard — ASM-2 rehearsal. |

**Timing check:** 15 + 50 + 30 + 25 = 120 min = 2 h ✓

## Client Tie-In (Dorel's rule)

The corpus is our own work, anonymized: the meeting-RAG system running in production is the proof point participants can cite in pre-sales — "we run this on our own meetings; here is how it's built, and here is where it breaks." A senior who has personally hit the boilerplate-chunk failure and the stale-corpus failure can answer the two questions every prospect asks: "why won't it just make things up?" and "what happens when our documents change?"

## Homework

**Artifact (graded, submit referencing LSN-2.4):** re-point the pipeline at a different small corpus — your own project docs (anonymized) or the provided fallback pack. Submit the notebook + one paragraph on retrieval quality: one query it handled well, one concrete miss, and the single change you'd make first. Grading standard: pipeline runs end-to-end; the paragraph names a real miss and a plausible fix (not "it worked great"). This artifact plus the ASM-2 whiteboard exercise verify OUT-2.4.

## Materials

| Material | Status | Path / source |
|---|---|---|
| RAG notebook (sections: "What is RAG?", "RAG Pipeline", "Document Chunking Strategies", "Retrieval Methods", "Implementation") | adapt (**GAP-9**) | notebooks/generative_ai/07_GenerativeAI_Retrieval_Augmented_Generation.ipynb |
| Meeting-notes corpus pack (12 docs, anonymized, reversal doc included) | build (**GAP-9**) | program/materials/ — to create |
| Recovery assets: `chunks.json`, `embeddings.npy`, model cache | build (**GAP-9**, with corpus) | lab repo — to create |
| Architecture one-slide | build (light — from "LLM in five pictures" style) | program/materials/ — to create |

## Delivery Notes

Not yet delivered. Record here: CP pass rates and times, which scripted break landed hardest, whether 50 min sufficed for the guided build. Feeds the MOD-2 retro and the GAP-9 close-out.
