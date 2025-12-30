"""
Used in: Analytics notebooks and any performance-critical workflows.
Purpose:
    Provide decorators and context managers for recording execution time.
    Automatically logs results into timestamped CSV files.
"""

import time  # Used for capturing timestamps before/after execution
import csv  # For writing time logs as CSV
from pathlib import Path  # Robust path handling for cross-platform support
from src.utils.paths import timestamped_path  # Centralized timestamped output paths

# Generate a timestamped log file name for each run.
# This ensures logs never overwrite each other.
# Note: This will be created on first use
LOG_PATH = None

def _get_log_path():
    """Get or create the log path."""
    global LOG_PATH
    if LOG_PATH is None:
        LOG_PATH = timestamped_path("outputs/logs", "timing", "csv")
    return LOG_PATH


def timeit(fn):
    """
    Decorator that measures how long a function takes to execute.

    Args:
        fn: The function being decorated.

    Returns:
        A wrapped version of fn that logs its execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()  # Start the timer

        result = fn(*args, **kwargs)  # Execute the wrapped function

        duration = time.time() - start  # Compute elapsed time

        # Append a row containing the function name, duration, and timestamp.
        log_path = _get_log_path()
        with open(log_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([fn.__name__, duration, time.time()])

        return result  # Return original function output

    return wrapper  # Return the wrapper to be used as decorator


class TimeBlock:
    """
    Context manager for timing a block of code.

    Usage:
        with TimeBlock("my_operation"):
            # code to time
            pass
    """
    def __init__(self, operation_name: str):
        """
        Initialize the time block with an operation name.

        Args:
            operation_name: Descriptive name for the operation being timed.
        """
        self.operation_name = operation_name
        self.start_time = None

    def __enter__(self):
        """Start timing when entering the context."""
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop timing and log the duration when exiting the context."""
        duration = time.time() - self.start_time

        # Log the timing information
        log_path = _get_log_path()
        with open(log_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.operation_name, duration, time.time()])

        return False  # Don't suppress exceptions

