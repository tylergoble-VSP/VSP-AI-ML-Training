---
name: SUP-1-project-qualification-gates
description: The ten questions that qualify an AI project, the three-stage go/no-go that governs it, and the "is this even a good task for AI" screen that comes before both.
serves: LSN-1.6, LSN-3.5, LSN-3.6, MOD-4
sources: SRC-3, SRC-4
---

# SUP-1 — Project Qualification Gates

**The problem this solves.** `LSN-1.6` teaches the data questions ("what data exists, how labeled, how
much, how fresh"). `LSN-3.5` teaches the production questions (observability, reliability, evals, KPIs,
cost). Neither currently teaches the question that comes *before* both: **should this project exist?**
Two of the donated courses converge on the same answer from opposite ends — one from a research-funding
tradition, one from a public-sector adoption tradition — and the convergence is the teachable thing.

This is the material a senior uses in the first thirty minutes of a discovery call.

---

## Screen 0 — Is this a good task for AI at all?

Four properties, from `SRC-3`. A task with none of them is a candidate for ordinary software, and saying
so is the fastest trust you will ever build with a client.

| Property | The tell | Commercial example |
|---|---|---|
| **Hard for people, so automation pays** | The client is paying skilled hours for something mechanical | Reading 4,000 supplier invoices a month to extract line items |
| **Only a few people can do it** | There is one person who "just knows," and they are a bus factor | The one estimator who can price a nonstandard job |
| **Too many inputs for a person to hold** | The client describes a decision made "on feel" from a dozen signals | Which of 900 open leads to call today |
| **Hard, but with well-defined right answers** | You can write down what correct looks like before you build | Classifying support tickets into an existing taxonomy |

**The inversion is the useful half.** A task that is *easy* for people, done by *many* people, on *few*
inputs, with *contested* right answers is where AI projects go to die. Name that out loud in the room.

**Drill (5 min, live-able in `LSN-1.6` segment 1 or `LSN-3.6`):** give the group three asks — one strong,
one weak, one genuinely ambiguous — and have them score against the four properties before anyone
mentions a model. The ambiguous one is the point.

---

## Screen 1 — The ten qualification questions

From `SRC-4`, originally a research-proposal checklist and still the sharpest one in circulation. It is
short enough to memorize, which is why it beats a 40-row discovery template.

1. **What are you trying to do?** State the objective with no jargon whatsoever.
2. **How is it done today, and what are the limits of current practice?**
3. **What is new in your approach, and why do you think it will succeed?**
4. **Who cares?** If you succeed, what difference does it make?
5. **What are the risks?**
6. **How much will it cost?**
7. **How long will it take?**
8. **What are the mid-point and final checks for success?**
9. **How will you measure the difference you claimed in (4)?**
10. **What happens if it does not work?**

**Why this belongs in pre-sales, not just project setup.** Questions 1, 2, and 4 are *client* questions —
they interrogate the ask. Questions 5–8 are *proposal* questions — they price it. Question 3 is the one
VSP answers. Question 9 is the one that most often has no answer, and finding that out in discovery
rather than in month three is worth the whole conversation.

**Question 1 is a stress test, not an icebreaker.** "Articulate your objective using absolutely no
jargon" fails loudly and usefully. A client who cannot say what they want without the words "AI-powered,"
"intelligent," or "leveraging" does not yet have a project. That is not a reason to walk away — it is the
first work package.

### How it composes with the existing `LSN-1.6` bank

The `LSN-1.6` question bank asks *what data exists*. These ten ask *why we are doing this*. They stack:

| Layer | Question bank | Owner |
|---|---|---|
| Should it exist? | The ten questions (this file) | Senior / TL in discovery |
| Can it be built? | `LSN-1.6` data reality checklist — exists / labeled / enough / fresh / legal | Senior / TL in discovery |
| Will it survive? | `LSN-3.5` production question bank — observability, reliability, evals, KPIs, cost | TL in architecture review |

Three banks, one conversation, in that order. That ordering is itself a teachable artifact — put it on
one page and it becomes the pre-sales kit's cover sheet.

---

## Screen 2 — The three-stage go/no-go

From `SRC-3`, adapted from a public-sector AI adoption checklist. The structural idea is the valuable
part: **three gates, and you do not pass one until the previous one is fully answered.** Most failed AI
projects passed straight from "interesting idea" to "building."

### Gate A — Planning (do not build until all five are answered)

| # | Question | What a bad answer sounds like |
|---|---|---|
| A1 | Is the task defined, with quantitative metrics and a benchmark to beat? | "We'll know it when we see it" |
| A2 | Who owns the candidate data, where did it come from, and is it relevant to *this* task? | "IT can probably pull something" |
| A3 | Who are the end users, the stakeholders, and the person accountable for outcomes? | Three names, no accountable one |
| A4 | What harm does a wrong answer cause, how likely, how large? | "It's only a recommendation" |
| A5 | How do you roll the system back, and how would you even notice it had gone wrong? | Silence |

### Gate B — Development (do not deploy until all five are answered)

| # | Question |
|---|---|
| B1 | How are intentional or accidental manipulations of the input data or the model's outputs addressed? (see `SUP-7`) |
| B2 | What is the procedure when the system is wrong, and who gets told? |
| B3 | Which named people hold which roles once this is live? |
| B4 | How is output correctness verified — by whom, on what sample, how often? |
| B5 | What is auditable after the fact, and for how long is it retained? |

### Gate C — Deployment (three activities that run *simultaneously*, forever)

- **Continuous task and data validation** — the world drifts; the training data does not.
- **Functional testing** — the software half is still software.
- **Harm assessment and quality control** — the thing that is nobody's job by default.

### The three lessons that source states plainly, and we should quote as our own

1. **Metrics for success are the whole ballgame.** No metric, no project.
2. **The technology must match the task** — not the other way around, which is how a client ends up with
   an agent where a filter would have done.
3. **Expectations are set in advance or they are set by disappointment.** This is `LSN-2.6`'s thesis,
   arriving from an adoption perspective rather than a limitations perspective — worth naming as the same
   idea seen twice.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-1.6` | Segment 1's "data reality checklist" gains the three-layer cover sheet (should it exist / can it be built / will it survive); Screen 0's four-property drill is a candidate swap for a homework task, not an addition | Additive to the bank; no re-timing | Builder writes one page |
| `LSN-3.5` | Gates A/B/C become the *structure* of the `GAP-4` TL question bank — the six production dimensions are Gate C, and Gates A/B are what a TL asks *before* the architecture review | Structural input to an unbuilt gap | Reduces `GAP-4` build effort |
| `LSN-3.6` | The ten questions applied live to a real case is a ready-made segment shape if any case walkthrough runs short | Reserve material | None |
| `MOD-4` capstone | Gate A is the natural shape for the capstone project proposal, and Gate C for the graduation demo's "what would it take to run this for real" question | Input to `GAP-10` | Reduces `GAP-10` build effort |

**Nothing here changes a contract.** All four placements are bank additions, structural inputs to
unbuilt material, or reserve segments.

## Proposals requiring a spec decision

None. This supplement fits inside existing outcomes (`OUT-1.6`, `OUT-3.4`, `OUT-3.5`).
