"""
Unit tests for src.llm.rag_utils module.
"""

import pytest
import numpy as np
from unittest.mock import Mock, patch


class TestChunkDocuments:
    """Test chunk_documents function."""

    def test_chunk_documents_basic(self):
        """Test basic document chunking."""
        from src.llm.rag_utils import chunk_documents

        documents = ["This is a long document that needs to be chunked. " * 20]
        chunks = chunk_documents(documents, chunk_size=100, chunk_overlap=10)

        assert len(chunks) > 0
        assert all("text" in chunk for chunk in chunks)
        assert all("metadata" in chunk for chunk in chunks)


class TestCreateVectorStore:
    """Test create_vector_store function."""

    @patch('src.llm.rag_utils.faiss')
    def test_create_vector_store(self, mock_faiss):
        """Test creating a FAISS vector store."""
        from src.llm.rag_utils import create_vector_store

        # Mock embedding model
        mock_model = Mock()
        mock_model.encode.return_value = np.random.rand(5, 384).astype(np.float32)

        # Mock FAISS
        mock_index = Mock()
        mock_faiss.IndexFlatL2.return_value = mock_index

        documents = ["doc1", "doc2", "doc3", "doc4", "doc5"]
        index, chunks = create_vector_store(documents, mock_model)

        assert index is not None
        assert len(chunks) > 0


class TestRetrieveRelevantDocs:
    """Test retrieve_relevant_docs function."""

    def test_retrieve_relevant_docs(self):
        """Test retrieving relevant documents."""
        from src.llm.rag_utils import retrieve_relevant_docs

        # Mock FAISS index
        mock_index = Mock()
        mock_index.search.return_value = (
            np.array([[0.1, 0.2, 0.3]]),
            np.array([[0, 1, 2]])
        )

        chunks = [
            {"text": "doc1", "metadata": {"doc_id": 0}},
            {"text": "doc2", "metadata": {"doc_id": 1}},
            {"text": "doc3", "metadata": {"doc_id": 2}}
        ]

        query_emb = np.random.rand(384).astype(np.float32)
        results = retrieve_relevant_docs(mock_index, chunks, query_emb, top_k=3)

        assert len(results) == 3
        assert all("similarity_score" in r for r in results)

