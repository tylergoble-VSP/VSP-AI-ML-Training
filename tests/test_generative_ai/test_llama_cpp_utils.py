"""
Unit tests for src.llm.llama_cpp_utils module.
"""

import pytest
from unittest.mock import Mock, patch


class TestLoadLlamaModel:
    """Test load_llama_model function."""

    @patch('src.llm.llama_cpp_utils.Llama')
    @patch('src.llm.llama_cpp_utils.os')
    def test_load_llama_model(self, mock_os, mock_llama_class):
        """Test loading a llama.cpp model."""
        from src.llm.llama_cpp_utils import load_llama_model

        # Mock CPU count
        mock_os.cpu_count.return_value = 4

        # Mock Llama class
        mock_llama = Mock()
        mock_llama_class.return_value = mock_llama

        # Call function
        result = load_llama_model("test_model.bin", n_threads=4)

        # Assertions
        assert result is not None
        mock_llama_class.assert_called_once()


class TestQuantizeModelInfo:
    """Test quantize_model_info function."""

    @patch('src.llm.llama_cpp_utils.os.path.getsize')
    @patch('src.llm.llama_cpp_utils.os.path.exists')
    def test_quantize_model_info(self, mock_exists, mock_getsize):
        """Test extracting quantization info from model path."""
        from src.llm.llama_cpp_utils import quantize_model_info

        # Mock file exists and size
        mock_exists.return_value = True
        mock_getsize.return_value = 4 * 1024 * 1024  # 4 MB

        # Test with Q4_0 quantization
        info = quantize_model_info("model_q4_0.bin")

        assert info["quantization"] == "4-bit (Q4_0)"
        assert info["file_size_mb"] == 4.0

        # Test with GGUF format
        info = quantize_model_info("model.gguf")
        assert info["format"] == "GGUF"


class TestBenchmarkLlamaInference:
    """Test benchmark_llama_inference function."""

    def test_benchmark_llama_inference(self):
        """Test benchmarking llama inference."""
        from src.llm.llama_cpp_utils import benchmark_llama_inference

        # Mock llama model
        mock_llm = Mock()
        mock_output = {
            "choices": [{"text": "This is a test response with multiple words"}]
        }
        mock_llm.return_value = mock_output

        # Call function
        with patch('src.llm.llama_cpp_utils.generate_with_llama', return_value=mock_output):
            with patch('src.llm.llama_cpp_utils.time.time', side_effect=[0, 1, 0, 1, 0, 1]):
                result = benchmark_llama_inference(
                    mock_llm,
                    ["test prompt 1", "test prompt 2"],
                    max_tokens=50,
                    num_runs=1
                )

                assert "average_time_seconds" in result
                assert "average_tokens_per_second" in result

