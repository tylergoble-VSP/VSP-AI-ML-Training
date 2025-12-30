# Installation Troubleshooting

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
   pip install -r requirements.txt
   ```

2. If you want to install scikit-survival (optional), uncomment it in requirements.txt:
   ```bash
   # Edit requirements.txt and uncomment:
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

