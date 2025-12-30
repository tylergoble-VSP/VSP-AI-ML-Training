"""
Used in: 03_GenerativeAI_Ollama_Model_Serving.ipynb
Purpose:
    Provide utilities for working with Ollama Python client,
    including model management, chat interactions, and streaming responses.
"""

from typing import Optional, Dict, List, Any, Iterator
import os  # For environment variables


def setup_ollama_client(
    base_url: Optional[str] = None,
    timeout: int = 120
) -> Any:
    """
    Initialize and configure Ollama client connection.

    Args:
        base_url: Base URL for Ollama server (default: http://localhost:11434).
        timeout: Request timeout in seconds.

    Returns:
        Configured Ollama client object.
    """
    try:
        import ollama
    except ImportError:
        raise ImportError(
            "ollama is not installed. Install it with: pip install ollama"
        )

    # Use default URL if not specified
    if base_url is None:
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    # Create client (ollama library uses a global client by default)
    # We'll return a wrapper that uses the ollama module functions
    client = {
        "base_url": base_url,
        "timeout": timeout
    }

    return client


def ollama_chat(
    model: str,
    messages: List[Dict[str, str]],
    stream: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """
    Send a chat request to Ollama and get response.

    Args:
        model: Name of the Ollama model to use.
        messages: List of message dicts with 'role' and 'content' keys.
        stream: Whether to stream the response.
        **kwargs: Additional parameters (temperature, top_p, etc.).

    Returns:
        Dictionary containing the response from Ollama.
    """
    import ollama

    try:
        # Call Ollama chat API
        response = ollama.chat(
            model=model,
            messages=messages,
            stream=stream,
            **kwargs
        )

        return response
    except Exception as e:
        raise RuntimeError(f"Ollama chat request failed: {str(e)}")


def stream_ollama_response(
    model: str,
    messages: List[Dict[str, str]],
    **kwargs
) -> Iterator[str]:
    """
    Stream responses from Ollama token by token.

    Args:
        model: Name of the Ollama model to use.
        messages: List of message dicts with 'role' and 'content' keys.
        **kwargs: Additional parameters.

    Yields:
        String chunks of the generated response.
    """
    import ollama

    try:
        # Stream the response
        stream = ollama.chat(
            model=model,
            messages=messages,
            stream=True,
            **kwargs
        )

        # Yield each chunk as it arrives
        for chunk in stream:
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content
    except Exception as e:
        raise RuntimeError(f"Ollama streaming failed: {str(e)}")


def list_ollama_models() -> List[Dict[str, Any]]:
    """
    List all available Ollama models.

    Returns:
        List of dictionaries containing model information.
    """
    import ollama

    try:
        # Get list of models
        models_list = ollama.list()

        # Extract model information
        models_info = []
        if hasattr(models_list, "models"):
            for model in models_list.models:
                models_info.append({
                    "name": getattr(model, "name", "unknown"),
                    "size": getattr(model, "size", 0),
                    "modified_at": getattr(model, "modified_at", None)
                })
        else:
            # Handle different response formats
            models_info = models_list if isinstance(models_list, list) else []

        return models_info
    except Exception as e:
        raise RuntimeError(f"Failed to list Ollama models: {str(e)}")


def get_ollama_model_info(model_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific Ollama model.

    Args:
        model_name: Name of the model.

    Returns:
        Dictionary containing model details.
    """
    import ollama

    try:
        # Get model information
        model_info = ollama.show(model_name)

        # Extract key information
        info = {
            "name": model_name,
            "details": model_info if model_info else {}
        }

        return info
    except Exception as e:
        raise RuntimeError(f"Failed to get model info for {model_name}: {str(e)}")


def pull_ollama_model(model_name: str) -> Dict[str, Any]:
    """
    Pull/download an Ollama model from the registry.

    Args:
        model_name: Name of the model to pull.

    Returns:
        Dictionary containing pull status.
    """
    import ollama

    try:
        # Pull the model
        result = ollama.pull(model_name)

        return {
            "status": "success",
            "model": model_name,
            "details": result if result else {}
        }
    except Exception as e:
        return {
            "status": "error",
            "model": model_name,
            "error": str(e)
        }

