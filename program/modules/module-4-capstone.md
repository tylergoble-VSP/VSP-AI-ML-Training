# MOD-4 — Capstone: Build an Agentic Harness that Scores Leads

> **Provenance:** created 2026-08-03 from the program spreadsheet (Phase 4, four rows,
> Dec 14–17, 5 h/day, zero homework). The spreadsheet defines the *dates, duration, and
> deliverable name only* — everything below the configuration table is a **provisional
> skeleton** awaiting its own planning round (the treatment MOD-0–3 got). This module
> replaces the generic "hackathon" in earlier documents with a named build.

## Configuration

| Field | Value |
|---|---|
| **Dates** | Mon 14 – Thu 17 December 2026 (daily) |
| **Format** | In-person build week — 5 h/day live, **no pre-work, no homework** (per spreadsheet) |
| **Deliverable** | A working **agentic harness that scores leads**, demoed at graduation |
| **Teams** | Cohort splits into build teams (size TBD at enrollment count) |
| **Presenter / facilitator** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC — spreadsheet has "Mazilu?") |
| **Gate** | `ASM-0`–`ASM-3` passed — capstone is the application of the full basics stack |
| **Open date question** | Fri 18 Dec (show-and-tell + graduation in the original plan) is **not on the spreadsheet** — confirm whether demos land Dec 17 or Dec 18 |

## Purpose

Graduation is a build, not an exam. Teams apply everything basics installed — ML triage
(MOD-1), LLM plumbing and RAG (MOD-2), agent loops, tools, and production questions
(MOD-3) — to one VSP-shaped problem: **scoring inbound leads**. The harness framing is
deliberate: the deliverable isn't just an agent, it's the scaffolding around one —
instrumentation, evals, guardrails — because that's the production-grade muscle VSP sells
(`GOAL-3`) and the translation-gap closer (`GOAL-4`).

## Outcomes

| ID | Can-do statement | Serves |
|---|---|---|
| `OUT-4.1` | Build an agentic harness end to end — LLM + tools + loop + stop conditions — against a real scoring task | `GOAL-3` |
| `OUT-4.2` | Instrument it: log every tool call, trace failures, run an eval set, and say out loud what the numbers mean | `GOAL-3`, `GOAL-4` |
| `OUT-4.3` | Demo and defend the design in client-facing language — what it does, where it breaks, what it costs | `GOAL-1`–`GOAL-4` |

## Day plan (provisional — planning round required)

| Day | Date | Focus (draft) |
|---|---|---|
| D1 | Mon 14 Dec | Brief + lead-data walkthrough; scope the scoring problem; harness skeleton — loop + first tool call working |
| D2 | Tue 15 Dec | Scoring logic + tool set; first end-to-end scored lead |
| D3 | Wed 16 Dec | Eval harness (golden set, regression on prompt changes) + observability (traces, logs) — the LSN-3.5 questions, answered in code |
| D4 | Thu 17 Dec | Hardening + failure drills; demo prep; graduation demo (or Dec 18 — see open question) |

## Checkpoint

**`ASM-4` — graduation demo.** Team demo + Q&A graded against a rubric (build: `GAP-10`).
Passing basics + demoing the capstone = program graduation.

## Traceability

| Outcome | Served by | Verified by |
|---|---|---|
| `OUT-4.1` | D1–D2 | `ASM-4` |
| `OUT-4.2` | D3 | `ASM-4` |
| `OUT-4.3` | D4 | `ASM-4` |

## Build list

| ID | Item | Needs | Priority |
|---|---|---|---|
| `GAP-10` | Capstone brief + lead dataset (real or anonymized proxy — Vlad/Dorel input), starter repo, and grading rubric | Vlad/Dorel for data; Tyler for repo/rubric | P1 — must exist before Dec 1 so MOD-3 can tee it up |
