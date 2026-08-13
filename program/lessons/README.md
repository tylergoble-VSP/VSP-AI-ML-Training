# lessons/ — Lesson Plans

One file per lesson, named `LSN-<n>.<m>-<kebab-title>.md`, authored from [`TEMPLATE.md`](TEMPLATE.md). The module spec's LSN section is the **contract** (outcomes served, duration, format); the lesson plan is the full working document (segment-by-segment session plan, pre-work tasks, drills, materials, delivery notes).

**Rule:** if writing a lesson plan reveals the contract is wrong (duration unrealistic, outcome misplaced), update the module spec first, then the plan. The spec is the source.

**Schedule:** delivery dates, the 1 h-live contract, and per-module homework budgets (2 h; 4 h for MOD-2) were locked from the program spreadsheet on 2026-08-03 — see [`../SCHEDULE.md`](../SCHEDULE.md). Every plan carries them in its frontmatter (`delivery_date`, `duration`, `prework_time`, `homework_time`) and its Schedule section. The spreadsheet lists **Tyler as presenter and Vlad as reviewer for every lesson**; the Owner column below preserves the build-ownership and co-teacher recruiting intent, which is a separate question from who presents.

## Status Board

| Lesson | Title | Owner | Plan status |
|---|---|---|---|
| `LSN-0.1` | Orientation & environment setup | Tyler + Marius | draft |
| `LSN-0.2` | Statistics I — distributions, sampling, variance | Tyler | draft |
| `LSN-0.3` | Statistics II — probability, correlation ≠ causation | Tyler | draft |
| `LSN-0.4` | Deterministic, probabilistic, stochastic | Tyler | draft |
| `LSN-1.1` | The five ML jobs & the nesting doll | Tyler | draft |
| `LSN-1.2` | Model I/O | Tyler | draft |
| `LSN-1.3` | Grading models | Tyler | draft |
| `LSN-1.4` | Hands-on: train MNIST | Tyler / Stefana | draft |
| `LSN-1.5` | Conversational deep learning | Tyler | draft |
| `LSN-1.6` | Data requirements & pre-sales question bank | Tyler + Vlad | draft |
| `LSN-2.1` | How LLMs actually work | Tyler | draft |
| `LSN-2.2` | Prompting as engineering | Tyler | draft |
| `LSN-2.3` | Embeddings & vector search | Tyler | draft |
| `LSN-2.4` | Hands-on: build a RAG | Tyler | draft |
| `LSN-2.5` | Prompt vs RAG vs fine-tune | Tyler | draft |
| `LSN-2.6` | Limitations & what to promise a client | Tyler | draft |
| `LSN-3.1` | What is an agent | Tyler | draft |
| `LSN-3.2` | Framework landscape | Guest / TBD | draft |
| `LSN-3.3` | Cloud landscape | Per-cloud owners TBD | draft |
| `LSN-3.4` | Hands-on: build a tool-calling agent | Tyler | draft |
| `LSN-3.5` | Production concerns | Tyler + guest | draft |
| `LSN-3.6` | Real VSP cases, end to end | Vlad + Dorel + Tyler | draft |

Status vocabulary (matches `TEMPLATE.md` frontmatter): `not started → draft → reviewed → approved → delivered`. Update this board whenever a plan changes status.

## Supplements — read before building

Fifteen of the plans below now carry `supplement` rows in their Materials tables, pointing at [`../sources/`](../sources/README.md). A supplement is build-ready raw material — a checklist, a decision ladder, a drill rubric, a question bank — extracted from a donated external course corpus and re-cast into VSP's commercial vocabulary. **Builders: read the supplement rows in your lesson's Materials table before writing anything.** They will not change your contract (no supplement re-times a session or grows a homework budget), but several of them replace a generic illustration with a sharper one or supply a rubric where the plan currently says "drill."

**All supplement proposals were resolved on 2026-08-11** — eleven content changes adopted, every one a swap or reframe inside an existing time budget, plus one build-standards change (`SI-30`: colour never carries a distinction alone) and the artifact debt it exposed (`COLOUR-1`). The full decision table is in [`../modules/README.md`](../modules/README.md). Nothing is pending your approval; what is pending is the rebuild work, and it is carried in the module build lists.

## Suggested build order (recalibrated 2026-08-03 to the locked calendar)

1. **Retiming debt** (`GAP-11`) — LSN-0.2/0.3/1.3/1.4 decks + notebooks are built for the old 90/150-min contracts; first delivery is Sep 2.
2. **MOD-2 builds in pre-work-ship order** — `GAP-9` (RAG lab, solo-runnable) by Nov 2; `GAP-7` by Nov 16; MOD-2 decks/notebooks from Oct 12 (LSN-2.1 pre-work ships a week ahead of Oct 19).
3. **MOD-3 + capstone** — `GAP-2`/`GAP-2b` by Nov 30/Dec 2, `GAP-3`/`GAP-4` for the wrap week, `GAP-10` (capstone) before Dec 1.
4. **Assessments** (`GAP-6`) — ASM-0 needed Fri 4 Sep, the rest per the proposed slots in [`../SCHEDULE.md`](../SCHEDULE.md).
