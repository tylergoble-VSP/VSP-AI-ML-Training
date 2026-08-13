---
name: SUP-3-metric-literacy-extension
description: The economics of precision vs recall, why a single score is a business decision, the AUC caveat, and the separate metric family you need once the output is generated text.
serves: LSN-1.3, LSN-2.6, LSN-3.5
sources: SRC-3, SRC-4
---

# SUP-3 — Metric Literacy Extension

**The problem this solves.** `LSN-1.3` already teaches MAE, precision/recall, the confusion matrix, and
AUC, and it already lands two strong beats: the rubber-stamp comparison (a 99.0%-accurate detector losing
to a 99.99% do-nothing stamp) and the metric-consistency feasibility check. What the corpus adds is the
layer *above* those: **which error is expensive here, and who decides.** Plus one thing `MOD-1` cannot
cover because it has not happened yet — metrics for when the model's output is generated text, which
`MOD-2` needs and `LSN-2.6` currently gestures at.

---

## 1. The one-sentence definitions, stated the way a client will hear them

Given a model that flags items:

- **Recall** = of the things that were genuinely there, what fraction did we catch?
- **Precision** = of the things we flagged, what fraction were genuinely there?

**Worked example, commercial and jargon-free.** An inspection model reviews finished panels. Quality
inspectors, going slowly by hand, find 100 genuinely defective panels in a batch. The model flags 80
panels: 60 of the genuinely defective ones, plus 20 good panels it got wrong.

- Recall = 60 / 100 = **0.60** — it missed 40 defects.
- Precision = 60 / 80 = **0.75** — a quarter of what it flagged wastes an inspector's time.

That single example carries the whole segment, and it survives being read aloud to a client.

---

## 2. You cannot have both, and the trade is a business decision

Push the threshold down and you catch everything, including a flood of false alarms: **high recall, low
precision.** Push it up and everything you flag is real, but you miss most of the problem: **high
precision, low recall.** The full sweep is the precision-recall curve, and a better model is one whose
curve sits above another's across the range you actually operate in.

**The commercial framing that makes this land — two industries, opposite answers:**

| Situation | Which error is expensive | Therefore optimize |
|---|---|---|
| Catching fraudulent transactions, safety defects, security incidents | A miss is a real loss; a false alarm costs a review | **Recall** — accept false alarms |
| Ranking search results, generating leads for a sales team to call, auto-approving anything | Nobody looks past the top few; a bad one wastes the expensive resource | **Precision** — accept misses |

Notice that both are "the same model doing the same job." The metric is chosen by the *cost structure*,
not by the algorithm — which is exactly the `LSN-1.3` question "which error is expensive for **this**
client?" now backed by two named industry patterns rather than one.

### The single-number squeeze, and its trap

When someone demands one score, the convention is the **F1 score** — the harmonic mean of precision and
recall, which can be written directly from counts as
`true positives / (true positives + ½ (false positives + false negatives))`.

The harmonic mean punishes imbalance: 0.9 precision with 0.1 recall gives F1 ≈ 0.18, not 0.5. That is the
feature.

**But F1 weights the two errors equally, and almost no business does.** The generalization (F-beta)
tilts it — weight recall more when misses hurt, precision more when false alarms hurt. The teachable
version is not the formula, it is the question: *"When you ask for one number, are you telling us that a
miss and a false alarm cost you the same? Because they usually don't."* That sentence belongs in the
`LSN-1.3` client drill and again in the `LSN-3.5` KPI segment.

---

## 3. Two traps that ride along with the metric

### "Find out what positive means"

`SRC-4` makes this its loudest point and it is worth stealing wholesale. Before reading anyone's
confusion matrix, establish which class was labeled positive. Half the confusion-matrix
misreadings in the wild are a transposed or relabeled matrix — and the numbers are all still *internally
consistent*, so nothing looks wrong.

**Drill (2 min, fits the existing `LSN-1.3` confusion-matrix segment):** hand the room one matrix with
the positive class unstated and ask for precision. There is no answer. That is the lesson.

### "0.9 AUC — that's great, right?"

Not necessarily. AUC summarizes the model's ranking across *every* threshold, including thresholds nobody
would ever run in production. A model can score 0.9 and still be useless at the one operating point the
client cares about — for example, at the false-alarm rate their review team can actually absorb.

**The question to ask instead:** *"At the false-alarm rate you can staff, what fraction do you catch?"*
That is a single point on the curve, and it is the only point that has a budget attached.

This composes directly with `LSN-1.3`'s existing feasibility check (does a quoted precision/recall/AUC
triple even sit inside the geometrically possible range?). Together they are two halves of one skill:
**is the number possible, and is it relevant?**

---

## 4. Class balance is a metric problem before it is a data problem

You need both positive and negative cases, in usable proportion. With a 1%-positive training set, a model
that always says no is 99% accurate and completely worthless — and every summary statistic will look
fine. Two consequences, both `LSN-1.3` material:

- **On the data side:** sample the rare class up (see `SUP-2` §5), aiming near a balanced training set.
- **On the metric side:** never quote accuracy on an imbalanced problem. Quote precision and recall, or
  quote against the do-nothing baseline — which `LSN-1.3` already does with the rubber-stamp beat.

**Pre-sales question:** *"What does your current process catch, and at what false-alarm rate?"* Without
that baseline, "our model is 92% accurate" is unfalsifiable.

---

## 5. Testing honestly — cross-validation and the vocabulary of tuning

Test on data you did not train on. But a single split is a lottery: a lucky test set flatters you and an
unlucky one buries you. **Cross-validation** rotates the split — train on one portion, test on the rest,
repeat several times with different portions, average the results. A typical setup is ten rotations of a
75/25 split.

This gives the room a clean distinction they will need in every later module:

- **Parameters** are what the model learns from the data.
- **Hyperparameters** are what *you* choose: the split ratio, the number of training passes, the decision
  threshold, the learning rate.

**Why this matters commercially:** when a vendor quotes a metric, "on what split, averaged over how many
runs?" separates a measured claim from a lucky one. It is the same instinct as `LSN-0.2`'s "92% accurate
— on what data?" drill, one level deeper.

---

## 6. Metrics change shape when the output is generated text

`MOD-1`'s metrics assume there is a correct answer to compare against. Once a model writes a paragraph,
there are many acceptable answers, and the metric family changes. `LSN-2.6` currently promises "measured
quality, not vibes" and the golden-eval homework delivers on it — this section gives that homework its
vocabulary.

| Metric | What it measures | Reads like |
|---|---|---|
| **Word-overlap, precision-flavored** | How much of what the model wrote appears in a reference answer | Precision, for generated text |
| **Word-overlap, recall-flavored** | How much of the reference answer the model managed to cover | Recall, for generated text |
| **Embedding similarity** | Whether the output *means* the same thing as the reference, even in different words | The upgrade over word overlap — and the reason `LSN-2.3` matters |
| **Perplexity** | How surprised the model is by the text — a model-health number, not a quality number | Frequently misquoted as quality; treat as a red flag when cited alone |
| **Relevance** | Did it answer the question that was asked? | Human or model-as-judge |
| **Coherence** | Is it well-written and internally consistent? | Human or model-as-judge |

**The honest framing for a client:** the first three need a reference answer, which means someone has to
write one — that is what a golden eval set *is*, and it is why `LSN-2.6`'s 20-question homework is
expensive. The last two need a judge. Neither is free, and a vendor claiming quality with neither has
measured nothing.

### The judged-quality caveat, kept from `SRC-1`

When a language model grades another model's output, it is fast, cheap, and correlates decently with
human judgment — and it inherits the grader's biases, prefers longer answers, and cannot catch an error
it would have made itself. Use it for regression detection (did today's prompt change make things
worse?), not for absolute quality claims. This is already the `LSN-3.5` position; `SUP-3` gives it the
metric context.

---

## 7. Benchmarks and leaderboards — the caveat that belongs in a client conversation

Four documented failure modes, from `SRC-1`:

1. **Overfitting to the benchmark** — models trained to win the test.
2. **Contamination** — the benchmark's questions were in the training data.
3. **Representation gaps** — the benchmark does not look like your work.
4. **Compressed scoring** — everyone clusters at the top, so the ranking stops discriminating.

The one-liner that carries it: **when a measure becomes a target, it stops being a good measure.**

**Therefore:** a public leaderboard position is a shortlist filter, not evidence. The evidence is a small
evaluation set built from *your* client's actual work — which is precisely `LSN-2.6`'s golden-eval
homework. Naming the leaderboard's weakness is what makes that homework feel necessary rather than
academic.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-1.3` | The panel-inspection worked example is a candidate replacement for a generic precision/recall illustration in segment 2; "find out what positive means" is a 2-min addition inside the existing confusion-matrix segment; the AUC caveat sharpens segment 4's existing "when a client quotes 99% accuracy" beat | Swap + sharpen inside existing segments — **no minute changes** | Deck edit |
| `LSN-1.3` homework | The F-beta question ("does a miss cost the same as a false alarm?") and the cross-validation question ("on what split, averaged how?") join the report-card verdict prompts | Bank additions | Small |
| `LSN-2.6` | §6 supplies the vocabulary for the existing 20-question golden-eval homework; §7 supplies the *motivation* for it | Framing input to `GAP-7` | Reduces `GAP-7` build effort |
| `LSN-3.5` | §2's cost-structure table and §6's judged-quality caveat feed the evals and KPI segments of the `GAP-4` build | Input to an unbuilt gap | Reduces `GAP-4` build effort |

## Proposals requiring a spec decision

None. `OUT-1.3`, `OUT-2.6`, and `OUT-3.4` all already claim this ground.
