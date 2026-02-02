"""
Typed configuration for LLM interview workflows.
"""

# stdlib dataclasses (lightweight typed containers)
from dataclasses import dataclass
# stdlib pathlib (filesystem paths)
from pathlib import Path
# stdlib typing (type hints)
from typing import Any, Dict, Optional

# PyYAML (YAML parsing for config files)
import yaml


@dataclass(frozen=True)
class ModelConfig:
    """Model identifiers and optional revision information."""

    model_id: str
    tokenizer_id: Optional[str]
    revision: Optional[str]


@dataclass(frozen=True)
class EmbeddingConfig:
    """Embedding model identifiers."""

    model_id: str


@dataclass(frozen=True)
class DeviceConfig:
    """Device and dtype configuration for model loading."""

    device_strategy: str
    device_map: str
    torch_dtype: str
    quantization: str


@dataclass(frozen=True)
class TokenizationConfig:
    """Tokenizer settings for padding, truncation, and max length."""

    padding: str
    truncation: bool
    max_length: int


@dataclass(frozen=True)
class GenerationConfig:
    """Default generation parameters."""

    max_new_tokens: int
    temperature: float
    top_p: float
    top_k: int
    repetition_penalty: float
    do_sample: bool


@dataclass(frozen=True)
class LoggingConfig:
    """Output directory policy."""

    output_root: str
    logs_dir: str
    results_dir: str


@dataclass(frozen=True)
class LLMConfig:
    """Full configuration for interview workflows."""

    run_id: str
    seed: int
    model: ModelConfig
    embeddings: EmbeddingConfig
    device: DeviceConfig
    tokenization: TokenizationConfig
    generation: GenerationConfig
    logging: LoggingConfig


def load_llm_config(config_path: Path) -> LLMConfig:
    """Load and validate an LLM config from a YAML file.

    Args:
        config_path: Path to the YAML config file.

    Returns:
        Parsed and validated LLMConfig.

    Raises:
        FileNotFoundError: If the config file is missing.
        ValueError: If required fields are missing or invalid.
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    raw_data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        raise ValueError("Config file must contain a YAML mapping at the root.")

    config = _parse_llm_config(raw_data)
    _validate_llm_config(config)
    return config


def _parse_llm_config(raw_data: Dict[str, Any]) -> LLMConfig:
    """Parse a raw YAML dictionary into a typed config object."""
    model_data = _require_mapping(raw_data, "model")
    embeddings_data = _require_mapping(raw_data, "embeddings")
    device_data = _require_mapping(raw_data, "device")
    tokenization_data = _require_mapping(raw_data, "tokenization")
    generation_data = _require_mapping(raw_data, "generation")
    logging_data = _require_mapping(raw_data, "logging")

    return LLMConfig(
        run_id=_require_str(raw_data, "run_id"),
        seed=_require_int(raw_data, "seed"),
        model=ModelConfig(
            model_id=_require_str(model_data, "model_id"),
            tokenizer_id=_optional_str(model_data, "tokenizer_id"),
            revision=_optional_str(model_data, "revision"),
        ),
        embeddings=EmbeddingConfig(
            model_id=_require_str(embeddings_data, "model_id")
        ),
        device=DeviceConfig(
            device_strategy=_require_str(device_data, "device_strategy"),
            device_map=_require_str(device_data, "device_map"),
            torch_dtype=_require_str(device_data, "torch_dtype"),
            quantization=_require_str(device_data, "quantization"),
        ),
        tokenization=TokenizationConfig(
            padding=_require_str(tokenization_data, "padding"),
            truncation=_require_bool(tokenization_data, "truncation"),
            max_length=_require_int(tokenization_data, "max_length"),
        ),
        generation=GenerationConfig(
            max_new_tokens=_require_int(generation_data, "max_new_tokens"),
            temperature=_require_float(generation_data, "temperature"),
            top_p=_require_float(generation_data, "top_p"),
            top_k=_require_int(generation_data, "top_k"),
            repetition_penalty=_require_float(generation_data, "repetition_penalty"),
            do_sample=_require_bool(generation_data, "do_sample"),
        ),
        logging=LoggingConfig(
            output_root=_require_str(logging_data, "output_root"),
            logs_dir=_require_str(logging_data, "logs_dir"),
            results_dir=_require_str(logging_data, "results_dir"),
        ),
    )


def _validate_llm_config(config: LLMConfig) -> None:
    """Validate constraints and allowed values."""
    if config.device.device_strategy not in {"cpu", "cuda", "mps"}:
        raise ValueError("device.device_strategy must be one of: cpu, cuda, mps.")
    if config.device.quantization not in {"none", "8bit", "4bit"}:
        raise ValueError("device.quantization must be one of: none, 8bit, 4bit.")
    if config.device.torch_dtype not in {"float32", "float16", "bfloat16"}:
        raise ValueError(
            "device.torch_dtype must be one of: float32, float16, bfloat16."
        )
    if config.tokenization.max_length <= 0:
        raise ValueError("tokenization.max_length must be positive.")
    if config.generation.max_new_tokens <= 0:
        raise ValueError("generation.max_new_tokens must be positive.")
    if not config.model.model_id:
        raise ValueError("model.model_id cannot be empty.")
    if not config.embeddings.model_id:
        raise ValueError("embeddings.model_id cannot be empty.")


def _require_mapping(raw_data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Require a nested mapping from the config."""
    value = raw_data.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"Config key '{key}' must be a mapping.")
    return value


def _require_str(raw_data: Dict[str, Any], key: str) -> str:
    """Require a non-empty string in the config."""
    value = raw_data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Config key '{key}' must be a non-empty string.")
    return value


def _optional_str(raw_data: Dict[str, Any], key: str) -> Optional[str]:
    """Allow an optional string (may be null)."""
    value = raw_data.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"Config key '{key}' must be a string or null.")
    return value


def _require_int(raw_data: Dict[str, Any], key: str) -> int:
    """Require an integer value."""
    value = raw_data.get(key)
    if not isinstance(value, int):
        raise ValueError(f"Config key '{key}' must be an integer.")
    return value


def _require_float(raw_data: Dict[str, Any], key: str) -> float:
    """Require a numeric float (int is accepted and cast)."""
    value = raw_data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"Config key '{key}' must be a number.")
    return float(value)


def _require_bool(raw_data: Dict[str, Any], key: str) -> bool:
    """Require a boolean value."""
    value = raw_data.get(key)
    if not isinstance(value, bool):
        raise ValueError(f"Config key '{key}' must be a boolean.")
    return value


__all__ = [
    "DeviceConfig",
    "EmbeddingConfig",
    "GenerationConfig",
    "LLMConfig",
    "LoggingConfig",
    "ModelConfig",
    "TokenizationConfig",
    "load_llm_config",
]
