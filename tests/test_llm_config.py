"""
Unit tests for src/llm/config.py
"""

# stdlib pathlib (filesystem paths)
from pathlib import Path

# pytest (testing framework)
import pytest

# src/llm/config.py
from src.llm.config import load_llm_config  # src/llm/config.py


def test_load_llm_config_parses_yaml(tmp_path: Path) -> None:
    """It loads a YAML config into typed fields."""
    config_path = tmp_path / "llm_config.yaml"
    config_path.write_text(
        """
run_id: "test_run"
seed: 7
model:
  model_id: "test-model"
  tokenizer_id: "test-tokenizer"
  revision: null
embeddings:
  model_id: "test-embedder"
device:
  device_strategy: "cpu"
  device_map: "cpu"
  torch_dtype: "float32"
  quantization: "none"
tokenization:
  padding: "max_length"
  truncation: true
  max_length: 16
generation:
  max_new_tokens: 8
  temperature: 0.1
  top_p: 0.95
  top_k: 10
  repetition_penalty: 1.0
  do_sample: false
logging:
  output_root: "outputs"
  logs_dir: "outputs/logs"
  results_dir: "outputs/results"
""",
        encoding="utf-8",
    )

    config = load_llm_config(config_path)

    assert config.run_id == "test_run"
    assert config.model.model_id == "test-model"
    assert config.embeddings.model_id == "test-embedder"
    assert config.generation.max_new_tokens == 8


def test_load_llm_config_rejects_bad_dtype(tmp_path: Path) -> None:
    """It raises a helpful error for unsupported dtypes."""
    config_path = tmp_path / "llm_config.yaml"
    config_path.write_text(
        """
run_id: "test_run"
seed: 7
model:
  model_id: "test-model"
  tokenizer_id: "test-tokenizer"
  revision: null
embeddings:
  model_id: "test-embedder"
device:
  device_strategy: "cpu"
  device_map: "cpu"
  torch_dtype: "float128"
  quantization: "none"
tokenization:
  padding: "max_length"
  truncation: true
  max_length: 16
generation:
  max_new_tokens: 8
  temperature: 0.1
  top_p: 0.95
  top_k: 10
  repetition_penalty: 1.0
  do_sample: false
logging:
  output_root: "outputs"
  logs_dir: "outputs/logs"
  results_dir: "outputs/results"
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="torch_dtype"):
        load_llm_config(config_path)
