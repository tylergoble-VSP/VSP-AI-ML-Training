"""
Unit tests for src/utils/timing.py
"""
import pytest
import time
import csv
from pathlib import Path
from src.utils.timing import timeit, TimeBlock


def test_timeit_decorator():
    """Test that @timeit decorator measures execution time"""
    @timeit
    def test_function():
        time.sleep(0.1)
        return 42
    
    result = test_function()
    assert result == 42, "Decorator should not modify return value"


def test_timeit_logs_to_file():
    """Test that @timeit logs to CSV file"""
    # Clear any existing log
    log_path = Path("outputs/logs")
    log_path.mkdir(parents=True, exist_ok=True)
    
    @timeit
    def test_function():
        return "test"
    
    test_function()
    
    # Check that log file exists (may have timestamp in name)
    log_files = list(log_path.glob("timing_*.csv"))
    assert len(log_files) > 0, "Log file should be created"


def test_timeblock_context_manager():
    """Test TimeBlock context manager"""
    with TimeBlock("test_operation") as tb:
        time.sleep(0.05)
        assert tb.operation_name == "test_operation"
    
    # Check that log was written
    log_path = Path("outputs/logs")
    log_files = list(log_path.glob("timing_*.csv"))
    assert len(log_files) > 0, "Log file should exist"


def test_timeblock_doesnt_suppress_exceptions():
    """Test that TimeBlock doesn't suppress exceptions"""
    with pytest.raises(ValueError):
        with TimeBlock("test"):
            raise ValueError("Test exception")

