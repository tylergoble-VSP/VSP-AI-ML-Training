---
name: SUP-7-failure-and-trust-catalog
description: The six structural weaknesses of learned systems, how a model gets deliberately fooled, and a method-by-method catalog of how you explain a conclusion to someone who distrusts it.
serves: LSN-2.6, LSN-3.5, LSN-1.5
sources: SRC-3, SRC-4
---

# SUP-7 — Failure and Trust Catalog

**The problem this solves.** `LSN-2.6` is the honesty lesson and `GAP-7` is its unbuilt failure pack.
`LSN-3.5` needs the production-side version of the same material. Both currently focus on
language-model-specific failures — hallucination, staleness, injection, privacy. The corpus adds the
older and more general layer underneath: **the ways learned systems fail regardless of what kind of model
they are**, plus a treatment of explainability that no other source in the corpus matches.

The explainability section in particular answers a question a client asks in almost every deal and that
`MOD-1` and `MOD-2` currently leave to improvisation: *"how will you tell me why it decided that?"*

---

## 1. Six structural weaknesses of any learned system

Not bugs. Properties. Each stated with its pre-sales question.

| # | Weakness | Pre-sales question |
|---|---|---|
| 1 | **Unrepresentative data yields confident wrong conclusions** | "How was this data collected, and who or what is missing from it?" |
| 2 | **Case selection carries its own bias** | "Which records made it into this extract, and which were filtered out?" |
| 3 | **Confounding factors can outrank the real ones** | "What else changed at the same time?" (`LSN-0.3`'s correlation drill, one level up) |
| 4 | **More inputs means more spurious importance** — with enough columns, something will look predictive by chance | "How many features, on how many rows?" |
| 5 | **With noisy data, the apparent best may be noise** — picking the top performer rewards luck | "How much did the second-best option differ, and is that gap larger than the run-to-run variation?" |
| 6 | **Outliers force a lose-lose** — leave them and the model overfits; remove them and you may delete the phenomenon the client cares about | "Are the unusual cases the noise, or the point?" |

Weakness 6 is the sharpest of these commercially, because the unusual cases are *routinely* the whole
business case — the fraud, the defect, the churn, the deal that closes. "We cleaned the outliers" and "we
removed the signal" are frequently the same sentence.

---

## 2. Adversarial manipulation — when someone wants your model to be wrong

### The demonstration to keep

A traffic sign classifier, reliable in ordinary conditions, is made to read a stop sign as a speed limit
sign by applying a few stickers — placed after deliberate experimentation to find the smallest change
that breaks it. A related result: changing a **single pixel** flips a classification.

**The point is not that the model is fragile.** The point is that **it was never using the features a
human uses.** A person identifies a stop sign by "red" and "octagon." The model found some other
correlated pattern that happened to work on the training data. It was always the wrong feature; the
stickers only made that visible.

This is `LSN-1.5`'s CNN segment with real stakes attached, and it is the honest answer to "the model gets
99% — why would it fail in the field?"

### The general strategy

Find cases near the decision boundary; construct similar cases that fall just on the wrong side. It
requires access or experimentation, not magic.

### Manipulation of the data you learn from

If a model analyses the behaviour of a party with an interest in the outcome, that party can shape the
data. Commercial versions, no domain jargon required:

- A supplier whose delivery reliability is scored learns which signals the model watches, and manages
  those rather than the underlying reliability.
- A merchant learns a fraud model's thresholds and structures activity just underneath them.
- Any party whose behaviour is scored eventually optimizes for the score. (`SUP-3` §7's Goodhart point
  again — a measure that becomes a target stops measuring.)

**The uncomfortable framing worth saying out loud:** a model's conclusions are inspected far less
carefully than a person's, which is exactly what makes them attractive to manipulate.

### Countermeasures, and their honest limits

- **Cross-check with a different kind of method.** If a statistical or neural model and a rule-based or
  tree-based model agree, manipulation targeted at one is less likely to have moved both.
- **Reduce model complexity** where overfitting is the exposure.
- **Compute statistics over your inputs** to detect distributional weirdness — which is a monitoring
  requirement, and therefore a `LSN-3.5` observability line item.
- **Keep some training data private.** If the data everyone can see has been shaped, the data only you
  hold has not.
- **Provide explanations**, so a strange conclusion can be interrogated rather than accepted.

**Terminology check worth making explicitly, because it is confused constantly:** *adversarial machine
learning* means an adversary manipulating your data or inputs. It is unrelated to *generative adversarial
networks*, which is a training technique. Confusing the two in a client meeting is expensive.

---

## 3. Explainability by method — the catalog

The commercial premise: **people distrust a surprising conclusion that arrives without a justification**,
and a good explanation covers both *why* and *why not*. This table is the most directly reusable artifact
in this file.

| Method family | What its explanation looks like |
|---|---|
| **Rules** | The rules that fired, and the data that matched them |
| **Decision trees** | The path down the tree, and the answer at each branch |
| **Probabilistic models** | The factors combined, and the statistics behind each |
| **Nearest-neighbour / case-based** | The most similar prior cases, shown to the user |
| **Sequence and path methods** | The chosen path, its cost, and the alternatives it beat |
| **Neural networks** | **None natively** — see below |

### Worked example of a rule explanation, kept because it is compact and domain-free

Given rules for triaging a support issue:

```
escalate_candidate   if  repeat_contact or sla_breach or vip_account
urgent               if  escalate_candidate and (revenue_at_risk or outage)
routine_escalation   if  escalate_candidate and not outage
direct_to_manager    if  revenue_at_risk and not escalate_candidate
```

A ticket is a repeat contact, has revenue at risk, and reports an outage → **urgent**.

- *"Why urgent?"* → repeat contact fired rule 1; revenue at risk and outage fired rule 2.
- *"Why not routine escalation?"* → rule 3 requires no outage; there is an outage.
- *"Why not direct to manager?"* → rule 4 requires *not* an escalate candidate; rule 1 already made it one.

Three questions, three precise answers, no hand-waving. **That is the standard against which a neural
system's explanation should be judged** — and it is why "the model is a black box" is a real cost, not a
philosophical remark.

### Explaining a neural network — the four honest options

Since the network offers nothing natively:

1. **Run an interpretable method alongside it** on the same data and show it reaches a similar
   conclusion — borrowing the simpler method's explanation.
2. **Train an interpretable method on the network's outputs** — the network can generate as much training
   data as you need. You get an approximate but inspectable stand-in.
3. **Show stability**: the same conclusion emerges from training on several different data sets,
   especially data the public does not have.
4. **Identify what mattered** — which inputs, neurons, or layers most influenced this specific
   conclusion.

**The residual honesty, worth teaching as the closing line:** none of these is the rule-based
explanation above. They are evidence about the model, not the model's reasoning. Trust in neural systems
is built largely by **accumulated successful use**, which is a slower and more expensive road than a
client expects — and saying so in discovery is exactly the credibility `GOAL-4` is asking for.

---

## 4. Testing a generative system is genuinely harder, and it is worth conceding

Three concrete reasons, useful because they explain a client's frustration rather than dismissing it:

1. **The output is natural language, which is ambiguous.** Precise specification is why we normally use
   mathematics or types.
2. **The behaviour varies run to run**, so a failure may not reproduce — which breaks the debugging loop
   most engineers rely on.
3. **Consequently it fits poorly with requirements-based acceptance**, which is how most enterprise
   software is contracted for.

Point 3 is a commercial fact, not a technical one, and it is the single most useful sentence in this file
for a delivery lead: **an acceptance criterion for a generative system has to be statistical** — a pass
rate on a defined evaluation set, not a list of behaviours that must always hold. `LSN-0.4`'s homework
already asks for exactly this ("a contract acceptance criterion per probabilistic/stochastic behaviour");
this is the argument for why that homework exists.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-2.6` segment 1 | §1's six weaknesses generalize the failure taxonomy beyond language models; §4 supplies the "why testing is hard" framing the segment currently asserts | Input to `GAP-7` | Reduces `GAP-7` build effort |
| `LSN-2.6` segment 3 | §3's rule-explanation example is a concrete standard for the "rewrite three overpromising statements" drill — "we'll explain the decisions" is one of the statements most in need of rewriting | Drill material | Small |
| `LSN-3.5` | §2's countermeasures are observability and monitoring requirements with a threat justification; §3 is a ready-made TL question-bank row ("how does this system explain a decision to a person who disagrees with it?") | Input to `GAP-4` | Reduces `GAP-4` build effort |
| `LSN-1.5` | The traffic-sign result is a strong, jargon-free closing beat for the CNN segment — the model was never using the features you assumed. Candidate swap, not an addition | Swap inside an existing segment — **no minute changes** | Deck edit |
| `LSN-1.6` | §1's six pre-sales questions are bank additions alongside the data-reality checks | Bank additions | Small |
| `LSN-0.4` | §4 is the justification for the existing acceptance-criterion homework; a two-line framing note | Framing note | None |

## Proposals requiring a spec decision

None. `OUT-2.6`, `OUT-3.4`, `OUT-1.5`, and `OUT-0.2` cover this ground. Deeper adversarial-robustness
work (attack construction, defensive training) is advanced/expert-tier and is deliberately not proposed
here.
