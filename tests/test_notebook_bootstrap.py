"""
Guard tests for notebook bootstrap cells.
"""

# stdlib json (parse notebook files)
import json
# stdlib pathlib (filesystem paths)
from pathlib import Path


REQUIRED_BOOTSTRAP_LINES = [
    "# stdlib pathlib (filesystem paths)",
    "from pathlib import Path",
    "# src/utils/pathing.py",
    "from src.utils.pathing import ensure_repo_root_on_sys_path  # src/utils/pathing.py",
    "ensure_repo_root_on_sys_path(Path.cwd())",
]


def _first_code_cell_source(notebook_path: Path) -> str:
    """Return the concatenated source of the first code cell in a notebook."""
    data = json.loads(notebook_path.read_text(encoding="utf-8"))
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "code":
            return "".join(cell.get("source", []))
    return ""


def test_notebooks_have_standard_bootstrap_cell() -> None:
    """All notebooks must start with the repo-root bootstrap snippet."""
    notebook_paths = sorted(Path("notebooks").rglob("*.ipynb"))
    missing = []
    for notebook_path in notebook_paths:
        first_code = _first_code_cell_source(notebook_path)
        if not all(line in first_code for line in REQUIRED_BOOTSTRAP_LINES):
            missing.append(str(notebook_path))

    assert not missing, f"Missing bootstrap cell in: {', '.join(missing)}"
