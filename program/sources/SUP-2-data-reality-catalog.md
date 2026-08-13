---
name: SUP-2-data-reality-catalog
description: What "we have the data" actually means — the extraction, cleaning, encoding, and sampling decisions that consume most of an AI project, turned into pre-sales questions and one scoping arithmetic.
serves: LSN-1.6, LSN-0.2, LSN-2.4
sources: SRC-3
---

# SUP-2 — The Data Reality Catalog

**The problem this solves.** `LSN-1.6` already teaches the five-check reality list — exists / labeled /
enough / fresh / legal. What it does not yet carry is the *second* conversation, the one that happens
after a client says yes to all five and the project still takes three months longer than quoted. This
file is that conversation, and its headline is the single most useful sentence in `SRC-3`:

> Running the AI software is rarely where the time goes. Finding, formatting, and fixing the data is.

Every item below is stated as something you can ask, or something you can price.

---

## 1. The five ways data arrives, and what each costs

| Source shape | Typical form | The hidden cost |
|---|---|---|
| Delimited text | CSV, TSV | Columns are positional and unlabeled — you need someone who knows what column 7 means, and that person may have left |
| Labeled text | JSON | Cheapest to work with; ask for it by name |
| Tree-structured | XML, HTML | Needs a parser and a schema conversation |
| Spreadsheets | XLSX | Human-edited, therefore inconsistent — merged cells, notes in cells, three header rows |
| Documents | PDF | The most common and the most expensive. Layout, tables, and headers/footers all have to be recovered before a single line of AI code runs (this is exactly what `LSN-2.4`'s chunking stage is fighting) |
| Live systems | SQL query, API, event stream | Cheap per row, expensive in access negotiation |

**Pre-sales question this generates:** *"In what format will we receive the data, and who on your side
can tell us what each field means?"* The second half is the one that saves the project.

---

## 2. The four data-sharing obstacles that are organizational, not technical

Recast from `SRC-3`'s public-sector framing into the commercial one — the failure modes are identical:

1. **Nobody has realized what combining two sources would reveal.** The data exists in two departments
   that have never spoken. There is no process for sharing because there was never a reason.
2. **The data cannot be shared in its current form.** The answer is embedded in a paragraph of a report,
   not in a field. Extraction is a project, not a step.
3. **It must be anonymized first — and sometimes de-anonymized later.** Both directions have to be
   designed up front. A pipeline that anonymizes irreversibly and then gets asked "which customer was
   that?" is a rebuild.
4. **Access tiers do not combine.** If one source is restricted, the merged result inherits the
   restriction, and now the whole output is harder to use than either input was.

**Pre-sales question:** *"Has anyone ever combined these two sources before? What stopped them?"*

---

## 3. The cleaning decisions, each of which is a client decision

### Missing values — six defensible choices, and they are not equivalent

| Choice | When it is right | What it silently assumes |
|---|---|---|
| Drop the row | Missingness is rare and random | That it is random — usually untested |
| Default value | The blank has a real-world meaning (a stopped machine reads speed 0) | That the meaning is stable |
| Explicit "unknown" class | A sensor failed; the failure is itself signal | That the model can use a category |
| "Not applicable" | The attribute does not exist for this row | That the model distinguishes this from unknown |
| Fill with mean / median / mode | The quantity varies little | That the row is otherwise typical |
| Model the missingness | Missingness correlates with the target | Effort |

**The teaching point:** these are five different beliefs about the world, and the client holds the
belief, not the engineer. This is a `LSN-1.6` question, not a preprocessing detail.

### Incorrect values

Find them with plausible ranges per field (a latitude above 90; a delivery date before the order date; a
negative quantity). Then the same menu: drop the row as tainted, substitute a default, carry the last
good value forward, substitute the average, or mark it unknown. **A value error is often correlated with
whatever produced it** — a broken sensor, a bad import, one operator's data-entry habit — which is why
"drop the row" is not automatically safe.

### Unit and format incompatibility

The canonical failure is two systems agreeing on a number and disagreeing on its unit. Commercial
versions: currencies without a date-stamped rate, weights in two systems, timestamps in local vs UTC, and
dates written five ways (`14 October 2026`, `October 14, 2026`, `10/14/26`, `14/10/26`, `2026-10-14`).
Only the last one is unambiguous.

**Pre-sales question:** *"Which system is authoritative when two of them disagree?"* If no system is,
that is a work package with a name.

### Identity resolution

One person's name appears as `James Charles Hall`, `Hall, James C.`, `Jim Hall`, `jhall`, `JCH`. Any join
on names is a fuzzy-matching project wearing a join's clothing. The same is true of company names,
addresses, and product SKUs across two ERPs.

**Scoping rule of thumb worth teaching:** if the integration involves joining two systems on anything
other than a shared key, budget for identity resolution as its own line item.

---

## 4. Encoding — turning the client's world into numbers

| Data type | Definition by what you can *do* with it | Encoding for a model |
|---|---|---|
| **Categorical (nominal)** | No meaningful order — customer names, regions, ticket types. You can count them | One-hot: one column per value, 1 in the right column |
| **Ordinal** | Orderable — `excellent / good / ok / poor`, severity tiers, sizes. You can take a median | Assign a numeric scale, and **be explicit that the spacing is a choice** |
| **Integer** | Usually counts | Direct, often log-transformed |
| **Continuous** | Usually measurements | Direct, usually standardized |
| **Boolean** | 1 / 0 | Direct |

Two transformations worth naming because they show up in every real project:

- **Take the logarithm when values span orders of magnitude.** File sizes, invoice amounts, session
  durations, company revenues. Without it, the largest handful of rows dominate everything the model
  learns. This is a direct callback to `LSN-0.2`'s variance-and-outliers segment: the log is what you do
  *after* you have seen that the average lies.
- **Standardize (subtract the mean, divide by the standard deviation)** when features are on wildly
  different scales. Costs the extra step of computing and *storing* those two numbers — and forgetting to
  apply the training-time mean and standard deviation at inference is a classic production bug, which
  makes it a `LSN-3.5` observability example.

Going the other way — **binning a continuous value into ranges** — is needed by rule-based and tree-based
methods, and the bin boundaries are a modeling choice with business meaning ("what counts as a large
order?"). Never let the boundaries be set by whoever wrote the loader.

---

## 5. Sampling — the section that pays for itself

### The square-root law

Estimating an average from a sample of size *n* has an error that shrinks in proportion to 1/√n.
**Four times the data to halve the error.** This one line does more pre-sales work than any other in the
catalog, because it converts "can we just get more data?" from a wish into arithmetic.

Direct connection to `LSN-1.4`'s degradation curve (accuracy vs training-set size at 10,000 → 1,000 →
100 → 10 examples): participants have already *seen* diminishing returns on their own trained model. This
gives them the shape's name and lets them quote it in a room.

### Stratified sampling, and why rare events break naive approaches

If the thing you care about is rare — fraud, defects, churn, a converting lead — a random sample contains
almost none of it, and a model trained on that sample learns to always say no. (Which, as `LSN-1.3`'s
rubber-stamp beat shows, will score beautifully on accuracy.)

The fix is to sample the rare class at a much higher rate than the common one, so the training set is
closer to balanced, and then to remember that **the model's output probabilities no longer match reality**
and must be corrected back. Aim for something near a 50/50 split when you can control the sample.

**Pre-sales question:** *"How often does the thing we are trying to catch actually happen?"* An answer
under 1% changes the data volume needed, the metric that matters (`SUP-3`), and the honest promise.

### Random sampling as bias defense

Beyond speed, sampling randomly protects you from an ordering artifact — the first rows of an export are
often an unrepresentative startup period, and the last rows are often incomplete.

---

## 6. Two estimates of the same thing

When two systems both report a quantity and disagree, the consensus is somewhere between them, weighted
by how much you trust each. Worth teaching only as the *question*: **"When your CRM and your ERP disagree
about this number, which one wins, and who decided that?"** The arithmetic is advanced-tier; the question
is basics.

---

## How this lands

| Lesson | Where it goes | Change type | Cost |
|---|---|---|---|
| `LSN-1.6` | Extends the five-check checklist with the "second conversation" — format, obstacles, missing/incorrect values, identity resolution. The four new pre-sales questions (format owner, prior attempt, authoritative system, base rate) are **question-bank additions**, drawn from as needed | Additive to the bank; no re-timing | One page in the `GAP-5` walkthrough workspace |
| `LSN-1.6` case walkthrough | The catalog is a ready-made spine for the walkthrough's step 3 while `GAP-5` remains open — it lets the workspace run on structure rather than on invented case facts | De-risks `GAP-5` | None |
| `LSN-0.2` | The log-transform and the 1/√n law are natural homework extensions to the existing variance/sampling notebook — the notebook already builds n = 30 / 3,000 / 30,000 | Optional homework variant | Small |
| `LSN-2.4` | Section 1's PDF row is why chunking is hard — a one-line callback that makes the pre-work build stages feel less arbitrary | Framing note | None |

## Proposals requiring a spec decision

None. Everything here serves `OUT-1.6` ("articulate data requirements and limitations") and `OUT-0.3`.
