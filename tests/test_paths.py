"""
Unit tests for src/utils/paths.py
"""
import pytest
from pathlib import Path
from src.utils.paths import timestamp, timestamped_path
import re


def test_timestamp_format():
    """Test that timestamp returns correct format YYYYMMDD_HHMMSS"""
    ts = timestamp()
    # Should match pattern: 8 digits, underscore, 6 digits
    assert re.match(r'^\d{8}_\d{6}$', ts), f"Timestamp {ts} does not match format YYYYMMDD_HHMMSS"


def test_timestamped_path_creates_directory():
    """Test that timestamped_path creates directory if it doesn't exist"""
    test_folder = "outputs/test_paths"
    path = timestamped_path(test_folder, "test", "txt")
    
    # Check that directory was created
    assert Path(test_folder).exists(), "Directory should be created"
    
    # Cleanup
    if Path(test_folder).exists():
        Path(test_folder).rmdir()


def test_timestamped_path_format():
    """Test that timestamped_path returns correct format"""
    test_folder = "outputs/test_paths"
    path = timestamped_path(test_folder, "test", "csv")
    
    # Check format: test_YYYYMMDD_HHMMSS.csv
    assert path.name.startswith("test_"), "Filename should start with base_name"
    assert path.name.endswith(".csv"), "Filename should end with extension"
    assert re.match(r'^test_\d{8}_\d{6}\.csv$', path.name), f"Filename {path.name} has incorrect format"
    
    # Cleanup
    if Path(test_folder).exists():
        Path(test_folder).rmdir()


def test_timestamped_path_returns_path():
    """Test that timestamped_path returns a Path object"""
    test_folder = "outputs/test_paths"
    path = timestamped_path(test_folder, "test", "txt")
    
    assert isinstance(path, Path), "Should return Path object"
    
    # Cleanup
    if Path(test_folder).exists():
        Path(test_folder).rmdir()

