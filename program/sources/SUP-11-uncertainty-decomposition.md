---
name: SUP-11-uncertainty-decomposition
description: The two kinds of uncertainty and the one question that separates them, why a single confidence number hides variation, what calibration actually means, and how a model should know it is out of its depth.
serves: LSN-0.4, LSN-0.2, LSN-1.6
sources: SRC-6 (deep-learning-for-science kit, Module 4)
---

# SUP-11 — The Uncertainty Decomposition

**The problem this solves.** `LSN-0.4` teaches three buckets — deterministic, probabilistic, stochastic —
and lands one excellent beat already built: the overconfident twin, two scorers making identical decisions
while one lies about its confidence by 9.6 points (`LL-23`). What the lesson does not yet have is
**vocabulary for *why* a system is uncertain**, and that vocabulary turns out to answer the single most
common pre-sales question in the whole program: *"if we give you more data, will it get better?"*

One slide of an otherwise graduate-level uncertainty-quantification lecture carries the whole thing. The
Bayesian machinery around it — posterior sampling, Hamiltonian Monte Carlo, variational inference,
Bayesian neural networks — is **explicitly out of scope for basics** and is noted at the end as an
expert-tier pointer.

---

## 1. Total uncertainty has three sources

When a model gives you an uncertain answer, the uncertainty came from somewhere, and there are only three
somewheres:

| Source | What it is | Commercial example |
|---|---|---|
| **The data** | Noisy measurements, gaps, records that were never collected | Delivery timestamps entered by hand, sometimes the next morning |
| **The model** | The chosen form is wrong, or the process itself has randomness the model does not represent | Estimating effort with a model that assumes tasks are independent when they block each other |
| **The fitting** | Architecture, hyperparameters, how much was fitted to how little | Two engineers train the same model on the same data and get different answers |

Naming three sources is already useful in a room: *"which of these three is your 8% error?"* is a
question a client's team can actually answer, and it usually reveals that nobody has asked it.

---

## 2. The two kinds — and the question that separates them

This is the core of the supplement.

| | **Aleatoric** | **Epistemic** |
|---|---|---|
| Comes from | Randomness in the process itself, and noise in the measurement | Not having enough data, and not knowing the right model |
| Reducible? | **No.** More data will not remove it | **Yes.** More and better data shrinks it |
| Feels like | "Two identical jobs took different amounts of time" | "We've never seen a job like this one" |
| Client sentence | "This much variation is real and will not go away" | "We can improve this, and here is roughly what it would take" |

**The whole thing collapses into one question, and it should be on a slide by itself:**

> ### Will more data fix this?

That question is:

- **The honest version of "how much data do we need?"** — the question `LSN-1.6` is built around and
  `LSN-1.4`'s degradation curve makes participants *feel* (accuracy vs training-set size at 10,000 →
  1,000 → 100 → 10). The curve flattens because the epistemic part is being eaten and the aleatoric part
  is not. **That flattening now has a name, one module before they see it.**
- **A quotable pre-sales differentiator.** "More data always helps" is what a weak vendor says. "More
  data will move about this much of your error, and this much of it is irreducible variation in your own
  process" is what a credible one says.
- **A direct fit for `LSN-0.4`'s three buckets.** Stochastic behaviour in the world produces aleatoric
  uncertainty. Probabilistic model outputs carry both kinds mixed together, and the client cannot tell
  them apart from the number alone — which is exactly the lesson's thesis about reading a confidence.

---

## 3. Constant spread versus varying spread

Two systems can report the same average error and behave completely differently:

- **Constant spread (homoscedastic)** — the model is about as uncertain everywhere. One error bar
  describes the whole system honestly.
- **Varying spread (heteroscedastic)** — the model is tight in the region it has seen a lot of and wide
  everywhere else. **A single reported error is then a fiction**: it is neither the reliable case nor the
  unreliable one.

**The commercial translation, and it is the sentence to teach:**

> *"It is accurate for your standard jobs and unreliable for your unusual ones — and the headline number
> is an average of the two, so it describes neither."*

This is `LSN-0.2` segment 3 ("when the average lies") arriving as a property of *model output* rather than
of input data — the same idea one lesson later, which is exactly the callback structure MOD-0 is built
on. It is also `LSN-1.3`'s per-segment decomposition beat (`LL-36`: a 38-hour headline MAE hiding
330-hour misses, with 85.9% of the error in 10% of the items) two modules early. **Three appearances of
one idea across three modules is a spine, not a repetition** — worth naming as such in the lesson plans.

**Pre-sales question this generates:** *"Is that error rate the same across all your cases, or is it an
average over easy and hard ones?"*

---

## 4. Calibration — what "90% confident" is supposed to mean

A model is **calibrated** if, across all the times it said "90% confident," it was right about 90% of the
time. Not 60%. Not 99%.

This is the name for what `LSN-0.4` already demonstrates. The overconfident-twin prop shows two scorers
making identical decisions where one's confidence is inflated by 9.6 points — that is a **calibration
failure**, and giving it the term turns a memorable demo into a transferable concept participants can
carry into a client meeting.

**The check is simple enough to run in the existing environment (pure numpy/pandas):**

1. Bucket every prediction by the confidence it stated — 50–60%, 60–70%, and so on.
2. In each bucket, compute the fraction that were actually correct.
3. Plot stated confidence against observed accuracy. A calibrated system sits on the diagonal; a system
   above the diagonal is underconfident; a system below it — the common case — is overconfident.

**Why this is the highest-value item in this file for `LSN-0.4`:** the lesson's homework already asks for
a contract acceptance criterion per probabilistic and stochastic behaviour. "Calibrated within X points
across confidence buckets" is a *real, checkable* acceptance criterion — arguably a better one than a
bare accuracy threshold, because it is what makes a confidence number safe to act on. It is a strong
candidate for the acceptance-criterion homework task, as a swap for one of the existing prompts.

**And the client sentence it unlocks:** *"Before you route anything on this model's confidence score, we
should check whether the score means what it says. That is a half-day of work and it decides whether you
can automate the high-confidence cases."*

---

## 5. Knowing when you are out of your depth

A separate property from calibration: can the system recognize that an input is unlike anything it was
trained on, and say so, rather than answering confidently?

This is the formal version of `LSN-1.6`'s "it can only infer so far" — the truism Vlad quoted back from
6MAP. At basics level the takeaway is not a method, it is a **question to ask**:

> *"What does the system do when it gets something it has never seen? Does it say so, or does it guess
> with the same confidence as always?"*

Most systems, unaided, do the second thing. That is worth knowing before promising anything about
robustness, and it is the concrete reason `LSN-2.6`'s golden eval set includes deliberately unanswerable
questions — that homework is already testing exactly this behaviour, one module later. Worth connecting
explicitly.

---

## 6. Explicitly out of scope

The source lecture's actual subject — Bayesian neural networks, posterior sampling, Hamiltonian Monte
Carlo, variational inference, deep ensembles, model averaging — is graduate-level and serves no basics
outcome. **Do not pull it into MOD-0.** The one place it could earn a mention is the expert tier's
evaluation-framework work, where ensemble disagreement is a practical uncertainty estimate. Noted in
`PROGRAM_PLAN.md` terms as an expert-tier candidate, not proposed here.

The rule this illustrates, worth keeping: a supplement's value is not the source's depth. One slide of a
30-slide graduate lecture was worth more to this program than the other 29 combined.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-0.4` segment 1 | The aleatoric/epistemic split and the "will more data fix this?" question sharpen the deterministic/probabilistic/stochastic buckets — participants' own examples get sorted twice, by bucket and by reducibility | **Sharpen an existing 25-min segment — no minutes move** | Deck edit |
| `LSN-0.4` segment 2 | §3's varying-spread sentence is a ready-made client-expectation line for "setting client expectations when outputs vary between runs" | Segment material | Deck edit |
| `LSN-0.4` homework | The calibration check (bucket by stated confidence, compare to observed accuracy) as a **candidate swap** into the acceptance-criterion task — it produces a criterion that is checkable rather than aspirational | **Swap within an existing 25-min task** | Notebook edit, pure numpy |
| `LSN-0.4` | Calibration names the existing overconfident-twin prop (`LL-23`) | Terminology | None |
| `LSN-0.2` segment 3 | §3 is the model-output half of "when the average lies" — a forward reference that sets up `LSN-0.4` and `LSN-1.3` | Framing note | None |
| `LSN-1.6` | §5's out-of-depth question is a question-bank addition; §2 is the honest answer to "how much data do we need?" | Bank addition | Small |
| `LSN-2.6` | §5 explains why the golden eval set carries deliberately unanswerable questions | Framing note | None |

## Proposals requiring a spec decision

**None outstanding — adopted 2026-08-11**, with a better placement than originally proposed. Rather than
displacing the eval-set sizing task, the calibration check became its **second half**: homework task 3 is
now 20 minutes split 12 + 8, covering *how many questions the acceptance bar needs* and *whether the
confidence attached to the answers is honest* — two halves of one acceptable criterion, which is a
stronger pairing than either alone. Segment 1 also gained the reducible/irreducible axis, bought from two
of the three misfiled-favourite debates. **`LSN-0.4` had no prior rebuild debt, so these two changes create
one small round** — carried in the MOD-0 build list, due before Fri 4 Sep 2026.
