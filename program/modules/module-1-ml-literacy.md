---
name: module-1-ml-literacy
description: ML literacy — triage a client ask into the five ML jobs, interpret model outputs and metrics, train one labeled model, and hold a pre-sales conversation without hand-waving.
---

# MOD-1 — ML Literacy

## Module Configuration

| Field | Value |
|---|---|
| **ID** | `MOD-1` |
| **Tier** | Basics |
| **Pillar** | ML (~5% of the total program — scoped to pre-sales fluency, per Vlad) |
| **Cadence** | Weekly, Mondays 7 Sep – 12 Oct 2026 (6 sessions) — per the program spreadsheet locked 2026-08-03; calendar of record is `program/SCHEDULE.md` |
| **Total effort** | **18 h** — 6 × 1 h live + 6 × 2 h out-of-session (pre-work + homework combined). `ASM-1` adds ~1 h once it gets a calendar slot. |
| **Roles** | Presenter: Tyler · Reviewer: Vlad · Guinea pig: Mazilu (TBC — the spreadsheet says "Mazilu?") |
| **Module owner** | Tyler Goble |
| **Prerequisite** | `ASM-0` passed |
| **Checkpoint** | `ASM-1` |

The weekly cadence is what makes the 2 h out-of-session budget work: each lesson's pre-work and homework have a full week of runway, so pre-work can be meatier (up to ~45 min) than in a daily-cadence module.

## Purpose

Vlad's scope, verbatim: "just enough ML to go through a pre-sales… to know what a neural network is, what a convolutional neural network is, what deep learning is, what reinforcement learning is — to have a mini conversation about this and not look completely stupid." Plus the hands-on floor he insisted on: "start up a Jupyter notebook… do that classical exercise, use PyTorch." Tyler's framing of the bar: "I can see the outputs of a model and I can interpret them."

This module is the existing ML literacy deck, restructured from a standalone training into lessons — the deck itself survives as the module's table-of-contents presentation (Vlad approved that reframing).

## Outcomes

| ID | After MOD-1 you can… | Serves |
|---|---|---|
| `OUT-1.1` | Triage a client ask into the five ML jobs — classify, cluster, regress, propensity, recommend — and distinguish ML from generative AI | GOAL-1, GOAL-4 |
| `OUT-1.2` | Say what each major model type takes in and kicks out, and interpret its outputs | GOAL-1, GOAL-4 |
| `OUT-1.3` | Read model grades — MAE, precision/recall, confusion matrix, AUC — and judge "is this good enough for the client's use case?" | GOAL-1, GOAL-4 |
| `OUT-1.4` | Personally train a simple labeled model (MNIST) in a Jupyter notebook with PyTorch/Keras | GOAL-1, GOAL-6 |
| `OUT-1.5` | Hold a conversational-level exchange on neural nets, CNNs, deep learning, and reinforcement learning | GOAL-1 |
| `OUT-1.6` | Articulate data requirements and ML limitations ("no data, no model; it can only infer so far") and run the pre-sales question bank | GOAL-1, GOAL-4 |

## Lesson Inventory

Every lesson runs on the same contract: **1 h live + 2 h out-of-session** (pre-work + homework combined). Where the spreadsheet's row title differs from the lesson name it is listed as an alias.

| ID | Lesson (spreadsheet alias) | Delivery date | Live | Out-of-session | Owner | Format | Material status |
|---|---|---|---|---|---|---|---|
| `LSN-1.1` | The five ML jobs & the nesting doll (= "ML Use Cases") | Mon 7 Sep 2026 | 1 h | 2 h (45 pre + 75 hw) | Tyler | Live | Built (deck + notebook) |
| `LSN-1.2` | Model I/O — inputs, outputs, interpretation (= "ML Model Inputs and Outputs") | Mon 14 Sep 2026 | 1 h | 2 h (40 pre + 80 hw) | Tyler | Live | Built (deck + notebook) |
| `LSN-1.3` | Grading models — MAE, precision/recall, AUC (= "Grading Models") | Mon 21 Sep 2026 | 1 h | 2 h (45 pre + 75 hw) | Tyler | Live | Built (deck + notebook); **deck timed to 90 — retiming round required** |
| `LSN-1.4` | **Hands-on: train MNIST with PyTorch/Keras** (= "Hands on Neural Nets") | Mon 28 Sep 2026 | 1 h | 2 h (45 pre + 75 hw) | Tyler / Stefana | Live lab | Built (lab notebook + deck); **deck timed to 150 — retiming round required** |
| `LSN-1.5` | Conversational deep learning — NN, CNN, RL (= "Conversations on Deep Learning") | Mon 5 Oct 2026 | 1 h | 2 h (40 pre + 80 hw) | Tyler | Recorded segments + live Q&A/drill, delivered in the hour | Built (deck + notebook, timed to 60) |
| `LSN-1.6` | Data requirements, limitations & the pre-sales question bank (= "Data Requirements for ML") | Mon 12 Oct 2026 | 1 h | 2 h (40 pre + 80 hw) | Tyler + Vlad | Live | Built (deck + notebook, timed to 60); case brief still **GAP-5** |
| — | `ASM-1` — quiz + mock pre-sales conversation | **unscheduled** (not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Oct 12–16, after LSN-1.6) | 1 h | — | Tyler + Vlad | Live roleplay | **BUILD — GAP-6** |

**Module totals:** 6 × 1 h live = 6 h; 6 × 2 h out-of-session = 12 h; **18 h total**, plus ~1 h for `ASM-1` once scheduled.

---

### LSN-1.1 — The Five ML Jobs & the Nesting Doll

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 7 Sep 2026 | 1 h live + 2 h out-of-session | Tyler | `OUT-1.1` |

Spreadsheet alias: **"ML Use Cases."**

**Purpose:** The triage skill. When a client says "AI," do they mean a predictive algorithm or ChatGPT? Sort any ask into: sort it (classification), group it (clustering), guess a number (regression), give the odds (propensity), pick the next move (recommender). ML ⊃ deep learning ⊃ generative AI — the nesting doll.

**Pre-work (45 min):** Read the five-jobs deck sections (20); bring one real ask from a project you've been on plus a guess at which job it is (10); run the session notebook's per-job visual cells (15).

**Session outline:**
1. "When they say AI…" — the two meanings, with tells ("I want to *know* X" vs "I want to *converse/reason*") (15 min)
2. The five jobs, each with the sales-world example (buyer conversion: sort / spend: regress / close odds: propensity / next action: recommend) (25 min)
3. Triage drill: participants' own asks, sorted live by the group (20 min)

**Homework (75 min):** Triage five fresh asks in the notebook's drill workspace against the graded key (25); write the one-paragraph triage memo on your own ask (25); harvest and triage two real asks from VSP proposals/emails (25).

**Support material:** Built — deck `program/lessons/decks/LSN-1.1-five-ml-jobs.html` (canonical per SI-25); session notebook `notebooks/lessons/LSN-1.1_Five_ML_Jobs_Nesting_Doll.ipynb` (executed end to end). Original ML literacy deck remains the source (not in repo).

---

### LSN-1.2 — Model I/O: What Goes In, What Comes Out

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 14 Sep 2026 | 1 h live + 2 h out-of-session | Tyler | `OUT-1.2` |

Spreadsheet alias: **"ML Model Inputs and Outputs."**

**Purpose:** Tyler's bar: "what does each model take in, what does it kick out, and how do you interpret it." Labels vs features, a probability vs a class vs a number vs a ranking, and what a prediction actually looks like on screen.

**Pre-work (40 min):** Deck sections on model types and reading outputs (15); the "what does 0.73 mean" sentence (5); run the notebook's four output-safari fits yourself before the session (20).

**Session outline:**
1. Features and labels — what training data actually is (15 min)
2. Output safari: a classifier's probabilities, a regressor's number, a cluster assignment, a recommender's ranked list — real outputs from repo notebooks shown side by side (30 min)
3. Interpretation drill: "the model says 0.73 — what do you tell the client?" (15 min)

**Homework (80 min):** Client-safe reading + next question for each of the four safari output types (30); written answers to the 0.51 / 8.2 curveballs plus one from your own project (20); specify the model I/O for the ask you triaged in LSN-1.1 — feature columns, label column, output type and units (30).

**Support material:** Built — deck `program/lessons/decks/LSN-1.2-model-io.html`; session notebook `notebooks/lessons/LSN-1.2_Model_IO.ipynb` (live output safari + graded drill, executed end to end); `notebooks/supervised/`, `unsupervised/` as go-deeper references.

---

### LSN-1.3 — Grading Models

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 21 Sep 2026 | 1 h live + 2 h out-of-session | Tyler | `OUT-1.3` |

Spreadsheet alias: **"Grading Models"** (same title).

**Purpose:** "Is the model any good?" MAE as the average miss in real units; precision vs recall as two different kinds of wrong; the confusion matrix; AUC in one picture. Builds directly on the base-rate lesson (`LSN-0.3`).

**Pre-work (45 min):** Revisit LSN-0.3 base-rate notes (15); deck grading section (15); StatQuest "ROC and AUC, Clearly Explained!" — promoted from optional to mandatory when the AUC segment was compressed (15).

**Session outline (rescoped 2026-08-03 from 90 min to 60):**
1. MAE: average miss in units the client cares about — house-price example; the segment-breakdown trap named, worked in homework card A (12 min)
2. Precision/recall via the fraud detector from LSN-0.3; which error is expensive for *this* client? — two quick-fire cases, third relocated to homework (22 min)
3. Confusion matrix reading drill — one matrix hand-computed live, the degenerate always-say-no matrix read together (15 min)
4. AUC in one picture; when a client quotes "99% accuracy," what to ask (11 min)

**Homework (75 min):** Three model report cards — ship it or not, and why (40); the relocated confusion-matrix computation set, three matrices checked against the notebook's pinned arithmetic (20); the relocated threshold sweep — precision/recall at three thresholds and what AUC summarizes (15).

**Support material:** Built — deck `program/lessons/decks/LSN-1.3-grading-models.html`; session notebook `notebooks/lessons/LSN-1.3_Grading_Models.ipynb` (executed end to end). Go-deeper: `notebooks/foundations/06_Classifier_Algorithms.ipynb` (the earlier `foundations/12` citation was a name-based error — it's a runtime-timing notebook; BUILD_LOG LL-32).

---

### LSN-1.4 — Hands-On: Train MNIST

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 28 Sep 2026 | 1 h live lab + 2 h out-of-session | Tyler / Stefana | `OUT-1.4` |

Spreadsheet alias: **"Hands on Neural Nets"** (the MNIST lab).

**Purpose:** Vlad's explicit ask: "start up a Jupyter notebook… do that classical exercise [MNIST], use PyTorch." Everyone trains a real model, watches loss fall, and interprets the confusion matrix on their own results. Karpathy-spirit: see enough of the mechanics to believe it's "all linear algebra," without drowning.

**Pre-work (45 min, mandatory — lab won't wait):** Environment verified again and the smoke test run (15); Python refresher confirmed clean (from LSN-0.1 homework) (10); read the guided notebook's intro cells (20).

**Session outline (rescoped 2026-08-03 from 150 min to 60 — the module's hardest restructure):** the live hour buys the two things that need the room — nobody blocked on setup, and everybody watching their *own* loss fall. Everything downstream of a trained model runs solo (the notebook trains 11 models in ~6 s total).
1. Dataset tour, compressed: load from warm cache, shapes, digit grid, per-digit histogram (10 min)
2. Guided MLP build: fill in `Linear(784,128)` → ReLU → `Linear(128,10)`, loss, optimizer; print every weight-matrix shape (20 min)
3. Train loop — watch your loss fall from ≈2.3 to below 0.5. This is the checkpoint the hour exists for (20 min)
4. Wrap + homework launch: the whole supervised story, and a walk-through of the two relocated blocks (10 min)

**Relocated to homework (not cut):** evaluation + confusion-matrix reading, and the break-it-on-purpose degradation runs. The by-hand forward pass moved with them.

**Homework (75 min, artifact graded):** Evaluate your model — test accuracy, 10×10 confusion matrix, the three reading questions (25); break it on purpose at 10,000 → 1,000 → 100 → 10 examples and plot accuracy vs training-set size (25) — **this is also the graded "re-run with one isolated change" artifact, folded in so one notebook serves both**; write-up plus the 200-labeled-photos exit answer (15); the hand-computed forward pass matched to the model's output (10).

**Support material:** Built (**GAP-8** closed, Round 7) — guided fill-in lab for non-ML engineers, synthesized from `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` (MLP framing — but sklearn, no MNIST) and `02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` (PyTorch + MNIST — but CNN). Neither is a PyTorch MLP on MNIST as-is; this is a synthesis, not a light adaptation. Deck is timed to the old 150-min lab — retiming round required before delivery.

---

### LSN-1.5 — Conversational Deep Learning

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 5 Oct 2026 | 1 h live + 2 h out-of-session | Tyler | `OUT-1.5` |

Spreadsheet alias: **"Conversations on Deep Learning."**

**Purpose:** The vocabulary Vlad listed: neural network, CNN, deep learning, reinforcement learning — "to have a mini conversation about this and not look completely stupid." Anchored to the MNIST lab they just did: they've *trained* a neural net, so NN/CNN are now concrete.

**Pre-work (40 min):** Curated Karpathy excerpt (~15 min clip from ["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0)) (15); one-page cheat sheet (10); four draft client-safe sentences (5); re-open your own LSN-1.4 loss curve and confusion matrix — you narrate them in segment 1 (10).

**Session outline (already 60 — unchanged):**
1. What you trained in LSN-1.4 *was* a neural net — layers, weights, learning (15 min)
2. CNNs: why images want convolutions; one picture, no math (15 min)
3. RL: learning by reward — where it fits (games, robotics, RLHF teaser for MOD-2) (15 min)
4. Mini-conversation drills in pairs: 2-minute client explanations, peer-graded (15 min)

**Homework (80 min):** Record yourself delivering all four 2-minute explanations, self-score against the pair-drill rubric, revise the weakest (35); run the companion notebook's three demo props and write one plain-language sentence per prop (20); the warehouse-robotics RL preconditions memo — reward function, simulator, what you'd actually tell the client (25).

**Support material:** Built — `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` (session companion + drill workspace; carries the canonical one-page NN/CNN/DL/RL cheat sheet) and `program/lessons/decks/LSN-1.5-conversational-deep-learning.html` (16 slides, notes timed to 60). References: `notebooks/neural_networks/01`, `02`, `notebooks/reinforcement/01` — caveats disclosed in the companion (`02` downloads MNIST via `fetch_openml`, bypassing the warm cache; `reinforcement/01` is unseeded).

---

### LSN-1.6 — Data Requirements, Limitations & the Pre-Sales Question Bank

| Delivery date | Duration | Owner | Serves |
|---|---|---|---|
| Mon 12 Oct 2026 | 1 h live + 2 h out-of-session | Tyler + Vlad (case material) | `OUT-1.6` |

Spreadsheet alias: **"Data Requirements for ML."**

**Purpose:** Vlad quoted this back from 6MAP: "I need data in order for the model — it was a truism, but it's the truth. It can only infer to a certain point." This lesson turns limitations into the pre-sales questions that make VSP look sharp: What data exists? How labeled? How much? How fresh? What's the cost of a wrong answer?

**Pre-work (40 min):** Read the anonymized case brief (from Vlad/Dorel — the construction-site photo/video prospect) (25); skim the starter question bank (5); re-open your LSN-1.4 degradation curve and write the "enough" number it implies (10).

**Session outline (already 60 — unchanged):**
1. The data reality checklist: exists / labeled / enough / fresh / legal to use (20 min)
2. Case walkthrough: construction-site completion detection — what's the ML job, what data does it need, where would it break? (25 min, Dorel's rule in action)
3. Build the question bank together — the module's take-home artifact (15 min)

**Homework (80 min):** Apply the refined question bank to one prospect or project you know first-hand, with the honest-limitation paragraph — the graded artifact and part of the ASM-1 evidence (50); fill the notebook's five-check coverage matrix and run the advisor pre-check (20); draft the three questions you'd open that discovery call with, in order (10).

**Support material:** Built — `notebooks/lessons/LSN-1.6_Data_Requirements_Presales_Question_Bank.ipynb` (checklist companion + walkthrough workspace with marked GAP-5 slots + homework template & advisor) and `program/lessons/decks/LSN-1.6-data-requirements.html` (18 slides, notes timed to 60). The anonymized case brief itself remains **GAP-5** (Vlad/Dorel input); every place it lands is explicitly marked in both artifacts, and the walkthrough runs today on labeled placeholders.

---

## Checkpoint — ASM-1

| Field | Value |
|---|---|
| **Format** | Async quiz (~15 scenario questions, 30 min) **+ live mock pre-sales conversation** (15 min/participant, Vlad or Dorel plays the client) |
| **Delivery date** | **Unscheduled** (not on the program spreadsheet — needs a calendar slot at the next review call; proposed: week of Oct 12–16, after LSN-1.6) |
| **Verifies** | `OUT-1.1`–`OUT-1.3`, `OUT-1.5`, `OUT-1.6` (conversation, rubric-graded); `OUT-1.4` (LSN-1.4 homework artifact) |
| **Pass bar** | Quiz 80% + rubric "client-ready" on triage and honesty-about-limitations dimensions |
| **Gate** | Must pass to start `MOD-2` |
| **Status** | **BUILD — GAP-6** (quiz + conversation rubric) |

The mock conversation is the point of the module — it rehearses the exact skill GOAL-1 names. The spreadsheet locked 2026-08-03 lists six MOD-1 rows and no checkpoint row; `ASM-1` is kept here on the module's authority and carried as an open scheduling item, because the `MOD-2` gate depends on it.

## Traceability

| Outcome | Served by | Verified by |
|---|---|---|
| `OUT-1.1` | LSN-1.1 | ASM-1 (quiz + conversation) |
| `OUT-1.2` | LSN-1.2 | ASM-1 (quiz) |
| `OUT-1.3` | LSN-1.3 | ASM-1 (quiz + homework) |
| `OUT-1.4` | LSN-1.4 | ASM-1 (artifact) |
| `OUT-1.5` | LSN-1.5 | ASM-1 (conversation) |
| `OUT-1.6` | LSN-1.6 | ASM-1 (conversation + question bank) |

## Build List

| ID | Item | Owner | Needed by |
|---|---|---|---|
| `GAP-8` | ~~Guided MNIST lab notebook~~ **CLOSED** — built Round 7 (`notebooks/lessons/LSN-1.4_Hands_On_Train_MNIST.ipynb`, BUILD_LOG) | Tyler (+ Stefana review) | done |
| `GAP-5` (share) | Construction-site case brief (question bank template now built — see LSN-1.6 notebook) | Vlad/Dorel + Tyler | **Mon 5 Oct 2026** — one week before LSN-1.6, so it ships with that lesson's pre-work |
| `GAP-6` (share) | ASM-1 quiz + mock-conversation rubric | Tyler | **Mon 12 Oct 2026** — before the ASM-1 slot, once that slot exists |
| `RETIME-1.3` | LSN-1.3 deck + notebook retimed from 90 min to the 60-min session | Tyler | before Mon 21 Sep 2026 |
| `RETIME-1.4` | LSN-1.4 deck + lab notebook resequenced for the 60-min live hour and the two relocated homework blocks | Tyler (+ Stefana review) | before Mon 28 Sep 2026 |
