"""
Unit tests for src/models/regression.py
"""
import pytest
import numpy as np
from src.models.regression import (
    calculate_residuals,
    calculate_goodness_of_fit,
    check_residual_normality
)


def test_calculate_residuals():
    """Test residual calculation"""
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 2.0, 2.9, 4.1, 4.9])
    residuals = calculate_residuals(y_true, y_pred)
    
    expected = np.array([-0.1, 0.0, 0.1, -0.1, 0.1])
    np.testing.assert_array_almost_equal(residuals, expected, decimal=5)


def test_calculate_goodness_of_fit():
    """Test goodness of fit metrics"""
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 2.0, 2.9, 4.1, 4.9])
    
    metrics = calculate_goodness_of_fit(y_true, y_pred)
    
    assert "r2_score" in metrics
    assert "mse" in metrics
    assert "rmse" in metrics
    assert "mae" in metrics
    assert isinstance(metrics["r2_score"], float)
    assert metrics["mse"] >= 0
    assert metrics["rmse"] >= 0
    assert metrics["mae"] >= 0


def test_check_residual_normality():
    """Test residual normality check"""
    # Create normally distributed residuals
    np.random.seed(42)
    residuals = np.random.normal(0, 1, 100)
    
    result = check_residual_normality(residuals)
    
    assert "shapiro_wilk" in result
    assert "dagostino" in result
    assert "statistic" in result["shapiro_wilk"]
    assert "p_value" in result["shapiro_wilk"]
    assert "is_normal" in result["shapiro_wilk"]


def test_calculate_residuals_empty_array():
    """Test residual calculation with empty arrays"""
    y_true = np.array([])
    y_pred = np.array([])
    residuals = calculate_residuals(y_true, y_pred)
    
    assert len(residuals) == 0

