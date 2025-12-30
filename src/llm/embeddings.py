"""
Used in: 10_Embedding_Models
Purpose:
    Provide utilities for working with embeddings including Word2Vec, BERT, and sentence transformers.
"""

import numpy as np  # NumPy for numerical operations
from typing import List, Optional  # Type hints


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.

    Args:
        vec1: First vector.
        vec2: Second vector.

    Returns:
        Cosine similarity score (range: -1 to 1).
    """
    # Compute dot product
    dot_product = np.dot(vec1, vec2)

    # Compute magnitudes
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    # Avoid division by zero
    if norm1 == 0 or norm2 == 0:
        return 0.0

    # Cosine similarity = dot product / (norm1 * norm2)
    similarity = dot_product / (norm1 * norm2)

    return float(similarity)


def average_word_embeddings(word_embeddings: List[np.ndarray]) -> np.ndarray:
    """
    Compute average of multiple word embeddings.

    Args:
        word_embeddings: List of word embedding vectors.

    Returns:
        Average embedding vector.
    """
    # Convert to numpy array for easier computation
    embeddings_array = np.array(word_embeddings)

    # Compute mean along the first axis (average across words)
    avg_embedding = np.mean(embeddings_array, axis=0)

    return avg_embedding

