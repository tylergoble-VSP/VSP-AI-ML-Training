---
name: LSN-0.3-statistics-2-probability-correlation-causation
description: Read model outputs as conditional probabilities, run base-rate arithmetic in your head, and catch correlation-vs-causation traps in a client's data story.
module: MOD-0
serves: OUT-0.3, OUT-0.4
duration: 1.5 h
prework_time: 30
owner: Tyler
status: draft
---

# LSN-0.3 — Statistics II: Probability, Conditioning, Correlation ≠ Causation

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.3`, `OUT-0.4` |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | `ASM-0` (scenario questions, not definitions) |

## Narrative

Two misconceptions die here: that "99% accurate" means an alert is 99% likely to be real, and that a chart moving with revenue proves the feature caused the revenue. Every model output the cohort will ever read is a conditional probability, and confusing P(alert | fraud) with P(fraud | alert) — or correlation with causation — is exactly how a pre-sales conversation goes wrong. Builds on the sampling skepticism from `LSN-0.2`; the fraud detector built here is deliberately reused in `LSN-1.3`, where "fraction of alerts that are real" gets its formal name: precision.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Watch 3Blue1Brown, "The medical test paradox, and redesigning Bayes' rule" — https://www.youtube.com/watch?v=lG4VkPoG3ko | 21 min | One written answer: a test catches 99% of cases — why isn't a positive result 99% proof you're sick? |
| 2 | Work the base-rate fraud one-pager (GAP-1 handout): a detector catching 99% of fraud, 1% false-positive rate, fraud in 1 of 10,000 transactions — fill in the counts table for 1,000,000 transactions | 9 min | The completed counts table (checked live in segment 2) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Probability as degrees of belief; conditioning via fraud | 25 min | talk + worked example | Probability as a bet, not a mystery: "0.87 spam" is a strength of belief given evidence. Conditioning in natural frequencies, no algebra: of transactions *that are fraud*, 99% trigger an alert — P(alert \| fraud) = 0.99. Flip it: of transactions *that triggered an alert*, how many are fraud? Not 99% — that's the inverse, and it depends on the base rate. Landing line: every model output is P(answer \| inputs, training data) — conditional on data you must ask about (callback to `LSN-0.2`) |
| Base rates: the arithmetic on screen | 25 min | worked example + discussion | Check pre-work tables, then build it together for 1,000,000 transactions: base rate 1/10,000 → **100 fraud**, detector catches 99% → **99 caught**; 999,900 legit × 1% false-positive → **9,999 false alarms**. Alert queue: 10,098 alerts, 99 real — **under 1% of alerts are fraud**, from a "99% accurate" detector. Discussion: what would you do — raise the threshold (miss more fraud), improve features, or staff the queue? Name the quantity — this fraction is *precision*; formal treatment with recall and the confusion matrix in `LSN-1.3` |
| Correlation vs causation | 20 min | talk + examples | The four explanations for "A moves with B": A→B, B→A, C→both (confounder), coincidence. Famous traps: ice-cream sales and drownings (confounder: summer); Tyler Vigen's spurious-correlations pairs (coincidence at scale — tylervigen.com); the business trap: "customers who use feature X churn 40% less" — power users self-select into X; X may drive nothing |
| Drill: the revenue chart | 20 min | drill | Scenario written below. Groups of 3, 8 min to list their questions; 12 min debrief against the instructor list |

**Timing check:** 25 + 25 + 20 + 20 = 90 min = 1.5 h contract duration.

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

## Homework

Three scenario questions, async, graded pass/fail; submission references LSN-0.3. Feeds `ASM-0`.

1. A prospect: "our churn model is right 95% of the time." Their churn rate is 5%. What single question do you ask first, and why might 95% be worth nothing? (Pass: names the always-predict-"no-churn" baseline or class balance.)
2. A vendor's chart shows teams using their AI code-review tool ship 30% faster. Give two explanations for the correlation that aren't "the tool causes speed." (Pass: any two of self-selection, confounder such as team seniority or project type, reverse causation.)
3. A security scanner: 98% detection rate, 3% false-positive rate; real intrusions hit 1 in 500 sessions. Out of 50,000 sessions, roughly what fraction of alerts are real? (Pass: works the counts — ~98 real of ~1,595 alerts, ≈ 6% — arithmetic within reason.)

## Materials

| Material | Status | Path / source |
|---|---|---|
| Stats II deck (conditioning, base rates, causation) | build (`GAP-1`) | `program/` — new |
| Base-rate fraud one-pager (pre-work handout) | build (`GAP-1`) | numbers in this file, segment 2 |
| Drill scenario card + homework questions | build (`GAP-1`) | this file — extract to cards |
| 3Blue1Brown — "The medical test paradox, and redesigning Bayes' rule" | exists | https://www.youtube.com/watch?v=lG4VkPoG3ko |
| StatQuest with Josh Starmer — "Conditional Probability, Clearly Explained" (optional reinforcement) | exists | youtube.com/@statquest (verify exact link at delivery prep) |
| Tyler Vigen — Spurious Correlations | exists | tylervigen.com |

## Delivery Notes

Not yet delivered — first run Week 1. Watch: does the base-rate arithmetic land in counts alone, or do participants ask for the Bayes formula? (Resist — natural frequencies are the point at this tier.)
