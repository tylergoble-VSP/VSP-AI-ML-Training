"""
Used in: 04_GenerativeAI_LoRA_PEFT_FineTuning.ipynb
Purpose:
    Provide utilities for working with LoRA (Low-Rank Adaptation) and PEFT
    (Parameter-Efficient Fine-Tuning) for fine-tuning large language models.
    
Educational Context:
    LoRA enables efficient fine-tuning of large models.
    
    Key Concepts:
    1. Full Fine-Tuning Problem:
       - Update all model parameters (billions)
       - Requires huge memory and compute
       - Slow and expensive
    
    2. LoRA Solution:
       - Freeze original model weights
       - Add small "adapter" matrices
       - Only train adapters (much smaller)
       - Combine adapters with base model at inference
    
    3. How LoRA Works:
       - Original: W (large matrix)
       - LoRA: W + BA (B and A are small matrices)
       - Rank r << original dimension
       - Example: 7B model → train only 8M parameters
    
    Why LoRA?
    - 10-100x fewer parameters to train
    - Much faster training
    - Lower memory requirements
    - Can fine-tune on single GPU
    - Multiple LoRAs for different tasks
"""

# Import type hints
from typing import Optional, Dict, Any, List

# Import PyTorch: For tensor operations
import torch


def setup_lora_model(
    model: Any,
    r: int = 8,
    lora_alpha: int = 32,
    target_modules: Optional[List[str]] = None,
    lora_dropout: float = 0.05,
    bias: str = "none"
) -> Any:
    """
    Configure and apply LoRA adapters to a model using PEFT.

    Args:
        model: Base model to apply LoRA to.
        r: LoRA rank (dimension of low-rank matrices).
        lora_alpha: Scaling factor for LoRA weights.
        target_modules: List of module names to apply LoRA to (e.g., ["q_proj", "v_proj"]).
        lora_dropout: Dropout probability for LoRA layers.
        bias: Bias handling ("none", "all", "lora_only").

    Returns:
        Model with LoRA adapters applied.
    """
    try:
        from peft import LoraConfig, get_peft_model
    except ImportError:
        raise ImportError(
            "peft is not installed. Install it with: pip install peft"
        )

    # Default target modules for common transformer architectures
    if target_modules is None:
        # Common attention projection names
        target_modules = ["q_proj", "v_proj"]

    # Create LoRA configuration
    lora_config = LoraConfig(
        r=r,
        lora_alpha=lora_alpha,
        target_modules=target_modules,
        lora_dropout=lora_dropout,
        bias=bias,
        task_type="CAUSAL_LM"  # For causal language modeling
    )

    # Apply LoRA to the model
    model = get_peft_model(model, lora_config)

    return model


def prepare_model_for_training(
    model: Any,
    use_int8: bool = False
) -> Any:
    """
    Prepare a model for training with 8-bit quantization if needed.

    Args:
        model: Model to prepare.
        use_int8: Whether to use 8-bit quantization (requires bitsandbytes).

    Returns:
        Prepared model ready for training.
    """
    if use_int8:
        try:
            from peft import prepare_model_for_int8_training
            model = prepare_model_for_int8_training(model)
        except ImportError:
            raise ImportError(
                "bitsandbytes is required for int8 training. Install with: pip install bitsandbytes"
            )

    # Enable gradient checkpointing if available to save memory
    if hasattr(model, "gradient_checkpointing_enable"):
        model.gradient_checkpointing_enable()

    return model


def merge_lora_weights(
    model: Any,
    save_path: Optional[str] = None
) -> Any:
    """
    Merge LoRA adapter weights into the base model.

    Args:
        model: Model with LoRA adapters.
        save_path: Optional path to save merged model.

    Returns:
        Merged model (base model with LoRA weights incorporated).
    """
    try:
        # Merge and unload LoRA weights
        merged_model = model.merge_and_unload()

        # Save if path provided
        if save_path:
            merged_model.save_pretrained(save_path)

        return merged_model
    except Exception as e:
        raise RuntimeError(f"Failed to merge LoRA weights: {str(e)}")


def save_load_lora(
    model: Any,
    save_path: str,
    load: bool = False
) -> Optional[Any]:
    """
    Save or load LoRA adapter weights.

    Args:
        model: Model with LoRA adapters (for saving) or base model (for loading).
        save_path: Path to save/load LoRA weights.
        load: If True, load weights; if False, save weights.

    Returns:
        If loading: model with loaded LoRA adapters.
        If saving: None.
    """
    try:
        from peft import PeftModel

        if load:
            # Load LoRA weights onto base model
            model = PeftModel.from_pretrained(model, save_path)
            return model
        else:
            # Save LoRA adapter weights
            model.save_pretrained(save_path)
            return None
    except Exception as e:
        raise RuntimeError(f"Failed to save/load LoRA weights: {str(e)}")


def get_lora_model_info(model: Any) -> Dict[str, Any]:
    """
    Get information about LoRA configuration and trainable parameters.

    Args:
        model: Model with LoRA adapters.

    Returns:
        Dictionary containing LoRA model information.
    """
    info = {
        "trainable_parameters": 0,
        "total_parameters": 0,
        "trainable_percentage": 0.0
    }

    # Count parameters
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())

    info["trainable_parameters"] = trainable_params
    info["total_parameters"] = total_params

    if total_params > 0:
        info["trainable_percentage"] = (trainable_params / total_params) * 100

    # Try to get LoRA config if available
    if hasattr(model, "peft_config"):
        info["lora_configs"] = str(model.peft_config)

    return info

