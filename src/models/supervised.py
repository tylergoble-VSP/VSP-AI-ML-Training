"""
Used in: 04_Machine_Learning_Algorithms, 05_Supervised_Learning, 06_Classifier_Algorithms
Purpose:
    Provide wrapper functions and utilities for supervised learning models.
    Includes regression and classification helpers.
    
Educational Context:
    Supervised learning uses labeled data (input-output pairs) to learn patterns.
    
    Key Concepts:
    1. Train/Test Split: Separate data for training (learning) and testing (evaluation)
    2. Cross-Validation: More robust evaluation using multiple train/test splits
    3. Classification: Predicting categories (discrete labels)
    4. Regression: Predicting continuous values (numbers)
    
    Why split data?
    - Test on unseen data (simulates real-world performance)
    - Prevents overfitting (model memorizing training data)
    - Gives honest performance estimate
    
    Why cross-validation?
    - Single split can be unlucky (bad random split)
    - Multiple splits give more reliable estimate
    - Better use of limited data
"""

# Import NumPy: For numerical operations on arrays
import numpy as np

# Import Pandas: For DataFrame operations
import pandas as pd

# Import scikit-learn model selection utilities
# train_test_split: Split data into training and testing sets
# cross_val_score: Perform k-fold cross-validation
from sklearn.model_selection import train_test_split, cross_val_score

# Import evaluation metrics
# accuracy_score: For classification (proportion correct)
# mean_squared_error: For regression (average squared error)
# classification_report: Comprehensive classification metrics
# confusion_matrix: Shows prediction vs actual class counts
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix

# Import type hints for better code documentation
from typing import Tuple, Any, Union


def split_data(X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray], test_size: float = 0.2, random_state: int = 42) -> Tuple:
    """
    Split data into training and testing sets.
    
    Educational Explanation:
        This function separates data into two sets:
        1. Training set: Used to teach the model (usually 80%)
        2. Test set: Used to evaluate the model (usually 20%)
        
        Why split data?
        - Test on unseen data (simulates real-world performance)
        - Prevents data leakage (test data influencing training)
        - Detects overfitting (model memorizing vs learning)
        
        Why random_state?
        - Makes split reproducible (same random seed = same split)
        - Essential for debugging and sharing results
        - Allows comparing models on identical splits
    
    Args:
        X: Feature matrix (inputs)
          - DataFrame: Tabular data with rows (samples) and columns (features)
          - Array: 2D array with shape (samples, features)
        y: Target vector (outputs to predict)
          - Series: Pandas Series (1D labeled array)
          - Array: 1D array with one label per sample
        test_size: Proportion of data for testing (default 0.2 = 20%)
                  - 0.2 means 20% test, 80% train
                  - Common values: 0.2, 0.25, 0.3
        random_state: Random seed for reproducibility (default 42)
                     - Same seed = same split every time
                     - Different seed = different split
    
    Returns:
        Tuple containing four arrays/DataFrames:
        - X_train: Training features (80% of data)
        - X_test: Test features (20% of data)
        - y_train: Training targets (corresponding labels)
        - y_test: Test targets (corresponding labels)
    """
    # Use scikit-learn's train_test_split for consistent splitting
    # This function:
    # 1. Randomly shuffles data (if random_state provided)
    # 2. Splits into train/test sets
    # 3. Maintains correspondence between X and y (same samples together)
    # 4. Handles both arrays and DataFrames automatically
    
    # Unpack the tuple returned by train_test_split
    # The function returns (X_train, X_test, y_train, y_test)
    X_train, X_test, y_train, y_test = train_test_split(
        X,  # Features to split
        y,  # Targets to split
        test_size=test_size,  # Proportion for test set (0.2 = 20%)
        random_state=random_state  # Seed for reproducibility
    )
    
    # Return all four splits
    # Caller can use these for training and evaluation
    return X_train, X_test, y_train, y_test


def evaluate_classifier(model: Any, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """
    Evaluate a classification model and return metrics.

    Args:
        model: Trained classifier (must have .predict method).
        X_test: Test feature matrix.
        y_test: True test labels.

    Returns:
        Dictionary containing accuracy, classification report, and confusion matrix.
    """
    # Make predictions on test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Generate classification report (precision, recall, F1)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    return {
        "accuracy": accuracy,
        "classification_report": report,
        "confusion_matrix": cm,
        "predictions": y_pred
    }


def evaluate_regressor(model: Any, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """
    Evaluate a regression model and return metrics.

    Args:
        model: Trained regressor (must have .predict method).
        X_test: Test feature matrix.
        y_test: True test values.

    Returns:
        Dictionary containing MSE, RMSE, and predictions.
    """
    # Make predictions on test set
    y_pred = model.predict(X_test)

    # Calculate mean squared error
    mse = mean_squared_error(y_test, y_pred)

    # Calculate root mean squared error
    rmse = np.sqrt(mse)

    return {
        "mse": mse,
        "rmse": rmse,
        "predictions": y_pred
    }


def cross_validate_model(model: Any, X: np.ndarray, y: np.ndarray, cv: int = 5, scoring: str = "accuracy") -> dict:
    """
    Perform k-fold cross-validation on a model.

    Args:
        model: Model to cross-validate.
        X: Feature matrix.
        y: Target vector.
        cv: Number of folds.
        scoring: Scoring metric (e.g., 'accuracy', 'neg_mean_squared_error').

    Returns:
        Dictionary with mean score and standard deviation.
    """
    # Perform cross-validation
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)

    return {
        "mean_score": scores.mean(),
        "std_score": scores.std(),
        "scores": scores
    }

