"""
Used in: All algorithm notebooks for validation and testing
Purpose:
    Provide validation utilities including statistical tests,
    assumption checking, and model diagnostics.
    
Educational Context:
    This module demonstrates:
    1. Model validation concepts (checking if predictions make sense)
    2. Statistical hypothesis testing
    3. Assumption checking for ML models
    4. Error handling and defensive programming
    
    Why validate model outputs?
    - Catch bugs early (wrong shapes, NaN values, etc.)
    - Ensure predictions are reasonable
    - Verify model assumptions are met
    - Compare models fairly
"""

# Import NumPy: The fundamental library for numerical computing in Python
# Provides arrays, mathematical functions, and efficient operations on large datasets
import numpy as np

# Import scipy.stats: Provides statistical tests and probability distributions
# We use this for normality tests, hypothesis testing, etc.
from scipy import stats

# Import type hints: These help document what types of data functions expect/return
# Dict = dictionary, Any = any type, Tuple = tuple
# Type hints don't change how code runs, but help IDEs and other developers
from typing import Dict, Any, Tuple

# Import sklearn metrics: Standard functions for evaluating ML model performance
# accuracy_score: For classification (percentage of correct predictions)
# mean_squared_error: For regression (average squared difference between predictions and truth)
from sklearn.metrics import accuracy_score, mean_squared_error


def validate_model_output(y_pred: np.ndarray, y_true: np.ndarray, 
                         task_type: str = 'classification') -> Dict[str, Any]:
    """
    Validate model predictions against ground truth.
    
    Educational Explanation:
        This function demonstrates defensive programming - checking inputs before using them.
        It catches common errors that could lead to incorrect results:
        1. Shape mismatches (predictions and truth must have same length)
        2. Invalid values (NaN, Inf) that break calculations
        3. Invalid class labels (predictions must be valid classes)
        4. Degenerate predictions (all zeros, all same value)
        
        Why validate?
        - Prevents silent failures (wrong results without error)
        - Makes debugging easier (clear error messages)
        - Catches bugs early in the pipeline
    
    Args:
        y_pred: Predicted values (numpy array)
        y_true: True/actual values (numpy array, same length as y_pred)
        task_type: 'classification' (discrete classes) or 'regression' (continuous values)
                  Default is 'classification'
    
    Returns:
        Dictionary with validation results:
        - "valid": True if predictions are valid, False otherwise
        - "error" or "warning": Description of any problems found
        - Task-specific metrics (accuracy for classification, MSE/RMSE for regression)
    """
    # First check: Do predictions and truth have the same shape?
    # .shape returns a tuple like (100,) for 1D array with 100 elements
    # or (100, 3) for 2D array with 100 rows and 3 columns
    # If shapes don't match, we can't compare them meaningfully
    if y_pred.shape != y_true.shape:
        # Return early with an error message
        # f-strings allow us to embed variables in strings
        # This gives a clear error message showing exactly what went wrong
        return {
            "valid": False,
            "error": f"Shape mismatch: y_pred {y_pred.shape} vs y_true {y_true.shape}"
        }
    
    # Second check: Are there any invalid numerical values?
    # np.isnan() checks for NaN (Not a Number) - can occur from division by zero, etc.
    # np.isinf() checks for Inf (Infinity) - can occur from overflow, etc.
    # np.any() returns True if ANY element is True (short-circuits for efficiency)
    # These values break mathematical operations and indicate a problem
    if np.any(np.isnan(y_pred)) or np.any(np.isinf(y_pred)):
        return {
            "valid": False,
            "error": "Predictions contain NaN or Inf values"
        }
    
    # Task-specific validation: Different checks for classification vs regression
    if task_type == 'classification':
        # Classification: Predictions should be discrete class labels
        
        # Get unique values in predictions and truth
        # np.unique() returns sorted array of unique values
        # Example: [0, 1, 1, 2, 0] -> [0, 1, 2]
        unique_pred = np.unique(y_pred)
        unique_true = np.unique(y_true)
        
        # Check that all predicted classes are valid (exist in true labels)
        # np.isin() checks if each element of unique_pred is in unique_true
        # np.all() returns True only if ALL elements are True
        # If a prediction is a class that doesn't exist in training, that's an error
        if not np.all(np.isin(unique_pred, unique_true)):
            return {
                "valid": False,
                "error": f"Invalid class labels in predictions: {unique_pred}"
            }
        
        # Calculate accuracy: percentage of correct predictions
        # accuracy_score compares y_true and y_pred element by element
        # Returns a float between 0.0 (all wrong) and 1.0 (all correct)
        accuracy = accuracy_score(y_true, y_pred)
        
        # Return success with metrics
        return {
            "valid": True,
            "accuracy": accuracy,  # Proportion of correct predictions
            "n_classes": len(unique_true)  # Number of distinct classes
        }
    
    elif task_type == 'regression':
        # Regression: Predictions should be continuous numerical values
        
        # Check 1: Are all predictions zero? (model might not be trained)
        # np.all() returns True if ALL elements are True
        # y_pred == 0 creates a boolean array (True where element equals 0)
        if np.all(y_pred == 0):
            return {
                "valid": False,
                "warning": "All predictions are zero"
            }
        
        # Check 2: Are all predictions the same? (model might be broken)
        # np.std() calculates standard deviation (measure of spread)
        # If std is 0, all values are identical (no variation)
        # This suggests the model isn't learning patterns, just predicting a constant
        if np.std(y_pred) == 0:
            return {
                "valid": False,
                "warning": "All predictions are constant"
            }
        
        # Calculate Mean Squared Error (MSE)
        # MSE = average of (prediction - truth)^2
        # Larger errors are penalized more (squared)
        # Lower is better (0 = perfect predictions)
        mse = mean_squared_error(y_true, y_pred)
        
        # Return success with metrics
        return {
            "valid": True,
            "mse": mse,  # Mean Squared Error
            "rmse": np.sqrt(mse)  # Root Mean Squared Error (in same units as target)
        }
    
    else:
        # Handle invalid task_type parameter
        # This is defensive programming - catch invalid inputs
        return {
            "valid": False,
            "error": f"Unknown task type: {task_type}"
        }


def test_statistical_assumptions(data: np.ndarray, test_type: str = 'normality') -> Dict[str, Any]:
    """
    Perform statistical tests on data to check assumptions.
    
    Educational Explanation:
        Many machine learning algorithms make assumptions about data:
        1. Normality: Data follows a normal (bell curve) distribution
        2. Homoscedasticity: Variance is constant across groups
        
        Why test assumptions?
        - Linear regression assumes residuals are normally distributed
        - Some tests assume equal variances between groups
        - Violating assumptions can lead to incorrect conclusions
        
        Statistical Hypothesis Testing:
        - Null hypothesis (H0): Data is normal (or has equal variance)
        - p-value: Probability of seeing this data if H0 is true
        - If p < 0.05, we reject H0 (data is NOT normal)
        - If p >= 0.05, we don't reject H0 (data might be normal)
    
    Args:
        data: Data array to test (1D numpy array)
        test_type: Type of test to perform
                  - 'normality': Check if data follows normal distribution
                  - 'homoscedasticity': Check if variances are equal (needs multiple groups)
    
    Returns:
        Dictionary with test results including:
        - Test statistics (measure of deviation from assumption)
        - p-values (probability of seeing this data if assumption is true)
        - is_normal/is_valid (boolean indicating if assumption is met)
    """
    if test_type == 'normality':
        # Test if data follows a normal (Gaussian) distribution
        # Many statistical methods assume normality, so we check it
        
        # Shapiro-Wilk test: Good for small to medium samples (n < 5000)
        # Returns two values: test statistic and p-value
        # Test statistic: Measures deviation from normality (higher = less normal)
        # p-value: Probability of seeing this data if data IS normal
        shapiro_stat, shapiro_p = stats.shapiro(data)
        
        # D'Agostino's normality test: Better for larger samples
        # Combines skewness and kurtosis tests
        # Skewness: Measure of asymmetry (normal distribution is symmetric)
        # Kurtosis: Measure of tail heaviness (normal distribution has specific kurtosis)
        dagostino_stat, dagostino_p = stats.normaltest(data)
        
        # Return results for both tests
        # We run both because they have different strengths
        return {
            "test_type": "normality",
            "shapiro_wilk": {
                "statistic": shapiro_stat,  # Test statistic (higher = less normal)
                "p_value": shapiro_p,  # p-value (lower = less likely to be normal)
                # Convention: p > 0.05 means "don't reject normality"
                # This is a common threshold, but not a hard rule
                "is_normal": shapiro_p > 0.05
            },
            "dagostino": {
                "statistic": dagostino_stat,  # Test statistic
                "p_value": dagostino_p,  # p-value
                "is_normal": dagostino_p > 0.05
            }
        }
    
    elif test_type == 'homoscedasticity':
        # Test if variances are equal across groups (homoscedasticity)
        # This requires multiple groups to compare
        # For a single array, we can't test this directly
        
        # Levene's test would be used here, but it needs multiple groups
        # Example: Compare variance of residuals across different ranges of predictions
        return {
            "test_type": "homoscedasticity",
            "error": "Requires multiple groups for homoscedasticity test"
        }
    
    else:
        # Handle invalid test_type
        return {
            "error": f"Unknown test type: {test_type}"
        }


def compare_models(metrics_dict: Dict[str, Dict[str, float]], 
                  metric_name: str = 'accuracy') -> Dict[str, Any]:
    """
    Compare multiple models based on a metric.
    
    Educational Explanation:
        This function demonstrates:
        1. Dictionary iteration and nested data structures
        2. Finding min/max with custom key functions
        3. Handling different metric types (higher vs lower is better)
        
        Why compare models?
        - Choose the best model for deployment
        - Understand trade-offs between different algorithms
        - Track improvements over iterations
    
    Args:
        metrics_dict: Dictionary where:
                     - Keys are model names (e.g., "RandomForest", "SVM")
                     - Values are dictionaries of metrics (e.g., {"accuracy": 0.95, "f1": 0.92})
        metric_name: Name of metric to compare (e.g., "accuracy", "mse", "f1_score")
    
    Returns:
        Dictionary with:
        - model_scores: All model scores for the metric
        - best_model: Name of the best performing model
        - best_score: Score of the best model
        - metric: The metric that was compared
    """
    # Extract scores for the specified metric from each model
    # Start with empty dictionary to collect scores
    model_scores = {}
    
    # Iterate through each model and its metrics
    # .items() returns (key, value) pairs from the dictionary
    # Example: {"model1": {"accuracy": 0.9}, "model2": {"accuracy": 0.95}}
    for model_name, metrics in metrics_dict.items():
        # Check if this model has the metric we're looking for
        # 'in' operator checks if key exists in dictionary
        if metric_name in metrics:
            # Store the score for this model
            # Example: model_scores["model1"] = 0.9
            model_scores[model_name] = metrics[metric_name]
    
    # Check if we found any scores
    # Empty dictionary is "falsy" in Python (evaluates to False in boolean context)
    if not model_scores:
        return {
            "error": f"Metric '{metric_name}' not found in any model"
        }
    
    # Determine if higher or lower is better for this metric
    # Some metrics: accuracy, F1, R² (higher is better)
    # Other metrics: loss, error, MSE, RMSE (lower is better)
    # We check the metric name to determine which direction is better
    
    # Check if metric name contains words that indicate "lower is better"
    # .lower() converts to lowercase for case-insensitive comparison
    # 'in' checks if substring exists in string
    if 'loss' in metric_name.lower() or 'error' in metric_name.lower() or 'mse' in metric_name.lower():
        # Lower is better (loss, error, MSE, RMSE, MAE)
        # min() finds the minimum value
        # key=model_scores.get means "use the value from model_scores as the comparison key"
        # This finds the model with the minimum score
        best_model = min(model_scores, key=model_scores.get)
        best_score = model_scores[best_model]
    else:
        # Higher is better (accuracy, precision, recall, F1, R²)
        # max() finds the maximum value
        # Same key function pattern as min()
        best_model = max(model_scores, key=model_scores.get)
        best_score = model_scores[best_model]
    
    # Return comprehensive comparison results
    return {
        "model_scores": model_scores,  # All scores for reference
        "best_model": best_model,  # Winner
        "best_score": best_score,  # Winning score
        "metric": metric_name  # Which metric was compared
    }


def check_cross_validation_stability(cv_scores: np.ndarray, 
                                    threshold: float = 0.1) -> Dict[str, Any]:
    """
    Check if cross-validation scores are stable (low variance).
    
    Educational Explanation:
        Cross-validation splits data into folds and trains on each fold.
        If scores vary wildly across folds, the model is unstable.
        
        Coefficient of Variation (CV):
        - CV = standard_deviation / mean
        - Measures relative variability (normalized by mean)
        - Lower CV = more stable (less variation relative to mean)
        - Example: CV of 0.1 means std is 10% of the mean
        
        Why check stability?
        - Unstable models may not generalize well
        - High variance suggests overfitting or insufficient data
        - Stable models are more reliable for deployment
    
    Args:
        cv_scores: Array of scores from cross-validation folds
                  Example: [0.92, 0.94, 0.91, 0.93, 0.92] for 5-fold CV
        threshold: Maximum acceptable CV coefficient (default 0.1 = 10% variation)
    
    Returns:
        Dictionary with stability analysis including mean, std, CV, and stability flag
    """
    # Calculate mean (average) score across all folds
    # This is the overall performance estimate
    mean_score = np.mean(cv_scores)
    
    # Calculate standard deviation (spread) of scores
    # Higher std = more variation between folds
    std_score = np.std(cv_scores)
    
    # Calculate coefficient of variation
    # CV = std / mean (relative measure of variability)
    # abs(mean_score) ensures we handle negative scores correctly
    # + 1e-10 prevents division by zero (tiny number added to denominator)
    # 1e-10 = 0.0000000001 (scientific notation)
    cv_coefficient = std_score / (abs(mean_score) + 1e-10)
    
    # Determine if scores are stable
    # Lower threshold = stricter requirement (less variation allowed)
    # Default 0.1 means "std should be less than 10% of mean"
    is_stable = cv_coefficient < threshold
    
    # Return comprehensive stability analysis
    return {
        "mean_score": mean_score,  # Average performance
        "std_score": std_score,  # Variation in performance
        "cv_coefficient": cv_coefficient,  # Relative variation (std/mean)
        "is_stable": is_stable,  # Boolean: is it stable?
        "threshold": threshold  # Threshold used for comparison
    }


def validate_hyperparameters(param_dict: Dict[str, Any], 
                             valid_ranges: Dict[str, Tuple[float, float]]) -> Dict[str, Any]:
    """
    Validate hyperparameters are within acceptable ranges.
    
    Educational Explanation:
        Hyperparameters are settings that control how models learn.
        Examples: learning_rate, max_depth, regularization strength
        
        Why validate ranges?
        - Some values cause errors (negative learning rate, etc.)
        - Some values are meaningless (max_depth = 0)
        - Prevents wasting time training with bad settings
        - Catches typos and configuration errors early
    
    Args:
        param_dict: Dictionary of hyperparameters to validate
                   Example: {"learning_rate": 0.01, "max_depth": 5}
        valid_ranges: Dictionary mapping parameter names to (min, max) tuples
                     Example: {"learning_rate": (0.0, 1.0), "max_depth": (1, 100)}
    
    Returns:
        Dictionary with validation results for each parameter
    """
    # Dictionary to store validation results for each parameter
    validation_results = {}
    
    # Flag to track if ALL parameters are valid
    # Start with True, set to False if any parameter fails
    all_valid = True
    
    # Iterate through each hyperparameter
    # .items() returns (key, value) pairs
    for param_name, param_value in param_dict.items():
        # Check if this parameter has a defined valid range
        if param_name in valid_ranges:
            # Unpack the tuple: (min_value, max_value)
            # Tuple unpacking: a, b = (1, 2) assigns a=1, b=2
            min_val, max_val = valid_ranges[param_name]
            
            # Check if parameter value is numeric (int or float)
            # isinstance() checks if object is instance of a class
            # (int, float) is a tuple of types to check against
            if isinstance(param_value, (int, float)):
                # Check if value is within valid range
                # <= allows values at boundaries (inclusive range)
                is_valid = min_val <= param_value <= max_val
                
                # Store validation result for this parameter
                validation_results[param_name] = {
                    "value": param_value,  # The actual value provided
                    "valid": is_valid,  # Whether it's in valid range
                    "range": (min_val, max_val)  # The valid range
                }
                
                # If this parameter is invalid, mark overall as invalid
                if not is_valid:
                    all_valid = False
            else:
                # Parameter is not numeric (wrong type)
                # Example: learning_rate = "0.01" (string instead of float)
                validation_results[param_name] = {
                    "value": param_value,
                    "valid": False,
                    "error": "Parameter must be numeric"
                }
                all_valid = False
    
    # Return comprehensive validation results
    return {
        "all_valid": all_valid,  # True if ALL parameters are valid
        "results": validation_results  # Detailed results for each parameter
    }

