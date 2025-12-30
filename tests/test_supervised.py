"""
Unit tests for src/models/supervised.py
"""
import pytest
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from src.models.supervised import (
    split_data,
    evaluate_classifier,
    evaluate_regressor
)


def test_split_data():
    """Test data splitting function"""
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    y = np.array([0, 1, 0, 1, 0])
    
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    
    assert len(X_train) == 4
    assert len(X_test) == 1
    assert len(y_train) == 4
    assert len(y_test) == 1


def test_evaluate_classifier():
    """Test classifier evaluation"""
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    results = evaluate_classifier(model, X_test, y_test)
    
    assert "accuracy" in results
    assert 0 <= results["accuracy"] <= 1


def test_evaluate_regressor():
    """Test regressor evaluation"""
    from sklearn.linear_model import LinearRegression
    from sklearn.datasets import make_regression
    
    X, y = make_regression(n_samples=100, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    results = evaluate_regressor(model, X_test, y_test)
    
    assert "r2_score" in results
    assert "mse" in results
    assert "rmse" in results

