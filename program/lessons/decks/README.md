# decks/ — Session Decks

One reveal.js deck per built lesson. **Decks are the program's public-facing artifact** — the
rules below exist so a future build round doesn't silently break that.

## The anonymization rule (2026-08-03, user decision)

Decks may become public. **No specific clients, internal project names, or internal people's
names in deck text or speaker notes.** The lesson plans and module specs keep the real names —
they are internal working documents; the decks deliberately diverge from plan wording on names
only. When building or editing a deck from a plan, apply this standing mapping:

| Internal (plans/specs/notebooks) | Public (decks) |
|---|---|
| 6MAP | **Project Atlas** |
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
  clickable anchors styled with the deck's accent variable.

## Known issues (cosmetic overflow, pre-existing in accepted decks — measured 2026-08-03)

| Deck | Slides | Overflow |
|---|---|---|
| LSN-1.1 | s6 "Five jobs map", s8 "Jobs 4–5" | +11 / +16 px (footer pushed under the clip; likely the real source of the LL-44 report) |
| LSN-0.2 | s2, s8 | +14 / +9 px |
| LSN-0.3 | s7 | +5 px |
| LSN-0.4 | s4, s9 | +14 / +26 px |

LSN-1.3's LL-44 footer clip was fixed 2026-08-03. The rows above are unchanged from their
accepted baselines — fix in a dedicated cosmetic round before public release.
