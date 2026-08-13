---
name: SUP-4-agent-architecture-ladder
description: Four agent designs from simplest to most capable, the five environment properties that force you up the ladder, and why this pre-LLM framing is the sharpest available answer to "what is an agent."
serves: LSN-3.1, LSN-3.2
sources: SRC-5
---

# SUP-4 — The Agent Architecture Ladder

**The problem this solves.** `LSN-3.1` opens by demanding precision about the word "agent," and the
industry supplies four incompatible definitions — "autonomous bots," "systems that intelligently
accomplish tasks," "programs where model outputs control the workflow," "AI employees." All four are
marketing. `SRC-5` supplies a framing that is thirty years older than any of them, still correct, and
completely free of framework churn: **an agent is defined by its loop and its environment, not by what is
inside it.**

Teach this and a participant can classify any system a vendor shows them — including ones built with
libraries that will not exist in two years.

---

## 1. The definition that does not expire

An agent is an autonomous program that:

- **perceives** an environment through sensors (for software: files, APIs, message queues, a database, a
  user's message),
- **acts** on that environment through effectors (for software: writes, API calls, sent messages, a
  screen),
- does **all its computation between the two, itself** — that is what "autonomous" means, and
- is judged by an explicit **performance measure**.

Three terms worth having:

- A **percept** is one observation. The **percept sequence** is everything it has observed so far — which
  is exactly what an LLM agent's context window holds, and naming it that way makes context-window limits
  feel like a design constraint rather than a quirk.
- A **rational agent** acts to maximize its expected performance *given what it can actually perceive*.
  Not what is true — what it can see. This is the cleanest available explanation of why an agent
  confidently does the wrong thing.
- A **performance measure** should ideally depend only on things the agent can observe, and frequently
  does not. That gap is where most disappointment lives.

### The worked example (keep it; it is perfect and carries no domain baggage)

A cleaning robot on a grid.

| Element | Value |
|---|---|
| Sensors | bump, dirt-present, at-home |
| Effectors | forward, turn right, turn left, suck, power off |
| Environment | a grid with walls, dirt, and a home square |
| Performance measure | each unit of dirt collected **+100**; each action taken **−1**; powering off anywhere but home **−1000** |

**Two questions that do a whole segment's work:**

1. Given the actions `forward, suck, forward, suck, forward, suck, power off`, what is the score? (Score
   it live. The −1000 is the point: the agent optimized the obvious term and lost on the term nobody
   emphasized.)
2. We want it to collect all dirt, return to its exact starting position and orientation, and shut down.
   **Can a purely reactive agent do this? Why not?**

Question 2 is the entire ladder in one prompt. The answer — it cannot, because "return to where you
started" requires remembering where you started — is what forces you up a rung.

**Why this belongs in an LLM-era lesson:** the performance measure with a hidden catastrophic term is the
exact shape of every agent-cost and agent-safety incident. It is the reward-farming beat from `LSN-1.5`,
one module later, now attached to a system that takes real actions.

---

## 2. The four rungs

### Rung 1 — Reflex agent
Sees the world now, applies condition–action rules, acts. No memory.

- **Pro:** almost no compute; usable where latency is the binding constraint; trivial to implement and to
  reason about.
- **Con:** cannot generally reach optimal behavior. Anything requiring "what did I already do?" is out.
- **LLM-era equivalent:** a single prompt-and-respond call. Also: a classifier-and-route rule.

### Rung 2 — Model-based reflex agent
Adds **state**: an internal model of how the world evolves and what its own actions do, so it can
maintain a picture of the world it cannot fully see right now.

- **Pro:** can reach optimal behavior in environments that are not fighting back; rules remain a natural
  way to express the logic.
- **Con:** hard to retarget — the rules encode the tasks that were anticipated at design time.
- **LLM-era equivalent:** a workflow with conversation memory and accumulated scratch state.

### Rung 3 — Goal-based agent
Adds an **explicit goal**, and chooses actions by asking what the world will look like if it acts.

- **Pro:** retargeting is changing the goal, not rewriting the rules — this is the rung where "tell it
  what you want" becomes possible; if the goal is specific enough you can reason backwards from it.
- **Con:** cannot optimize an arbitrary performance measure — a goal is binary, reached or not.
- **LLM-era equivalent:** the planning pattern (see `SUP-6`) — decompose the goal, execute, check.

### Rung 4 — Utility-based agent
Adds a **utility function**: not just "is this a goal state" but "how good is this state," so it can
trade off, hedge, and rank partial successes.

- **Pro:** the only rung that can optimize an arbitrary performance measure; a goal-based agent is just a
  utility agent whose utility is 1 at the goal and 0 elsewhere.
- **Con:** the most computation; the hardest to build; and **it cannot reason backwards**, because there
  is no single target state to reason back from.
- **LLM-era equivalent:** scored, ranked, or evaluated action selection — including a model-as-judge
  choosing among candidate actions. Directly relevant to the `MOD-4` capstone, which *is* a scoring
  problem.

### The decision this ladder actually delivers

`LSN-3.1`'s live drill is "workflow vs agent — pick and defend." The ladder upgrades that binary into a
four-way with a stated cost per rung, and gives the defense a shape:

> *"Rung 2, because the task needs memory of what it already tried, but the success condition is fixed
> and checkable — nothing here needs the system to weigh partial successes against each other."*

That sentence is what "client-ready" sounds like for `OUT-3.1`.

---

## 3. The five environment properties that force you up the ladder

This is the diagnostic half, and it is the more valuable half for pre-sales. You do not choose a rung by
preference; the client's environment chooses it for you.

| Property | Meaning | What it forces | Commercial tell |
|---|---|---|---|
| **Partially observable** | You cannot sense every relevant variable at every moment | State estimation — you must *infer* what you cannot see (rung 2+) | "The system doesn't know whether the customer already replied" |
| **Nondeterministic** | The same action does not always produce the same result | Reasoning over multiple possible outcomes | Any external API, any human in the loop, any model with temperature above zero |
| **Dynamic** | The world changes while the agent is deciding | React fast where time matters, think deep only where it pays | Prices, inventory, a queue that keeps filling |
| **Continuous** | State or actions are best described by real numbers, not a finite list | You cannot enumerate the options; you need scoring or search | "Set the discount" rather than "approve or reject" |
| **Non-episodic** | This action affects the next situation | Long-horizon consequences must be weighed now | Anything that sends an email, writes to a system of record, or spends money |

**The insight worth putting on a slide:** *partial observability and nondeterminism look identical from
inside the agent.* An agent that cannot see a variable and an agent facing a coin flip both face
uncertainty they cannot resolve. That equivalence explains why "just give it more tools" and "just make
it more deterministic" are the same fix wearing two hats.

### The diagnostic drill

Give a client ask and score it against the five properties before naming a single framework:

> *"Route incoming support email to the right team and draft a first reply."*
> Partially observable (you cannot see the customer's actual intent) · nondeterministic (the model's
> draft varies) · mildly dynamic (queue depth changes) · discrete actions (a fixed team list, so not
> continuous) · **episodic for routing, non-episodic the moment it sends.**

The last clause is the finding: routing is a rung-1 problem, and sending is not. **The architecture
boundary falls exactly where the irreversible action begins** — which is the argument for the
human-in-the-loop gate in `LSN-3.1` segment 2, arrived at by analysis rather than by assertion.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-3.1` segment 1 | The four-part definition (percepts, effectors, autonomy, performance measure) is a sharper spine for "goal, loop, tools, memory, stop condition" — same content, provenance that outlives frameworks. The cleaning-robot scoring question is a 3-min opener that lands the performance-measure trap | Sharpen an existing segment — **no minute changes** | Deck edit |
| `LSN-3.1` segment 3 | The five-property diagnostic gives the workflow-vs-agent drill an explicit rubric, so the defense is scoreable rather than a matter of taste | Rubric for an existing drill; also a homework-memo rubric | Small |
| `LSN-3.1` homework | The two relocated drill scenarios (D2/D4) become far more gradeable with the property table attached | Grading aid | None |
| `LSN-3.2` | "Which rung does this framework assume you are on?" is a genuinely discriminating axis for the framework cards — better than feature lists, and it ages well | Input to `GAP-2` card structure | Reduces `GAP-2` build effort |

## Proposals requiring a spec decision

None. `OUT-3.1` ("explain what an agent is… and judge when an agent beats a plain workflow") is exactly
this material. The ladder replaces nothing in the contract; it gives the existing drill a rubric.
