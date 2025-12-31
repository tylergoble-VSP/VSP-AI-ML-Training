"""
Used in: 33_NeuralNetworks_Perceptron_MLP.ipynb, 34_NeuralNetworks_Convolutional_Neural_Networks.ipynb,
         35_NeuralNetworks_Recurrent_Neural_Networks_LSTM.ipynb, 36_NeuralNetworks_Generative_Adversarial_Networks.ipynb,
         37_NeuralNetworks_Transformers.ipynb
Purpose:
    Provide neural network utilities including architecture visualization,
    gradient flow analysis, and activation visualization.
    
Educational Context:
    Neural networks are computing systems inspired by biological brains.
    
    Key Concepts:
    1. Perceptron: Single neuron (simplest neural network)
    2. MLP (Multi-Layer Perceptron): Stack of layers (input → hidden → output)
    3. CNNs: Convolutional layers for images (detect patterns, edges, shapes)
    4. RNNs/LSTMs: Recurrent layers for sequences (text, time series)
    5. GANs: Generative models (generator + discriminator)
    6. Transformers: Attention-based models (BERT, GPT)
    
    How Neural Networks Learn:
    - Forward pass: Data flows through layers
    - Loss calculation: Compare prediction to truth
    - Backpropagation: Calculate gradients
    - Update weights: Adjust to reduce loss
"""

# Import NumPy: For numerical operations
import numpy as np

# Import matplotlib: For plotting visualizations
import matplotlib.pyplot as plt

# Import type hints
from typing import List, Tuple, Optional, Dict, Any

# Try to import PyTorch (optional dependency)
# PyTorch is a deep learning framework for building neural networks
# We use try/except because PyTorch might not be installed
try:
    import torch  # PyTorch tensor library
    import torch.nn as nn  # Neural network modules
    TORCH_AVAILABLE = True  # Flag indicating PyTorch is available
except ImportError:
    # PyTorch not installed - some functions won't work
    TORCH_AVAILABLE = False


def visualize_architecture(model: Any, input_shape: Tuple[int, ...], 
                          title: str = "Model Architecture") -> None:
    """
    Visualize neural network architecture (for PyTorch models).

    Args:
        model: PyTorch model.
        input_shape: Shape of input tensor (excluding batch dimension).
        title: Plot title.
    """
    if not TORCH_AVAILABLE:
        print("PyTorch not available. Cannot visualize architecture.")
        return
    
    if not isinstance(model, nn.Module):
        print("Model is not a PyTorch nn.Module. Cannot visualize.")
        return
    
    # Count parameters in each layer
    layers = []
    param_counts = []
    
    for name, module in model.named_modules():
        if len(list(module.children())) == 0:  # Leaf module
            param_count = sum(p.numel() for p in module.parameters())
            if param_count > 0:
                layers.append(name if name else "root")
                param_counts.append(param_count)
    
    # Create visualization
    if layers:
        plt.figure(figsize=(12, max(6, len(layers) * 0.5)))
        plt.barh(range(len(layers)), param_counts)
        plt.yticks(range(len(layers)), layers)
        plt.xlabel('Number of Parameters')
        plt.title(title)
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
    else:
        print("No layers found to visualize.")


def plot_training_history(history: Dict[str, List[float]], 
                          title: str = "Training History") -> None:
    """
    Plot training and validation loss/accuracy over epochs.

    Args:
        history: Dictionary with keys like 'train_loss', 'val_loss', 'train_acc', 'val_acc'.
        title: Plot title.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot loss
    if 'train_loss' in history:
        axes[0].plot(history['train_loss'], label='Train Loss', marker='o')
    if 'val_loss' in history:
        axes[0].plot(history['val_loss'], label='Validation Loss', marker='s')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Loss Over Time')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot accuracy
    if 'train_acc' in history:
        axes[1].plot(history['train_acc'], label='Train Accuracy', marker='o')
    if 'val_acc' in history:
        axes[1].plot(history['val_acc'], label='Validation Accuracy', marker='s')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Accuracy')
    axes[1].set_title('Accuracy Over Time')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


def analyze_gradient_flow(model: Any) -> Dict[str, float]:
    """
    Analyze gradient flow through a PyTorch model.
    Returns statistics about gradient magnitudes.

    Args:
        model: PyTorch model.

    Returns:
        Dictionary with gradient statistics.
    """
    if not TORCH_AVAILABLE:
        return {"error": "PyTorch not available"}
    
    if not isinstance(model, nn.Module):
        return {"error": "Model is not a PyTorch nn.Module"}
    
    gradient_norms = []
    layer_names = []
    
    for name, param in model.named_parameters():
        if param.grad is not None:
            grad_norm = param.grad.data.norm(2).item()
            gradient_norms.append(grad_norm)
            layer_names.append(name)
    
    if not gradient_norms:
        return {"error": "No gradients found"}
    
    return {
        "mean_gradient_norm": np.mean(gradient_norms),
        "std_gradient_norm": np.std(gradient_norms),
        "min_gradient_norm": np.min(gradient_norms),
        "max_gradient_norm": np.max(gradient_norms),
        "layer_names": layer_names,
        "gradient_norms": gradient_norms
    }


def visualize_activations(activations: Dict[str, np.ndarray], 
                         title: str = "Layer Activations") -> None:
    """
    Visualize activations from different layers of a neural network.

    Args:
        activations: Dictionary mapping layer names to activation arrays.
        title: Plot title.
    """
    n_layers = len(activations)
    if n_layers == 0:
        print("No activations to visualize")
        return
    
    fig, axes = plt.subplots(1, n_layers, figsize=(5 * n_layers, 5))
    if n_layers == 1:
        axes = [axes]
    
    for idx, (layer_name, activation) in enumerate(activations.items()):
        # Flatten activation for histogram
        flat_activation = activation.flatten()
        
        axes[idx].hist(flat_activation, bins=50, alpha=0.7, edgecolor='black')
        axes[idx].set_xlabel('Activation Value')
        axes[idx].set_ylabel('Frequency')
        axes[idx].set_title(f'{layer_name}\nMean: {np.mean(flat_activation):.3f}')
        axes[idx].grid(True, alpha=0.3)
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


def count_parameters(model: Any) -> Dict[str, int]:
    """
    Count total and trainable parameters in a PyTorch model.

    Args:
        model: PyTorch model.

    Returns:
        Dictionary with parameter counts.
    """
    if not TORCH_AVAILABLE:
        return {"error": "PyTorch not available"}
    
    if not isinstance(model, nn.Module):
        return {"error": "Model is not a PyTorch nn.Module"}
    
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    return {
        "total_parameters": total_params,
        "trainable_parameters": trainable_params,
        "non_trainable_parameters": total_params - trainable_params
    }


def plot_feature_maps(feature_maps: np.ndarray, n_maps: int = 16,
                     title: str = "Feature Maps") -> None:
    """
    Visualize feature maps from a convolutional layer.

    Args:
        feature_maps: Array of feature maps (batch, channels, height, width) or (channels, height, width).
        n_maps: Number of feature maps to display.
        title: Plot title.
    """
    # Handle different input shapes
    if feature_maps.ndim == 4:
        # Batch dimension present - take first sample
        feature_maps = feature_maps[0]
    
    n_channels = feature_maps.shape[0]
    n_maps = min(n_maps, n_channels)
    
    # Create grid of subplots
    cols = 4
    rows = (n_maps + cols - 1) // cols
    
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 2, rows * 2))
    if rows == 1:
        axes = axes.reshape(1, -1)
    
    for idx in range(n_maps):
        row = idx // cols
        col = idx % cols
        ax = axes[row, col]
        
        # Display feature map
        im = ax.imshow(feature_maps[idx], cmap='viridis')
        ax.set_title(f'Map {idx}')
        ax.axis('off')
        plt.colorbar(im, ax=ax)
    
    # Hide unused subplots
    for idx in range(n_maps, rows * cols):
        row = idx // cols
        col = idx % cols
        axes[row, col].axis('off')
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

