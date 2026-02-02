"""
Generation wrapper with deterministic seeding and token accounting.
"""

# stdlib random (seedable RNG)
import random
# stdlib time (latency measurement)
import time
# stdlib dataclasses (lightweight typed containers)
from dataclasses import dataclass
# stdlib typing (type hints)
from typing import Dict

# numpy (seedable RNG for array ops)
import numpy as np
# torch (model execution + seeds)
import torch
# transformers tokenizer protocol
from transformers import PreTrainedTokenizerBase
# transformers base model type
from transformers import PreTrainedModel

# src/llm/config.py
from .config import LLMConfig  # src/llm/config.py


@dataclass(frozen=True)
class GenerationResult:
    """Structured generation result with token counts."""

    prompt: str
    output_text: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    latency_ms: float


def set_global_seed(seed: int) -> None:
    """Seed Python, NumPy, and Torch for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def _move_to_device(
    tensor_batch: Dict[str, torch.Tensor],
    model: PreTrainedModel,
) -> Dict[str, torch.Tensor]:
    """Move tokenized inputs to the model device when available."""
    try:
        device = next(model.parameters()).device
    except StopIteration:
        return tensor_batch
    return {key: value.to(device) for key, value in tensor_batch.items()}


def generate_text(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizerBase,
    prompt: str,
    config: LLMConfig,
) -> GenerationResult:
    """Generate text from a prompt using config-driven parameters."""
    set_global_seed(config.seed)

    tokenized = tokenizer(
        prompt,
        padding=config.tokenization.padding,
        truncation=config.tokenization.truncation,
        max_length=config.tokenization.max_length,
        return_tensors="pt",
    )
    tokenized = _move_to_device(tokenized, model)

    start_time = time.perf_counter()
    with torch.no_grad():
        output_ids = model.generate(
            **tokenized,
            max_new_tokens=config.generation.max_new_tokens,
            temperature=config.generation.temperature,
            top_p=config.generation.top_p,
            top_k=config.generation.top_k,
            repetition_penalty=config.generation.repetition_penalty,
            do_sample=config.generation.do_sample,
        )
    latency_ms = (time.perf_counter() - start_time) * 1000

    decoded_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    prompt_tokens = int(tokenized["input_ids"].shape[1])
    total_tokens = int(output_ids.shape[1])
    completion_tokens = max(total_tokens - prompt_tokens, 0)

    return GenerationResult(
        prompt=prompt,
        output_text=decoded_text,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=total_tokens,
        latency_ms=latency_ms,
    )


__all__ = ["GenerationResult", "generate_text", "set_global_seed"]
