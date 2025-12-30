"""
Used in: 13_Supervised_Linear_Regression.ipynb and other regression notebooks
Purpose:
    Provide regression-specific utilities including residual analysis,
    goodness-of-fit metrics, and assumption checking.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error  # Regression metrics
from scipy import stats  # Statistical tests
from typing import Tuple, Dict, Any  # Type hints
import matplotlib.pyplot as plt  # For plotting residuals


def calculate_residuals(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """
    Calculate residuals (errors) between true and predicted values.

    Args:
        y_true: True target values.
        y_pred: Predicted target values.

    Returns:
        Array of residuals (y_true - y_pred).
    """
    # Residuals are the difference between actual and predicted values
    residuals = y_true - y_pred
    return residuals


def plot_residuals(y_true: np.ndarray, y_pred: np.ndarray, title: str = "Residual Plot") -> None:
    """
    Plot residuals against predicted values to check for patterns.

    Args:
        y_true: True target values.
        y_pred: Predicted target values.
        title: Plot title.
    """
    residuals = calculate_residuals(y_true, y_pred)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Residuals vs Predicted
    axes[0].scatter(y_pred, residuals, alpha=0.6)
    axes[0].axhline(y=0, color='r', linestyle='--')
    axes[0].set_xlabel('Predicted Values')
    axes[0].set_ylabel('Residuals')
    axes[0].set_title('Residuals vs Predicted')
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Q-Q plot for normality check
    stats.probplot(residuals, dist="norm", plot=axes[1])
    axes[1].set_title('Q-Q Plot (Normality Check)')
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


def check_residual_normality(residuals: np.ndarray) -> Dict[str, Any]:
    """
    Test if residuals are normally distributed using statistical tests.

    Args:
        residuals: Array of residuals.

    Returns:
        Dictionary with test statistics and p-values.
    """
    # Shapiro-Wilk test for normality (works well for small to medium samples)
    shapiro_stat, shapiro_p = stats.shapiro(residuals)
    
    # D'Agostino's normality test (more robust for larger samples)
    dagostino_stat, dagostino_p = stats.normaltest(residuals)
    
    return {
        "shapiro_wilk": {
            "statistic": shapiro_stat,
            "p_value": shapiro_p,
            "is_normal": shapiro_p > 0.05
        },
        "dagostino": {
            "statistic": dagostino_stat,
            "p_value": dagostino_p,
            "is_normal": dagostino_p > 0.05
        }
    }


def calculate_goodness_of_fit(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """
    Calculate multiple goodness-of-fit metrics for regression models.

    Args:
        y_true: True target values.
        y_pred: Predicted target values.

    Returns:
        Dictionary with R², RMSE, MAE, and other metrics.
    """
    # R-squared (coefficient of determination)
    r2 = r2_score(y_true, y_pred)
    
    # Mean Squared Error
    mse = mean_squared_error(y_true, y_pred)
    
    # Root Mean Squared Error
    rmse = np.sqrt(mse)
    
    # Mean Absolute Error
    mae = mean_absolute_error(y_true, y_pred)
    
    # Mean Absolute Percentage Error (MAPE)
    # Avoid division by zero
    mape = np.mean(np.abs((y_true - y_pred) / np.where(y_true != 0, y_true, 1))) * 100
    
    return {
        "r2_score": r2,
        "mse": mse,
        "rmse": rmse,
        "mae": mae,
        "mape": mape
    }


def check_linearity_assumptions(X: np.ndarray, y: np.ndarray, y_pred: np.ndarray) -> Dict[str, Any]:
    """
    Check linear regression assumptions (linearity, homoscedasticity, independence).

    Args:
        X: Feature matrix.
        y: True target values.
        y_pred: Predicted target values.

    Returns:
        Dictionary with assumption check results.
    """
    residuals = calculate_residuals(y, y_pred)
    
    # Check homoscedasticity using Breusch-Pagan test (if we have statsmodels)
    # For now, use correlation between residuals and predictions
    correlation = np.corrcoef(y_pred, residuals)[0, 1]
    
    # Check for patterns in residuals (should be random)
    # Calculate Durbin-Watson statistic for independence
    dw_numerator = np.sum(np.diff(residuals)**2)
    dw_denominator = np.sum(residuals**2)
    durbin_watson = dw_numerator / dw_denominator if dw_denominator > 0 else 0
    
    # Normality check
    normality = check_residual_normality(residuals)
    
    return {
        "residual_prediction_correlation": correlation,
        "durbin_watson": durbin_watson,
        "normality": normality,
        "homoscedasticity_ok": abs(correlation) < 0.3,  # Low correlation suggests homoscedasticity
        "independence_ok": 1.5 < durbin_watson < 2.5  # DW statistic should be around 2
    }

