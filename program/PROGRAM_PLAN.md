# VSP AI/ML Training Program — Initial Plan

**Source:** ML discussion call, July 28, 2026 (Vlad Damian, Dorel Macra, Marius Mazilu, Tyler Goble)
**Immediate deliverable:** Basics skeleton in the (M)LLM Literacy spreadsheet by EOD **Wednesday, July 30** — review call same day.

> **Note (July 28):** This document is the narrative analysis of the meeting and remains the reference for the advanced/expert outlines (§4–5), logistics (§6), and asset map (§8). The **program has since been formalized as a spec** — see [`program-spec.md`](program-spec.md) (governing spec) and [`modules/`](modules/) (per-module specs). Where this plan's §3 tables and the module specs disagree, **the module specs win**.
>
> **Note (Aug 3):** The schedule was locked from the program spreadsheet — Basics runs **Sep 1 – Dec 4, 2026** (1 h live per lesson; 2 h homework budget, 4 h in MOD-2), followed by a **Phase-4 capstone Dec 14–17** ("Build an Agentic Harness that Scores Leads", 5 h/day). This supersedes §2's "Sept 2026 basics / 4 weeks" timeline and §3's per-lesson durations. See [`SCHEDULE.md`](SCHEDULE.md) and [`modules/module-4-capstone.md`](modules/module-4-capstone.md).

---

## 1. Vlad's intent, distilled

What Vlad actually asked for (his definition of done):

1. **A presentable program plan, not a deck.** "Literally a table, an Excel" — modules, submodules, lessons, **duration per lesson**, **responsible owner per lesson**, homework/exams, and **goals per module** stated as capabilities, not dictionary definitions. This is what he presents to Marius Banici.
2. **The business goal:** close the translation gap between ML/AI engineers (Tyler, Stefana) and delivery engineers. Seniors/TLs must be able to *talk intelligently to customers* about (a) ML, (b) LLM-based solutions, and (c) agentic systems — and be able to actually **build production-grade agentic systems**, because that's the work VSP will be hired for.
3. **Weighting:** agentic systems are the lion's share. ML is ~5% of the total — "just enough ML to go through a pre-sales" (neural nets, CNNs, deep learning, RL at conversation level, backed by one small hands-on exercise).
4. **Success bar:** "walk at a brisk pace," not run a marathon. Well-rounded first, then inflate — no spikes.
5. **Audience & stakes:** seniors and TLs (plus directors — Dorel and Vlad intend to be trainees), **10–12 spots**, basics is mandatory-complete (no pick-and-choose), and anyone who doesn't do the work is out. Incentive: staying employable as client AI demand grows.
6. **Delivery:** ~90% remote self-study with **intentional pre-work** (the Andrei Ciobanu training failed because there was none), curated resources over hand-holding ("I don't need hand-holding, I need direction"), multimodal support material per lesson, multiple owners/co-teachers, and an in-person **hackathon the week before Christmas** as graduation.
7. **It's a living program:** expert-tier work feeds discoveries back into advanced/basics. "Education that never stops."
8. **Dorel's constraint:** anchor lessons to real VSP prospects/projects (e.g., the construction-site photo/video completion prospect, 6MAP, agents-in-production) so material sticks.

---

## 2. Program architecture

Three pillars × three tiers. Every tier covers all three pillars (well-rounded, then inflate).

| | **ML Literacy** (~5% overall) | **LLM Literacy** | **Agentic Systems** (lion's share) |
|---|---|---|---|
| **Basics** (1 mo, mandatory, complete) | Five ML jobs, model I/O, metrics, one hands-on trained model | How LLMs work, prompting, embeddings, RAG fundamentals | What agents are, framework/cloud landscape, one hands-on agent, production questions to ask |
| **Advanced** (3 mo, self-study + direction) | Curated pointers only (Stanford ML coursework) | Fine-tuning, graph RAG, eval basics | Framework deep dives, one cloud per person, ship a real agentic feature with observability |
| **Expert** (6 mo, deep dives) | — | Karpathy build-from-scratch spirit | Evaluation frameworks (AISI Inspect, CyberBench-style), harness design, chaos/production hardening, cost & hardware |

**Timeline proposal:**
- **Aug 2026** — finalize basics curriculum + build missing material; enroll the 10–12
- **Sept 2026** — run Basics (all participants)
- **Oct–Dec 2026** — Advanced (self-study cadence with weekly check-ins)
- **Week of Dec 14–18, 2026** — in-person hackathon: 4 days build, Friday show-and-tell + graduation
- **Jan–Jun 2027** — Expert tier for those continuing; findings feed back into basics/advanced

---

## 3. Basics skeleton (the Wednesday deliverable)

~21 lessons over 4 weeks, ≈ 30–34 hours total (~8 hrs/week alongside normal work). Each lesson = pre-work + live/recorded session + homework. Owners: Tyler unless noted; guest co-teachers from Tyler's network TBD; Stefana as candidate hands-on co-owner.

**Module goals are "can-do" statements** — the format Vlad asked for.

### Module 0 — Orientation & Statistics Foundation (Week 1, ~5.5h)
*Goal: You can explain why ML answers come with uncertainty attached, and you have a working environment.*

| # | Lesson | Duration | Owner | Hands-on / support |
|---|---|---|---|---|
| 0.1 | Program orientation: rules, cadence, pre-work contract, environment setup (Python, Jupyter, this repo) | 1h | Tyler + Marius | `ACTIVATE_VENV.md`, `requirements.txt`, `foundations/01_Beginning_Python` (optional pre-work for non-Python folks) |
| 0.2 | Statistics I: distributions, mean/variance, sampling, why "all models are wrong, some are useful" | 1.5h | Tyler | New material |
| 0.3 | Statistics II: probability, conditional probability, correlation ≠ causation | 1.5h | Tyler | New material |
| 0.4 | Deterministic vs probabilistic vs stochastic — reading a confidence number like a grown-up | 1h | Tyler | Existing ML literacy deck (§ keywords) |
| — | Checkpoint quiz | 0.5h | Tyler | New |

### Module 1 — ML Literacy (Weeks 1–2, ~8h)
*Goal: You can triage a client ask into classify/cluster/regress/propensity/recommend, interpret a model's outputs and metrics, and you have personally trained one labeled model.*

| # | Lesson | Duration | Owner | Hands-on / support |
|---|---|---|---|---|
| 1.1 | The five ML jobs + the nesting doll (ML ⊃ deep learning ⊃ generative AI) | 1h | Tyler | Existing ML literacy deck |
| 1.2 | Model I/O: what each model type takes in, kicks out, and how to interpret it | 1h | Tyler | Deck + `foundations/04–08` notebooks as reference |
| 1.3 | Grading models: MAE, precision/recall, confusion matrix, AUC | 1.5h | Tyler | Deck + `foundations/12_Analytics_Performance` |
| 1.4 | **Hands-on: train MNIST with PyTorch/Keras in a Jupyter notebook** | 2.5h | Tyler / Stefana | `neural_networks/01_Perceptron_MLP`, `02_CNN` (adapt) |
| 1.5 | Conversational deep learning: neural nets, CNNs, RL — enough to not look stupid | 1h | Tyler | `neural_networks/*`, `reinforcement/*` as pointers |
| 1.6 | Data requirements & limitations: "no data, no model," what ML can't do, the pre-sales question bank | 1h | Tyler + Vlad (real cases) | New; anchor to 6MAP + construction-site prospect |
| — | Checkpoint: mock pre-sales Q&A (roleplay graded) | — | Vlad plays the client | New |

### Module 2 — LLM Literacy (Weeks 2–3, ~8.5h)
*Goal: You can explain how an LLM works at the token level, sketch a RAG architecture on a whiteboard, and say when to prompt vs RAG vs fine-tune.*

| # | Lesson | Duration | Owner | Hands-on / support |
|---|---|---|---|---|
| 2.1 | How LLMs actually work: tokens, training, inference (Karpathy-spirit, curated excerpts) | 1.5h | Tyler | Karpathy "LLM from scratch" (curated clips), Stanford GenAI course |
| 2.2 | Prompting, context windows, structured outputs, tool use | 1.5h | Tyler | `generative_ai/05_ChainOfThought`, `06_Tool_Calling` |
| 2.3 | Embeddings & vector search | 1.5h | Tyler | `foundations/10_Embedding_Models` |
| 2.4 | **Hands-on: RAG fundamentals — build one against real docs** | 2h | Tyler | `generative_ai/07_RAG` |
| 2.5 | Prompt vs RAG vs fine-tune: decision framework + cost/latency basics | 1h | Tyler | `generative_ai/04_LoRA_PEFT` as pointer |
| 2.6 | LLM limitations: hallucination, evals at a glance, what to promise a client | 1h | Tyler | New |
| — | Checkpoint quiz + whiteboard exercise | — | | New |

### Module 3 — Agentic Systems Literacy (Weeks 3–4, ~9.5h)
*Goal: You can explain what an agent is, name the major frameworks and cloud offerings and when each fits, ask the right observability/reliability/cost questions, and you have personally built a tool-calling agent.*

| # | Lesson | Duration | Owner | Hands-on / support |
|---|---|---|---|---|
| 3.1 | What is an agent: tools, loops, harnesses, when agents beat workflows | 1.5h | Tyler | `generative_ai/06_Tool_Calling_Agents` |
| 3.2 | Framework landscape: LangChain / LangGraph / LangSmith / Haystack — what each is for | 1.5h | Guest / TBD | New material |
| 3.3 | Cloud landscape: GCP Vertex, AWS Bedrock, Azure AI Foundry — offerings & tradeoffs | 1.5h | Split: one owner per cloud (TBD) | New material |
| 3.4 | **Hands-on: build a tool-calling agent end to end** | 2.5h | Tyler | `generative_ai/06` (extend) |
| 3.5 | Production concerns: observability, reliability, evals, KPIs, hardware & cost — the questions a TL must ask | 1.5h | Tyler + guest | New; this is Vlad's translation-gap lesson |
| 3.6 | Real VSP case walk-throughs: 6MAP, construction-site vision prospect, agents-in-production | 1h | Vlad + Dorel + Tyler | New (Dorel's ask) |
| — | **Final assessment: graded exam + mock client conversation covering all three pillars** | 1.5h | All | Seed from `interview/` notebooks |

---

## 4. Advanced tier outline (3 months, ~90% self-study)

Per-person cadence: weekly 1h group check-in; everything else curated self-study with deliverables.

- **LLM:** graph-based RAG (`generative_ai/08_Neo4j`, `09_Graph_RAG`), fine-tuning in practice (`04_LoRA_PEFT`), local models (`02_LlamaCPP`, `03_Ollama`)
- **Agentic:** one framework deep-dive per person (LangGraph, Haystack, cloud-native); **each person owns one cloud provider** and teaches it back (Vlad: "maybe somebody knows Azure, somebody knows Bedrock — it doesn't have to be one person")
- **Capstone:** ship one real agentic feature (internal or client-adjacent) with observability and an eval harness — this becomes hackathon prep
- **Companions:** Stanford ML / GenAI coursework (Tyler pulling actual slide decks via academic contacts)
- Advanced RAG patterns promoted/demoted between basics and advanced as the group decides (Vlad explicitly left this to the group)

## 5. Expert tier outline (6 months, deep dives)

- Evaluation frameworks: **AISI Inspect**, CyberBench-style benches — learn, fork, adapt
- Harness design and agent reliability engineering; "put chaos monkey on it" production hardening
- Cost/hardware optimization at scale
- **Feedback loop:** every expert deep-dive produces a lesson or resource that feeds back into basics/advanced — this is how the program stays alive

---

## 6. Delivery model & logistics

- **Format:** ~90% remote. Every lesson = mandatory pre-work → session → homework. Pre-work is enforced: no pre-work, no session (the Ciobanu lesson).
- **Support material:** each lesson row in the spreadsheet links to its material (deck, notebook, video, reading). This repo is the home for hands-on notebooks; the spreadsheet is the source of truth for the curriculum.
- **Option A (logistics doc):** Tyler flies in for a 1–2 week intensive basics boot camp (phones-in-the-closet format). **Option B:** fully remote basics + December hackathon. Recommend B for basics, keep A as accelerator if remote traction is poor.
- **Hackathon:** week of Dec 14–18, 2026. Mon–Thu build (teams apply the full stack to a real VSP-shaped problem), Friday show-and-tell + graduation. Gives the program gravitas (Vlad's word).
- **Owners:** not one person. Tyler anchors ML/LLM; guest co-teachers from Tyler's network for specific lessons; per-cloud owners recruited from participants; Vlad/Dorel own the real-case lessons.
- **Discipline:** 10–12 spots, seniors/TLs (+ directors). Miss the work → out.

## 7. Assessment model

- Checkpoint quiz per module + hands-on artifact (trained model, working RAG, working agent)
- Final basics assessment = graded exam **+ mock pre-sales conversation** (the actual job skill Vlad wants)
- The `interview/` notebooks (junior/mid/senior GenAI implementation, ML Engineer test + answer key) are ready-made seeds for exams

## 8. Asset map — what exists vs. what to build

**Already in this repo (basics hands-on is mostly built):**
- Python on-ramp: `foundations/01–03`
- ML reference library: `supervised/` (7), `unsupervised/` (7), `ensemble/` (4), `reinforcement/` (2), `foundations/04–09, 12`
- Deep learning: `neural_networks/01–05` (incl. MLP/CNN for the MNIST lesson)
- LLM/GenAI: `generative_ai/01–09` (transformers, local models, LoRA, CoT, tool-calling agents, RAG, Neo4j, graph RAG), `foundations/10–11`
- Assessment seeds: `interview/` notebooks
- The ML literacy deck → reframe as the **table-of-contents / companion presentation** (Vlad approved this framing)

**Gaps to build (priority order):**
1. Statistics foundation module (0.2–0.4)
2. Agentic frameworks + cloud landscape lessons (3.2–3.3) — biggest content gap, and the program's center of gravity
3. Production concerns lesson (3.5): observability, reliability, evals, KPIs, cost
4. VSP real-case walk-throughs (1.6, 3.6) — needs Vlad/Dorel input
5. Module quizzes + final exam + roleplay rubric
6. LLM limitations / what-to-promise-a-client lesson (2.6)

## 9. Immediate next steps (before EOD Wed, July 30)

1. **Transfer §3 into the (M)LLM Literacy spreadsheet** — columns: Module | Lesson | Duration | Owner | Goal | Support material | Prerequisite. This is the exact artifact Vlad asked for. *(Tyler — the action item)*
2. Pull Stanford intro-ML / intro-GenAI course structures (and slide decks via contacts) to sanity-check module ordering and fill duration estimates. *(Tyler)*
3. Reframe the current ML literacy deck as the program's table-of-contents presentation. *(Tyler)*
4. List 2–3 candidate co-teachers from network for lessons 3.2/3.3/3.5. *(Tyler)*
5. Marius schedules the July 30 review call; walk the skeleton, assign owners, lock durations. *(Marius — his action item)*
6. Ask Vlad/Dorel for the shortlist of real prospects/projects for the case lessons. *(At the review call)*
