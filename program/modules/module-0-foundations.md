---
name: module-0-foundations
description: Orientation and statistics foundation — working environment, probabilistic thinking, and the math floor every later module stands on.
---

# MOD-0 — Foundations: Orientation & Statistics

## Module Configuration

| Field | Value |
|---|---|
| **ID** | `MOD-0` |
| **Tier** | Basics |
| **Pillar** | Cross-cutting (enables all three) |
| **Week** | 1 |
| **Total effort** | ~5.5 h sessions + ~2 h pre-work/homework |
| **Module owner** | Tyler Goble |
| **Prerequisite** | Enrollment gate passed (see `program-spec.md`) |
| **Checkpoint** | `ASM-0` |

## Purpose

Vlad's requirement, verbatim: basics must include "a statistics foundation" because "you're not gonna really understand what's going on unless you understand some fundamental math" (Tyler, confirmed by Vlad in the July 28 meeting). This module sets the floor: a working local environment and enough probabilistic thinking that a confidence number, an error metric, or a "the model can only infer so far" statement means something. No dictionary definitions — every concept lands via a small exercise.

## Outcomes

| ID | After MOD-0 you can… | Serves |
|---|---|---|
| `OUT-0.1` | Run Python + Jupyter locally and execute a notebook end to end | GOAL-6, GOAL-7 |
| `OUT-0.2` | Explain deterministic vs probabilistic vs stochastic, and read "95% confident" as a claim about uncertainty — not a decoration | GOAL-1, GOAL-4 |
| `OUT-0.3` | Reason about distributions, sampling, and variance well enough to ask "how reliable is this answer, on what data?" | GOAL-1, GOAL-4 |
| `OUT-0.4` | Spot correlation-vs-causation traps and small-sample traps in a client's claim | GOAL-1, GOAL-2 |

## Lesson Inventory

| ID | Lesson | Duration | Owner | Format | Material status |
|---|---|---|---|---|---|
| `LSN-0.1` | Orientation & environment setup | 1 h | Tyler + Marius | Live, hands-on | Exists (repo) |
| `LSN-0.2` | Statistics I — distributions, sampling, variance | 1.5 h | Tyler | Live | Built (deck + notebook) |
| `LSN-0.3` | Statistics II — probability, conditioning, correlation ≠ causation | 1.5 h | Tyler | Live | Built (deck + notebook) |
| `LSN-0.4` | Deterministic, probabilistic, stochastic — reading uncertainty | 1 h | Tyler | Live or recorded | Built (deck + notebook) |
| — | `ASM-0` checkpoint quiz | 0.5 h | Tyler | Async | **BUILD — GAP-6** |

---

### LSN-0.1 — Orientation & Environment Setup

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler + Marius | `OUT-0.1` |

**Purpose:** The program's contract and a working machine. Everyone leaves with a running notebook — nobody hits Week 2 fighting their environment.

**Pre-work (~45 min, mandatory):** Read the program README and `program-spec.md` ceremonies section; clone `VSP-AI-ML-Training`; attempt setup via `ACTIVATE_VENV.md` + `requirements.txt` (fallback: `INSTALL_TROUBLESHOOTING.md`). Arrive with your error message if it failed.

**Session outline:**
1. Program walkthrough: three pillars, tiers, cadence, the pre-work rule and why (the Ciobanu story), checkpoint gates (15 min)
2. Environment triage: fix every broken setup live (25 min)
3. All together: `Run All` on `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb` — five checkpoints ending in the ASM-0 evidence screenshot (15 min)
4. Baseline self-rating against all basics outcomes (5 min)

**Homework:** Non-Python participants work through `foundations/01_Beginning_Python.ipynb` (and `02_Intermediate_Python.ipynb` as needed) before `LSN-1.4`.

**Support material:** `ACTIVATE_VENV.md`, `INSTALL_TROUBLESHOOTING.md`, `notebooks/foundations/01–03`; session notebook `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb`; deck `program/lessons/decks/LSN-0.1-orientation.html`.

---

### LSN-0.2 — Statistics I: Distributions, Sampling, Variance

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-0.3` |

**Purpose:** The "how reliable is this answer" muscle. Mean/median/variance, what a distribution's shape tells you, why sample size and sampling bias decide whether a number can be trusted.

**Pre-work (~30 min):** StatQuest with Josh Starmer — ["Histograms, Clearly Explained"](https://www.youtube.com/watch?v=qBigTkBLU6g) and ["The Main Ideas behind Probability Distributions"](https://www.youtube.com/watch?v=oI3hZJqXJuc) + a 10-line notebook that plots two distributions with the same mean and wildly different variance.

**Session outline:**
1. Distributions as pictures of uncertainty — histograms of real data (20 min)
2. Sampling: why 30 data points and 30,000 give different confidence; bias in how the sample was collected (25 min)
3. Variance and outliers: when the average lies (20 min)
4. Client-conversation drill: "our model is 92% accurate" — the three questions to ask before believing it (25 min)

**Homework:** Short notebook — given a small dataset, compute and interpret mean/variance, then write two sentences on whether you'd trust a model trained on it.

**Support material:** Built — deck `program/lessons/decks/LSN-0.2-statistics-1.html`; session notebook `notebooks/lessons/LSN-0.2_Statistics_1_Distributions_Sampling_Variance.ipynb` (pre-work + session + self-checking homework, executed end to end). Candidate companions: Stanford intro-stats excerpts (Tyler pulling from academic contacts).

**Client tie-in (Dorel's rule):** the "92% accurate" drill uses a VSP-shaped scenario.

---

### LSN-0.3 — Statistics II: Probability, Conditioning, Correlation ≠ Causation

| Duration | Owner | Serves |
|---|---|---|
| 1.5 h | Tyler | `OUT-0.3`, `OUT-0.4` |

**Purpose:** Enough probability to read model outputs (they're all conditional probabilities) and to not get fooled — by a client's data story or by a model's coincidences.

**Pre-work (~30 min):** 3Blue1Brown — ["The medical test paradox, and redesigning Bayes' rule"](https://www.youtube.com/watch?v=lG4VkPoG3ko) + one worked example: base-rate fallacy in a fraud-detection framing.

**Session outline:**
1. Probability as degrees of belief; conditional probability via the fraud example (25 min)
2. Base rates: why a 99%-accurate detector on a 1-in-10,000 event is mostly false alarms — this is precision/recall foreshadowing for `LSN-1.3` (25 min)
3. Correlation vs causation: famous traps + one business trap (20 min)
4. Drill: client shows a chart "proving" their feature drives revenue — what do you ask? (20 min)

**Homework:** Three short scenario questions (async, graded pass/fail).

**Support material:** Built — deck `program/lessons/decks/LSN-0.3-statistics-2.html`; session notebook `notebooks/lessons/LSN-0.3_Statistics_2_Probability_Correlation_Causation.ipynb` (pre-work counts table + session + self-checking homework, executed end to end).

---

### LSN-0.4 — Deterministic, Probabilistic, Stochastic

| Duration | Owner | Serves |
|---|---|---|
| 1 h | Tyler | `OUT-0.2` |

**Purpose:** The vocabulary bridge into everything that follows: why ML answers vary, what a confidence attached to a guess means, and "all models are wrong, some are useful" as a working attitude rather than a quip.

**Pre-work (~20 min):** Re-read the keywords section of the ML literacy deck; write one example of each term from your own project experience.

**Session outline:**
1. Deterministic (2+2) vs probabilistic (a guess with confidence) vs stochastic (randomness in the process) — participants' own examples reviewed live (25 min)
2. Why this matters commercially: setting client expectations when outputs vary between runs (20 min)
3. Bridge to MOD-1: the five ML jobs all produce probabilistic answers — preview (15 min)

**Homework:** None — checkpoint week.

**Support material:** Built — deck `program/lessons/decks/LSN-0.4-deterministic-probabilistic-stochastic.html` (slide 2 carries the keywords, the pre-work target); session notebook `notebooks/lessons/LSN-0.4_Deterministic_Probabilistic_Stochastic.ipynb` (executed end to end). Original ML literacy deck keywords section remains the source (not yet in repo).

---

## Checkpoint — ASM-0

| Field | Value |
|---|---|
| **Format** | Async quiz, ~20 questions, 30 min |
| **Verifies** | `OUT-0.1` (setup evidence: screenshot of executed notebook), `OUT-0.2`–`OUT-0.4` (scenario questions, not definitions) |
| **Pass bar** | 80%; one retake within the week |
| **Gate** | Must pass to start `MOD-1`. No pass + no engagement → out (per GOAL-7) |
| **Status** | **BUILD — GAP-6** |

## Traceability

| Outcome | Served by | Verified by |
|---|---|---|
| `OUT-0.1` | LSN-0.1 | ASM-0 (artifact) |
| `OUT-0.2` | LSN-0.4 | ASM-0 |
| `OUT-0.3` | LSN-0.2, LSN-0.3 | ASM-0 |
| `OUT-0.4` | LSN-0.3 | ASM-0 |

## Build List

| ID | Item | Owner | Needed by |
|---|---|---|---|
| `GAP-1` | ~~Stats I & II decks + exercise notebooks + drills~~ **CLOSED** — built Rounds 1–2 (see `program/lessons/BUILD_LOG.md`) | Tyler | done |
| `GAP-6` (share) | ASM-0 quiz | Tyler | End of Week 1 |
