"""
Tokenizer loading and prompt token counting utilities.
"""

# stdlib typing (type hints)
from typing import Iterable, List

# transformers AutoTokenizer (Hugging Face tokenizer loader)
from transformers import AutoTokenizer
# transformers BatchEncoding + base tokenizer (tokenized output types)
from transformers import BatchEncoding, PreTrainedTokenizerBase

# src/llm/config.py
from .config import LLMConfig  # src/llm/config.py


def load_tokenizer(config: LLMConfig) -> PreTrainedTokenizerBase:
    """Load a tokenizer using config-driven identifiers.

    Args:
        config: Full LLMConfig with model/tokenizer identifiers.

    Returns:
        Loaded tokenizer instance.
    """
    tokenizer_id = config.model.tokenizer_id or config.model.model_id
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_id,
        revision=config.model.revision,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    return tokenizer


def tokenize_prompts(
    tokenizer: PreTrainedTokenizerBase,
    prompts: Iterable[str],
    config: LLMConfig,
) -> BatchEncoding:
    """Tokenize prompts with configured padding and truncation.

    Args:
        tokenizer: Tokenizer instance.
        prompts: Iterable of prompt strings.
        config: Full LLMConfig with tokenization settings.

    Returns:
        BatchEncoding with input_ids and attention_mask.
    """
    return tokenizer(
        list(prompts),
        padding=config.tokenization.padding,
        truncation=config.tokenization.truncation,
        max_length=config.tokenization.max_length,
        return_tensors="pt",
    )


def count_prompt_tokens(
    tokenizer: PreTrainedTokenizerBase,
    prompts: Iterable[str],
) -> List[int]:
    """Count tokens for each prompt string.

    Args:
        tokenizer: Tokenizer instance.
        prompts: Iterable of prompt strings.

    Returns:
        List of token counts per prompt.
    """
    counts: List[int] = []
    for prompt in prompts:
        token_ids = tokenizer.encode(prompt, add_special_tokens=True)
        counts.append(len(token_ids))
    return counts


__all__ = ["count_prompt_tokens", "load_tokenizer", "tokenize_prompts"]
