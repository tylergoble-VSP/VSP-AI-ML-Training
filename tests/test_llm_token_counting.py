"""
Unit tests for src/llm/tokenization.py
"""

# typing (type hints)
from typing import List

# src/llm/tokenization.py
from src.llm.tokenization import count_prompt_tokens  # src/llm/tokenization.py


class FakeTokenizer:
    """Simple tokenizer stub that counts words."""

    def encode(self, text: str, add_special_tokens: bool = True) -> List[int]:
        tokens = [token for token in text.split(" ") if token]
        return list(range(len(tokens)))


def test_count_prompt_tokens_counts_each_prompt() -> None:
    """It counts tokens for each prompt in a list."""
    tokenizer = FakeTokenizer()
    counts = count_prompt_tokens(tokenizer, ["hello world", "one two three"])

    assert counts == [2, 3]
