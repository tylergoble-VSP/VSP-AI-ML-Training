---
name: LSN-{{N}}.{{M}}-{{kebab-title}}
description: {{One line — what the participant can do after this lesson that they couldn't before.}}
module: MOD-{{N}}
delivery_date: {{YYYY-MM-DD — from program/SCHEDULE.md}}
serves: {{OUT-N.M[, OUT-N.M]}}
duration: {{session hours — 1 for every basics lesson per the locked spreadsheet}}
prework_time: {{minutes}}
homework_time: {{minutes — prework_time + homework_time must equal the module's out-of-session budget}}
owner: {{lesson owner}}
status: draft | reviewed | approved | delivered
---

# LSN-{{N}}.{{M}} — {{Title}}

<!--
Lesson plans are built FROM the module spec (program/modules/module-N-*.md) — the spec's
LSN section is the contract; this file is the full working plan. Authoring-time tokens use
{{double-braces}} and must all be resolved before status: reviewed. Runtime tokens
(<participant>, <date>) stay. Keep the whole file under 200 lines.

Approval flow (program-spec.md, Human Decision Points): author drafts → lesson owner
reviews → Curriculum Lead approves against the module spec. A lesson plan that drifts
from its LSN contract updates the SPEC FIRST, then itself.
-->

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | {{OUT refs — copy from module spec}} |
| **Duration** | 1 h live + {{2 or 4}} h out-of-session (pre-work + homework) |
| **Format** | {{live / live lab / recorded + Q&A / panel}} |
| **Verified by** | {{ASM-n — how this lesson's outcomes get checked}} |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | {{Weekday, D Month 2026 — from program/SCHEDULE.md}} |
| **Live session** | 1 h |
| **Out-of-session budget** | {{2 or 4}} h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

## Narrative

{{2–4 sentences: the story of the session. What misconception does it kill, what capability
does it install, and how does it connect backward (callbacks) and forward (setups)?}}

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | {{task}} | {{min}} | {{what they show up with}} |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| {{name}} | {{min}} | {{talk / demo / lab / drill / discussion}} | {{what happens, concretely — for a lab: the checkpoints; for a drill: the scenarios}} |

**Timing check:** segments must sum to 60 min — the spreadsheet contract.

## Client Tie-In (Dorel's rule)

{{Which real VSP case, prospect, or scenario grounds this lesson. No dictionary definitions.}}

## Homework

{{Artifact + grading standard, or "None — feeds into <next lesson> pre-work". Graded artifacts
reference this LSN id in their submission.}}

**Time accounting:** pre-work {{X}} min + homework {{Y}} min = {{2 or 4}} h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| {{deck / notebook / video / reading}} | exists / adapt / build ({{GAP-n}}) | {{path or link}} |

## Delivery Notes

{{Filled after each delivery: what landed, what dragged, timing reality. Feeds the module
retro; retro findings that change scope update the module spec.}}
