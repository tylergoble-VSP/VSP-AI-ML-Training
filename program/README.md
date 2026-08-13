# program/ — The VSP AI/ML Training Program Spec

Spec-driven curriculum development, mirroring [`vsp-tech/ai-way`](https://github.com/vsp-tech/ai-way): a governing spec is the single source of truth, everything downstream references it by ID, and the leadership spreadsheet is a generated view — not the working document.

## Start here: `program-spec.md`

The governing spec — program goals (`GOAL-n`), the traceability model, the ID registry, ceremonies, decision points, and ownership. Read it before touching anything else; every other file traces back to it.

## Then: `modules/`

One spec per basics module (`MOD-0`–`MOD-3`). Each module spec defines its outcomes (`OUT-n.m`), its lesson inventory (`LSN-n.m`) with duration/owner/pre-work/materials, its checkpoint (`ASM-n`), a traceability table, and its build list (`GAP-n`).

## Then: `lessons/`

Full lesson plans, one file per `LSN-n.m`, built from the module specs using `lessons/TEMPLATE.md`. This is the next phase of work — the module specs carry enough detail that each lesson plan can be drafted, reviewed by the lesson owner, and approved by the Curriculum Lead.

## What's in this directory

| Path | What it is | ai-way analogue |
|---|---|---|
| `program-spec.md` | Governing spec — goals, IDs, traceability, ceremonies, roles — **start here** | `sdlc.md` / the App Spec |
| `PROGRAM_PLAN.md` | The narrative plan from the July 28 meeting analysis (incl. advanced/expert outlines, logistics, asset map) | `README.md` overview + roadmap |
| `modules/` | Module specs, one per `MOD-n`, plus a catalog `README.md` | `skills/` catalog |
| `lessons/` | Lesson plans (`LSN-n.m`), built from module specs via `TEMPLATE.md` | `SKILL.md` files |
| `sources/` | External course corpus catalogued (`SRC-n`) and processed into build-ready supplements (`SUP-n`) attached to existing lessons | curated external references |
| `../meetings/` | Raw Circleback transcripts + notes — the requirements inputs | meeting transcripts in the App Spec |

## The rules

1. **The spec is the source.** The (M)LLM Literacy spreadsheet, session invites, and any deck are generated from the spec. Change the spec first.
2. **Everything references by ID.** A lesson plan serves `OUT-n.m`; an assessment verifies `OUT-n.m`; a notebook or deck belongs to `LSN-n.m`. No orphans.
3. **Coverage is queryable.** Every outcome needs ≥1 serving lesson and ≥1 verifying assessment; every gap needs an owner. Check before each curriculum review.
4. **Pre-work is load-bearing.** Every lesson ships with mandatory pre-work — this is the design fix for the failure mode Vlad flagged (audience lost by minute 20).
5. **No dictionary definitions.** Every concept is anchored to an exercise or a real VSP case (Dorel's rule).
6. **External material is a supplement, never a lesson.** Donated course material enters through [`sources/`](sources/README.md), is re-cast into VSP's commercial vocabulary, and attaches to an existing `LSN-n.m` by ID. It may sharpen a segment, add to a question bank, or shorten a `GAP-n` build — it may not re-time a session or grow a homework budget.

## Regenerating the spreadsheet view

To produce the (M)LLM Literacy spreadsheet for leadership: flatten every module spec's lesson inventory into rows — `Module | Lesson ID | Lesson | Duration | Owner | Goal (OUT refs) | Pre-work | Support material | Prerequisite`. One row per `LSN-n.m`, module checkpoint rows included.
