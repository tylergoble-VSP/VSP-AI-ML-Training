"""
Used in: All algorithm notebooks for traceability and interpretability
Purpose:
    Provide traceability utilities including feature importance tracking,
    decision path extraction, and model interpretation helpers.
    
Educational Context:
    This module demonstrates model interpretability - understanding WHY models make predictions.
    
    Key Concepts:
    1. Feature Importance: Which features matter most for predictions
    2. Decision Paths: How a model reached a specific prediction (for trees)
    3. Support Vectors: Key data points that define the model (for SVMs)
    4. Cluster Analysis: Understanding grouping patterns (for clustering)
    
    Why interpretability matters:
    - Trust: Users need to understand model decisions
    - Debugging: Find why model makes wrong predictions
    - Fairness: Detect bias in model decisions
    - Regulatory: Some industries require explainable AI
    - Improvement: Understand what model learns to improve it
"""

# Import NumPy: For numerical operations and array handling
import numpy as np

# Import Pandas: For DataFrame operations (tabular data)
import pandas as pd

# Import type hints: Document expected types
from typing import Dict, List, Any, Optional, Tuple

# Import our utility for timestamped file paths
from src.utils.paths import timestamped_path

# Import json: For saving complex data structures to files
# JSON (JavaScript Object Notation) is a text format for structured data
import json


def extract_feature_importance_trace(model: Any, feature_names: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Extract and trace feature importance from a model.
    
    Educational Explanation:
        Feature importance tells us which features (input variables) the model
        relies on most when making predictions.
        
        Different model types use different importance measures:
        1. Tree-based models (Random Forest, Decision Trees):
           - feature_importances_: Based on how much each feature reduces impurity
           - Higher value = feature is used more often in splits
        
        2. Linear models (Logistic Regression, Linear Regression):
           - coef_: Coefficient weights (how much each feature contributes)
           - Use absolute value (magnitude matters, not just sign)
           - For multi-class: average across all classes
        
        Why extract feature importance?
        - Understand what the model learned
        - Identify most predictive features
        - Feature selection (remove unimportant features)
        - Debugging (check if model uses expected features)
        - Explainability (show users which factors matter)
    
    Args:
        model: Trained model with feature_importances_ or coef_ attribute
              (scikit-learn style models)
        feature_names: Optional list of feature names for readability
                      If None, generates generic names like "Feature_0", "Feature_1"
    
    Returns:
        DataFrame with columns:
        - feature: Feature name
        - importance: Importance value (higher = more important)
        - importance_type: Which attribute was used ("feature_importances_" or "coef_")
        - rank: Ranking (1 = most important)
        Sorted by importance (most important first)
    """
    # Variables to store importance values and type
    # We'll determine which type of importance the model provides
    importance_values = None
    importance_type = None
    
    # Check if model has feature_importances_ attribute
    # hasattr() checks if an object has a specific attribute
    # Tree-based models (Random Forest, Decision Trees) have this
    if hasattr(model, 'feature_importances_'):
        # Extract feature importances directly
        # These are already normalized (sum to 1.0) and positive
        importance_values = model.feature_importances_
        importance_type = "feature_importances_"
    
    # Check if model has coef_ attribute (linear models)
    # Linear models (Logistic Regression, Linear Regression) have this
    elif hasattr(model, 'coef_'):
        # For linear models, coefficients can be positive or negative
        # We use absolute value because magnitude matters (not direction)
        # Example: coef = -5 is as important as coef = +5
        
        # Check if coefficients are 1D (binary classification or regression)
        # .ndim returns number of dimensions
        if model.coef_.ndim == 1:
            # Single set of coefficients (binary classification or regression)
            # np.abs() takes absolute value of each coefficient
            importance_values = np.abs(model.coef_)
        else:
            # Multi-class classification: coef_ is 2D (classes × features)
            # We average across classes to get overall feature importance
            # axis=0 means average across rows (across classes)
            # This gives one importance value per feature
            importance_values = np.mean(np.abs(model.coef_), axis=0)
        
        importance_type = "coef_"
    
    else:
        # Model doesn't support feature importance extraction
        # Raise an error with a helpful message
        raise ValueError("Model does not have feature_importances_ or coef_ attribute")
    
    # Create feature names if not provided
    # This makes the output more readable
    if feature_names is None:
        # List comprehension: creates a list of strings
        # f"Feature_{i}" creates strings like "Feature_0", "Feature_1", etc.
        # range(len(importance_values)) generates indices 0, 1, 2, ...
        feature_names = [f"Feature_{i}" for i in range(len(importance_values))]
    
    # Create traceability DataFrame
    # DataFrame is a Pandas table structure (like Excel spreadsheet)
    trace_df = pd.DataFrame({
        'feature': feature_names,  # Feature names (for readability)
        'importance': importance_values,  # Importance values
        'importance_type': importance_type,  # Which method was used
        # Calculate rank: most important = rank 1
        # np.argsort() returns indices that would sort the array
        # [::-1] reverses the order (descending: highest first)
        # + 1 converts from 0-based to 1-based ranking
        'rank': np.argsort(importance_values)[::-1] + 1
    })
    
    # Sort by importance (descending: most important first)
    # sort_values() sorts the DataFrame by a column
    # ascending=False means highest values first
    trace_df = trace_df.sort_values('importance', ascending=False)
    
    # Return the sorted DataFrame
    return trace_df


def trace_decision_path(model: Any, X_sample: np.ndarray, 
                       feature_names: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Trace decision path for a tree-based model (Decision Tree, Random Forest).
    
    Educational Explanation:
        Decision trees make predictions by following a path from root to leaf.
        Each step checks a feature value against a threshold.
        This function shows exactly which checks were made for a specific prediction.
        
        Example path:
        1. Is age > 30? → Yes
        2. Is income > 50000? → No
        3. Prediction: Class B
        
        Why trace decision paths?
        - Explain individual predictions
        - Debug why model made a specific decision
        - Verify model logic is correct
        - Build trust with users
    
    Args:
        model: Trained tree-based model (DecisionTreeClassifier, RandomForest, etc.)
        X_sample: Single sample to trace (1D array with one value per feature)
        feature_names: Optional list of feature names for readability
    
    Returns:
        Dictionary with:
        - leaf_id: ID of the leaf node where prediction was made
        - path: List of nodes visited, with feature/threshold checks
        - prediction: The model's prediction for this sample
    """
    # Handle different model types
    # Decision trees have decision_path() directly
    # Random Forests have multiple trees, we use the first one
    
    # Check if model has decision_path method
    if not hasattr(model, 'decision_path'):
        # Random Forest: has multiple trees in estimators_ list
        if hasattr(model, 'estimators_'):
            # Use first tree from the forest
            # We trace one tree's path (forests average across trees)
            tree = model.estimators_[0]
        # Single Decision Tree: has tree_ attribute
        elif hasattr(model, 'tree_'):
            tree = model
        else:
            raise ValueError("Model does not support decision path tracing")
    else:
        # Model has decision_path method (standard Decision Tree)
        tree = model
    
    # Get decision path through the tree
    if hasattr(tree, 'decision_path'):
        # decision_path() needs 2D array (samples × features)
        # X_sample is 1D, so we reshape to (1, -1) meaning "1 row, auto columns"
        # -1 means "figure out columns from data"
        path = tree.decision_path(X_sample.reshape(1, -1))
        
        # Convert sparse matrix to dense array
        # Sparse matrices only store non-zero values (memory efficient)
        # toarray() converts to regular array
        # [0] gets first row (we only have one sample)
        node_indicator = path.toarray()[0]
        
        # Get the leaf node ID (final node in the path)
        # apply() returns the leaf node ID for each sample
        # [0] gets the result for our single sample
        leaf_id = tree.apply(X_sample.reshape(1, -1))[0]
        
        # Extract information about each node in the path
        path_info = []
        
        # np.where(node_indicator == 1) finds all nodes visited (value = 1)
        # [0] gets the array of node IDs
        for node_id in np.where(node_indicator == 1)[0]:
            # Check if this is an internal node (has children)
            # Leaf nodes have children_left == children_right (both point to same place)
            # Internal nodes have different left/right children
            if tree.tree_.children_left[node_id] != tree.tree_.children_right[node_id]:
                # This is an internal node (decision point)
                
                # Get which feature is checked at this node
                feature_idx = tree.tree_.feature[node_id]
                
                # Get the threshold value for comparison
                threshold = tree.tree_.threshold[node_id]
                
                # Get feature name (or generate generic name)
                feature_name = feature_names[feature_idx] if feature_names else f"Feature_{feature_idx}"
                
                # Store information about this decision point
                path_info.append({
                    "node_id": int(node_id),  # Node identifier
                    "feature": feature_name,  # Which feature is checked
                    "threshold": float(threshold),  # Threshold value
                    "value": float(X_sample[feature_idx])  # Actual feature value
                })
        
        # Return comprehensive path information
        return {
            "leaf_id": int(leaf_id),  # Final leaf node
            "path": path_info,  # All decision points in the path
            "prediction": float(tree.predict(X_sample.reshape(1, -1))[0])  # Final prediction
        }
    else:
        return {"error": "Cannot extract decision path from this model"}


def trace_support_vectors(model: Any, X: np.ndarray, y: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """
    Trace support vectors for an SVM model.

    Args:
        model: Trained SVM model.
        X: Training features.
        y: Optional training labels.

    Returns:
        Dictionary with support vector information.
    """
    if not hasattr(model, 'support_'):
        raise ValueError("Model is not an SVM or does not have support_ attribute")
    
    support_indices = model.support_
    support_vectors = model.support_vectors_
    
    trace_info = {
        "n_support_vectors": len(support_indices),
        "support_indices": support_indices.tolist(),
        "support_vectors": support_vectors.tolist()
    }
    
    # Add labels if provided
    if y is not None:
        support_labels = y[support_indices]
        trace_info["support_labels"] = support_labels.tolist()
    
    # Add coefficients if available
    if hasattr(model, 'dual_coef_'):
        trace_info["dual_coefficients"] = model.dual_coef_.tolist()
    
    return trace_info


def trace_cluster_assignments(model: Any, X: np.ndarray, 
                             cluster_labels: Optional[np.ndarray] = None) -> pd.DataFrame:
    """
    Trace cluster assignments and characteristics.

    Args:
        model: Trained clustering model.
        X: Input features.
        cluster_labels: Optional cluster labels (if not from model).

    Returns:
        DataFrame with cluster assignment traceability.
    """
    # Get cluster labels
    if cluster_labels is None:
        if hasattr(model, 'labels_'):
            cluster_labels = model.labels_
        elif hasattr(model, 'predict'):
            cluster_labels = model.predict(X)
        else:
            raise ValueError("Cannot extract cluster labels from model")
    
    # Create trace DataFrame
    trace_df = pd.DataFrame(X)
    trace_df['cluster'] = cluster_labels
    
    # Add cluster statistics
    cluster_stats = []
    unique_clusters = np.unique(cluster_labels[cluster_labels >= 0])  # Exclude noise (-1)
    
    for cluster_id in unique_clusters:
        cluster_mask = cluster_labels == cluster_id
        cluster_data = X[cluster_mask]
        
        stats = {
            "cluster_id": int(cluster_id),
            "n_points": int(np.sum(cluster_mask)),
            "centroid": cluster_data.mean(axis=0).tolist(),
            "std": cluster_data.std(axis=0).tolist()
        }
        
        # Add centroid from model if available
        if hasattr(model, 'cluster_centers_'):
            stats["model_centroid"] = model.cluster_centers_[cluster_id].tolist()
        
        cluster_stats.append(stats)
    
    return {
        "assignments": trace_df,
        "cluster_statistics": pd.DataFrame(cluster_stats)
    }


def save_traceability_data(trace_data: Dict[str, Any], filename_prefix: str = "trace") -> str:
    """
    Save traceability data to a timestamped JSON file.

    Args:
        trace_data: Dictionary with traceability information.
        filename_prefix: Prefix for the output filename.

    Returns:
        Path to the saved file.
    """
    # Convert numpy arrays to lists for JSON serialization
    def convert_to_serializable(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, dict):
            return {k: convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, pd.DataFrame):
            return obj.to_dict('records')
        else:
            return obj
    
    serializable_data = convert_to_serializable(trace_data)
    
    output_path = timestamped_path("outputs/results", filename_prefix, "json")
    with open(output_path, 'w') as f:
        json.dump(serializable_data, f, indent=2)
    
    return str(output_path)


def create_model_card(model: Any, model_name: str, dataset_info: Dict[str, Any],
                     performance_metrics: Dict[str, float],
                     hyperparameters: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a model card with traceability information.

    Args:
        model: Trained model.
        model_name: Name of the model.
        dataset_info: Dictionary with dataset information.
        performance_metrics: Dictionary with performance metrics.
        hyperparameters: Dictionary with hyperparameters used.

    Returns:
        Dictionary representing the model card.
    """
    model_card = {
        "model_name": model_name,
        "model_type": type(model).__name__,
        "dataset": dataset_info,
        "hyperparameters": hyperparameters,
        "performance": performance_metrics,
        "timestamp": pd.Timestamp.now().isoformat()
    }
    
    # Add feature importance if available
    try:
        if hasattr(model, 'feature_importances_') or hasattr(model, 'coef_'):
            feature_importance = extract_feature_importance_trace(model)
            model_card["feature_importance"] = feature_importance.to_dict('records')
    except Exception:
        pass  # Skip if feature importance not available
    
    return model_card

