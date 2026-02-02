"""
Model loading utilities for generation and embeddings.
"""

# stdlib typing (type hints)
from typing import Dict

# torch (tensor framework and dtype mapping)
import torch
# transformers AutoModelForCausalLM (Hugging Face model loader)
from transformers import AutoModelForCausalLM
# transformers base model type
from transformers import PreTrainedModel
# sentence-transformers SentenceTransformer (embedding model loader)
from sentence_transformers import SentenceTransformer

# src/llm/config.py
from .config import LLMConfig  # src/llm/config.py


def resolve_torch_dtype(dtype_name: str) -> torch.dtype:
    """Convert a dtype string into a torch.dtype.

    Args:
        dtype_name: One of float32, float16, bfloat16.

    Returns:
        torch.dtype mapping.
    """
    mapping = {
        "float32": torch.float32,
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
    }
    if dtype_name not in mapping:
        raise ValueError(f"Unsupported torch_dtype: {dtype_name}")
    return mapping[dtype_name]


def _quantization_kwargs(config: LLMConfig) -> Dict[str, bool]:
    """Build optional quantization kwargs for HF model loading."""
    if config.device.quantization == "8bit":
        return {"load_in_8bit": True}
    if config.device.quantization == "4bit":
        return {"load_in_4bit": True}
    return {}


def load_generation_model(config: LLMConfig) -> PreTrainedModel:
    """Load a causal language model using config-driven settings."""
    dtype = resolve_torch_dtype(config.device.torch_dtype)
    quantization_kwargs = _quantization_kwargs(config)

    model = AutoModelForCausalLM.from_pretrained(
        config.model.model_id,
        revision=config.model.revision,
        device_map=config.device.device_map,
        torch_dtype=dtype,
        **quantization_kwargs,
    )
    return model


def load_embedding_model(config: LLMConfig) -> SentenceTransformer:
    """Load an embedding model (SentenceTransformer) using config settings."""
    return SentenceTransformer(
        config.embeddings.model_id,
        device=config.device.device_strategy,
    )


__all__ = ["load_embedding_model", "load_generation_model", "resolve_torch_dtype"]
