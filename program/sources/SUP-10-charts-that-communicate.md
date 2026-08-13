---
name: SUP-10-charts-that-communicate
description: Charts that carry a number versus charts that bury it — a decision case, the mystery-dataset reveal, a defensible outlier rule, the perception constraints behind chart choice, and the accessibility check our own palette needs.
serves: LSN-0.2, LSN-0.3, LSN-1.3
sources: SRC-4 (and primary sources it cites, which we can use directly)
---

# SUP-10 — Charts That Communicate

**The problem this solves.** `LSN-0.2`'s first segment is "distributions as pictures of uncertainty," and
its whole thesis is that a number's *shape* decides whether it can be trusted. The lesson currently
teaches the statistics and leaves the picture-making implicit. The visualization modules of `SRC-4` are
the strongest MOD-0-relevant material in the entire donated corpus, and they close exactly that gap:
**a chart is not decoration on an analysis, it is the part of the analysis that reaches the decision-maker.**

**Licensing note that makes this the cheapest supplement to use.** Most of the best items here are the
kit's own citations of primary sources — Tufte's *Visual Explanations*, Anscombe's 1973 paper, Tukey's
box plot, ColorBrewer, the Heer & Bostock perception study. We can cite and build from those **directly**,
bypassing the kit's non-commercial licence entirely. Nothing below requires the kit itself.

---

## 1. The decision case — a chart that failed, with consequences

The Space Shuttle *Challenger* broke up 73 seconds after launch on 28 January 1986, killing all seven
aboard. The cause was a rubber O-ring seal that lost resilience in cold weather. Air temperature at launch was about 36°F, and the estimated temperature of the
joint seals was lower still — roughly 28–31°F. The coldest previous launch had been 53°F. **Engineers at the booster manufacturer
had recommended against launching, the night before, and were overruled.** Tufte's reconstruction argues
that the relationship between temperature and seal damage was present in the data the engineers held,
and that the charts they presented did not make it visible — the damage evidence was spread across
thirteen separate exhibits, sorted by mission rather than by temperature, and the flights with *no*
damage were omitted entirely, removing the contrast that would have shown the pattern.

**Why this is the right opening for `LSN-0.2`.** Its two live segments are "distributions as pictures of
uncertainty" and "the client-conversation drill." This case is both at once:

- The number existed. The analysis was roughly right. **The presentation lost the argument.**
- Sorting by the wrong variable hid a real relationship. That is a distribution question, not a design
  question — the engineers plotted incident *order* when the relevant axis was *temperature*.
- Dropping the no-damage flights removed the comparison group. That is the same defect as the
  positive-cases-only training set in `SUP-3` §4 and the survivorship bait already planted in `LSN-0.2`'s
  own homework (`LL-12`) — one idea, three appearances across the program.
- And it is the most serious possible answer to "why does it matter how I draw this?"

**Two handling notes for the presenter.**

1. Seven people died. Present it as an engineering-ethics case — which is how it is taught in
   engineering programs worldwide — not as a chart-crit anecdote. No dark humor, no "look how bad this
   chart is" framing.
2. **There is documented scholarly disagreement with the pure-chart-design reading.** Published critiques
   have argued that Tufte's account understates the organizational pressure the engineers were under and
   overstates what a better chart could have achieved against a management decision already forming.
   *Say this in the room.* It makes the case stronger, not weaker: the honest lesson is that a chart is
   necessary and not sufficient — and a senior who has to persuade a client of an uncomfortable number
   needs to know both halves of that.

**Placement:** a 4–5 minute opener or closer for `LSN-0.2` segment 1, or the framing for the segment-4
client drill ("our model is 92% accurate"). **Candidate swap, not an addition** — segment 1 is 12 minutes
and already has the participants' own pre-work plots on screen.

---

## 2. The mystery-dataset reveal — Anscombe's quartet, restaged

`LSN-0.2`'s homework already includes Anscombe's quartet (relocated out of the live session, 25 min with
the outlier arithmetic). The kit's staging is better than a straight presentation of it, and the upgrade
costs nothing:

**Show the summary statistics first, and ask participants to draw what they think the data looks like:**

| Property | Value |
|---|---|
| mean of x | 9 |
| variance of x | 11 |
| mean of y | 7.5 |
| variance of y | ≈ 4.13 |
| correlation of x and y | ≈ 0.816 |
| fitted line | y = 3 + 0.5x |

*Then* reveal that four completely different datasets produce those numbers to two significant figures —
(the variances are 4.127 / 4.128 / 4.123 / 4.123 and one correlation is 0.817; quote them honestly, the
point does not need them to be bit-identical) —
one roughly linear, one clearly curved, one linear with a single outlier dragging the fit, one where all
but a single point share the same x value.

**Why the restaging matters.** Presented as a fact, Anscombe's quartet is a curiosity. Presented as a
prediction the participant made and got wrong, it is the moment they stop trusting a summary statistic
they have not plotted — which is `OUT-0.3` in one exercise. It is also a direct setup for `LSN-1.3`'s
metric-consistency work: *the summary is not the data.*

**Placement:** a reframe inside the existing homework task — the notebook asks for the prediction before
it plots. **No minutes move.** Cite Anscombe (1973) directly.

---

## 3. A defensible outlier rule — the box plot and the interquartile range

`LSN-0.2` segment 3 is "Variance and outliers: when the average lies," and its homework includes an
outlier recompute. Right now the identification of an outlier is by eye. The kit supplies the standard
rule, and it is five lines of numpy:

1. Sort the values.
2. Q1 = the 25th percentile; Q3 = the 75th percentile.
3. IQR = Q3 − Q1.
4. Lower fence = Q1 − 1.5 × IQR; upper fence = Q3 + 1.5 × IQR.
5. Anything outside the fences is flagged.

A Tukey box plot is exactly this, drawn: the box spans Q1 to Q3, the line inside is the median, the
whiskers reach the most extreme points still inside the fences, and everything beyond is plotted
individually.

**Why it belongs in this lesson.** It converts "that point looks wrong" into "that point is outside the
1.5 × IQR fence," which is the difference between an opinion and a method — and it gives the segment-4
client drill a second question with teeth: **"which points did you exclude, and by what rule?"** A vendor
who cannot answer that has hand-tuned their metric.

**And the caveat that must ship with it,** because it is the commercially important half: the rule flags
outliers, it does not tell you what to do with them. The kit's own framing is right — sometimes the
outlier is bad data, and sometimes it is the entire business case (the fraud, the defect, the deal). This
is the same point `SUP-7` §1 makes as weakness 6, arriving four modules earlier.

**Fits the environment.** Pure numpy/pandas — no `SI-1` violation, no new dependency.

**Placement:** the existing homework outlier task gains a rule instead of an eyeball. **No minutes move.**

---

## 4. Why some charts work — the perception constraints

Two findings that turn chart choice from taste into engineering.

### Pre-attentive processing

Some visual properties are detected in parallel, in roughly the time between eye movements
(~200 ms), without conscious search: hue, size, length, width, curvature, orientation, closure, motion.
Others require serial, item-by-item scanning.

**The critical result: a single channel is pre-attentive; a *conjunction* of two is not.** Finding the
red dot among blue dots is instant. Finding the circle among squares is instant. Finding the *red circle*
among red squares and blue circles is a slow, deliberate search.

**Direct consequence for our decks and notebooks:** one visual channel per question. A chart that encodes
category by colour *and* status by shape and expects the viewer to find "the red circles" has just made a
20 ms task into a 3 second one — and in a 60-minute session run at pace, that is a slide nobody reads.

### Encoding accuracy is measured, not a matter of opinion

Position along a common scale is read most accurately, then length, then angle and area, then colour
saturation. This is why bar charts, scatter plots, and line charts win for quantitative comparison and
why pie charts and 3-D effects lose: they encode magnitude in the channels people read worst.

**Detecting quickly is not the same as detecting accurately** — and you generally want both.

---

## 5. The chart rules worth handing participants as a one-pager

Tufte's three principles, plus the specific corrections that follow from them:

**Principle 1 — do not lie. Principle 2 — maximize the data-to-ink ratio. Principle 3 — minimize chart junk.**

| Rule | Why |
|---|---|
| **Bar charts start at zero. Line charts need not.** | A bar encodes magnitude in its *length*, so truncating the axis lies about the ratio. A line encodes *change* in its slope, so a non-zero baseline is legitimate — but too flat obscures the message and too steep overstates the trend |
| **No pie charts. No 3-D or perspective charts.** | Angle and area are read poorly; perspective actively reverses rankings — a documented example had 19.5% drawn to look larger than 21.2% |
| **Use a log scale when values span orders of magnitude** | Otherwise a handful of large values crush everything else into a strip at the bottom. **This is `LL-10` in our own build log** — a `LSN-0.2` figure was illegible until the axis went log, and the same lesson's data (a p99-wide latency tail) is exactly the case that demands it. `SUP-2` §4 makes the same point about the underlying data |
| **Avoid tilted or rotated tick labels — go horizontal instead** | Rotated text is read serially and slowly. If labels do not fit, flip the chart |
| **Small multiples beat many overlapping lines** | A grid of small, identical charts is compared by position; eight overlapping lines are compared by colour memory |
| **When everything is emphasized, nothing is** | Bold, italic, and colour applied everywhere carry no information |
| **Figures must be self-contained** | Title and caption should carry the message without the surrounding text. This is already our deck house style — it is worth telling participants *why* |

---

## 6. Colour — and an accessibility check our own palette needs

Colour buys four things: it draws attention, adds appeal, adds a dimension to encode, and improves
recall. It costs one thing, reliably:

- **About 8% of men have red-green colour vision deficiency** (roughly 1 in 12; about 0.5% of women). A palette
  that distinguishes categories by red versus green distinguishes nothing for them.
- **Quantitative data needs an ordered scale**, not a set of distinct hues — the viewer must be able to
  rank the colours without a legend.
- **Cultural encoding is real**: do not draw profit in red.
- ColorBrewer remains the standard tool for picking scales that survive both constraints.

### The check on our own palette — run 2026-08-11, and it found something

Simulated with the Machado et al. (2009) severity-1.0 model, compared with CIEDE2000 perceptual distance
in CIELAB. The result is **narrower and more actionable than expected**: the palette is fine, with exactly
one exception.

| Pair | Normal | Protanopia | Deuteranopia | Verdict |
|---|---|---|---|---|
| **`yellow` `#ffe86b` / `mint` `#97f377`** | 22.0 | **1.7** | **5.5** | **Unusable as a two-category distinction** |
| `green` / `yellow` | 29.2 | 19.6 | 23.5 | safe |
| `green` / `mint` | 19.1 | 19.0 | 19.0 | safe |
| `navy` / `green` | 46.4 | 45.0 | 43.4 | safe |
| `navy` / `mint` | 57.4 | 56.1 | 55.0 | safe |
| `navy` / `yellow` | 58.4 | 57.1 | 59.9 | safe |

A CIEDE2000 distance of 1.7 is at the just-noticeable-difference boundary — for a viewer with protanopia,
`yellow` and `mint` are **the same colour**. The pair is also the palette's weakest in greyscale
(relative luminance 0.800 vs 0.720, a gap of 0.08), so it fails printed and photocopied too. Every other
pair in the full seven-colour palette scores ≥10 worst-case.

**So the finding is not "the palette is bad." It is one rule:**

> ### Never let `yellow` and `mint` be the only thing separating two categories in one view.
> Pair `yellow` with `navy` or `green` instead. `mint` is safe against everything except `yellow`.

### Four confirmed defects in built artifacts

Checked against every executed notebook. Colour is the sole distinguishing encoding in these four:

| Artifact | Cell | What it does | Why it breaks |
|---|---|---|---|
| `LSN-1.5_Conversational_Deep_Learning.ipynb` | 14 | `ListedColormap([yellow, mint])` — a two-category image | **Worst case.** Both categories render as one colour; the figure conveys nothing |
| `LSN-0.3_Statistics_2_...ipynb` | 17 | Five temperature bands in the spurious-correlation scatter; bands 4 and 5 are `mint` and `yellow`, read via legend | Two bands merge — and the *pedagogy* is that the bands separate |
| `LSN-1.4_Hands_On_Train_MNIST.ipynb` | 12 | Bar chart whose title reads "yellow = rarest class, mint = most common" | Colour is the only encoding, and the title depends on the reader distinguishing it |
| `LSN-1.6_Data_Requirements_...ipynb` | 32 | Four-phase colour dict: `yellow`, `navy`, `green`, `mint` | Two of the four phases collapse |

**Three more are marginal and should be reviewed, not necessarily changed:** `LSN-1.4` cell 46 and
`LSN-1.6` cell 14 (yellow vs mint markers, partly rescued by differing marker sizes); `LSN-1.5` cell 24
(a white→mint→yellow sequential ramp that flattens through its middle).

**One is already safe and shows the right pattern:** `LSN-1.4` cell 32's confusion matrix runs a
white→mint→yellow→orange ramp but prints the count in every cell — colour is redundant, so the ramp
flattening costs nothing. That is double-encoding done correctly, and it is the model for the fixes.

### The two mitigations

1. **Double-encode.** Never let colour alone carry a distinction that matters — add position, marker
   shape, line style, direct labels, or the printed value. Our own house pattern of moving the number into
   the title (`LL-49`) is a form of this, and `LSN-1.4` cell 32 is the exemplar.
2. **Swap the pair, not the palette.** These are four one-line changes. No brand colour needs to change.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-0.2` segment 1 | The decision case as opener or as the segment-4 drill's framing — the number was in the room and the chart lost the argument | **Candidate swap** inside an existing 12-min segment | Deck edit |
| `LSN-0.2` segment 3 + homework | The IQR fence rule replaces eyeballing; the "by what rule did you exclude it?" question joins the client drill | Method for an existing task — **no minutes move** | Notebook edit, pure numpy |
| `LSN-0.2` homework | Anscombe restaged as predict-then-reveal inside the existing 25-min task | Reframe — **no minutes move** | Notebook edit |
| `LSN-0.2` homework | §5's rules become the standard the participants' own histogram is graded against — the homework already asks them to produce one | Grading aid | Small |
| `LSN-1.3` | §4's encoding-accuracy result is why the confusion matrix is read as a matrix and not as a set of percentages in prose | Framing note | None |
| **Builder guidance** | §4 (one channel per question), §5 (log scale, self-contained figures), §6 (the `yellow`/`mint` rule and double-encoding) — **adopted as `SI-30`**, see `BUILD_LOG.md` | Standing Instruction | done |
| **Artifact debt** | Four confirmed colour-encoding defects, named by file and cell in §6 — logged as `COLOUR-1` in the MOD-0 and MOD-1 build lists | Fix round | ~1 h incl. re-execution |

## Proposals requiring a spec decision

**None outstanding.** The palette check was run on 2026-08-11 and confirmed one unusable pair; the
build-standards consequence is adopted as `SI-30` in `BUILD_LOG.md`, and the four artifact defects are
carried as `COLOUR-1` in the module build lists. **The artifacts themselves were deliberately not
hot-patched here** — they are executed, reviewed, committed notebooks, and changing them outside a
sanctioned build round would bypass the re-execution and byte-identity checks (`SI-2`, `SI-22`) that make
them trustworthy. Each defect is named down to the cell so the fix is mechanical.
