"""
Used in: 01_GenerativeAI_HuggingFace_Transformers.ipynb
Purpose:
    Provide utilities for working with Hugging Face Transformers library,
    including model loading, text generation, classification, and model information extraction.
    
Educational Context:
    Hugging Face Transformers provides pre-trained language models.
    
    Key Concepts:
    1. Tokenization: Convert text to numbers (tokens)
       - Models work with token IDs, not raw text
       - Tokenizer handles special characters, subwords
    
    2. Model Types:
       - Causal LM: Generates text (GPT-style)
       - Sequence Classification: Classifies text (sentiment, etc.)
       - Auto classes: Automatically select correct architecture
    
    3. Generation Parameters:
       - Temperature: Controls randomness (higher = more creative)
       - Top-p: Nucleus sampling (diversity control)
       - Max tokens: Length limit
    
    Why Hugging Face?
    - Easy access to thousands of pre-trained models
    - Consistent API across models
    - Handles tokenization automatically
    - Supports many tasks
"""

# Import type hints
from typing import Optional, Dict, List, Union, Any

# Import PyTorch: Deep learning framework
import torch  # Tensor operations, device management

# Import Hugging Face Transformers
# AutoTokenizer: Automatically loads correct tokenizer for model
# AutoModelForCausalLM: Language models for text generation (GPT-style)
# AutoModelForSequenceClassification: Models for classification tasks
# pipeline: High-level API for common NLP tasks
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    pipeline,
    Pipeline
)


def load_transformers_model(
    model_name: str,
    task: str = "text-generation",
    device: Optional[str] = None,
    torch_dtype: Optional[torch.dtype] = None
) -> tuple:
    """
    Load a Hugging Face model and tokenizer for a specific task.

    Args:
        model_name: Name of the model from Hugging Face Hub (e.g., "gpt2", "distilgpt2").
        task: Task type ("text-generation", "classification", etc.).
        device: Device to load model on ("cuda", "cpu", or None for auto).
        torch_dtype: Data type for model weights (e.g., torch.float16).

    Returns:
        Tuple of (model, tokenizer) or (pipeline, None) if using pipeline API.
    """
    # Auto-detect device if not specified
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load tokenizer (always needed for text processing)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Handle padding token if not present
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Load model based on task
    if task == "text-generation":
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch_dtype or torch.float32
        )
    elif task == "classification":
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            torch_dtype=torch_dtype or torch.float32
        )
    else:
        # For other tasks, use pipeline API
        pipeline_obj = pipeline(task, model=model_name, device=device)
        return pipeline_obj, None

    # Move model to specified device
    model = model.to(device)
    model.eval()  # Set to evaluation mode

    return model, tokenizer


def generate_text(
    model: Any,
    tokenizer: Any,
    prompt: str,
    max_new_tokens: int = 50,
    temperature: float = 1.0,
    top_p: float = 0.9,
    do_sample: bool = True,
    num_return_sequences: int = 1
) -> List[str]:
    """
    Generate text using a loaded model and tokenizer.

    Args:
        model: Loaded transformer model.
        tokenizer: Loaded tokenizer.
        prompt: Input text prompt.
        max_new_tokens: Maximum number of new tokens to generate.
        temperature: Sampling temperature (higher = more random).
        top_p: Nucleus sampling parameter.
        do_sample: Whether to use sampling (True) or greedy decoding (False).
        num_return_sequences: Number of different sequences to generate.

    Returns:
        List of generated text strings.
    """
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt")

    # Move inputs to same device as model
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Generate with specified parameters
    with torch.no_grad():  # Disable gradient computation for inference
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=do_sample,
            num_return_sequences=num_return_sequences,
            pad_token_id=tokenizer.pad_token_id
        )

    # Decode generated tokens to text
    generated_texts = []
    for output in outputs:
        # Decode only the new tokens (skip the input prompt)
        generated = tokenizer.decode(output[inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        generated_texts.append(generated)

    return generated_texts


def classify_text(
    model: Any,
    tokenizer: Any,
    text: str,
    return_probs: bool = True
) -> Union[str, Dict[str, Any]]:
    """
    Classify text using a loaded classification model.

    Args:
        model: Loaded classification model.
        tokenizer: Loaded tokenizer.
        text: Text to classify.
        return_probs: Whether to return probability scores.

    Returns:
        If return_probs=False: predicted label string.
        If return_probs=True: dict with 'label' and 'score' keys.
    """
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

    # Move inputs to same device as model
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Apply softmax to get probabilities
    probs = torch.nn.functional.softmax(logits, dim=-1)

    # Get predicted class (highest probability)
    predicted_id = torch.argmax(probs, dim=-1).item()
    predicted_score = probs[0][predicted_id].item()

    # Get label name if model has id2label mapping
    if hasattr(model.config, "id2label") and model.config.id2label:
        predicted_label = model.config.id2label[predicted_id]
    else:
        predicted_label = str(predicted_id)

    if return_probs:
        return {
            "label": predicted_label,
            "score": predicted_score,
            "all_probs": probs[0].cpu().numpy().tolist()
        }
    else:
        return predicted_label


def get_model_info(model_name: str) -> Dict[str, Any]:
    """
    Extract metadata and information about a Hugging Face model.

    Args:
        model_name: Name of the model from Hugging Face Hub.

    Returns:
        Dictionary containing model information (config, tokenizer info, etc.).
    """
    from transformers import AutoConfig

    # Load model configuration
    config = AutoConfig.from_pretrained(model_name)

    # Load tokenizer to get vocabulary info
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Extract key information
    info = {
        "model_name": model_name,
        "model_type": getattr(config, "model_type", "unknown"),
        "vocab_size": getattr(config, "vocab_size", len(tokenizer) if tokenizer else None),
        "max_position_embeddings": getattr(config, "max_position_embeddings", None),
        "hidden_size": getattr(config, "hidden_size", None),
        "num_attention_heads": getattr(config, "num_attention_heads", None),
        "num_layers": getattr(config, "num_hidden_layers", None),
        "tokenizer_vocab_size": len(tokenizer) if tokenizer else None,
        "pad_token": tokenizer.pad_token if tokenizer else None,
        "eos_token": tokenizer.eos_token if tokenizer else None,
        "bos_token": tokenizer.bos_token if tokenizer else None,
    }

    return info

