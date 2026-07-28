---
name: LSN-0.1-orientation-environment-setup
description: Understand the program's contract and leave with Python + Jupyter running a notebook end to end on your own machine.
module: MOD-0
serves: OUT-0.1
duration: 1 h
prework_time: 45
owner: Tyler + Marius
status: draft
---

# LSN-0.1 — Orientation & Environment Setup

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-0.1` |
| **Duration** | 1 h session + 45 min pre-work |
| **Format** | Live, hands-on |
| **Verified by** | `ASM-0` (setup evidence: screenshot of executed notebook) |

## Narrative

This session is the program's contract made physical: everyone hears why pre-work is enforced (the Ciobanu failure — no intentional prior work, 90% of the audience lost in the first 20%) and everyone leaves with a running notebook, because nobody gets to spend Week 2 fighting their environment instead of learning. It kills the assumption that this is another watch-and-forget training, and it installs the one capability everything else stands on: a local Python + Jupyter setup that executes end to end. Sets up `LSN-0.2` (which opens in a notebook) and the `LSN-1.4` MNIST lab; the baseline self-rating taken here is the yardstick the whole program is measured against at graduation.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read `program/README.md` and the **Ceremonies** + **Enrollment Gate** sections of `program/program-spec.md` | 10 min | One written question or concern about the cadence (pre-work → session → homework → checkpoint) |
| 2 | Clone the `VSP-AI-ML-Training` repo | 5 min | Local clone path |
| 3 | Create the virtualenv and install dependencies per `ACTIVATE_VENV.md` + `requirements.txt` | 15 min | Terminal output: activated venv prompt + `python --version` + clean `pip install` finish (or the failure output) |
| 4 | If step 3 failed: work through `INSTALL_TROUBLESHOOTING.md` | 10 min | The exact error message, copied as text — this is a valid pre-work artifact; broken setups get fixed live |
| 5 | Launch Jupyter and open `notebooks/foundations/01_Beginning_Python.ipynb`; run the first cell if you can | 5 min | Screenshot of the open notebook (executed cell if it worked) |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Program walkthrough | 15 min | talk | Three pillars (ML / LLM / agentic) × three tiers (basics 1 mo / advanced 3 mo / expert 6 mo); why agentic is the lion's share and ML is ~5%; the cadence and the pre-work rule with the Ciobanu story told straight; checkpoint gates `ASM-0`–`ASM-3` and the GOAL-7 deal: do the work or you're out; hackathon graduation Dec 14–18 |
| Environment triage | 25 min | lab | Working setups pair with broken ones; Tyler + Marius float. Every failure and its fix gets logged into `INSTALL_TROUBLESHOOTING.md` on the spot. Checkpoints, in order: (1) venv activates, (2) `import numpy, pandas, matplotlib` succeeds, (3) Jupyter server opens in the browser |
| Run the notebook together | 15 min | lab | All together: open `notebooks/foundations/01_Beginning_Python.ipynb` and execute the opening cells (variables, printing, list operations). Checkpoint: every screen shows executed cell output. Each participant captures the screenshot that becomes their `ASM-0` setup evidence |
| Baseline self-rating | 5 min | exercise | Rate yourself 1–5 against every basics outcome (`OUT-0.1`–`OUT-3.4`, from the module specs) in the shared form. Said explicitly: not a filter — the baseline that measures the program's lift at graduation (per the enrollment gate) |

**Timing check:** 15 + 25 + 15 + 5 = 60 min = 1 h contract duration.

## Client Tie-In (Dorel's rule)

The program itself is the case: on 6MAP, AI engineers and delivery engineers talked past each other — the translation gap this cohort exists to close (GOAL-4). The walkthrough previews the three real cases that anchor the curriculum — the construction-site completion prospect (`LSN-1.6`), 6MAP (`LSN-3.6`), and the in-production meeting-RAG system (`LSN-3.6`) — so from minute one, every concept has a client conversation waiting for it.

## Homework

Participants who don't work in Python daily: complete `notebooks/foundations/01_Beginning_Python.ipynb` end to end (and `02_Intermediate_Python.ipynb` as needed) before `LSN-1.4`. Artifact: the executed notebook, all cells run, submitted referencing LSN-0.1. Graded pass/fail on completion, not elegance. Daily-Python participants: none.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Environment setup guide | exists | `ACTIVATE_VENV.md` |
| Dependency list | exists | `requirements.txt` |
| Troubleshooting guide (living doc — updated during triage) | exists | `INSTALL_TROUBLESHOOTING.md` |
| Python foundations notebooks | exists | `notebooks/foundations/01_Beginning_Python.ipynb`, `02_Intermediate_Python.ipynb`, `03_Advanced_Python.ipynb` |
| Program walkthrough deck (~10 slides) | adapt | from `program/program-spec.md` + `program/PROGRAM_PLAN.md` |
| Baseline self-rating form | adapt | outcome tables in `program/modules/module-0` through `module-3` |

## Delivery Notes

Not yet delivered — first run Week 1. Watch: does triage fit in 25 min for 10–12 machines (mixed macOS/Windows)? If not, that's a retro finding for the module spec.
