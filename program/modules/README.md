# modules/ — Basics Tier Module Specs

One spec per module. Every module spec follows the same format: configuration table → purpose → outcomes (`OUT-n.m`) → lesson inventory (`LSN-n.m`, one detailed section per lesson) → checkpoint (`ASM-n`) → traceability table → build list (`GAP-n`).

## Catalog

| Module | Spec | Week | Effort | Pillar | Checkpoint |
|---|---|---|---|---|---|
| `MOD-0` Foundations — Orientation & Statistics | [`module-0-foundations.md`](module-0-foundations.md) | 1 | ~5.5 h | Cross-cutting | `ASM-0` quiz |
| `MOD-1` ML Literacy | [`module-1-ml-literacy.md`](module-1-ml-literacy.md) | 1–2 | ~9 h | ML (~5% of program) | `ASM-1` quiz + mock pre-sales |
| `MOD-2` LLM Literacy | [`module-2-llm-literacy.md`](module-2-llm-literacy.md) | 2–3 | ~9 h | LLM | `ASM-2` quiz + whiteboard RAG |
| `MOD-3` Agentic Systems Literacy | [`module-3-agentic-systems.md`](module-3-agentic-systems.md) | 3–4 | ~11 h | Agentic (lion's share) | `ASM-3` basics final: exam + mock client conversation |

**Basics total:** ~34 h over 4 weeks (~8 h/week). Progression is strictly sequential — `MOD-n` checkpoint gates `MOD-n+1`. Basics is complete-or-nothing: no module skipping.

## Aggregate build list

All open `GAP-n` items across modules, by priority (details live in each module spec):

| ID | Build item | Module | Priority |
|---|---|---|---|
| `GAP-1` | Statistics foundation material (2 sessions + exercises) | MOD-0 | P0 |
| `GAP-2` | Agentic framework landscape lesson (LangChain/LangGraph/LangSmith/Haystack) | MOD-3 | P0 — program's center of gravity |
| `GAP-3` | Cloud provider landscape lesson (Vertex, Bedrock, Microsoft Foundry) | MOD-3 | P0 |
| `GAP-4` | Production concerns lesson — observability, reliability, evals, KPIs, cost | MOD-3 | P0 — the translation-gap lesson |
| `GAP-5` | Real VSP case walkthrough material (needs Vlad + Dorel input) | MOD-1, MOD-3 | P1 |
| `GAP-6` | Checkpoint quizzes, final exam, mock-conversation rubric | all | P1 |
| `GAP-7` | LLM limitations / client-expectations lesson | MOD-2 | P1 |
| `GAP-8` | MNIST hands-on for non-ML engineers (new guided notebook synthesized from `neural_networks/01–02`) | MOD-1 | P1 |
| `GAP-9` | RAG hands-on adapted with a VSP-relevant corpus | MOD-2 | P2 |

## Adding a module (advanced/expert tiers)

Copy the section structure of any module spec here, register the module ID in `program-spec.md`'s ID registry, add outcomes serving `GOAL-n`, and list it in this catalog. Same discipline, same traceability.
