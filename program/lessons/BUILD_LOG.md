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
- **SI-3** — Seed all randomness (`rng = np.random.default_rng(42)`) so committed outputs are reproducible and re-runs don't churn diffs. When a lesson must *show* run-to-run variation, derive the "runs" from distinct child seeds of one pinned parent (`np.random.SeedSequence(parent).spawn(n)`) — real variation across simulated runs, byte-identical output across executions — and tell participants the trick (production systems pin seeds for the same reason).
- **SI-4** — Per-participant artifacts (evidence files, homework saves) write to `outputs/lsn-<id>/` — gitignored via `outputs/lsn-*/`. Never commit personal artifacts; delete any your test run creates outside that path.
- **SI-5** — Locate the repo root by walking up (see LSN-0.1 notebook "Checkpoint 4" / `src/utils/pathing.py`). Never hardcode absolute paths inside a notebook.
- **SI-6** — Verify every file path you reference actually exists (`ls` it) — module specs have had filename drift before; the real file wins, and a wrong citation is a review reject.

### Notebook house style (exemplar: `notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb`)
- **SI-7** — Open with a lesson-metadata markdown table (lesson ID, module, serves, verified-by, lesson-plan path) and a "how to run this" paragraph.
- **SI-8** — Comment imports with a one-line purpose (repo convention); markdown-heavy explanations between code cells; friendly `[PASS]/[FAIL]/[TODO]`-style prints for anything checkable.
- **SI-9** — The notebook mirrors the lesson plan's structure: pre-work section(s) → session segments in order → homework section. Every drill from the lesson plan appears **with its exact specified numbers and scenarios** — no substituting generic examples for the plan's scripted ones.
- **SI-10** — Charts use the VSP palette (`#59709c` navy-light, `#65a74e` green, `#ffe86b` yellow, `#97f377` green-lightest), labeled axes, `ax.spines[["top","right"]].set_visible(False)`, `plt.tight_layout()`. **Read `SI-30` before choosing which two palette entries encode which two categories — `yellow` and `mint` are the same colour to a viewer with protanopia.**
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
- **SI-18** — Graded stats cells must tolerate legitimate convention differences: accept both variance conventions (ddof=0 and ddof=1), use numeric tolerances rather than exact equality, and require substance (40–60 char minimum) for free-text answers — never exact strings. When the true numeric answer could collide with a convention or a misconception (e.g., 0.98% true vs 0.99 misconception, percent vs fraction), ask for a second, unit-free representation ("1 real alert per N") that cannot be confused.
- **SI-19** — Render-verify everything visual: execute and *look at* every figure (redesign illegible panels — log-scale wide-tailed axes, fix label collisions); render decks headless at 1280×720 and check for overflow/clipping before handoff.

### Added after Round 2
- **SI-20** — Exit-code-clean is not content-correct. After generating a notebook, verify its *mass*: expected file size, output/figure counts, and spot-read a cell — a generator bug once produced a notebook that executed "cleanly" because every cell had collapsed to a single comment line.
- **SI-21** — Drill reveals should decompose, not gotcha: give the scripted effect a real (small) true value the honest method recovers, so the debrief ends on "measuring this properly makes the client money" rather than "your feature is worthless." (Pattern from LSN-0.3's revenue drill: +18% observed = +14.6% seasonality + 3% real effect; the simulated holdout finds the 3%.)

### Added after Round 3
- **SI-22** — Prove reproducibility, don't assert it: after executing, re-execute a copy and compare output blocks byte-for-byte (including PNG byte lengths). Byte-identical re-runs are the actual SI-3 acceptance test.
- **SI-23** — 720 px is the law; slide counts are guidance. If a slide overflows at 1280×720, split it — never shrink content into illegibility to hit a target count. Any eval-shaped number in a plan or artifact (test-set size + pass bar) gets a sizing sanity check: compute P(false fail) at plausible true quality before shipping it.

### Added for the MOD-1 cycle (Rounds 4–9)
- **SI-24** — MOD-1 environment policy (supersedes SI-1's "core only" for MOD-1 lessons): the venv now also carries **scikit-learn 1.9, torch 2.13, torchvision 0.28** (Apple MPS available). Rules: (a) still no transformers/LLM libraries — those arrive in MOD-2; (b) datasets cache OUTSIDE the repo at `~/.cache/vsp-training-data` (MNIST train+test already pre-downloaded there — use `datasets.MNIST(root=Path.home()/".cache"/"vsp-training-data", download=True)`); never write datasets into the repo; (c) bound per-cell runtime — training cells must finish in well under 5 minutes on CPU/MPS (subset the data or cap epochs), and execute with `--ExecutePreprocessor.timeout=600`; state expected runtime in *markdown* and never print measured wall-clock — variable timings break SI-22 byte-identity (LL-24); (d) `torch.manual_seed` + `numpy` seeding both required (SI-3 applies to torch too); note that bit-identical torch outputs across machines are NOT guaranteed — keep SI-22's byte-comparison for numpy/prints, and use tolerance asserts for torch numbers.
- **SI-25** — MOD-1 lessons 1.1–1.3 lean on Tyler's original "ML literacy deck," which is NOT in the repo (LL-21 precedent). The session deck you build IS the canonical deck for the lesson: carry the needed content yourself, cite the original as source, and report the workaround. Do not block on the missing file.

### Added after Round 6
- **SI-26** — Three trust rules learned the hard way: (a) **read what you cite** — open every referenced notebook and confirm it contains what its name implies (`12_Analytics_Performance` = runtime timing, not model metrics; LL-32); (b) **no pandas `DataFrame.style` in committed notebooks** — Styler output embeds a random uuid + memory address and silently breaks SI-22 byte-identity (LL-33); (c) **test graders with planted answers** (good / deliberately thin / wrong) before shipping — reading the probe list is not enough (LL-35, LL-30's substring traps).

### Added after Round 7 (torch-lab practices)
- **SI-27** — Torch labs: (a) pin `device="cpu"` for committed runs (deterministic; MPS is a curiosity beat); (b) **re-pin `loader.generator.manual_seed(SEED)` at `train()` entry** — a DataLoader's generator is consumed by every `iter()`, so a peeked batch silently changes the shuffle (LL-37); (c) never write an expected accuracy/metric into a plan or checkpoint without training the actual config (LL-38 — the plan's "≥95%" was unreachable); (d) offline fallback = synthetic data + a `DATA_IS_REAL` flag that skips data-pinned asserts, keeping Run All clean without faking results; (e) tolerance asserts for all trained numbers, exact asserts only for counts and hand-matched matrix math.

### Added after Round 9
- **SI-29** — Advisory graders (LSN-1.5's drill advisor, LSN-1.6's bank pre-check) are pre-checks, never gates: saving/submitting is gated only on substance minimums (SI-18), the advisor verdict is recorded as metadata, and the notebook must disclose the advisor's limits in print (what beats it, what it under-scores). Verdict text must name the missing cue family with an actionable remedy, because cue lexicons under-score legitimate paraphrase (LL-48) and the real grader is the human checkpoint (ASM-1).

### Added after the supplement-integration pass (2026-08-11)
- **SI-30** — Colour never carries a distinction alone. (a) **`yellow` `#ffe86b` and `mint` `#97f377` must never be the only thing separating two categories in one view** — measured CIEDE2000 distance 1.7 under protanopia and 5.5 under deuteranopia (i.e. the same colour), and only 0.08 apart in greyscale, so it fails on screen *and* in print. Pair `yellow` with `navy` or `green` instead; `mint` is safe against everything except `yellow`. Every other pair in the seven-colour palette scores ≥10 worst-case, so **the palette is fine and this is one rule, not a redesign**. (b) More generally, any distinction that matters gets a second encoding — position, marker shape, line style, a direct label, or the printed value. The exemplar is `LSN-1.4`'s confusion matrix (cell 32): it runs a ramp *through* the unsafe pair but prints the count in every cell, so the colour is redundant and the flattening costs nothing. (c) A conjunction of two channels is not pre-attentive — if a reader has to find "the yellow circles" among yellow squares and navy circles, that is a serial search, and in a 60-minute session it is a slide nobody reads. One channel per question.
- **SI-30 (tooling)** — Re-run `scripts/check_palette_accessibility.py` (repo `.venv`, stdlib + numpy only) whenever a palette colour is added or changed. It simulates protanopia / deuteranopia / tritanopia, reports pairwise CIEDE2000 distances and greyscale separation, and names any pair that falls below the usable threshold. Twenty minutes of measurement beat a redesign argument — the 2026-08-11 run found the palette sound and exactly one pair unusable.
- **SI-32** — Diff the working tree against `HEAD` before you edit an executed notebook, and rebuild from `HEAD` if the working copy has been stripped. A notebook can lose every output and several cell ids without erroring, without looking wrong, and without anyone noticing (`LL-55`). `git diff --stat` on a notebook is not enough — compare output and figure counts.
- **SI-31** — Cite the primary source, not the secondary one that showed it to you. Several supplement items (Anscombe's quartet, Tukey's box-plot fences, Tufte's chart principles, ColorBrewer) reached us through a teaching kit licensed non-commercially, but each is a citable primary source we can build from directly. Check whether the thing you want is the intermediary's own work before you inherit its licence — see `program/sources/README.md`, Licensing.

### Added after Round 8
- **SI-28** — Notebook naming + warning hygiene: (a) never use `_`-prefixed cross-cell variables — `_i`, `_`, `__`, `_ih` are IPython-reserved input/output-history names, so a cross-cell `_i` silently becomes the *previous cell's source text* (LL-41; plain-Python execution cannot reproduce it — name cross-cell values in CAPS); (b) any warning emitted during execution is an SI-22 byte-identity hazard — warning *text* can embed PIDs and ipykernel temp paths (`tight_layout` over a gridspec containing a `twinx` axes does, LL-42); fix the cause (explicit margins), never just suppress the display.

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

### Round 2 — LSN-0.3 (builder: Opus 5, agent a3679d7909cb9b3fd) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-0.3_Statistics_2_Probability_Correlation_Causation.ipynb` (34 cells, 7 figures, executed clean — independently re-executed by reviewer) · `program/lessons/decks/LSN-0.3-statistics-2.html` (10 slides, timed notes, minutes sum to 90).

**Review verification:** independent re-execution clean; fraud construction recomputed against the plan (100/99/9,999/10,098 → 0.98%, plus the 99.0%-accuracy callback to LSN-0.2); homework Q3 arithmetic verified (98/1,497/1,595 → 6.1%); threshold-sweep model pinned by in-cell asserts to exactly 1% FPR / 99% sensitivity; trap-3 wobble and weekly/monthly reconciliation honestly disclosed in-notebook; SI sweep clean (imports, 7 seeded rngs, palette, CSS core identical, CDN-only externals, 10/10 timed notes). Builder applied Round-1 patterns (LL-12) unprompted. No fix round needed.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-13 | process | **Silent no-op notebook:** a generator bug (splitting sources without newlines) collapsed every code cell to one comment line — the notebook executed "cleanly" with zero errors and zero outputs. Caught only via file-size anomaly (69 KB vs ~800 KB expected) | Builder caught + rebuilt; mass-verification codified | SI-20 |
| LL-14 | content | Units trap in graded numerics: true answer 0.98% collides with the 99% misconception when a field accepts both percent and fraction — no single number disambiguates | Dual representation: percent + "1 real alert per N" (102) | SI-18 (extended) |
| LL-15 | content | Drill design upgrade: giving the widget a real +3% effect (not zero) turns the reveal from gotcha into attribution, and the simulated holdout *recovers* the true number — better pre-sales pedagogy | Kept; codified | SI-21 |
| LL-16 | content | Weekly and monthly revenue series came from separate generators, so cross-views only approximately reconcile — builder disclosed it in the cell output rather than hiding it | Accepted with disclosure; prefer one generator for related views next time | note |
| LL-17 | process | Plan quality improving upstream: LSN-0.3's scripted numbers were all internally consistent (verified independently by builder and reviewer) — the SI-17 discipline is working at authoring time too | — | — |

### Round 3 — LSN-0.4 (builder: Opus 5, agent a85f00f4f6e920d68) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-0.4_Deterministic_Probabilistic_Stochastic.ipynb` (31 cells, 4 figures, executed clean; byte-identical independent re-run) · `program/lessons/decks/LSN-0.4-deterministic-probabilistic-stochastic.html` (10 slides, timed notes sum to 60).

**Review verification:** independent re-execution clean; acceptance-test arithmetic recomputed exactly (P(fail | true 92%, n=50, bar 45) = 20.8%; at 95% true quality 3.8%; ~470 questions for a reliable bar); float-tie wording honest ("two mathematically tied candidates"); deck compliance clean (shared CSS core, keywords slide as pre-work target, SUP-2291 case, Box quote, CDN-only externals). Builder resolved both pre-briefed tensions well and self-caught two rendering defects. No fix round needed.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-18 | process | Builder proved SI-3 by re-executing a copy and byte-comparing all 26 output blocks — a stronger acceptance test than "runs clean," and it caught nothing this time precisely because the SeedSequence pattern works | Codified as the standard reproducibility check | SI-22 |
| LL-19 | content | The plan's own example acceptance criterion ("≥90% of a 50-question test set") is statistically fragile — a genuinely-92% system fails it 1 run in 5. Eval-shaped numbers need sizing checks at authoring time, same as scripted stats (LL-7) | Builder built AND priced the plan's numbers; reviewer added the sizing parenthetical to the plan | SI-23 |
| LL-20 | design | A slide carrying pins + arithmetic together overflowed 720 px; the honest fix was splitting it (10 slides vs the prompt's 7–9), not shrinking | Split accepted | SI-23 |
| LL-21 | process | The ML literacy deck (LSN-0.4's pre-work target) still isn't in the repo — Round-0 gap finally canonicalized: deck slide 2 + notebook pre-work section now carry the keywords and the plan points there | Plan Materials + pre-work rows updated | — |
| LL-22 | design | reveal.js nav arrows overlay the footer's right-hand text on all four decks — cosmetic, consistent, left as house pattern; revisit only if a presenter complains | noted | — |
| LL-23 | content | Keeper patterns this round: the overconfident-twin scorer (identical decisions, 9.6-point confidence lie — the cleanest OUT-0.2 vehicle yet); pre-briefing known tensions in the builder prompt produced the round's best design work (SeedSequence resolution) rather than a discrepancy report | Tension pre-briefing adopted as orchestration practice | — |

---

## Round summary (Rounds 0–3 complete — all four MOD-0 lessons built)

Four lessons, four decks, four executed notebooks, zero fix rounds needed after Round 0's conventions were codified.
The compounding worked: Round 1 surfaced arithmetic-defect and render-verification lessons (SI-17/18/19); Round 2
executed those flawlessly and added content-mass + reveal-design lessons (SI-20/21); Round 3 executed *those*
flawlessly and added reproducibility-proof + eval-sizing lessons (SI-22/23). Each builder independently applied the
prior rounds' LL patterns unprompted. Next builds (MOD-1: LSN-1.1–1.6, incl. the GAP-8 MNIST lab) start from SI-1..23.

---

## MOD-1 cycle (Rounds 4–9) — LSN-1.1 through LSN-1.6

Environment prepped 2026-07-28: sklearn/torch/torchvision installed, MNIST pre-cached (see SI-24). Known
dependencies going in: LSN-1.6's case brief is `GAP-5` (Vlad/Dorel input) — build the runnable structure, mark the
brief dependency; LSN-1.4 is `GAP-8` (a synthesis, not an adaptation — see Round 1 of the lesson-plan builds).

### Round 4 — LSN-1.1 (builder: Opus 5, agent add410c2e98dd3016) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-1.1_Five_ML_Jobs_Nesting_Doll.ipynb` (28 cells, 5 figures, executed clean; builder proved byte-identical re-run) · `program/lessons/decks/LSN-1.1-five-ml-jobs.html` (10 slides, timed notes 15/25/20 = 60).

**Review verification:** independent re-execution clean; all 7 drill scenarios (6 + reserve) confirmed verbatim in notebook AND deck; answer key audited against the plan's key (all six match; builder's DEFENSIBLE-tier extensions on scenarios 1 and 5 accepted as pedagogically sound); no LLM libs imported (string hits were a compliance comment + diagram label); deck CSS core identical, CDN-only, 10/10 timed notes. Builder self-caught two figure defects and one prose-vs-computed-number drift. No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-24 | process | SI-24(c)'s "state the wall-clock" collides with SI-22 byte-identity for fast cells: printed timings vary run to run. Builder's resolution: stable `[PASS] fit finished in well under a second` text; measured timings never printed | Codified: expected runtime goes in *markdown*; never print measured wall-clock | SI-24 (amended) |
| LL-25 | process | **Reviewer-side defect:** the review battery's verbatim check used a greedy quote regex that matched across markdown table cells → false 0/13 alarm on scenarios that were in fact verbatim. Cost one investigation loop | Battery fixed: verbatim checks extract exact scenario strings and compare whitespace-normalized | reviewer battery |
| LL-26 | content | Keeper patterns: three-verdict drill grading (MATCH / DEFENSIBLE / MISS, each with prose reasons — richer than right/wrong and matches how triage really works); the fourth dashed nesting-doll ring ("also sold as AI: rule engines · RPA · dashboards") ; teaching a genuine tie (construction "% complete" → classify *or* regress) instead of hiding it | Kept as house patterns | — |
| LL-27 | content | Discussion-lesson notebooks (vs labs/checkpoint lessons) need no checkpoint battery — companion + drill workspace is the right shape. First non-checkpoint notebook in the series establishes the template | Shape noted for LSN-1.2/1.5 (also discussion-shaped) | — |

### Round 5 — LSN-1.2 (builder: Opus 5, agent ae91d1ecb64eb6dea) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-1.2_Model_IO.ipynb` (32 cells, 3 figures, 6 pinning asserts — `#4127 → 0.73` etc. fail loudly if numbers drift) · `program/lessons/decks/LSN-1.2-model-io.html` (10 slides, timed notes 15/30/15 = 60).

**Review verification:** independent in-repo re-execution → zero reproducibility mismatches (concatenated-stream comparison); drill scenario + both curveballs verbatim in notebook and deck; scripted numbers (0.73/0.51/0.31/$29,375) present in executed outputs; no mlxtend import (string hit is the disclosed go-deeper caveat); deck CSS core identical, CDN-only, 10/10 timed notes. Plan's "rendered, not run live" safari design superseded by live tiny fits — spec updated. No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-28 | process | Jupyter may split one cell's stdout into different `stream`-block boundaries across runs (transport artifact) — block-by-block comparison can false-alarm on identical output | SI-22 comparisons (builder + reviewer battery) now compare *concatenated* stream text per cell | SI-22 (practice) |
| LL-29 | environment | Repo notebooks cited as go-deeper references can import libraries the venv lacks (`unsupervised/07` needs `mlxtend`) — a citation is a dependency claim | Builder computed the same support/confidence/lift in pandas; citation carries the caveat; check cited notebooks' imports before pointing at them | SI-6 (practice) |
| LL-30 | content | Keeper patterns: one coherent dataset world across the whole lesson (`#30xx` closed history / `#41xx` open pipeline — no deal both trains and predicts); reverse-engineering a few rows to land the plan's scripted numbers, *disclosed in the setup markdown*; grader keyword probes need word-boundary matching ("lose"⊂"close", "bet"⊂"better" false-positives found in testing) | Kept as house patterns | — |
| LL-31 | process | Reviewer-side: notebooks that walk up to find the repo root cannot execute from the scratchpad — re-execution copies must live inside the repo (builder had already worked inside the repo for the same reason) | Battery uses in-repo hidden temp copies | reviewer battery |

### Round 6 — LSN-1.3 (builder: Opus 5, agent a4e107fe039cabb2e) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-1.3_Grading_Models.ipynb` (38 cells, 3 figures, 44 pinning asserts) · `program/lessons/decks/LSN-1.3-grading-models.html` (11 slides, timed notes sum to 90).

**Review verification:** independent in-repo re-execution → zero mismatches (rich-output comparison incl. HTML block lengths); all three report cards recomputed by hand (A: 92,160 h / 2,400 = 38.4; B: 99.26% accuracy / 75% precision / 11.25% recall / 99.20% flag-nothing baseline; C: matrix sums to 4,000, 62.03%/78.06%); fraud continuity with LSN-0.3 pinned by asserts (same 100/99/9,999/10,098 → 0.98%); AUC concave-ROC bounds verified by hull geometry (0.8378–0.9770 through the operating point); the plan's `foundations/12` citation confirmed wrong (timing notebook, no ROC) and `foundations/06` confirmed right. No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-32 | content | **Name-based citation error in the plan:** `12_Analytics_Performance.ipynb` sounds like model metrics but is a runtime-timing notebook (3 cells, no ROC). Planning rounds cited it by name without reading it; the real ROC/AUC content lives in `06_Classifier_Algorithms.ipynb` | Citations fixed in plan + module spec; "read what you cite" now explicit | SI-26 |
| LL-33 | process | pandas `DataFrame.style` stamps a random uuid into HTML and a live memory address into text/plain — three tables silently broke SI-22 byte-identity | Styler banned in committed notebooks (plain-DataFrame `show()` helper instead) | SI-26 |
| LL-34 | content | Card C's reported AUC 0.88 is **not reachable** from a standard bi-normal scorer at the stated precision/recall (that gives 0.924) — builder turned the impossibility into a *feasibility check*: quoted AUC must lie within the concave-ROC bounds implied by the quoted precision/recall (0.8378–0.9770). A genuinely new pre-sales tool: "is the vendor's metrics triple even internally consistent?" | Kept; presented as "reported, not simulated" — honest | — |
| LL-35 | process | Grader probes with overlapping patterns (`recall*` and `recall`) double-counted one word, promoting thin answers to MATCH — found by *testing* the grader with planted answers, not by reading it | `probe_spans()` counts distinct matched words; in-notebook self-tests; graders must be tested with planted good/thin/wrong answers | SI-26 |
| LL-36 | content | Keeper beats: the rubber-stamp comparison (a 99.0%-accurate detector is *worse* than a 99.99% do-nothing stamp); per-segment MAE decomposition (38 h headline hides 330 h epic misses, 85.9% of error in 10% of items) | Kept as house patterns | — |

### Round 7 — LSN-1.4 (builder: Opus 5, agent aa07a8eed94d3cfe2) — 2026-07-28 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-1.4_Hands_On_Train_MNIST.ipynb` (55 cells, 6 figures, 52 asserts, 11 trained models, **~6 s total runtime**) · `program/lessons/decks/LSN-1.4-hands-on-mnist.html` (11 slides, runbook surface — checkpoints/failures/recoveries in the notes — timed to 150).

**Review verification:** independent re-execution in 7.6 s wall → zero mismatches; key numbers confirmed in outputs (lab model 92.77% test / full-60k 97.04% / degradation 23.88→53.38→84.23→92.77 / forward-pass hand-match 0.00e+00); CPU pinned, 12 seed calls, torchvision cache used (fetch_openml superseded), no Styler; deck CSS core identical, CDN-only, checkpoint/failure/recovery vocabulary present in notes. GAP-8 closed. No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-37 | process | **DataLoader shuffle hazard:** a loader's `generator` is consumed by every `iter()` — displaying one batch before training silently changes the shuffle and every downstream number (723 → 786 errors). Load-bearing fix: `train()` re-pins `loader.generator.manual_seed(SEED)` at entry | Fixed + documented in-notebook | SI-27 |
| LL-38 | content | The plan's "expect ≥95%" lab checkpoint is **unreachable at the plan's own config** (784-128-10 / 3 epochs / 10k → 92.77%; 36-config sweep confirmed). Model-performance expectations in plans are eval-shaped numbers (LL-19 generalized): never write an expected accuracy without training the actual config | Honest resolution: full-60k run (97.04%) meets the bar and *becomes* the break-it thesis; plan wording fixed | SI-27 |
| LL-39 | content | Keeper beats: equal-compute control (same gradient steps, small data → 75.63% — "you cannot buy your way out of a small dataset with compute"); the compounding beat (92.77%⁵ = 68.7% on a 5-digit invoice); stale-weights trap demonstrated (91.16% lie vs 53.38% truth); the 200-photo client point *trained*, not interpolated | Kept as house patterns | — |
| LL-40 | process | Torch-on-CPU with pinned seeds proved bit-exact and thread-count-independent for this workload; synthetic-digit fallback with a `DATA_IS_REAL` flag that skips data-pinned asserts keeps the notebook runnable offline without faking results | Kept; codified | SI-27 |

### Round 8 — LSN-1.5 (builder: Opus 5, agent abc86234c1197c2f4) — 2026-07-29 — **ACCEPTED**

**Artifacts:** `notebooks/lessons/LSN-1.5_Conversational_Deep_Learning.ipynb` (35 cells — 18 code / 17 markdown, 4 figures, 45 asserts, ~5 s total runtime; discussion-shaped per LL-27: pre-work + cheat sheet + three segments + drill workspace, no homework) · `program/lessons/decks/LSN-1.5-conversational-deep-learning.html` (16 slides, timed notes 15/15/15/15 = 60). Builder run was interrupted once by a transient API stall and resumed with context intact; no work lost.

**Review verification:** independent in-repo re-execution → byte-identical (18/18 concatenated streams per LL-28, 10/10 rich blocks, 4/4 PNGs by sha256); all four drill prompts + all four rubric rows + the 6/8-no-zero pass bar verbatim in notebook AND deck (reviewer's first verbatim pass false-alarmed on markdown formatting chars — the LL-25 extraction fix resolved it); every LSN-1.4 number actually cited confirmed against LSN-1.4's executed outputs (101,770 params / 471 steps / 2.3117 / 0.7554-0.3195-0.2585 / 92.77% = 723 errors / 68.7% compound / 97.04% / 64.41% / 82.90% / 3↔5 at 66 / 48-of-128; the handoff also listed the degradation series 23.88/53.38/84.23 as used — it is not, harmless); drill advisor graded the reviewer's own planted good/thin/salad answers (not the builder's test strings) correctly: 6/6, 2/6-with-a-zero fails, 0/6; deck CSS core 113/113 exemplar lines contained, CDN-only, text wordmark; all 16 slides fit 720 px under a rect-based headless harness validated against the accepted LSN-0.1/1.4 decks; all four figures visually inspected (builder's three self-caught render fixes confirmed). Plan's ambiguous "two rounds fit" drill timing priced and clarified in the plan (two deliveries, one per partner: 5+2×3+4 = 15); cheat sheet built now with canonical home in the notebook — Materials table and module spec updated per SI-16. No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-41 | process | `_i` is IPython-reserved (input history): a cross-cell variable named `_i` silently becomes the previous cell's source text — cost the builder a debug loop; unreproducible under plain Python | Cross-cell values named in CAPS | SI-28 |
| LL-42 | process | `tight_layout` on a gridspec containing a `twinx` emits a warning whose text embeds an ipykernel temp path with a PID — a byte-identity breaker hiding in warning *text*, not outputs proper | Warning eliminated via explicit margins; codified | SI-28 |
| LL-43 | content | Citation caveats are dependency claims (LL-29 extended): `neural_networks/02` loads MNIST via `fetch_openml` (~55 MB network pull that bypasses the SI-24b warm cache); `reinforcement/01` is fully unseeded (numbers differ every run); all three references ship zero stored outputs | Caveats disclosed in a live verification cell in the companion + in plan/spec | — |
| LL-44 | content | **Pre-existing, found while validating the overflow harness:** LSN-1.3 deck footer clips past 720 px on 2 slides (+5/+10 px reviewer-measured; builder's harness reported 3 slides at +16/+20 — method/font variance). Cosmetic: `overflow:hidden` trims the footer edge | Logged as an open cosmetic fix for a future round — accepted artifacts are not hot-fixed inside another lesson's commit | open item |
| LL-45 | content | Keeper beats: the collapse proof (two linear layers = one matrix, `atol 1e-12`) as the *reason* depth needs the squash; engineered-feature control (47% line / 100% line+hand-made radius / 100% at 91 params — LL-39's control-run pattern applied to features); translation reuse measured exactly (digit shifted 4 px, same detector, map slides, `0.00e+00`); reward-farming agent (two-square loop, never finishes) with the SI-21 decompose ending (bonus collectable once → optimal path *through* the bonus square); demos framed as props, not evidence; drill advisor with the jargon→plain swap table | Kept as house patterns | — |

### Round 9 — LSN-1.6 (builder: Opus 5, agent a531ce75511cf356a) — 2026-07-29 — **ACCEPTED** — *MOD-1 lesson builds complete (ASM-1 = GAP-6 remains)*

**Artifacts:** `notebooks/lessons/LSN-1.6_Data_Requirements_Presales_Question_Bank.ipynb` (40 cells — 21 code / 19 markdown, 4 figures, 46 asserts, ~3 s runtime; workshop-shaped: checklist companion + case-walkthrough workspace + homework template & advisor) · `program/lessons/decks/LSN-1.6-data-requirements.html` (18 slides, timed notes sum 60 = 20/25/15 by segment, footer segment map).

**Review verification:** independent in-repo re-execution → byte-identical (21/21 concatenated streams, 18/18 rich blocks, 4/4 PNGs by sha256); full contract verbatim in BOTH artifacts — all 5 checklist rows (question + failure columns), all 5 walkthrough step titles + bodies (step 3 as its six sub-prompts on the deck, disclosed), all 11 starter questions, homework pass bar (deck carries the operative clause verbatim, notebook the full line) — 0 failures after fixing two reviewer-battery bugs (LL-46); 12/12 LSN-1.4 numbers confirmed in LSN-1.4's executed outputs incl. the `CURVE_FOR_LSN_1_6` handoff dict; GAP-5 discipline confirmed — banner + labeled hypothetical placeholders, zero invented case facts (20 notebook references, 9 deck chips/panels); advisor exercised with reviewer-authored planted submissions (healthcare — a fourth industry): THIN and WRONG fail hard at 0, STRONG scored 10/12 with two conservative 1/2s whose remedy text was precise (see LL-48) — acceptable because the save is completeness-gated only; deck CSS core 113/113, CDN-only, 18/18 slides fit 720 px (content harness); all four figures inspected — fig 1's agreement matrix internally consistent (115+3+33+49 = 200, 82% agreement, sign-off ratio 1.58×), fig 2 re-plots the LSN-1.4 curve without retraining. `~10 questions` header fixed to 11 in the plan; Materials + module spec updated per SI-16 (question-bank template closed; case brief stays GAP-5). No fix round.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-46 | process | Two reviewer-battery normalization traps: (a) builder-predicted — inline tags at punctuation boundaries and blockquote `>` prefixes break naive verbatim diffs; (b) new — applying an HTML tag-stripper to concatenated *notebook source* silently swallows everything between a Python `<` and the next `>` (comparison operators), erasing whole contract strings from the corpus. Normalize per-side: tags only for HTML corpora, never for code | Battery fixed; builders also keep each contract string in one tag-free run | reviewer battery |
| LL-47 | process | Naive SI-28a/SI-26b detectors false-positive on within-cell `_`-prefixed loop/comprehension variables and on the anti-Styler compliance docstring. AST load-before-store per cell is the correct cross-cell test (three flags on this notebook, all comprehension targets — zero real leaks) | Context-aware checks codified in the battery | reviewer battery |
| LL-48 | content | Advisor cue lexicons under-score legitimate paraphrase: reviewer's semantically complete `fresh`/`legal` answers ("lands nightly", "state law limits…") scored 1/2 for missing cue words. Non-blocking here because the advisor never gates the save, prints its own limits, and its remedy text names exactly what to add — the behaviors now required by SI-29 | Codified | SI-29 |
| LL-49 | content | Keeper beats: inherited-labeller prop (two honest managers, 82%/κ≈0.6, one signs off 1.58× the other → model inherits +8.0 points of optimism — "a model does not learn 'complete', it learns whoever labelled it"); confidence-doesn't-fall drift prop (accuracy −25.5 pts, confidence +0.6 — monitoring becomes a line item); the five-row "no → work package" commercial inversion ("you cannot lose a deal by asking"); `recorded ≠ exists` four-way; the κ audit as a first-meeting ask; the bank coverage matrix as a workshop instrument (gold-flags `enough`/`legal` at one question each); figure pattern — when a panel has no free interior space, move the number into the title | Kept as house patterns | — |

---

## Supplement-integration pass — 2026-08-11 (not a build round)

An external course corpus was processed into `SUP-1`–`SUP-12` (`program/sources/`) and attached to
existing lesson plans by ID. No artifact was rebuilt. This entry records the findings that touch built
material, so the next builder inherits them rather than rediscovering them.

**Deliberate scope limit:** executed, reviewed, committed notebooks were **not** hot-patched here. Fixing
them outside a sanctioned round would bypass `SI-2` re-execution and `SI-22` byte-identity verification,
which is what makes them trustworthy. Every defect below is named down to the cell so the fix is
mechanical rather than investigative.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-50 | design | **Measured colour-vision defect in the palette, four confirmed artifact hits.** `yellow` and `mint` are perceptually the same colour under protanopia (CIEDE2000 = 1.7) and near-identical under deuteranopia (5.5), and are the palette's closest pair in greyscale (0.08 luminance apart). Confirmed sole-encoding failures: `LSN-1.5` cell 14 (a two-category `ListedColormap` of exactly this pair — the figure conveys nothing), `LSN-0.3` cell 17 (two of five legend bands, in the figure whose *point* is that bands separate), `LSN-1.4` cell 12 (title reads "yellow = rarest, mint = most common"), `LSN-1.6` cell 32 (two of four phases). Marginal, review only: `LSN-1.4` cell 46, `LSN-1.6` cell 14, `LSN-1.5` cell 24. Already-safe exemplar: `LSN-1.4` cell 32 prints the count in every cell, so its ramp through the unsafe pair costs nothing | Rule adopted; four fixes carried as `COLOUR-1` in the MOD-0/MOD-1 build lists | SI-30 |
| LL-51 | process | **Every palette colour was fine; the defect was in one pair.** The initial hypothesis ("three of four are green-ish, they probably all collide") was wrong in a way that would have caused a needless palette redesign. Simulating and measuring took twenty minutes and converted a vague accessibility worry into one testable rule and four one-line fixes | Measure before redesigning; the check script pattern is reusable for any future palette change | SI-30 |
| LL-52 | process | **A citation can be inherited along with a licence you do not want.** Several of the strongest supplement items reached us through a non-commercially-licensed teaching kit but are primary sources in their own right (Anscombe 1973; Tukey's fences; Tufte's principles; ColorBrewer). Building from the primary source removes the licence constraint entirely | Check provenance before inheriting terms | SI-31 |
| LL-53 | content | **The corpus's best single item was one slide of a thirty-slide graduate lecture** (the reducible/irreducible uncertainty split, now `SUP-11`) — from a kit the first pass had logged as "nothing at basics level." Depth of source and value to the program are uncorrelated; the first pass's summary judgement was wrong and is corrected in the source catalog | Second-pass every source dismissed wholesale | note |
| LL-54 | content | **Four lessons were independently teaching one idea** — the average lies (`LSN-0.2`), the aggregate lies (`LSN-0.3`), the confidence lies (`LSN-0.4`), the MAE lies (`LSN-1.3`) — with no plan calling forward or back to the others. Named as the "refuse the aggregate" spine and cross-referenced in all four plans and both module specs | Look for accidental spines when adding material; they are cheaper to connect than to build | note |

---

## Round 10 — MOD-0 supplement-integration build (LSN-0.1 – LSN-0.4) — 2026-08-11 — **ACCEPTED WITH FIXES**

The 2026-08-11 supplement pass adopted eleven content changes; this round put them into the artifacts and
closed the MOD-0 half of the `GAP-11` notebook debt. **Decks were already on the 60-min contract** (retimed
2026-08-03) — only the notebooks were carrying the old 90-min structure, which is the opposite of what the
module spec's wording implied and is worth correcting there.

**Artifacts.** All four notebooks executed end to end, zero errors, cell ids normalised:
`LSN-0.1` 17 cells · `LSN-0.2` 42 cells / 8 figures · `LSN-0.3` 35 cells / 7 figures ·
`LSN-0.4` 41 cells / 5 figures. Decks: `LSN-0.2` (+5 edits), `LSN-0.3` (+3), `LSN-0.4` (+1 slide),
all four render clean at 1280×720.

**What changed, by lesson.**

| Lesson | Notebook | Deck |
|---|---|---|
| `LSN-0.1` | Removed a stray empty cell left by an editor; re-executed | — |
| `LSN-0.2` | Segment headers retimed 20/25/20/25 → **12/15/13/20 = 60**; six named bias types + the CRM-export drill; the 1.5 × IQR fence added as fix 3 **with a computation cell** (flags only the $2M whale, mean $208,000 → $80,000, median unmoved); Anscombe lifted out of segment 3 into homework task 2 behind a **commit-your-prediction** cell; homework restructured into the plan's five tasks | Six bias types + the CRM drill on the sampling slide; "four cheap fixes" incl. the fence; Anscombe reframed as predict-then-reveal |
| `LSN-0.3` | Headers retimed 25/25/20/20 → **12/15/13/20 = 60**; **`COLOUR-1` fixed** (see below); homework Q1 swapped to the disaggregation question, with the answer-key cell rewritten around it; the five test strategies added ahead of the holdout task | Q1 swapped on the close slide; holdout task now names the strategy choice; spine labelled on the base-rates slide |
| `LSN-0.4` | **The "no homework — checkpoint week" closing was contradicting its own plan** and is replaced by the four-task, 100-min homework, including the calibration check (bucket by stated confidence, compare to observed); segment 1 gained the reducible/irreducible second axis with a measured demo | New slide, "If we send you more data, will it get better?", 3 min bought from the misfiles; segment-1 timings rebalanced to hold at 25 |

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-55 | process | **An executed notebook had been silently stripped of every output** (`LSN-0.4`: 26 outputs and 4 figures → 0, and 5 cells lost their ids) in the working tree, uncommitted and unrelated to any build. Caught only by diffing working against `HEAD` before editing. A stripped notebook still opens, still runs, and looks fine in a diff summary | Rebuilt from `HEAD` rather than the working copy; re-executed | see SI-32 |
| LL-56 | content | **`SI-17` earns its keep again.** Both new `LSN-0.4` constructions failed on first computation: the reducible/irreducible fit converged at n=10 (a 2-parameter fit on a strong signal has nothing to learn), and the calibration set came out a coin flip in every bucket (the "correct" flag was built from the wrong comparison). Rebuilt at 8 parameters and with the prediction/label comparison fixed — the published numbers (floor 4.83, 34.86 → 4.83; honest gap 3.4 pts vs overconfident 15.3 pts) are the second attempt | Both pre-computed in a scratch script before embedding | SI-17 (holds) |
| LL-57 | design | **`SI-19` caught a fresh illegible figure.** The reducible/irreducible curve on a linear y-axis let the n=10 point (34.86) crush the interesting region (4.8–6.8) into a strip — the `LL-10` failure, reproduced exactly. Fixed with log-log axes plus a second panel showing the reducible part alone | Redesigned and re-inspected | SI-19 (holds) |
| LL-58 | design | **`SI-23` caught a fresh overflow.** The six-bias-type block plus a drill callout pushed `LSN-0.2` slide 4 past 720 px, clipping the callout's last line. Fixed by compressing the type list to one line and tightening callout padding — not by shrinking type | Re-rendered and re-inspected | SI-23 (holds) |
| LL-59 | content | `COLOUR-1` fix pattern, now the house answer: `LSN-0.3`'s five-band scatter keeps its colours and adds **marker shape and size** per band (circle · circle · square · triangle · diamond), so the mint and yellow bands survive protanopia. Colour was not removed — a second channel was added, per `SI-30(b)`. Remaining yellow/mint co-uses in MOD-0 are all double-encoded and were re-checked | Applied; the other three `COLOUR-1` defects (`LSN-1.4` c12, `LSN-1.5` c14, `LSN-1.6` c32) remain open in the MOD-1 build list | SI-30 |

**Still open after this round:** MOD-0 notebooks are **not yet anonymised** (the other half of `GAP-11`);
`ASM-0` remains `GAP-6`; the three MOD-1 `COLOUR-1` defects are unfixed; and this round has **not been
independently reviewed** — it was built and self-verified in one pass, which is not the two-agent process
this file specifies.

### Round 10 review — 2026-08-11

**Independence caveat, stated up front:** this review was run in the same session as the build, not by a
separate reviewer agent. It re-executed every notebook from scratch, recomputed the mathematics
independently, and audited against the contracts — but it does not carry the independence the two-agent
process is designed to give. **A genuine second-agent pass is still worth running before delivery.**

**Battery results.** Fresh in-repo re-execution of all four notebooks: **zero errors**. `SI-22`
byte-identity: `LSN-0.2` (8 figures), `LSN-0.3` (7), `LSN-0.4` (5) all **0 mismatches**. Segment minutes
in notebooks: 0.2 and 0.3 both **12+15+13+20 = 60**, 0.4 **25+20+15 = 60**. Deck speaker-note minutes:
all four decks sum to **60**. Every number quoted in the `LSN-0.4` deck confirmed present in that
notebook's executed output. `SI-1` clean, `SI-3` seeded throughout (9 / 7 / 17 generators), `SI-26b` no
Styler, `SI-30` colour compliant. Links in `program/`: **0 broken**.

Four defects found and fixed during review; two accepted as-is with reasons.

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-60 | content | **The Anscombe prediction table overstated the agreement.** The restaged homework asks participants to commit to a prediction from six statistics quoted as exact — but the reveal in the very next cell prints variance 4.127 / 4.128 / 4.123 / 4.123 and correlation 0.816 / 0.816 / 0.816 / **0.817**. Two of four disagree at the precision the table claimed. A participant who reads carefully catches the artifact contradicting itself at the exact moment it asks for their trust | Quoted as ≈ 4.13 / ≈ 0.816 with the third decimal disclosed, in the notebook, the plan, the deck **and** `SUP-10`; the reveal's own summary line now says "variance 4.123–4.128, correlation 0.816–0.817" | see SI-33 |
| LL-61 | content | **The disaggregation question was unanswerable as posed.** "91% overall, 95% majority, 32% minority" is consistent only for a specific split (~94/6), and the material never stated it. A participant asking "how big is each group?" got nothing — and the naive reading (91 is the average of 95 and 32) is arithmetically impossible, so the item risked *teaching* a misconception | Group sizes stated (94% / 6%) with the check shown: 0.94 × 95 + 0.06 × 32 = 91.2%. It also sharpens the lesson — a subgroup does not have to be large to be badly served, only small enough to hide | — |
| LL-62 | content | **Two inherited facts were carried at the source's precision rather than checked.** `SUP-10` stated the *Challenger* launch temperature as a flat 31°F (air temperature was ~36°F; the ~28–31°F figure is the estimated joint-seal temperature), and repeated the teaching kit's "one in ten men" for red-green colour deficiency (the standard figure is ~8%, roughly 1 in 12) | Both corrected. **Inheriting a source's rounding is inheriting its errors** — `SI-31` said cite the primary source; this extends it to the numbers | see SI-33 |
| LL-63 | process | **`LSN-0.1` cannot satisfy `SI-22` and never will.** Its checkpoint cell deliberately stamps `datetime.now(timezone.utc)` into the setup-evidence output, so re-execution always differs by one line. This is intended behaviour that `SI-22` does not carve out, so every future reviewer will rediscover it as a failure | Documented as a standing exception. Also noted: the committed output embeds the builder's `user@hostname`, which ships to participants — cosmetic, pre-existing, left alone | see SI-33 |
| LL-64 | process | **The review battery false-positived twice**, both previously documented: it flagged `seaborn` as a heavy `SI-1` import (`SI-1` explicitly permits it), and flagged four `_`-prefixed comprehension targets as cross-cell leaks — the exact `LL-47` trap. A correct free-variable analysis (loads before first store, per cell, with comprehension and for-targets bound properly) found **zero** real leaks | Battery corrected; the load-before-store implementation is the one to reuse | reviewer battery |
| — | design | **Accepted, not changed:** `LSN-0.2` deck slide 6 draws the Anscombe fit line in `yellow` over data points in `mint` — the `SI-30` unsafe pair. Accepted because the two are separated by form (a thin dashed line versus filled circles), which is exactly the double-encoding `SI-30(b)` requires. Logged so the next reviewer does not re-open it | — | — |

### Round 10 addendum — `ACTIVATE_VENV.md` — 2026-08-13

| ID | Category | Finding | Action | Promoted to |
|---|---|---|---|---|
| LL-65 | environment | **`LL-1` was never actually fixed — only worked around.** Round 0 found that `ACTIVATE_VENV.md` claimed the virtual environment "has been created successfully" when it did not exist; the venv was created and the doc was left alone. But `.venv/` is gitignored, so the claim is false for **every participant who clones the repo** — and this file is `LSN-0.1`'s pre-work target, read cold by twelve people on 31 August. The doc also sent them to `pip install -r requirements.txt`, which pulls PyTorch, transformers, `llama-cpp-python`, FAISS, Neo4j and `bitsandbytes` (CUDA-only, fails on a Mac) — the heavy-install trap `LL-2` identified for MOD-0 and then only fixed inside the venv, not in the instructions | Rewritten around what a fresh clone actually faces: create the environment (uv or stdlib), staged installs per module, `.venv/bin/python` by path throughout to dodge the macOS system-`pip3` trap, verified-versions table, and the honest note that the old claim was untrue | SI-34 |
| LL-66 | process | **Documentation was tested, not just written.** Both install paths were run from scratch in throwaway environments (uv: ~1 s warm, 313 MB; stdlib pip: 26 s), and `LSN-0.2` was executed end-to-end against a **stage-1-only** environment to prove the MOD-0 package set is genuinely sufficient. Every command, link and file path in the file was then run as literally written | Kept as the acceptance standard for setup docs | SI-34 |

| LL-67 | environment | **`uv venv` creates an environment with no `pip` in it.** Found by running the documented setup rather than trusting it: `uv venv .venv` followed by `.venv/bin/python -m pip install -r requirements.txt` fails with `No module named pip`. Since `python -m pip` is the form every generic instruction uses — and the form the `LSN-0.1` notebook prints as its fix — this would have stopped anyone who took the recommended `uv` path | `uv venv --seed` documented, which installs pip; the uv-native `uv pip install --python .venv/bin/python -r ...` given as the alternative. Both paths now tested from scratch | SI-34 |
| LL-68 | environment | **The dependency list and the setup instructions had drifted apart.** `requirements.txt` was the aspirational full-program list (CUDA-only `bitsandbytes`, `llama-cpp-python`, FAISS, Neo4j), while `ACTIVATE_VENV.md` told people not to install it — yet the `LSN-0.1` notebook still printed `pip install -r requirements.txt` as its remedy when an import failed. Three artifacts, three different answers | Rather than adding a fourth instruction, `requirements.txt` was **made safe**: it is now the MOD-0 stage and every existing call site became correct without being edited. Staging is `requirements.txt` -> `requirements-mod1.txt` -> `requirements-full.txt` (retired, marked do-not-install) | SI-35 |

### Added after the Round 10 review
### Added after the Round 10 review
- **SI-35** — When several artifacts give conflicting setup instructions, fix the thing they all point at rather than adding another instruction. Making `requirements.txt` safe corrected the notebook, the README, the setup script and the troubleshooting doc at once, without touching their call sites (`LL-68`). Corollary: a dependency file participants are told *not* to run is a defect, not documentation.
- **SI-34** — A setup document is an artifact and gets acceptance-tested like one: run every command as literally written, from a clean environment, on the paths a fresh clone actually has. State the verified interpreter and package versions. Never tell a participant to install a dependency set the module in front of them does not need. And never describe repo state that `.gitignore` excludes as though the reader already has it (`LL-65`).
- **SI-33** — Three precision rules, all learned the same way. (a) **Never quote a statistic more precisely than it is true**: if an artifact claims several things are identical, quote them at the precision at which they actually agree and disclose the next decimal — the reveal will print it anyway (`LL-60`). (b) **A scenario built from part-and-whole numbers must state the weights**, or it is unanswerable and may teach a misconception (`LL-61`). (c) **Facts inherited from a source get checked, not copied** — its rounding becomes your error (`LL-62`). And note the standing `SI-22` exception: `LSN-0.1` deliberately stamps a UTC timestamp, so it is exempt from byte-identity on that one cell (`LL-63`).
