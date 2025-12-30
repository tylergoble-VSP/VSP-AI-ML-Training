"""
Unit tests for src.llm.transformers_utils module.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import torch


class TestLoadTransformersModel:
    """Test load_transformers_model function."""

    @patch('src.llm.transformers_utils.AutoTokenizer')
    @patch('src.llm.transformers_utils.AutoModelForCausalLM')
    def test_load_text_generation_model(self, mock_model_class, mock_tokenizer_class):
        """Test loading a text generation model."""
        from src.llm.transformers_utils import load_transformers_model

        # Mock tokenizer and model
        mock_tokenizer = Mock()
        mock_tokenizer.pad_token = None
        mock_tokenizer.eos_token = "<eos>"
        mock_tokenizer_class.from_pretrained.return_value = mock_tokenizer

        mock_model = Mock()
        mock_model.to.return_value = mock_model
        mock_model_class.from_pretrained.return_value = mock_model

        # Call function
        model, tokenizer = load_transformers_model("gpt2", task="text-generation")

        # Assertions
        assert model is not None
        assert tokenizer is not None
        mock_tokenizer_class.from_pretrained.assert_called_once_with("gpt2")
        mock_model_class.from_pretrained.assert_called_once()


class TestGenerateText:
    """Test generate_text function."""

    def test_generate_text_basic(self):
        """Test basic text generation."""
        from src.llm.transformers_utils import generate_text

        # Mock model and tokenizer
        mock_tokenizer = Mock()
        mock_tokenizer.pad_token_id = 0
        mock_tokenizer.decode.return_value = "generated text"

        mock_model = Mock()
        mock_model.parameters.return_value = [torch.tensor([1.0])]
        mock_outputs = Mock()
        mock_outputs.__getitem__.return_value = torch.tensor([[1, 2, 3, 4, 5]])
        mock_model.generate.return_value = mock_outputs

        # Mock inputs
        with patch('src.llm.transformers_utils.torch') as mock_torch:
            mock_torch.no_grad.return_value.__enter__ = Mock()
            mock_torch.no_grad.return_value.__exit__ = Mock(return_value=False)

            result = generate_text(
                mock_model,
                mock_tokenizer,
                "test prompt",
                max_new_tokens=10
            )

            assert isinstance(result, list)
            assert len(result) > 0


class TestGetModelInfo:
    """Test get_model_info function."""

    @patch('src.llm.transformers_utils.AutoConfig')
    @patch('src.llm.transformers_utils.AutoTokenizer')
    def test_get_model_info(self, mock_tokenizer_class, mock_config_class):
        """Test getting model information."""
        from src.llm.transformers_utils import get_model_info

        # Mock config
        mock_config = Mock()
        mock_config.model_type = "gpt2"
        mock_config.vocab_size = 50257
        mock_config.max_position_embeddings = 1024
        mock_config.hidden_size = 768
        mock_config.num_attention_heads = 12
        mock_config.num_hidden_layers = 12
        mock_config_class.from_pretrained.return_value = mock_config

        # Mock tokenizer
        mock_tokenizer = Mock()
        mock_tokenizer.__len__ = Mock(return_value=50257)
        mock_tokenizer.pad_token = "<pad>"
        mock_tokenizer.eos_token = "<eos>"
        mock_tokenizer.bos_token = "<bos>"
        mock_tokenizer_class.from_pretrained.return_value = mock_tokenizer

        # Call function
        info = get_model_info("gpt2")

        # Assertions
        assert info["model_name"] == "gpt2"
        assert info["model_type"] == "gpt2"
        assert info["vocab_size"] == 50257

