"""
Used in: 14_Supervised_Logistic_Regression.ipynb and other classification notebooks
Purpose:
    Provide classification-specific utilities including extended metrics,
    ROC curve generation, and confusion matrix analysis.
    
Educational Context:
    Classification is predicting discrete categories (classes) from data.
    Examples: spam/not spam, cat/dog/bird, disease/no disease.
    
    Key Metrics:
    1. Accuracy: Overall correctness (correct predictions / total)
    2. Precision: Of predicted positives, how many were actually positive?
    3. Recall: Of actual positives, how many did we find?
    4. F1 Score: Harmonic mean of precision and recall (balanced metric)
    5. ROC-AUC: Area under ROC curve (measures classifier quality)
    
    Confusion Matrix:
    - Shows true positives, false positives, true negatives, false negatives
    - Helps understand what types of errors the model makes
    
    ROC Curve:
    - Plots True Positive Rate vs False Positive Rate
    - Shows trade-off between sensitivity and specificity
    - AUC (Area Under Curve) summarizes classifier performance
"""

# Import NumPy: For numerical operations on arrays
import numpy as np

# Import Pandas: For DataFrame operations
import pandas as pd

# Import scikit-learn classification metrics
# These are standard metrics for evaluating classification models
from sklearn.metrics import (
    accuracy_score,  # Proportion of correct predictions
    precision_score,  # Precision: TP / (TP + FP)
    recall_score,  # Recall (Sensitivity): TP / (TP + FN)
    f1_score,  # F1: harmonic mean of precision and recall
    roc_curve,  # Generate points for ROC curve
    auc,  # Calculate area under curve
    roc_auc_score,  # Calculate ROC-AUC directly
    confusion_matrix,  # Generate confusion matrix
    classification_report,  # Comprehensive classification metrics
    precision_recall_curve,  # Precision-recall curve
    average_precision_score  # Average precision score
)

# Import type hints for better code documentation
from typing import Tuple, Dict, Any, Optional

# Import matplotlib for plotting visualizations
import matplotlib.pyplot as plt


def calculate_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray, 
                                     y_proba: Optional[np.ndarray] = None) -> Dict[str, float]:
    """
    Calculate comprehensive classification metrics.
    
    Educational Explanation:
        This function computes multiple metrics to thoroughly evaluate a classifier.
        
        Metrics Explained:
        1. Accuracy: (TP + TN) / (TP + TN + FP + FN)
           - Overall correctness
           - Can be misleading with imbalanced classes
        
        2. Precision: TP / (TP + FP)
           - "Of what we predicted as positive, how many were actually positive?"
           - High precision = few false positives
           - Important when false positives are costly
        
        3. Recall: TP / (TP + FN)
           - "Of all actual positives, how many did we find?"
           - High recall = few false negatives
           - Important when missing positives is costly
        
        4. F1 Score: 2 × (precision × recall) / (precision + recall)
           - Harmonic mean of precision and recall
           - Balances both metrics
           - Good single-number summary
        
        5. ROC-AUC: Area Under ROC Curve
           - Measures classifier's ability to distinguish classes
           - Range: 0.5 (random) to 1.0 (perfect)
           - Requires probability predictions
    
    Args:
        y_true: True class labels (ground truth)
        y_pred: Predicted class labels (model predictions)
        y_proba: Optional predicted probabilities
                - Binary: 1D array of probabilities for positive class
                - Multiclass: 2D array (samples × classes)
    
    Returns:
        Dictionary with metrics:
        - accuracy: Overall correctness (0.0 to 1.0)
        - precision: Precision score (0.0 to 1.0)
        - recall: Recall score (0.0 to 1.0)
        - f1_score: F1 score (0.0 to 1.0)
        - roc_auc: ROC-AUC score (if y_proba provided, 0.0 to 1.0)
    """
    # Calculate basic classification metrics
    # These metrics work with class labels (not probabilities)
    
    # Accuracy: Proportion of correct predictions
    # Simple but can be misleading with imbalanced data
    accuracy = accuracy_score(y_true, y_pred)
    
    # Precision: Weighted average across all classes
    # 'weighted' accounts for class imbalance (weights by class frequency)
    # zero_division=0 handles edge case when no predictions of a class
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # Recall: Weighted average across all classes
    # Also handles class imbalance with 'weighted' average
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # F1 Score: Harmonic mean of precision and recall
    # Provides balanced view of model performance
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    # Build metrics dictionary with basic metrics
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
    
    # Add ROC-AUC if probability predictions are provided
    # ROC-AUC requires probabilities, not just class labels
    if y_proba is not None:
        try:
            # Check if binary or multiclass classification
            # .ndim returns number of dimensions
            if y_proba.ndim == 1:
                # Binary classification: 1D array of probabilities
                # Each value is probability of positive class
                roc_auc = roc_auc_score(y_true, y_proba)
            else:
                # Multiclass: 2D array (samples × classes)
                # Each row has probabilities for all classes
                # 'ovr' = one-vs-rest (compare each class vs all others)
                # 'weighted' = average across classes, weighted by frequency
                roc_auc = roc_auc_score(y_true, y_proba, multi_class='ovr', average='weighted')
            
            # Add ROC-AUC to metrics dictionary
            metrics["roc_auc"] = roc_auc
        except Exception:
            # If ROC-AUC calculation fails (e.g., only one class in y_true),
            # skip it rather than crashing
            # This makes the function more robust
            pass
    
    # Return all calculated metrics
    return metrics


def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, 
                         class_names: Optional[list] = None, 
                         title: str = "Confusion Matrix") -> None:
    """
    Plot a confusion matrix with annotations.

    Args:
        y_true: True class labels.
        y_pred: Predicted class labels.
        class_names: Optional list of class names for labels.
        title: Plot title.
    """
    cm = confusion_matrix(y_true, y_pred)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    
    # Set labels
    if class_names is None:
        class_names = [f"Class {i}" for i in range(len(np.unique(y_true)))]
    
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=class_names,
           yticklabels=class_names,
           title=title,
           ylabel='True Label',
           xlabel='Predicted Label')
    
    # Add text annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                   ha="center", va="center",
                   color="white" if cm[i, j] > thresh else "black")
    
    plt.tight_layout()
    plt.show()


def plot_roc_curve(y_true: np.ndarray, y_proba: np.ndarray, 
                   title: str = "ROC Curve") -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Plot ROC curve and calculate AUC.

    Args:
        y_true: True binary class labels (0 or 1).
        y_proba: Predicted probabilities for positive class.
        title: Plot title.

    Returns:
        Tuple of (AUC score, fpr array, tpr array).
    """
    # Calculate ROC curve
    fpr, tpr, thresholds = roc_curve(y_true, y_proba)
    
    # Calculate AUC
    roc_auc = auc(fpr, tpr)
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
             label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return roc_auc, fpr, tpr


def plot_precision_recall_curve(y_true: np.ndarray, y_proba: np.ndarray,
                                title: str = "Precision-Recall Curve") -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Plot precision-recall curve and calculate average precision.

    Args:
        y_true: True binary class labels (0 or 1).
        y_proba: Predicted probabilities for positive class.
        title: Plot title.

    Returns:
        Tuple of (average precision, precision array, recall array).
    """
    # Calculate precision-recall curve
    precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
    
    # Calculate average precision
    avg_precision = average_precision_score(y_true, y_proba)
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(recall, precision, color='blue', lw=2,
             label=f'PR curve (AP = {avg_precision:.2f})')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(title)
    plt.legend(loc="lower left")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return avg_precision, precision, recall


def analyze_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, Any]:
    """
    Analyze confusion matrix and extract per-class metrics.

    Args:
        y_true: True class labels.
        y_pred: Predicted class labels.

    Returns:
        Dictionary with confusion matrix and per-class metrics.
    """
    cm = confusion_matrix(y_true, y_pred)
    
    # Calculate per-class metrics
    n_classes = cm.shape[0]
    per_class_metrics = {}
    
    for i in range(n_classes):
        tp = cm[i, i]  # True positives
        fp = cm[:, i].sum() - tp  # False positives
        fn = cm[i, :].sum() - tp  # False negatives
        tn = cm.sum() - tp - fp - fn  # True negatives
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        per_class_metrics[f"class_{i}"] = {
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "support": tp + fn
        }
    
    return {
        "confusion_matrix": cm,
        "per_class_metrics": per_class_metrics
    }

