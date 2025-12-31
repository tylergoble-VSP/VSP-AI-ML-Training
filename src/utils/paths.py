"""
Used in: ALL scripts writing files to disk.
Purpose:
    Provide a single, consistent mechanism for generating timestamped paths.
    
Educational Context:
    This module demonstrates several important Python concepts:
    1. Path handling using pathlib (modern, cross-platform file path operations)
    2. String formatting with f-strings (Python 3.6+ feature)
    3. Function design for reusability and consistency
    4. Type hints for better code documentation and IDE support
    
    Why timestamped files?
    - Prevents overwriting previous outputs
    - Enables tracking of results over time
    - Makes it easy to compare different runs
    - Essential for reproducibility in data science workflows
"""

# Import pathlib.Path: This is Python's modern way to handle file paths
# Unlike string paths, Path objects work across Windows, Mac, and Linux
# Path objects have methods like .mkdir(), .exists(), and support the / operator
from pathlib import Path

# Import datetime: Python's built-in module for working with dates and times
# We use this to generate timestamps that are unique and sortable
from datetime import datetime


def timestamp() -> str:
    """
    Create a timestamp string in the format YYYYMMDD_HHMMSS.
    
    Educational Explanation:
        This function demonstrates:
        1. Function definition with type hints (-> str means returns a string)
        2. Using datetime.now() to get the current system time
        3. Using strftime() to format dates into strings
        4. Why this format? YYYYMMDD_HHMMSS is:
           - Sortable alphabetically (later dates come after earlier ones)
           - No spaces or special characters (safe for filenames)
           - Human-readable (you can tell when it was created)
    
    Returns:
        A formatted timestamp string like "20251230_143022"
        
    Example:
        >>> timestamp()
        '20251230_143022'
    """
    # datetime.now() gets the current date and time from the system clock
    # This returns a datetime object with year, month, day, hour, minute, second, etc.
    current_time = datetime.now()
    
    # strftime() stands for "string format time" - it converts a datetime object to a string
    # The format codes:
    #   %Y = 4-digit year (e.g., 2025)
    #   %m = 2-digit month (01-12)
    #   %d = 2-digit day (01-31)
    #   %H = 2-digit hour in 24-hour format (00-23)
    #   %M = 2-digit minute (00-59)
    #   %S = 2-digit second (00-59)
    # The underscore (_) is a literal character that separates date from time
    # This format ensures filenames are sortable and filename-safe
    formatted_timestamp = current_time.strftime("%Y%m%d_%H%M%S")
    
    # Return the formatted string to the caller
    return formatted_timestamp


def timestamped_path(base_folder: str, base_name: str, ext: str) -> Path:
    """
    Generate a timestamped file path inside base_folder.
    
    Educational Explanation:
        This function demonstrates:
        1. Function parameters with type hints
        2. Path object creation and manipulation
        3. Directory creation with error handling
        4. String formatting with f-strings
        5. Path concatenation using the / operator
        
        Why create directories automatically?
        - Prevents errors when writing files
        - Makes code more robust (doesn't fail if folder doesn't exist)
        - Follows the principle of "make it work, make it easy"
        
        Why use Path objects instead of strings?
        - Cross-platform compatibility (Windows uses \, Unix uses /)
        - Better error handling
        - More readable code
    
    Args:
        base_folder: Directory where file will be stored (e.g., "outputs/results")
        base_name: Descriptive filename prefix (e.g., "model_predictions")
        ext: File extension without dot (e.g., 'csv', 'json', 'txt')
            Note: We don't include the dot because we add it in the f-string
    
    Returns:
        A Path object for the timestamped file (e.g., outputs/results/model_predictions_20251230_143022.csv)
        
    Example:
        >>> path = timestamped_path("outputs/results", "data", "csv")
        >>> print(path)
        outputs/results/data_20251230_143022.csv
    """
    # Convert the string path to a Path object
    # Path() constructor accepts strings and converts them to Path objects
    # This is safe even if the path doesn't exist yet
    folder = Path(base_folder)
    
    # Create the directory if it doesn't exist
    # mkdir() creates a directory, but raises an error if parent directories don't exist
    # parents=True tells it to create all parent directories too (like mkdir -p in bash)
    # exist_ok=True means "don't raise an error if the directory already exists"
    # This is important because:
    #   - Without parents=True, creating "outputs/logs" would fail if "outputs" doesn't exist
    #   - Without exist_ok=True, the function would crash if run twice
    folder.mkdir(parents=True, exist_ok=True)
    
    # Generate a timestamp string using our helper function
    # This ensures every file gets a unique timestamp
    ts = timestamp()
    
    # Construct the filename using an f-string (formatted string literal)
    # f-strings are Python 3.6+ feature that embeds expressions inside strings
    # Syntax: f"text {variable} more text"
    # The curly braces {} contain Python expressions that are evaluated
    # We format it as: base_name_timestamp.extension
    # Example: "results_20251230_143022.csv"
    filename = f"{base_name}_{ts}.{ext}"
    
    # Combine the folder path and filename using the / operator
    # Path objects support the / operator for path concatenation
    # This is much cleaner than using os.path.join() or string concatenation
    # The / operator automatically handles the correct path separator for the OS
    # Example: Path("outputs/results") / "data.csv" = Path("outputs/results/data.csv")
    full_path = folder / filename
    
    # Return the complete Path object
    # The caller can use this Path object to:
    #   - Write to the file: full_path.write_text("content")
    #   - Check if it exists: full_path.exists()
    #   - Convert to string: str(full_path)
    return full_path

