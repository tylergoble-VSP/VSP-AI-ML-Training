"""
Unit tests for src/models/classification.py
"""
import pytest
import numpy as np
from src.models.classification import (
    calculate_classification_metrics,
    analyze_confusion_matrix
)


def test_calculate_classification_metrics_basic():
    """Test basic classification metrics calculation"""
    y_true = np.array([0, 1, 0, 1, 0])
    y_pred = np.array([0, 1, 0, 1, 0])
    
    metrics = calculate_classification_metrics(y_true, y_pred)
    
    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "f1_score" in metrics
    assert metrics["accuracy"] == 1.0
    assert 0 <= metrics["precision"] <= 1
    assert 0 <= metrics["recall"] <= 1
    assert 0 <= metrics["f1_score"] <= 1


def test_calculate_classification_metrics_with_proba():
    """Test classification metrics with probabilities"""
    y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 1])
    y_proba = np.array([0.1, 0.9, 0.2, 0.8])
    
    metrics = calculate_classification_metrics(y_true, y_pred, y_proba)
    
    assert "roc_auc" in metrics
    assert 0 <= metrics["roc_auc"] <= 1


def test_analyze_confusion_matrix():
    """Test confusion matrix analysis"""
    y_true = np.array([0, 0, 1, 1, 0, 1])
    y_pred = np.array([0, 0, 1, 1, 0, 0])
    
    result = analyze_confusion_matrix(y_true, y_pred)
    
    assert "confusion_matrix" in result
    assert "per_class_metrics" in result
    assert result["confusion_matrix"].shape == (2, 2)


def test_calculate_classification_metrics_multiclass():
    """Test classification metrics for multiclass"""
    y_true = np.array([0, 1, 2, 0, 1])
    y_pred = np.array([0, 1, 2, 0, 1])
    
    metrics = calculate_classification_metrics(y_true, y_pred)
    
    assert metrics["accuracy"] == 1.0
    assert "precision" in metrics
    assert "recall" in metrics

