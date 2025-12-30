"""
Unit tests for src.llm.neo4j_utils module.
"""

import pytest
from unittest.mock import Mock, patch


class TestConnectNeo4j:
    """Test connect_neo4j function."""

    @patch('src.llm.neo4j_utils.GraphDatabase')
    @patch('src.llm.neo4j_utils.os.getenv')
    def test_connect_neo4j(self, mock_getenv, mock_graph_db):
        """Test connecting to Neo4j."""
        from src.llm.neo4j_utils import connect_neo4j

        # Mock environment variables
        mock_getenv.side_effect = lambda key, default: {
            "NEO4J_URI": "bolt://localhost:7687",
            "NEO4J_USER": "neo4j",
            "NEO4J_PASSWORD": "test"
        }.get(key, default)

        # Mock driver
        mock_driver = Mock()
        mock_session = Mock()
        mock_session.run.return_value = Mock()
        mock_driver.session.return_value.__enter__ = Mock(return_value=mock_session)
        mock_driver.session.return_value.__exit__ = Mock(return_value=False)
        mock_graph_db.driver.return_value = mock_driver

        driver = connect_neo4j()

        assert driver is not None
        mock_graph_db.driver.assert_called_once()


class TestCreateGraphNodes:
    """Test create_graph_nodes function."""

    def test_create_graph_nodes(self):
        """Test creating graph nodes."""
        from src.llm.neo4j_utils import create_graph_nodes

        # Mock driver
        mock_driver = Mock()
        mock_session = Mock()
        mock_record = Mock()
        mock_record.single.return_value = Mock()
        mock_session.run.return_value = mock_record
        mock_driver.session.return_value.__enter__ = Mock(return_value=mock_session)
        mock_driver.session.return_value.__exit__ = Mock(return_value=False)

        properties = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]

        count = create_graph_nodes(mock_driver, "Person", properties)

        assert count == 2


class TestQueryNeo4j:
    """Test query_neo4j function."""

    def test_query_neo4j(self):
        """Test executing a Cypher query."""
        from src.llm.neo4j_utils import query_neo4j

        # Mock driver
        mock_driver = Mock()
        mock_session = Mock()
        mock_record = Mock()
        mock_record.keys.return_value = ["name"]
        mock_record.__getitem__.return_value = "Alice"
        mock_session.run.return_value = [mock_record]
        mock_driver.session.return_value.__enter__ = Mock(return_value=mock_session)
        mock_driver.session.return_value.__exit__ = Mock(return_value=False)

        results = query_neo4j(mock_driver, "MATCH (n:Person) RETURN n.name AS name")

        assert len(results) > 0
        assert results[0]["name"] == "Alice"

