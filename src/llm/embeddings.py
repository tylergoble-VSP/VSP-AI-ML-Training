"""
Used in: 10_Embedding_Models
Purpose:
    Provide utilities for working with embeddings including Word2Vec, BERT, and sentence transformers.
    
Educational Context:
    Embeddings convert text into numerical vectors that capture meaning.
    
    Key Concepts:
    1. Word Embeddings: Dense vector representations of words
       - Similar words have similar vectors
       - Can do arithmetic: king - man + woman ≈ queen
       - Examples: Word2Vec, GloVe
    
    2. Contextual Embeddings: Vectors that depend on context
       - Same word has different vectors in different contexts
       - Examples: BERT, ELMo, GPT
    
    3. Sentence Embeddings: Vectors representing entire sentences
       - Capture semantic meaning of full sentences
       - Examples: Sentence-BERT, Universal Sentence Encoder
    
    Why embeddings?
    - ML models need numbers, not text
    - Capture semantic relationships
    - Enable similarity search
    - Foundation for NLP tasks
"""

# Import NumPy: For numerical operations on arrays
import numpy as np

# Import type hints
from typing import List, Optional


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Educational Explanation:
        Cosine similarity measures the angle between two vectors, not their magnitude.
        Formula: cos(θ) = (A · B) / (||A|| × ||B||)
        
        Why cosine similarity?
        - Measures direction, not magnitude (good for embeddings)
        - Range: -1 (opposite) to 1 (identical) to 0 (orthogonal)
        - Normalized (not affected by vector length)
        - Standard metric for comparing embeddings
        
        Interpretation:
        - 1.0: Vectors point in same direction (very similar)
        - 0.0: Vectors are perpendicular (unrelated)
        - -1.0: Vectors point in opposite directions (opposites)
    
    Args:
        vec1: First embedding vector
        vec2: Second embedding vector (same dimension as vec1)
    
    Returns:
        Cosine similarity score (float between -1.0 and 1.0)
        Higher = more similar
    """
    # Compute dot product (sum of element-wise products)
    # Measures how much vectors point in same direction
    # Example: [1,2] · [3,4] = 1×3 + 2×4 = 11
    dot_product = np.dot(vec1, vec2)
    
    # Compute magnitudes (lengths) of vectors
    # np.linalg.norm() calculates Euclidean norm (L2 norm)
    # ||v|| = sqrt(v₁² + v₂² + ... + vₙ²)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    # Handle edge case: zero vectors
    # If either vector has zero magnitude, similarity is undefined
    # Return 0.0 as neutral value (no similarity)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    # Calculate cosine similarity
    # Formula: cos(θ) = (A · B) / (||A|| × ||B||)
    # This normalizes by vector lengths, measuring angle between vectors
    similarity = dot_product / (norm1 * norm2)
    
    # Convert to Python float (NumPy might return numpy.float64)
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

