# Environment Setup

**This is `LSN-0.1` pre-work.** Do it before Tuesday 1 September. If it fails, **come to the session with
your error message** — segment 2 is 25 minutes of live triage and fixing your machine in the room is the
point, not a failure.

> **Read this first:** the repo does **not** ship a virtual environment. `.venv/` is in `.gitignore`, so a
> fresh clone has no Python environment at all — you create one below. (An earlier version of this file
> claimed the environment "has been created successfully." It was not true for anyone who cloned the repo,
> and that is exactly the kind of claim `LSN-0.2` teaches you to check.)

---

## What you need before you start

| | |
|---|---|
| **Python** | **3.12** — the notebooks are built and verified on 3.12.13 |
| **Disk** | ~350 MB for `MOD-0`, ~1 GB once `MOD-1` adds PyTorch |
| **Time** | 2–5 minutes with `uv`, or 5–10 minutes with `pip` |

Check what you have:

```bash
python3 --version
```

If that is not 3.12.x, install it — [python.org/downloads](https://www.python.org/downloads/), or
`brew install python@3.12` on a Mac, or your distribution's package manager. You do not need to make it
your system default; the next step points at it explicitly.

> **macOS note:** a bare `pip3` on your PATH is often Apple's system Python 3.9, not your 3.12. Every
> command below calls the interpreter *inside* the virtual environment by path, which avoids that trap
> entirely. If you find yourself typing plain `pip`, stop and re-read the command.

---

## Create the environment

### Option A — `uv` (recommended, and what the repo was built with)

[`uv`](https://docs.astral.sh/uv/) is a fast Python package manager. Install it once:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# or, on a Mac with Homebrew
brew install uv
```

Then, from the repo root:

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python numpy pandas matplotlib seaborn jupyterlab
```

### Option B — the standard library, no extra tooling

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install numpy pandas matplotlib seaborn jupyterlab
```

**On Windows**, replace `.venv/bin/python` with `.venv\Scripts\python.exe` in every command on this page.

---

## Verify it worked

```bash
.venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, jupyterlab; print('environment OK')"
```

Then run the orientation notebook, which is the real check — five checkpoints ending in the screenshot
that serves as your `ASM-0` setup evidence:

```bash
.venv/bin/jupyter lab notebooks/lessons/LSN-0.1_Orientation_Environment_Setup.ipynb
```

Choose **Run → Run All Cells**. All five checkpoints should print ✅.

**Verified working set** (what the committed notebook outputs were produced with):

| Package | Version |
|---|---|
| Python | 3.12.13 |
| numpy | 2.5.1 |
| pandas | 3.0.5 |
| matplotlib | 3.11.1 |
| seaborn | 0.13.2 |
| jupyterlab | 4.6.2 |

Newer point releases are fine. If a notebook behaves oddly, this table is what to compare against.

---

## Installing packages in stages — and why

**Do not run `pip install -r requirements.txt`.** That file is the *full-program* dependency list: it
pulls PyTorch, transformers, sentence-transformers, `llama-cpp-python`, `bitsandbytes` (which needs CUDA
and will fail on a Mac), FAISS, Neo4j and more. It is slow, it is failure-prone on a laptop, and
**`MOD-0` needs none of it.** Installing it on 31 August is the most common way to arrive at `LSN-0.1`
blocked.

Instead, install what the module in front of you actually needs:

| Stage | When | Install | Adds |
|---|---|---|---|
| **1 — `MOD-0`** | Before **1 Sep** | `numpy pandas matplotlib seaborn jupyterlab` | ~350 MB |
| **2 — `MOD-1`** | Before **28 Sep** (`LSN-1.4`, the MNIST lab) | `scikit-learn torch torchvision` | ~650 MB more (PyTorch alone is ~515 MB) |
| **3 — `MOD-2`/`MOD-3`** | From **October** | Announced with the lesson | The LLM stack |

Stage 2, when you get there:

```bash
uv pip install --python .venv/bin/python scikit-learn torch torchvision
# or:  .venv/bin/python -m pip install scikit-learn torch torchvision
```

**Datasets live outside the repo**, at `~/.cache/vsp-training-data` — the MNIST lab writes there rather
than into your clone, so training data never lands in a commit. The notebook creates it for you.

---

## Activating the environment (optional)

Nothing on this page requires activation — calling `.venv/bin/python` directly always works and is harder
to get wrong. But if you prefer an activated shell:

```bash
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\Activate.ps1         # Windows PowerShell
.venv\Scripts\activate.bat         # Windows Command Prompt
```

Your prompt gains a `(.venv)` prefix. Leave it with `deactivate`.

If PowerShell refuses to run the activation script:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## If it goes wrong

1. **Read the actual error.** The first traceback line matters more than the last.
2. **Wrong Python.** `.venv/bin/python --version` must say 3.12.x. If not, delete `.venv` and recreate it
   with an explicit `--python 3.12`.
3. **Start clean.** `rm -rf .venv` (Windows: `rmdir /s .venv`) and repeat the create step. Deleting the
   environment is free — it is gitignored and holds nothing of yours.
4. **A compiler error mentioning `Python.h`** means you are missing development headers on Linux — see
   [`INSTALL_TROUBLESHOOTING.md`](INSTALL_TROUBLESHOOTING.md). *(That file currently covers Linux only and
   is written around a package this staged setup no longer installs; if you are on macOS or Windows and
   stuck, bring the error to the session rather than fighting it alone.)*
5. **Still stuck?** Stop. Bring the error message to `LSN-0.1`. Twenty-five minutes of that hour exist for
   exactly this, and a machine that is fixed in the room on day one is worth more than a weekend lost to
   it alone.

---

## Why a virtual environment at all

An isolated Python environment keeps this project's packages separate from your system Python and from
your other projects. It buys four things:

- **Isolation** — this project's versions cannot break another project.
- **Reproducibility** — everyone runs the same versions, so a notebook that works for one person works
  for the next. This is why the verified-versions table above exists.
- **A clean system** — nothing here touches your system Python.
- **Disposability** — the most useful property. When something breaks, delete `.venv` and rebuild it in
  under a minute. You will do this at least once, and it is not a setback.

That last point is the one worth carrying into the rest of the program: **an environment you can throw
away and rebuild is an environment you can trust.** It is the same instinct as pinning a seed
(`LSN-0.4`) or writing down how a sample was collected (`LSN-0.2`) — reproducibility is a practice, not a
package.
