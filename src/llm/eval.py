"""
Evaluation utilities for golden prompt checks.
"""

# stdlib dataclasses (structured records)
from dataclasses import dataclass
# stdlib typing (type hints)
from typing import Dict, List


@dataclass(frozen=True)
class GoldenPromptCase:
    """Definition of a golden prompt with expected properties."""

    prompt: str
    expected_substrings: List[str]
    forbidden_substrings: List[str]


def evaluate_golden_prompts(
    cases: List[GoldenPromptCase],
    generated_texts: List[str],
) -> Dict[str, object]:
    """Evaluate generated outputs against golden prompt expectations.

    Args:
        cases: List of golden prompt cases.
        generated_texts: Generated outputs aligned with cases.

    Returns:
        Dictionary with per-case results and summary metrics.
    """
    if len(cases) != len(generated_texts):
        raise ValueError("cases and generated_texts must have the same length.")

    results = []
    passed_count = 0
    for case, output_text in zip(cases, generated_texts):
        expected_hits = [text for text in case.expected_substrings if text in output_text]
        forbidden_hits = [
            text for text in case.forbidden_substrings if text in output_text
        ]
        passed = len(expected_hits) == len(case.expected_substrings) and not forbidden_hits
        if passed:
            passed_count += 1
        results.append(
            {
                "prompt": case.prompt,
                "expected_hits": expected_hits,
                "forbidden_hits": forbidden_hits,
                "passed": passed,
            }
        )

    pass_rate = passed_count / len(cases) if cases else 0.0
    return {"pass_rate": pass_rate, "total_cases": len(cases), "results": results}


__all__ = ["GoldenPromptCase", "evaluate_golden_prompts"]
