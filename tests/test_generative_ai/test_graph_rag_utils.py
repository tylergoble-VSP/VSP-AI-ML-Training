"""
Unit tests for src.llm.graph_rag_utils module.
"""

import pytest
import numpy as np
from unittest.mock import Mock, patch


class TestFormatGraphContext:
    """Test format_graph_context function."""

    def test_format_graph_context_natural(self):
        """Test formatting graph context in natural language."""
        from src.llm.graph_rag_utils import format_graph_context

        graph_results = [
            {
                "n": {
                    "labels": ["Person"],
                    "properties": {"name": "Alice"}
                },
                "r": {
                    "type": "FRIEND_OF",
                    "properties": {}
                },
                "m": {
                    "labels": ["Person"],
                    "properties": {"name": "Bob"}
                }
            }
        ]

        context = format_graph_context(graph_results, format_style="natural")

        assert len(context) > 0
        assert isinstance(context, str)


class TestMultiHopGraphQuery:
    """Test multi_hop_graph_query function."""

    @patch('src.llm.graph_rag_utils.query_neo4j')
    def test_multi_hop_graph_query(self, mock_query):
        """Test multi-hop graph traversal."""
        from src.llm.graph_rag_utils import multi_hop_graph_query

        # Mock query results
        mock_query.return_value = [
            {"path": "mock_path", "start": "Alice", "end": "Charlie"}
        ]

        # Mock driver
        mock_driver = Mock()

        results = multi_hop_graph_query(
            mock_driver,
            "Alice",
            "Person",
            max_hops=2
        )

        assert len(results) > 0
        mock_query.assert_called_once()


class TestHybridRagRetrieve:
    """Test hybrid_rag_retrieve function."""

    @patch('src.llm.graph_rag_utils.retrieve_relevant_docs')
    @patch('src.llm.graph_rag_utils.graph_rag_retrieve')
    def test_hybrid_rag_retrieve(self, mock_graph_retrieve, mock_vector_retrieve):
        """Test hybrid vector + graph retrieval."""
        from src.llm.graph_rag_utils import hybrid_rag_retrieve

        # Mock retrievers
        mock_vector_retrieve.return_value = [
            {"text": "doc1", "metadata": {}}
        ]
        mock_graph_retrieve.return_value = [
            {"n": {"properties": {"name": "Alice"}}}
        ]

        # Mock inputs
        mock_index = Mock()
        mock_chunks = [{"text": "doc1"}]
        mock_driver = Mock()
        query_emb = np.random.rand(384).astype(np.float32)

        vector_results, graph_results = hybrid_rag_retrieve(
            mock_index,
            mock_chunks,
            mock_driver,
            "test query",
            query_emb
        )

        assert len(vector_results) > 0
        assert len(graph_results) > 0

