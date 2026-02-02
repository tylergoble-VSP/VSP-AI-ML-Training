"""
Unit tests for src/llm/telemetry.py
"""

# stdlib json (JSON parsing)
import json
# stdlib pathlib (filesystem paths)
from pathlib import Path

# src/llm/generation.py
from src.llm.generation import GenerationResult  # src/llm/generation.py
# src/llm/telemetry.py
from src.llm.telemetry import (  # src/llm/telemetry.py
    TimingContext,
    build_token_usage_record,
    log_token_usage,
)


def test_log_token_usage_writes_jsonl(tmp_path: Path) -> None:
    """It writes a token usage record as JSONL."""
    log_path = tmp_path / "llm_tokens.jsonl"
    generation_result = GenerationResult(
        prompt="hello",
        output_text="hello world",
        prompt_tokens=2,
        completion_tokens=3,
        total_tokens=5,
        latency_ms=10.0,
    )

    record = build_token_usage_record(
        generation_result=generation_result,
        run_id="test_run",
        model_id="test_model",
        task_name="summarization",
        input_ref="inputs/sample.txt",
        output_ref="outputs/sample.txt",
    )
    log_token_usage(log_path, record)

    lines = log_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["total_tokens"] == 5
    assert payload["task_name"] == "summarization"


def test_timing_context_writes_record(tmp_path: Path) -> None:
    """It writes a timing record on exit."""
    log_path = tmp_path / "llm_timing.jsonl"
    with TimingContext(
        log_path=log_path,
        run_id="test_run",
        model_id="test_model",
        step_name="model_load",
        device="cpu",
        torch_dtype="float32",
        batch_size=1,
        sequence_length=4,
    ):
        _ = sum([1, 2, 3])

    payload = json.loads(log_path.read_text(encoding="utf-8").strip())
    assert payload["step_name"] == "model_load"
    assert payload["device"] == "cpu"
