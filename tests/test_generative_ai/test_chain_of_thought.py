"""
Unit tests for src.llm.chain_of_thought module.
"""

import pytest


class TestApplyCotPrompting:
    """Test apply_cot_prompting function."""

    def test_apply_cot_prompting_basic(self):
        """Test basic CoT prompting."""
        from src.llm.chain_of_thought import apply_cot_prompting

        question = "What is 2 + 2?"
        prompt = apply_cot_prompting(question)

        assert "Q:" in prompt
        assert question in prompt
        assert "Let's think step by step" in prompt

    def test_apply_cot_prompting_with_examples(self):
        """Test CoT prompting with few-shot examples."""
        from src.llm.chain_of_thought import apply_cot_prompting

        examples = [
            {
                "question": "What is 1 + 1?",
                "answer": "2",
                "reasoning": "1 plus 1 equals 2"
            }
        ]

        prompt = apply_cot_prompting("What is 3 + 3?", few_shot_examples=examples)

        assert "Q:" in prompt
        assert "1 + 1" in prompt
        assert "3 + 3" in prompt


class TestExtractReasoningSteps:
    """Test extract_reasoning_steps function."""

    def test_extract_reasoning_steps_numbered(self):
        """Test extracting numbered reasoning steps."""
        from src.llm.chain_of_thought import extract_reasoning_steps

        text = """
        1. First step: Add the numbers
        2. Second step: Check the result
        3. Final step: Verify
        """

        steps = extract_reasoning_steps(text)

        assert len(steps) >= 2
        assert "First step" in steps[0] or "Add" in steps[0]


class TestExtractFinalAnswer:
    """Test extract_final_answer function."""

    def test_extract_final_answer_pattern1(self):
        """Test extracting answer with 'Therefore' pattern."""
        from src.llm.chain_of_thought import extract_final_answer

        text = "Let's think. First step. Therefore, the answer is 42."
        answer = extract_final_answer(text)

        assert answer is not None
        assert "42" in answer

    def test_extract_final_answer_pattern2(self):
        """Test extracting answer with 'Answer is' pattern."""
        from src.llm.chain_of_thought import extract_final_answer

        text = "Reasoning here. Answer is 100."
        answer = extract_final_answer(text)

        assert answer is not None
        assert "100" in answer

