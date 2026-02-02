"""
Telemetry utilities for token accounting and timing logs.
"""

# stdlib json (JSONL serialization)
import json
# stdlib time (timing measurements)
import time
# stdlib dataclasses (structured records)
from dataclasses import asdict, dataclass
# stdlib datetime (UTC timestamps)
from datetime import datetime, timezone
# stdlib pathlib (filesystem paths)
from pathlib import Path
# stdlib typing (type hints)
from typing import Any, Dict, Optional

# src/llm/generation.py
from .generation import GenerationResult  # src/llm/generation.py


@dataclass(frozen=True)
class TokenUsageRecord:
    """Token accounting record for a single generation request."""

    timestamp_utc: str
    run_id: str
    model_id: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    task_name: str
    latency_ms: float
    input_ref: str
    output_ref: str


@dataclass(frozen=True)
class TimingRecord:
    """Timing record for a single step."""

    timestamp_utc: str
    run_id: str
    model_id: str
    step_name: str
    duration_ms: float
    device: str
    torch_dtype: str
    batch_size: Optional[int]
    sequence_length: Optional[int]


def utc_timestamp() -> str:
    """Return a UTC timestamp string suitable for logs."""
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")


def _append_jsonl(log_path: Path, record: Dict[str, Any]) -> None:
    """Append a JSON record to a JSONL file."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(record) + "\n")


def build_token_usage_record(
    generation_result: GenerationResult,
    run_id: str,
    model_id: str,
    task_name: str,
    input_ref: str,
    output_ref: str,
) -> TokenUsageRecord:
    """Build a token usage record from a generation result."""
    return TokenUsageRecord(
        timestamp_utc=utc_timestamp(),
        run_id=run_id,
        model_id=model_id,
        prompt_tokens=generation_result.prompt_tokens,
        completion_tokens=generation_result.completion_tokens,
        total_tokens=generation_result.total_tokens,
        task_name=task_name,
        latency_ms=generation_result.latency_ms,
        input_ref=input_ref,
        output_ref=output_ref,
    )


def log_token_usage(log_path: Path, record: TokenUsageRecord) -> None:
    """Persist a token usage record to a JSONL log."""
    _append_jsonl(log_path, asdict(record))


class TimingContext:
    """Context manager for timing a step and writing a JSONL record."""

    def __init__(
        self,
        log_path: Path,
        run_id: str,
        model_id: str,
        step_name: str,
        device: str,
        torch_dtype: str,
        batch_size: Optional[int] = None,
        sequence_length: Optional[int] = None,
    ) -> None:
        self._log_path = log_path
        self._run_id = run_id
        self._model_id = model_id
        self._step_name = step_name
        self._device = device
        self._torch_dtype = torch_dtype
        self._batch_size = batch_size
        self._sequence_length = sequence_length
        self._start_time: Optional[float] = None

    def __enter__(self) -> "TimingContext":
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        if self._start_time is None:
            return
        duration_ms = (time.perf_counter() - self._start_time) * 1000
        record = TimingRecord(
            timestamp_utc=utc_timestamp(),
            run_id=self._run_id,
            model_id=self._model_id,
            step_name=self._step_name,
            duration_ms=duration_ms,
            device=self._device,
            torch_dtype=self._torch_dtype,
            batch_size=self._batch_size,
            sequence_length=self._sequence_length,
        )
        _append_jsonl(self._log_path, asdict(record))


__all__ = [
    "TimingContext",
    "TimingRecord",
    "TokenUsageRecord",
    "build_token_usage_record",
    "log_token_usage",
    "utc_timestamp",
]
