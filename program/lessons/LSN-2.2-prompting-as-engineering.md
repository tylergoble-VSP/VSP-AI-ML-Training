---
name: LSN-2.2-prompting-as-engineering
description: Prompt deliberately — system prompts, few-shot, chain-of-thought, structured JSON outputs — and explain non-determinism to a client.
module: MOD-2
delivery_date: 2026-10-26
serves: OUT-2.2
duration: 1
prework_time: 110
homework_time: 130
owner: Tyler
status: draft
---

# LSN-2.2 — Prompting as Engineering

## Contract (from module spec — do not edit here)

| Field | Value |
|---|---|
| **Serves** | OUT-2.2 |
| **Duration** | 1 h live + 4 h out-of-session (pre-work + homework) |
| **Format** | Live lab |
| **Verified by** | ASM-2 (quiz + artifact) |

## Schedule (program spreadsheet, locked 2026-08-03)

| Field | Value |
|---|---|
| **Delivery date** | Monday, 26 October 2026 |
| **Live session** | 1 h |
| **Out-of-session budget** | 4 h total (pre-work + homework) |
| **Presenter** | Tyler |
| **Reviewer** | Vlad |
| **Guinea pig** | Mazilu (TBC) |

## Narrative

From "typing questions" to engineering. The misconception to kill: prompting is vibes. The capability to install: prompts are interfaces with anatomy (system vs user), techniques (few-shot, chain-of-thought), and contracts (structured JSON you can build on) — and their outputs are stochastic, which is a property to engineer around, not a defect (callback to LSN-0.4). Ends with the on-ramp to tool use that MOD-3 runs with.

## Pre-work (mandatory — no pre-work, no seat)

| # | Task | Time | Artifact to bring |
|---|---|---|---|
| 1 | Run prompts P1–P5 (below) against any LLM you have access to, exactly as written. **Then run the escalation ladder (below P5): one question, six versions, each changing exactly one thing, output re-read at every step.** Five independent samples show you that prompts differ; a controlled sequence shows you *which change bought what*, which is the difference between the lesson's title and its thesis | 25 min | Saved outputs for all five, plus the six escalation outputs |
| 2 | For each prompt, write one line: what (if anything) surprised you. For the escalation ladder, write one line per step: **what did this change buy?** | 5 min | The five lines + six one-liners |
| 3 | **Read and run** `notebooks/generative_ai/05_GenerativeAI_ChainOfThought_Reasoning.ipynb` — sections "What is Chain-of-Thought?", "Self-Consistency", and execute the "Implementation" cells once end-to-end. *(Relocated out of the live hour: this theory used to be taught on screen in segments 2–3.)* | 45 min | Your executed notebook + one line on where CoT changed the output and where it just burned tokens |
| 4 | **Self-consistency mini-experiment.** Run P4 five times in fresh chats at default temperature. Majority-vote the numeric answers. Is the majority answer actually correct? | 20 min | Five answers, the vote, and your verdict |
| 5 | Read `notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb` — section "What is Tool Calling?" only. *(Relocated: this was the live closing teaser; reading it beforehand means the session can spend its last minute pointing at MOD-3 rather than explaining it.)* | 15 min | One sentence: what a tool call is, in client-safe language |

**Time accounting (pre-work):** 25 + 5 + 45 + 20 + 15 = 110 min.

**P1 — role framing.** Run: `Explain what a context window is.` Then, in a fresh chat: `You are briefing a construction-company CFO with no technical background. Explain what a context window is and why it limits what an AI assistant can "remember" about their project documents. Three sentences max.` Compare.

**P2 — stochasticity (LSN-0.4 callback).** Run this twice, in two fresh chats: `List the five biggest risks of putting an AI chatbot in front of our customers, ranked most to least severe.` Diff the two rankings.

**P3 — few-shot.** Run: `Classify this support ticket's urgency as LOW, MEDIUM, or HIGH: "The invoicing screen shows last month's totals but finance already closed the books."` Then re-run with these examples prepended: `Ticket: "Whole warehouse is offline, nothing scans." -> HIGH` / `Ticket: "Please add a user for our intern starting next month." -> LOW` / `Ticket: "Report export takes 10 minutes, used to take 1." -> MEDIUM`. Compare labels and how much explanation the model volunteers.

**P4 — chain-of-thought.** Run: `A crew of 6 works 8-hour shifts. Safety rules require 1 supervisor per 4 workers on site at all times. Shifts overlap 30 minutes for handover. How many supervisor-hours are needed to cover two consecutive shifts? Answer with a number only.` Then re-run with the last sentence replaced by `Work through it step by step, then give the number.` Is either answer actually right?

**P5 — structured output.** Run: `Extract this email into JSON with keys: requester, site, equipment_id, issue, requested_action, deadline. Email: "Hi — Dave again from the Northgate site. that excavator (unit EX-241? or maybe 214, check with Priya) is leaking hydraulic fluid again, second time this month. need someone out before Thursday or we lose the pour window. thx"` Is the JSON valid? What did it do with the uncertain equipment ID?

**The escalation ladder — one question, six versions, one change each.** Run these in order, in fresh chats, and read the output every time. *(Added 2026-08-11 inside pre-work task 1's existing 25 min — see `SUP-9` §3.)*

1. `Delivery risk is…` — bare and ambiguous; it will still answer something
2. `For a fixed-price software project, delivery risk is…` — **added context**
3. `Concisely define delivery risk for a fixed-price software project.` — **made it an instruction, and constrained length**
4. `Concisely define delivery risk for a fixed-price software project. Answer in JSON.` — **constrained format**
5. `Concisely define delivery risk for a fixed-price software project. Answer in JSON. Only provide the JSON.` — **forbade the preamble**
6. `You are a delivery manager writing for a client steering committee. Concisely define delivery risk for a fixed-price software project.` — **added a role**

Step 5 is the one to watch: *"only provide the JSON"* is one clause, and it is the whole difference between output you can parse and output you have to clean — which is the argument segment 3 then makes with code. Step 6 usually shifts register more than content, which is its own lesson about what a role prompt actually buys.

## Session Plan

| Segment | Time | Method | Detail |
|---|---|---|---|
| Anatomy of a prompt | 10 min | talk + demo | System vs user roles: in a product, you own the system prompt, the user owns the user turn, the model guarantees nothing. P1/P2 debrief: role framing changes register; temperature explains the P2 diff (LSN-0.4). |
| Few-shot and chain-of-thought | 15 min | debrief + discussion | P3/P4 debrief on screen, plus the pre-work self-consistency votes collected and compared across the room — a live sample of how often the majority answer is right. Theory was read in pre-work; here we only settle the judgment call: when CoT buys accuracy and when it just burns tokens. |
| Structured outputs — live lab | 20 min | lab | Everyone prompts against the messy site-incident document (below). Checkpoints: (1) valid JSON, (2) correct fields, (3) uncertain values as `null` — not invented. Stability across runs is homework; in the room we only need one clean pass each. |
| Failure gallery + the client conversation | 15 min | demo + discussion | Three failure patterns (below) — demoed live, because seeing format drift break a parser in real time is what makes it stick. How to say "same input can give different output" to a client without losing the room. One-line close pointing at MOD-3 tool calling (already read in pre-work task 5). |

**Timing check:** 10 + 15 + 20 + 15 = 60 min = 1 h — matches the spreadsheet contract.

**What moved out of the live hour (1.5 h → 1 h):** CoT/self-consistency theory → pre-work task 3 (read *and* run, so participants arrive having executed it rather than watched it); the three-consecutive-runs stability requirement → homework task 1, expanded to five runs; the tool-calling teaser → pre-work task 5. Nothing was dropped.

**Lab document (messy on purpose):** a forwarded email chain, "FW: FW: northgate issues w/e 07/24" — inconsistent date formats (`7/24`, `24th`, `next Thu`), the reporter's name spelled two ways, two candidate equipment IDs, an ambiguous near-injury mention ("Marius nearly caught his hand"), and a deadline buried in the last line. Target schema: `{site, report_date, reporter, incidents: [{type, equipment_id, severity, injury}], delay_days, followup_owner, followup_deadline}`.

**Failure gallery — three real patterns:**
1. **Format drift under pressure.** The JSON prompt that worked all lab suddenly prepends "Here is the JSON you requested:" or wraps output in markdown fences when the input gets longer — the downstream parser dies. Fixes: "output only JSON, no prose", schema-first prompting, validate-and-retry.
2. **The "are you sure?" flip.** The model extracts `EX-241` correctly; challenged with "are you sure? I think it's EX-214", it agrees — against the document. Confidence tracks the conversation, not the truth (sets up 2.6).
3. **Few-shot bleed.** A value from your few-shot examples ("Northgate") appears in the output for a document about a different site — the model pattern-matched the examples, not the input. Fixes: neutral placeholder examples, clear delimiters between examples and input.

## Client Tie-In (Dorel's rule)

The lab document is the construction-site prospect's actual data shape: field reports written on phones, half-remembered IDs, deadlines in prose. "We can extract structured data from your site emails" is a sellable sentence only if the engineer saying it has personally fought format drift and the are-you-sure flip — and can explain, calmly, why run-to-run variation exists and how it's engineered around (validation, retries, evals).

## Homework

| # | Task | Time | Deliverable |
|---|---|---|---|
| 1 | **The graded artifact.** Build a prompt that reliably extracts structured fields from a messy document — the lab document or an equally messy one of your own (anonymized). Write it schema-first: state the target schema in the prompt before asking for anything. Run it **5** separate times (was 3 — the bigger budget buys a real stability sample). *Grading standard:* valid JSON on all five runs; fields correct; missing or uncertain data represented explicitly (`null` / `"unknown"`), never invented | 60 min | Prompt + five raw outputs + a pass/fail line per run |
| 2 | **Harden it against format drift** (failure pattern 1). Add a validate-and-retry step — parse the output, and on failure re-prompt with the parser error — then re-run against an input roughly twice as long. Document what broke before the retry loop and whether length alone triggered the drift | 30 min | Before/after outputs + 3–4 sentences on what the retry actually fixed |
| 3 | **Few-shot bleed test** (failure pattern 3). Replace your few-shot examples with neutral placeholders (`Site X`, `EQ-000`), then run on a document about a *different* site. Did the bleed disappear? | 25 min | The two outputs side by side + your verdict |
| 4 | Write the **client sentence on non-determinism**: ≤3 sentences explaining to a non-technical buyer why the same input can produce different output, and what you do about it. It must name a mechanism (validation, retries, evals), not just reassure | 15 min | The sentences, submitted referencing `LSN-2.2` |

Task 1 feeds ASM-2. Task 4's sentence is reused in LSN-2.6's expectation-setting drill.

**Time accounting:** pre-work 110 min + homework 130 min = 4 h out-of-session budget.

## Materials

| Material | Status | Path / source |
|---|---|---|
| Chain-of-thought notebook (sections: "What is Chain-of-Thought?", "Self-Consistency", "Implementation") | exists — **note:** now assigned as runnable pre-work, not shown live, so confirm at delivery prep that its cells execute standalone in the participant environment | notebooks/generative_ai/05_GenerativeAI_ChainOfThought_Reasoning.ipynb |
| Tool-calling teaser (section: "What is Tool Calling?") | exists | notebooks/generative_ai/06_GenerativeAI_Tool_Calling_Agents.ipynb |
| Pre-work prompt sheet (P1–P5, as above) | build (light — copy from this plan) | program/materials/ — to create |
| Messy site-incident lab document | build (light — write from spec above) | program/materials/ — to create |
| Second, longer messy document for the drift test (homework task 2) | build (light — new, supports relocated stability work) | program/materials/ — to create |
| Supplement — inference settings, prompt component checklists, the five-step escalation drill (candidate pre-work swap), the six-technique ladder with cost column | supplement | [`program/sources/SUP-9-prompt-and-inference-controls.md`](../sources/SUP-9-prompt-and-inference-controls.md) |

## Delivery Notes

Not yet delivered. Record here: which failure pattern reproduced live, lab checkpoint pass rates, timing reality. Feeds the MOD-2 retro.
