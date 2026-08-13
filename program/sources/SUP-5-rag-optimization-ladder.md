---
name: SUP-5-rag-optimization-ladder
description: The full RAG pipeline as twelve named knobs in the order you turn them, each with the symptom that tells you to turn it and the cost of doing so — plus how to evaluate the result.
serves: LSN-2.3, LSN-2.4, LSN-2.5, LSN-2.6
sources: SRC-1, SRC-2
---

# SUP-5 — The RAG Optimization Ladder

**The problem this solves.** `LSN-2.4` builds the canonical pipeline — chunk, embed, store, retrieve,
augment, answer — and its homework already sweeps `k` × chunk size × grounding instruction. What the
lesson cannot currently answer is the question every participant will get in their first client meeting
after building one: **"it's returning the wrong passages — now what?"**

`SRC-1` devotes two full weeks to exactly that, and its structure is the most reusable thing in the whole
donated corpus. Its teaching sequence is worth copying wholesale: **build the naive version, write down
its shortfalls yourself, then fix them one at a time and check whether the shortfall actually moved.**
That is not a lecture; it is the shape of `LSN-2.4`'s homework and `LSN-2.6`'s eval homework, joined up.

---

## 0. The frame: RAG is a search problem wearing a language-model hat

Everything below is retrieval engineering. Say that out loud early — it reframes RAG from "AI magic" into
a discipline with forty years of prior art, and it explains why the biggest wins come from the parts that
have nothing to do with the model.

**Why anyone bothers (the client-facing list):** stale knowledge, hallucination, no attribution, no
access to private data, no cheap way to update, and a context window that cannot hold the corpus. RAG
addresses all six, at the cost of a system to run.

---

## The ladder

Twelve knobs, grouped into the four stages where they live. **Turn them roughly in this order** — the
earlier ones are cheaper and their gains are larger.

### Stage 1 — Ingest (before anything is embedded)

**Knob 1 — Extraction quality.**
Symptom: retrieved chunks are full of headers, footers, page numbers, or garbled tables; a chunk is
half a sentence. Fix: a real document-conversion step that preserves structure — headings, table cell
relationships, reading order — and strips furniture. Cost: a pipeline dependency and processing time.
**This is the single highest-leverage knob and it is invisible in most tutorials**, which start from clean
text. `LSN-2.4`'s own header-stripping fix in pre-work is this knob, and naming it as knob 1 tells
participants that their annoying boilerplate problem was actually the main event.

**Knob 2 — Chunking strategy.**
Five options in increasing sophistication: fixed character count · recursive character splitting (respect
paragraph and sentence boundaries) · document-structure-aware (split at headings) · semantic (split where
the topic shifts) · model-assisted (ask a model where to split). Plus **overlap** — repeat a little text
across chunk boundaries so an answer straddling a boundary survives.
Symptom: answers are almost right but truncated; the right document is retrieved but the wrong part of
it. Cost: mostly thought, some processing.
**The trade this knob expresses:** small chunks retrieve precisely and lose context; large chunks carry
context and dilute the signal. That is a sentence a participant can say to a client, and it is the
`LSN-2.4` homework's chunk-size axis given a reason.

**Knob 3 — Metadata capture.**
Attach source document, section, date, author, and access tier to every chunk at ingest. Symptom: you
cannot filter, you cannot cite, and you cannot tell the client where an answer came from. Cost: near
zero at ingest, expensive to retrofit. **Capture it even if you do not use it yet** — this is the cheapest
future-proofing in the pipeline, and attribution is half of why clients trust RAG at all.

### Stage 2 — Encode and index

**Knob 4 — Embedding model choice.**
Three properties actually decide it: how much text it can take at once, how many dimensions it produces
(storage and search cost), and how well it does on *your* kind of text. Symptom: semantically obvious
matches are missed. Cost: re-embedding the whole corpus to change it — which is why this decision wants
to be made deliberately once. Direct extension of `LSN-2.3`'s two-model ranking homework.

**Knob 5 — Sparse vs dense vs hybrid retrieval.**
- **Sparse / lexical** matching (term-frequency scoring) is fast, cheap, interpretable, and unbeatable on
  exact terms — part numbers, error codes, proper nouns, contract clause identifiers.
- **Dense / semantic** matching finds meaning across different wording, and misses exact strings.
- **Hybrid** runs both and merges the scores.

Symptom pointing at sparse: the user searched for a literal identifier and got thematically related
nonsense. Symptom pointing at dense: the user asked a question in their own words and got nothing.
**Hybrid is the default answer for real client corpora**, and the merge — how you normalize and weight
two score scales — is the actual engineering. Cost: a second index and a tuning parameter.

**Knob 6 — Index algorithm and where it lives.**
Approximate-nearest-neighbour indexes trade recall for speed; the choice between in-memory, local, and
managed cloud is a cost and operations decision, not an accuracy one. Symptom: search latency, or a
memory bill. **For basics, the teaching point is only that a vector database is a search index with
tuning knobs, not a magic box** — and that "recall vs speed vs memory" is the triangle.

### Stage 3 — Query, before retrieval

**Knob 7 — Query rewriting.**
The user asks a question; the documents are written as statements. That mismatch alone loses matches.
Rewrite the query into the shape the corpus is written in. Symptom: obviously-present answers are not
found for conversational questions.

**Knob 8 — Query decomposition.**
*"What's a newer waterfront hotel with a good restaurant, and do they have vacancies?"* is three
retrievals, not one. Split compound questions, retrieve for each, then compose. Symptom: multi-part
questions get a partial answer that addresses whichever part came first.

**Knob 9 — Query expansion.**
Generate several phrasings of the same question and retrieve for all of them. Symptom: retrieval quality
swings wildly on small wording changes — which, notably, is a *stochasticity* symptom and a live callback
to `LSN-0.4`.

All three cost an extra model call per query — real money and latency, which makes them a `LSN-2.5`
cost-reasoning example with actual numbers attached.

### Stage 4 — After retrieval, before generation

**Knob 10 — Filtering and cut-offs.**
Filter by metadata (date range, document type, access tier) before ranking. Then handle the
**top-k tail problem**: with a fixed `k`, the last result is included merely because something had to be
last. Two fixes — a maximum-distance threshold, or an automatic cut where the score gaps jump. Symptom:
one irrelevant chunk poisons an otherwise good answer. Cost: near zero. **This is the best
effort-to-payoff ratio on the whole ladder** and it is a two-line change to `LSN-2.4`'s
`retrieve(query, k)`.

**Knob 11 — Re-ranking.**
Retrieval casts a wide, fast net; re-ranking scores that shortlist carefully. The trade is explicit: a
model that encodes query and document *together* judges relevance far better and costs far more, because
nothing can be precomputed. Choose on three axes — ranking quality, latency, and whether it understands
your domain. Symptom: the right passage is in your top 20 but not your top 3. Cost: latency and money per
query, on the shortlist only.

**Knob 12 — Context assembly.**
Two opposite moves, both useful:
- **Enrich** — prepend each chunk's metadata (source, date, section) so the model can cite and can weigh
  recency.
- **Compress** — strip retrieved text down to what actually bears on the question, cutting tokens and
  cost and sharpening focus.

And one placement rule with an evidence base: **models attend less well to the middle of a long context.**
Put the strongest chunks first and last. Free to implement, and a nicely concrete example of
"the context window is working memory" from `LSN-2.1`.

---

## Evaluating the pipeline — and the diagnosis this enables

RAG has two failure surfaces, and conflating them is the most common mistake in the room:

| Failure surface | Question | Measured by |
|---|---|---|
| **Retrieval** | Did we hand the model the right passages? | Was the correct passage in the top *k* (hit rate); how high was it ranked (mean reciprocal rank) |
| **Generation** | Given the right passages, did it answer well? | Faithfulness to the passages, relevance to the question, correctness against a reference |

**Diagnose in that order.** If the correct passage was never retrieved, no prompt engineering will save
the answer — and every hour spent on the prompt is wasted. Teaching this ordering is worth more than
teaching any single knob.

Plus the two dimensions clients ask about and engineers forget: **latency** and **cost per query**.

**On automated evaluation frameworks and model-as-judge scoring:** genuinely useful for catching
regressions when you change a knob, unreliable as an absolute quality claim (see `SUP-3` §6). The
practical rule: use them to answer *"did knob 11 make things better than knob 10 alone?"* — a relative
question on a fixed question set — and use human judgment for *"is this good enough to ship?"*

---

## The teaching sequence worth stealing

`SRC-1` runs it over two weeks, and it maps cleanly onto material `MOD-2` already has:

1. Build the naive pipeline. *(`LSN-2.4` pre-work, already built.)*
2. **Query it and write down its shortfalls yourself, in bullets, with a paragraph on why each one
   happens.** *(This is the missing step, and it is where the learning is.)*
3. Implement fixes from the ladder.
4. **Return to your own shortfall list and state, per bullet, whether it moved.**

Step 4 is what turns a knob-tour into judgment. It is also, notably, the same self-critical loop as the
`LSN-2.6` golden-eval homework — the difference is that here the participant writes the failure list
*before* being told what the failures are called.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-2.4` segment 4 | The three scripted failure demos (bad chunks, stale corpus, unanswerable question) map onto knobs 2, 3, and the retrieval/generation split — naming the knob after each demo turns a failure gallery into a repair manual | Sharpen an existing segment — **no minute changes** | Deck edit |
| `LSN-2.4` homework | The existing k × chunk-size × grounding grid gains a fourth cheap axis: **the top-k cut-off (knob 10)**, two lines of code, usually a visible win. Candidate swap for one grid cell, not an addition | Swap within the existing 45-min task | Notebook edit |
| `LSN-2.4` homework | Steps 2 and 4 of the teaching sequence (write your own shortfall list, then revisit it) are a framing change to the existing "one paragraph on retrieval quality" deliverable — same minutes, far better output | Reframe an existing deliverable | Wording |
| `LSN-2.3` | Knobs 4 and 5 give the existing two-model comparison homework its vocabulary; the lexical-vs-semantic contrast explains the scripted polarity miss in segment 2 | Framing note | None |
| `LSN-2.5` | Knobs 7–9 and 11 are where RAG's cost actually goes — concrete per-query numbers for the cost-reality segment, beyond token counts | Input to the cost calculator homework | Small |
| `LSN-2.6` | The retrieval/generation failure split is the diagnostic backbone for the `GAP-7` failure pack | Input to an unbuilt gap | Reduces `GAP-7` build effort |
| `MOD-3` advanced pointer | Knobs 6 and 11 at production scale are advanced-tier material — noted, not taught at basics | Scope boundary | None |

## Proposals requiring a spec decision

**None outstanding — adopted 2026-08-11.** `LSN-2.4`'s graded artifact (homework task 2) is now staged as
*write your own shortfall list → apply one or two ladder fixes → return to your own list and state, per
bullet, whether it moved*. Same 45 minutes; the grading standard now requires at least one bullet honestly
marked unmoved. Cost is zero: `GAP-9` is unbuilt, so the notebook will be written to the new shape rather
than rewritten to it.
