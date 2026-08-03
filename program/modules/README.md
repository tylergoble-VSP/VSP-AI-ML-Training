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

## Adding a module (advanced/expert tiers)

Copy the section structure of any module spec here, register the module ID in `program-spec.md`'s ID registry, add outcomes serving `GOAL-n`, and list it in this catalog. Same discipline, same traceability.
