---
name: LSN-1.3-grading-models
description: Read model grades — MAE, precision/recall, confusion matrix, AUC — and judge "is this good enough for this client's use case?" instead of accepting a headline accuracy number.
module: MOD-1
serves: OUT-1.3
duration: 1.5 h
prework_time: 30
owner: Tyler Goble
status: draft
---

# LSN-1.3 — Grading Models

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.3` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-1 (quiz + homework) |

## Narrative

Kills the misconception that one headline number ("99% accurate!") settles whether a model is good. Installs the judging skill: MAE as the average miss in units the client cares about; precision and recall as two different kinds of wrong with two different price tags; the confusion matrix as the raw truth behind every metric; AUC in one picture. Builds directly on LSN-0.3's base-rate lesson — the 99%-accurate fraud detector that is mostly false alarms returns here as the precision/recall centerpiece — and arms the homework: three report cards, ship-or-don't-ship.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Revisit your LSN-0.3 base-rate notes (the 1-in-10,000 fraud detector) | 15 min | One line: why is a 99%-accurate detector on a rare event mostly false alarms? |
| 2 | Read the ML literacy deck (see PROGRAM_PLAN.md §8) grading/metrics section | 15 min | Nothing to submit |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| MAE: the average miss | 20 min | talk + worked example | MAE in real units — a house-price model with MAE $23k: "on average we're off by $23k; is that livable for your decision?" Then the trap: an average hides the spread — a model that misses small items by a little and big items by a lot can have a flattering MAE. Ask for error broken out by segment. (This trap is homework card A.) |
| Precision vs recall: two kinds of wrong | 30 min | talk + drill | The LSN-0.3 fraud detector, upgraded from base rates to metrics: precision = of what we flagged, how much was real; recall = of what was real, how much we caught. Compute both live from the LSN-0.3 numbers. Then the client question that matters: *which error is expensive for this client?* Missed fraud vs annoyed customers; missed defect vs unnecessary site inspection. Participants pick the priority metric for three quick-fire cases. |
| Confusion matrix reading drill | 20 min | drill | Two 2×2 matrices on screen; participants extract accuracy, precision, recall by hand and say in one client-safe sentence what the model does well and badly. Matrix 2 is the always-say-no degenerate case — high accuracy, zero recall — the base-rate lesson wearing a metrics costume. |
| AUC in one picture + "they quoted 99% accuracy" | 20 min | talk + discussion | AUC as "how well the model separates the classes across all thresholds" — one ROC picture, no math (`notebooks/foundations/12_Analytics_Performance.ipynb` renders it). Close with the checklist for when a client or vendor quotes one shiny number: What's the base rate? Accuracy on *what* data — did the model see it in training? Precision and recall, per class? What does each error cost you? |

**Timing check:** 20 + 30 + 20 + 20 = 90 min = 1.5 h contract duration. ✓

## Client Tie-In (Dorel's rule)

Every metric is priced in a delivery-company scenario: MAE on effort estimates that back fixed-bid quotes (an average miss you eat in margin), recall on rare defects/fraud where a miss is the expensive error, and the "vendor quotes 99% accuracy" checklist rehearses the exact pre-sales moment GOAL-1 names. Homework card B reuses the fraud framing from LSN-0.3 so the base-rate callback is explicit.

## Homework

**Three model report cards — for each, write one paragraph: ship it or not, and why.** Submit referencing `LSN-1.3`. Pass = the right call on all three *for the right reason* (A: catches the segment-level error behind the MAE; B: invokes base rate/recall, not accuracy; C: ties the metrics to the client's error costs).

**Card A — Effort estimator (regression).** Estimates delivery hours per work item to back fixed-bid quotes. **MAE = 38 hours** across 2,400 historical items. Breakdown the vendor didn't volunteer: 90% of items are small tasks (< 40 h) where the average miss is ~6 h; the 10% that are large epics (> 400 h) miss by ~330 h on average. The client wants it precisely for quoting large projects. *(Trap: a flattering MAE dominated by easy small items — useless on the segment the client will actually bet money on.)*

**Card B — Warranty-fraud detector (classifier).** Test set: 10,000 claims, 80 fraudulent (0.8% base rate). Confusion matrix: TP = 9, FN = 71, FP = 3, TN = 9,917. Headline: **accuracy 99.26%**, precision 75%. Unstated: **recall = 9/80 ≈ 11%** — it misses 89% of fraud. A detector that flags nothing scores 99.2% accuracy on this data (LSN-0.3). *(Trap: great accuracy, terrible recall on the rare class — the entire point of the model.)*

**Card C — Churn early-warning (classifier), the genuinely good one.** Base rate 18%; on a held-out most-recent quarter: **precision 62%, recall 78%, AUC 0.88**. Costs are stated: a flagged customer gets a ~$50 retention call; a missed churner is a ~$2,000 lost account — so favoring recall over precision is the right trade, and the temporal holdout means it wasn't graded on data it memorized. *(Shippable: honest evaluation, metrics chosen against the client's actual error costs. The paragraph should say so — and may add a monitoring caveat.)*

## Materials

| Material | Status | Path / source |
|---|---|---|
| ML literacy deck (grading/metrics section) | exists | ML literacy deck (see PROGRAM_PLAN.md §8) — not in repo |
| Metrics/ROC rendering for the AUC picture | exists | `notebooks/foundations/12_Analytics_Performance.ipynb` |
| Three model report cards + answer key | exists | This plan (Homework, above) |
| Confusion-matrix drill slides (two matrices incl. always-say-no case) | adapt | Extract from deck at delivery prep |
| Optional pre-work video: StatQuest with Josh Starmer — "ROC and AUC, Clearly Explained!" | exists | (verify at delivery prep) |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality. Feeds the MOD-1 retro.
