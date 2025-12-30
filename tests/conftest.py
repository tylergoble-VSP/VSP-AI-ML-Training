"""
Pytest configuration and shared fixtures for all tests.
"""

import pytest
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression, make_blobs


@pytest.fixture
def sample_regression_data():
    """Generate sample regression dataset."""
    X, y = make_regression(n_samples=100, n_features=5, noise=10, random_state=42)
    return X, y


@pytest.fixture
def sample_classification_data():
    """Generate sample classification dataset."""
    X, y = make_classification(n_samples=100, n_features=5, n_classes=3, 
                               n_informative=3, random_state=42)
    return X, y


@pytest.fixture
def sample_clustering_data():
    """Generate sample clustering dataset."""
    X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
    return X, y


@pytest.fixture
def sample_dataframe():
    """Generate sample DataFrame."""
    return pd.DataFrame({
        'feature1': np.random.randn(100),
        'feature2': np.random.randn(100),
        'target': np.random.randint(0, 3, 100)
    })

