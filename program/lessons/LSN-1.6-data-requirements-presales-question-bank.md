---
name: LSN-1.6-data-requirements-presales-question-bank
description: Articulate ML's data requirements and limits ("no data, no model; it can only infer so far") and run a pre-sales question bank against a real prospect without over-promising.
module: MOD-1
delivery_date: 2026-10-12
serves: OUT-1.6
duration: 1
prework_time: 40
homework_time: 80
owner: Tyler Goble + Vlad Damian (case material)
status: draft
---

# LSN-1.6 — Data Requirements, Limitations & the Pre-Sales Question Bank

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.6` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | ASM-1 (mock pre-sales conversation + question bank artifact) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 12 October 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Data Requirements for ML."** This is the last MOD-1 row on the spreadsheet; `ASM-1` follows but has no slot yet.

## Narrative

Closes the module by turning limitations into an asset. Vlad's 6MAP takeaway — "I need data in order for the model… it can only infer to a certain point" — sounds like a truism until you watch a deal wobble because nobody asked about the data early. This lesson installs the data-reality checklist (exists / labeled / enough / fresh / legal) and converts it into the pre-sales question bank: the questions that make VSP look sharp precisely *because* they're honest. Everything from LSN-1.1–1.5 gets exercised on the construction-site case; the take-home question bank feeds directly into the ASM-1 mock conversation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the anonymized construction-site case brief (Vlad/Dorel, GAP-5) | 25 min | One data-reality risk you spotted in the brief, one sentence |
| 2 | Skim the starter question bank below | 5 min | One question you'd add, sharpen, or cut |
| 3 | Re-open your own LSN-1.4 degradation curve and write down the number it implies for **enough**: at what training-set size did your model become useless? The session opens on this chart | 10 min | One number and one sentence — your own evidence for the "enough" row |

**Pre-work total: 40 min.** Task 3 is where LSN-1.4's relocated break-it homework pays off: the "no data, no model" claim arrives as a chart each participant produced themselves, which is also where the collective moment lost from that lab's live hour gets recovered.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| The data reality checklist | 20 min | talk + examples | Walk the five checks (table below), each with a real failure story — leading with the 6MAP data lesson for **exists**. The through-line: every "no" on the checklist is not a dealbreaker, it's a scoping conversation you want to have *before* the SOW, not after. |
| Case walkthrough: construction-site completion detection | 25 min | discussion (structured walkthrough below) | Group works the real prospect end to end using the walkthrough structure; instructor facilitates, participants supply the answers. Pre-work risks read out at step 3. |
| Build the question bank | 15 min | workshop | Starter bank below on screen; group refines wording, adds/cuts against the case they just worked, and orders the questions the way a real discovery call flows. The refined bank is the module's take-home artifact. |

**Timing check:** 20 + 25 + 15 = 60 min = 1 h — matches the spreadsheet contract. Unchanged by the 2026-08-03 rescope; the deck's notes are already timed 20/25/15.

### The data reality checklist (draft — session refines)

| Check | The question | The failure it catches |
|---|---|---|
| **Exists** | Is the thing you want predicted actually recorded anywhere today? | "We'll start collecting once the project starts" — no data, no model. |
| **Labeled** | Does each example carry the answer, or must a human add it? Who, and at what cost per label? | Labeling quietly becomes the project's biggest line item — or gets skipped and poisons the model. |
| **Enough** | How many examples — especially of the rare outcome you care about? | 40 examples of the event of interest won't train anything; base rates bite (LSN-0.3/1.3). |
| **Fresh** | How recent is the data, and has the business changed since it was collected? | A model trained on the pre-reorg world confidently predicts a world that no longer exists. |
| **Legal** | Do you own this data and may you use it this way — privacy, contract, people in frame? | The model works; the deal dies in legal review. |

### Case walkthrough structure (runs even before the GAP-5 brief lands)

1. **Restate the ask** (2 min): client wants to know, from periodic site photos/video, whether work milestones are actually complete.
2. **Triage the job** (3 min — LSN-1.1 callback): per-milestone "complete: yes/no" → classification; "% complete" → regression; on images → CNN territory (LSN-1.5).
3. **Run the checklist** (12 min): *Exists* — are there historical photos, and from how many sites? *Labeled* — who says which photos show "complete," and do two site managers even agree? *Enough* — how many examples per milestone type; rare milestones = rare classes. *Fresh* — seasons, camera positions, new construction methods. *Legal* — workers identifiable in frame; who owns drone footage; client vs subcontractor data rights. Pre-work risks surface here.
4. **Where it breaks** (5 min): occlusion and camera angle, label ambiguity ("complete" is a judgment call), few examples per site type, distribution shift between sites.
5. **What VSP should promise** (3 min): a scoped pilot on one milestone type with human-in-the-loop review — not "AI that watches your sites." Honest scoping is the sales move.

### Starter pre-sales question bank (draft — session refines; 11 questions)

1. What decision will the model's output drive, and who acts on it?
2. Is this a prediction problem at all — or do you need something generative/conversational? (LSN-1.1 triage)
3. What data do you have *today* that records the thing you want predicted?
4. Is the outcome written in the data, or would someone have to label it? Who, and at what cost?
5. How many examples do you have of the outcome you actually care about — especially if it's rare?
6. How old is the data, and has the business changed since it was collected?
7. How does new data arrive — a live feed, or a one-time dump someone exported once?
8. Who owns the data, and are there privacy, contractual, or regulatory limits on using it this way?
9. What does each kind of wrong answer cost you — a false alarm vs a miss? (LSN-1.3)
10. What's the current human baseline, and how good would the model have to be to beat it usefully?
11. What happens to the cases the model can't handle — is there a human fallback path?

## Client Tie-In (Dorel's rule)

The centerpiece *is* the real construction-site completion prospect, walked end to end; the checklist's "exists" row carries the 6MAP data lesson in Vlad's own words. This closes the module — the next step is ASM-1, where the mock client conversation grades exactly what was rehearsed here.

## Homework

**80 min**, in `notebooks/lessons/LSN-1.6_Data_Requirements_Presales_Question_Bank.ipynb`. The existing graded artifact keeps its full weight and gains two supports; nothing here is filler, because this is the last work before ASM-1 and the bank is the thing being graded there.

| # | Task | Time | Checkpoint / artifact |
|---|---|---|---|
| 1 | **The graded artifact.** Apply the refined question bank to one prospect or project you know first-hand, in the notebook's homework template. Every checklist dimension answered with specifics, plus at least one honestly-stated limitation — where the model would break and what you would scope instead | 50 min | Filled bank saved to `outputs/lsn-1.6/`, submitted referencing `LSN-1.6`; run the built-in advisor before submitting |
| 2 | **The coverage matrix.** Fill the notebook's five-check matrix for that same prospect: for each of exists / labeled / enough / fresh / legal, state the evidence you actually have versus the evidence you would need, and mark which gaps you could close with one phone call | 20 min | Completed matrix; at least one gap marked "one phone call" and at least one marked genuinely unknown |
| 3 | **The opening three.** From your bank, pick the three questions you would actually open that discovery call with, in order, and write one line on why that order | 10 min | Three ordered questions — this is what you walk into ASM-1 with |

**Pass (task 1, unchanged):** every checklist dimension addressed with specifics, plus at least one honestly-stated limitation. This artifact is part of the ASM-1 evidence for `OUT-1.6`. **Pass (tasks 2–3):** the matrix distinguishes what you know from what you assume, and the opening three do not lead with a data question — a discovery call opens on the decision the client wants to make (bank question 1), because that is what makes every later data question answerable.

**Time accounting:** pre-work 40 min + homework 80 min = 2 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| **Session companion notebook** — checklist with one number per row, case-walkthrough workspace (GAP-5 slots marked), coverage matrix, homework template + advisor | exists | `notebooks/lessons/LSN-1.6_Data_Requirements_Presales_Question_Bank.ipynb` |
| **Session deck** — 18 slides, speaker notes timed 20/25/15 = 60, GAP-5 placeholder chips | exists | `program/lessons/decks/LSN-1.6-data-requirements.html` |
| Anonymized construction-site case brief | **build (GAP-5) — depends on Vlad/Dorel input; walkthrough runs today with marked placeholders; brief's facts slot into the marked cells/slides. Hard date now set: needed by Mon 5 Oct 2026, one week before delivery, because 25 min of pre-work is reading it** | Vlad/Dorel to supply; Tyler formats |
| Data reality checklist (draft) | exists | This plan (above) |
| Starter pre-sales question bank (draft) | exists | This plan (above) |
| Question bank template (blank, for homework submissions) | exists — starter template; refined live at delivery, updated after first delivery | Fill-in homework cell in `notebooks/lessons/LSN-1.6_Data_Requirements_Presales_Question_Bank.ipynb` (saves to `outputs/lsn-1.6/`; advisor pre-checks against the pass bar without gating the save) |
| ML literacy deck (limitations section) | exists | ML literacy deck (see PROGRAM_PLAN.md §8) — not in repo |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality (the 15-min bank workshop is tight). Feeds the MOD-1 retro.

**Rescope note (2026-08-03):** the live hour is unchanged — deck and notebook are already timed 20/25/15 = 60, so no retiming is needed. Two artifact edits follow from the rescope: the notebook's homework section now launches three tasks rather than one, and its opening should lead with the participant's own LSN-1.4 degradation curve (pre-work task 3), which the previous design assumed would be fresh from a live lab segment rather than from that lesson's homework. GAP-5's deadline is now a hard date (Mon 5 Oct 2026) rather than "Week 2."
