"""
Used in: All algorithm notebooks for validation and testing
Purpose:
    Provide validation utilities including statistical tests,
    assumption checking, and model diagnostics.
"""

import numpy as np  # NumPy for numerical operations
from scipy import stats  # Statistical tests
from typing import Dict, Any, Tuple  # Type hints
from sklearn.metrics import accuracy_score, mean_squared_error  # Basic metrics


def validate_model_output(y_pred: np.ndarray, y_true: np.ndarray, 
                         task_type: str = 'classification') -> Dict[str, Any]:
    """
    Validate model predictions against ground truth.

    Args:
        y_pred: Predicted values.
        y_true: True values.
        task_type: 'classification' or 'regression'.

    Returns:
        Dictionary with validation results.
    """
    # Check shapes match
    if y_pred.shape != y_true.shape:
        return {
            "valid": False,
            "error": f"Shape mismatch: y_pred {y_pred.shape} vs y_true {y_true.shape}"
        }
    
    # Check for NaN or Inf values
    if np.any(np.isnan(y_pred)) or np.any(np.isinf(y_pred)):
        return {
            "valid": False,
            "error": "Predictions contain NaN or Inf values"
        }
    
    # Task-specific validation
    if task_type == 'classification':
        # Check predictions are valid class labels
        unique_pred = np.unique(y_pred)
        unique_true = np.unique(y_true)
        
        # Check all predictions are in valid class range
        if not np.all(np.isin(unique_pred, unique_true)):
            return {
                "valid": False,
                "error": f"Invalid class labels in predictions: {unique_pred}"
            }
        
        accuracy = accuracy_score(y_true, y_pred)
        return {
            "valid": True,
            "accuracy": accuracy,
            "n_classes": len(unique_true)
        }
    
    elif task_type == 'regression':
        # Check predictions are reasonable (not all zeros, not constant)
        if np.all(y_pred == 0):
            return {
                "valid": False,
                "warning": "All predictions are zero"
            }
        
        if np.std(y_pred) == 0:
            return {
                "valid": False,
                "warning": "All predictions are constant"
            }
        
        mse = mean_squared_error(y_true, y_pred)
        return {
            "valid": True,
            "mse": mse,
            "rmse": np.sqrt(mse)
        }
    
    else:
        return {
            "valid": False,
            "error": f"Unknown task type: {task_type}"
        }


def test_statistical_assumptions(data: np.ndarray, test_type: str = 'normality') -> Dict[str, Any]:
    """
    Perform statistical tests on data to check assumptions.

    Args:
        data: Data array to test.
        test_type: Type of test ('normality', 'homoscedasticity').

    Returns:
        Dictionary with test results.
    """
    if test_type == 'normality':
        # Shapiro-Wilk test (good for small to medium samples)
        shapiro_stat, shapiro_p = stats.shapiro(data)
        
        # D'Agostino's test (better for larger samples)
        dagostino_stat, dagostino_p = stats.normaltest(data)
        
        return {
            "test_type": "normality",
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
    
    elif test_type == 'homoscedasticity':
        # Levene's test for equal variances (requires multiple groups)
        # For single array, we can't test homoscedasticity directly
        return {
            "test_type": "homoscedasticity",
            "error": "Requires multiple groups for homoscedasticity test"
        }
    
    else:
        return {
            "error": f"Unknown test type: {test_type}"
        }


def compare_models(metrics_dict: Dict[str, Dict[str, float]], 
                  metric_name: str = 'accuracy') -> Dict[str, Any]:
    """
    Compare multiple models based on a metric.

    Args:
        metrics_dict: Dictionary mapping model names to their metrics.
        metric_name: Name of metric to compare.

    Returns:
        Dictionary with comparison results including best model.
    """
    model_scores = {}
    for model_name, metrics in metrics_dict.items():
        if metric_name in metrics:
            model_scores[model_name] = metrics[metric_name]
    
    if not model_scores:
        return {
            "error": f"Metric '{metric_name}' not found in any model"
        }
    
    # Find best model
    if 'loss' in metric_name.lower() or 'error' in metric_name.lower() or 'mse' in metric_name.lower():
        # Lower is better
        best_model = min(model_scores, key=model_scores.get)
        best_score = model_scores[best_model]
    else:
        # Higher is better (accuracy, F1, etc.)
        best_model = max(model_scores, key=model_scores.get)
        best_score = model_scores[best_model]
    
    return {
        "model_scores": model_scores,
        "best_model": best_model,
        "best_score": best_score,
        "metric": metric_name
    }


def check_cross_validation_stability(cv_scores: np.ndarray, 
                                    threshold: float = 0.1) -> Dict[str, Any]:
    """
    Check if cross-validation scores are stable (low variance).

    Args:
        cv_scores: Array of cross-validation scores.
        threshold: Coefficient of variation threshold for stability.

    Returns:
        Dictionary with stability analysis.
    """
    mean_score = np.mean(cv_scores)
    std_score = np.std(cv_scores)
    cv_coefficient = std_score / (abs(mean_score) + 1e-10)  # Coefficient of variation
    
    is_stable = cv_coefficient < threshold
    
    return {
        "mean_score": mean_score,
        "std_score": std_score,
        "cv_coefficient": cv_coefficient,
        "is_stable": is_stable,
        "threshold": threshold
    }


def validate_hyperparameters(param_dict: Dict[str, Any], 
                             valid_ranges: Dict[str, Tuple[float, float]]) -> Dict[str, Any]:
    """
    Validate hyperparameters are within acceptable ranges.

    Args:
        param_dict: Dictionary of hyperparameters to validate.
        valid_ranges: Dictionary mapping parameter names to (min, max) tuples.

    Returns:
        Dictionary with validation results.
    """
    validation_results = {}
    all_valid = True
    
    for param_name, param_value in param_dict.items():
        if param_name in valid_ranges:
            min_val, max_val = valid_ranges[param_name]
            
            if isinstance(param_value, (int, float)):
                is_valid = min_val <= param_value <= max_val
                validation_results[param_name] = {
                    "value": param_value,
                    "valid": is_valid,
                    "range": (min_val, max_val)
                }
                if not is_valid:
                    all_valid = False
            else:
                validation_results[param_name] = {
                    "value": param_value,
                    "valid": False,
                    "error": "Parameter must be numeric"
                }
                all_valid = False
    
    return {
        "all_valid": all_valid,
        "results": validation_results
    }

