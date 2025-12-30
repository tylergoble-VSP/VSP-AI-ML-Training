"""
Used in: All algorithm notebooks for traceability and interpretability
Purpose:
    Provide traceability utilities including feature importance tracking,
    decision path extraction, and model interpretation helpers.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from typing import Dict, List, Any, Optional, Tuple  # Type hints
from src.utils.paths import timestamped_path  # For timestamped output files
import json  # For saving traceability data


def extract_feature_importance_trace(model: Any, feature_names: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Extract and trace feature importance from a model.

    Args:
        model: Trained model with feature_importances_ or coef_ attribute.
        feature_names: Optional list of feature names.

    Returns:
        DataFrame with feature importance traceability information.
    """
    importance_values = None
    importance_type = None
    
    # Try different attribute names
    if hasattr(model, 'feature_importances_'):
        importance_values = model.feature_importances_
        importance_type = "feature_importances_"
    elif hasattr(model, 'coef_'):
        # For linear models, use absolute coefficients
        if model.coef_.ndim == 1:
            importance_values = np.abs(model.coef_)
        else:
            # Multi-class: use mean absolute coefficient
            importance_values = np.mean(np.abs(model.coef_), axis=0)
        importance_type = "coef_"
    else:
        raise ValueError("Model does not have feature_importances_ or coef_ attribute")
    
    # Create feature names if not provided
    if feature_names is None:
        feature_names = [f"Feature_{i}" for i in range(len(importance_values))]
    
    # Create traceability DataFrame
    trace_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importance_values,
        'importance_type': importance_type,
        'rank': np.argsort(importance_values)[::-1] + 1  # Rank 1 is most important
    })
    
    # Sort by importance
    trace_df = trace_df.sort_values('importance', ascending=False)
    
    return trace_df


def trace_decision_path(model: Any, X_sample: np.ndarray, 
                       feature_names: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Trace decision path for a tree-based model (Decision Tree, Random Forest).

    Args:
        model: Trained tree-based model.
        X_sample: Single sample to trace (1D array).
        feature_names: Optional list of feature names.

    Returns:
        Dictionary with decision path information.
    """
    # Check if model has decision_path method
    if not hasattr(model, 'decision_path'):
        # Try to get underlying estimator (for Random Forest)
        if hasattr(model, 'estimators_'):
            # Use first tree
            tree = model.estimators_[0]
        elif hasattr(model, 'tree_'):
            tree = model
        else:
            raise ValueError("Model does not support decision path tracing")
    else:
        tree = model
    
    # Get decision path
    if hasattr(tree, 'decision_path'):
        path = tree.decision_path(X_sample.reshape(1, -1))
        node_indicator = path.toarray()[0]
        
        # Get leaf node
        leaf_id = tree.apply(X_sample.reshape(1, -1))[0]
        
        # Get feature and threshold for each node in path
        path_info = []
        for node_id in np.where(node_indicator == 1)[0]:
            if tree.tree_.children_left[node_id] != tree.tree_.children_right[node_id]:
                # Internal node
                feature_idx = tree.tree_.feature[node_id]
                threshold = tree.tree_.threshold[node_id]
                feature_name = feature_names[feature_idx] if feature_names else f"Feature_{feature_idx}"
                
                path_info.append({
                    "node_id": int(node_id),
                    "feature": feature_name,
                    "threshold": float(threshold),
                    "value": float(X_sample[feature_idx])
                })
        
        return {
            "leaf_id": int(leaf_id),
            "path": path_info,
            "prediction": float(tree.predict(X_sample.reshape(1, -1))[0])
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

