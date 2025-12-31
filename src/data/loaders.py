"""
Used in: Multiple notebooks (02_Intermediate_Python, 04-11)
Purpose:
    Provide standardized data-loading functions to keep notebooks clean and modular.
    Handles CSV files, scikit-learn datasets, and text files.
    
Educational Context:
    This module demonstrates:
    1. File I/O (Input/Output) operations
    2. Working with different file formats (CSV, text)
    3. Path handling with pathlib
    4. Data structures (DataFrames, lists, strings)
    5. Optional parameters and type hints
    
    Why separate data loading into functions?
    - Reusability: Use same loading code in multiple places
    - Consistency: Same error handling and formatting everywhere
    - Testability: Easy to test loading logic separately
    - Clean notebooks: Keep notebooks focused on analysis, not file I/O
"""

# Import pandas: The primary library for working with tabular data in Python
# DataFrame is like a spreadsheet: rows (samples) and columns (features)
# Provides powerful data manipulation, filtering, and analysis tools
import pandas as pd

# Import Optional from typing: Allows parameters that can be None or a specific type
# Example: Optional[int] means "int or None"
# This documents that a parameter is optional
from typing import Optional

# Import Path from pathlib: Modern, object-oriented way to handle file paths
# Works across Windows, Mac, and Linux automatically
# More robust than string concatenation for paths
from pathlib import Path


def load_csv(path: str, nrows: Optional[int] = None) -> pd.DataFrame:
    """
    Load a CSV file as a DataFrame.
    
    Educational Explanation:
        CSV (Comma-Separated Values) is a simple text format for tabular data.
        Each line is a row, values are separated by commas.
        
        Example CSV:
        name,age,city
        Alice,30,New York
        Bob,25,London
        
        Pandas read_csv() automatically:
        - Detects headers (first row)
        - Parses numbers (converts "30" to integer 30)
        - Handles missing values (empty cells become NaN)
        - Infers data types (int, float, string)
    
    Args:
        path: Path to the CSV file (string)
             Example: "data/iris.csv" or "/absolute/path/to/file.csv"
        nrows: Optional number of rows to read
              None = read entire file
              Integer = read only first n rows
              Useful for:
              - Quick preview of large files
              - Testing code without loading full dataset
              - Memory management (avoid loading huge files)
    
    Returns:
        DataFrame containing the loaded data
        DataFrame has:
        - .shape: (rows, columns) dimensions
        - .head(): Preview first few rows
        - .columns: Column names
        - .dtypes: Data types of each column
    
    Example:
        >>> df = load_csv("data/iris.csv")
        >>> print(df.shape)
        (150, 5)
    """
    # Use pandas read_csv() to load the file
    # pandas automatically handles:
    # - Detecting delimiter (comma, semicolon, tab, etc.)
    # - Parsing dates and numbers
    # - Handling missing values
    # - Inferring data types
    
    # nrows parameter:
    # - If None: reads entire file (default behavior)
    # - If integer: reads only first n rows
    # This is useful for large files where you want a quick preview
    # or when testing code without loading the full dataset
    df = pd.read_csv(path, nrows=nrows)
    
    # Return the DataFrame to the caller
    # The caller can now use this DataFrame for analysis, visualization, etc.
    return df


def load_text_file(path: str) -> str:
    """
    Load a text file and return its contents as a string.
    
    Educational Explanation:
        This function reads a text file and returns its entire contents as a string.
        Useful for:
        - Reading configuration files
        - Loading documents for NLP (Natural Language Processing)
        - Reading code or scripts
        - Loading any plain text content
    
    Args:
        path: Path to the text file (string)
             Example: "data/document.txt"
    
    Returns:
        String containing the entire file contents
        Includes all newlines, spaces, and characters exactly as in file
    
    Example:
        >>> content = load_text_file("data/readme.txt")
        >>> print(len(content))  # Number of characters
        1234
    """
    # Open file in read mode ("r") with UTF-8 encoding
    # "r" means read-only (we're not modifying the file)
    # encoding="utf-8" ensures proper handling of special characters
    # UTF-8 is the standard encoding that handles:
    # - English letters and numbers
    # - Accented characters (é, ñ, etc.)
    # - Emojis and symbols
    # - Characters from many languages
    
    # The 'with' statement is a context manager
    # It automatically closes the file when done (even if an error occurs)
    # This is important to avoid file handle leaks
    with open(path, "r", encoding="utf-8") as f:
        # Read the entire file contents into a string
        # .read() reads from current position to end of file
        # For a newly opened file, this means reading everything
        content = f.read()
    
    # Return the file contents as a string
    return content


def load_text_files(folder_path: str) -> list[str]:
    """
    Load all .txt files from a specified folder and return their contents as a list of strings.
    
    Educational Explanation:
        This function demonstrates:
        1. Directory traversal (finding files in a folder)
        2. File pattern matching (glob patterns)
        3. List accumulation (building a list by appending)
        4. Batch processing (processing multiple files)
        
        Use cases:
        - Loading multiple documents for text analysis
        - Processing a corpus of text files
        - Batch loading configuration files
        - NLP tasks requiring multiple documents
    
    Args:
        folder_path: Path to the folder containing .txt files
                    Example: "data/documents/" or "corpus/"
    
    Returns:
        List of strings, where each string is the content of one .txt file
        Order matches the order files are found (may vary by OS)
        Example: ["content of file1.txt", "content of file2.txt", ...]
    
    Example:
        >>> docs = load_text_files("data/documents/")
        >>> print(f"Loaded {len(docs)} documents")
        Loaded 5 documents
    """
    # List to accumulate the text contents of each file
    # We'll append each file's content to this list
    docs = []
    
    # Convert string path to Path object for easier manipulation
    # Path() constructor accepts strings and creates a Path object
    # Path objects have useful methods like .glob(), .exists(), etc.
    folder = Path(folder_path)
    
    # Use glob() to find all files matching a pattern
    # "*.txt" is a glob pattern meaning "any filename ending in .txt"
    # The * is a wildcard matching any characters
    # glob() returns an iterator of Path objects for matching files
    # Example: folder contains "doc1.txt", "doc2.txt", "readme.md"
    #          glob("*.txt") returns Path objects for doc1.txt and doc2.txt
    for path in folder.glob("*.txt"):
        # Open each matching file
        # path is a Path object, but open() accepts Path objects (converts automatically)
        # "r" = read mode, encoding="utf-8" = UTF-8 encoding
        with open(path, "r", encoding="utf-8") as f:
            # Read the entire file content as a string
            # .read() reads everything from current position to end
            # Append the content to our list
            # Each element in docs will be the full text of one file
            docs.append(f.read())
    
    # Return the list of all file contents
    # Each element corresponds to one .txt file from the folder
    return docs

