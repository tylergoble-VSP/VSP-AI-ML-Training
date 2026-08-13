---
name: SUP-12-bias-and-disaggregation
description: Six named ways a dataset misrepresents the world, the headline metric that hides a 63-point gap, five test strategies, and why "fair" has competing definitions the client must choose between.
serves: LSN-0.3, LSN-0.2, LSN-1.3, LSN-1.6
sources: SRC-4 (data-science kit, Module 4)
---

# SUP-12 — Bias and Disaggregation

**The problem this solves.** `LSN-0.2` segment 2 is "Sampling debrief + bias, which no sample size fixes"
— fifteen minutes of discussion on a concept the lesson plan names but does not enumerate. `LSN-0.3`
teaches the correlation-versus-causation traps and the base-rate flip. Both are one level short of the
question a senior actually gets asked: **"how would this data be wrong in a way we would not notice?"**

`SRC-4`'s data-ethics module answers it with named types and one arithmetic example that is worth the
whole module.

---

## 1. Six named ways a dataset misrepresents the world

Generic "bias" is unactionable. Named types are checkable. Each below is stated with a commercial tell
rather than the source's societal examples — the mechanism is identical and the vocabulary transfers.

| Type | What happens | Commercial tell |
|---|---|---|
| **Reporting bias** | What gets recorded does not match how often things actually happen — people record the notable, not the normal | Support tickets capture complaints, not satisfaction. A model trained on tickets learns a world where everything is broken |
| **Selection bias** | The records you have are not a random sample of the records that exist | The CRM contains deals someone bothered to log. Deals that died in week one are missing — so the model never learns what a dying deal looks like |
| **Temporal bias** | The population or behaviour changed between when the data was collected and now | Two years of pre-reorganization delivery data, used to estimate post-reorganization delivery |
| **In-group bias** | The people building or labelling favour patterns they recognize | Estimators rate work resembling their own past projects as lower risk |
| **Out-group homogeneity bias** | Cases outside the familiar group get treated as interchangeable | Every client in an unfamiliar sector is scored on one generic profile |
| **Confirmation bias** | Data is processed in a way that confirms what was already believed | The analysis that keeps getting rerun until it agrees with the pitch |

**Two structural points from the source worth keeping verbatim in spirit:**

1. **Data is a mirror.** Bias exists in the process the data came from; a model trained on it learns the
   pattern, including that part. Nothing about the algorithm introduces or removes it.
2. **Labels carry the labeller's beliefs.** This is already one of the program's strongest built props —
   `LSN-1.6`'s inherited-labeller demonstration (`LL-49`: two honest managers, ~82% agreement, one signs
   off 1.58× as often as the other, and the model inherits +8.0 points of optimism). **`LSN-0.3` can now
   name the mechanism two modules before `LSN-1.6` demonstrates it**, which is exactly the callback
   structure MOD-0 exists to set up.

**The drill this supports (fits `LSN-0.2` segment 2's existing 15 minutes as a swap):** give the room one
dataset description — *"18 months of won and lost deals, exported from the CRM"* — and ask which of the
six are present. The answer is at least three, and participants find them themselves.

---

## 2. The headline metric that hides a 63-point gap

The single most valuable item in the module. An admissions-screening model reports:

> **91% accurate.**

Broken down by group, the same model is:

> **95% on the majority group. 32% on the minority group.**

Nothing is wrong with the 91%. It is arithmetically correct, and it describes a model that is worse than
a coin flip for a third of the people it decides about.

**Why this is `LSN-0.3` material and not just an ethics point.** The lesson already teaches that a
conditional probability flips (`P(alert | fraud)` versus `P(fraud | alert)`) and that a base rate makes a
headline number meaningless. This is the third member of that family: **a headline number averaged over
unequal subgroups describes none of them.** Same skill — refuse the aggregate, ask for the decomposition.

**The rule to teach, in the form a senior uses it:**

> *"Never accept a single headline metric. Ask for it broken down by the segments the client actually
> cares about — and if nobody has ever computed that, that is the finding."*

**This is now the program's spine, appearing four times:**

| Lesson | Appearance |
|---|---|
| `LSN-0.2` | The average lies when variance is high or outliers dominate |
| `LSN-0.3` | The aggregate lies when subgroups differ — 91% = 95% and 32% |
| `LSN-0.4` | The confidence lies when spread varies by region (`SUP-11` §3) |
| `LSN-1.3` | The MAE lies when error concentrates — 38 h headline, 330 h misses, 85.9% of error in 10% of items (`LL-36`) |

Worth stating explicitly in the module-0 spec: it is one idea, taught four times at increasing
resolution, and naming it as a spine makes the callbacks land instead of feeling repetitive.

---

## 3. Five ways to test for it

A reusable evaluation-design checklist, and the most transferable part of the module:

| Strategy | What it is | Cost |
|---|---|---|
| **Targeted** | Test the cases prior knowledge says are likely to fail | Cheap; needs domain knowledge |
| **Quick** | Check the extremes. Low coverage, fast, catches the obvious | Very cheap — do this always |
| **Comprehensive** | Enough test data for every subgroup, and every relevant combination of attributes | Expensive; reserve for high-impact decisions |
| **Ecologically valid** | Test on real-world conditions and on newer data than the model was trained on | Moderate; the one most often skipped |
| **Adversarial** | Test rare but severe failures deliberately | Needs domain knowledge; where the reputational risk lives |

**Where this lands beyond MOD-0:** it is a ready-made structure for designing an evaluation set at any
level — `LSN-2.6`'s 20-question golden set (15 answerable, 5 unanswerable) is *quick* plus *adversarial*,
and naming the two strategies it uses shows participants what it is missing. `LSN-3.5`'s eval suites and
`SUP-8`'s assessment design use the same five.

---

## 4. "Fair" has competing definitions, and the client picks

Three standard definitions, and they **cannot generally all hold at once**:

- **Equal catch rate** — the model catches the same fraction of genuine cases in each group.
- **Equal catch rate *and* equal false-alarm rate** — both error rates match across groups.
- **Equal flag rate** — the model flags the same proportion of each group, regardless of the underlying
  rates.

Pick different definitions and you get different models from the same data. That is a mathematical fact,
not a values disagreement — and it means **someone has to choose, and it should not be the engineer
choosing by default.**

**The basics-level takeaway is the judgment, not the formulas:**

> *"There are at least three definitions of 'treated fairly' here and they conflict. Which one does your
> policy actually mean? That is your decision, and we will build to whichever you name."*

This is `GOAL-4` — the translation gap — in a single exchange, and it fits `LSN-0.3`'s existing
correlation-versus-causation segment as one worked contrast rather than a new topic. The detailed
metric definitions belong in `LSN-1.3` if anywhere; at MOD-0 the point is that a choice exists.

---

## 5. Two documentation artifacts worth asking a vendor for

Both are established practice and both are excellent pre-sales questions because a vendor who has them
is a different kind of vendor:

- **A datasheet for the dataset** — how it was collected, who is in it, what it was intended for, what it
  should not be used for.
- **A model card** — what the model was evaluated on, its performance **broken down by segment**, and its
  known limitations.

**Pre-sales question:** *"Do you have a model card, and does it break performance down by segment?"* The
answer is usually no, which makes it a work package with a name — the same commercial inversion
`LSN-1.6` already teaches with its five-row "no → work package" pattern.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-0.2` segment 2 | The six named types replace generic "bias" in the existing sampling-bias discussion; the CRM-export drill gives the segment a concrete artifact to work on | **Swap inside an existing 15-min segment — no minutes move** | Deck edit |
| `LSN-0.3` segment 2 | The 91% / 95% / 32% decomposition joins the base-rate family as the third member — refuse the aggregate, ask for the breakdown | **Addition to an existing 15-min segment as a worked example** | Deck + notebook |
| `LSN-0.3` segment 3 | §4's competing-definitions contrast is one worked exchange, not a new topic | Segment material | Deck edit |
| `LSN-0.3` homework | §3's five test strategies structure the existing "design the phase-two holdout" task | Structure for an existing task | Small |
| `LSN-1.3` | §2 is the classification-metric sibling of the per-segment MAE beat already built | Framing note | None |
| `LSN-1.6` | §1.2 names the mechanism the inherited-labeller prop demonstrates; §5's two artifacts are question-bank additions | Bank additions | Small |
| `LSN-2.6`, `LSN-3.5` | §3's five strategies are an eval-design structure at every level | Input to `GAP-7`, `GAP-4` | None |

## Proposals requiring a spec decision

**None outstanding — adopted 2026-08-11.** The "refuse the aggregate" spine is now named in all four
lesson plans' Narrative sections, numbered 1-of-4 through 4-of-4, and tabulated in
`module-0-foundations.md`. `LSN-0.3` also swapped scenario question 1 (which duplicated question 3's
base-rate skill) for the disaggregation question, and homework task 4's holdout design is now structured
by the five test strategies. Both are swaps inside existing budgets.
