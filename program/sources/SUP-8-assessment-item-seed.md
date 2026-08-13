---
name: SUP-8-assessment-item-seed
description: Coverage map, item-quality rules with two documented failure modes, worked definition-to-scenario rewrites, and the deliverable shapes that make an assessment rubric gradeable — seed material for GAP-6.
serves: ASM-0, ASM-1, ASM-2, ASM-3
sources: SRC-2, SRC-3
---

# SUP-8 — Assessment Item Seed

**The problem this solves.** `GAP-6` — every checkpoint quiz, the basics final, and the mock-conversation
rubrics — is open across all four modules, needed from **Fri 4 Sep 2026** (`ASM-0`), and currently a blank
page. The corpus contains a ~537-item multiple-choice bank across nine generative-AI modules and a
short but unusually sharp treatment of how machine-drafted assessment items go wrong.

**Read the licensing rule first.** That bank is licensed non-commercially (`README.md`, Licensing). Do
**not** copy items. Use it for two things it is genuinely good for — **coverage** (what a competent course
tests) and **format discipline** — and write VSP's own items, which the spec requires regardless:
`ASM-n` items are *scenario* questions, not definitions (`module-0-foundations.md`, ASM-0: "scenario
questions, not definitions").

---

## 1. What the source bank is good for

**Format, per item:** a question stem, exactly four options, one recorded correct answer. Flat, machine-
gradeable, one concept per item. That format is right for the async portions of `ASM-0`–`ASM-3` and is
worth adopting.

**Coverage, as a checklist.** Mapping the source bank's topic distribution against our outcomes shows
where a quiz would naturally under-test:

| Source coverage area | Our outcome | Verdict |
|---|---|---|
| Field history, milestone models, terminology | — | **Skip.** Trivia. No `OUT-n.m` claims it and no client conversation needs it |
| Generative vs non-generative model families | `OUT-1.1` | **Test**, as triage: given an ask, which family |
| Tokens, tokenization, context | `OUT-2.1` | **Test**, as consequence: what happens to cost and reliability |
| Embeddings and similarity | `OUT-2.3` | **Test**, as design placement: where in a solution does this go |
| Attention and transformer internals | `OUT-2.1` | **Test lightly.** Basics needs "why it hallucinates," not architecture recall |
| Scaling, model families, training regimes | `OUT-2.5` | **Test** only through the prompt/RAG/fine-tune decision |
| Fine-tuning and parameter-efficient methods | `OUT-2.5` | **Test** as "what would you decline, and why" |
| Orchestration, RAG, agents, guardrails | `OUT-2.4`, `OUT-3.1`, `OUT-3.4` | **Test heavily.** This is the program's centre of gravity |
| Multimodal, diffusion, distributed training | — | **Skip at basics.** Advanced-tier candidates |

The distribution is the finding: **a bank built from a standard course would spend roughly half its items
on material our outcomes do not claim.** Coverage is a filter, not a template.

---

## 2. Two documented item-quality failures — the most valuable half of this file

`SRC-3` records two machine-generated items that were *wrong in ways that are easy to reproduce*. Both
belong in the build instructions for `GAP-6`.

### Failure 1 — More than one option is defensible

> *"Which of the following best represents artificial intelligence?"*
> (a) A machine that can think like a human ← marked correct
> (b) A computer program that solves problems
> (c) Any advanced technology
> (d) Software that uses data

Options (b) and (d) are also defensible. The item is unanswerable by anyone who knows the field *better*
than the item's author — which inverts the entire point of an assessment.

**Rule:** every distractor must be **defensibly wrong**, not merely less good. If you cannot write one
sentence explaining why a distractor is wrong, it is not a distractor.

### Failure 2 — Negation gets mishandled

An item asking which option is **NOT** an example of a category had its correct answer mislabeled, and
the item's own explanatory note contradicted the recorded key.

**Rule:** avoid `NOT` and `EXCEPT` stems. If a negative item is unavoidable, the negation is bold and
capitalized, and the key is verified by a second person against each option individually.

### Three more rules, from our own build history

- **Two conventions must not collide with the key.** `SI-18` and `LL-14`: if the true answer can be
  legitimately expressed two ways (percent vs fraction, two variance conventions), the item must
  disambiguate or accept both.
- **Test the grader with planted answers.** `SI-26(c)` and `LL-35`: write a deliberately good, a
  deliberately thin, and a deliberately wrong response, and confirm the grader sorts them correctly.
  Reading the key is not testing it.
- **Price the pass bar.** `SI-23` and `LL-19`: an 80% bar on a 20-question quiz fails a genuinely
  85%-capable participant more often than anyone expects. Compute the false-fail rate before locking the
  bar, and size the quiz to the bar you want.

---

## 3. Worked rewrites — definition item → VSP scenario item

The transformation to apply to any topic in §1's "test" rows. Three worked examples, ready to use.

### `ASM-1`, serving `OUT-1.3`

**Definitional (reject):** *"What does precision measure?"*

**Scenario (use):**
> A client's inspection model reviews finished panels. On a batch containing 100 genuinely defective
> panels, the model flags 80 panels, of which 60 are genuinely defective. Their quality lead says
> *"75% accurate is good enough for us."* What is the most useful next thing to say?
> (a) Agree — 75% is the model's precision and it meets their bar.
> (b) Point out that the model is missing 40% of defects, and ask what a missed defect costs versus a
>     wasted re-inspection. ✓
> (c) Recommend retraining until precision exceeds 90%.
> (d) Explain that accuracy is the wrong metric and propose measuring the area under the ROC curve.

Every distractor is defensibly wrong: (a) accepts a number without asking about the miss rate; (c)
optimizes the metric the client happened to name; (d) is technically fluent and commercially useless —
and it is the most tempting wrong answer for exactly the cohort being tested.

### `ASM-2`, serving `OUT-2.4` / `OUT-2.5`

**Definitional (reject):** *"What is retrieval-augmented generation?"*

**Scenario (use):**
> A prospect wants a question-answering assistant over 4,000 internal policy documents that are revised
> monthly. Which approach do you propose first, and on what grounds?
> (a) Fine-tune a model on the documents, because the knowledge is domain-specific.
> (b) Put the documents in the system prompt, because modern context windows are large.
> (c) Retrieval over the documents, because the knowledge is theirs and it changes — fine-tuning changes
>     behaviour, not knowledge. ✓
> (d) Retrieval plus fine-tuning together, to get both accuracy and domain style.

(d) is the strongest distractor and the one worth writing: it is not absurd, it is *premature*, and the
grading note should say so.

### `ASM-3`, serving `OUT-3.1` / `OUT-3.4`

**Definitional (reject):** *"Name three agentic design patterns."*

**Scenario (use):**
> A client wants a system that reads inbound supplier emails, extracts order changes, updates their
> system of record, and replies. In an architecture review, which is the strongest first question?
> (a) Which agent framework are we standardizing on?
> (b) Which of these four steps is irreversible, and what gates it? ✓
> (c) How many tokens will this consume per email?
> (d) Should this be one agent or several specialized agents?

(b) wins because writing to a system of record and sending a reply are irreversible, and everything about
the architecture follows from where that boundary sits (`SUP-4` §3, `SUP-6` §1). (c) and (d) are real
questions asked in the wrong order — which is precisely the judgment `OUT-3.4` claims.

---

## 4. Rubric shapes for the non-quiz halves

`ASM-1`, `ASM-2`, and `ASM-3` all pair a quiz with a live performance (mock pre-sales conversation,
whiteboard defense, mock client conversation). `SRC-1` runs an eleven-week course on three
deliverable shapes that are worth borrowing for the rubric language, because each one grades something a
multiple-choice item cannot reach:

| Shape | What it is | What it grades | Where it fits |
|---|---|---|---|
| **One paragraph plus evidence, due before the next session** | A short written claim with a screenshot, trace, or output attached | Whether they actually ran the thing, and whether they can say what they observed | Already the shape of most `MOD-2`/`MOD-3` homework — the rubric should say so explicitly |
| **Written proposal, then a short spoken defense** | One page — problem, method, data — followed by a timed presentation | Whether the problem is stated without jargon and the data claim is real | `ASM-1`'s mock pre-sales; `MOD-4`'s capstone proposal (`GAP-10`) |
| **Demonstration plus design explanation plus honest performance assessment** | Show it working, explain the design, state what it does badly | Whether they can be honest about their own system under observation | `ASM-3` artifact review; `MOD-4` graduation demo |

**The third row is the one to steal deliberately.** Grading "state what it does badly" as an explicit
rubric dimension converts `GOAL-4`'s honesty requirement from a value into a score. Suggested dimension
wording for the `ASM-3` conversation rubric:

> **Honest limitation** — names at least one thing the system does badly, unprompted, with evidence from
> their own traces or evaluation set, and states what they would do about it.

That dimension is gradeable, it is impossible to bluff, and it is the single closest proxy for
"client-ready" the program has.

---

## 5. Build order for `GAP-6`

Driven by the calendar, not by module order:

| Assessment | Needed | Items | Source of items |
|---|---|---|---|
| `ASM-0` | Fri 4 Sep 2026 | ~20, async, 30 min | Scenario rewrites against `OUT-0.1`–`OUT-0.4`; the `LSN-0.2`/`0.3`/`0.4` notebooks already contain graded drills whose numbers are pinned — mine those first, they are pre-verified |
| `ASM-1` | ~week of Oct 12–16 | ~15 scenario items + conversation rubric | §3's first pattern across `OUT-1.1`–`OUT-1.6`; `LSN-1.3`'s three report cards and `LSN-1.6`'s bank pre-check are near-ready item sources |
| `ASM-2` | ~week of Nov 23–27 | ~15 items + whiteboard rubric | §3's second pattern; `LSN-2.6`'s golden-eval homework supplies real per-participant evidence |
| `ASM-3` | ~week of Dec 7–11 | ~25 items across all modules + conversation rubric + artifact review | §3's third pattern; §4's third row for the rubric; retention samples drawn from `ASM-0`–`ASM-2` |

**Reuse note:** `module-3-agentic-systems.md` already names `notebooks/interview/` (the existing GenAI and
ML Engineer interview tests with answer keys) as an `ASM-3` seed. Those are VSP-authored, carry no
licensing constraint, and are already scenario-shaped — check them before writing anything new.

---

## How this lands

| Assessment | Where it goes | Change type | Cost |
|---|---|---|---|
| `GAP-6`, all four | Coverage map, five item-quality rules, three worked rewrites, and rubric dimension wording — the build starts from structure rather than a blank page | Input to an unbuilt gap | Reduces `GAP-6` build effort materially |
| `ASM-3` rubric | The "honest limitation" dimension is a concrete, gradeable expression of `GOAL-4` | Rubric proposal | Needs Curriculum Lead sign-off |
| `MOD-4` (`GAP-10`) | §4's rows two and three are the capstone proposal gate and demo rubric | Input to an unbuilt gap | Reduces `GAP-10` build effort |

## Proposals requiring a spec decision

**None outstanding — adopted 2026-08-11.** "Honest limitation" is now a named dimension in both module
specs: `ASM-1`'s pass bar ("names at least one thing the approach or model does badly, unprompted, with
evidence, and states what they would do about it") and `ASM-3`'s artifact review, which is graded as
demonstration + design explanation + honest performance assessment. Cost is zero — `GAP-6` is unbuilt, so
the rubrics get written with the dimension in them.
