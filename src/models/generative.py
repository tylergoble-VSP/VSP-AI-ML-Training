"""
Used in: 11_Generative_Models
Purpose:
    Provide utilities for generative models including VAE and GAN implementations.
    Uses PyTorch for neural network construction.
    
Educational Context:
    Generative models create new data similar to training data.
    
    Key Concepts:
    1. VAE (Variational Autoencoder):
       - Encodes data to latent space (compressed representation)
       - Decodes latent code back to data
       - Learns smooth latent space (can generate new samples)
       - Uses variational inference (probabilistic approach)
    
    2. GAN (Generative Adversarial Network):
       - Generator: Creates fake data
       - Discriminator: Distinguishes real from fake
       - They compete (adversarial training)
       - Generator improves by fooling discriminator
    
    Why generative models?
    - Create new images, text, music
    - Data augmentation (generate more training data)
    - Understand data distribution
    - Anomaly detection
"""

# Import PyTorch: Deep learning framework
import torch  # Core PyTorch library (tensors, operations)

# Import neural network modules
import torch.nn as nn  # Layers, activation functions, loss functions

# Import optimizers: Algorithms for updating model weights
import torch.optim as optim  # SGD, Adam, etc.

# Import DataLoader: Efficient data loading and batching
from torch.utils.data import DataLoader

# Import type hints
from typing import Tuple


class SimpleVAE(nn.Module):
    """
    Simple Variational Autoencoder for MNIST-like data.
    
    Encodes input to latent space, then decodes back to original space.
    """
    def __init__(self, input_dim: int = 784, latent_dim: int = 20, hidden_dim: int = 400):
        """
        Initialize the VAE.

        Args:
            input_dim: Size of input (e.g., 28*28 for MNIST).
            latent_dim: Size of latent representation.
            hidden_dim: Size of hidden layers.
        """
        super(SimpleVAE, self).__init__()

        # Encoder layers: input -> hidden -> latent (mean and log variance)
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )

        # Mean and log variance of latent distribution
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        # Decoder layers: latent -> hidden -> output
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim),
            nn.Sigmoid()  # Output between 0 and 1
        )

    def encode(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Encode input to latent space parameters."""
        h = self.encoder(x)
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)
        return mu, logvar

    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        """Reparameterization trick for VAE."""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """Decode latent vector to output."""
        return self.decoder(z)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Forward pass through the VAE."""
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon = self.decode(z)
        return recon, mu, logvar


class SimpleGenerator(nn.Module):
    """
    Simple Generator for GAN (takes noise, outputs image).
    """
    def __init__(self, noise_dim: int = 100, output_dim: int = 784, hidden_dim: int = 256):
        """
        Initialize the Generator.

        Args:
            noise_dim: Size of input noise vector.
            output_dim: Size of output (e.g., 28*28 for MNIST).
            hidden_dim: Size of hidden layers.
        """
        super(SimpleGenerator, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(noise_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim * 2),
            nn.ReLU(),
            nn.Linear(hidden_dim * 2, output_dim),
            nn.Tanh()  # Output between -1 and 1
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        """Generate image from noise."""
        return self.model(z)


class SimpleDiscriminator(nn.Module):
    """
    Simple Discriminator for GAN (takes image, outputs real/fake probability).
    """
    def __init__(self, input_dim: int = 784, hidden_dim: int = 256):
        """
        Initialize the Discriminator.

        Args:
            input_dim: Size of input (e.g., 28*28 for MNIST).
            hidden_dim: Size of hidden layers.
        """
        super(SimpleDiscriminator, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_dim * 2),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()  # Output probability
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Classify image as real or fake."""
        return self.model(x)


def vae_loss(recon_x: torch.Tensor, x: torch.Tensor, mu: torch.Tensor, 
             logvar: torch.Tensor, beta: float = 1.0) -> torch.Tensor:
    """
    Compute VAE loss (reconstruction + KL divergence).

    Args:
        recon_x: Reconstructed input.
        x: Original input.
        mu: Mean of latent distribution.
        logvar: Log variance of latent distribution.
        beta: Weight for KL term.

    Returns:
        Total VAE loss.
    """
    # Reconstruction loss (binary cross-entropy)
    recon_loss = nn.functional.binary_cross_entropy(recon_x, x, reduction='sum')

    # KL divergence loss
    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    # Total loss
    total_loss = recon_loss + beta * kl_loss

    return total_loss

