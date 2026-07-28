---
name: LSN-0.2-statistics-1-distributions-sampling-variance
description: Read a distribution's shape, judge whether a sample can be trusted, and ask the three questions before believing any accuracy claim.
module: MOD-0
serves: OUT-0.3
duration: 1.5 h
prework_time: 30
owner: Tyler
status: draft
---

# LSN-0.2 — Statistics I: Distributions, Sampling, Variance

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.3` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Narrative

The misconception this session kills: a single number — a mean, an accuracy score — tells you something on its own. It doesn't; it hides a distribution, a sample size, and a collection method, and any of the three can make the number a lie. The capability installed is the "how reliable is this answer, on what data?" reflex, exercised on data senior engineers already have intuition for (latencies, cycle times, deal sizes) and cashed out in a pre-sales drill. Builds on the environment from `LSN-0.1` (the session runs in a notebook); sets up `LSN-0.3` (conditioning and base rates) and the formal model-grading treatment in `LSN-1.3`.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch StatQuest with Josh Starmer: "Histograms, Clearly Explained" and "The Main Ideas behind Probability Distributions" (links in GAP-1 deck; verify at delivery prep) | 20 min | One written sentence: what does a histogram tell you that the mean alone cannot? |
| 2 | In your `LSN-0.1` environment, write a ~10-line notebook: draw 10,000 samples from `normal(mean=50, sd=2)` and 10,000 from `normal(mean=50, sd=20)`, plot both histograms overlaid | 10 min | The executed notebook with the plot — same mean, wildly different spread |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Distributions as pictures of uncertainty | 20 min | talk + demo | Open with 3–4 pre-work plots on screen: same mean, different worlds. Then histograms of real engineering data: production API latency (p50 = 180 ms, mean = 240 ms, p99 = 2.1 s — right-skewed, the mean sits where almost no request lives) vs. adult heights (symmetric — the mean is a fine summary). The rule: a distribution answers "which values are plausible, and how plausible?"; a mean answers almost nothing without the shape |
| Sampling: n = 30 vs n = 30,000 | 25 min | demo + discussion | Live notebook: a 100,000-value latency "population"; repeatedly draw samples of n = 30, n = 3,000, and n = 30,000 (with replacement) and plot the sample means — watch n = 30 bounce by tens of ms while the larger samples barely move. Then bias, which no sample size fixes: an NPS survey only angry users answer; latency measured only during EU business hours; Wald's WWII bombers (armor where the returning planes *weren't* hit). Two questions for any number: how many, and collected how? |
| Variance and outliers: when the average lies | 20 min | demo + discussion | Two delivery teams, both mean cycle time 5 days: Team A σ = 0.5 days, Team B σ = 4 days — whose estimate do you put in a client commitment? One $2M outlier deal drags "average deal size" from $80k to $208k (15 deals: 14 averaging exactly $80k + the whale — 2.6×) while the median barely moves. Fixes: median, percentiles, and always plotting before summarizing (Anscombe's quartet, one slide) |
| Client drill: "our model is 92% accurate" | 25 min | drill | Scenario written below. Pairs get the card, 5 min prep; 2–3 pairs run the conversation live against Tyler playing the prospect; 8 min debrief against the three questions |

**Timing check:** 20 + 25 + 20 + 25 = 90 min = 1.5 h contract duration.

### The "92% accurate" drill — scenario card

A construction-firm prospect is evaluating vendors for milestone tracking. Their incumbent's pitch: *"Our model detects completed milestones from site photos with 92% accuracy."* The prospect's PM asks the VSP participant: "Sounds great — should we just go with them?"

The numbers behind the claim (revealed in debrief): the vendor's test set is 1,000 photos — 920 "in progress", 80 "milestone complete". A model that answers **"in progress" every single time scores 92%** while finding zero completed milestones.

The three questions to ask before believing it:

1. **92% on what data?** Held-out data or the data it trained on? From the same sites, cameras, seasons, and lighting it will see in production — or from a curated demo set?
2. **What's the class balance?** If 92% of photos are "in progress", 92% accuracy is achievable by a model that never detects anything. What's accuracy on *each class*?
3. **Which mistakes make up the missing 8%?** Missed completions (late invoicing) vs. false completions (billing for unfinished work) cost differently — which one is the 8%? (Named in debrief as precision vs. recall — formal treatment in `LSN-1.3`.)

## Client Tie-In (Dorel's rule)

The drill is the construction-site completion-detection prospect (the real vision/ML pre-sales case, fully walked in `LSN-1.6` and `LSN-3.6`). The distribution and sampling segments use data shapes every VSP senior already owns — API latencies, cycle times, deal sizes — so the reflex transfers to the next client meeting, not just the quiz.

## Homework

Notebook (from the GAP-1 exercise notebook): a provided 32-row dataset of schedule slip in days from past fixed-bid projects, containing one +45-day outlier. Tasks: (1) compute mean, median, variance; (2) plot the histogram; (3) identify the outlier and recompute without it; (4) write two sentences: would you trust a model trained on these 32 points to predict overrun for a new project, and what one thing about *how this sample was collected* would you check first? Graded pass/fail on the interpretation, not the code; submission references LSN-0.2. Feeds `ASM-0`.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Stats I deck** — 10 slides w/ timing notes, VSP design system | exists | `program/lessons/decks/LSN-0.2-statistics-1.html` |
| **Session notebook** — pre-work + all four segments + homework (32-row slip dataset, self-checking), executed end to end | exists | `notebooks/lessons/LSN-0.2_Statistics_1_Distributions_Sampling_Variance.ipynb` |
| "92% accurate" drill scenario card | exists | this file (section above) + notebook drill section + deck slide 8 |
| StatQuest with Josh Starmer — "Histograms, Clearly Explained"; "The Main Ideas behind Probability Distributions" | exists | youtube.com/@statquest (verify exact links at delivery prep) |
| Stanford intro-stats excerpts | adapt | Tyler's academic contacts (candidate companion per module spec) |

## Delivery Notes

Not yet delivered — first run Week 1. Watch: does the sampling demo (segment 2) hold non-notebook-fluent participants, or does it need a pre-built notebook they only execute?
