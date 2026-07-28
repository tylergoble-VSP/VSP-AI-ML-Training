# lessons/ — Lesson Plans

One file per lesson, named `LSN-<n>.<m>-<kebab-title>.md`, authored from [`TEMPLATE.md`](TEMPLATE.md). The module spec's LSN section is the **contract** (outcomes served, duration, format); the lesson plan is the full working document (segment-by-segment session plan, pre-work tasks, drills, materials, delivery notes).

**Rule:** if writing a lesson plan reveals the contract is wrong (duration unrealistic, outcome misplaced), update the module spec first, then the plan. The spec is the source.

## Status Board

| Lesson | Title | Owner | Plan status |
|---|---|---|---|
| `LSN-0.1` | Orientation & environment setup | Tyler + Marius | not started |
| `LSN-0.2` | Statistics I — distributions, sampling, variance | Tyler | not started |
| `LSN-0.3` | Statistics II — probability, correlation ≠ causation | Tyler | not started |
| `LSN-0.4` | Deterministic, probabilistic, stochastic | Tyler | not started |
| `LSN-1.1` | The five ML jobs & the nesting doll | Tyler | not started |
| `LSN-1.2` | Model I/O | Tyler | not started |
| `LSN-1.3` | Grading models | Tyler | not started |
| `LSN-1.4` | Hands-on: train MNIST | Tyler / Stefana | not started |
| `LSN-1.5` | Conversational deep learning | Tyler | not started |
| `LSN-1.6` | Data requirements & pre-sales question bank | Tyler + Vlad | not started |
| `LSN-2.1` | How LLMs actually work | Tyler | not started |
| `LSN-2.2` | Prompting as engineering | Tyler | not started |
| `LSN-2.3` | Embeddings & vector search | Tyler | not started |
| `LSN-2.4` | Hands-on: build a RAG | Tyler | not started |
| `LSN-2.5` | Prompt vs RAG vs fine-tune | Tyler | not started |
| `LSN-2.6` | Limitations & what to promise a client | Tyler | not started |
| `LSN-3.1` | What is an agent | Tyler | not started |
| `LSN-3.2` | Framework landscape | Guest / TBD | not started |
| `LSN-3.3` | Cloud landscape | Per-cloud owners TBD | not started |
| `LSN-3.4` | Hands-on: build a tool-calling agent | Tyler | not started |
| `LSN-3.5` | Production concerns | Tyler + guest | not started |
| `LSN-3.6` | Real VSP cases, end to end | Vlad + Dorel + Tyler | not started |

Status vocabulary (matches `TEMPLATE.md` frontmatter): `not started → draft → reviewed → approved → delivered`. Update this board whenever a plan changes status.

## Suggested build order

1. **Week-1 lessons first** (`LSN-0.*`) — they run soonest and carry `GAP-1`.
2. **The two P0 hands-on labs** (`LSN-1.4`, `LSN-3.4`) — longest lead time, existing notebooks to adapt.
3. **The center of gravity** (`LSN-3.2`, `LSN-3.3`, `LSN-3.5`) — new content plus owner recruitment.
4. Everything else in calendar order.
