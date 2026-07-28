---
name: LSN-0.4-deterministic-probabilistic-stochastic
description: Sort any system behavior into deterministic / probabilistic / stochastic, and set client expectations for outputs that vary between runs.
module: MOD-0
serves: OUT-0.2
duration: 1 h
prework_time: 20
owner: Tyler
status: draft
---

# LSN-0.4 — Deterministic, Probabilistic, Stochastic

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.2` |
| **Duration** | 1 h session + 20 min pre-work |
| **Format** | Live or recorded |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Narrative

Senior engineers spend careers making systems deterministic, so "the same question gave a different answer" reads as a defect — this session reframes it as a property. It kills the instinct to promise deterministic behavior from probabilistic systems, and installs the vocabulary bridge into everything after: "95% confident" as a claim about uncertainty, not a decoration (`OUT-0.2`), and "all models are wrong, some are useful" as a working attitude rather than a quip. Draws on the distribution and probability muscles from `LSN-0.2`/`LSN-0.3`; bridges directly into `MOD-1`, where the five ML jobs all produce exactly this kind of answer.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-read the **keywords** section of the ML literacy deck (deterministic, probabilistic, stochastic, confidence, inference) | 10 min | None — feeds task 2 |
| 2 | Write one example of each term from your own project experience — one line each, e.g. a system you built that is deterministic, an output you've seen that was a guess with a confidence, a process with randomness inside it | 10 min | Three one-line examples, submitted before session (they are the raw material for segment 1) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The three-bucket sort | 25 min | discussion | Participants' pre-work examples go on a shared board, sorted live into deterministic / probabilistic / stochastic. Anchors: deterministic — `2+2`, a SQL `SUM`, a build with pinned deps (same input, same output, every time); probabilistic — "spam, confidence 0.87": a guess with stated uncertainty; stochastic — randomness in the process itself: retry jitter, load-balancer routing, SGD training, LLM sampling at temperature > 0. Debate the misfiled favorites: a "flaky test" (deterministic code in a stochastic environment), a hash function (deterministic, however random it looks), an LLM at temperature 0 (near-deterministic in practice, not contractually — batching and floating-point effects) |
| Why this matters commercially | 20 min | case discussion | The in-production meeting-RAG case: a user asks the same question twice, gets two differently-worded answers, and files a defect. Was it one? Work it as a group: what was (implicitly) promised vs. what should have been. The fix is upstream, in expectation-setting: acceptance criteria for probabilistic systems are eval sets and thresholds ("≥ 90% of a 50-question test set judged correct"), never exact-match outputs. Close with Box — "all models are wrong, some are useful": the deliverable is a system whose errors are understood, bounded, and priced in |
| Bridge to MOD-1 | 15 min | talk | Preview: the five ML jobs — classify, cluster, regress, propensity, recommend (`LSN-1.1`) — every one returns a probabilistic answer. Today's vocabulary is how you'll read those outputs in `LSN-1.2` and grade them in `LSN-1.3`; the fraud detector from `LSN-0.3` comes back with its formal report card. Reminder: `ASM-0` opens this week — scenario questions, and the `LSN-0.1` notebook screenshot is the setup evidence |

**Timing check:** 25 + 20 + 15 = 60 min = 1 h contract duration.

## Client Tie-In (Dorel's rule)

The in-production meeting-RAG system (walked end-to-end in `LSN-3.6`): the one VSP system where clients meet output variation directly, and where "is that a bug or a property?" is a live support question. Segment 2 is that conversation, rehearsed before it happens with a client.

## Homework

None — checkpoint week. `ASM-0` (async quiz, ~30 min, pass bar 80%) runs this week and verifies `OUT-0.2` through scenario questions from this lesson plus the `LSN-0.2`/`LSN-0.3` material.

## Materials

| Material | Status | Path / source |
|---|---|---|
| ML literacy deck — keywords section | exists (light polish at delivery prep) | Tyler's deck, not yet in repo — link at delivery prep |
| Shared sorting board (three columns, pre-seeded with anchors) | adapt | any shared whiteboard tool; anchors from segment 1 |
| Meeting-RAG expectation-setting mini-case (½-page) | build (share of `GAP-1` polish) | segment 2 of this file — extract |

## Delivery Notes

Not yet delivered — first run Week 1. If delivered recorded rather than live, the three-bucket sort needs an async substitute: post examples in the channel, sort by comment, review misfiles in the recording. Watch whether the temperature-0 nuance derails segment 1 — cap it at two minutes and park the rest for `LSN-2.1`.
