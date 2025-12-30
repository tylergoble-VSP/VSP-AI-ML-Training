"""
Used in: 20_Ensemble_Random_Forest.ipynb, 21_Ensemble_AdaBoost.ipynb, 
         22_Ensemble_Gradient_Boosting.ipynb, 23_Ensemble_XGBoost.ipynb
Purpose:
    Provide ensemble-specific utilities including feature importance extraction,
    out-of-bag error calculation, and ensemble prediction aggregation.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from typing import Dict, List, Any, Optional  # Type hints
import matplotlib.pyplot as plt  # For plotting


def extract_feature_importance(model: Any, feature_names: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Extract feature importance from an ensemble model.

    Args:
        model: Trained ensemble model (Random Forest, Gradient Boosting, etc.).
        feature_names: Optional list of feature names. If None, uses indices.

    Returns:
        DataFrame with features and their importance scores, sorted by importance.
    """
    # Check if model has feature_importances_ attribute
    if not hasattr(model, 'feature_importances_'):
        raise ValueError("Model does not have feature_importances_ attribute")
    
    importances = model.feature_importances_
    
    # Create feature names if not provided
    if feature_names is None:
        feature_names = [f"Feature_{i}" for i in range(len(importances))]
    
    # Create DataFrame
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    })
    
    # Sort by importance (descending)
    importance_df = importance_df.sort_values('importance', ascending=False)
    
    return importance_df


def plot_feature_importance(importance_df: pd.DataFrame, top_n: Optional[int] = None,
                           title: str = "Feature Importance") -> None:
    """
    Plot feature importance as a horizontal bar chart.

    Args:
        importance_df: DataFrame with 'feature' and 'importance' columns.
        top_n: Number of top features to display. If None, shows all.
        title: Plot title.
    """
    # Select top N features if specified
    if top_n is not None:
        plot_df = importance_df.head(top_n)
    else:
        plot_df = importance_df
    
    # Create plot
    plt.figure(figsize=(10, max(6, len(plot_df) * 0.3)))
    plt.barh(range(len(plot_df)), plot_df['importance'], align='center')
    plt.yticks(range(len(plot_df)), plot_df['feature'])
    plt.xlabel('Importance')
    plt.title(title)
    plt.gca().invert_yaxis()  # Show highest importance at top
    plt.tight_layout()
    plt.show()


def aggregate_predictions(predictions: List[np.ndarray], method: str = 'mean') -> np.ndarray:
    """
    Aggregate predictions from multiple models in an ensemble.

    Args:
        predictions: List of prediction arrays from different models.
        method: Aggregation method ('mean', 'median', 'vote' for classification).

    Returns:
        Aggregated predictions.
    """
    if not predictions:
        raise ValueError("Predictions list is empty")
    
    predictions_array = np.array(predictions)
    
    if method == 'mean':
        # Average predictions (for regression or probability averaging)
        aggregated = np.mean(predictions_array, axis=0)
    elif method == 'median':
        # Median predictions (more robust to outliers)
        aggregated = np.median(predictions_array, axis=0)
    elif method == 'vote':
        # Majority voting (for classification)
        # Assumes predictions are class labels (integers)
        aggregated = np.apply_along_axis(
            lambda x: np.bincount(x).argmax(), axis=0, arr=predictions_array
        )
    else:
        raise ValueError(f"Unknown aggregation method: {method}")
    
    return aggregated


def calculate_oob_error(model: Any) -> Optional[float]:
    """
    Calculate out-of-bag (OOB) error for Random Forest models.

    Args:
        model: Trained Random Forest model with oob_score enabled.

    Returns:
        OOB error (1 - oob_score) if available, None otherwise.
    """
    # Check if model has oob_score_ attribute
    if hasattr(model, 'oob_score_'):
        oob_error = 1 - model.oob_score_
        return oob_error
    else:
        return None


def analyze_ensemble_stability(models: List[Any], X: np.ndarray, 
                              y: np.ndarray) -> Dict[str, Any]:
    """
    Analyze stability of an ensemble by comparing predictions across models.

    Args:
        models: List of trained ensemble models.
        X: Feature matrix.
        y: True target values.

    Returns:
        Dictionary with stability metrics including prediction variance.
    """
    # Get predictions from all models
    all_predictions = [model.predict(X) for model in models]
    
    # Calculate mean prediction
    mean_prediction = np.mean(all_predictions, axis=0)
    
    # Calculate variance of predictions (higher variance = less stable)
    prediction_variance = np.var(all_predictions, axis=0)
    mean_variance = np.mean(prediction_variance)
    
    # Calculate agreement (for classification, how often models agree)
    if all_predictions[0].dtype in [np.int32, np.int64]:
        # Classification case
        predictions_array = np.array(all_predictions)
        # Count how many models agree with the majority vote
        majority_vote = np.apply_along_axis(
            lambda x: np.bincount(x).argmax(), axis=0, arr=predictions_array
        )
        agreement = np.mean([
            np.mean(pred == majority_vote) for pred in all_predictions
        ])
    else:
        # Regression case - use coefficient of variation
        std_pred = np.std(all_predictions, axis=0)
        cv = std_pred / (np.abs(mean_prediction) + 1e-10)  # Avoid division by zero
        agreement = 1 - np.mean(cv)  # Lower CV = higher agreement
    
    return {
        "mean_prediction": mean_prediction,
        "prediction_variance": prediction_variance,
        "mean_variance": mean_variance,
        "agreement": agreement,
        "n_models": len(models)
    }

