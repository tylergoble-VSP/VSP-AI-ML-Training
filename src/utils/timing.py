"""
Used in: Analytics notebooks and any performance-critical workflows.
Purpose:
    Provide decorators and context managers for recording execution time.
    Automatically logs results into timestamped CSV files.
    
Educational Context:
    This module demonstrates two advanced Python concepts:
    1. Decorators: Functions that modify other functions
    2. Context Managers: Objects that manage resources with 'with' statements
    
    Why measure execution time?
    - Identify performance bottlenecks
    - Compare different algorithms
    - Track performance improvements over time
    - Understand scalability (how time grows with data size)
    
    Decorators vs Context Managers:
    - Decorators: Best for timing entire functions
    - Context Managers: Best for timing code blocks within functions
"""

# Import time module: Provides time.time() which returns seconds since Unix epoch (Jan 1, 1970)
# We use this to capture timestamps before and after code execution
import time

# Import csv module: Python's built-in module for reading/writing CSV files
# CSV (Comma-Separated Values) is a simple text format for tabular data
# We use this to log timing data in a format that's easy to analyze later
import csv

# Import Path from pathlib: For robust, cross-platform file path handling
from pathlib import Path

# Import our timestamped_path function: Ensures each log file has a unique name
from src.utils.paths import timestamped_path

# Global variable to store the log file path
# Using None initially means "not created yet" - this is a common Python pattern
# We use lazy initialization: create the path only when first needed
# This is better than creating it at import time because:
#   1. The outputs directory might not exist when the module is imported
#   2. We want a fresh timestamp each time the script runs, not when Python loads the module
LOG_PATH = None


def _get_log_path():
    """
    Get or create the log path using lazy initialization pattern.
    
    Educational Explanation:
        This function demonstrates:
        1. Global variables and the 'global' keyword
        2. Lazy initialization (create only when needed)
        3. The singleton pattern (one log file per Python session)
        
        Why use a global variable here?
        - We want all timing operations to write to the same file
        - Creating a new file for each timing would be wasteful
        - The global variable ensures consistency across all timing calls
    
    Returns:
        Path object pointing to the timing log file
    """
    # Declare we're modifying the global LOG_PATH variable
    # Without 'global', Python would create a local variable instead
    # This is necessary because we're assigning to LOG_PATH (LOG_PATH = ...)
    global LOG_PATH
    
    # Check if we've already created the log path
    # If LOG_PATH is None, this is the first time we're timing something
    if LOG_PATH is None:
        # Create a timestamped path for the log file
        # This ensures each script run gets its own log file
        # Format: outputs/logs/timing_YYYYMMDD_HHMMSS.csv
        LOG_PATH = timestamped_path("outputs/logs", "timing", "csv")
    
    # Return the log path (either newly created or previously created)
    return LOG_PATH


def timeit(fn):
    """
    Decorator that measures how long a function takes to execute.
    
    Educational Explanation:
        This demonstrates Python decorators - a powerful feature that allows
        you to modify or enhance functions without changing their code.
        
        How decorators work:
        1. A decorator is a function that takes a function as input
        2. It returns a new function (wrapper) that does something extra
        3. The wrapper calls the original function and adds timing logic
        
        Why use decorators?
        - Separation of concerns: timing logic separate from business logic
        - Reusability: apply timing to any function with @timeit
        - Non-invasive: don't need to modify the original function
        
        Usage:
            @timeit
            def my_function():
                # your code here
                pass
    
    Args:
        fn: The function being decorated (the original function to time)
    
    Returns:
        A wrapped version of fn that logs its execution time before returning
    
    Example:
        @timeit
        def train_model():
            # This function will automatically be timed
            model.fit(X, y)
    """
    # Define the wrapper function that will replace the original function
    # *args and **kwargs allow the wrapper to accept any arguments
    # *args = positional arguments (like my_func(1, 2, 3))
    # **kwargs = keyword arguments (like my_func(x=1, y=2))
    # This makes the decorator work with any function signature
    def wrapper(*args, **kwargs):
        # Record the start time using time.time()
        # time.time() returns the current time as a float (seconds since epoch)
        # We store this before executing the function
        start = time.time()
        
        # Execute the original function with all its arguments
        # This is where the actual work happens
        # We capture the result so we can return it unchanged
        result = fn(*args, **kwargs)
        
        # Calculate how long the function took to execute
        # Subtract start time from current time to get duration in seconds
        duration = time.time() - start
        
        # Get the log file path (creates it if needed)
        log_path = _get_log_path()
        
        # Open the log file in append mode ("a")
        # Append mode means: add to the end of the file, don't overwrite
        # This allows multiple timing calls to write to the same file
        # newline="" is required for CSV writing on Windows (prevents extra blank lines)
        # The 'with' statement ensures the file is closed automatically
        with open(log_path, "a", newline="") as f:
            # Create a CSV writer object
            # This handles proper formatting (commas, quotes, etc.)
            writer = csv.writer(f)
            
            # Write a row with three columns:
            #   1. Function name (fn.__name__ gets the function's name as a string)
            #   2. Duration in seconds (how long it took)
            #   3. Timestamp (when it finished, for tracking over time)
            writer.writerow([fn.__name__, duration, time.time()])
        
        # Return the original function's result unchanged
        # This is crucial: the decorator shouldn't change the function's behavior
        # It only adds timing, it doesn't modify the output
        return result
    
    # Return the wrapper function
    # When Python sees @timeit, it calls timeit(my_function) and uses the returned wrapper
    return wrapper


class TimeBlock:
    """
    Context manager for timing a block of code.
    
    Educational Explanation:
        This demonstrates context managers - Python's way of managing resources
        (files, locks, database connections, etc.) with automatic cleanup.
        
        How context managers work:
        1. __enter__() is called when entering the 'with' block
        2. Your code executes
        3. __exit__() is called when leaving the 'with' block (even if there's an error)
        
        Why use context managers?
        - Automatic cleanup (files closed, locks released)
        - Exception safety (cleanup happens even if code crashes)
        - Cleaner code than try/finally blocks
        
        Usage:
            with TimeBlock("my_operation"):
                # code to time
                model.fit(X, y)
    
    Example:
        with TimeBlock("data_loading"):
            data = load_large_dataset()
        # Timing is automatically logged when we exit the block
    """
    
    def __init__(self, operation_name: str):
        """
        Initialize the time block with an operation name.
        
        Educational Explanation:
            __init__ is the constructor method - called when creating a new object
            'self' refers to the instance being created
            We store the operation name so we can use it later when logging
        
        Args:
            operation_name: Descriptive name for the operation being timed
                          (e.g., "model_training", "data_preprocessing")
        """
        # Store the operation name as an instance variable
        # self.operation_name means "this object's operation_name attribute"
        # We'll use this later to label the timing entry in the log
        self.operation_name = operation_name
        
        # Initialize start_time to None (not started yet)
        # We'll set this in __enter__ when timing actually begins
        self.start_time = None
    
    def __enter__(self):
        """
        Start timing when entering the context.
        
        Educational Explanation:
            This method is called automatically when Python enters the 'with' block
            It's part of the context manager protocol (the rules Python follows)
            The return value is assigned to the variable after 'as' (if used)
        
        Returns:
            self (the TimeBlock object itself)
        """
        # Record the current time as the start time
        # This marks when we entered the 'with' block
        self.start_time = time.time()
        
        # Return self so the caller can access the TimeBlock object if needed
        # Example: with TimeBlock("op") as tb: print(tb.operation_name)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop timing and log the duration when exiting the context.
        
        Educational Explanation:
            This method is called automatically when Python exits the 'with' block
            It's called even if an exception occurs (that's why it's so useful!)
            
            The parameters are for exception handling:
            - exc_type: The exception class (e.g., ValueError)
            - exc_val: The exception instance
            - exc_tb: The traceback object
            
            Return value:
            - False (or None): Let the exception propagate (normal behavior)
            - True: Suppress the exception (rare, usually not recommended)
        
        Args:
            exc_type: Exception type if an exception occurred, None otherwise
            exc_val: Exception value if an exception occurred, None otherwise
            exc_tb: Traceback if an exception occurred, None otherwise
        """
        # Calculate how long the code block took to execute
        # Subtract start time from current time to get duration in seconds
        duration = time.time() - self.start_time
        
        # Get the log file path (creates it if needed)
        log_path = _get_log_path()
        
        # Open the log file in append mode
        # Append mode means we add to the end, preserving previous entries
        # newline="" prevents extra blank lines on Windows
        # The 'with' statement ensures the file is closed automatically
        with open(log_path, "a", newline="") as f:
            # Create a CSV writer for proper formatting
            writer = csv.writer(f)
            
            # Write a row with three columns:
            #   1. Operation name (descriptive label for what was timed)
            #   2. Duration in seconds (how long it took)
            #   3. Timestamp (when it finished, for chronological tracking)
            writer.writerow([self.operation_name, duration, time.time()])
        
        # Return False to indicate we don't want to suppress exceptions
        # If an exception occurred in the 'with' block, it will be raised normally
        # This is the standard behavior - we just add timing, we don't hide errors
        return False

