"""
Used in: 03_Advanced_Python, 05_Supervised_Learning, 06_Classifier_Algorithms
Purpose:
    Provide data preprocessing utilities for NumPy arrays and Pandas DataFrames.
    Includes scaling, encoding, and basic transformations.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from sklearn.preprocessing import StandardScaler, LabelEncoder  # Scikit-learn preprocessing tools
from typing import Union, Optional  # Type hints for flexible input types


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """
    Normalize a NumPy array to have zero mean and unit variance.

    Args:
        arr: Input NumPy array.

    Returns:
        Normalized array with mean=0 and std=1.
    """
    # Compute mean and standard deviation
    mean = np.mean(arr)
    std = np.std(arr)

    # Avoid division by zero
    if std == 0:
        return arr - mean

    # Normalize: subtract mean, divide by std
    normalized = (arr - mean) / std

    return normalized


def scale_features(X: Union[pd.DataFrame, np.ndarray], fit: bool = True, scaler: Optional[StandardScaler] = None) -> tuple[np.ndarray, StandardScaler]:
    """
    Scale features using StandardScaler (zero mean, unit variance).

    Args:
        X: Input features (DataFrame or array).
        fit: Whether to fit a new scaler (True) or use existing one (False).
        scaler: Existing scaler to use if fit=False.

    Returns:
        Tuple of (scaled_features, scaler_object).
    """
    # Create new scaler if needed
    if fit or scaler is None:
        scaler = StandardScaler()
        scaled_X = scaler.fit_transform(X)
    else:
        # Use existing scaler to transform
        scaled_X = scaler.transform(X)

    return scaled_X, scaler


def encode_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Encode categorical columns using label encoding.

    Args:
        df: Input DataFrame.
        columns: List of column names to encode.

    Returns:
        DataFrame with encoded columns.
    """
    df_encoded = df.copy()  # Don't modify original

    # Encode each specified column
    for col in columns:
        if col in df_encoded.columns:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

    return df_encoded


def handle_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.

    Args:
        df: Input DataFrame.
        strategy: Strategy to use ('mean', 'median', 'drop', 'zero').

    Returns:
        DataFrame with missing values handled.
    """
    df_clean = df.copy()  # Don't modify original

    # Apply strategy based on input
    if strategy == "mean":
        df_clean = df_clean.fillna(df_clean.mean())
    elif strategy == "median":
        df_clean = df_clean.fillna(df_clean.median())
    elif strategy == "drop":
        df_clean = df_clean.dropna()
    elif strategy == "zero":
        df_clean = df_clean.fillna(0)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return df_clean

