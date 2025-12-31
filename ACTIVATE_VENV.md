# Activating the Virtual Environment

## Educational Context

A virtual environment is an isolated Python environment that keeps project dependencies separate from your system Python installation. This prevents conflicts between different projects that might need different versions of the same package.

**Why use virtual environments?**
- **Isolation**: Each project has its own packages
- **Version Control**: Different projects can use different package versions
- **Clean System**: Keeps your system Python installation clean
- **Reproducibility**: Ensures everyone uses the same environment

The virtual environment (`.venv`) has been created successfully. Here's how to activate it:

## On Linux/Mac:

```bash
source .venv/bin/activate
```

## On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

## On Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

## Verify Activation

After activating, you should see `(.venv)` at the beginning of your command prompt:

```bash
(.venv) user@machine:~/VSP-AI-ML-Training$
```

## If You Get Permission Errors

If you see errors about permissions or execution policies:

1. **On Linux/Mac**: Make sure the activate script is executable:
   ```bash
   chmod +x .venv/bin/activate
   ```

2. **On Windows PowerShell**: You may need to set the execution policy:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

## Install Dependencies

Once activated, install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Deactivate

To deactivate the virtual environment when you're done:

```bash
deactivate
```

