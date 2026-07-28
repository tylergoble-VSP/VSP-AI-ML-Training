---
name: LSN-3.6-real-vsp-cases
description: Walk three real VSP cases from client ask → triage → architecture → production questions, speaking both languages — the dry run for ASM-3's mock client conversation.
module: MOD-3
serves: OUT-3.5
duration: 1
prework_time: 30
owner: Vlad + Dorel + Tyler
status: draft
---

# LSN-3.6 — Real VSP Cases, End to End

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | `OUT-3.5` |
| **Duration** | 1 h session + 30 min pre-work |
| **Format** | Live |
| **Verified by** | ASM-3 (conversation) |

## Narrative

This is the basics tier's capstone-before-the-final: nothing new is taught. One week before ASM-3, everything the program installed — pillar triage (MOD-1), LLM patterns (MOD-2), agent and production literacy (MOD-3) — gets exercised on three pieces of real VSP work. Participants arrive carrying the two instruments the program built for them: the **pre-sales question bank (LSN-1.6)** and the **TL production question bank (LSN-3.5)** — and use them against a live "client" played by Vlad or Dorel. It kills the last misconception standing: that client-ready means knowing definitions. Dorel's rule, applied end to end; the same walk (ask → triage → architecture → production questions) is the spine of the ASM-3 mock client conversation the following week.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Read the three anonymized case briefs (GAP-5, from Vlad/Dorel) | 20 | One written triage question per case |
| 2 | Refresh your LSN-1.6 pre-sales question bank and LSN-3.5 TL question bank | 10 | Both banks, printed or open |

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Case 1 — Construction-site completion | 20 | drill + whiteboard | Same choreography each case: 3 min facilitator reads the ask **in character as the client**; 6 min group triage (questions only — facilitator answers in character); 8 min architecture convergence at the whiteboard, one participant holding the marker; 3 min production-question rapid fire + facilitator debrief. Facilitation guide below. |
| Case 2 — Meeting-RAG in production | 20 | drill + Q&A | Same choreography, with a twist: this system is **live in production**, so every production question has a real answer. Facilitator answers as the system's operator. Guide below. |
| Case 3 — 6MAP: the translation gap | 20 | discussion | Same choreography, but the "architecture" the group converges toward is an engagement architecture, not a system diagram. This is the program grading itself against its origin story. Guide below. |

**Timing check:** 20 + 20 + 20 = **60 min** = 1 h contract duration. ✓ (Tight by design — the facilitator cuts triage, not debrief.)

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

None — final week. The walk practiced here (ask → triage → architecture → production questions) is the spine of the ASM-3 mock client conversation; participants should bring both question banks to the final.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Case briefs ×3 (anonymized, one page each) | build (`GAP-5`) | Vlad + Dorel input — request at the July 30 curriculum review. **Fallback:** the session is runnable from a one-paragraph brief per case using the guides above; source quotes in `meetings/2026-07-28-ml-discussion/transcript.md` |
| Facilitation guides | exists | This file, Session Plan section |
| Pre-sales question bank | exists after Week 2 | Participant-owned artifact from LSN-1.6 |
| TL production question bank | build (`GAP-4`) | Delivered in LSN-3.5, earlier in Week 4 — hard dependency |
| Whiteboard or shared canvas | exists | Room logistics; one marker-holder per case, rotate |

## Delivery Notes

None yet — first delivery scheduled Week 4, final week before ASM-3. Fill after delivery: what landed, what dragged, timing reality (the 20-min-per-case budget is the known risk). Feeds the module retro.
