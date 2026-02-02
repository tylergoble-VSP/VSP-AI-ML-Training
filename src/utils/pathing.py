"""Utilities for locating the repository root and bootstrapping sys.path.

This module keeps notebook imports reliable when the working directory
is inside `notebooks/` or another subfolder.
"""

# stdlib pathlib (filesystem paths)
from pathlib import Path
# stdlib sys (Python path management)
import sys
# stdlib typing (type hints)
from typing import Sequence


def find_repo_root(
    start_path: Path,
    marker_dirs: Sequence[str] = ("src",),
    marker_files: Sequence[str] = ("README.md", "PROGRESS.md"),
) -> Path:
    """Find the repository root by walking up from a starting path.

    Args:
        start_path: File or directory path to start searching from.
        marker_dirs: Directory names that indicate a repo root.
        marker_files: File names that indicate a repo root.

    Returns:
        The resolved repo root path.

    Raises:
        ValueError: If no repo root can be found.
    """
    resolved_start = start_path.resolve()
    search_path = resolved_start if resolved_start.is_dir() else resolved_start.parent

    for candidate in [search_path, *search_path.parents]:
        has_marker_dir = any((candidate / marker).is_dir() for marker in marker_dirs)
        has_marker_file = any((candidate / marker).is_file() for marker in marker_files)
        if has_marker_dir or has_marker_file:
            return candidate

    raise ValueError(
        "Repository root not found. Expected a parent directory with "
        f"{', '.join(marker_dirs)} or {', '.join(marker_files)}."
    )


def ensure_repo_root_on_sys_path(start_path: Path) -> Path:
    """Add the repo root to sys.path so `import src...` works in notebooks.

    Args:
        start_path: File or directory path to start searching from.

    Returns:
        The resolved repo root path that was added (or already present).
    """
    repo_root = find_repo_root(start_path)
    repo_root_str = str(repo_root)
    if repo_root_str not in sys.path:
        sys.path.insert(0, repo_root_str)
    return repo_root
