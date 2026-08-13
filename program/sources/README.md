# sources/ — External Course Corpus → Program Supplements

A graduate-level AI/ML course corpus was donated to the program (see the `SRC-n` catalog below). This
directory is where that corpus is **processed into the program**, under the same discipline as everything
else in `program/`: nothing is dropped into a lesson raw, everything carries an ID, and every supplement
names the `LSN-n.m` it serves.

## What a supplement is (and is not)

A `SUP-n` file is **build-ready raw material for an existing lesson or gap** — a checklist, a decision
ladder, a drill bank, a failure catalog. It is the thing a builder or lesson owner reads *before* writing
a deck, notebook, or question bank.

| A supplement **is** | A supplement **is not** |
|---|---|
| Concepts, checklists, and drills extracted and re-cast into VSP's commercial context | A lecture to deliver as-is |
| Attached to `LSN-n.m` by ID, with an explicit "how this lands" note | A new lesson (a new lesson requires a module-spec change first) |
| Sized so it fits the existing contract — a bank to draw from, an option to swap in | A reason to re-time a 60-min session or grow a homework budget |
| Honest about what it costs to use (licensing, build effort) | A closed `GAP-n` |

**Supplements do not close gaps.** `GAP-2`/`3`/`4`/`5`/`6`/`7`/`9` stay open with their owners and dates.
What supplements do is shorten the build: `GAP-4`'s question bank, `GAP-6`'s item bank, and `GAP-7`'s
failure pack each now start from drafted material instead of a blank page.

## The four rules this directory runs on

1. **No jargon from the source domain.** The corpus comes from a defense-adjacent graduate school. Every
   worked example, drill, metric story, and case in these files has been re-cast into commercial work —
   manufacturing inspection, fraud review, document search, lead scoring, delivery estimation. The
   concepts are what transferred; the vocabulary did not. If a phrase from the source domain survives
   into a deck, that is a defect — report it.
2. **Concepts, not copies.** These files are our own formulations. Source slides, question banks, and lab
   notebooks are **reference, not redistributable content** — see Licensing below. Nothing here should be
   pasted into a participant-facing deck without being rewritten in VSP's own words and examples.
3. **No dictionary definitions** (`program-spec.md`, Dorel's rule). Every entry below lands as a
   checklist item, a drill, a decision, or a question you can ask a client. Anything that reduced to a
   definition was cut.
4. **The spec is still the source.** A supplement that would change a lesson's duration, outcomes, or
   homework budget is a *proposal*, flagged as such at the bottom of its file — the module spec changes
   first, then the plan, then the material.

## Supplement index

| ID | Supplement | Serves | Feeds gap | Primary sources |
|---|---|---|---|---|
| [`SUP-1`](SUP-1-project-qualification-gates.md) | Project qualification gates — the ten questions, and the three-stage go/no-go | `LSN-1.6`, `LSN-3.5`, `LSN-3.6`, `MOD-4` | `GAP-4`, `GAP-10` | `SRC-3`, `SRC-4` |
| [`SUP-2`](SUP-2-data-reality-catalog.md) | Data reality catalog — what "we have data" actually means | `LSN-1.6`, `LSN-0.2`, `LSN-2.4` | `GAP-5` (walkthrough spine) | `SRC-3` |
| [`SUP-3`](SUP-3-metric-literacy-extension.md) | Metric literacy extension — the economics of precision vs recall, and metrics for generated text | `LSN-1.3`, `LSN-2.6`, `LSN-3.5` | `GAP-4`, `GAP-7` | `SRC-3`, `SRC-4` |
| [`SUP-4`](SUP-4-agent-architecture-ladder.md) | The agent architecture ladder — four designs, and the environment properties that force each one | `LSN-3.1`, `LSN-3.2` | `GAP-2` | `SRC-5` |
| [`SUP-5`](SUP-5-rag-optimization-ladder.md) | RAG optimization ladder — the twelve knobs, in the order you turn them | `LSN-2.3`, `LSN-2.4`, `LSN-2.5`, `LSN-2.6` | `GAP-9`, `GAP-7` | `SRC-1`, `SRC-2` |
| [`SUP-6`](SUP-6-agentic-patterns-and-limits.md) | Agentic design patterns and their limits — five patterns, six failure modes, the when-not-to list | `LSN-3.1`, `LSN-3.2`, `LSN-3.4`, `LSN-3.5` | `GAP-2`, `GAP-2b`, `GAP-4` | `SRC-1`, `SRC-2` |
| [`SUP-7`](SUP-7-failure-and-trust-catalog.md) | Failure and trust catalog — how models get fooled, and how you explain a conclusion | `LSN-2.6`, `LSN-3.5`, `LSN-1.5` | `GAP-7`, `GAP-4` | `SRC-3`, `SRC-4` |
| [`SUP-8`](SUP-8-assessment-item-seed.md) | Assessment item seed — coverage map, item-quality rules, and worked scenario rewrites | `ASM-0`–`ASM-3` | `GAP-6` | `SRC-2`, `SRC-3` |
| [`SUP-9`](SUP-9-prompt-and-inference-controls.md) | Prompt and inference controls — the knobs, the technique ladder, and the benchmark caveat | `LSN-2.1`, `LSN-2.2`, `LSN-2.6` | — (enriches built material) | `SRC-1`, `SRC-2` |
| [`SUP-10`](SUP-10-charts-that-communicate.md) | Charts that communicate — the decision case, the mystery-dataset reveal, the IQR fence rule, perception limits, the palette check | `LSN-0.2`, `LSN-0.3`, `LSN-1.3` | — (enriches built material); proposes an `SI-10`/`SI-19` amendment | `SRC-4` + primary sources |
| [`SUP-11`](SUP-11-uncertainty-decomposition.md) | The uncertainty decomposition — reducible vs irreducible, varying spread, calibration, out-of-depth detection | `LSN-0.4`, `LSN-0.2`, `LSN-1.6` | — (enriches built material) | `SRC-6` |
| [`SUP-12`](SUP-12-bias-and-disaggregation.md) | Bias and disaggregation — six named bias types, the headline metric that hides a 63-point gap, five test strategies, competing fairness definitions | `LSN-0.3`, `LSN-0.2`, `LSN-1.3`, `LSN-1.6` | `GAP-7`, `GAP-4` | `SRC-4` |

## Source catalog

| ID | Source | What it is | What was usable | What was dropped |
|---|---|---|---|---|
| `SRC-1` | Graduate seminar: applied large language models (11 weeks, 6 lecture decks + 6 lab notebooks + a project phase) | The closest existing analogue to `MOD-2`+`MOD-3`: prompting → evaluation → RAG → RAG optimization → agentic systems → tool protocols, each week paired with a runnable lab and a one-paragraph deliverable | The week-by-week build sequence, the RAG optimization ladder, the agentic pattern set, the assignment shape (one paragraph + evidence, due before next session), the project-proposal gate | The domain corpus (sector-specific policy documents), the sector benchmarks, the campus compute setup |
| `SRC-2` | Vendor-authored generative-AI teaching kit (9 modules: intro, tokens/embeddings, transformer, scaling laws, multimodal, diffusion, training/PEFT, orchestration, distributed serving) — each module carries lecture decks, demo notebooks, a lab, and a multiple-choice knowledge check | The orchestration module (chains → RAG → agents → guardrails) and the ~537-item knowledge-check bank as a coverage/format template | Diffusion, multimodal, distributed pre-training and serving — out of basics scope; revisit for the advanced tier |
| `SRC-3` | Executive AI overview short course (9 parts: intro, getting data, inference, machine learning, search and planning, performance metrics, perception, management, outlook) | Parts 2, 6, and 8 are the strongest material in the whole corpus for pre-sales work: data preparation reality, metric economics, and an adoption/failure/explainability treatment aimed at decision-makers rather than builders | Parts 5 and 7 (classical search, perception) — no `OUT-n.m` claims them at basics level |
| `SRC-4` | Vendor-authored accelerated data-science teaching kit (24 modules, each with lecture decks, a quiz with answers, and some with labs) | **Upgraded on second pass (2026-08-11) — this is the corpus's strongest MOD-0 source.** Originally logged as three narrow items (project-idea checklist; confusion-matrix/ROC/AUC "find out what positive means"; the eight-way problem-type taxonomy). The visualization modules (7, 8) and the data-ethics module (4) turned out to carry `SUP-10` and `SUP-12` almost whole, and module 3's outlier lab is directly runnable in the MOD-0 environment | Everything GPU/cluster-specific; the quizzes as items (see `SUP-8` — they are recall trivia, useful only as a negative example) |
| `SRC-5` | Graduate course: AI for simulation (agents, systematic search, neural networks, reinforcement learning, transformers) | The agent-architecture ladder and the environment-properties list — the best available conceptual grounding for `LSN-3.1`, and it predates and outlives the current framework churn | Game-tree search, the simulation platform, and the entire scenario domain |
| `SRC-6` | Two further vendor teaching kits (accelerated computing; deep learning for science and engineering) and an edge/robotics kit | **Corrected on second pass (2026-08-11).** The first pass logged "nothing at basics level," which was wrong: one slide of the deep-learning-for-science kit's Module 4 (uncertainty quantification) carries the reducible/irreducible split that became `SUP-11` — the highest-value single slide found in the whole corpus for `LSN-0.4`. The other ~29 slides of that lecture, and the accelerated-computing and edge/robotics kits, remain out of scope | Bayesian neural networks, posterior sampling, Monte Carlo methods (expert-tier candidates); all GPU/CUDA and robotics material |

Raw source files live outside `program/` in the donated corpus directory, which is **gitignored** — 16 GB
of third-party material with no redistribution grant does not belong in a repo whose decks are
public-facing. This directory holds only our own formulations.

### Where the corpus turned out to be thin

Recording the misses matters as much as the hits, so nobody re-mines the same ground:

- **`LSN-0.1` (orientation & environment setup) — low yield, and this is expected.** The kits are content
  courses; `LSN-0.1` is a contract-and-a-working-machine lesson. Its version-control and team modules are
  beginner-level ("Git backs up your code," "keep new repositories private"), and its useful content —
  the software-licence warning and the project-idea checklist — is already captured in `SUP-1`. One
  optional item survives: the third-wave/hype-cycle framing and the narrow-versus-general distinction, as
  a pre-work reading rather than live minutes. See `LSN-0.1`'s Materials table.
- **The vendor quiz banks are recall trivia, not assessment models.** Sampled across seven modules, they
  test which slide said what, several cite the wrong lecture number for their own answers, and multi-select
  items routinely have every option correct. They earn one role only: a worked negative example in
  `SUP-8`'s item-quality rules.
- **Diffusion, multimodal, distributed training, GPU programming, robotics, and the Bayesian half of the
  uncertainty lecture** serve no basics outcome. Advanced/expert-tier candidates at best.

## Licensing — read before copying anything into a deck

Two constraints, both real:

- **The vendor teaching kits (`SRC-2`, `SRC-4`, `SRC-6`) are licensed Creative Commons
  Attribution-NonCommercial 4.0.** VSP's training program is internal corporate enablement funded by a
  commercial firm. Treat the non-commercial clause as **binding against verbatim reuse**: do not lift
  slides, figures, lab notebooks, or knowledge-check items into VSP materials. Use them as a coverage and
  format reference and write our own items and examples — which the spec requires anyway (`ASM-n`
  questions are scenario questions, not definitions).
- **The university course material (`SRC-1`, `SRC-3`, `SRC-5`) carries no redistribution grant** that we
  have on file. Same rule: reference for structure and concepts, not a content source.

**Practical consequence:** every `SUP-n` file here is written as our own formulation with our own
examples, and is safe to build from. The source files are not. If a builder wants a figure or a phrasing
from a source, the answer is to make our own version — see `SI-25`'s precedent for exactly this
situation.

## How to add a supplement

1. Confirm the material serves an existing `OUT-n.m` through an existing `LSN-n.m`. If it doesn't, it is
   an advanced/expert-tier candidate — note it in `PROGRAM_PLAN.md`, not here.
2. Write it as checklist/drill/decision content, in commercial vocabulary, with a **"How this lands"**
   table naming the lesson, the segment or homework task, and whether it is a swap, an addition to a
   bank, or a builder reference.
3. Register it in the index above and add a row to the serving lesson plan's Materials table
   (`status: supplement`).
4. If it would change a contract, stop and flag it — spec first.
