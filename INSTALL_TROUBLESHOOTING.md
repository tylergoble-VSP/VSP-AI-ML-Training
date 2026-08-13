# Installation Troubleshooting

> **Scope note.** This file covers a Linux build-headers failure hit by the *legacy* full dependency
> list (`requirements-full.txt`). The training program no longer installs that list — see
> [`ACTIVATE_VENV.md`](ACTIVATE_VENV.md) for the staged setup, which does not compile anything from
> source and is what you should be following. If you are on macOS or Windows and stuck, the fastest
> path is to bring the error to `LSN-0.1`; 25 minutes of that session exist for exactly this.

## Issue: Failed to build scikit-survival and ecos

If you see errors like:
```
fatal error: Python.h: No such file or directory
```

This means Python development headers are missing.

### Solution

Install the Python development headers:

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-dev python3.12-dev build-essential
```

**On Fedora/RHEL:**
```bash
sudo dnf install python3-devel gcc gcc-c++
```

**On Arch Linux:**
```bash
sudo pacman -S python python-pip base-devel
```

### After Installing Headers

1. Retry the installation:
   ```bash
   source .venv/bin/activate
   .venv/bin/python -m pip install -r requirements-full.txt
   ```

2. If you want to install scikit-survival (optional), uncomment it in requirements-full.txt:
   ```bash
   # Edit requirements-full.txt and uncomment:
   # scikit-survival>=0.19.0
   ```

### Alternative: Skip scikit-survival

The `scikit-survival` package is optional. The survival analysis module (09_Survival_Analysis.ipynb) uses `lifelines` which is already installed. You can skip `scikit-survival` if you don't need it.

### Verify Installation

After installing headers and retrying:
```bash
python -c "import lifelines; print('lifelines OK')"
python -c "import sklearn; print('scikit-learn OK')"
```

