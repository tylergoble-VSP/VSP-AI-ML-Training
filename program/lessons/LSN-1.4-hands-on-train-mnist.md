---
name: LSN-1.4-hands-on-train-mnist
description: Personally train an MNIST digit classifier in PyTorch, watch the loss fall, read your own confusion matrix, and see performance collapse when the data shrinks.
module: MOD-1
delivery_date: 2026-09-28
serves: OUT-1.4
duration: 1
prework_time: 45
homework_time: 75
owner: Tyler / Stefana
status: draft
---

# LSN-1.4 — Hands-On: Train MNIST

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.4` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live lab |
| **Verified by** | `ASM-1` (artifact — the LSN-1.4 homework notebook) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 28 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Hands on Neural Nets."**

## Narrative

This session kills the misconception that training a model is arcane. Every participant loads 70,000 labeled digits, defines a small MLP, runs a training loop, and watches loss fall on their own machine — Karpathy-spirit: enough mechanics (weight matrix shapes, one forward pass by hand) to believe "it's all linear algebra" without drowning in calculus. It calls back to LSN-0.1 (the environment they verified), LSN-0.2 (the label distribution is a sampling question), and LSN-1.3 (the confusion matrix they learned to read is now *their* confusion matrix). The break-it-on-purpose finale — shrinking the training set and watching accuracy collapse — is the setup for LSN-1.6's "no data, no model," and having trained a real neural net makes LSN-1.5's vocabulary concrete.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-verify environment per `ACTIVATE_VENV.md`; run the lab notebook's cell 0 smoke test (imports `torch`, `sklearn`, `matplotlib`; triggers the MNIST download so the lab doesn't wait on the network) | 15 | Screenshot of the smoke-test cell's success output |
| 2 | Confirm your LSN-0.1 Python refresher homework runs clean — the lab assumes you can read a `for` loop over batches without help | 10 | The completed refresher notebook |
| 3 | Read the guided lab notebook's intro cells (Learning Objectives + Theory & Mechanics summary adapted from `neural_networks/01–02`) | 20 | One written question about anything unclear — collected at the door |

## Session Plan

Rescoped 2026-08-03 from a 150-min live lab to the spreadsheet's 60-min hour. **The reasoning:** only two things genuinely need a room full of people and an instructor — (a) nobody sitting stuck on an environment or a shape error, and (b) every participant watching *their own* loss fall, which is the moment the abstraction becomes real and cannot be recovered from a recording. Everything downstream of a trained model is solo work that the notebook already supports: it trains 11 models in ~6 s of total compute, every guided cell has a paste-ready canonical twin, and every drill has a built-in grader. So evaluation, the confusion matrix and the break-it runs move out of the room and into structured homework with checkpoints — **relocated, not deleted**; the section-by-section mapping is in Homework below.

| Segment | Time | Method | Detail |
|---|---|---|---|
| Dataset tour, compressed | 10 | demo + lab | **Where:** notebook §"Segment 1 — Dataset tour" (cells 7–12). Load MNIST from the pre-warmed local cache — `datasets.MNIST(root=~/.cache/vsp-training-data)` (SI-24(b), BUILD_LOG Round 7) — print train/test sizes (60,000/10,000), render the 5×5 digit grid, show the per-digit histogram. The LSN-1.2 "a digit image *is* a feature row" callback and the LSN-0.2 balance callback are stated in one line each and read properly in homework; live they are captions, not discussions. **Lab checkpoint:** shapes printed, digit grid on screen, for everyone. **Likely failure:** cache missing despite pre-work. **Recovery:** instructor's pre-downloaded copy on the shared drive + the notebook's synthetic-data fallback; nobody debugs networking live. |
| Guided build: data → model → loss | 20 | lab | **Where:** §"Segment 2" steps 1–3 (cells 14–21). Subset + `DataLoader`; the fill-in MLP `nn.Linear(784,128)` → ReLU → `nn.Linear(128,10)`; `CrossEntropyLoss` + Adam, with the loss-at-init check against `2.3026` that catches most wiring bugs before a single epoch runs. **Lab checkpoint:** everyone has a model object and a loss at init near 2.30. **Likely failure:** shape mismatch — 28×28 fed without flattening, or labels not `long`. **Recovery:** the shape-debug ritual (print `.shape` at every boundary); the STEP-1/2/3 canonical cells are paste-ready for anyone more than 3 min behind — at this cadence the instruction is to paste and keep moving, not to debug. |
| The train loop — **your loss falling** | 20 | lab | **Where:** §"Segment 2" step 4 + the loss curve + the shape chain (cells 22–27). Order the five lines of the loop, run 3 epochs on the 10k subset, plot the curve, then print every array in the model and the shape chain from image to answer — the "it really is all linear algebra" beat, kept live because it costs one cell and it is the payoff of the build. **This is the checkpoint the hour exists for:** every participant sees ≈2.3 fall below 0.5 by epoch 3 on their own machine. Nobody leaves the room without it — an instructor sweep confirms person by person, and the canonical `train()` cell is the pressure valve. **Likely failure:** the loop lines in the wrong order (loss computed after the step). **Recovery:** paste the canonical cell, then read the correct order aloud against what they had. |
| Wrap + homework launch | 10 | talk + discussion | **Where:** §"Segment 5" (cell 49) and the homework walkthrough. What you just did — data → model → loss → gradient descent — is the spine of the whole supervised story; map back to LSN-1.1's "sort it." Then, explicitly, the handoff that makes the short hour work: walk the four homework blocks on screen, name the trap each one contains (evaluating on training data; forgetting `fresh_model()`), and state the deadline. Tee-ups: LSN-1.5 ("you have now trained a neural network") and LSN-1.6 ("bring your degradation curve — that session opens on it"). |

**Timing check:** 10 + 20 + 20 + 10 = 60 min = 1 h — matches the spreadsheet contract.

**What this costs, stated honestly:** the confusion-matrix reading drill loses its live group energy, and the break-it runs lose the shared gasp when accuracy collapses at 10 examples. Mitigation: LSN-1.6 opens on the saved degradation curve (the notebook already writes it out for exactly this handoff), so the collective moment happens there instead — one lesson later, with the client case in front of it.

## Client Tie-In (Dorel's rule)

The break-it block — homework task 2 since the 2026-08-03 rescope — is the pre-sales "no data, no model" reality that Vlad carried out of 6MAP ("I need data in order for the model — it was a truism, but it's the truth"). The construction-site completion-detection prospect (the LSN-1.6 case) is exactly this lab's final chart: a client with a few hundred site photos asking for detection is a point on the left edge of the accuracy-vs-training-size curve every participant just plotted themselves. When a client says "we have some data," this lab is why VSP's next question is "how much, and how labeled?" — asked from experience, not from a slide.

## Homework

**75 min**, all in the same lab notebook you trained in, on the model you trained in the room. Tasks 1 and 2 are the old segments 3 and 4 relocated by the 60-min rescope; task 4 is the by-hand forward pass moved out of the build. **Task 2 also absorbs the module's graded artifact** — the old "re-run with exactly one change" homework asked for a training-set-size variant, which is precisely what the degradation runs are, so one notebook now serves both and the budget stays at 2 h instead of ballooning to 100 min of homework.

| # | Task | Time | Checkpoint |
|---|---|---|---|
| 1 | **Relocated: evaluate your model.** Notebook §"Segment 3" (cells 30–39). Compute held-out test accuracy — and run the on-purpose trap cell that shows what training-set accuracy would have told you instead. Build the 10×10 confusion matrix, read the per-digit report card (LSN-1.3 callback), look at the actual misclassified images, then complete the three-question reading drill in its workspace and run the grader: which digit does your model most mistake for a 9; is that a precision or a recall problem for class 9; would you ship this for reading handwritten invoice totals, and what does one 4→9 error cost. Finish with the all-60,000-digits run and note the one number that moves | 25 min | Drill workspace passes its grader; you can name your worst digit pair (typically 4/9 or 3/5) |
| 2 | **Relocated + graded artifact.** Notebook §"Segment 4" (cells 41–47). Run the re-initialization trap cell first, then the four runs at 10,000 → 1,000 → 100 → 10 with fixed epochs, then the equal-gradient-steps control run that answers the client objection ("maybe it just trained less"). Plot the degradation curve and save it — LSN-1.6 opens on it. **This is your graded one-change artifact:** training-set size is the single isolated change, and the four-row table is its comparison | 25 min | 4-row size-vs-accuracy table + control run + curve saved to disk |
| 3 | **The write-up** (graded with task 2). Three sentences: what you changed, what moved — *which* digits, *which* direction — and why. Plus the exit question from §"Segment 5": a client says they have 200 labeled photos; what does your curve say? | 15 min | Three sentences + exit answer, submitted referencing `LSN-1.4` |
| 4 | **Relocated: one forward pass by hand** (cell 28). Reproduce the model's output for a single digit with plain matmuls — torch, then numpy, then the model itself — and confirm all three agree | 10 min | Three matching outputs; you have seen that there is no magic between the pixels and the answer |

**Grading standard (unchanged in substance):** notebook runs top to bottom; the change is isolated and named; the three sentences correctly attribute the metric shift to the change (not "it got better" — *which* digits, *which* direction, *why*). Reviewed at ASM-1 as the `OUT-1.4` evidence.

**Time accounting:** pre-work 45 min + homework 75 min = 2 h out-of-session budget.

**Why 75 min of homework is realistic here:** compute is not the constraint — the notebook's 11 model trainings total ~6 s. The time is reading outputs, filling graded workspaces, and writing. Every relocated cell already exists, is executed end to end, and carries its own grader or answer key, which is what makes solo completion safe without an instructor in the room.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Guided MNIST lab notebook** — GAP-8 synthesis, executed end to end (11 trained models, ~6 s total; degradation curve saved for LSN-1.6) | exists | `notebooks/lessons/LSN-1.4_Hands_On_Train_MNIST.ipynb` |
| **Session deck** — 11 slides w/ per-segment checkpoints, likely failures, recovery moves in the notes; retimed 2026-08-03 to the 60-min live hour (relocated segments re-purposed as the "tonight, solo" homework launch) | exists | `program/lessons/decks/LSN-1.4-hands-on-mnist.html` |
| Source notebook — perceptron & MLP concepts | exists | `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` |
| Source notebook — MNIST load, PyTorch training loop, evaluation | exists | `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` |
| Pre-downloaded MNIST fallback (shared-drive copy of `~/.cache/vsp-training-data/`) | build | shared drive — location set at delivery prep; notebook also carries a synthetic-digit fallback that keeps every cell runnable offline |
| Optional pre-work video: 3Blue1Brown, "But what is a neural network?" — Deep Learning chapter 1 | exists | [youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk) |
| Environment setup guide | exists | `ACTIVATE_VENV.md` |

## Delivery Notes

To be filled after each delivery: what landed, what dragged, timing reality (watch the 20-min train-loop segment — the hour's whole purpose is that everyone's loss falls inside it; the paste-ready canonical cells are the pressure valve, and at this cadence pasting is the correct move, not a failure). Feeds the MOD-1 retro; retro findings that change scope update `program/modules/module-1-ml-literacy.md` first.

**Rescope note (2026-08-03):** the **deck was retimed on 2026-08-03** — live speaker-note timings now sum to 10 + 20 + 20 + 10 = 60, and the evaluation / break-it / by-hand-pass slides are re-purposed as the homework launch (their checkpoints, likely failures and recovery moves survive as homework guidance in the notes); **the notebook is still pending.** Specifically: the notebook's segment headers still read *(15 min)* / *(60 min)* / *(30 min)* / *(30 min)* / *(15 min)* and cells 29, 40 and 51 still frame segments 3 and 4 as live and the one-change run as separate homework — the retiming pass must relabel segments 3 and 4 as homework blocks, fold the cell 51–53 homework machinery into the segment-4 narrative, and reprice the live headers to 10/20/20/10. This is the largest single retiming job in MOD-1.

**Open question for the next review call:** a 60-min first exposure to PyTorch is tight even with everything downstream relocated. If the guinea-pig run (Mazilu, TBC) shows the room cannot reach a falling loss inside 40 minutes of build-plus-train, the fallback to propose is a second 1 h slot rather than reinstating the 2.5 h block — two hours on the spreadsheet's own terms, not one exception to it.
