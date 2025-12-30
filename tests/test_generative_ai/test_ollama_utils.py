"""
Unit tests for src.llm.ollama_utils module.
"""

import pytest
from unittest.mock import Mock, patch


class TestSetupOllamaClient:
    """Test setup_ollama_client function."""

    @patch('src.llm.ollama_utils.os.getenv')
    def test_setup_ollama_client_default(self, mock_getenv):
        """Test setting up Ollama client with defaults."""
        from src.llm.ollama_utils import setup_ollama_client

        mock_getenv.return_value = "http://localhost:11434"

        client = setup_ollama_client()

        assert client["base_url"] == "http://localhost:11434"
        assert client["timeout"] == 120


class TestOllamaChat:
    """Test ollama_chat function."""

    @patch('src.llm.ollama_utils.ollama')
    def test_ollama_chat(self, mock_ollama):
        """Test sending chat request to Ollama."""
        from src.llm.ollama_utils import ollama_chat

        # Mock response
        mock_response = {"message": {"content": "Hello!"}}
        mock_ollama.chat.return_value = mock_response

        messages = [{"role": "user", "content": "Hello"}]
        result = ollama_chat("llama2", messages)

        assert result == mock_response
        mock_ollama.chat.assert_called_once()


class TestListOllamaModels:
    """Test list_ollama_models function."""

    @patch('src.llm.ollama_utils.ollama')
    def test_list_ollama_models(self, mock_ollama):
        """Test listing Ollama models."""
        from src.llm.ollama_utils import list_ollama_models

        # Mock response
        mock_models = Mock()
        mock_model1 = Mock()
        mock_model1.name = "llama2"
        mock_model1.size = 1000000
        mock_model1.modified_at = "2024-01-01"
        mock_models.models = [mock_model1]
        mock_ollama.list.return_value = mock_models

        result = list_ollama_models()

        assert len(result) > 0
        assert result[0]["name"] == "llama2"

