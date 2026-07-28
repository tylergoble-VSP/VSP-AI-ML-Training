---
name: LSN-2.2-prompting-as-engineering
description: Prompt deliberately — system prompts, few-shot, chain-of-thought, structured JSON outputs — and explain non-determinism to a client.
module: MOD-2
serves: OUT-2.2
duration: 1.5 h
prework_time: 30
owner: Tyler
status: draft
---

# LSN-2.2 — Prompting as Engineering

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.2 |
| **Duration** | 1.5 h session + 30 min pre-work |
| **Format** | Live lab |
| **Verified by** | ASM-2 (quiz + artifact) |

## Narrative

From "typing questions" to engineering. The misconception to kill: prompting is vibes. The capability to install: prompts are interfaces with anatomy (system vs user), techniques (few-shot, chain-of-thought), and contracts (structured JSON you can build on) — and their outputs are stochastic, which is a property to engineer around, not a defect (callback to LSN-0.4). Ends with the on-ramp to tool use that MOD-3 runs with.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Run prompts P1–P5 (below) against any LLM you have access to, exactly as written | ~25 min | Saved outputs for all five |
| 2 | For each prompt, write one line: what (if anything) surprised you | ~5 min | The five lines |

**P1 — role framing.** Run: `Explain what a context window is.` Then, in a fresh chat: `You are briefing a construction-company CFO with no technical background. Explain what a context window is and why it limits what an AI assistant can "remember" about their project documents. Three sentences max.` Compare.

**P2 — stochasticity (LSN-0.4 callback).** Run this twice, in two fresh chats: `List the five biggest risks of putting an AI chatbot in front of our customers, ranked most to least severe.` Diff the two rankings.

**P3 — few-shot.** Run: `Classify this support ticket's urgency as LOW, MEDIUM, or HIGH: "The invoicing screen shows last month's totals but finance already closed the books."` Then re-run with these examples prepended: `Ticket: "Whole warehouse is offline, nothing scans." -> HIGH` / `Ticket: "Please add a user for our intern starting next month." -> LOW` / `Ticket: "Report export takes 10 minutes, used to take 1." -> MEDIUM`. Compare labels and how much explanation the model volunteers.

**P4 — chain-of-thought.** Run: `A crew of 6 works 8-hour shifts. Safety rules require 1 supervisor per 4 workers on site at all times. Shifts overlap 30 minutes for handover. How many supervisor-hours are needed to cover two consecutive shifts? Answer with a number only.` Then re-run with the last sentence replaced by `Work through it step by step, then give the number.` Is either answer actually right?

**P5 — structured output.** Run: `Extract this email into JSON with keys: requester, site, equipment_id, issue, requested_action, deadline. Email: "Hi — Dave again from the Northgate site. that excavator (unit EX-241? or maybe 214, check with Priya) is leaking hydraulic fluid again, second time this month. need someone out before Thursday or we lose the pour window. thx"` Is the JSON valid? What did it do with the uncertain equipment ID?

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Anatomy of a prompt | 15 min | talk + demo | System vs user roles: in a product, you own the system prompt, the user owns the user turn, the model guarantees nothing. P1/P2 debrief: role framing changes register; temperature explains the P2 diff (LSN-0.4). |
| Few-shot and chain-of-thought | 25 min | demo + discussion | P3/P4 debrief on screen. Theory from `generative_ai/05` sections "What is Chain-of-Thought?" and "Self-Consistency": when CoT buys accuracy (multi-step reasoning) and when it just burns tokens. |
| Structured outputs — live lab | 30 min | lab | From `generative_ai/05` "Implementation": everyone prompts against the messy site-incident document (below). Checkpoints: (1) valid JSON, (2) correct fields, (3) three consecutive runs stable, with uncertain values as `null` — not invented. |
| Failure gallery + the client conversation | 20 min | demo + discussion | Three failure patterns (below). How to say "same input can give different output" to a client without losing the room. Close: tool-calling teaser from `generative_ai/06` "What is Tool Calling?" — the bridge MOD-3 crosses. |

**Timing check:** 15 + 25 + 30 + 20 = 90 min = 1.5 h ✓

**Lab document (messy on purpose):** a forwarded email chain, "FW: FW: northgate issues w/e 07/24" — inconsistent date formats (`7/24`, `24th`, `next Thu`), the reporter's name spelled two ways, two candidate equipment IDs, an ambiguous near-injury mention ("Marius nearly caught his hand"), and a deadline buried in the last line. Target schema: `{site, report_date, reporter, incidents: [{type, equipment_id, severity, injury}], delay_days, followup_owner, followup_deadline}`.

**Failure gallery — three real patterns:**
1. **Format drift under pressure.** The JSON prompt that worked all lab suddenly prepends "Here is the JSON you requested:" or wraps output in markdown fences when the input gets longer — the downstream parser dies. Fixes: "output only JSON, no prose", schema-first prompting, validate-and-retry.
2. **The "are you sure?" flip.** The model extracts `EX-241` correctly; challenged with "are you sure? I think it's EX-214", it agrees — against the document. Confidence tracks the conversation, not the truth (sets up 2.6).
3. **Few-shot bleed.** A value from your few-shot examples ("Northgate") appears in the output for a document about a different site — the model pattern-matched the examples, not the input. Fixes: neutral placeholder examples, clear delimiters between examples and input.

## Client Tie-In (Dorel's rule)

The lab document is the construction-site prospect's actual data shape: field reports written on phones, half-remembered IDs, deadlines in prose. "We can extract structured data from your site emails" is a sellable sentence only if the engineer saying it has personally fought format drift and the are-you-sure flip — and can explain, calmly, why run-to-run variation exists and how it's engineered around (validation, retries, evals).

## Homework

**Artifact (graded, submit referencing LSN-2.2):** build a prompt that reliably extracts structured fields from a messy document — the lab document or an equally messy one of your own (anonymized). Submit the prompt + outputs from 3 separate runs. Grading standard: valid JSON on all three runs; fields correct; missing or uncertain data represented explicitly (`null` / `"unknown"`), never invented. Feeds ASM-2.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Chain-of-thought notebook (sections: "What is Chain-of-Thought?", "Self-Consistency", "Implementation") | exists | notebooks/generative_ai/05_GenerativeAI_ChainOfThought_Reasoning.ipynb |
| Tool-calling teaser (section: "What is Tool Calling?") | exists | notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb |
| Pre-work prompt sheet (P1–P5, as above) | build (light — copy from this plan) | program/materials/ — to create |
| Messy site-incident lab document | build (light — write from spec above) | program/materials/ — to create |

## Delivery Notes

Not yet delivered. Record here: which failure pattern reproduced live, lab checkpoint pass rates, timing reality. Feeds the MOD-2 retro.
