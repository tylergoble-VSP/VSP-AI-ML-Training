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
| **Cadence** | **Daily boot week** — Tuesday 1 – Friday 4 September 2026, one lesson per day, per the program spreadsheet locked 2026-08-03 |
| **Total effort** | **12 h** — 4 × 1 h live (4 h) + 4 × 2 h out-of-session (8 h, pre-work + homework combined). `ASM-0` adds no extra time: its 30 min sits inside LSN-0.4's homework budget |
| **Roles** | Presenter: Tyler · Reviewer: Vlad · Guinea pig: Mazilu (TBC — the spreadsheet says "Mazilu?") |
| **Module owner** | Tyler Goble |
| **Prerequisite** | Enrollment gate passed (see `program-spec.md`) |
| **Checkpoint** | `ASM-0` — *(not on the program spreadsheet — needs a calendar slot at the next review call; proposed: async within LSN-0.4's homework budget, weekend of Sep 5–6)* |

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

Every lesson runs on the same contract: **1 h live + 2 h out-of-session** (pre-work + homework combined), Presenter Tyler, Reviewer Vlad, Guinea pig Mazilu (TBC). The spreadsheet's row title is listed as an alias where it differs from the lesson name.

| ID | Lesson (spreadsheet alias) | Delivery date | Live | Out-of-session | Owner | Format | Material status |
|---|---|---|---|---|---|---|---|
| `LSN-0.1` | Orientation & environment setup (= "Orientation") | Tue 1 Sep 2026 | 1 h | 2 h (45 pre + 75 hw) | Tyler + Marius | Live, hands-on | Exists (repo); live session already timed to 60 |
| `LSN-0.2` | Statistics I — distributions, sampling, variance (= "Statistics 1") | Wed 2 Sep 2026 | 1 h | 2 h (30 pre + 90 hw) | Tyler | Live | Built (deck + notebook); **timed to 90 — retiming round required** |
| `LSN-0.3` | Statistics II — probability, conditioning, correlation ≠ causation (= "Statistics 2") | Thu 3 Sep 2026 | 1 h | 2 h (30 pre + 90 hw) | Tyler | Live | Built (deck + notebook); **timed to 90 — retiming round required** |
| `LSN-0.4` | Deterministic, probabilistic, stochastic — reading uncertainty (= "Deterministic vs Probablistic vs Stocastic", sic) | Fri 4 Sep 2026 | 1 h | 2 h (20 pre + 100 hw) | Tyler | Live or recorded | Built (deck + notebook, timed to 60) |
| — | `ASM-0` checkpoint quiz | **unscheduled** (not on the program spreadsheet — needs a calendar slot at the next review call; proposed: async within LSN-0.4's homework budget, weekend of Sep 5–6) | — | 30 min, inside LSN-0.4's homework budget | Tyler | Async | **BUILD — GAP-6** |

**Module totals:** 4 × 1 h live = 4 h; 4 × 2 h out-of-session = 8 h; **12 h total**, with `ASM-0`'s 30 min already counted inside LSN-0.4's homework.

The 1.5 h → 1 h squeeze on `LSN-0.2` and `LSN-0.3` does not delete content: the mechanical notebook walk-throughs (the sampling simulation, the base-rate counts build, the spurious-correlation gallery) move into pre-work and homework as guided, time-estimated tasks. The room keeps discussion, the misconception-killing beats, and both client drills.

## Cadence & Evening Load (daily boot week)

Four lessons on four consecutive days means each evening carries **two different budgets at once**: lesson *N*'s homework plus lesson *N+1*'s pre-work. Pre-work is therefore held thin (≤ 30 min) and the weight sits in homework:

| Evening | Carries | Load |
|---|---|---|
| Mon 31 Aug | LSN-0.1 pre-work (45) | 45 min |
| Tue 1 Sep | LSN-0.1 homework (75) + LSN-0.2 pre-work (30) | 105 min |
| Wed 2 Sep | LSN-0.2 homework (90) + LSN-0.3 pre-work (30) | **120 min** |
| Thu 3 Sep | LSN-0.3 homework (90) + LSN-0.4 pre-work (20) | **110 min** |
| Fri 4 Sep – Sun 6 Sep | LSN-0.4 homework (100, incl. the 30 min `ASM-0` quiz) | 100 min across the weekend |

Total out-of-session: 480 min = 8 h = 4 × 2 h — the contract holds per lesson.

**Flag for the review call:** Wednesday and Thursday evenings both land at ~2 h back to back — the real risk to this module, not the live hours. Two relief valves are already built in: (1) `LSN-0.1`'s Python-foundations tranche is due before `LSN-1.4`, not next morning, so it can slide off Tuesday evening; (2) `LSN-0.4`'s homework runs into the weekend, which is where `ASM-0` is proposed. If the cohort reports overload after the guinea-pig run, the trim order is LSN-0.2 homework tasks 4–5, then LSN-0.3 task 4.

---

### LSN-0.1 — Orientation & Environment Setup

| Date | Live | Out-of-session | Owner | Serves |
|---|---|---|---|---|
| Tuesday, 1 September 2026 | 1 h | 2 h (45 min pre-work + 75 min homework) | Tyler + Marius | `OUT-0.1` |

Presenter Tyler · Reviewer Vlad · Guinea pig Mazilu (TBC).

**Purpose:** The program's contract and a working machine. Everyone leaves with a running notebook — nobody spends the rest of the boot week, or `MOD-1`, fighting their environment.

**Pre-work (~45 min, mandatory):** Read the program README and `program-spec.md` ceremonies section; clone `VSP-AI-ML-Training`; attempt setup via `ACTIVATE_VENV.md` + `requirements.txt` (fallback: `INSTALL_TROUBLESHOOTING.md`). Arrive with your error message if it failed. Held at 45 min rather than the ≤ 30 min boot-week norm because it lands on Monday 31 Aug, the one clear evening with no prior homework stacked on it.

**Session outline:**
1. Program walkthrough: three pillars, tiers, cadence, the pre-work rule and why (the Ciobanu story), checkpoint gates (15 min)
2. Environment triage: fix every broken setup live (25 min)
3. All together: `Run All` on `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb` — five checkpoints ending in the ASM-0 evidence screenshot (15 min)
4. Baseline self-rating against all basics outcomes (5 min)

**Homework (75 min):** Finish the session notebook and the baseline self-rating if triage ran long (25 min); then a 50 min tranche of the Python track — non-Python participants start `foundations/01_Beginning_Python.ipynb` (full completion, plus `02_Intermediate_Python.ipynb` as needed, due before `LSN-1.4`), daily-Python participants take the `03_Advanced_Python.ipynb` sections instead. This is the module's one sliding budget: it is the only MOD-0 homework not due the next morning.

**Support material:** `ACTIVATE_VENV.md`, `INSTALL_TROUBLESHOOTING.md`, `notebooks/foundations/01–03`; session notebook `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb`; deck `program/lessons/decks/LSN-0.1-orientation.html`.

---

### LSN-0.2 — Statistics I: Distributions, Sampling, Variance

| Date | Live | Out-of-session | Owner | Serves |
|---|---|---|---|---|
| Wednesday, 2 September 2026 | 1 h | 2 h (30 min pre-work + 90 min homework) | Tyler | `OUT-0.3` |

Presenter Tyler · Reviewer Vlad · Guinea pig Mazilu (TBC).

**Purpose:** The "how reliable is this answer" muscle. Mean/median/variance, what a distribution's shape tells you, why sample size and sampling bias decide whether a number can be trusted.

**Pre-work (~30 min):** StatQuest with Josh Starmer — ["Histograms, Clearly Explained"](https://www.youtube.com/watch?v=qBigTkBLU6g) and ["The Main Ideas behind Probability Distributions"](https://www.youtube.com/watch?v=oI3hZJqXJuc) (15 min) + run sections 1–2 of the session notebook: the same-mean/different-variance overlay and the n = 30 / 3,000 / 30,000 sampling simulation, changing one parameter in each (15 min). The simulation moved here from the live session — it is mechanical and solo-executable, and running it beforehand also answers the old delivery worry about notebook-fluency.

**Session outline (60 min):**
1. Distributions as pictures of uncertainty — participants' pre-work plots on screen, then the latency-vs-heights contrast (12 min)
2. Sampling debrief + bias, which no sample size fixes — discussion, not simulation (15 min)
3. Variance and outliers: when the average lies — the client-commitment decision (13 min)
4. Client-conversation drill: "our model is 92% accurate" — the three questions to ask before believing it (20 min)

**Homework (90 min):** The 32-row schedule-slip notebook (mean/median/variance, histogram, outlier recompute, trust write-up, 30 min); the outlier arithmetic and Anscombe's quartet cells relocated out of the live session (25 min); write the three questions as an email to the prospect's PM (15 min); apply the two sampling questions to a number from your own current project (10 min); notebook extension — sampling on the right-skewed latency population (10 min).

**Support material:** Built — deck `program/lessons/decks/LSN-0.2-statistics-1.html`; session notebook `notebooks/lessons/LSN-0.2_Statistics_1_Distributions_Sampling_Variance.ipynb` (pre-work + session + self-checking homework, executed end to end). **Both are timed to the previous 90-min session — a retiming round is required before delivery** (resection the notebook into pre-work / live / homework blocks matching the new split). Candidate companions: Stanford intro-stats excerpts (Tyler pulling from academic contacts).

**Client tie-in (Dorel's rule):** the "92% accurate" drill uses a VSP-shaped scenario.

---

### LSN-0.3 — Statistics II: Probability, Conditioning, Correlation ≠ Causation

| Date | Live | Out-of-session | Owner | Serves |
|---|---|---|---|---|
| Thursday, 3 September 2026 | 1 h | 2 h (30 min pre-work + 90 min homework) | Tyler | `OUT-0.3`, `OUT-0.4` |

Presenter Tyler · Reviewer Vlad · Guinea pig Mazilu (TBC).

**Purpose:** Enough probability to read model outputs (they're all conditional probabilities) and to not get fooled — by a client's data story or by a model's coincidences.

**Pre-work (~30 min, unchanged):** 3Blue1Brown — ["The medical test paradox, and redesigning Bayes' rule"](https://www.youtube.com/watch?v=lG4VkPoG3ko) (21 min) + the base-rate fraud counts table for 1,000,000 transactions (9 min). The pre-work table now *is* the arithmetic — the live segment checks it instead of building it from zero, which is where the 10 min comes from.

**Session outline (60 min):**
1. Probability as degrees of belief; the P(alert | fraud) → P(fraud | alert) flip (12 min)
2. Base rates: check the pre-work tables, then "what would you do" — threshold, features, or staff the queue; precision/recall foreshadowing for `LSN-1.3` (15 min)
3. Correlation vs causation: the four explanations + the business trap (13 min)
4. Drill: client shows a chart "proving" their feature drives revenue — what do you ask? (20 min)

**Homework (90 min):** Three scenario questions (async, graded pass/fail, 25 min); notebook threshold exercise relocated from the live "what would you do" discussion (20 min); spurious-correlations gallery write-up, relocated from segment 3 (15 min); design the phase-two holdout the drill asks for (20 min); the 6MAP "0.93" translation rewrite (10 min).

**Support material:** Built — deck `program/lessons/decks/LSN-0.3-statistics-2.html`; session notebook `notebooks/lessons/LSN-0.3_Statistics_2_Probability_Correlation_Causation.ipynb` (pre-work counts table + session + self-checking homework, executed end to end). **Both are timed to the previous 90-min session — a retiming round is required before delivery.**

---

### LSN-0.4 — Deterministic, Probabilistic, Stochastic

| Date | Live | Out-of-session | Owner | Serves |
|---|---|---|---|---|
| Friday, 4 September 2026 | 1 h | 2 h (20 min pre-work + 100 min homework, incl. `ASM-0`) | Tyler | `OUT-0.2` |

Presenter Tyler · Reviewer Vlad · Guinea pig Mazilu (TBC).

**Purpose:** The vocabulary bridge into everything that follows: why ML answers vary, what a confidence attached to a guess means, and "all models are wrong, some are useful" as a working attitude rather than a quip.

**Pre-work (~20 min):** Re-read the keywords section of the ML literacy deck; write one example of each term from your own project experience.

**Session outline (60 min — already on contract, content unchanged):**
1. Deterministic (2+2) vs probabilistic (a guess with confidence) vs stochastic (randomness in the process) — participants' own examples reviewed live (25 min)
2. Why this matters commercially: setting client expectations when outputs vary between runs (20 min)
3. Bridge to MOD-1: the five ML jobs all produce probabilistic answers — preview (15 min)

**Homework (100 min, runs into the weekend of Sep 5–6):** was "none — checkpoint week", which no longer fits a 2 h out-of-session contract. Now: consolidation pass over the week's three notebooks as `ASM-0` prep (25 min); three-bucket sort applied to a live VSP system, with a SOW acceptance criterion per probabilistic/stochastic behaviour (25 min); eval-set sizing from the notebook's acceptance-arithmetic cell (20 min); **`ASM-0` itself (30 min)** — the quiz is not on the program spreadsheet, so this budget is where it is proposed to live.

**Support material:** Built — deck `program/lessons/decks/LSN-0.4-deterministic-probabilistic-stochastic.html` (slide 2 carries the keywords, the pre-work target); session notebook `notebooks/lessons/LSN-0.4_Deterministic_Probabilistic_Stochastic.ipynb` (executed end to end). Original ML literacy deck keywords section remains the source (not yet in repo).

---

## Checkpoint — ASM-0

| Field | Value |
|---|---|
| **Format** | Async quiz, ~20 questions, 30 min |
| **Schedule** | **Not on the program spreadsheet — needs a calendar slot at the next review call; proposed: async within LSN-0.4's homework budget, weekend of Sep 5–6.** Accounted for: 30 of LSN-0.4's 100 homework minutes are the quiz itself, so it consumes no extra participant time beyond the 2 h contract |
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
| `GAP-6` (share) | ASM-0 quiz | Tyler | Fri 4 Sep 2026 (live for the proposed Sep 5–6 async window) |
| — | Retiming round (no GAP id — rescope debt, not a content gap): `LSN-0.2` and `LSN-0.3` decks + notebooks rebuilt to the 60 min live split, with the relocated cells re-labelled pre-work / homework. Both were built to 90 min | Tyler | Tue 1 Sep 2026 |
