"""
Unit tests for src/models/unsupervised.py
"""
import pytest
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs
from src.models.unsupervised import (
    evaluate_clustering,
    perform_pca
)


def test_evaluate_clustering_kmeans():
    """Test clustering evaluation for KMeans"""
    X, y = make_blobs(n_samples=100, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)
    
    result = evaluate_clustering(X, labels)
    
    assert "silhouette_score" in result
    assert "inertia" in result
    assert -1 <= result["silhouette_score"] <= 1


def test_evaluate_clustering_dbscan():
    """Test clustering evaluation for DBSCAN"""
    X, y = make_blobs(n_samples=100, centers=3, random_state=42)
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(X)
    
    result = evaluate_clustering(X, labels)
    
    assert "silhouette_score" in result
    # DBSCAN may produce -1 (noise), so silhouette might be -1
    assert result["silhouette_score"] >= -1


def test_perform_pca():
    """Test PCA dimensionality reduction"""
    X, _ = make_blobs(n_samples=100, n_features=10, random_state=42)
    
    X_reduced, pca = perform_pca(X, n_components=2)
    
    assert X_reduced.shape[1] == 2
    assert X_reduced.shape[0] == X.shape[0]
    assert hasattr(pca, 'explained_variance_ratio_')

