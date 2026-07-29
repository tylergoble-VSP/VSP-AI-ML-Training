---
name: LSN-1.5-conversational-deep-learning
description: Hold a two-minute, jargon-free client exchange on neural networks, CNNs, deep learning, and reinforcement learning — anchored to the neural net you personally trained in LSN-1.4.
module: MOD-1
serves: OUT-1.5
duration: 1 h
prework_time: 30
owner: Tyler Goble
status: draft
---

# LSN-1.5 — Conversational Deep Learning: NN, CNN, RL

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.5` |
| **Duration** | 1 h session + 30 min pre-work |
| **Format** | Recorded + Q&A |
| **Verified by** | ASM-1 (mock pre-sales conversation) |

## Narrative

Kills the fear of the vocabulary. You are not learning what a neural network is from a slide — you *trained one* in the LSN-1.4 MNIST lab, watched its loss fall, and read its confusion matrix; this lesson just gives you the words for what you already did. Installs Vlad's bar verbatim: "have a mini conversation about this and not look completely stupid" — NN, CNN, deep learning, RL, each explainable in two plain-language minutes. The pair drill is a direct rehearsal for the ASM-1 mock pre-sales conversation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch the curated ~15-min excerpt from Andrej Karpathy, "The spelled-out intro to neural networks and backpropagation: building micrograd" (Neural Networks: Zero to Hero) — excerpt selection (verify at delivery prep) | 15 min | One question the excerpt left you with |
| 2 | Read the one-page NN/CNN/DL/RL cheat sheet | 10 min | Nothing to submit |
| 3 | Draft one client-safe sentence for each of the four terms | 5 min | Your four sentences — raw material for the pair drill |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| What you trained *was* a neural net | 15 min | recorded talk | Replay of the LSN-1.4 lab in vocabulary: the MLP you built is layers of weighted sums plus squashing functions; "training" was nudging weights until outputs matched labels; the falling loss curve was learning. "Deep learning" = the same thing with many layers, so the network learns its own features instead of being handed them. Reference build: `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb`. |
| CNNs: why images want convolutions | 15 min | recorded talk | One picture, no math: a small pattern-detector (edge, corner, texture) slid across the whole image, layers stacking detectors into shapes into objects. Why that beats a plain MLP on pixels: reuse and locality. This is the architecture the construction-site photo prospect would need. Reference: `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb`. |
| RL: learning by reward | 15 min | recorded talk | No labels — an agent acts, gets a reward, adjusts. Where it earns its keep: games, robotics, route/sequence optimization — anywhere you can fail cheaply a million times (usually a simulator). One-slide teaser: RLHF, the RL that shaped the LLMs in MOD-2. Reference: `notebooks/reinforcement/01_Reinforcement_QLearning.ipynb`. |
| Live Q&A + pair drill | 15 min | drill (live) | Q&A on the recording (5 min), then pairs: each person draws one prompt below, delivers the 2-minute explanation to their partner playing the named client, partner scores against the rubric, swap. Two deliveries fit — one per partner (5 min Q&A + 2 × (2 min delivery + 1 min scoring) + 4 min whole-group = 15); instructor pulls one strong and one shaky delivery for whole-group feedback. |

**Timing check:** 15 + 15 + 15 + 15 = 60 min = 1 h contract duration (45 min recorded + 15 min live Q&A/drill). ✓

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

None — the pair drill is the rehearsal; the graded performance is the ASM-1 mock pre-sales conversation. Keep your four sentences, revised with your partner's scores.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session companion notebook** — pre-work + cheat sheet + three segments (live demos as props) + drill workspace with tested advisor | exists | `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` |
| **Session deck** — 16 slides, speaker notes timed 15/15/15/15 = 60 | exists | `program/lessons/decks/LSN-1.5-conversational-deep-learning.html` |
| Karpathy excerpt (pre-work #1) | exists | Andrej Karpathy, "The spelled-out intro to neural networks and backpropagation: building micrograd" — Neural Networks: Zero to Hero series (excerpt + timestamps chosen at delivery prep; verify at delivery prep) |
| One-page NN/CNN/DL/RL cheat sheet | exists | Canonical home: the cheat-sheet markdown cells in `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` (distilled from the reference notebooks' intros + Tyler's original ML literacy deck per SI-25) |
| NN reference notebook | exists | `notebooks/neural_networks/01_NeuralNetworks_Perceptron_MLP.ipynb` |
| CNN reference notebook | exists | `notebooks/neural_networks/02_NeuralNetworks_Convolutional_Neural_Networks.ipynb` |
| RL reference notebook | exists | `notebooks/reinforcement/01_Reinforcement_QLearning.ipynb` |
| Optional: 3Blue1Brown — "But what is a neural network?" (Deep Learning, Chapter 1) | exists | (verify at delivery prep) |
| Pair-drill prompts + rubric | exists | This plan (above) |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality (especially whether two drill rounds fit in 15 min). Feeds the MOD-1 retro.
