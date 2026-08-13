---
name: LSN-0.1-orientation-environment-setup
description: Understand the program's contract and leave with Python + Jupyter running a notebook end to end on your own machine.
module: MOD-0
delivery_date: 2026-09-01
serves: OUT-0.1
duration: 1
prework_time: 45
homework_time: 75
owner: Tyler + Marius
status: draft
---

# LSN-0.1 — Orientation & Environment Setup

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.1` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live, hands-on |
| **Verified by** | `ASM-0` (setup evidence: screenshot of executed notebook) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Tuesday, 1 September 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

Spreadsheet row title: **"Orientation."** First day of the daily boot week — `LSN-0.2` follows the next morning.

## Narrative

This session is the program's contract made physical: everyone hears why pre-work is enforced (the Ciobanu failure — no intentional prior work, 90% of the audience lost in the first 20%) and everyone leaves with a running notebook, because nobody gets to spend the rest of the boot week — `LSN-0.2` is tomorrow morning — fighting their environment instead of learning. It kills the assumption that this is another watch-and-forget training, and it installs the one capability everything else stands on: a local Python + Jupyter setup that executes end to end. Sets up `LSN-0.2` (which opens in a notebook) and the `LSN-1.4` MNIST lab; the baseline self-rating taken here is the yardstick the whole program is measured against at graduation.

## Pre-work (mandatory — no pre-work, no seat) — 45 min

Held at 45 min rather than the boot week's ≤ 30 min norm: this pre-work lands on Monday 31 August, the one evening of the week with no prior lesson's homework stacked on it.

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read `program/README.md` and the **Ceremonies** + **Enrollment Gate** sections of `program/program-spec.md` | 10 min | One written question or concern about the cadence (pre-work → session → homework → checkpoint) |
| 2 | Clone the `VSP-AI-ML-Training` repo | 5 min | Local clone path |
| 3 | Create the virtualenv and install MOD-0 dependencies per `ACTIVATE_VENV.md` + `requirements.txt`, then register the kernel so the venv is selectable in Jupyter/VS Code | 15 min | Terminal output: activated venv prompt + `python --version` + clean `pip install` finish (or the failure output) |
| 4 | If step 3 failed: work through `INSTALL_TROUBLESHOOTING.md` | 10 min | The exact error message, copied as text — this is a valid pre-work artifact; broken setups get fixed live |
| 5 | Launch Jupyter and open `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb`; run the first cells if you can | 5 min | Screenshot of the open notebook (executed cell if it worked) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Program walkthrough | 15 min | talk | Three pillars (ML / LLM / agentic) × the locked calendar (basics Sep 1 – Dec 4, capstone Dec 14–17 — see `program/SCHEDULE.md`); why agentic is the lion's share and ML is ~5%; the cadence and the pre-work rule with the Ciobanu story told straight; checkpoint gates `ASM-0`–`ASM-3` and the GOAL-7 deal: do the work or you're out; capstone graduation build Dec 14–17 (Dec 18 show-and-tell unconfirmed) |
| Environment triage | 25 min | lab | Working setups pair with broken ones; Tyler + Marius float. Every failure and its fix gets logged into `INSTALL_TROUBLESHOOTING.md` on the spot. Checkpoints, in order: (1) venv activates, (2) `import numpy, pandas, matplotlib` succeeds, (3) Jupyter server opens in the browser |
| Run the notebook together | 15 min | lab | All together: `Run All` on `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb` — five checkpoints (interpreter/venv, core imports, compute & plot, repo layout, later-module preview). Checkpoint: every screen shows the summary cell with five ✅s. Each participant screenshots that summary — it is their `ASM-0` setup evidence (a JSON copy lands in `outputs/lsn-0.1/`) |
| Baseline self-rating | 5 min | exercise | In the same notebook's final cells: rate yourself 1–5 against all 21 basics outcomes (`OUT-0.1`–`OUT-3.5`, from the module specs); the cell validates and saves to `outputs/lsn-0.1/`. Said explicitly: not a filter — the baseline that measures the program's lift at graduation (per the enrollment gate) |

**Timing check:** 15 + 25 + 15 + 5 = 60 min = 1 h — matches the spreadsheet contract.

## Client Tie-In (Dorel's rule)

The program itself is the case: on 6MAP, AI engineers and delivery engineers talked past each other — the translation gap this cohort exists to close (GOAL-4). The walkthrough previews the three real cases that anchor the curriculum — the construction-site completion prospect (`LSN-1.6`), 6MAP (`LSN-3.6`), and the in-production meeting-RAG system (`LSN-3.6`) — so from minute one, every concept has a client conversation waiting for it.

## Homework — 75 min

| # | Task | Time | Artifact |
|---|---|---|---|
| 1 | Finish the session notebook solo if triage ate the live run: `Run All` to five ✅s, then screenshot the summary cell | 15 min | The `ASM-0` setup-evidence screenshot + `outputs/lsn-0.1/` JSON |
| 2 | Complete and submit the baseline self-rating (all 21 basics outcomes) if the last cells didn't get finished live, and write your one cadence question from pre-work task 1 into the channel | 10 min | Saved rating file + the posted question |
| 3 | **Python track, first tranche** — *not daily in Python:* work `notebooks/foundations/01_Beginning_Python.ipynb` as far as 50 min takes you (full completion, plus `02_Intermediate_Python.ipynb` as needed, is due before `LSN-1.4` — not tomorrow). *Daily in Python:* the corresponding sections of `03_Advanced_Python.ipynb` instead, same 50 min | 50 min | Executed notebook, all attempted cells run, submitted referencing LSN-0.1. Graded pass/fail on completion, not elegance |

**Time accounting:** pre-work 45 min + homework 75 min = 2 h out-of-session budget.

Task 3 is deliberately the module's shock absorber: it is the only MOD-0 homework not due the next morning, so on a heavy Tuesday evening (this homework plus `LSN-0.2`'s 30 min pre-work = 105 min) it is the piece that may slide to the weekend without breaking a session.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Environment setup guide | exists | `ACTIVATE_VENV.md` |
| Dependency list — staged by module | exists | `requirements.txt` (MOD-0) · `requirements-mod1.txt` (adds PyTorch for LSN-1.4) · `requirements-full.txt` (legacy, do not install) |
| Troubleshooting guide (living doc — updated during triage) | exists | `INSTALL_TROUBLESHOOTING.md` |
| Python foundations notebooks | exists | `notebooks/foundations/01_Beginning_Python.ipynb`, `02_Intermediate_Python.ipynb`, `03_Advanced_Python.ipynb` |
| **Session notebook** — 5 checkpoints + ASM-0 evidence + baseline self-rating, executed end to end | exists | `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb` |
| **Program walkthrough deck** — 10 slides w/ speaker notes, VSP design system (reveal.js) | exists | `program/lessons/decks/LSN-0.1-orientation.html` |
| Baseline self-rating form | exists | final cells of the session notebook (all 21 outcomes, saves to `outputs/lsn-0.1/`) |
| Supplement (optional pre-work reading only — the external corpus yields little for this lesson, by design) — third-wave framing, narrow vs general capability, and "be cautiously optimistic" as the program's posture | supplement | [`program/sources/README.md`](../sources/README.md) (Where the corpus turned out to be thin) |

## Delivery Notes

Not yet delivered — first run Tuesday 1 September 2026. Watch: does triage fit in 25 min for 10–12 machines (mixed macOS/Windows)? If not, that's a retro finding for the module spec. The 2026-08-03 rescope left this live session untouched (it was already a 1 h contract summing to 60 min), so the deck and notebook need no retiming — only the homework section grew, and homework task 1 is the deliberate overflow valve if triage runs past its 25 min.
