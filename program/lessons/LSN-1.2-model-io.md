---
name: LSN-1.2-model-io
description: Say what each major model type takes in (features, labels) and kicks out (a probability, a class, a number, a ranking), and interpret a real model output for a client without over- or under-claiming.
module: MOD-1
serves: OUT-1.2
duration: 1 h
prework_time: 20
owner: Tyler Goble
status: draft
---

# LSN-1.2 — Model I/O: What Goes In, What Comes Out

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.2` |
| **Duration** | 1 h session + 20 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-1 (quiz) |

## Narrative

Kills the misconception that a model output is a verdict. Installs Tyler's bar: for each model type, say what it takes in, what it kicks out, and how to read it — a probability is not a fact, a number carries units, a cluster id has no meaning until a human names it, a ranking is relative. Builds on LSN-1.1 (you know which job it is; now you know what that job's model consumes and produces) and sets up LSN-1.3: once you can read one output, the next question is whether the model is any *good*, which is a metrics question.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the model-I/O material — canonical target: `program/lessons/decks/LSN-1.2-model-io.html` (mirrors the original ML literacy deck's model-types + reading-outputs sections, not yet in repo) | 15 min | Nothing to submit |
| 2 | Write one sentence: what do you think a "lead score of 0.73" means, exactly? | 5 min | Your sentence — it gets stress-tested in the drill |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Features and labels | 15 min | talk | What training data actually is: a table where columns are features, one column is the label, rows are examples. Supervised = the label column exists; unsupervised = it doesn't (callback to LSN-1.1's cluster job). One slide of the same CRM table shown twice — once with the "closed?" column (propensity training data), once without (segmentation data). |
| Output safari | 30 min | demo | Four real output types generated live in the session notebook from tiny seeded fits (instant; supersedes the earlier "rendered, not run live" design — see BUILD_LOG Round 5), with per-type "go deeper" pointers to the repo notebooks: (1) logistic regression → per-class probabilities (`notebooks/supervised/02_Supervised_Logistic_Regression.ipynb`); (2) linear regression → a number with units (`notebooks/supervised/01_Supervised_Linear_Regression.ipynb`); (3) K-Means → a bare cluster id, meaningless until named (`notebooks/unsupervised/01_Unsupervised_KMeans_Clustering.ipynb`); (4) Apriori association rules → a ranked "people who X also Y" list, the recommender's shape (`notebooks/unsupervised/07_Unsupervised_Apriori.ipynb`). For each: what went in, what came out, the one-sentence client-safe reading. |
| Interpretation drill: "the model says 0.73" | 15 min | drill | Scenario below run as a role-play — instructor plays the client, participants answer, group critiques against the model answer. Pre-work sentences read back first: most will say "73% chance," and the drill sharpens what that does and does not license. |

**Timing check:** 15 + 30 + 15 = 60 min = 1 h contract duration. ✓

### Interpretation drill — scenario and model answer

**Scenario.** A client's sales org bought a lead-scoring model. In the pipeline review, deal #4127 shows a score of **0.73**. The VP of Sales asks you: *"0.73 — so this deal is basically won, right? Should we stop working it?"*

**Model answer (the shape a pass looks like):**
1. **What it is:** 0.73 is the model's estimated *probability* that this deal closes, given the features it saw. If the model is well calibrated, of 100 deals scored around 0.73, roughly 73 close — and 27 don't. It is a betting line, not a verdict on this deal.
2. **What it's for:** ranking and prioritizing — a 0.73 deserves attention before a 0.31. It says nothing about *why*, and it never says "stop working it."
3. **The next questions to ask:** Is the score calibrated — when it said 0.7 historically, did ~70% actually close? What features feed it, and how fresh are they? What threshold and action has the client attached to the score?

**Curveballs (time permitting):** *"Another deal says 0.51."* — near a coin flip; the model is telling you it doesn't know; don't dress it up. *"Our forecasting model says 8.2."* — that's a regression output; 8.2 *what*? Units first, interpretation second — a number without units is not an answer.

## Client Tie-In (Dorel's rule)

The whole drill is a realistic pre-sales scene: a client who bought (or was sold) "AI lead scoring" and reads the score as a verdict — the exact conversation where a senior who can say "it's a calibrated probability, here's what it licenses and here's what I'd ask next" looks sharp, per GOAL-1. The output safari uses the CRM/sales framing carried over from the deck's sales-world examples.

## Homework

None. The output-reading skill is verified in the ASM-1 quiz; keep your corrected "0.73" sentence — it is the seed of your mock pre-sales answers.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session deck** — 10 slides w/ timed notes; carries features/labels + reading-outputs content (canonical, per SI-25) | exists | `program/lessons/decks/LSN-1.2-model-io.html` |
| **Session notebook** — pre-work fill-in + live output safari (4 types, raw outputs interpreted line by line) + "0.73" drill workspace w/ graded key, executed end to end | exists | `notebooks/lessons/LSN-1.2_Model_IO.ipynb` |
| ML literacy deck (model types + reading outputs — original source) | exists | ML literacy deck (see PROGRAM_PLAN.md §8) — not in repo |
| Go-deeper: classifier probabilities | exists | `notebooks/supervised/02_Supervised_Logistic_Regression.ipynb` |
| Go-deeper: regression number | exists | `notebooks/supervised/01_Supervised_Linear_Regression.ipynb` |
| Go-deeper: cluster assignment | exists | `notebooks/unsupervised/01_Unsupervised_KMeans_Clustering.ipynb` |
| Go-deeper: ranked association rules (note: imports `mlxtend`, not in the MOD-1 venv — see BUILD_LOG LL-29) | exists | `notebooks/unsupervised/07_Unsupervised_Apriori.ipynb` |
| "The model says 0.73" scenario + model answer | exists | This plan (above) + notebook drill cells (verbatim) |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality. Feeds the MOD-1 retro.
