---
name: LSN-0.3-statistics-2-probability-correlation-causation
description: Read model outputs as conditional probabilities, run base-rate arithmetic in your head, and catch correlation-vs-causation traps in a client's data story.
module: MOD-0
delivery_date: 2026-09-03
serves: OUT-0.3, OUT-0.4
duration: 1
prework_time: 30
homework_time: 90
owner: Tyler
status: draft
---

# LSN-0.3 — Statistics II: Probability, Conditioning, Correlation ≠ Causation

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.3`, `OUT-0.4` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Thursday, 3 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Statistics 2."**

Rescoped from a 90 min session to 60 min. The base-rate counts were already pre-work, so the live segment now *checks* the arithmetic instead of building it from zero; the threshold exploration and the spurious-correlations gallery moved to homework. Both flips — P(alert | fraud) → P(fraud | alert), and the four explanations for "A moves with B" — stay in the room, because they are the misconceptions this lesson exists to kill.

## Narrative

Two misconceptions die here: that "99% accurate" means an alert is 99% likely to be real, and that a chart moving with revenue proves the feature caused the revenue. Every model output the cohort will ever read is a conditional probability, and confusing P(alert | fraud) with P(fraud | alert) — or correlation with causation — is exactly how a pre-sales conversation goes wrong. Builds on the sampling skepticism from `LSN-0.2`; the fraud detector built here is deliberately reused in `LSN-1.3`, where "fraction of alerts that are real" gets its formal name: precision.

## Pre-work (mandatory — no pre-work, no seat) — 30 min

Unchanged by the rescope, and deliberately so: it is already at the boot week's ≤ 30 min ceiling, and Thursday evening carries `LSN-0.2`'s 90 min homework as well. Task 2 now carries more weight than before — the live session checks it rather than rebuilding it, which is where 10 of the session's recovered minutes come from, so arriving without a filled table costs you the segment.

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch 3Blue1Brown, ["The medical test paradox, and redesigning Bayes' rule"](https://www.youtube.com/watch?v=lG4VkPoG3ko) | 21 min | One written answer: a test catches 99% of cases — why isn't a positive result 99% proof you're sick? |
| 2 | Work the base-rate fraud one-pager (GAP-1 handout): a detector catching 99% of fraud, 1% false-positive rate, fraud in 1 of 10,000 transactions — fill in the counts table for 1,000,000 transactions | 9 min | The completed counts table (checked live in segment 2 — **now load-bearing**, not a warm-up) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Probability as degrees of belief; conditioning via fraud | 12 min | talk + worked example | Probability as a bet, not a mystery: "0.87 spam" is a strength of belief given evidence. Conditioning in natural frequencies, no algebra: of transactions *that are fraud*, 99% trigger an alert — P(alert \| fraud) = 0.99. Flip it: of transactions *that triggered an alert*, how many are fraud? Not 99% — that's the inverse, and it depends on the base rate. Landing line: every model output is P(answer \| inputs, training data) — conditional on data you must ask about (callback to `LSN-0.2`). *Rescope: tightened to the flip itself; the leisurely build-up goes, the flip does not* |
| Base rates: check the arithmetic, then decide | 15 min | worked example + discussion | Participants arrive with the counts table filled (pre-work task 2), so this segment **checks** rather than builds: put two tables on screen, reconcile against the reference — base rate 1/10,000 → **100 fraud**, detector catches 99% → **99 caught**; 999,900 legit × 1% false-positive → **9,999 false alarms**. Alert queue: 10,098 alerts, 99 real — **under 1% of alerts are fraud**, from a "99% accurate" detector. Then the discussion worth a room: what would you do — raise the threshold (miss more fraud), improve features, or staff the queue? Name the quantity: this fraction is *precision*; formal treatment with recall and the confusion matrix in `LSN-1.3`. *Rescope: the "what would you do" gets tested numerically in homework task 2* |
| Correlation vs causation | 13 min | talk + examples | The frame, which is the transferable part: the four explanations for "A moves with B" — A→B, B→A, C→both (confounder), coincidence. One famous trap live (ice-cream sales and drownings; confounder: summer) plus the business trap that lands in VSP conversations: "customers who use feature X churn 40% less" — power users self-select into X; X may drive nothing. *Rescope: the [Tyler Vigen](https://tylervigen.com/spurious-correlations) gallery is browsing, not teaching — it moves to homework task 3, where each pair gets classified against the four explanations* |
| Drill: the revenue chart | 20 min | drill | Scenario written below. Groups of 3, 6 min to list their questions; 14 min debrief against the instructor list. Untouched by the rescope — the drill is the reason to be in a room |

**Timing check:** 12 + 15 + 13 + 20 = 60 min = 1 h — matches the spreadsheet contract.

### The revenue-chart drill — scenario card

A retail e-commerce prospect (~$40M GMV) wants VSP to expand their "AI success." The chart: a recommendation widget launched **Nov 3**; Nov–Dec revenue is **+18%** vs. Sep–Oct; the widget-adoption curve rises right alongside revenue. The CTO: *"The widget drove the 18%. We want you to build phase two."*

What do you ask? Instructor debrief list:

1. **Seasonality** — Nov–Dec is the holiday quarter. What did revenue do last Nov–Dec, without the widget?
2. **What else changed?** — Ad spend, promotions, pricing, a site redesign shipping in the same window?
3. **Self-selection** — Who uses the widget? If engaged buyers click recommendations, the widget marks good customers rather than making them.
4. **Was there a holdout?** — Did any traffic run without the widget? A/B numbers, or observational only?
5. **The denominator** — Is that total revenue, or revenue *through widget clicks*? (Attributed revenue often just relabels purchases that would have happened anyway.)

Punchline: the only clean answer to "did it cause the lift?" is a counterfactual — a holdout. If none exists, phase two should include one. That's the intelligent-next-question move (GOAL-1) — the drill's pass bar is asking for the counterfactual, not reciting "correlation isn't causation."

## Client Tie-In (Dorel's rule)

The 6MAP translation gap (GOAL-4) is the frame: an AI engineer says "the model scores 0.93" and a delivery engineer hears "93% correct" — this session is where that misreading becomes impossible. The revenue-chart drill is a realistic pre-sales scenario of the kind VSP fields; the fraud detector is the shared example that `LSN-1.3` grades formally.

## Homework — 90 min

Async, graded pass/fail; submissions reference LSN-0.3. Feeds `ASM-0`.

| # | Task | Time | Artifact |
|---|---|---|---|
| 1 | The three scenario questions (below) | 25 min | Written answers — question 3 needs the counts shown |
| 2 | **Relocated from live segment 2:** run the session notebook's threshold cells and answer the "what would you do" question with numbers instead of instinct — what alert threshold gets the queue to 20% real, what recall do you give up to get there, and would you sell that trade to the client? | 20 min | The threshold/recall pair + three sentences of recommendation |
| 3 | **Relocated from live segment 3:** browse [Tyler Vigen's spurious correlations](https://tylervigen.com/spurious-correlations), pick two pairs, and add one correlation from your own project's reporting. For each of the three, name which of the four explanations you believe and why | 15 min | Three classified pairs with one-line justifications |
| 4 | Finish the drill properly: design the phase-two holdout you told the CTO they needed. What traffic is split and how, what is measured, for how long, and what result would make you say the widget does nothing? | 20 min | ~5 sentences — this is the GOAL-1 pass bar, asking for the counterfactual rather than reciting the slogan |
| 5 | The 6MAP translation: an AI engineer hands you "the model scores 0.93." Write the sentence you would say to a delivery engineer that is both true and useful — no jargon, no false precision | 10 min | One sentence, plus one line on what you had to ask the AI engineer first |

**Time accounting:** pre-work 30 min + homework 90 min = 2 h out-of-session budget.

Thursday evening also carries `LSN-0.4`'s 20 min pre-work (~110 min total). Task 4 is the designated trim — it is the most valuable task here, so trimming it is a real cost and should be a decision, not a default.

### The three scenario questions

1. A prospect: "our churn model is right 95% of the time." Their churn rate is 5%. What single question do you ask first, and why might 95% be worth nothing? (Pass: names the always-predict-"no-churn" baseline or class balance.)
2. A vendor's chart shows teams using their AI code-review tool ship 30% faster. Give two explanations for the correlation that aren't "the tool causes speed." (Pass: any two of self-selection, confounder such as team seniority or project type, reverse causation.)
3. A security scanner: 98% detection rate, 3% false-positive rate; real intrusions hit 1 in 500 sessions. Out of 50,000 sessions, roughly what fraction of alerts are real? (Pass: works the counts — ~98 real of ~1,595 alerts, ≈ 6% — arithmetic within reason.)

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Stats II deck** — 10 slides w/ timing notes, VSP design system | exists | `program/lessons/decks/LSN-0.3-statistics-2.html` |
| **Session notebook** — pre-work counts table + all four segments + drill reveal + self-checking homework, executed end to end | exists | `notebooks/lessons/LSN-0.3_Statistics_2_Probability_Correlation_Causation.ipynb` |
| Base-rate fraud one-pager (pre-work handout) | exists | notebook pre-work cell (fill-in counts table) |
| Drill scenario card + homework questions | exists | this file + notebook drill/homework sections + deck slide 8 |
| 3Blue1Brown — "The medical test paradox, and redesigning Bayes' rule" | exists | [youtube.com/watch?v=lG4VkPoG3ko](https://www.youtube.com/watch?v=lG4VkPoG3ko) |
| StatQuest with Josh Starmer — "Conditional Probabilities, Clearly Explained!!!" (optional reinforcement) | exists | [youtube.com/watch?v=_IgyaD7vOOA](https://www.youtube.com/watch?v=_IgyaD7vOOA) |
| Tyler Vigen — Spurious Correlations | exists | [tylervigen.com/spurious-correlations](https://tylervigen.com/spurious-correlations) |

## Delivery Notes

Not yet delivered — first run Thursday 3 September 2026. Watch: does the base-rate arithmetic land in counts alone, or do participants ask for the Bayes formula? (Resist — natural frequencies are the point at this tier.) New rescope risk: segment 2 now assumes filled pre-work tables. If more than two or three arrive without one, the check-and-decide segment collapses into a rebuild and the drill loses time — have the reference table on the slide so a cold participant can catch up in 30 seconds rather than 5 minutes.

**Rescope note (2026-08-03):** deck **retimed 2026-08-03** — segments 12 / 15 / 13 / 20, per-slide speaker-note timings summing to 60, segment 2 reframed as a check of the pre-work counts table, and the threshold sweep / spurious-correlations gallery reframed as homework hand-offs. The **notebook is still pending** its retiming round before delivery.
