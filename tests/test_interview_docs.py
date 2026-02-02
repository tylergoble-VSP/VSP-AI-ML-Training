"""
Tests for interview material documentation files.
"""
from pathlib import Path  # standard library: filesystem paths
import pytest  # third-party: pytest test runner


@pytest.mark.parametrize(
    "doc_path,required_headings",
    [
        (
            Path("Interview/Machine_Learning/Traditional_ML_Interview_Section.md"),
            [
                "# Traditional ML Interview Section",
                "## Purpose",
                "## Anonymized Role Alignment",
                "## Skill Matrix and 1-5 Scoring Rubric",
                "## Sample Questions (Fundamentals + Applied Reasoning)",
                "## Hands-On Notebook Plan (Interview Exercise)",
                "## Evaluation Criteria (Anti-Recipe Checks)",
                "## Traceability Notes",
            ],
        ),
        (
            Path("Interview/Generative/Generative_AI_Implementation_Section.md"),
            [
                "# Generative AI Implementation Section",
                "## Purpose",
                "## Anonymized Role Alignment",
                "## Skill Matrix and 1-5 Scoring Rubric",
                "## Sample Questions (Implementation + Reasoning)",
                "## Hands-On Notebook Plan (Interview Exercise)",
                "## Evaluation Criteria (Anti-Recipe Checks)",
                "## Traceability Notes",
            ],
        ),
    ],
)
def test_interview_doc_headings_exist(doc_path: Path, required_headings: list[str]) -> None:
    """Ensure interview docs exist and contain required headings."""
    assert doc_path.exists(), f"Missing interview doc: {doc_path}"
    content = doc_path.read_text(encoding="utf-8")
    for heading in required_headings:
        assert heading in content, f"Missing heading '{heading}' in {doc_path}"
