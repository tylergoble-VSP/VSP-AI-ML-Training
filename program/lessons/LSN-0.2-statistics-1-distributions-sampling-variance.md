---
name: LSN-0.2-statistics-1-distributions-sampling-variance
description: Read a distribution's shape, judge whether a sample can be trusted, and ask the three questions before believing any accuracy claim.
module: MOD-0
delivery_date: 2026-09-02
serves: OUT-0.3
duration: 1
prework_time: 30
homework_time: 90
owner: Tyler
status: draft
---

# LSN-0.2 — Statistics I: Distributions, Sampling, Variance

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.3` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Wednesday, 2 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Statistics 1."**

Rescoped from a 90 min session to 60 min. Nothing was cut: the two mechanical notebook runs moved into pre-work, and the outlier/Anscombe arithmetic moved into homework. The room keeps the misconception-killing beats and the drill.

## Narrative

The misconception this session kills: a single number — a mean, an accuracy score — tells you something on its own. It doesn't; it hides a distribution, a sample size, and a collection method, and any of the three can make the number a lie. The capability installed is the "how reliable is this answer, on what data?" reflex, exercised on data senior engineers already have intuition for (latencies, cycle times, deal sizes) and cashed out in a pre-sales drill. Builds on the environment from `LSN-0.1` (the session runs in a notebook); sets up `LSN-0.3` (conditioning and base rates) and the formal model-grading treatment in `LSN-1.3`.

## Pre-work (mandatory — no pre-work, no seat) — 30 min

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch StatQuest with Josh Starmer: ["Histograms, Clearly Explained"](https://www.youtube.com/watch?v=qBigTkBLU6g) and ["The Main Ideas behind Probability Distributions"](https://www.youtube.com/watch?v=oI3hZJqXJuc) | 15 min | One written sentence: what does a histogram tell you that the mean alone cannot? |
| 2 | In your `LSN-0.1` environment, run the session notebook's **§1 Distributions** cells: 10,000 samples from `normal(mean=50, sd=2)` overlaid on 10,000 from `normal(mean=50, sd=20)`. Then change `sd` on one of them and re-run | 8 min | The executed notebook with the plot — same mean, wildly different spread — plus one line on what your `sd` change did |
| 3 | **Relocated from the live session:** run the notebook's **§2 Sampling** simulation — draw repeated samples of n = 30, n = 3,000 and n = 30,000 from the 100,000-value latency population and plot the sample means. Mechanical and solo-executable, so it happens here rather than in the room | 7 min | Two one-line observations: which sample size stopped bouncing, and roughly by how much n = 30 swung |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Distributions as pictures of uncertainty | 12 min | talk + demo | Open with 3–4 pre-work plots on screen: same mean, different worlds. Then the contrast, straight to the punchline: production API latency (p50 = 180 ms, mean = 240 ms, p99 = 2.1 s — right-skewed, the mean sits where almost no request lives) vs. adult heights (symmetric — the mean is a fine summary). The rule: a distribution answers "which values are plausible, and how plausible?"; a mean answers almost nothing without the shape. *Rescope: the histogram exploration participants can do alone is now pre-work task 2 — this segment reacts to their plots instead of generating them* |
| Sampling debrief + bias | 15 min | discussion | Everyone ran the n = 30 / 3,000 / 30,000 simulation in pre-work task 3, so this is the debrief, not the demo: collect what they saw, put two of their plots on screen, name the effect. Then the part that needs a room, because it is judgement and not arithmetic — bias, which no sample size fixes: an NPS survey only angry users answer; latency measured only during EU business hours; Wald's WWII bombers (armor where the returning planes *weren't* hit). Land the two questions for any number: how many, and collected how? |
| Variance and outliers: when the average lies | 13 min | discussion | Kept live because it is a decision, not a computation: two delivery teams, both mean cycle time 5 days, Team A σ = 0.5 days vs Team B σ = 4 days — whose estimate do you put in a client commitment, and what do you write in the SOW? Reveal the $2M whale dragging "average deal size" from $80k to $208k while the median barely moves. Fixes named: median, percentiles, plot before you summarize. *Rescope: the recompute arithmetic and Anscombe's quartet moved to homework task 2 — here they are shown as results, not worked* |
| Client drill: "our model is 92% accurate" | 20 min | drill | Scenario written below. Pairs get the card, 4 min prep; 2 pairs run the conversation live against Tyler playing the prospect; 8 min debrief against the three questions. Untouched by the rescope — a live drill is exactly what an hour in a room is for |

**Timing check:** 12 + 15 + 13 + 20 = 60 min = 1 h — matches the spreadsheet contract.

### The "92% accurate" drill — scenario card

A construction-firm prospect is evaluating vendors for milestone tracking. Their incumbent's pitch: *"Our model detects completed milestones from site photos with 92% accuracy."* The prospect's PM asks the VSP participant: "Sounds great — should we just go with them?"

The numbers behind the claim (revealed in debrief): the vendor's test set is 1,000 photos — 920 "in progress", 80 "milestone complete". A model that answers **"in progress" every single time scores 92%** while finding zero completed milestones.

The three questions to ask before believing it:

1. **92% on what data?** Held-out data or the data it trained on? From the same sites, cameras, seasons, and lighting it will see in production — or from a curated demo set?
2. **What's the class balance?** If 92% of photos are "in progress", 92% accuracy is achievable by a model that never detects anything. What's accuracy on *each class*?
3. **Which mistakes make up the missing 8%?** Missed completions (late invoicing) vs. false completions (billing for unfinished work) cost differently — which one is the 8%? (Named in debrief as precision vs. recall — formal treatment in `LSN-1.3`.)

## Client Tie-In (Dorel's rule)

The drill is the construction-site completion-detection prospect (the real vision/ML pre-sales case, fully walked in `LSN-1.6` and `LSN-3.6`). The distribution and sampling segments use data shapes every VSP senior already owns — API latencies, cycle times, deal sizes — so the reflex transfers to the next client meeting, not just the quiz.

## Homework — 90 min

Graded pass/fail on the interpretation, not the code; submissions reference LSN-0.2. Feeds `ASM-0`.

| # | Task | Time | Artifact |
|---|---|---|---|
| 1 | The schedule-slip notebook (from the GAP-1 exercise notebook): a provided 32-row dataset of schedule slip in days from past fixed-bid projects, containing one +45-day outlier. (a) compute mean, median, variance; (b) plot the histogram; (c) identify the outlier and recompute without it; (d) write two sentences — would you trust a model trained on these 32 points to predict overrun for a new project, and what one thing about *how this sample was collected* would you check first? | 30 min | Executed notebook + the two sentences |
| 2 | **Relocated from live segment 3:** work the two arithmetic pieces the session now only shows as results — rebuild the 15-deal whale table (14 deals averaging exactly $80k + one $2M) and confirm the mean moves 2.6× while the median holds; then plot Anscombe's quartet and write one line on what the four identical summary statistics hide | 25 min | The deal table with both statistics + the quartet plot + one line |
| 3 | Turn the drill into deliverable words: write the three questions as a short email to the construction prospect's PM — the ones you would actually send after that call, in client language, without the word "accuracy" doing any unexamined work | 15 min | ~150-word email draft |
| 4 | Applied drill: take one real number from a project you are on right now (a latency SLO, a velocity average, a conversion rate) and answer the session's two sampling questions about it — how many, and collected how? Name one bias you cannot rule out | 10 min | Three or four sentences naming the number and the bias |
| 5 | Notebook extension: re-run the §2 sampling simulation against the **right-skewed** latency population instead of the normal one, and answer — how large does n have to get before the sample mean settles within ±5 ms? Skew is why the answer is bigger than you expect | 10 min | The extension cell output + your n |

**Time accounting:** pre-work 30 min + homework 90 min = 2 h out-of-session budget.

Wednesday evening also carries `LSN-0.3`'s 30 min pre-work, so this is the week's heaviest night at ~120 min. Tasks 4 and 5 are the designated trim if the guinea-pig run says it is too much.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Stats I deck** — 10 slides w/ timing notes, VSP design system | exists | `program/lessons/decks/LSN-0.2-statistics-1.html` |
| **Session notebook** — pre-work + all four segments + homework (32-row slip dataset, self-checking), executed end to end | exists | `notebooks/lessons/LSN-0.2_Statistics_1_Distributions_Sampling_Variance.ipynb` |
| "92% accurate" drill scenario card | exists | this file (section above) + notebook drill section + deck slide 8 |
| StatQuest with Josh Starmer — "Histograms, Clearly Explained"; "The Main Ideas behind Probability Distributions" | exists | [youtube.com/watch?v=qBigTkBLU6g](https://www.youtube.com/watch?v=qBigTkBLU6g); [youtube.com/watch?v=oI3hZJqXJuc](https://www.youtube.com/watch?v=oI3hZJqXJuc) |
| Stanford intro-stats excerpts | adapt | Tyler's academic contacts (candidate companion per module spec) |

## Delivery Notes

Not yet delivered — first run Wednesday 2 September 2026. The old open question — does the sampling demo hold non-notebook-fluent participants, or does it need a pre-built notebook they only execute? — is answered by the rescope: it is now a pre-built notebook they execute alone beforehand, and the room gets the debrief. New watch item: does a 12 min opener leave enough air to react to their plots, or does segment 1 need to steal 2 min from segment 3?

**Rescope note (2026-08-03):** deck **retimed 2026-08-03** — segments 12 / 15 / 13 / 20, per-slide speaker-note timings summing to 60, pre-work slide carrying the relocated §2 sampling run, and the whale/Anscombe slides reframed as homework hand-offs. The **notebook is still pending** its retiming round before delivery.
