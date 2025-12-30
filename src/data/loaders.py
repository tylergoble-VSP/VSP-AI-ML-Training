"""
Used in: Multiple notebooks (02_Intermediate_Python, 04-11)
Purpose:
    Provide standardized data-loading functions to keep notebooks clean and modular.
    Handles CSV files, scikit-learn datasets, and text files.
"""

import pandas as pd  # Pandas is the main library for working with tabular data
from typing import Optional  # Optional allows parameters that may be None
from pathlib import Path  # Object-oriented path handling


def load_csv(path: str, nrows: Optional[int] = None) -> pd.DataFrame:
    """
    Load a CSV file as a DataFrame.

    Args:
        path: Path to the CSV file.
        nrows: Number of rows to read (None means read entire file).

    Returns:
        DataFrame containing the data.
    """
    # Use pandas to load the file.
    # nrows makes large files easier to preview or test.
    df = pd.read_csv(path, nrows=nrows)

    # Return the DataFrame to the caller
    return df


def load_text_file(path: str) -> str:
    """
    Load a text file and return its contents as a string.

    Args:
        path: Path to the text file.

    Returns:
        String containing the file contents.
    """
    # Open file in read mode with UTF-8 encoding
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    return content


def load_text_files(folder_path: str) -> list[str]:
    """
    Load all .txt files from a specified folder and return their contents as a list of strings.

    Args:
        folder_path: The folder containing .txt files.

    Returns:
        A list where each element corresponds to the content of a file.
    """
    docs = []  # Will accumulate the text contents of each file

    # pathlib.Path(...) converts the string path into a Path object for easier traversal
    for path in Path(folder_path).glob("*.txt"):
        # 'glob("*.txt")' returns all files with a .txt extension
        with open(path, "r", encoding="utf-8") as f:
            # Read the entire file into memory as a string
            docs.append(f.read())

    return docs  # Return the full list of text documents

