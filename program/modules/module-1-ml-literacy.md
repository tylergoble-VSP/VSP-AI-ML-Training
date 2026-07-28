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
| **Week** | 1–2 |
| **Total effort** | ~9 h sessions incl. checkpoint + ~3 h pre-work/homework |
| **Module owner** | Tyler Goble |
| **Prerequisite** | `ASM-0` passed |
| **Checkpoint** | `ASM-1` |

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

| ID | Lesson | Duration | Owner | Format | Material status |
|---|---|---|---|---|---|
| `LSN-1.1` | The five ML jobs & the nesting doll | 1 h | Tyler | Live | Exists (ML literacy deck) |
| `LSN-1.2` | Model I/O — inputs, outputs, interpretation | 1 h | Tyler | Live | Exists (deck + notebooks) |
| `LSN-1.3` | Grading models — MAE, precision/recall, AUC | 1.5 h | Tyler | Live | Exists (deck + `foundations/12`) |
| `LSN-1.4` | **Hands-on: train MNIST with PyTorch/Keras** | 2.5 h | Tyler / Stefana | Live lab | Build (**GAP-8**) |
| `LSN-1.5` | Conversational deep learning — NN, CNN, RL | 1 h | Tyler | Recorded (45 min) + live Q&A/drill (15 min) | Exists (notebooks as refs) |
| `LSN-1.6` | Data requirements, limitations & the pre-sales question bank | 1 h | Tyler + Vlad | Live | **BUILD — GAP-5** |
| — | `ASM-1` — quiz + mock pre-sales conversation | 1 h | Tyler + Vlad | Live roleplay | **BUILD — GAP-6** |

---

### LSN-1.1 — The Five ML Jobs & the Nesting Doll

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-1.1` |

**Purpose:** The triage skill. When a client says "AI," do they mean a predictive algorithm or ChatGPT? Sort any ask into: sort it (classification), group it (clustering), guess a number (regression), give the odds (propensity), pick the next move (recommender). ML ⊃ deep learning ⊃ generative AI — the nesting doll.

**Pre-work (~30 min):** Read the ML literacy deck through the five-jobs section; bring one real ask from a project you've been on and a guess at which job it is.

**Session outline:**
1. "When they say AI…" — the two meanings, with tells ("I want to *know* X" vs "I want to *converse/reason*") (15 min)
2. The five jobs, each with the sales-world example (buyer conversion: sort / spend: regress / close odds: propensity / next action: recommend) (25 min)
3. Triage drill: participants' own asks, sorted live by the group (20 min)

**Homework:** None (pre-work for 1.2 instead).

**Support material:** Exists — ML literacy deck.

---

### LSN-1.2 — Model I/O: What Goes In, What Comes Out

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-1.2` |

**Purpose:** Tyler's bar: "what does each model take in, what does it kick out, and how do you interpret it." Labels vs features, a probability vs a class vs a number vs a ranking, and what a prediction actually looks like on screen.

**Pre-work (~20 min):** Deck sections on model types and reading outputs.

**Session outline:**
1. Features and labels — what training data actually is (15 min)
2. Output safari: a classifier's probabilities, a regressor's number, a cluster assignment, a recommender's ranked list — real outputs from repo notebooks shown side by side (30 min)
3. Interpretation drill: "the model says 0.73 — what do you tell the client?" (15 min)

**Homework:** None.

**Support material:** Exists — deck + outputs pulled from `notebooks/supervised/`, `unsupervised/` (rendered, not run live).

---

### LSN-1.3 — Grading Models

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-1.3` |

**Purpose:** "Is the model any good?" MAE as the average miss in real units; precision vs recall as two different kinds of wrong; the confusion matrix; AUC in one picture. Builds directly on the base-rate lesson (`LSN-0.3`).

**Pre-work (~30 min):** Rewatch base-rate segment notes; deck grading section.

**Session outline:**
1. MAE: average miss in units the client cares about — house-price example (20 min)
2. Precision/recall via the fraud detector from LSN-0.3; which error is expensive for *this* client? (30 min)
3. Confusion matrix reading drill (20 min)
4. AUC in one picture; when a client quotes "99% accuracy," what to ask (20 min)

**Homework:** Given three model report cards, write one paragraph each: ship it or not, and why.

**Support material:** Exists — deck + `notebooks/foundations/12_Analytics_Performance.ipynb`.

---

### LSN-1.4 — Hands-On: Train MNIST

| Duration | Owner | Serves |
|---|---|---|
| 2.5 h (live lab) | Tyler / Stefana | `OUT-1.4` |

**Purpose:** Vlad's explicit ask: "start up a Jupyter notebook… do that classical exercise [MNIST], use PyTorch." Everyone trains a real model, watches loss fall, and interprets the confusion matrix on their own results. Karpathy-spirit: see enough of the mechanics to believe it's "all linear algebra," without drowning.

**Pre-work (~45 min, mandatory — lab won't wait):** Environment verified again; Python refresher done (from LSN-0.1 homework); read the guided notebook's intro cells.

**Session outline:**
1. Dataset tour: what 60,000 labeled digits look like (15 min)
2. Guided build: load data → define a small MLP → train loop → watch loss (60 min)
3. Evaluate: accuracy, confusion matrix — which digits confuse the model and why (30 min)
4. Break it on purpose: shrink the training set, watch performance fall — data requirements made visceral (foreshadows LSN-1.6) (30 min)
5. Wrap: what you just did is the whole supervised-learning story (15 min)

**Homework (artifact, graded):** Re-run with one change (layer size, epochs, training-set size) and submit the notebook + three sentences on what changed and why.

**Support material:** Build (**GAP-8**) — new guided fill-in lab for non-ML engineers, synthesized from `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` (MLP framing — but sklearn, no MNIST) and `02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` (PyTorch + MNIST — but CNN). Neither is a PyTorch MLP on MNIST as-is; this is a synthesis, not a light adaptation.

---

### LSN-1.5 — Conversational Deep Learning

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-1.5` |

**Purpose:** The vocabulary Vlad listed: neural network, CNN, deep learning, reinforcement learning — "to have a mini conversation about this and not look completely stupid." Anchored to the MNIST lab they just did: they've *trained* a neural net, so NN/CNN are now concrete.

**Pre-work (~30 min):** Curated Karpathy excerpt (~15 min clip) + one-page cheat sheet.

**Session outline:**
1. What you trained in LSN-1.4 *was* a neural net — layers, weights, learning (15 min)
2. CNNs: why images want convolutions; one picture, no math (15 min)
3. RL: learning by reward — where it fits (games, robotics, RLHF teaser for MOD-2) (15 min)
4. Mini-conversation drills in pairs: 2-minute client explanations, peer-graded (15 min)

**Homework:** None.

**Support material:** Exists as reference — `notebooks/neural_networks/*`, `notebooks/reinforcement/*`; cheat sheet to be extracted at lesson-plan time.

---

### LSN-1.6 — Data Requirements, Limitations & the Pre-Sales Question Bank

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler + Vlad (case material) | `OUT-1.6` |

**Purpose:** Vlad quoted this back from 6MAP: "I need data in order for the model — it was a truism, but it's the truth. It can only infer to a certain point." This lesson turns limitations into the pre-sales questions that make VSP look sharp: What data exists? How labeled? How much? How fresh? What's the cost of a wrong answer?

**Pre-work (~30 min):** Read the anonymized case brief (from Vlad/Dorel — the construction-site photo/video prospect).

**Session outline:**
1. The data reality checklist: exists / labeled / enough / fresh / legal to use (20 min)
2. Case walkthrough: construction-site completion detection — what's the ML job, what data does it need, where would it break? (25 min, Dorel's rule in action)
3. Build the question bank together — the module's take-home artifact (15 min)

**Homework:** Apply the question bank to one prospect or project you know; submit filled bank.

**Support material:** **BUILD (`GAP-5`)** — case brief needs Vlad/Dorel input; question bank template new.

---

## Checkpoint — ASM-1

| Field | Value |
|---|---|
| **Format** | Async quiz (~15 scenario questions, 30 min) **+ live mock pre-sales conversation** (15 min/participant, Vlad or Dorel plays the client) |
| **Verifies** | `OUT-1.1`–`OUT-1.3`, `OUT-1.5`, `OUT-1.6` (conversation, rubric-graded); `OUT-1.4` (LSN-1.4 homework artifact) |
| **Pass bar** | Quiz 80% + rubric "client-ready" on triage and honesty-about-limitations dimensions |
| **Gate** | Must pass to start `MOD-2` |
| **Status** | **BUILD — GAP-6** (quiz + conversation rubric) |

The mock conversation is the point of the module — it rehearses the exact skill GOAL-1 names.

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
| `GAP-8` | Guided MNIST lab notebook (synthesized from `neural_networks/01–02` — see LSN-1.4) | Tyler (+ Stefana review) | Week 2 |
| `GAP-5` (share) | Construction-site case brief + question bank template | Vlad/Dorel + Tyler | Week 2 |
| `GAP-6` (share) | ASM-1 quiz + mock-conversation rubric | Tyler | End of Week 2 |
