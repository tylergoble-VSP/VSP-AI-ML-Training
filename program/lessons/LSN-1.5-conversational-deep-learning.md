---
name: LSN-1.5-conversational-deep-learning
description: Hold a two-minute, jargon-free client exchange on neural networks, CNNs, deep learning, and reinforcement learning — anchored to the neural net you personally trained in LSN-1.4.
module: MOD-1
delivery_date: 2026-10-05
serves: OUT-1.5
duration: 1
prework_time: 40
homework_time: 80
owner: Tyler Goble
status: draft
---

# LSN-1.5 — Conversational Deep Learning: NN, CNN, RL

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.5` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Recorded + Q&A |
| **Verified by** | ASM-1 (mock pre-sales conversation) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 5 October 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Conversations on Deep Learning."**

## Narrative

Kills the fear of the vocabulary. You are not learning what a neural network is from a slide — you *trained one* in the LSN-1.4 MNIST lab, watched its loss fall, and read its confusion matrix; this lesson just gives you the words for what you already did. Installs Vlad's bar verbatim: "have a mini conversation about this and not look completely stupid" — NN, CNN, deep learning, RL, each explainable in two plain-language minutes. The pair drill is a direct rehearsal for the ASM-1 mock pre-sales conversation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch the curated ~15-min excerpt from Andrej Karpathy, ["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0) (Neural Networks: Zero to Hero) — excerpt selection at delivery prep | 15 min | One question the excerpt left you with |
| 2 | Read the one-page NN/CNN/DL/RL cheat sheet | 10 min | Nothing to submit |
| 3 | Draft one client-safe sentence for each of the four terms | 5 min | Your four sentences — raw material for the pair drill |
| 4 | Re-open your own LSN-1.4 loss curve and confusion matrix — segment 1 asks you to narrate them, not watch someone else's | 10 min | Both charts open on your screen at session start |

**Pre-work total: 40 min.**

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| What you trained *was* a neural net | 15 min | recorded talk | Replay of the LSN-1.4 lab in vocabulary: the MLP you built is layers of weighted sums plus squashing functions; "training" was nudging weights until outputs matched labels; the falling loss curve was learning. "Deep learning" = the same thing with many layers, so the network learns its own features instead of being handed them. Reference build: `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb`. |
| CNNs: why images want convolutions | 15 min | recorded talk | One picture, no math: a small pattern-detector (edge, corner, texture) slid across the whole image, layers stacking detectors into shapes into objects. Why that beats a plain MLP on pixels: reuse and locality. This is the architecture the construction-site photo prospect would need. Reference: `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb`. |
| RL: learning by reward | 15 min | recorded talk | No labels — an agent acts, gets a reward, adjusts. Where it earns its keep: games, robotics, route/sequence optimization — anywhere you can fail cheaply a million times (usually a simulator). One-slide teaser: RLHF, the RL that shaped the LLMs in MOD-2. Reference: `notebooks/reinforcement/01_Reinforcement_QLearning.ipynb`. |
| Live Q&A + pair drill | 15 min | drill (live) | Q&A on the recording (5 min), then pairs: each person draws one prompt below, delivers the 2-minute explanation to their partner playing the named client, partner scores against the rubric, swap. Two deliveries fit — one per partner (5 min Q&A + 2 × (2 min delivery + 1 min scoring) + 4 min whole-group = 15); instructor pulls one strong and one shaky delivery for whole-group feedback. |

**Timing check:** 15 + 15 + 15 + 15 = 60 min = 1 h — matches the spreadsheet contract (45 min recorded + 15 min live Q&A/drill, all inside the hour). Unchanged by the 2026-08-03 rescope; the deck's notes are already timed 15/15/15/15.

### Pair drill — the four 2-minute prompts

1. **NN** — A client CTO says: *"Your team keeps saying 'neural network.' In plain terms, what actually is one — and what did you people actually do when you 'trained' it?"* (Expected anchor: your own MNIST lab — layers, weights, nudged until the guesses match the labels.)
2. **CNN** — The construction prospect's ops director asks: *"Why do you need a special kind of network for our site photos? Why not the normal one?"* (Expected anchor: a pattern-detector slid across the image; edges → shapes → objects.)
3. **Deep learning** — A skeptical VP asks: *"Is 'deep learning' actually different from machine learning, or is it just marketing?"* (Expected anchor: the LSN-1.1 nesting doll — ML ⊃ deep learning; many layers that learn their own features; real, but not magic.)
4. **RL** — A warehouse-automation client asks: *"Could reinforcement learning optimize our picking robots' routes? Our vendor says yes."* (Expected anchor: learning by trial and reward; needs somewhere safe and cheap to fail millions of times — a simulator — plus a reward you can actually write down.)

### Peer-grading rubric (0–2 each; pass = 6/8 with no zero)

| Criterion | 2 | 0 |
|---|---|---|
| Plain language | No unexplained jargon; a non-engineer follows it | Term salad |
| Concrete anchor | One real example (your MNIST run, site photos, robot routes) | Abstractions only |
| Honest boundary | Says what it can't do or what it needs (data, simulator, labels) | Implies magic |
| Lands in 2 minutes | Client leaves with a takeaway or a sharp next question | Rambles past time or trails off |

## Client Tie-In (Dorel's rule)

Prompts 2 and 4 are pre-sales scenes: the construction-site photo/video prospect (why vision means CNNs) and a warehouse-robotics vendor claim to sanity-check (RL's real preconditions). The drill rehearses the exact "mini conversation" Vlad scoped this module around, and the rubric's honest-boundary row is the same dimension ASM-1 grades.

## Homework

Previously none. The spreadsheet's 2 h out-of-session budget leaves **80 min** after pre-work, and this lesson is the one place to spend it well: the live pair drill fits only two deliveries per person, and ASM-1 grades the same skill under pressure. So homework is rehearsal with a machine grader, not reading.

| # | Task | Time | Checkpoint / artifact |
|---|---|---|---|
| 1 | **Rehearse all four, not just the two you drew.** Write your four post-session sentences into the notebook's drill cell and run the sentence advisor on each (it checks three of the four rubric rows mechanically). Then record yourself delivering each of the four 2-minute explanations out loud — phone voice memo is fine — self-score against the rubric, and re-record whichever scored lowest | 35 min | 4 advisor-passing sentences + 4 recordings + 1 re-recording, self-scores noted |
| 2 | **Run the three props and say what you saw.** The squash-removal collapse (why a network without its non-linearity is just one big linear layer), the shift-the-digit reuse proof (why a convolution is cheaper *and* more robust), and the reward-hacking run (same agent, same grid, badly-written reward). One plain-language sentence per prop — the sentence you would say to a client, not to an engineer | 20 min | 3 sentences, each naming what the demo *showed* rather than what it *is* |
| 3 | **The RL preconditions memo** — prompt 4's vendor claim, answered properly. Write the reward function you would actually propose for the picking robots, then name how it could be gamed (cite your own reward-hacking run as the evidence), state the simulator requirement and who would have to build it, and finish with the two sentences you would say to the client about the vendor's "yes" | 25 min | A one-page memo submitted referencing `LSN-1.5` |

**Pass:** every one of the four recorded deliveries lands inside 2 minutes with a concrete anchor and an honest boundary (rubric ≥ 6/8, no zero), and the memo's reward function is specific enough to be gamed — a reward nobody could game is a reward nobody wrote down properly. The graded performance is still the ASM-1 mock conversation; this is the rehearsal that makes it survivable.

**Time accounting:** pre-work 40 min + homework 80 min = 2 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session companion notebook** — pre-work + cheat sheet + three segments (live demos as props) + drill workspace with tested advisor | exists | `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` |
| **Session deck** — 16 slides, speaker notes timed 15/15/15/15 = 60 | exists | `program/lessons/decks/LSN-1.5-conversational-deep-learning.html` |
| Karpathy excerpt (pre-work #1) | exists | Andrej Karpathy, ["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0) — Neural Networks: Zero to Hero series (excerpt + timestamps chosen at delivery prep) |
| One-page NN/CNN/DL/RL cheat sheet | exists | Canonical home: the cheat-sheet markdown cells in `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` (distilled from the reference notebooks' intros + Tyler's original ML literacy deck per SI-25) |
| NN reference notebook | exists | `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` |
| CNN reference notebook | exists | `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` |
| RL reference notebook | exists | `notebooks/reinforcement/01_Reinforcement_QLearning.ipynb` |
| Optional: 3Blue1Brown — "But what is a neural network?" (Deep Learning, Chapter 1) | exists | [youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk) |
| Pair-drill prompts + rubric | exists | This plan (above) |
| Supplement — the traffic-sign adversarial result as a CNN closing beat (the model was never using the features you assumed) | supplement | [`program/sources/SUP-7-failure-and-trust-catalog.md`](../sources/SUP-7-failure-and-trust-catalog.md) §2 |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality (especially whether two drill rounds fit in 15 min). Feeds the MOD-1 retro.

**Rescope note (2026-08-03):** the live hour is unchanged — deck and notebook are already timed to 60, so no retiming is needed. One artifact edit is: the companion notebook's closing section is titled "Before you leave — **no homework**, and what `LSN-1.6` opens with," which the new 80-min homework block contradicts. That section needs rewriting to launch the three tasks; the cells they use (sentence advisor, drill workspace, model answers, the three demo props) all already exist and are executed.

**Format question for the next review call:** the spreadsheet books 1 h live, and this lesson spends 45 of those 60 minutes on recorded segments. If the recordings are watched out of session instead, the live hour would need 45 min of new drill content and the out-of-session budget would absorb the recordings. Kept as-is for now — the 15/15/15/15 shape is what the deck and notebook are built and reviewed against — but it is a deliberate decision, not an oversight.
