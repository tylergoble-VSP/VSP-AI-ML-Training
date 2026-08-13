---
name: SUP-6-agentic-patterns-and-limits
description: The workflow-to-agent continuum, five design patterns with their maturity ratings, the anatomy of a tool, the four ways agents execute harmful actions, and an explicit when-not-to-use list.
serves: LSN-3.1, LSN-3.2, LSN-3.4, LSN-3.5
sources: SRC-1, SRC-2
---

# SUP-6 — Agentic Design Patterns and Their Limits

**The problem this solves.** `MOD-3` is the module the program exists for, and three of its six lessons
are unbuilt (`GAP-2`, `GAP-3`, `GAP-4`). Two independent courses in the donated corpus converge on the
same pattern vocabulary and — more usefully — on the same *reservations*. The reservations are the part
that makes a senior sound credible rather than enthusiastic, and they are what `OUT-3.1` and `OUT-3.4`
actually require.

`SUP-4` gives the architecture ladder that outlives frameworks. This file gives the current-generation
patterns and their sharp edges.

---

## 1. The continuum, and why it is the whole lesson

There are not two categories. There is one axis, and where a system sits on it is an **engineering
decision you defend**, not a label you apply.

| | Workflow | Agent |
|---|---|---|
| Who decides the next step | Your code, along predefined paths | The model, dynamically |
| Where the exit condition lives | In the code — known, enumerable | With the model — it decides when it is done |
| Predictability | High | Lower, by construction |
| Debuggability | Ordinary software debugging | Trace reading |

Both ends can use tools. Both ends can be augmented with retrieval. **An agent can be one step inside a
workflow**, which is usually the right architecture and almost never the one that gets pitched.

**The sentence to teach:** *maximum autonomy is not the goal — the goal is the least autonomy that solves
the problem.* Every additional degree of freedom is paid for in predictability, cost, and debugging time.

This is also the honest answer to a client who says "we want agents": *"which decisions do you want the
system to make on its own, and which do you want in your code? That answer sets the architecture."*

### The four traits, for classifying anything a vendor demos

Autonomy · understanding of its environment · ability to take actions · ability to remember. Score a
demo against these four and the marketing evaporates. Note that these are the same four elements as
`SUP-4`'s definition — percepts, effectors, autonomy, and state — which is the point: **the vocabulary
changed, the structure did not.**

---

## 2. The five patterns

Ordered by maturity, which is also roughly the order in which you should reach for them.

### Pattern 1 — Workflows (most mature)
Three named shapes, all fully deterministic in control flow:
- **Prompt chaining** — each step consumes the previous step's output. Use when the task decomposes
  cleanly and the decomposition is stable.
- **Parallelization** — independent subtasks run at once, results merged by code. Use when subtasks are
  known in advance and do not depend on each other.
- **Routing** — classify the input, dispatch to a specialist path. Use when different input kinds need
  genuinely different handling, and mixing them degrades all of them.

**Every one of these has a defined exit.** That is what makes them the default.

### Pattern 2 — Reflection
The system examines its own output and produces a critique, then revises. This is the automation of
something you already do by hand: get a bad answer, tell it what is wrong, get a better one.

- **Maturity: high.** Quick to implement, reliably helpful, composes with every other pattern.
- **Best on:** code generation, structured reasoning, anything with a checkable form.
- **Cost:** at least doubles token spend per task. Say that out loud in a cost conversation.

### Pattern 3 — Tool use
The model is given functions it can call to gather information, take action, or manipulate data.

- **Maturity: high**, and it is more predictable than the two patterns below because the action space is
  enumerated by you.
- **Best on:** anything RAG alone cannot do — live lookups, calculations, writes to a system.
- **The design skill is picking the right tools**, not adding more. A large tool list degrades selection.

### Pattern 4 — Planning
The model produces a multi-step plan and executes it.

- **Maturity: moderate. Explicitly less predictable.**
- **Best on:** open-ended work — drafting options for a decision, research assistance, exploratory
  analysis.
- **The honest warning:** more agency means it will plan things in ways that surprise you. That is
  simultaneously the feature and the risk.

### Pattern 5 — Multi-agent
Several agents with distinct roles split the work and communicate.

- **Maturity: lowest. Highest complexity. Least predictable.** And it does work.
- **Best on:** genuinely multi-role problems where subtasks are discovered rather than known —
  software development, design exploration, simulation.
- **Cost:** superlinear. Every agent is a full model context.
- **The reservation to state plainly:** most problems pitched as multi-agent are a workflow with three
  routing branches, and the workflow is cheaper, faster, and debuggable.

---

## 3. Anatomy of a tool (the `LSN-3.4` lab's core object)

A tool is a function wrapped in the metadata a model needs to decide whether and how to call it:

1. **Name**
2. **Description of what it does** — this is what the model reads to decide. It is prompt engineering, not
   documentation. Most "the agent won't use my tool" bugs are here.
3. **A schema for the inputs** — types and required fields.
4. **The function itself.**

**Two things worth teaching in the lab:**

- **Failures partition cleanly.** Did the model fail to *select* the tool (a description problem), fail
  to *construct valid arguments* (a schema problem), or did the tool itself *fail* (an ordinary software
  problem)? Three different fixes. This is the classification for `LSN-3.4` segment 4's break-it drill
  and a ready-made rubric for the trace-annotation homework.
- **Actions can be expressed as code rather than as structured calls**, and there is real evidence this
  works better for some problems — because code is composable, verifiable by running it, and testable.
  It is also the pattern that most demands sandboxing (see §5). Basics-level takeaway: know the option
  exists and know it raises the security bar.

### Tool protocols — the standardization layer

There is now a standard for how models connect to tools and data sources — a host/client/server
separation, so a tool built once works with any compliant system instead of being wired per-framework.

- **Why it matters commercially:** it decouples tool investment from framework choice. A client's
  integration work stops being a bet on a library.
- **The reservations, stated as they should be to a client:** authentication is the immature part,
  security posture is evolving, multi-tenant scaling is unsettled, and the standard is still moving.

That is exactly the shape of a `LSN-3.3` cloud-rubric row and a `LSN-3.2` framework-card row: *does this
speak the standard protocol, or does it want its own?*

---

## 4. The failure modes — six, and they are what `LSN-3.5` is for

1. **Spiralling** — the loop does not terminate, or terminates only after burning a budget. The mitigation
   is boring and mandatory: hard turn limits. (`LSN-3.4` Stage B already builds this.)
2. **Debugging difficulty** — a failure is a trace, not a stack. The system's behaviour is not
   reproducible by re-running it.
3. **Validation difficulty** — "is it working?" has no single answer, which is why offline eval suites
   exist.
4. **Unexpected behaviour** — the plan was legal, sensible, and wrong.
5. **Cost** — nondeterministic token spend per task. A cost per task is a *distribution*, not a number,
   and quoting the mean without the tail is how a project blows its budget. This is `LSN-0.4`
   (stochastic) arriving in a finance conversation.
6. **Unsafe execution** — see below.

---

## 5. The four ways an agent executes something harmful

Worth teaching as a discrete list because it is the security content `LSN-2.6` promises at awareness
level and `LSN-3.5` needs at architecture level:

| Route | Mechanism | Likelihood |
|---|---|---|
| **Plain model error** | It generates a damaging command while genuinely trying to help | Low but observed |
| **Compromised model supply chain** | The model weights or serving stack are untrusted | Very low with known models on controlled infrastructure — but not zero, and it is a real procurement question |
| **Indirect prompt injection** | The agent reads content — a web page, a document, an email, a retrieved chunk — that contains instructions, and follows them | **The one that matters.** It is not exotic; it is the default consequence of letting an agent read untrusted text |
| **Exposed agent abuse** | A publicly reachable agent is fed adversarial input by someone who wants it to misbehave | Proportional to exposure |

Once harmful code runs, the blast radius is the file system, cloud resources, API spend, and network
position. **Which is the argument for sandboxing, least-privilege tool design, and a human gate on
irreversible actions** — the same three controls `LSN-3.1` segment 2 introduces as "the harness," now with
a threat model attached rather than asserted.

**Note the composition with `SUP-5`:** a RAG pipeline retrieves text and puts it in the context. An agent
with tools acts on its context. Chain them and **your retrieval corpus becomes an injection surface**.
That is a genuinely sharp point for `LSN-3.6`'s case walkthroughs and for the `MOD-4` capstone, where
lead data is external text.

---

## 6. Guardrails — the control layer

Rules and checks that constrain what the system may say and do. Five types, useful as a checklist rather
than a taxonomy:

- **Content** — blocks harmful, discriminatory, or off-brand output.
- **Compliance** — enforces regulatory constraints for the client's sector.
- **Topical** — keeps the conversation inside scope.
- **Security** — resists manipulation and instruction injection.
- **Adaptive** — updated as policy changes, because policy always changes.

Two implementation shapes exist: a **rules-and-flows layer** that sits between the user and the model and
enforces conversation policy, and a **classifier model** that screens inputs and outputs against a risk
taxonomy. Both are real products; the pattern is what matters at basics level.

**The client-facing framing:** guardrails are how you answer *"what stops it from saying something
terrible to our customer?"* with an architecture instead of a reassurance.

---

## 7. The when-not-to list

The most valuable half-slide in the corpus, and directly the `OUT-3.1` judgment call.

| ✅ Reach for an agentic system when | ⛔ Do not when |
|---|---|
| The task is genuinely complex and does not decompose in advance | A simpler approach already does it — a filter, a query, a workflow |
| The environment is dynamic and the right steps vary per case | Cost is tightly bounded |
| Adaptability is a requirement, not a preference | Stability is a hard requirement |
| Simpler approaches have been tried and measurably fall short | Predictability is what the client is buying |

Plus the six operating principles, which double as the `LSN-3.4` lab's design rules:

1. **Start simple** — build the workflow first; prove it is insufficient.
2. **Mix and match** — a reflection step inside a routed workflow is often the whole answer.
3. **Understand what the agent is doing** — if you cannot read the trace, you do not have a system.
4. **Limit your loops** — always.
5. **Optimize model choice per step** — not every step needs the largest model, and this is where cost
   control actually lives.
6. **Do not forget the earlier techniques** — a better prompt or better retrieval beats an agent, often.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-3.1` segment 3 | The when-not-to table is the scoring rubric for the workflow-vs-agent drill; the continuum framing replaces the binary. Composes with `SUP-4`'s five-property diagnostic — properties diagnose, this table decides | Rubric for an existing drill — **no minute changes** | Deck edit |
| `LSN-3.1` segment 2 | §5's four routes give "the harness" a threat model, turning three asserted controls into three derived ones | Sharpen an existing segment | Deck edit |
| `LSN-3.2` | The five patterns with maturity ratings, and "does it speak the standard tool protocol," are two strong card rows for the `GAP-2` framework cards. The pattern set is also the honest answer to "why do these frameworks all look the same?" — they implement the same five patterns | Input to `GAP-2` | Reduces `GAP-2` build effort |
| `LSN-3.4` | §3's three-way tool-failure partition (selection / arguments / execution) is a ready-made classification rubric for segment 4's break-it drill and for the Stage-C eval check | Rubric for existing drills | Notebook edit |
| `LSN-3.5` | §4's six failure modes and §6's guardrail checklist map onto the six production dimensions; the cost-as-a-distribution point sharpens the cost segment's worked example | Input to `GAP-4` | Reduces `GAP-4` build effort |
| `LSN-3.6` / `MOD-4` | The retrieval-corpus-as-injection-surface point is a live architecture question for any case involving external text | Case-walkthrough material | None |

## Proposals requiring a spec decision

None. `OUT-3.1`, `OUT-3.2`, and `OUT-3.4` cover all of it. Note that §5's supply-chain and exposure routes
brush against security-architecture depth that belongs in the advanced tier — hold the basics treatment
to the four-route awareness list and the three controls.
