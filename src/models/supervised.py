"""
Used in: 04_Machine_Learning_Algorithms, 05_Supervised_Learning, 06_Classifier_Algorithms
Purpose:
    Provide wrapper functions and utilities for supervised learning models.
    Includes regression and classification helpers.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from sklearn.model_selection import train_test_split, cross_val_score  # Scikit-learn model selection
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix  # Evaluation metrics
from typing import Tuple, Any, Union  # Type hints
import numpy as np  # NumPy for numerical operations


def split_data(X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray], test_size: float = 0.2, random_state: int = 42) -> Tuple:
    """
    Split data into training and testing sets.

    Args:
        X: Feature matrix (DataFrame or array).
        y: Target vector (Series or array).
        test_size: Proportion of data to use for testing (0.0 to 1.0).
        random_state: Random seed for reproducibility.

    Returns:
        Tuple of (X_train, X_test, y_train, y_test).
    """
    # Use scikit-learn's train_test_split for consistent splitting
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

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

