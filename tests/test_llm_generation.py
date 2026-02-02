"""
Unit tests for src/llm/generation.py
"""

# typing (type hints)
from typing import Dict

# torch (tensor utilities)
import torch

# src/llm/config.py
from src.llm.config import (  # src/llm/config.py
    DeviceConfig,
    EmbeddingConfig,
    GenerationConfig,
    LLMConfig,
    LoggingConfig,
    ModelConfig,
    TokenizationConfig,
)
# src/llm/generation.py
from src.llm.generation import generate_text  # src/llm/generation.py


class FakeTokenizer:
    """Tokenizer stub that returns fixed token IDs."""

    def __call__(self, text: str, **kwargs) -> Dict[str, torch.Tensor]:
        return {"input_ids": torch.tensor([[1, 2, 3]])}

    def decode(self, token_ids, skip_special_tokens: bool = True) -> str:
        return "decoded text"


class FakeModel(torch.nn.Module):
    """Model stub that returns deterministic output IDs."""

    def __init__(self) -> None:
        super().__init__()
        self._dummy = torch.nn.Parameter(torch.zeros(1))

    def generate(self, **kwargs) -> torch.Tensor:
        return torch.tensor([[1, 2, 3, 4, 5]])


def _build_config() -> LLMConfig:
    """Create a minimal config for generation tests."""
    return LLMConfig(
        run_id="test_run",
        seed=123,
        model=ModelConfig(model_id="dummy", tokenizer_id=None, revision=None),
        embeddings=EmbeddingConfig(model_id="dummy-embedder"),
        device=DeviceConfig(
            device_strategy="cpu",
            device_map="cpu",
            torch_dtype="float32",
            quantization="none",
        ),
        tokenization=TokenizationConfig(
            padding="max_length",
            truncation=True,
            max_length=8,
        ),
        generation=GenerationConfig(
            max_new_tokens=5,
            temperature=0.1,
            top_p=0.95,
            top_k=10,
            repetition_penalty=1.0,
            do_sample=False,
        ),
        logging=LoggingConfig(
            output_root="outputs",
            logs_dir="outputs/logs",
            results_dir="outputs/results",
        ),
    )


def test_generate_text_returns_token_counts() -> None:
    """It returns prompt, completion, and total token counts."""
    config = _build_config()
    model = FakeModel()
    tokenizer = FakeTokenizer()

    result = generate_text(model, tokenizer, "hello", config)

    assert result.prompt_tokens == 3
    assert result.completion_tokens == 2
    assert result.total_tokens == 5
    assert result.output_text == "decoded text"
