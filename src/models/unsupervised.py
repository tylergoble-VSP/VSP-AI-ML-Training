"""
Used in: 04_Machine_Learning_Algorithms, 07_Unsupervised_Learning, 08_Clustering_Algorithms
Purpose:
    Provide utilities for unsupervised learning including clustering and dimensionality reduction.
"""

import numpy as np  # NumPy for numerical operations
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering  # Clustering algorithms
from sklearn.decomposition import PCA  # Principal Component Analysis
from sklearn.metrics import silhouette_score  # Clustering evaluation metric
from typing import Tuple  # Type hints


def perform_pca(X: np.ndarray, n_components: int = 2) -> Tuple[np.ndarray, PCA]:
    """
    Perform Principal Component Analysis on data.

    Args:
        X: Input feature matrix.
        n_components: Number of principal components to keep.

    Returns:
        Tuple of (transformed_data, pca_model).
    """
    # Create PCA model with specified number of components
    pca = PCA(n_components=n_components)

    # Fit and transform the data
    X_transformed = pca.fit_transform(X)

    return X_transformed, pca


def kmeans_cluster(X: np.ndarray, n_clusters: int = 3, random_state: int = 42) -> Tuple[np.ndarray, KMeans]:
    """
    Perform K-Means clustering on data.

    Args:
        X: Input feature matrix.
        n_clusters: Number of clusters to create.
        random_state: Random seed for reproducibility.

    Returns:
        Tuple of (cluster_labels, kmeans_model).
    """
    # Create K-Means model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)

    # Fit the model and get cluster labels
    labels = kmeans.fit_predict(X)

    return labels, kmeans


def evaluate_clustering(X: np.ndarray, labels: np.ndarray) -> float:
    """
    Evaluate clustering quality using silhouette score.

    Args:
        X: Input feature matrix.
        labels: Cluster labels assigned to each point.

    Returns:
        Silhouette score (higher is better, range: -1 to 1).
        Returns -1.0 if fewer than 2 clusters are found (invalid for silhouette score).
    """
    # Count unique labels (excluding noise points labeled -1 for DBSCAN)
    unique_labels = np.unique(labels)
    # Remove noise label (-1) from count if present
    n_clusters = len(unique_labels[unique_labels != -1])
    
    # Silhouette score requires at least 2 clusters
    if n_clusters < 2:
        return -1.0  # Return invalid score if insufficient clusters
    
    # Calculate silhouette score
    # Note: silhouette_score can handle noise points (-1) but needs at least 2 clusters
    score = silhouette_score(X, labels)

    return score


def dbscan_cluster(X: np.ndarray, eps: float = 0.5, min_samples: int = 5) -> Tuple[np.ndarray, DBSCAN]:
    """
    Perform DBSCAN clustering on data.

    Args:
        X: Input feature matrix.
        eps: Maximum distance between samples in the same neighborhood.
        min_samples: Minimum number of samples in a neighborhood.

    Returns:
        Tuple of (cluster_labels, dbscan_model).
    """
    # Create DBSCAN model
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)

    # Fit and predict cluster labels
    labels = dbscan.fit_predict(X)

    return labels, dbscan


def hierarchical_cluster(X: np.ndarray, n_clusters: int = 3) -> Tuple[np.ndarray, AgglomerativeClustering]:
    """
    Perform hierarchical clustering on data.

    Args:
        X: Input feature matrix.
        n_clusters: Number of clusters to create.

    Returns:
        Tuple of (cluster_labels, clustering_model).
    """
    # Create hierarchical clustering model
    clustering = AgglomerativeClustering(n_clusters=n_clusters)

    # Fit and predict cluster labels
    labels = clustering.fit_predict(X)

    return labels, clustering

