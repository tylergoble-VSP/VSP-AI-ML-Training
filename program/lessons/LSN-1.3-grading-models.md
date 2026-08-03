---
name: LSN-1.3-grading-models
description: Read model grades — MAE, precision/recall, confusion matrix, AUC — and judge "is this good enough for this client's use case?" instead of accepting a headline accuracy number.
module: MOD-1
delivery_date: 2026-09-21
serves: OUT-1.3
duration: 1
prework_time: 45
homework_time: 75
owner: Tyler Goble
status: draft
---

# LSN-1.3 — Grading Models

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.3` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | ASM-1 (quiz + homework) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 21 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Grading Models"** (matches the lesson name).

## Narrative

Kills the misconception that one headline number ("99% accurate!") settles whether a model is good. Installs the judging skill: MAE as the average miss in units the client cares about; precision and recall as two different kinds of wrong with two different price tags; the confusion matrix as the raw truth behind every metric; AUC in one picture. Builds directly on LSN-0.3's base-rate lesson — the 99%-accurate fraud detector that is mostly false alarms returns here as the precision/recall centerpiece — and arms the homework: three report cards, ship-or-don't-ship.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Revisit your LSN-0.3 base-rate notes (the 1-in-10,000 fraud detector) | 15 min | One line: why is a 99%-accurate detector on a rare event mostly false alarms? |
| 2 | Read the grading/metrics material — canonical target: `program/lessons/decks/LSN-1.3-grading-models.html` (mirrors the original ML literacy deck's grading section, not yet in repo) | 15 min | Nothing to submit |
| 3 | Watch StatQuest, "ROC and AUC, Clearly Explained!" — **promoted from optional to mandatory** by the 90→60 rescope: the live AUC segment is now 11 min and assumes you have seen the curve drawn once | 15 min | One line: what does a point on the ROC curve represent? |

**Pre-work total: 45 min.**

## Session Plan

Rescoped 2026-08-03 from 90 min to 60. What kept the room: the precision/recall cost judgment (it is an argument, not a formula) and one confusion matrix computed by hand under supervision. What compressed or moved out: MAE's segment-breakdown trap is now *named* live and *worked* in homework card A, the third quick-fire case is relocated, and AUC leans on mandatory pre-work video instead of being built from scratch.

| Segment | Time | Method | Detail |
|---|---|---|---|
| MAE: the average miss | 12 min | talk + worked example | MAE in real units — a house-price model with MAE $23k: "on average we're off by $23k; is that livable for your decision?" Then name the trap without working it: an average hides the spread, so ask for error broken out by segment. The full worked version is homework card A, which participants now arrive at primed rather than pre-solved. |
| Precision vs recall: two kinds of wrong | 22 min | talk + drill | The LSN-0.3 fraud detector, upgraded from base rates to metrics: precision = of what we flagged, how much was real; recall = of what was real, how much we caught. Compute both live from the LSN-0.3 numbers. Then the client question that matters: *which error is expensive for this client?* Missed fraud vs annoyed customers; missed defect vs unnecessary site inspection. Two quick-fire cases run live (was three — the third is relocated to homework task 2). |
| Confusion matrix reading drill | 15 min | drill | One 2×2 matrix computed by hand live — participants extract accuracy, precision, recall and give the one client-safe sentence on what the model does well and badly. Then the always-say-no degenerate matrix read together at speed: high accuracy, zero recall, the base-rate lesson wearing a metrics costume. Both matrices plus a third go home for solo repetition (homework task 2), so the live job is installing the method, not drilling it to fluency. |
| AUC in one picture + "they quoted 99% accuracy" | 11 min | talk + discussion | Assumes the pre-work StatQuest video: AUC as "how well the model separates the classes across all thresholds" — the notebook's ROC picture shown and read, not derived (`notebooks/foundations/06_Classifier_Algorithms.ipynb` is the go-deeper with real `roc_curve`/`roc_auc_score` usage — NOT `foundations/12`, which is a runtime-timing notebook despite its name; see BUILD_LOG LL-32). Close with the checklist for when a client or vendor quotes one shiny number: What's the base rate? Accuracy on *what* data — did the model see it in training? Precision and recall, per class? What does each error cost you? |

**Timing check:** 12 + 22 + 15 + 11 = 60 min = 1 h — matches the spreadsheet contract.

## Client Tie-In (Dorel's rule)

Every metric is priced in a delivery-company scenario: MAE on effort estimates that back fixed-bid quotes (an average miss you eat in margin), recall on rare defects/fraud where a miss is the expensive error, and the "vendor quotes 99% accuracy" checklist rehearses the exact pre-sales moment GOAL-1 names. Homework card B reuses the fraud framing from LSN-0.3 so the base-rate callback is explicit.

## Homework

**75 min total**, all of it in `notebooks/lessons/LSN-1.3_Grading_Models.ipynb`. Tasks 2 and 3 are the drill repetition and threshold exploration relocated out of the live session by the 90→60 rescope — nothing was cut.

| # | Task | Time | Checkpoint / artifact |
|---|---|---|---|
| 1 | The three model report cards (below) — one paragraph each: ship it or not, and why | 40 min | Three paragraphs submitted referencing `LSN-1.3` |
| 2 | **Relocated drill repetition.** Fill the notebook's drill workspace completely for *both* vendors — six figures, two client-safe sentences, and the ship call with its reason — including the field whose honest answer is a word, not a number. Live, only vendor A was hand-computed and vendor B was read at speed; here you do both cold. Then answer quick-fire case 3 (the at-risk project flag for the Monday delivery review), which the 60-min session drops | 20 min | Drill workspace passing its checker + `QF3_METRIC`/`QF3_WHY` filled |
| 3 | **Relocated threshold sweep.** Using the `scores` and `labels` arrays the AUC cell already builds, pick three cut-offs — permissive, the shipped one, strict — and compute precision and recall at each. Then one sentence: what does AUC summarize that a single precision/recall pair cannot? | 15 min | A 3-row threshold table + the AUC sentence |

**Pass (task 1):** the right call on all three *for the right reason* (A: catches the segment-level error behind the MAE; B: invokes base rate/recall, not accuracy; C: ties the metrics to the client's error costs). **Pass (tasks 2–3):** arithmetic matches the pinned values, and the threshold table shows precision and recall moving in opposite directions — if both rose, the sweep was done wrong.

**Time accounting:** pre-work 45 min + homework 75 min = 2 h out-of-session budget.

**Card A — Effort estimator (regression).** Estimates delivery hours per work item to back fixed-bid quotes. **MAE = 38 hours** across 2,400 historical items. Breakdown the vendor didn't volunteer: 90% of items are small tasks (< 40 h) where the average miss is ~6 h; the 10% that are large epics (> 400 h) miss by ~330 h on average. The client wants it precisely for quoting large projects. *(Trap: a flattering MAE dominated by easy small items — useless on the segment the client will actually bet money on.)*

**Card B — Warranty-fraud detector (classifier).** Test set: 10,000 claims, 80 fraudulent (0.8% base rate). Confusion matrix: TP = 9, FN = 71, FP = 3, TN = 9,917. Headline: **accuracy 99.26%**, precision 75%. Unstated: **recall = 9/80 ≈ 11%** — it misses 89% of fraud. A detector that flags nothing scores 99.2% accuracy on this data (LSN-0.3). *(Trap: great accuracy, terrible recall on the rare class — the entire point of the model.)*

**Card C — Churn early-warning (classifier), the genuinely good one.** Base rate 18%; on a held-out most-recent quarter: **precision 62%, recall 78%, AUC 0.88**. Costs are stated: a flagged customer gets a ~$50 retention call; a missed churner is a ~$2,000 lost account — so favoring recall over precision is the right trade, and the temporal holdout means it wasn't graded on data it memorized. *(Shippable: honest evaluation, metrics chosen against the client's actual error costs. The paragraph should say so — and may add a monitoring caveat.)*

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session deck** — 11 slides w/ timed notes; carries the grading content (canonical, per SI-25) | exists | `program/lessons/decks/LSN-1.3-grading-models.html` |
| **Session notebook** — MAE/precision-recall/AUC segments, fraud report card (LSN-0.3 continuity, pinned), confusion-matrix drill + three report-card homework w/ graded verdicts, executed end to end | exists | `notebooks/lessons/LSN-1.3_Grading_Models.ipynb` |
| ML literacy deck (grading/metrics — original source) | exists | ML literacy deck (see PROGRAM_PLAN.md §8) — not in repo |
| Go-deeper: real ROC/AUC usage | exists | `notebooks/foundations/06_Classifier_Algorithms.ipynb` (replaces the erroneous `foundations/12` citation — LL-32) |
| Three model report cards + answer key | exists | This plan (Homework, above) + notebook homework cells (pinned arithmetic) |
| Confusion-matrix drill slides (two vendor matrices incl. the always-say-no case) | exists | Deck + notebook drill section — vendor A hand-computed live, both completed in homework task 2 |
| **Mandatory** pre-work video: StatQuest with Josh Starmer — "ROC and AUC, Clearly Explained!" (promoted from optional by the 2026-08-03 rescope) | exists | [youtube.com/watch?v=4jRBRDbJemM](https://www.youtube.com/watch?v=4jRBRDbJemM) |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality. Feeds the MOD-1 retro.

**Rescope note (2026-08-03):** **deck retimed 2026-08-03** to 12/22/15/11 — kickers, footers and per-slide note timings now sum to 60, quick-fire case 3 and the vendor-B hand computation are reframed as homework hand-offs, AUC leans on the now-mandatory pre-work video, the homework slide carries all three tasks and the time accounting, and the LL-44 footer overflow is fixed on the two offending slides; **the notebook is still pending** — its segment headers still read *(20 min)*, *(30 min)*, *(20 min)*, *(20 min)* and its quick-fire cell still frames three cases at 10 min, so the notebook pass must move case 3 into the homework section and reprice the four segment headers to 12/22/15/11.
