"""
Unit tests for src/utils/pathing.py
"""

# pytest (testing framework)
import pytest
# stdlib pathlib (filesystem paths)
from pathlib import Path
# stdlib sys (Python path management)
import sys

# src/utils/pathing.py
from src.utils.pathing import find_repo_root, ensure_repo_root_on_sys_path


def test_find_repo_root_detects_src_marker(tmp_path: Path) -> None:
    """It finds the repo root by walking up to a folder that contains src."""
    repo_root = tmp_path / "example_repo"
    notebooks_dir = repo_root / "notebooks" / "ensemble"
    src_dir = repo_root / "src"
    readme_file = repo_root / "README.md"

    notebooks_dir.mkdir(parents=True)
    src_dir.mkdir()
    readme_file.write_text("# Example Repo", encoding="utf-8")

    detected_root = find_repo_root(notebooks_dir)

    assert detected_root == repo_root


def test_find_repo_root_raises_when_missing(tmp_path: Path) -> None:
    """It raises a helpful error when no repo markers exist."""
    orphan_dir = tmp_path / "orphan"
    orphan_dir.mkdir()

    with pytest.raises(ValueError, match="Repository root not found"):
        find_repo_root(orphan_dir)


def test_ensure_repo_root_on_sys_path_adds_path(tmp_path: Path) -> None:
    """It inserts the repo root at the front of sys.path when missing."""
    repo_root = tmp_path / "example_repo"
    src_dir = repo_root / "src"
    src_dir.mkdir(parents=True)

    original_sys_path = list(sys.path)
    try:
        detected_root = ensure_repo_root_on_sys_path(repo_root)
        assert detected_root == repo_root
        assert str(repo_root) in sys.path
    finally:
        sys.path[:] = original_sys_path
