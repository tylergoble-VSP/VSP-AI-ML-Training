---
name: LSN-2.4-hands-on-build-a-rag
description: Build the canonical RAG pipeline end-to-end against a VSP-shaped corpus; sketch and defend the architecture on a whiteboard afterward.
module: MOD-2
delivery_date: 2026-11-09
serves: OUT-2.4
duration: 1
prework_time: 150
homework_time: 90
owner: Tyler
status: draft
---

# LSN-2.4 — Hands-On: Build a RAG

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.4 |
| **Duration** | 1 h live + 4 h out-of-session (pre-work + homework) |
| **Format** | Live lab |
| **Verified by** | ASM-2 (whiteboard + artifact) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 9 November 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 4 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

## Narrative

RAG is basics by Vlad's explicit call ("RAG is here somewhere… it's in basic"). Everyone builds the canonical pipeline — chunk → embed → store → retrieve → augment → answer — with their own hands, against a corpus that feels like client work: anonymized meeting notes, because the in-production meeting-RAG system is our in-house proof point. Builds directly on LSN-2.3 (the retrieval half is already in their notebook). They leave able to draw and defend this on a whiteboard because they built it and watched it break.

**Restructure note (2 h → 1 h live).** The build does not shrink; it moves. Solo stages — chunk, embed, index, retrieve — become guided pre-work with self-verifying checkpoints, because they are individual keyboard work that does not need a room. The live hour keeps exactly what does need a room: **unblocking the people whose pipeline didn't come up**, getting everyone to a working end-to-end answer *together*, and the three scripted failure demos, which only land as a shared argument. Consequence for GAP-9 is real and recorded in Materials: a notebook that must survive being run alone.

## Pre-work (mandatory — no pre-work, no seat)

Tasks 4–7 are the build stages relocated out of the live lab. Each ends in a self-check cell that prints PASS or FAIL with the reason; recovery assets are referenced inline so a stall never blocks the next stage.

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | LSN-2.3 lab notebook and homework complete and running (embed + nearest-neighbor query; model cached locally) | — (done in 2.3) | Screenshot of your Q1 query results |
| 2 | Read the guided notebook intro — sections "What is RAG?", "RAG Pipeline", "Document Chunking Strategies", "Retrieval Methods" | 25 min | Nothing — quizzed cold at session start |
| 3 | Download the meeting-notes corpus pack; run the setup cell; confirm `len(docs) == 12` prints | 15 min | The printed confirmation in your notebook |
| 4 | **Build stage 1 — chunk.** Chunk the corpus at size 500 / overlap 50; self-check expects ~150 chunks. *If it fails:* load the pre-baked `chunks.json` and continue — note in your log that you used it | 25 min | Chunk count + PASS/FAIL |
| 5 | **Build stage 2 — embed.** Embed all chunks with the same sentence-transformers model as 2.3; self-check prints the matrix shape. *If the model stalls:* load `embeddings.npy` and continue | 25 min | Matrix shape + PASS/FAIL |
| 6 | **Build stage 3 — index + smoke query.** Build the index; run "Who owns the follow-up on the Client A pilot?" and confirm the action-item chunk lands in the top 3. *Expected failure, documented in the notebook:* every query returns the attendee-list/header chunk because boilerplate dominates similarity. *Fix:* strip headers, re-chunk, re-embed. **This failure is the lesson — retrieval quality is a data-cleaning problem — so the notebook makes you fix it rather than handing you the answer** | 35 min | Your top-3 for the smoke query, before and after any header fix |
| 7 | **Build stage 4 — retrieve.** `retrieve(query, k)` returns (chunk, score) pairs for arbitrary k. Then post your PASS/FAIL summary for stages 1–4 to the pre-session thread | 25 min | The posted summary — this is how Tyler knows who to unblock in segment 2 |

**Time accounting (pre-work):** 25 + 15 + 25 + 25 + 35 + 25 = 150 min.

**Corpus (GAP-9):** 12 anonymized VSP-style meeting notes (clients → "Client A/B", people → roles). Contents engineered for the lab: kickoffs, status calls, action items with owners, and one architecture decision that is **reversed in a later meeting** — deliberately, for the staleness demo in the failure segment. ~40 pages → ~150 chunks at default settings.

## Session Plan

Runbook format. Tyler reads the pre-session PASS/FAIL thread **before** the room and arrives knowing who is broken and at which stage.

| Segment | Time | Method | Detail |
|---|---|---|---|
| The architecture on one slide | 8 min | talk | Chunk → embed → store → retrieve → augment → answer. Why retrieval fixes *some* hallucination: the model generates from evidence in context instead of from its weights. What it doesn't fix (final segment). **Checkpoint:** cold-call two people to name the six stages unprompted — they built it last week, so this should be fast. |
| Unblock and green-light | 17 min | lab triage | Everyone runs their pre-work pipeline live. Target state: every participant has `retrieve(query, k)` returning (chunk, score) pairs. Triage order from the pre-session thread — stage-3 boilerplate failures first (they need the header-stripping conversation), then missing embeddings (drop in `embeddings.npy`), then environment breaks (drop in `chunks.json` + `embeddings.npy` and move on; they can rebuild after). **Nobody proceeds to the next segment red.** Whoever hit the boilerplate failure in pre-work narrates their fix to the room — 2 min, and it teaches the data-cleaning lesson better than a slide. |
| Augment and answer — together | 15 min | lab | Wire top-k chunks into the prompt, everyone at once, one shared configuration (k=3, chunk 500). Then one change, live: add "Answer only from the provided context; if the answer is not there, say so," and diff before/after on the same question. *Likely failure:* model answers from world knowledge, ignoring context → that diff **is** the demo. The full parameter grid is homework task 1; here we only need everyone answering end-to-end, which is the thing that needed a room. |
| Where it breaks — honest failure modes | 15 min | demo + discussion | Three scripted breaks, run from Tyler's machine so timing is controlled: **(a) bad chunks** — a mid-sentence split produces a garbage citation; **(b) stale corpus** — ask about the reversed architecture decision with and without the later meeting's doc in the index: confident, outdated answer vs corrected answer; **(c) unanswerable question** — the corpus can't answer; watch retrieval + confabulation blend, then fix with the "say so" instruction. Revisit 2.3's polarity miss as a retrieval hazard. Kept live deliberately: these only work as a shared argument. |
| Whiteboard rehearsal | 5 min | drill | One volunteer draws the pipeline cold on the whiteboard while the room corrects them — direct ASM-2 rehearsal. |

**Timing check:** 8 + 17 + 15 + 15 + 5 = 60 min = 1 h — matches the spreadsheet contract.

**What moved out of the live hour (2 h → 1 h):** the four solo build checkpoints CP1–CP4 (50 min live) → pre-work tasks 4–7, where they get 110 min and self-verifying checkpoints; the k × chunk-size × grounding grid (30 min live) → homework task 1, where exploring nine configurations is actually feasible. What stayed live: architecture framing, **unblocking**, one shared end-to-end answer path, the three scripted breaks, and the whiteboard rehearsal. Nothing was dropped.

## Client Tie-In (Dorel's rule)

The corpus is our own work, anonymized: the meeting-RAG system running in production is the proof point participants can cite in pre-sales — "we run this on our own meetings; here is how it's built, and here is where it breaks." A senior who has personally hit the boilerplate-chunk failure and the stale-corpus failure can answer the two questions every prospect asks: "why won't it just make things up?" and "what happens when our documents change?"

## Homework

| # | Task | Time | Deliverable |
|---|---|---|---|
| 1 | **The parameter grid** (relocated from the live hour, where it was rushed). Sweep k ∈ {1, 3, 8} × chunk size {200, 500, 1000}, each with and without the grounding instruction, on one fixed question. Watch for the two failures the live hour no longer has time to stage: the model answering from world knowledge, and k=8 × 1000-char chunks degrading or overflowing the context window (LSN-2.1 callback) | 45 min | A filled comparison table + 3–4 sentences naming your chosen configuration and the trade-off you accepted |
| 2 | **The graded artifact.** Re-point the pipeline at a different small corpus — your own project docs (anonymized) or the provided fallback pack. Submit the notebook + one paragraph on retrieval quality: one query it handled well, one concrete miss, and the single change you'd make first. *Grading standard:* pipeline runs end-to-end; the paragraph names a real miss and a plausible fix (not "it worked great") | 45 min | Notebook + the paragraph, submitted referencing `LSN-2.4` |

Task 2 plus the ASM-2 whiteboard exercise verify OUT-2.4. **Keep this pipeline runnable** — LSN-2.6's homework builds a 20-question eval set against this exact corpus, which is how "measured quality, not vibes" becomes a number you own.

**Time accounting:** pre-work 150 min + homework 90 min = 4 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| RAG notebook (sections: "What is RAG?", "RAG Pipeline", "Document Chunking Strategies", "Retrieval Methods", "Implementation") | adapt (**GAP-9**) — **scope changed by the 2 h → 1 h cut.** The build stages are now solo pre-work, so the notebook must run unattended: (1) a self-check cell per stage printing PASS/FAIL **with the reason**, (2) recovery assets referenced inline at the point of failure rather than handed out by the instructor, (3) the boilerplate-chunk failure staged so the participant diagnoses and fixes it alone — hint first, answer in a collapsed cell, (4) a troubleshooting appendix covering path/encoding errors, missing deps and model-download stalls, (5) a stage-summary cell that emits the PASS/FAIL text to paste into the pre-session thread. Same content, higher build bar; **needed by 2 Nov 2026**, a week before the session | notebooks/generative_ai/07_GenerativeAI_Retrieval_Augmented_Generation.ipynb |
| Meeting-notes corpus pack (12 docs, anonymized, reversal doc included) | build (**GAP-9**) — needed by 2 Nov 2026 (pre-work now contains the build) | program/materials/ — to create |
| Recovery assets: `chunks.json`, `embeddings.npy`, model cache | build (**GAP-9**, with corpus) — **now load-bearing rather than a safety net:** they are the only thing standing between a solo stall and a participant arriving red | lab repo — to create |
| Architecture one-slide | build (light — from "LLM in five pictures" style) | program/materials/ — to create |
| Pre-session PASS/FAIL thread (channel + template) | build (light — **new**, required by the pre-work handover) | program/materials/ — to create |

## Delivery Notes

Not yet delivered. Record here: how many arrived green on all four pre-work stages vs needed triage (this is the number that says whether GAP-9's solo-run design worked), how many used recovery assets and at which stage, whether 17 min of unblocking sufficed, which scripted break landed hardest. Feeds the MOD-2 retro and the GAP-9 close-out.
