# modules/ — Basics Tier Module Specs

One spec per module. Every module spec follows the same format: configuration table → purpose → outcomes (`OUT-n.m`) → lesson inventory (`LSN-n.m`, one detailed section per lesson) → checkpoint (`ASM-n`) → traceability table → build list (`GAP-n`).

## Catalog

| Module | Spec | Dates (2026) | Effort (live + out-of-session) | Pillar | Checkpoint |
|---|---|---|---|---|---|
| `MOD-0` Foundations — Orientation & Statistics | [`module-0-foundations.md`](module-0-foundations.md) | Sep 1–4, daily | 4 h + 8 h = 12 h | Cross-cutting | `ASM-0` quiz |
| `MOD-1` ML Literacy | [`module-1-ml-literacy.md`](module-1-ml-literacy.md) | Sep 7 – Oct 12, Mondays | 6 h + 12 h = 18 h | ML (~5% of program) | `ASM-1` quiz + mock pre-sales |
| `MOD-2` LLM Literacy | [`module-2-llm-literacy.md`](module-2-llm-literacy.md) | Oct 19 – Nov 23, Mondays | 6 h + 24 h = 30 h | LLM | `ASM-2` quiz + whiteboard RAG |
| `MOD-3` Agentic Systems Literacy | [`module-3-agentic-systems.md`](module-3-agentic-systems.md) | Nov 30 – Dec 4, daily (2× on Dec 4) | 6 h + 12 h = 18 h | Agentic (lion's share) | `ASM-3` basics final: exam + mock client conversation |
| `MOD-4` Capstone — Agentic Lead-Scoring Harness | [`module-4-capstone.md`](module-4-capstone.md) | Dec 14–17, daily in-person | 20 h + 0 | Agentic (applied) | `ASM-4` graduation demo |

**Basics total:** 22 h live + 56 h out-of-session ≈ 78 h, Sep 1 – Dec 4 (pace varies — see [`../SCHEDULE.md`](../SCHEDULE.md)); capstone adds 20 h. Progression is strictly sequential — `MOD-n` checkpoint gates `MOD-n+1`. Basics is complete-or-nothing: no module skipping. Schedule, live times (1 h/lesson), and homework budgets locked from the program spreadsheet 2026-08-03.

## Aggregate build list

All open `GAP-n` items across modules, by priority (details live in each module spec):

| ID | Build item | Module | Priority |
|---|---|---|---|
| `GAP-1` | ~~Statistics foundation material (2 sessions + exercises)~~ **CLOSED** — LSN-0.2/0.3 decks + notebooks built (BUILD_LOG Rounds 1–2) | MOD-0 | done |
| `GAP-2` | Agentic framework landscape lesson (LangChain/LangGraph/LangSmith/Haystack) — framework cards double as LSN-3.1 homework | MOD-3 | P0 — needed Mon 30 Nov (pulled a day earlier by the 2026-08-03 re-scope) |
| `GAP-2b` | LSN-3.4 lab notebook restructured for the 1 h contract: three staged sections (pre-work / live / homework) with PASS/FAIL checkpoint cells, unattended fallback-index path; GAP-2 demo cells self-study-readable | MOD-3 | P0 — needed Wed 2 Dec |
| `GAP-3` | Cloud provider landscape lesson (Vertex, Bedrock, Microsoft Foundry) | MOD-3 | P0 |
| `GAP-4` | Production concerns lesson — observability, reliability, evals, KPIs, cost; now incl. cost-model + eval-regression **worksheets** (participants reproduce solo) and the TL question bank handout-ready Friday morning | MOD-3 | P0 — the translation-gap lesson |
| `GAP-5` | Real VSP case walkthrough material (needs Vlad + Dorel input) | MOD-1, MOD-3 | P1 — **hard dates:** LSN-1.6 brief by Mon 5 Oct (ships as pre-work a week ahead); MOD-3 briefs by Thu 3 Dec |
| `GAP-6` | Checkpoint quizzes, final exam, mock-conversation rubric | all | P1 — ASM-0 by Fri 4 Sep; ASM-1 ~Oct 12–16; ASM-2 ~Nov 23–27; ASM-3 ~Dec 7–11 (none on the spreadsheet — slots need confirming) |
| `GAP-7` | LLM limitations / client-expectations lesson — scope grown 2026-08-03: 4 pre-read cases (adds injection + privacy), golden-eval template, injection-test demo | MOD-2 | P1 — needed Mon 16 Nov |
| `GAP-8` | ~~MNIST hands-on for non-ML engineers~~ **CLOSED** — built Round 7 (BUILD_LOG) | MOD-1 | done |
| `GAP-9` | RAG hands-on adapted with a VSP-relevant corpus — scope changed 2026-08-03: build stages are now solo pre-work, so the notebook must run unattended (per-stage PASS/FAIL cells, inline recovery assets, staged failure with collapsed answer, pre-session thread summary cell) | MOD-2 | P1 — **needed Mon 2 Nov** (pre-work ship date, not session date) |
| `GAP-10` | Capstone brief + lead dataset (Vlad/Dorel) + starter repo + grading rubric | MOD-4 | P1 — needed before Dec 1 |
| `GAP-11` | **Retiming debt from the 2026-08-03 re-scope.** Decks: ~~all 10 retimed to 60-min + anonymized for public release 2026-08-03~~ **done** (see `lessons/decks/README.md` for the anonymization convention + remaining cosmetic overflow list). **Notebooks still pending:** LSN-0.2/0.3 (90-min session structure), LSN-1.3 (20/30/20/20 segment headers + quick-fire cell), LSN-1.4 (segments 3–4 relabel as homework blocks), LSN-1.5 ("no homework" closing section contradicts its plan) — and notebooks are **not anonymized** (internal names throughout) | MOD-0, MOD-1 | P0 — notebooks in participants' hands from Sep 2 |

## Supplement coverage of the build list

A donated external course corpus was processed into `SUP-n` supplements in [`../sources/`](../sources/README.md) on 2026-08-11. **No gap is closed by a supplement** — every row above keeps its owner and its date. What changed is that six of them now start from drafted structure instead of a blank page:

| Gap | Supplement input | What it supplies |
|---|---|---|
| `GAP-2` / `GAP-2b` | `SUP-4`, `SUP-6` | Framework-card row structure (which architecture rung, which of five patterns, does it speak the standard tool protocol); the three-way tool-failure partition as a break-it-drill rubric |
| `GAP-3` | `SUP-6` | One rubric row that actually discriminates between clouds — tool-protocol support |
| `GAP-4` | `SUP-1`, `SUP-3`, `SUP-6`, `SUP-7` | The TL question bank's spine (three go/no-go gates), six failure modes, guardrail checklist, cost-as-a-distribution, explainability questions |
| `GAP-5` | `SUP-2` | A case-walkthrough spine that runs on structure while the case briefs remain blocked on Vlad/Dorel |
| `GAP-6` | `SUP-8` | Coverage map, five item-quality rules, three worked scenario items, rubric dimension wording, and a build order keyed to the calendar |
| `GAP-7` | `SUP-3`, `SUP-5`, `SUP-7` | Generated-text metric vocabulary, the retrieval-vs-generation failure split, six structural weaknesses of learned systems |
| `GAP-9` | `SUP-5` | The twelve-knob optimization ladder — turns the RAG lab's failure demos into a repair manual |
| `GAP-10` | `SUP-1`, `SUP-8` | Capstone proposal gate and demo rubric shapes |

### Decisions taken 2026-08-11

All outstanding supplement proposals were resolved. Every one is a swap or a reframe inside an existing time budget — **no contract changed**, no session was re-timed, no homework budget grew.

| Change | Lesson | Nature | Rebuild cost |
|---|---|---|---|
| Six named bias types + CRM-export drill | `LSN-0.2` seg 2 | content inside 15 min | folds into the retiming round |
| 1.5 × IQR fence as the outlier rule | `LSN-0.2` seg 3 + hw 1 | method for an existing task | folds into the retiming round |
| Anscombe restaged as predict-then-reveal | `LSN-0.2` hw 2 | reframe inside 25 min | folds into the retiming round |
| Scenario question 1 → the disaggregation question | `LSN-0.3` hw 1 | **swap** (the old Q1 duplicated Q3's base-rate skill; Q3 still carries it) | folds into the retiming round |
| Five test strategies structuring the holdout design | `LSN-0.3` hw 4 | structure for an existing task | folds into the retiming round |
| Reducible/irreducible as a second sort axis | `LSN-0.4` seg 1 | bought from two misfiled-favourite debates | **new small round** |
| Calibration check as the second half of the sizing task | `LSN-0.4` hw 3 | 20 min split 12 + 8 | **new small round** |
| The "refuse the aggregate" spine named in all four plans | `LSN-0.2`/`0.3`/`0.4`/`1.3` | narrative cross-references | folds into existing rounds |
| Escalation ladder added to pre-work task 1 | `LSN-2.2` | content inside 25 min | **free** — materials unbuilt |
| Graded artifact → write-your-own-shortfalls-then-fix-them | `LSN-2.4` hw 2 | reframe inside 45 min | **free** — `GAP-9` unbuilt |
| "Honest limitation" as a named rubric dimension | `ASM-1`, `ASM-3` | pass-bar wording | **free** — `GAP-6` unbuilt |

Plus one build-standards change adopted as `SI-30`/`SI-31` in `lessons/BUILD_LOG.md`, and the resulting artifact debt as `COLOUR-1` in the MOD-0 and MOD-1 build lists — see below.

### `COLOUR-1` — measured accessibility defect in four built notebooks

A colour-vision check run on 2026-08-11 found that two palette entries, `yellow` `#ffe86b` and `mint` `#97f377`, are **perceptually the same colour under protanopia** (CIEDE2000 = 1.7) and near-identical under deuteranopia (5.5) — and are also the palette's closest pair in greyscale, so they fail in print too. Every other pair scores ≥10 worst-case, so **the palette is sound and this is one rule, not a redesign**.

Four notebooks use exactly that pair as the sole distinction between two categories: `LSN-0.3` cell 17, `LSN-1.4` cell 12, `LSN-1.5` cell 14 (a two-category colormap — the worst of the four), `LSN-1.6` cell 32. Fixes are one-line colour swaps plus re-execution. Three of the four fold into rebuild rounds already scheduled; `LSN-1.5` and `LSN-1.6` need one small joint round. Full analysis and the marginal cases: [`../sources/SUP-10-charts-that-communicate.md`](../sources/SUP-10-charts-that-communicate.md) §6.

## Adding a module (advanced/expert tiers)

Copy the section structure of any module spec here, register the module ID in `program-spec.md`'s ID registry, add outcomes serving `GOAL-n`, and list it in this catalog. Same discipline, same traceability.
