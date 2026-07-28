---
name: LSN-1.1-five-ml-jobs-nesting-doll
description: Triage any client "AI" ask into one of the five ML jobs — classify, cluster, regress, propensity, recommend — or correctly call it a generative-AI ask, and place it on the ML ⊃ deep learning ⊃ generative AI nesting doll.
module: MOD-1
serves: OUT-1.1
duration: 1 h
prework_time: 30
owner: Tyler Goble
status: draft
---

# LSN-1.1 — The Five ML Jobs & the Nesting Doll

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-1.1` |
| **Duration** | 1 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-1 (quiz + mock pre-sales conversation) |

## Narrative

Kills the misconception that "AI" means one thing — clients use the word for both predictive ML and ChatGPT, and the two lead to completely different projects, data needs, and prices. Installs the triage skill: sort any ask into sort-it (classify), group-it (cluster), guess-a-number (regress), give-the-odds (propensity), pick-the-next-move (recommend) — or route it out of ML entirely ("that's an LLM ask — Module 2"). Connects back to LSN-0.4 (every ML answer is probabilistic) and forward: LSN-1.2 asks what each job's model takes in and kicks out, and LSN-1.6 returns to the construction-site ask worked as the demo here.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the ML literacy deck (see PROGRAM_PLAN.md §8) through the five-jobs section | 20 min | Nothing to submit — quizzed cold in the drill |
| 2 | Write down one real "AI" ask from a project or client you've been on, plus your guess at which job it is | 10 min | The ask + your guess, one or two sentences |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| "When they say AI…" | 15 min | talk + worked example | The two meanings of "AI" and the tells: "I want to *know/predict* X" → ML; "I want it to *converse/write/reason*" → LLM. The nesting doll: ML ⊃ deep learning ⊃ generative AI. Instructor works one ask live: the construction-site prospect ("tell us from drone photos whether each milestone is done") → classification per milestone; the "% complete" variant → regression. Same client, two jobs. |
| The five jobs | 25 min | talk | Each job gets its one-line definition, the sales-world example from the deck (buyer conversion → sort; deal size → regress; close odds → propensity; next best action → recommend; account segments → cluster), and its tell-phrase to listen for in a client's mouth. Deck sections shown as-is; no math. |
| Triage drill | 20 min | drill | Six scenarios (below) sorted live by the group — instructor plays the client and pushes back. Then participants' own pre-work asks, triaged rapid-fire by a different participant than the one who brought it. |

**Timing check:** 15 + 25 + 20 = 60 min = 1 h contract duration. ✓

### Triage drill scenarios

| # | The client says… | Answer key |
|---|---|---|
| 1 | Logistics client: "We have three years of delivery records. Can AI tell us the odds a given shipment arrives late, so dispatch can intervene early?" | Propensity — "give the odds" of an event per shipment. (If they only wanted a late/on-time flag, it collapses to classification — the tell is *odds* + *intervene*.) |
| 2 | Retail client: "We have 40,000 customers. Group them into meaningful segments so marketing can target each differently." | Clustering — no labels exist; the model invents the groups, humans name them. |
| 3 | SaaS client: "Support gets 800 tickets a day. Route each one to the right team automatically." | Classification — fixed set of known buckets, historical tickets are already labeled by which team resolved them. |
| 4 | CFO: "Forecast next quarter's cloud spend from usage history." | Regression — guess a number, in dollars. |
| 5 | Field-services client: "Given the job description, tell the technician which spare parts to load on the truck." | Recommender — rank the next-best items from co-occurrence in past jobs. |
| 6 | Ops director: "We want a chatbot that answers staff questions from our 500-page policy manual." | **Not ML — it's an LLM/RAG ask.** No prediction target, no labels; they want retrieval + conversation. Route to Module 2; think of VSP's meeting-RAG system, not a classifier. |

Reserve (if the group is fast): "Can AI draft our proposals from past winning bids?" → generative AI, not one of the five jobs — the second "this isn't ML" tell.

## Client Tie-In (Dorel's rule)

The worked example is the real construction-site completion prospect (photo/video milestone detection) — triaged lightly here, walked in full in LSN-1.6. The drill scenarios are delivery-company-shaped pre-sales asks, and scenario 6 mirrors the in-production meeting-RAG system so the "this isn't ML" call lands on something VSP actually built.

## Homework

None — feeds into LSN-1.2 pre-work. Keep your triaged ask; LSN-1.2 asks what that model would take in and kick out.

## Materials

| Material | Status | Path / source |
|---|---|---|
| ML literacy deck (five-jobs + nesting-doll sections) | exists | ML literacy deck (see PROGRAM_PLAN.md §8) — not in repo |
| Triage drill scenarios + answer key | exists | This plan (above) |
| Participants' pre-work asks | exists | Collected at session start |

## Delivery Notes

To be filled after first delivery: what landed, what dragged, timing reality. Feeds the MOD-1 retro.
