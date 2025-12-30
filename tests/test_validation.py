"""
Unit tests for src/utils/validation.py
"""
import pytest
import numpy as np
from src.utils.validation import (
    validate_model_output,
    check_cross_validation_stability
)


def test_validate_model_output_regression():
    """Test model output validation for regression"""
    predictions = np.array([1.0, 2.0, 3.0, 4.0])
    actuals = np.array([1.1, 2.1, 2.9, 4.1])
    
    result = validate_model_output(predictions, actuals, 'regression')
    
    assert result["valid"] is True
    assert "mse" in result
    assert "rmse" in result
    assert result["rmse"] > 0


def test_validate_model_output_classification():
    """Test model output validation for classification"""
    predictions = np.array([0, 1, 0, 1])
    actuals = np.array([0, 1, 0, 1])
    
    result = validate_model_output(predictions, actuals, 'classification')
    
    assert result["valid"] is True
    assert "accuracy" in result
    assert 0 <= result["accuracy"] <= 1


def test_validate_model_output_length_mismatch():
    """Test validation with mismatched lengths"""
    predictions = np.array([1, 2, 3])
    actuals = np.array([1, 2])
    
    result = validate_model_output(predictions, actuals, 'regression')
    
    assert result["valid"] is False
    assert "reason" in result


def test_check_cross_validation_stability():
    """Test CV stability check"""
    cv_scores = np.array([0.8, 0.82, 0.79, 0.81, 0.80])
    
    result = check_cross_validation_stability(cv_scores)
    
    assert "is_stable" in result
    assert "cv_coefficient" in result
    assert isinstance(result["is_stable"], bool)
    assert result["cv_coefficient"] >= 0


def test_check_cross_validation_stability_unstable():
    """Test CV stability check with unstable scores"""
    cv_scores = np.array([0.5, 0.9, 0.3, 0.8, 0.4])
    
    result = check_cross_validation_stability(cv_scores, threshold=0.1)
    
    assert result["is_stable"] is False

