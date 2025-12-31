"""
Used in: 03_Advanced_Python, 05_Supervised_Learning, 06_Classifier_Algorithms
Purpose:
    Provide data preprocessing utilities for NumPy arrays and Pandas DataFrames.
    Includes scaling, encoding, and basic transformations.
    
Educational Context:
    Data preprocessing is a crucial step in machine learning:
    1. Normalization/Scaling: Make features comparable (age vs income)
    2. Encoding: Convert text categories to numbers (red=0, blue=1, green=2)
    3. Missing Values: Handle incomplete data (NaN, null values)
    
    Why preprocess?
    - Many algorithms assume features are on similar scales
    - Algorithms need numerical inputs (can't use text directly)
    - Missing values cause errors in most algorithms
    - Better preprocessing = better model performance
    
    Common preprocessing steps:
    - Standardization: (x - mean) / std (mean=0, std=1)
    - Normalization: Scale to [0, 1] range
    - Label encoding: Convert categories to integers
    - One-hot encoding: Convert categories to binary vectors
"""

# Import NumPy: For numerical operations on arrays
import numpy as np

# Import Pandas: For DataFrame operations (tabular data)
import pandas as pd

# Import scikit-learn preprocessing tools
# StandardScaler: Normalizes features (zero mean, unit variance)
# LabelEncoder: Converts text categories to integers (0, 1, 2, ...)
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Import type hints
# Union: Allows multiple types (e.g., Union[int, str] = int or str)
# Optional: Shorthand for Union[Type, None] (can be Type or None)
from typing import Union, Optional


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """
    Normalize a NumPy array to have zero mean and unit variance.
    
    Educational Explanation:
        Normalization (also called standardization or z-score normalization) transforms
        data so it has:
        - Mean = 0 (centered around zero)
        - Standard deviation = 1 (unit variance)
        
        Formula: normalized = (value - mean) / std
        
        Why normalize?
        - Makes features comparable (age in years vs income in dollars)
        - Many algorithms work better with normalized data
        - Prevents features with large values from dominating
        - Gradient descent converges faster
        
        Example:
        Original: [10, 20, 30, 40, 50]
        Mean: 30, Std: ~15.81
        Normalized: [-1.26, -0.63, 0, 0.63, 1.26]
    
    Args:
        arr: Input NumPy array (1D or multi-dimensional)
            Example: np.array([1, 2, 3, 4, 5])
    
    Returns:
        Normalized array with same shape as input
        Mean ≈ 0, Standard deviation = 1
    """
    # Compute mean (average) of the array
    # np.mean() calculates the arithmetic mean
    # For array [1, 2, 3, 4, 5], mean = 3.0
    mean = np.mean(arr)
    
    # Compute standard deviation (measure of spread)
    # np.std() calculates standard deviation
    # Standard deviation measures how spread out values are
    # For array [1, 2, 3, 4, 5], std ≈ 1.41
    std = np.std(arr)
    
    # Handle edge case: constant array (all values the same)
    # If std == 0, all values are identical (no variation)
    # Division by zero would cause an error
    # In this case, we just center the data (subtract mean)
    # Result: all values become 0 (since they're all the same)
    if std == 0:
        # Return centered array (mean subtracted, but no division)
        # This prevents division by zero error
        return arr - mean
    
    # Normalize using z-score formula: (value - mean) / std
    # Step 1: (arr - mean) centers the data (subtracts mean from each value)
    #         This makes the mean = 0
    # Step 2: / std scales the data (divides by standard deviation)
    #         This makes the standard deviation = 1
    # Result: normalized array with mean=0 and std=1
    normalized = (arr - mean) / std
    
    # Return the normalized array
    return normalized


def scale_features(X: Union[pd.DataFrame, np.ndarray], fit: bool = True, scaler: Optional[StandardScaler] = None) -> tuple[np.ndarray, StandardScaler]:
    """
    Scale features using StandardScaler (zero mean, unit variance).
    
    Educational Explanation:
        This function uses scikit-learn's StandardScaler for normalization.
        StandardScaler is preferred over manual normalization because:
        1. It remembers the mean/std from training data
        2. Can apply same scaling to test data (critical!)
        3. Handles edge cases automatically
        
        Important: fit on training, transform on test!
        - fit_transform(): Learn scaling from data AND apply it (training)
        - transform(): Apply learned scaling (test data)
        - Why? Test data shouldn't influence scaling parameters
        
        Example workflow:
        1. Train: X_train_scaled, scaler = scale_features(X_train, fit=True)
        2. Test: X_test_scaled, _ = scale_features(X_test, fit=False, scaler=scaler)
    
    Args:
        X: Input features (DataFrame or NumPy array)
          DataFrame: Tabular data with rows (samples) and columns (features)
          Array: 2D array with shape (samples, features)
        fit: Whether to fit a new scaler
            True: Learn scaling from this data (use for training)
            False: Use existing scaler (use for test data)
        scaler: Existing scaler to reuse (required if fit=False)
                This scaler was fitted on training data
    
    Returns:
        Tuple containing:
        - scaled_X: Scaled features (NumPy array, always)
        - scaler: The scaler object (save this for test data!)
    """
    # Determine if we need to create a new scaler
    # We create new scaler if:
    # 1. fit=True (explicitly requested)
    # 2. scaler is None (no existing scaler provided)
    if fit or scaler is None:
        # Create a new StandardScaler
        # StandardScaler will learn mean and std from the data
        scaler = StandardScaler()
        
        # fit_transform() does two things:
        # 1. fit(): Learn mean and std from X
        # 2. transform(): Apply scaling to X
        # This is the correct approach for training data
        scaled_X = scaler.fit_transform(X)
    else:
        # Use existing scaler (fitted on training data)
        # transform() applies the learned scaling without refitting
        # This is critical: test data uses training statistics
        # Prevents data leakage (test data influencing preprocessing)
        scaled_X = scaler.transform(X)
    
    # Return both the scaled data and the scaler
    # The scaler is important: save it to scale test data later
    return scaled_X, scaler


def encode_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Encode categorical columns using label encoding.
    
    Educational Explanation:
        Machine learning algorithms need numerical inputs.
        Categorical data (text like "red", "blue", "green") must be converted to numbers.
        
        Label Encoding:
        - Converts each unique category to an integer
        - "red" → 0, "blue" → 1, "green" → 2
        - Simple and preserves order (if categories have order)
        
        When to use:
        - Ordinal categories (small, medium, large have order)
        - Tree-based models (can handle integer encoding)
        
        When NOT to use:
        - Nominal categories without order (colors, cities)
        - Linear models (may interpret as having order)
        - Use one-hot encoding instead for nominal categories
    
    Args:
        df: Input DataFrame with categorical columns
        columns: List of column names to encode
                Example: ["color", "size", "category"]
    
    Returns:
        DataFrame with specified columns encoded as integers
        Original DataFrame is not modified (copy is returned)
    """
    # Create a copy of the DataFrame
    # .copy() creates a new DataFrame so we don't modify the original
    # This is important: original data should remain unchanged
    df_encoded = df.copy()
    
    # Encode each specified column
    # Loop through the list of column names to encode
    for col in columns:
        # Check if column exists in DataFrame
        # This prevents errors if user specifies a non-existent column
        if col in df_encoded.columns:
            # Create a LabelEncoder for this column
            # Each column gets its own encoder (different mappings)
            # Example: "color" column: red=0, blue=1, green=2
            #          "size" column: small=0, medium=1, large=2
            le = LabelEncoder()
            
            # Encode the column
            # .astype(str) converts all values to strings first
            # This handles mixed types (some numbers, some text)
            # fit_transform() learns the mapping and applies it
            # Returns array of integers (0, 1, 2, ...)
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    
    # Return the encoded DataFrame
    return df_encoded


def handle_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.
    
    Educational Explanation:
        Missing values (NaN, None, null) are common in real-world data.
        Most ML algorithms can't handle missing values, so we must fix them.
        
        Strategies:
        1. "mean": Replace with average (good for numerical data)
        2. "median": Replace with middle value (robust to outliers)
        3. "drop": Remove rows with missing values (loses data)
        4. "zero": Replace with 0 (simple, but may not be appropriate)
        
        Choosing a strategy:
        - Mean: When data is normally distributed
        - Median: When data has outliers
        - Drop: When missing values are rare (< 5% of data)
        - Zero: When 0 is a meaningful value
    
    Args:
        df: Input DataFrame that may contain missing values (NaN)
        strategy: How to handle missing values
                - "mean": Replace with column mean
                - "median": Replace with column median
                - "drop": Remove rows with any missing values
                - "zero": Replace with 0
    
    Returns:
        DataFrame with missing values handled
        Original DataFrame is not modified (copy is returned)
    """
    # Create a copy to avoid modifying the original DataFrame
    df_clean = df.copy()
    
    # Apply the chosen strategy
    # Different strategies are appropriate for different situations
    if strategy == "mean":
        # Replace missing values with the mean (average) of each column
        # .mean() calculates mean for each column (ignoring NaN)
        # .fillna() replaces NaN values with the provided value
        # This preserves the overall distribution
        df_clean = df_clean.fillna(df_clean.mean())
    
    elif strategy == "median":
        # Replace missing values with the median (middle value) of each column
        # Median is more robust to outliers than mean
        # If data has extreme values, median is often better
        df_clean = df_clean.fillna(df_clean.median())
    
    elif strategy == "drop":
        # Remove rows that contain any missing values
        # .dropna() removes rows with NaN in any column
        # Warning: This reduces dataset size (loses information)
        # Only use if missing values are rare
        df_clean = df_clean.dropna()
    
    elif strategy == "zero":
        # Replace missing values with 0
        # Simple approach, but 0 may not be meaningful for all features
        # Example: Age = 0 doesn't make sense, but count = 0 might
        df_clean = df_clean.fillna(0)
    
    else:
        # Invalid strategy provided
        # Raise an error with a helpful message
        raise ValueError(f"Unknown strategy: {strategy}")
    
    # Return the cleaned DataFrame
    return df_clean

