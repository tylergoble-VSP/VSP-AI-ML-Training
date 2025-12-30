"""
Used in: 14_Supervised_Logistic_Regression.ipynb and other classification notebooks
Purpose:
    Provide classification-specific utilities including extended metrics,
    ROC curve generation, and confusion matrix analysis.
"""

import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_curve, auc, roc_auc_score, confusion_matrix,
    classification_report, precision_recall_curve, average_precision_score
)  # Classification metrics
from typing import Tuple, Dict, Any, Optional  # Type hints
import matplotlib.pyplot as plt  # For plotting


def calculate_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray, 
                                     y_proba: Optional[np.ndarray] = None) -> Dict[str, float]:
    """
    Calculate comprehensive classification metrics.

    Args:
        y_true: True class labels.
        y_pred: Predicted class labels.
        y_proba: Predicted probabilities (optional, for ROC-AUC).

    Returns:
        Dictionary with accuracy, precision, recall, F1, and optionally ROC-AUC.
    """
    # Basic metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
    
    # Add ROC-AUC if probabilities are provided
    if y_proba is not None:
        try:
            # Handle binary and multiclass cases
            if y_proba.ndim == 1:
                # Binary classification
                roc_auc = roc_auc_score(y_true, y_proba)
            else:
                # Multiclass - use one-vs-rest
                roc_auc = roc_auc_score(y_true, y_proba, multi_class='ovr', average='weighted')
            metrics["roc_auc"] = roc_auc
        except Exception:
            # If ROC-AUC calculation fails, skip it
            pass
    
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

