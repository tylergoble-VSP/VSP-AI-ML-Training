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

### Round 8 — LSN-1.5 (builder: Opus 5) — *pending*

### Round 9 — LSN-1.6 (builder: Opus 5) — *pending*
