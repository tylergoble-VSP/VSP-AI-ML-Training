"""
Used in: 02_GenerativeAI_LlamaCPP_Local_Models.ipynb
Purpose:
    Provide utilities for working with llama.cpp Python bindings,
    including model loading, text generation, and performance benchmarking.
"""

from typing import Optional, Dict, Any, List
import time  # For timing operations


def load_llama_model(
    model_path: str,
    n_threads: Optional[int] = None,
    n_ctx: int = 2048,
    n_gpu_layers: int = 0
) -> Any:
    """
    Load a llama.cpp model from a file path.

    Args:
        model_path: Path to the GGML/GGUF model file.
        n_threads: Number of threads to use (None = auto-detect).
        n_ctx: Context window size in tokens.
        n_gpu_layers: Number of layers to offload to GPU (0 = CPU only).

    Returns:
        Loaded Llama model object.
    """
    try:
        from llama_cpp import Llama
    except ImportError:
        raise ImportError(
            "llama-cpp-python is not installed. Install it with: pip install llama-cpp-python"
        )

    # Auto-detect thread count if not specified
    if n_threads is None:
        import os
        n_threads = os.cpu_count() or 4

    # Load the model with specified parameters
    llm = Llama(
        model_path=model_path,
        n_threads=n_threads,
        n_ctx=n_ctx,
        n_gpu_layers=n_gpu_layers,
        verbose=False
    )

    return llm


def generate_with_llama(
    llm: Any,
    prompt: str,
    max_tokens: int = 64,
    temperature: float = 0.7,
    top_p: float = 0.9,
    stop: Optional[List[str]] = None,
    echo: bool = False
) -> Dict[str, Any]:
    """
    Generate text using a loaded llama.cpp model.

    Args:
        llm: Loaded Llama model object.
        prompt: Input text prompt.
        max_tokens: Maximum number of tokens to generate.
        temperature: Sampling temperature (higher = more random).
        top_p: Nucleus sampling parameter.
        stop: List of stop sequences (generation stops when encountered).
        echo: Whether to echo the prompt in the output.

    Returns:
        Dictionary containing generated text and metadata.
    """
    # Call the model with generation parameters
    output = llm(
        prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stop=stop or [],
        echo=echo
    )

    return output


def quantize_model_info(model_path: str) -> Dict[str, Any]:
    """
    Extract quantization information from a model file path.

    Args:
        model_path: Path to the model file.

    Returns:
        Dictionary containing quantization details.
    """
    import os
    from pathlib import Path

    path = Path(model_path)
    filename = path.name.lower()

    # Parse quantization from filename (common patterns)
    quant_info = {
        "model_path": model_path,
        "file_size_mb": os.path.getsize(model_path) / (1024 * 1024) if os.path.exists(model_path) else None,
        "quantization": "unknown",
        "format": "unknown"
    }

    # Detect format
    if filename.endswith(".gguf"):
        quant_info["format"] = "GGUF"
    elif filename.endswith(".ggml") or any(filename.endswith(f".ggml{q}") for q in ["q4_0", "q4_1", "q5_0", "q5_1", "q8_0"]):
        quant_info["format"] = "GGML"

    # Detect quantization level from filename
    if "q4_0" in filename or "q4_0.bin" in filename:
        quant_info["quantization"] = "4-bit (Q4_0)"
    elif "q4_1" in filename:
        quant_info["quantization"] = "4-bit (Q4_1)"
    elif "q5_0" in filename:
        quant_info["quantization"] = "5-bit (Q5_0)"
    elif "q5_1" in filename:
        quant_info["quantization"] = "5-bit (Q5_1)"
    elif "q8_0" in filename:
        quant_info["quantization"] = "8-bit (Q8_0)"
    elif "f16" in filename or "fp16" in filename:
        quant_info["quantization"] = "16-bit float"
    elif "f32" in filename or "fp32" in filename:
        quant_info["quantization"] = "32-bit float"
    else:
        quant_info["quantization"] = "unknown (possibly unquantized)"

    return quant_info


def benchmark_llama_inference(
    llm: Any,
    prompts: List[str],
    max_tokens: int = 50,
    num_runs: int = 3
) -> Dict[str, Any]:
    """
    Benchmark llama.cpp inference performance.

    Args:
        llm: Loaded Llama model object.
        prompts: List of test prompts.
        max_tokens: Maximum tokens to generate per prompt.
        num_runs: Number of runs to average over.

    Returns:
        Dictionary containing performance metrics.
    """
    times = []
    tokens_per_second = []

    for prompt in prompts:
        for _ in range(num_runs):
            start_time = time.time()

            # Generate text
            output = generate_with_llama(llm, prompt, max_tokens=max_tokens)

            elapsed = time.time() - start_time

            # Calculate tokens per second
            # Estimate: count tokens in generated text (rough approximation)
            generated_text = output.get("choices", [{}])[0].get("text", "")
            # Rough token estimate: ~4 characters per token
            estimated_tokens = len(generated_text) / 4
            if elapsed > 0:
                tps = estimated_tokens / elapsed
            else:
                tps = 0

            times.append(elapsed)
            tokens_per_second.append(tps)

    # Calculate statistics
    avg_time = sum(times) / len(times) if times else 0
    avg_tps = sum(tokens_per_second) / len(tokens_per_second) if tokens_per_second else 0
    min_time = min(times) if times else 0
    max_time = max(times) if times else 0

    return {
        "average_time_seconds": avg_time,
        "min_time_seconds": min_time,
        "max_time_seconds": max_time,
        "average_tokens_per_second": avg_tps,
        "total_runs": len(times)
    }

