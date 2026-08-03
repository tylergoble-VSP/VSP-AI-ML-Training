# decks/ — Session Decks

One reveal.js deck per built lesson. **Decks are the program's public-facing artifact** — the
rules below exist so a future build round doesn't silently break that.

## The anonymization rule (2026-08-03, user decision)

Decks may become public. **No specific clients, internal project names, or internal people's
names in deck text or speaker notes.** The lesson plans and module specs keep the real names —
they are internal working documents; the decks deliberately diverge from plan wording on names
only. When building or editing a deck from a plan, apply this standing mapping:

**Project Atlas is more than an alias (Tyler's decision, 2026-08-03):** it is the program's
*fictional running client case study* — a made-up client whose engagement threads through the
entire training (triage → data → RAG → agent → production, run end to end in LSN-3.6). Teach
anything real-but-unnameable through the Atlas storyline. A real client, prospect, or engagement
name must never appear in a deck, even anonymized-sounding ones.

| Internal (plans/specs/notebooks) | Public (decks) |
|---|---|
| 6MAP | **Project Atlas** (folded into the running case study) |
| Andrei Ciobanu / "the Ciobanu failure" | "a previous training attempt" (no name) |
| Vlad | the program sponsor |
| Dorel / "Dorel's rule" | one of our directors / "the director's rule" |
| Marius | the program manager |
| Stefana | the co-instructor |
| Mazilu / guinea-pig mentions | the pilot participant, or omit (internal process) |
| Tyler | the instructor |
| Any client/prospect/engagement name | generic description or bracketed placeholder |

Quoted lines stay **verbatim** — only attributions change to roles. Keeps: VSP / Victory Square
Partners branding; public authors and products (Karpathy, 3Blue1Brown, StatQuest / Josh Starmer,
Tyler Vigen, PyTorch, cloud vendor names); fictional IDs shared with notebooks (e.g. `SUP-2291`).
The **notebooks are NOT yet anonymized** — they still carry the internal names.

## Build rules (carried from the accepted-round conventions + the 2026-08-03 re-scope)

- **Timing:** speaker notes open with "N min"; per-deck live timings must sum to **60**
  (the locked 1 h contract). Footer agenda strings and segment kickers must match the
  lesson plan's Session Plan table.
- **CSS core:** the shared `<style>` block is review-verified — never modify it; style via
  existing classes and inline styles on content elements only.
- **720 px:** every slide must fit 720 px height (`overflow:hidden` clips silently). Measure
  headless before accepting; harness variance is real (~5–20 px between methods), so target
  ≥30 px headroom.
- **Links:** only verified URLs (see the 2026-08-03 link-verification pass); YouTube titles are
  clickable anchors styled with the deck's accent variable. Any document a participant needs
  (repo, setup guides, notebooks, SCHEDULE.md) gets a clickable GitHub link — repo URL
  `https://github.com/tylergoble-VSP/VSP-AI-ML-Training`, `blob/main/...` paths. LSN-0.1
  carries the program-wide reference slide (appendix, 0 min) with every link; keep it current.
- **Bullets over paragraphs (Tyler's feedback, LSN-0.1 round):** card and callout body copy
  should be scannable `p-chk` bullets, not prose paragraphs. Single-line `p-callout` punch
  lines are fine as-is.

## Known issues (cosmetic overflow, pre-existing in accepted decks — measured 2026-08-03)

| Deck | Slides | Overflow |
|---|---|---|
| LSN-1.1 | s6 "Five jobs map", s8 "Jobs 4–5" | +11 / +16 px (footer pushed under the clip; likely the real source of the LL-44 report) |
| LSN-0.2 | s2, s8 | +14 / +9 px |
| LSN-0.3 | s7 | +5 px |
| LSN-0.4 | s4, s9 | +14 / +26 px |

LSN-1.3's LL-44 footer clip was fixed 2026-08-03. The rows above are unchanged from their
accepted baselines — fix in a dedicated cosmetic round before public release.
