---
name: LSN-0.4-deterministic-probabilistic-stochastic
description: Sort any system behavior into deterministic / probabilistic / stochastic, and set client expectations for outputs that vary between runs.
module: MOD-0
delivery_date: 2026-09-04
serves: OUT-0.2
duration: 1
prework_time: 20
homework_time: 100
owner: Tyler
status: draft
---

# LSN-0.4 — Deterministic, Probabilistic, Stochastic

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.2` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live or recorded |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Friday, 4 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Deterministic vs Probablistic vs Stocastic"** (sic — two typos in the spreadsheet; the repo keeps the corrected spelling).

Last day of the daily boot week. The live session was already a 1 h contract and is unchanged; the out-of-session side changed the most in the module — homework went from "none" to 100 min, and it is the natural home for `ASM-0` because nothing follows it the next morning.

## Narrative

Senior engineers spend careers making systems deterministic, so "the same question gave a different answer" reads as a defect — this session reframes it as a property. It kills the instinct to promise deterministic behavior from probabilistic systems, and installs the vocabulary bridge into everything after: "95% confident" as a claim about uncertainty, not a decoration (`OUT-0.2`), and "all models are wrong, some are useful" as a working attitude rather than a quip. Draws on the distribution and probability muscles from `LSN-0.2`/`LSN-0.3`; bridges directly into `MOD-1`, where the five ML jobs all produce exactly this kind of answer.

## Pre-work (mandatory — no pre-work, no seat) — 20 min

The thinnest pre-work in MOD-0, on purpose: Thursday evening is already carrying `LSN-0.3`'s 90 min homework.

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the **keywords** definitions (deterministic, probabilistic, stochastic, confidence, inference) — canonical target: LSN-0.4 deck slide 2 / session-notebook pre-work section (mirrors the ML literacy deck's keywords section, which is not yet in the repo) | 10 min | None — feeds task 2 |
| 2 | Write one example of each term from your own project experience — one line each, e.g. a system you built that is deterministic, an output you've seen that was a guess with a confidence, a process with randomness inside it | 10 min | Three one-line examples, submitted before session (they are the raw material for segment 1) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The three-bucket sort | 25 min | discussion | Participants' pre-work examples go on a shared board, sorted live into deterministic / probabilistic / stochastic. Anchors: deterministic — `2+2`, a SQL `SUM`, a build with pinned deps (same input, same output, every time); probabilistic — "spam, confidence 0.87": a guess with stated uncertainty; stochastic — randomness in the process itself: retry jitter, load-balancer routing, SGD training, LLM sampling at temperature > 0. Debate the misfiled favorites: a "flaky test" (deterministic code in a stochastic environment), a hash function (deterministic, however random it looks), an LLM at temperature 0 (near-deterministic in practice, not contractually — batching and floating-point effects) |
| Why this matters commercially | 20 min | case discussion | The in-production meeting-RAG case: a user asks the same question twice, gets two differently-worded answers, and files a defect. Was it one? Work it as a group: what was (implicitly) promised vs. what should have been. The fix is upstream, in expectation-setting: acceptance criteria for probabilistic systems are eval sets and thresholds ("≥ 90% of a 50-question test set judged correct"), never exact-match outputs — and the eval set must be *sized*: a genuinely-92% system fails that 50-question bar one run in five (the session works the arithmetic; ~470 questions makes the bar reliable). Close with Box — "all models are wrong, some are useful": the deliverable is a system whose errors are understood, bounded, and priced in |
| Bridge to MOD-1 | 15 min | talk | Preview: the five ML jobs — classify, cluster, regress, propensity, recommend (`LSN-1.1`) — every one returns a probabilistic answer. Today's vocabulary is how you'll read those outputs in `LSN-1.2` and grade them in `LSN-1.3`; the fraud detector from `LSN-0.3` comes back with its formal report card. Reminder: `ASM-0` opens this week — scenario questions, and the `LSN-0.1` notebook screenshot is the setup evidence |

**Timing check:** 25 + 20 + 15 = 60 min = 1 h — matches the spreadsheet contract. Verified against the 2026-08-03 rescope: this session was already a 1 h contract, so no segment was cut, moved, or retimed.

## Client Tie-In (Dorel's rule)

The in-production meeting-RAG system (walked end-to-end in `LSN-3.6`): the one VSP system where clients meet output variation directly, and where "is that a bug or a property?" is a live support question. Segment 2 is that conversation, rehearsed before it happens with a client.

## Homework — 100 min (runs across the weekend of Sep 5–6)

"None — checkpoint week" no longer fits: the spreadsheet gives every lesson a 2 h out-of-session budget, so this lesson now owns 100 min of homework. That is not padding — it is where the module's consolidation and its checkpoint actually live, and Friday is the only slot in the boot week with a clear weekend behind it.

| # | Task | Time | Artifact |
|---|---|---|---|
| 1 | `ASM-0` **prep / consolidation pass:** re-run the summary sections of the three week notebooks (`LSN-0.2`, `LSN-0.3`, `LSN-0.4`) and write the one-line version of each misconception the week killed — single number hides a distribution; P(alert \| fraud) ≠ P(fraud \| alert); correlation has four explanations; varying output is a property, not a defect | 25 min | Four one-liners in your own words |
| 2 | **Three-bucket sort, applied for real:** pick a system you actually work on, list five of its behaviours, sort each into deterministic / probabilistic / stochastic — and for every non-deterministic one, write the acceptance criterion you would put in a SOW (an eval set and a threshold, never an exact-match output) | 25 min | The five-row sort + the acceptance criteria |
| 3 | **Eval-set sizing** (notebook's acceptance-arithmetic cell): a genuinely-92% system faces a "≥ 90% of the test set judged correct" bar. Compute the test-set size that makes it pass 19 runs in 20, and state what you would tell a client who wants the bar set on 50 questions | 20 min | Your n, the arithmetic, and the client sentence |
| 4 | **`ASM-0` checkpoint quiz** — async, ~20 questions, 30 min, pass bar 80%, one retake. Verifies `OUT-0.2` through scenario questions from this lesson plus the `LSN-0.2`/`LSN-0.3` material; `OUT-0.1` is verified by the `LSN-0.1` notebook screenshot | 30 min | Submitted quiz + the setup-evidence screenshot |

**Time accounting:** pre-work 20 min + homework 100 min = 2 h out-of-session budget.

**Scheduling flag:** `ASM-0` is **not on the program spreadsheet** — it needs a calendar slot at the next review call. Proposed here: async within this lesson's homework budget, weekend of Sep 5–6. Accounted for as task 4, so the quiz costs no participant time beyond the 2 h contract — but it does mean 30 of these 100 min are a graded gate, not practice, and the module spec carries the same flag.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session deck** — 11 slides w/ timed notes incl. the keywords slide (pre-work target) and the homework slide added 2026-08-03 | exists | `program/lessons/decks/LSN-0.4-deterministic-probabilistic-stochastic.html` |
| **Session notebook** — pre-work fill-in + three-bucket demos (SeedSequence-spawned "runs") + SUP-2291 case + acceptance arithmetic + MOD-1 bridge, executed end to end | exists | `notebooks/lessons/LSN-0.4_Deterministic_Probabilistic_Stochastic.ipynb` |
| ML literacy deck — keywords section (original source; deck slide 2 mirrors it) | exists (light polish at delivery prep) | Tyler's deck, not yet in repo — link at delivery prep |
| Shared sorting board (three columns, pre-seeded with anchors) | adapt | any shared whiteboard tool; anchors from segment 1 |
| Meeting-RAG expectation-setting mini-case (½-page) | exists | notebook segment-2 section (ticket SUP-2291) + deck |

## Delivery Notes

Not yet delivered — first run Friday 4 September 2026. If delivered recorded rather than live, the three-bucket sort needs an async substitute: post examples in the channel, sort by comment, review misfiles in the recording. Watch whether the temperature-0 nuance derails segment 1 — cap it at two minutes and park the rest for `LSN-2.1`. No *retiming* was needed for the deck or notebook: the session was already 1 h and summed to 60 min, so both remain correctly timed — the 2026-08-03 change here is entirely out-of-session. The **deck was updated 2026-08-03** for that change: a new slide 10 carries the 100 min homework (consolidation pass, three-bucket SOW exercise, eval-set sizing, `ASM-0`), the close slide no longer says "no homework", and segment 3's `ASM-0` reminder now names the Sep 5–6 weekend window explicitly. The **notebook's homework sections are still pending.**
