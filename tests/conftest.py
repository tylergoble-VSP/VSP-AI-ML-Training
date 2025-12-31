"""
Pytest configuration and shared fixtures for all tests.
    
Educational Context:
    conftest.py is a special pytest file that provides:
    1. Shared fixtures (reusable test data)
    2. Configuration for all tests in the directory
    3. Common setup/teardown code
    
    Fixtures:
    - Functions decorated with @pytest.fixture
    - Automatically available to all tests
    - Can be passed as function parameters
    - Run before test, cleaned up after
    
    Why fixtures?
    - Avoid duplicating test data creation
    - Consistent test data across tests
    - Easy to modify test data in one place
    - Can have setup/teardown logic
"""

# Import pytest: Testing framework
import pytest

# Import NumPy: For numerical operations
import numpy as np

# Import Pandas: For DataFrame operations
import pandas as pd

# Import scikit-learn dataset generators
# make_classification: Generate synthetic classification data
# make_regression: Generate synthetic regression data
# make_blobs: Generate synthetic clustering data (Gaussian blobs)
from sklearn.datasets import make_classification, make_regression, make_blobs


@pytest.fixture
def sample_regression_data():
    """
    Generate sample regression dataset.
    
    Educational Explanation:
        This fixture creates synthetic regression data for testing.
        Regression predicts continuous values (numbers).
        
        Parameters:
        - n_samples: Number of data points (100)
        - n_features: Number of input features (5)
        - noise: Amount of random noise (10)
        - random_state: Seed for reproducibility (42)
    
    Returns:
        Tuple of (X, y):
        - X: Feature matrix (100 samples × 5 features)
        - y: Target values (100 continuous values)
    """
    # Generate synthetic regression data
    # make_regression creates data where y is a linear combination of X features
    # noise parameter adds random variation (makes it more realistic)
    # random_state ensures same data every time (reproducible tests)
    X, y = make_regression(n_samples=100, n_features=5, noise=10, random_state=42)
    return X, y


@pytest.fixture
def sample_classification_data():
    """
    Generate sample classification dataset.
    
    Educational Explanation:
        This fixture creates synthetic classification data for testing.
        Classification predicts discrete categories (classes).
        
        Parameters:
        - n_samples: Number of data points (100)
        - n_features: Number of input features (5)
        - n_classes: Number of classes to predict (3)
        - n_informative: Number of informative features (3)
        - random_state: Seed for reproducibility (42)
    
    Returns:
        Tuple of (X, y):
        - X: Feature matrix (100 samples × 5 features)
        - y: Class labels (100 integers: 0, 1, or 2)
    """
    # Generate synthetic classification data
    # make_classification creates data with clear class boundaries
    # n_informative: Features that actually help classify
    # Other features are redundant or noise
    X, y = make_classification(n_samples=100, n_features=5, n_classes=3, 
                               n_informative=3, random_state=42)
    return X, y


@pytest.fixture
def sample_clustering_data():
    """
    Generate sample clustering dataset.
    
    Educational Explanation:
        This fixture creates synthetic clustering data for testing.
        Clustering finds groups in data (unsupervised learning).
        
        Parameters:
        - n_samples: Number of data points (100)
        - centers: Number of clusters (3)
        - n_features: Number of features (2, for easy visualization)
        - random_state: Seed for reproducibility (42)
    
    Returns:
        Tuple of (X, y):
        - X: Feature matrix (100 samples × 2 features)
        - y: True cluster labels (for validation, 0, 1, or 2)
    """
    # Generate synthetic clustering data
    # make_blobs creates Gaussian blobs (clusters) in feature space
    # Perfect for testing clustering algorithms
    # 2 features makes it easy to visualize (can plot in 2D)
    X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
    return X, y


@pytest.fixture
def sample_dataframe():
    """
    Generate sample DataFrame.
    
    Educational Explanation:
        This fixture creates a simple DataFrame for testing pandas operations.
        DataFrame is a 2D table structure (rows and columns).
        
        Columns:
        - feature1: Random numbers from normal distribution
        - feature2: Random numbers from normal distribution
        - target: Random integers (0, 1, or 2) for classification
    
    Returns:
        DataFrame with 100 rows and 3 columns
    """
    # Create DataFrame with synthetic data
    # np.random.randn(): Random numbers from standard normal distribution (mean=0, std=1)
    # np.random.randint(): Random integers in range [0, 3) (0, 1, or 2)
    return pd.DataFrame({
        'feature1': np.random.randn(100),  # 100 random numbers
        'feature2': np.random.randn(100),  # 100 random numbers
        'target': np.random.randint(0, 3, 100)  # 100 random integers (0, 1, or 2)
    })

