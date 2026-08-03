---
name: LSN-3.6-real-vsp-cases
description: Walk three real VSP cases from client ask → triage → architecture → production questions, speaking both languages — the dry run for ASM-3's mock client conversation.
module: MOD-3
delivery_date: 2026-12-04
serves: OUT-3.5
duration: 1
prework_time: 15
homework_time: 105
owner: Tyler
status: draft
---

# LSN-3.6 — Real VSP Cases, End to End

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.5` |
| **Duration** | 1 h live + 2 h out-of-session (pre-work + homework) |
| **Format** | Live |
| **Verified by** | ASM-3 (conversation) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Friday, 4 December 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 2 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |
| **Note** | Double-header: LSN-3.5 and LSN-3.6 both run Friday, 4 December |

**Preserved recruiting note:** Vlad and Dorel were the intended facilitators — they own these cases and would play the client in character. The spreadsheet assigns Tyler as presenter (Vlad is reviewer; Dorel is not listed). **The ask stays open and matters more here than anywhere else in MOD-3:** an in-character case owner is what makes the session real, and `GAP-5` still hard-depends on Vlad/Dorel for the briefs — Tyler cannot substitute for them, because **no case fact may be invented.**

## Narrative

This is the basics tier's dress rehearsal before the final: nothing new is taught. Days before `ASM-3` (proposed week of Dec 7–11) and ten days before the **Phase-4 capstone (Dec 14–17, "Build an Agentic Harness that Scores Leads")**, everything the program installed — pillar triage (MOD-1), LLM patterns (MOD-2), agent and production literacy (MOD-3) — gets exercised on three pieces of real VSP work. Participants arrive carrying the two instruments the program built for them: the **pre-sales question bank (LSN-1.6)** and the **TL production question bank (LSN-3.5)** — and use them against a live "client" played by Vlad or Dorel. It kills the last misconception standing: that client-ready means knowing definitions. Dorel's rule, applied end to end; the same walk (ask → triage → architecture → production questions) is the spine of the ASM-3 mock client conversation the following week.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Re-read your three triage questions and pick the one case you feel least ready on | 10 | One written triage question per case |
| 2 | Have both banks to hand — LSN-1.6 pre-sales and the LSN-3.5 TL bank you received an hour ago | 5 | Both banks, printed or open |

**Pre-work total: 15 min — the module's thinnest, deliberately.** This is the second session of a Friday double-header, and its pre-work would otherwise land on the Thursday evening that already carries LSN-3.4's homework and LSN-3.5's pre-work. So the substantive part — **reading the three anonymized case briefs (`GAP-5`) and writing one triage question per case** — is folded into **LSN-3.4 homework task 4** (10 min, budgeted there). Nothing was dropped; it was paid for a day earlier out of a different budget.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Case 1 — Construction-site completion | 20 | drill + whiteboard | Same choreography each case: 3 min facilitator reads the ask **in character as the client**; 6 min group triage (questions only — facilitator answers in character); 8 min architecture convergence at the whiteboard, one participant holding the marker; 3 min production-question rapid fire + facilitator debrief. Facilitation guide below. |
| Case 2 — Meeting-RAG in production | 20 | drill + Q&A | Same choreography, with a twist: this system is **live in production**, so every production question has a real answer. Facilitator answers as the system's operator. Guide below. |
| Case 3 — 6MAP: the translation gap | 20 | discussion | Same choreography, but the "architecture" the group converges toward is an engagement architecture, not a system diagram. This is the program grading itself against its origin story. Guide below. |

**Timing check:** 20 + 20 + 20 = 60 min = 1 h — matches the spreadsheet contract. (Tight by design — the facilitator cuts triage, not debrief. Unchanged by the 2026-08-03 re-scope: this lesson was already a 1 h session.)

### Case 1 facilitation guide — construction-site completion (Dorel's prospect)

**The ask (as the client says it):** "We want to take a picture or a video of a construction site and have the system decide if it is done or not."

**Triage questions the group should surface** (pillar: **ML — vision**; job: **classification**, LSN-1.1):
- What does "done" mean — binary sign-off, or a checklist of milestones? Who decides today, and against what document?
- What labeled history exists — past site photos *with* their inspection outcomes? How many, how varied (angle, lighting, weather, site type)?
- Which error is expensive: calling an unfinished site "done" (false positive) or flagging a finished one (false negative)? → precision/recall framing, LSN-1.3.
- Photo or video? Phone or drone? Volume per week?

**Architecture the group should converge toward:** capture app → image preprocessing → vision model → confidence score → **human inspector queue for low-confidence calls** → inspector decisions feed back as labels. Two candidate model shapes to surface and weigh (LSN-2.5 tradeoff move): (a) fine-tuned classifier/detector against the completion checklist — needs labeled data, cheap per image; (b) multimodal LLM with a structured-output checklist (LSN-2.2) — near-zero data to prototype, costlier per image, harder to grade.

**Production questions that matter (LSN-3.5):** the eval set (historical inspections, held out); the gate metric (precision on "done"); cost per image at projected volume for the LLM route; site connectivity — on-device vs upload; liability — human sign-off stays in the loop, the model ranks the queue.

**Facilitator trap to spring:** someone will propose an agent. Replay LSN-3.1 drill D1: one decision, fixed steps — an AI ask is not an agent ask.

### Case 2 facilitation guide — meeting-RAG in production (the proof point)

**The setup:** Vlad's market read from the July 28 meeting — there's practically "nobody… who has done a RAG system and it's in production for meetings." VSP has one. The group's task: reconstruct it as if in pre-sales, then compare their sketch and questions against the real thing.

**Triage questions the group should surface** (pillar: **LLM**; pattern: **RAG**, LSN-2.4 — *not* fine-tuning, corpus changes daily, LSN-2.5):
- What's the corpus — transcripts, notes, action items? How fresh must answers be?
- Access control: who may query whose meetings? Where is that enforced?
- How are transcripts chunked — speaker turns? timestamps? Are citations required in answers?

**Architecture the group should converge toward:** meeting tool → transcript ingestion → chunking with speaker + timestamp metadata → embeddings → vector store → retrieval **with permission filtering at retrieval time, not generation time** → generation with citations → chat surface.

**Production questions that matter — the payoff of this case:** have the group fire the LSN-3.5 bank at the operator, in character: What is logged per query? What's the golden-question eval set and when does it run? What's the hallucination/citation policy? Cost per query? Usage and answer-acceptance KPIs? What actually broke in production and how did you find out?

**Debrief line:** production answers are specific numbers and dashboards, not adjectives. "We have one in production" beats any slide in a client conversation — but only if the person saying it can survive these questions. That is what OUT-3.5 means.

### Case 3 facilitation guide — 6MAP (the translation gap, the program's origin)

**The setup (not a client ask — the origin story):** Vlad, July 28: on 6MAP, "on one side, you and Stefana would speak a language, and on the other side these guys would speak another language, and stuff would be lost in translation. You need to close this gap." This program exists because of this case.

**Triage questions the group should surface:** Where exactly did translation break — pre-sales scoping, architecture review, or delivery handoff? What questions were never asked, and by whom? Which items from Vlad's list — observability, reliability, KPIs, hardware requirements, cost — surfaced late, and what did the lateness cost?

**"Architecture" the group should converge toward** (an engagement architecture — checkpoints where both languages must meet):
1. **Pre-sales:** the LSN-1.6 question bank + data-requirements checklist run *before* commitment.
2. **Design:** eval plan and KPIs agreed *before* build (LSN-3.5) — both sides sign the same success definition.
3. **Delivery:** one observability dashboard both the AI engineer and the delivery TL read.

**Group exercise (the heart of the segment):** from the brief, identify one concrete moment where a question from either bank would have changed the outcome — then answer "how would this cohort run 6MAP now?"

**Debrief line:** this case is the program grading itself. If the room can do this walk unprompted, GOAL-4 is met and ASM-3's conversation is a formality.

## Client Tie-In (Dorel's rule)

This lesson **is** the client tie-in for MOD-3 — all three cases are real VSP work, sourced from the July 28, 2026 meeting: Dorel's construction-site prospect, the in-production meeting-RAG system, and 6MAP. Nothing hypothetical appears in this session.

## Homework

MOD-3 is the last taught module of the basics tier, but **not the end of the program** — `ASM-3` and then the Dec 14–17 Phase-4 capstone follow. So the spreadsheet's 2 h out-of-session budget converts the old "none — final week" into the on-ramp for both. All of it lands on the weekend of 5–6 Dec, when no session competes for the time.

| # | Task | Time | Due | Artifact |
|---|---|---|---|---|
| 1 | Pick **one** of the three cases and write the full walk as a one-page pre-sales brief: the ask as the client said it → triage (pillar, job) → architecture sketch → the top five production questions you'd ask, with why each one matters here. **No invented facts** — anything not in the brief or the session is written as an open question, not an assumption | 45 | Sun 6 Dec | One-page brief, references `LSN-3.6` |
| 2 | **`ASM-3` rehearsal.** Pair up and run a 15-min mock client conversation each way on a case you did *not* write up — partner plays the client from the brief only. Afterwards each of you records the three questions you wish you'd asked | 30 | Sun 6 Dec | Three questions each, plus your partner's name |
| 3 | Read the Phase-4 capstone brief ("Build an Agentic Harness that Scores Leads", Dec 14–17) and write which of your MOD-3 artifacts you carry in — agent, traces, eval check, question banks — and which gap you most need to close first | 15 | Sun 6 Dec | Half-page carry-in note |
| 4 | Re-rate yourself 1–5 against `OUT-3.1`–`OUT-3.5` and compare with your LSN-0.1 baseline. Not a filter — the program measuring its own lift | 15 | Sun 6 Dec | Ratings + one line on the biggest delta |

**Time accounting:** pre-work 15 min + homework 105 min = 2 h out-of-session budget.

The walk practiced here (ask → triage → architecture → production questions) is the spine of the `ASM-3` mock client conversation; task 2 rehearses it directly, and participants should bring both question banks to the final.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Case briefs ×3 (anonymized, one page each) | build (`GAP-5`) | Vlad + Dorel input — request at the next curriculum review. **Needed by Thu 3 Dec, one day earlier than the session:** the briefs are now pre-read as LSN-3.4 homework task 4, so they must **stand alone at ~1 page with no facilitator preamble.** **Untouchable rule: no invented case facts** — if a fact cannot be sourced from Vlad/Dorel or `meetings/2026-07-28-ml-discussion/transcript.md`, it is not written. **Fallback:** the session is runnable from a one-paragraph sourced brief per case using the guides above, and a case runs shorter rather than fuller |
| Facilitation guides | exists | This file, Session Plan section |
| Pre-sales question bank | exists | Participant-owned artifact from LSN-1.6 |
| TL production question bank | build (`GAP-4`) | Delivered in LSN-3.5 **the same morning** — hard dependency, and the tightest one in the module: the bank must be handout-ready, not draft, by Fri 4 Dec |
| Phase-4 capstone brief (homework task 3) | exists (skeleton) | `program/modules/module-4-capstone.md` — configuration is locked (Dec 14–17, 5 h/day, no pre-work/homework), the rest is a provisional skeleton awaiting its own planning round. Only the title and dates are needed for the carry-in note; if the full brief slips, task 3 falls back to "name your carry-in artifacts" alone |
| Whiteboard or shared canvas | exists | Room logistics; one marker-holder per case, rotate |

## Delivery Notes

None yet — first delivery Fri 4 Dec 2026, **second hour of a double-header** and the last taught session of the basics tier. Fill after delivery: what landed, what dragged, timing reality (the 20-min-per-case budget is the known risk). Two double-header risks to record: whether the room still has energy for three case drills after LSN-3.5, and whether the case briefs were actually pre-read given Thursday's load — if not, case 1 loses its triage segment. Feeds the module retro.
