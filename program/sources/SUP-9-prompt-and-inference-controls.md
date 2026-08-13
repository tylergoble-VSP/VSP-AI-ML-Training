---
name: SUP-9-prompt-and-inference-controls
description: The inference knobs a client will ask about, a prompt component checklist, the six prompting techniques ranked by when to reach for them, and the escalation drill that shows why prompt iteration is engineering.
serves: LSN-2.1, LSN-2.2, LSN-2.6
sources: SRC-1, SRC-2
---

# SUP-9 — Prompt and Inference Controls

**The problem this solves.** `LSN-2.2` teaches prompting as engineering and its material exists
(structured outputs, chain-of-thought, the failure gallery). What the corpus adds is the layer around it
that participants will be asked about in their first client conversation and that the lesson does not
currently name: **the inference settings**, a **checklist for what a prompt is made of**, and a technique
ladder with a "reach for this when" column rather than a list of names.

---

## 1. The inference knobs

Six settings, applied roughly in this order at generation time. A senior should be able to say what each
does in one sentence — clients ask, and "I'd have to check" is a bad answer to a question this basic.

| Setting | What it does | When it comes up |
|---|---|---|
| **Temperature** | How random the choice among likely next words is. Low = repeatable and flat; high = varied and prone to wandering | "Why does it give a different answer each time?" (`LSN-0.4` callback — this is the knob) |
| **Top-k** | Only ever choose among the *k* most likely next words | Cheap way to stop the tail from producing nonsense |
| **Top-p** | Only choose among the most likely words that together account for *p* of the probability | The usual default; adapts to how confident the model is at each step |
| **Frequency penalty** | Discourages words already used a lot | Repetition loops |
| **Presence penalty** | Encourages introducing new topics | Output that will not move on |
| **Maximum tokens** | Hard cap on output length | Cost control; also the cause of mysteriously truncated JSON |

**The demonstration worth running (2 min, live).** Take one stem — *"The wind was…"* — and generate at
temperature 0.3 versus 1.8, then at top-p 0.7 versus 1.0 with top-k held fixed. The room sees
non-determinism become a dial rather than a mystery.

**The commercially load-bearing point:** temperature zero is *more repeatable*, not deterministic — batching,
hardware, and model updates still move outputs. `LSN-0.4`'s three buckets already teach why that
distinction matters in a contract; this is where it becomes a settings conversation.

---

## 2. What a prompt is made of

Two checklists — one for ordinary prompts, one for prompts that carry weight:

- **Simple:** role · context · format · task.
- **Full:** role · tone · actions · constraints · format · examples · context · task · output indicators.

Three drafting principles from `SRC-1`, all of which survive contact with reality: **be clear, relevant,
and consistent**; **use an organized structure** rather than a paragraph; **prefer simplicity** and add
complexity only when a failure demands it.

The do-list, worth putting on a slide verbatim because every item is a correction of a real habit:

- Check the output for accuracy — the model is not the reviewer.
- Be specific rather than clever.
- Put context *in the instruction*, not in a follow-up message.
- **Start simple and iterate to complex** — not the other way around.
- Break complex tasks into explicit steps.
- Read prompts that work and test them yourself.

### Two mechanisms that silently change behaviour

- **Chat templates** — how a conversation is formatted before it reaches the model.
- **Prompt templates** — how your variables are assembled into the final string.

Neither is visible in a playground, and both change results. **Knowing whether a template is being
applied is a debugging skill**, and it is a good candidate for the `LSN-2.2` failure gallery: the same
prompt through two paths, two outputs, one cause.

---

## 3. The escalation drill

`SRC-1` runs an exercise that does more for "prompting is engineering" than any slide: **one question,
escalated one change at a time, with the output re-read at every step.** Re-cast onto a subject this room
owns:

1. `"Delivery risk is…"` — bare, ambiguous, and it will answer something
2. `"For a fixed-price software project, delivery risk is…"` — add context
3. `"Concisely define delivery risk for a fixed-price software project."` — make it an instruction, and
   constrain the length
4. `"Concisely define delivery risk for a fixed-price software project. Answer in JSON."` — constrain the
   format
5. `"…Answer in JSON. Only provide the JSON."` — constrain the format *and forbid the preamble*
6. `"You are a delivery manager writing for a client steering committee. …"` — add a role

**Why it works:** each step changes exactly one thing, and each step's effect is visible in the output.
Step 5 lands hardest — *"only provide the JSON"* is the difference between output you can parse and output
you have to clean, and it is a single clause. That is the whole thesis of `LSN-2.2`'s structured-output
segment, demonstrated in ninety seconds. Step 6 usually changes the *register* more than the content,
which is its own lesson about what a role prompt buys you.

This is a **candidate replacement for the existing pre-work task "run the 5 provided prompts and note the
surprises"** — same 30-minute budget, but the five prompts now form a controlled sequence instead of five
independent samples, so the write-up has a shape.

---

## 4. The technique ladder

Six techniques with the trigger that should make you reach for each. The trigger column is the part that
converts a list into judgment.

| Technique | What it is | Reach for it when | Cost |
|---|---|---|---|
| **Zero-shot** | Just ask | Always start here | 1 call |
| **Few-shot** | Include 2–5 worked examples in the prompt | Output *format* or *style* is inconsistent | 1 call, longer prompt |
| **Chain-of-thought** | Ask it to work through the steps | The task needs multi-step reasoning and it is skipping to an answer | 1 call, longer output |
| **Self-consistency** | Generate several independent answers, take the most common | The answer varies run to run and you need reliability | *n* calls — the expensive one |
| **Generated knowledge** | Have it write the arguments on each side first, then answer | Judgment calls where it anchors on the first framing | 1–2 calls |
| **Plan-and-solve** | Have it state constraints and a plan, then execute the plan | Structured problems with interacting constraints | 1–2 calls |

**Two composites worth naming** because they are the bridge into `MOD-3`: interleaving **reasoning with
tool calls** in a loop is what makes an agent an agent (`SUP-6`), and having the model **write code as its
reasoning step** and executing it offloads arithmetic to something that cannot get arithmetic wrong.

### The cost column is the teaching point

Self-consistency multiplies token spend by *n*. Chain-of-thought lengthens every output. These are not
free quality — they are purchased quality, and a senior who can say *"we can raise reliability roughly
threefold in cost by voting across runs"* is doing `LSN-2.5`'s job one lesson early. `LSN-2.2`'s pre-work
already includes a five-run self-consistency mini-experiment; attaching the cost multiplier to it turns
an experiment into a commercial fact.

---

## 5. Why prompt work is the right first move, commercially

Six reasons a client can follow, and they double as the opening of the `LSN-2.5` decision framework:

1. It improves the model's performance on the task.
2. It is fast and cheap relative to every alternative.
3. It transfers approximately across models, so it is not a lock-in bet.
4. It needs no training data.
5. It is transparent — the change is legible in the prompt.
6. It preserves the model's general capability, which fine-tuning can erode.

**And the three triggers to stop iterating and change approach:** you are not getting the results and
more prompting is not moving them; you need *reliable* output rather than usually-good output; the
instructions have grown so complex that nobody can read the prompt. Each is a doorway to a different
answer — retrieval, structure, or a different decomposition — which is exactly `LSN-2.5`'s decision.

---

## 6. Evaluating prompts, not just models

Three distinctions worth having before `LSN-2.6`'s eval homework:

- **What is being evaluated — the model, or the system?** A prompt change, a retrieval change, and a
  model change all move the same end-to-end number. Without isolation you cannot attribute an
  improvement, which is the argument for the `LSN-3.5` eval-regression homework.
- **Evaluation mode:** zero-shot, few-shot, or fine-tuned. A benchmark number without its mode is
  meaningless.
- **Method:** human versus automated, and direct scoring versus comparing two outputs head to head.
  Head-to-head comparison is markedly easier to do consistently, by people *and* by models.

Standard evaluation harnesses exist and are worth naming as a category — the point for basics is that
**running a defined question set against a fixed configuration is a normal, tooled activity**, not an
exotic one. That framing is what makes `LSN-2.6`'s 20-question golden set feel like standard practice
rather than homework invented for the course.

For the benchmark and leaderboard caveats that belong alongside this, see `SUP-3` §7.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-2.2` pre-work | §3's escalation sequence is a **candidate replacement** for the "run the 5 provided prompts" task — same 30 min, controlled sequence, better write-up | Swap within an existing task | Notebook edit |
| `LSN-2.2` segment 1 | §2's component checklists give "anatomy of a prompt" a concrete artifact participants keep | Sharpen an existing segment — **no minute changes** | Deck edit |
| `LSN-2.2` segment 4 | The chat-template/prompt-template invisibility is a strong failure-gallery entry with a diagnosable cause | Gallery addition | Small |
| `LSN-2.2` homework | Attaching §4's cost column to the existing self-consistency experiment turns it into a cost/reliability trade | Framing note | None |
| `LSN-2.1` | §1's six settings are the concrete face of "inference and why it costs money" in segment 2; the temperature demo is the cleanest available non-determinism illustration | Demo material | Small |
| `LSN-2.5` | §5's six reasons and three stop-triggers are the framework's opening panel — prompt-first is a *defensible* default, not a lazy one | Input to the decision one-pager | Reduces build effort |
| `LSN-2.6` | §6's three distinctions frame the golden-eval homework as standard practice | Input to `GAP-7` | Small |

## Proposals requiring a spec decision

**None outstanding — adopted 2026-08-11.** The six-step escalation ladder is now part of `LSN-2.2`
pre-work task 1, inside its existing 25 minutes, with one line per step in task 2 ("what did this change
buy?"). It sits alongside P1–P5 rather than replacing them: the five independent prompts show *that*
prompts differ, the ladder shows *which change bought what*. Cost is zero — `LSN-2.2`'s materials are
unbuilt.
