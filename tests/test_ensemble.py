"""
Unit tests for src/models/ensemble.py
"""
import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from src.models.ensemble import (
    extract_feature_importance,
    aggregate_predictions,
    calculate_oob_error
)


def test_extract_feature_importance():
    """Test feature importance extraction"""
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    importance_df = extract_feature_importance(model)
    
    assert isinstance(importance_df, pd.DataFrame)
    assert "feature" in importance_df.columns
    assert "importance" in importance_df.columns
    assert len(importance_df) == 5
    assert importance_df["importance"].sum() > 0


def test_extract_feature_importance_with_names():
    """Test feature importance with custom names"""
    X, y = make_classification(n_samples=100, n_features=3, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    feature_names = ["feat1", "feat2", "feat3"]
    importance_df = extract_feature_importance(model, feature_names)
    
    assert list(importance_df["feature"]) == feature_names


def test_aggregate_predictions_mean():
    """Test prediction aggregation with mean"""
    predictions = [
        np.array([1.0, 2.0, 3.0]),
        np.array([2.0, 3.0, 4.0]),
        np.array([0.0, 1.0, 2.0])
    ]
    
    aggregated = aggregate_predictions(predictions, method='mean')
    
    expected = np.array([1.0, 2.0, 3.0])
    np.testing.assert_array_almost_equal(aggregated, expected)


def test_aggregate_predictions_mode():
    """Test prediction aggregation with mode"""
    predictions = [
        np.array([0, 1, 0]),
        np.array([0, 1, 1]),
        np.array([0, 0, 1])
    ]
    
    aggregated = aggregate_predictions(predictions, method='mode')
    
    assert len(aggregated) == 3
    assert all(x in [0, 1] for x in aggregated)


def test_calculate_oob_error():
    """Test OOB error calculation"""
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    model = RandomForestClassifier(n_estimators=10, oob_score=True, random_state=42)
    model.fit(X, y)
    
    oob_error = calculate_oob_error(model)
    
    assert oob_error is not None
    assert 0 <= oob_error <= 1

