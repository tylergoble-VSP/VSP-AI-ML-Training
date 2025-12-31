"""
Used in: 07_GenerativeAI_Retrieval_Augmented_Generation.ipynb
Purpose:
    Provide utilities for Retrieval-Augmented Generation (RAG),
    including vector store creation, document chunking, retrieval, and context formatting.
    
Educational Context:
    RAG (Retrieval-Augmented Generation) combines retrieval and generation.
    
    How RAG Works:
    1. Chunk documents into smaller pieces
    2. Create embeddings for each chunk
    3. Store embeddings in vector database
    4. When query comes in:
       a. Embed the query
       b. Find similar document chunks (retrieval)
       c. Pass chunks as context to LLM
       d. LLM generates answer using context
    
    Why RAG?
    - LLMs have limited knowledge (training cutoff date)
    - Can't update LLM knowledge easily
    - RAG allows using external documents
    - Reduces hallucinations (grounded in retrieved docs)
    - Enables domain-specific knowledge
    
    Key Components:
    - Document chunking: Split large docs into manageable pieces
    - Vector store: Fast similarity search
    - Retrieval: Find relevant chunks for query
    - Context formatting: Prepare context for LLM
"""

# Import type hints
from typing import List, Dict, Any, Optional, Tuple

# Import NumPy: For array operations
import numpy as np


def chunk_documents(
    documents: List[str],
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    separator: str = "\n\n"
) -> List[Dict[str, Any]]:
    """
    Split documents into chunks for embedding and retrieval.

    Args:
        documents: List of document strings.
        chunk_size: Target size of each chunk in characters.
        chunk_overlap: Number of characters to overlap between chunks.
        separator: Separator to use when splitting documents.

    Returns:
        List of dictionaries with 'text' and 'metadata' keys.
    """
    chunks = []

    for doc_idx, doc in enumerate(documents):
        # Split document by separator first
        sections = doc.split(separator)

        current_chunk = ""
        chunk_idx = 0

        for section in sections:
            # If adding this section would exceed chunk size, save current chunk
            if len(current_chunk) + len(section) > chunk_size and current_chunk:
                chunks.append({
                    "text": current_chunk.strip(),
                    "metadata": {
                        "doc_id": doc_idx,
                        "chunk_id": chunk_idx,
                        "chunk_size": len(current_chunk)
                    }
                })
                chunk_idx += 1

                # Start new chunk with overlap
                if chunk_overlap > 0 and current_chunk:
                    overlap_text = current_chunk[-chunk_overlap:]
                    current_chunk = overlap_text + section
                else:
                    current_chunk = section
            else:
                current_chunk += separator + section if current_chunk else section

        # Add remaining chunk
        if current_chunk.strip():
            chunks.append({
                "text": current_chunk.strip(),
                "metadata": {
                    "doc_id": doc_idx,
                    "chunk_id": chunk_idx,
                    "chunk_size": len(current_chunk)
                }
            })

    return chunks


def create_vector_store(
    documents: List[str],
    embedding_model: Any,
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> Tuple[Any, List[Dict[str, Any]]]:
    """
    Create a FAISS vector store from documents.

    Args:
        documents: List of document strings.
        embedding_model: Sentence transformer or embedding model.
        chunk_size: Size of document chunks.
        chunk_overlap: Overlap between chunks.

    Returns:
        Tuple of (FAISS index, list of chunk dictionaries).
    """
    try:
        import faiss
    except ImportError:
        raise ImportError(
            "faiss-cpu or faiss-gpu is not installed. Install with: pip install faiss-cpu"
        )

    # Chunk documents
    chunks = chunk_documents(documents, chunk_size, chunk_overlap)

    # Generate embeddings for all chunks
    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = embedding_model.encode(chunk_texts)

    # Convert to numpy array with float32
    embeddings = np.array(embeddings, dtype=np.float32)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity

    # Add embeddings to index
    index.add(embeddings)

    return index, chunks


def retrieve_relevant_docs(
    index: Any,
    chunks: List[Dict[str, Any]],
    query_embedding: np.ndarray,
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Retrieve top-k most relevant documents using vector similarity.

    Args:
        index: FAISS index containing document embeddings.
        chunks: List of chunk dictionaries.
        query_embedding: Query embedding vector.
        top_k: Number of documents to retrieve.

    Returns:
        List of retrieved chunk dictionaries with similarity scores.
    """
    # Ensure query embedding is float32 and 2D
    query_emb = np.array([query_embedding], dtype=np.float32)

    # Search for top-k similar vectors
    distances, indices = index.search(query_emb, top_k)

    # Retrieve corresponding chunks
    retrieved = []
    for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
        if idx < len(chunks):
            chunk = chunks[idx].copy()
            chunk["similarity_score"] = float(dist)
            chunk["rank"] = i + 1
            retrieved.append(chunk)

    return retrieved


def format_rag_context(
    retrieved_docs: List[Dict[str, Any]],
    query: str,
    format_style: str = "numbered"
) -> str:
    """
    Format retrieved documents into context for LLM prompt.

    Args:
        retrieved_docs: List of retrieved document chunks.
        query: Original user query.
        format_style: Format style ("numbered", "bullet", "paragraph").

    Returns:
        Formatted context string.
    """
    context_parts = []

    if format_style == "numbered":
        for i, doc in enumerate(retrieved_docs, 1):
            context_parts.append(f"Context {i}: {doc['text']}")
    elif format_style == "bullet":
        for doc in retrieved_docs:
            context_parts.append(f"- {doc['text']}")
    else:  # paragraph
        context_parts = [doc['text'] for doc in retrieved_docs]

    context = "\n\n".join(context_parts)

    # Create full prompt
    prompt = f"""Context:
{context}

Question: {query}

Answer based on the context above:"""

    return prompt


def evaluate_rag_quality(
    retrieved_docs: List[Dict[str, Any]],
    ground_truth_doc_ids: Optional[List[int]] = None
) -> Dict[str, Any]:
    """
    Evaluate RAG retrieval quality.

    Args:
        retrieved_docs: List of retrieved documents.
        ground_truth_doc_ids: Optional list of ground truth document IDs that should be retrieved.

    Returns:
        Dictionary containing quality metrics.
    """
    metrics = {
        "num_retrieved": len(retrieved_docs),
        "avg_similarity": 0.0,
        "recall": None,
        "precision": None
    }

    if retrieved_docs:
        # Calculate average similarity
        similarities = [doc.get("similarity_score", 0.0) for doc in retrieved_docs]
        metrics["avg_similarity"] = sum(similarities) / len(similarities) if similarities else 0.0

        # Calculate recall and precision if ground truth provided
        if ground_truth_doc_ids:
            retrieved_ids = [doc.get("metadata", {}).get("doc_id") for doc in retrieved_docs]
            retrieved_set = set(retrieved_ids)
            truth_set = set(ground_truth_doc_ids)

            # Recall: how many relevant docs were retrieved
            if truth_set:
                metrics["recall"] = len(retrieved_set & truth_set) / len(truth_set)

            # Precision: how many retrieved docs are relevant
            if retrieved_set:
                metrics["precision"] = len(retrieved_set & truth_set) / len(retrieved_set)

    return metrics

