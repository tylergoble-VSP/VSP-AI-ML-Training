---
name: LSN-1.4-hands-on-train-mnist
description: Personally train an MNIST digit classifier in PyTorch, watch the loss fall, read your own confusion matrix, and see performance collapse when the data shrinks.
module: MOD-1
serves: OUT-1.4
duration: 2.5
prework_time: 45
owner: Tyler / Stefana
status: draft
---

# LSN-1.4 — Hands-On: Train MNIST

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.4` |
| **Duration** | 2.5 h session + 45 min pre-work |
| **Format** | Live lab |
| **Verified by** | `ASM-1` (artifact — the LSN-1.4 homework notebook) |

## Narrative

This session kills the misconception that training a model is arcane. Every participant loads 70,000 labeled digits, defines a small MLP, runs a training loop, and watches loss fall on their own machine — Karpathy-spirit: enough mechanics (weight matrix shapes, one forward pass by hand) to believe "it's all linear algebra" without drowning in calculus. It calls back to LSN-0.1 (the environment they verified), LSN-0.2 (the label distribution is a sampling question), and LSN-1.3 (the confusion matrix they learned to read is now *their* confusion matrix). The break-it-on-purpose finale — shrinking the training set and watching accuracy collapse — is the setup for LSN-1.6's "no data, no model," and having trained a real neural net makes LSN-1.5's vocabulary concrete.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-verify environment per `ACTIVATE_VENV.md`; run the lab notebook's cell 0 smoke test (imports `torch`, `sklearn`, `matplotlib`; triggers the MNIST download so the lab doesn't wait on the network) | 15 | Screenshot of the smoke-test cell's success output |
| 2 | Confirm your LSN-0.1 Python refresher homework runs clean — the lab assumes you can read a `for` loop over batches without help | 10 | The completed refresher notebook |
| 3 | Read the guided lab notebook's intro cells (Learning Objectives + Theory & Mechanics summary adapted from `neural_networks/01–02`) | 20 | One written question about anything unclear — collected at the door |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Dataset tour | 15 | demo + lab | **Where:** lab notebook §"Loading Dataset: MNIST Handwritten Digits" (adapted from `02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` §Implementation). Load MNIST from the pre-warmed local cache — `datasets.MNIST(root=~/.cache/vsp-training-data)`, superseding the earlier `fetch_openml` design (SI-24(b), BUILD_LOG Round 7) — print the train/test sizes (60,000/10,000), render a 5×5 grid of digits with labels, plot the per-digit count histogram (LSN-0.2 callback: is this sample balanced?). **Lab checkpoint:** everyone has the shape printed and the digit grid rendered. **Likely failure:** OpenML download blocked (proxy / no network) despite pre-work. **Recovery:** instructor's pre-downloaded `.npz` on the shared drive + the notebook's built-in synthetic-data fallback cell; nobody debugs networking live. |
| Guided MLP build + train loop | 60 | lab | **Where:** §"Define the Model" and §"Training" (MLP concepts from `01_NeuralNetworks_Perceptron_MLP.ipynb` §Multilayer Perceptron; PyTorch pipeline from `02` §Training). Fill-in build: `nn.Linear(784, 128)` → ReLU → `nn.Linear(128, 10)`, `CrossEntropyLoss`, Adam; train 3 epochs on a 10k subset, print epoch loss, plot the loss curve (§Learning Curve pattern from `01`). The linear-algebra moment: print every weight matrix shape, then compute one forward pass by hand as `x @ W1.T + b1` and match it to the model's output. **Lab checkpoint:** everyone has a model training with loss visibly falling (≈2.3 → below 0.5 by epoch 3). **Likely failure:** shape mismatch — feeding 28×28 without flattening, or labels not `long` dtype. **Recovery:** the rehearsed shape-debug ritual (print `.shape` at every layer boundary); a known-good model cell ready to paste for anyone more than 5 min behind. |
| Evaluate: accuracy + confusion matrix | 30 | lab + drill | **Where:** §"Evaluation" (adapted from `02` §Evaluation). Compute held-out test accuracy (expect ~93% on the 10k training subset at this config; ≥95% requires the full 60,000 — and that gap is deliberately segment 4's setup), build the 10×10 confusion matrix with labeled axes. Reading drill, LSN-1.3 callback — checkpoint questions asked live: "Which digit does your model most mistake for a 9?" "Is that a precision or a recall problem for class 9?" "Would you ship this for reading handwritten invoice totals? What's the cost of one 4→9 error?" **Lab checkpoint:** everyone has test accuracy + a rendered confusion matrix and can name their model's worst digit pair (typically 4/9 or 3/5). **Likely failure:** evaluating on training data ("I got 99.8%!") or transposed matrix axes. **Recovery:** the notebook's plotting helper hard-labels true-vs-predicted axes; suspicious scores get the "which loader did you use?" question first. |
| Break it on purpose | 30 | lab + drill | **Where:** §"Break It: Starve the Model" (new section, built for GAP-8). Re-initialize and retrain at 10,000 → 1,000 → 100 → 10 training examples, fixed epochs; record test accuracy each run; plot accuracy vs training-set size. This is LSN-1.6's "no data, no model" made visceral — keep the curve, it returns in that session. **Lab checkpoint:** everyone has the 4-row size-vs-accuracy table and the degradation curve plotted. **Likely failure:** forgetting to re-initialize the model, so run n fine-tunes run n−1's weights and the curve looks flat. **Recovery:** the `fresh_model()` helper cell everyone must call per run; if time is tight, drop the 10,000 row and start at 1,000. |
| Wrap: the whole supervised story | 15 | talk + discussion | **Where:** §"Summary & Key Takeaways". What you just did — data → model → loss → gradient descent → evaluation — *is* the entire supervised-learning story; everything else is scale. Map back to the five ML jobs (LSN-1.1: this was "sort it"). Tee-ups: LSN-1.5 ("you have now trained a neural network — next session we get the vocabulary to say so to a client") and LSN-1.6 (bring your degradation curve). **Lab checkpoint:** exit question, one sentence per person — "a client says they have 200 labeled photos; what does your curve say?" |

**Timing check:** 15 + 60 + 30 + 30 + 15 = 150 min = 2.5 h — matches the contract duration.

## Client Tie-In (Dorel's rule)

The break-it segment is the pre-sales "no data, no model" reality that Vlad carried out of 6MAP ("I need data in order for the model — it was a truism, but it's the truth"). The construction-site completion-detection prospect (the LSN-1.6 case) is exactly this lab's final chart: a client with a few hundred site photos asking for detection is a point on the left edge of the accuracy-vs-training-size curve every participant just plotted themselves. When a client says "we have some data," this lab is why VSP's next question is "how much, and how labeled?" — asked from experience, not from a slide.

## Homework

**Artifact (graded, references LSN-1.4; reviewed at ASM-1):** Re-run the lab with exactly one change — layer width, number of epochs, or training-set size — and submit the notebook plus three sentences: what you changed, what moved (accuracy and/or confusion matrix), and why. **Grading standard:** notebook runs top to bottom; the change is isolated and named; the three sentences correctly attribute the metric shift to the change (not "it got better" — *which* digits, *which* direction, *why*).

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Guided MNIST lab notebook** — GAP-8 synthesis, executed end to end (11 trained models, ~6 s total; degradation curve saved for LSN-1.6) | exists | `notebooks/lessons/LSN-1.4_Hands_On_Train_MNIST.ipynb` |
| **Session deck** — 11 slides w/ per-segment checkpoints, likely failures, recovery moves in the notes | exists | `program/lessons/decks/LSN-1.4-hands-on-mnist.html` |
| Source notebook — perceptron & MLP concepts | exists | `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` |
| Source notebook — MNIST load, PyTorch training loop, evaluation | exists | `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` |
| Pre-downloaded MNIST fallback (shared-drive copy of `~/.cache/vsp-training-data/`) | build | shared drive — location set at delivery prep; notebook also carries a synthetic-digit fallback that keeps every cell runnable offline |
| Optional pre-work video: 3Blue1Brown, "But what is a neural network?" — Deep Learning chapter 1 | exists | (verify at delivery prep) |
| Environment setup guide | exists | `ACTIVATE_VENV.md` |

## Delivery Notes

To be filled after each delivery: what landed, what dragged, timing reality (watch the 60-min guided build — it is the segment most likely to overrun; the paste-ready known-good cells are the pressure valve). Feeds the MOD-1 retro; retro findings that change scope update `program/modules/module-1-ml-literacy.md` first.
