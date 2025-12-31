"""
Used in: 04_Machine_Learning_Algorithms, 07_Unsupervised_Learning, 08_Clustering_Algorithms
Purpose:
    Provide utilities for unsupervised learning including clustering and dimensionality reduction.
    
Educational Context:
    Unsupervised learning finds patterns in data WITHOUT labels.
    
    Key Concepts:
    1. Clustering: Group similar data points together
       - K-Means: Partition data into k clusters
       - DBSCAN: Density-based clustering (finds arbitrary shapes)
       - Hierarchical: Builds tree of clusters
    
    2. Dimensionality Reduction: Reduce number of features
       - PCA: Finds directions of maximum variance
       - Preserves most information with fewer dimensions
       - Useful for visualization and speeding up algorithms
    
    Why unsupervised learning?
    - No labels needed (cheaper, faster to collect data)
    - Discover hidden patterns
    - Data exploration and understanding
    - Preprocessing for supervised learning
"""

# Import NumPy: For numerical operations
import numpy as np

# Import clustering algorithms from scikit-learn
# KMeans: Partition data into k clusters (centroid-based)
# DBSCAN: Density-based clustering (finds clusters of arbitrary shape)
# AgglomerativeClustering: Hierarchical clustering (builds cluster tree)
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

# Import PCA: Principal Component Analysis for dimensionality reduction
from sklearn.decomposition import PCA

# Import silhouette_score: Metric for evaluating clustering quality
# Measures how well-separated clusters are
from sklearn.metrics import silhouette_score

# Import type hints
from typing import Tuple


def perform_pca(X: np.ndarray, n_components: int = 2) -> Tuple[np.ndarray, PCA]:
    """
    Perform Principal Component Analysis on data.
    
    Educational Explanation:
        PCA finds new directions (principal components) that capture maximum variance.
        It transforms high-dimensional data into lower dimensions while preserving
        as much information as possible.
        
        How PCA works:
        1. Finds directions of maximum variance in data
        2. Projects data onto these directions
        3. First component captures most variance, second captures second-most, etc.
        
        Why use PCA?
        - Visualization: Reduce to 2D/3D for plotting
        - Speed: Fewer features = faster algorithms
        - Noise reduction: Removes less important dimensions
        - Feature extraction: Create new meaningful features
    
    Args:
        X: Input feature matrix (samples × features)
        n_components: Number of principal components to keep (default 2 for visualization)
    
    Returns:
        Tuple containing:
        - X_transformed: Data in lower-dimensional space (samples × n_components)
        - pca: Fitted PCA model (can transform new data later)
    """
    # Create PCA model with specified number of components
    # n_components determines how many dimensions to keep
    # Lower = more compression, less information retained
    pca = PCA(n_components=n_components)
    
    # Fit PCA to data and transform it
    # fit_transform() does two things:
    # 1. fit(): Learn the principal components from X
    # 2. transform(): Project X onto these components
    # Result: Data in lower-dimensional space
    X_transformed = pca.fit_transform(X)
    
    # Return transformed data and the model
    # The model can transform new data using the same components
    return X_transformed, pca


def kmeans_cluster(X: np.ndarray, n_clusters: int = 3, random_state: int = 42) -> Tuple[np.ndarray, KMeans]:
    """
    Perform K-Means clustering on data.
    
    Educational Explanation:
        K-Means partitions data into k clusters by:
        1. Initialize k cluster centers (centroids) randomly
        2. Assign each point to nearest centroid
        3. Update centroids to center of their points
        4. Repeat steps 2-3 until convergence
        
        Why K-Means?
        - Simple and fast
        - Works well with spherical clusters
        - Easy to interpret (each point belongs to one cluster)
        
        Limitations:
        - Must specify k (number of clusters) beforehand
        - Assumes clusters are spherical
        - Sensitive to initialization
    
    Args:
        X: Input feature matrix (samples × features)
        n_clusters: Number of clusters to create (k)
        random_state: Random seed for reproducibility (affects initialization)
    
    Returns:
        Tuple containing:
        - labels: Cluster assignment for each sample (0 to k-1)
        - kmeans: Fitted K-Means model (can predict clusters for new data)
    """
    # Create K-Means model
    # n_clusters: Number of clusters to find
    # random_state: Seed for random initialization (ensures reproducibility)
    # n_init=10: Run algorithm 10 times with different initializations, keep best
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    
    # Fit the model to data and get cluster labels
    # fit_predict() does two things:
    # 1. fit(): Learn cluster centers from X
    # 2. predict(): Assign each point to nearest cluster
    # Returns array of cluster labels (0, 1, 2, ..., k-1)
    labels = kmeans.fit_predict(X)
    
    # Return labels and model
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

