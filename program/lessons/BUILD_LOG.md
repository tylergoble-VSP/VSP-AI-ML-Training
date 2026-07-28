# Build Log & Lessons Learned — Session Artifact Builds

Structured record of every notebook/deck build round: what was built, what the review found, and what
each finding taught us. **Builder agents must read and follow every Standing Instruction (SI-n) below
before writing anything.** Reviewers append findings (LL-n) after each round and promote recurring ones
into new Standing Instructions — this file is how each build gets smarter than the last.

**Process per lesson:** builder agent (Opus 5) builds notebook + deck per the lesson-plan contract →
reviewer (Fable 5) independently re-executes, recomputes the math, and audits against the contract →
substantive fixes go back to the builder; findings are recorded here → artifacts commit only after review.

---

## Standing Instructions for builder agents

### Environment & execution
- **SI-1** — Use the repo `.venv` (Python 3.12; core stack only: numpy, pandas, matplotlib, seaborn + Jupyter tooling). MOD-0 notebooks must not import anything heavier (no sklearn/torch/transformers) — heavy libs arrive in Week 2 and aren't installed.
- **SI-2** — Execute the notebook end to end before handing off: `.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/lessons/<file>.ipynb`. Hand off the *executed* notebook (outputs visible) and state that it executed cleanly.
- **SI-3** — Seed all randomness (`rng = np.random.default_rng(42)`) so committed outputs are reproducible and re-runs don't churn diffs.
- **SI-4** — Per-participant artifacts (evidence files, homework saves) write to `outputs/lsn-<id>/` — gitignored via `outputs/lsn-*/`. Never commit personal artifacts; delete any your test run creates outside that path.
- **SI-5** — Locate the repo root by walking up (see LSN-0.1 notebook "Checkpoint 4" / `src/utils/pathing.py`). Never hardcode absolute paths inside a notebook.
- **SI-6** — Verify every file path you reference actually exists (`ls` it) — module specs have had filename drift before; the real file wins, and a wrong citation is a review reject.

### Notebook house style (exemplar: `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb`)
- **SI-7** — Open with a lesson-metadata markdown table (lesson ID, module, serves, verified-by, lesson-plan path) and a "how to run this" paragraph.
- **SI-8** — Comment imports with a one-line purpose (repo convention); markdown-heavy explanations between code cells; friendly `[PASS]/[FAIL]/[TODO]`-style prints for anything checkable.
- **SI-9** — The notebook mirrors the lesson plan's structure: pre-work section(s) → session segments in order → homework section. Every drill from the lesson plan appears **with its exact specified numbers and scenarios** — no substituting generic examples for the plan's scripted ones.
- **SI-10** — Charts use the VSP palette (`#59709c` navy-light, `#65a74e` green, `#ffe86b` yellow, `#97f377` green-lightest), labeled axes, `ax.spines[["top","right"]].set_visible(False)`, `plt.tight_layout()`.
- **SI-11** — Fill-in/homework cells must never raise when unfilled: validate-and-instruct (see LSN-0.1's self-rating cell). A fresh `Run All` of the whole notebook must complete with zero errors.

### Decks (exemplar: `program/lessons/decks/LSN-0.1-orientation.html`)
- **SI-12** — Copy the design system verbatim from the **LSN-0.1 deck**, not `index.html` — index.html references a missing `vsp-logo-white.svg`; use the `.vsp-wordmark` text mark instead.
- **SI-13** — reveal.js 5.1.0 via CDN, 1280×720, same `Reveal.initialize` config; every slide carries `<aside class="notes">` speaker notes with timing cues; slide flow maps to the lesson plan's session segments and the stated minutes must sum to the contract duration.
- **SI-14** — Deck content uses the lesson plan's concrete drill numbers and scenarios, not filler; house idiom: kicker → H2 with one `vsp-glow` phrase → cards/callout; footer carries lesson ID + segment map.

### Specs & bookkeeping
- **SI-15** — The lesson plan is the contract. If the build reveals a contract problem (timing that can't work, a wrong path, a factual error), do **not** edit specs or lesson plans — build to the contract where sane, deviate only where broken, and **report every discrepancy** in your handoff. Spec-first fixes happen at review.
- **SI-16** — (Reviewer) After acceptance: update the lesson plan's Materials table + the module spec's support-material line, record findings below, commit per lesson. Artifact homes: notebooks → `notebooks/lessons/`, decks → `program/lessons/decks/` — one combined notebook per lesson (pre-work + session + homework), regardless of what older Materials tables say.

### Added after Round 1
- **SI-17** — Pre-compute every scripted statistic in a scratch script **before** embedding it in a notebook or deck, and cross-check against the notebook's own printed output. Lesson-plan numbers are not automatically achievable — two of LSN-0.2's were arithmetically impossible as written. Where the plan's number is unreachable, build the closest honest construction and report it (SI-15).
- **SI-18** — Graded stats cells must tolerate legitimate convention differences: accept both variance conventions (ddof=0 and ddof=1), use numeric tolerances rather than exact equality, and require substance (e.g., minimum length) for free-text answers — never exact strings.
- **SI-19** — Render-verify everything visual: execute and *look at* every figure (redesign illegible panels — log-scale wide-tailed axes, fix label collisions); render decks headless at 1280×720 and check for overflow/clipping before handoff.

---

## Build log

### Round 0 — LSN-0.1 (baseline, built directly by Fable 5) — 2026-07-28

**Artifacts:** `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb` (executed, 5/5 checkpoints) · `program/lessons/decks/LSN-0.1-orientation.html` (10 slides). Committed `98cacae`.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-1 | environment | `.venv` did not exist despite `ACTIVATE_VENV.md` claiming it was created — environment docs can lie; verify before trusting | Created `.venv` (uv, py3.12, core stack) | SI-1 |
| LL-2 | environment | Full `requirements.txt` (torch, llama-cpp, bitsandbytes) is heavy and failure-prone; MOD-0 needs none of it | Core-subset venv; notebook probes heavy libs informationally | SI-1 |
| LL-3 | design | `vsp-logo-white.svg` referenced by `index.html` is missing from the repo — broken image in the style exemplar | Text wordmark in decks | SI-12 |
| LL-4 | process | Repo had no `.gitignore`; venv + per-participant artifacts would pollute status | Added `.gitignore`; `outputs/lsn-*/` ignored | SI-4 |
| LL-5 | content | Lesson plan said self-rating covers "OUT-0.1–OUT-3.4" but specs define through OUT-3.5 — building artifacts surfaces spec typos | Fixed plan at review; notebook carries all 21 outcomes | SI-15 |
| LL-6 | content | Module specs had cited shortened notebook filenames that don't exist on disk (earlier round) | Paths verified against `ls` in all artifacts | SI-6 |

### Round 1 — LSN-0.2 (builder: Opus 5, agent a3c8508385f765066) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-0.2_Statistics_1_Distributions_Sampling_Variance.ipynb` (37 cells, 8 figures, executed clean — independently re-executed by reviewer) · `program/lessons/decks/LSN-0.2-statistics-1.html` (10 slides, notes on all, segment minutes sum to 90).

**Review verification:** independent re-execution clean; drill math recomputed (1,000/920/80 → 92% exact; $208k mean; latency mixture hits p50 180 / mean 240 / p99 2.1 s within tolerance asserts); SI compliance checked programmatically (imports, 9 seeded rngs, palette, outputs path, CSS core byte-contained, only CDN externals, 10/10 slides with timed notes). No fix round needed.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-7 | content | Two of the lesson plan's scripted statistics were arithmetically impossible ($80k→$210k unreachable with the stated inputs → real answer $208k; p50/mean/p99 triple unreachable with a single log-normal → needs a fast/slow-path mixture). Plan authors wrote numbers nobody had computed | Builder built honest constructions and reported; reviewer fixed the plan | SI-17 |
| LL-8 | content | Plan self-contradicted on sample sizes (title n=30 vs 30,000; detail n=30 vs 3,000) | Notebook builds all three; plan detail fixed to match | SI-17 |
| LL-9 | content | numpy (ddof=0) vs pandas (ddof=1) variance disagree (78.75 vs 81.29 on the homework set) — an exact-match grader would mark a correct answer wrong | Checker accepts both + teaches the gotcha | SI-18 |
| LL-10 | design | Two figures were illegible as first designed (linear axis crushed by a p99-wide tail; bar labels colliding with a reference line) — only caught by *looking* at rendered output | Redesigned (log-x panel; layout fix); deck headless-rendered at 1280×720 | SI-19 |
| LL-11 | process | Materials tables written before artifact-location conventions existed pointed to wrong homes (`notebooks/foundations/`, `program/`) | Reviewer updates tables at acceptance; homes codified | SI-16 |
| LL-12 | content | Builder's unprompted good moves worth keeping: second-vendor comparison (accuracy ranks two models backwards — sets up LSN-1.3 without teaching it), gamma instead of normal for cycle times (normals go negative), per-cell seeded generators (single-cell re-runs can't drift), survivorship bait planted in the homework dataset for task 4b | Kept; patterns noted for future stats lessons | — |

### Round 2 — LSN-0.3 (builder: Opus 5) — *pending*

### Round 3 — LSN-0.4 (builder: Opus 5) — *pending*
