"""
Unit tests for src/utils/timing.py

Educational Context:
    This file demonstrates unit testing with pytest.
    
    Testing Concepts:
    1. Unit Tests: Test individual functions in isolation
    2. Assertions: Check that code behaves correctly
    3. Fixtures: Reusable test data (from conftest.py)
    4. Test Functions: Must start with "test_"
    
    Why test?
    - Catch bugs before they reach production
    - Ensure code works as expected
    - Document expected behavior
    - Enable refactoring with confidence
    - Regression testing (prevent old bugs from returning)
    
    Test Structure:
    - Arrange: Set up test data
    - Act: Execute the code being tested
    - Assert: Verify the result is correct
"""
import pytest  # Testing framework
import time  # For timing operations
import csv  # For reading CSV logs
from pathlib import Path  # For file path operations
from src.utils.timing import timeit, TimeBlock  # Functions being tested


def test_timeit_decorator():
    """
    Test that @timeit decorator measures execution time.
    
    Educational Explanation:
        This test verifies that the @timeit decorator:
        1. Doesn't change the function's return value
        2. Still executes the function correctly
        3. Adds timing functionality without breaking behavior
        
        Test strategy:
        - Create a simple function that returns a known value (42)
        - Apply @timeit decorator
        - Verify return value is unchanged
        - Timing happens in background (we don't check it here)
    """
    # Define a test function with @timeit decorator
    # @timeit adds timing functionality without changing function behavior
    @timeit
    def test_function():
        # Sleep for 0.1 seconds to ensure measurable time
        # This makes the timing more reliable
        time.sleep(0.1)
        return 42  # Known return value for testing
    
    # Call the decorated function
    result = test_function()
    
    # Assert that return value is unchanged
    # This verifies decorator doesn't break function behavior
    # assert statement: if condition is False, test fails
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

