"""
Unit tests for src.llm.peft_utils module.
"""

import pytest
from unittest.mock import Mock, patch


class TestSetupLoraModel:
    """Test setup_lora_model function."""

    @patch('src.llm.peft_utils.get_peft_model')
    @patch('src.llm.peft_utils.LoraConfig')
    def test_setup_lora_model(self, mock_lora_config, mock_get_peft):
        """Test setting up LoRA on a model."""
        from src.llm.peft_utils import setup_lora_model

        # Mock model
        mock_model = Mock()

        # Mock PEFT functions
        mock_peft_model = Mock()
        mock_get_peft.return_value = mock_peft_model

        # Call function
        result = setup_lora_model(mock_model, r=8, lora_alpha=32)

        # Assertions
        assert result is not None
        mock_lora_config.assert_called_once()
        mock_get_peft.assert_called_once()


class TestGetLoraModelInfo:
    """Test get_lora_model_info function."""

    def test_get_lora_model_info(self):
        """Test getting LoRA model information."""
        from src.llm.peft_utils import get_lora_model_info
        import torch

        # Mock model with parameters
        mock_model = Mock()
        mock_param1 = Mock()
        mock_param1.numel.return_value = 1000
        mock_param1.requires_grad = True
        mock_param2 = Mock()
        mock_param2.numel.return_value = 9000
        mock_param2.requires_grad = False
        mock_model.parameters.return_value = [mock_param1, mock_param2]

        # Call function
        info = get_lora_model_info(mock_model)

        # Assertions
        assert info["trainable_parameters"] == 1000
        assert info["total_parameters"] == 10000
        assert info["trainable_percentage"] == 10.0

