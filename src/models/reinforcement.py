"""
Used in: 31_Reinforcement_QLearning.ipynb, 32_Reinforcement_Policy_Gradient.ipynb
Purpose:
    Provide reinforcement learning utilities including Q-table management,
    policy evaluation, and reward tracking.
    
Educational Context:
    Reinforcement Learning (RL) learns by trial and error through interaction.
    
    Key Concepts:
    1. Agent: The learner (makes decisions)
    2. Environment: The world the agent interacts with
    3. State: Current situation
    4. Action: What the agent does
    5. Reward: Feedback (positive/negative)
    6. Policy: Strategy for choosing actions
    
    Q-Learning:
    - Learns Q-values: Expected future reward for state-action pairs
    - Q-table: Stores Q-values for all state-action combinations
    - Explores (tries new actions) and exploits (uses learned knowledge)
    
    Policy Gradient:
    - Learns policy directly (probability distribution over actions)
    - Uses gradient ascent to maximize expected reward
    - Better for continuous action spaces
"""

# Import NumPy: For numerical operations
import numpy as np

# Import Pandas: For DataFrame operations
import pandas as pd

# Import type hints
from typing import Dict, Tuple, List, Optional, Callable

# Import defaultdict: Dictionary that creates default values for missing keys
# Useful for Q-tables (automatically creates entries for new states)
from collections import defaultdict


class QTable:
    """
    Q-table for Q-Learning algorithm.
    Stores Q-values for state-action pairs.
    """
    
    def __init__(self, default_value: float = 0.0):
        """
        Initialize Q-table with default Q-values.

        Args:
            default_value: Default Q-value for unseen state-action pairs.
        """
        # Use defaultdict to automatically create entries for new states
        self.q_table = defaultdict(lambda: defaultdict(lambda: default_value))
        self.default_value = default_value
    
    def get(self, state: Tuple, action: int) -> float:
        """
        Get Q-value for a state-action pair.

        Args:
            state: Current state (tuple or hashable).
            action: Action index.

        Returns:
            Q-value for the state-action pair.
        """
        return self.q_table[state][action]
    
    def set(self, state: Tuple, action: int, value: float) -> None:
        """
        Set Q-value for a state-action pair.

        Args:
            state: Current state (tuple or hashable).
            action: Action index.
            value: Q-value to set.
        """
        self.q_table[state][action] = value
    
    def update(self, state: Tuple, action: int, new_value: float) -> None:
        """
        Update Q-value (same as set, but more explicit for Q-learning updates).

        Args:
            state: Current state (tuple or hashable).
            action: Action index.
            new_value: New Q-value.
        """
        self.set(state, action, new_value)
    
    def get_best_action(self, state: Tuple, actions: List[int]) -> int:
        """
        Get the action with the highest Q-value for a given state.

        Args:
            state: Current state (tuple or hashable).
            actions: List of available actions.

        Returns:
            Action index with highest Q-value.
        """
        q_values = [self.get(state, action) for action in actions]
        best_action_idx = np.argmax(q_values)
        return actions[best_action_idx]
    
    def get_max_q_value(self, state: Tuple, actions: List[int]) -> float:
        """
        Get the maximum Q-value for a given state.

        Args:
            state: Current state (tuple or hashable).
            actions: List of available actions.

        Returns:
            Maximum Q-value.
        """
        q_values = [self.get(state, action) for action in actions]
        return max(q_values) if q_values else self.default_value
    
    def to_dict(self) -> Dict:
        """
        Convert Q-table to dictionary for serialization.

        Returns:
            Dictionary representation of Q-table.
        """
        # Convert nested defaultdicts to regular dicts
        return {str(k): dict(v) for k, v in self.q_table.items()}


class RewardTracker:
    """
    Track rewards and episode statistics for reinforcement learning.
    """
    
    def __init__(self):
        """Initialize reward tracker."""
        self.episode_rewards = []  # List of total rewards per episode
        self.episode_lengths = []  # List of episode lengths
        self.all_rewards = []  # All individual rewards
    
    def record_episode(self, total_reward: float, episode_length: int) -> None:
        """
        Record statistics for a completed episode.

        Args:
            total_reward: Total reward accumulated in the episode.
            episode_length: Number of steps in the episode.
        """
        self.episode_rewards.append(total_reward)
        self.episode_lengths.append(episode_length)
    
    def record_reward(self, reward: float) -> None:
        """
        Record an individual reward.

        Args:
            reward: Reward value.
        """
        self.all_rewards.append(reward)
    
    def get_statistics(self) -> Dict[str, float]:
        """
        Get summary statistics for all episodes.

        Returns:
            Dictionary with mean, std, min, max for rewards and lengths.
        """
        if not self.episode_rewards:
            return {}
        
        return {
            "mean_reward": np.mean(self.episode_rewards),
            "std_reward": np.std(self.episode_rewards),
            "min_reward": np.min(self.episode_rewards),
            "max_reward": np.max(self.episode_rewards),
            "mean_episode_length": np.mean(self.episode_lengths),
            "std_episode_length": np.std(self.episode_lengths),
            "total_episodes": len(self.episode_rewards)
        }
    
    def plot_rewards(self, window: int = 100, title: str = "Episode Rewards") -> None:
        """
        Plot episode rewards over time with moving average.

        Args:
            window: Window size for moving average.
            title: Plot title.
        """
        import matplotlib.pyplot as plt
        
        if not self.episode_rewards:
            print("No rewards to plot")
            return
        
        episodes = np.arange(1, len(self.episode_rewards) + 1)
        
        plt.figure(figsize=(12, 6))
        plt.plot(episodes, self.episode_rewards, alpha=0.3, label='Raw Rewards')
        
        # Calculate moving average
        if len(self.episode_rewards) >= window:
            moving_avg = pd.Series(self.episode_rewards).rolling(window=window).mean()
            plt.plot(episodes, moving_avg, label=f'Moving Average (window={window})', linewidth=2)
        
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()


def epsilon_greedy_policy(q_table: QTable, state: Tuple, actions: List[int], 
                          epsilon: float) -> int:
    """
    Epsilon-greedy policy: choose random action with probability epsilon,
    otherwise choose best action.

    Args:
        q_table: Q-table with Q-values.
        state: Current state.
        actions: List of available actions.
        epsilon: Exploration probability (0 to 1).

    Returns:
        Selected action index.
    """
    # Random action with probability epsilon
    if np.random.random() < epsilon:
        return np.random.choice(actions)
    else:
        # Greedy action (best Q-value)
        return q_table.get_best_action(state, actions)


def evaluate_policy(q_table: QTable, env: Any, n_episodes: int = 100) -> Dict[str, float]:
    """
    Evaluate a policy by running episodes and collecting statistics.

    Args:
        q_table: Q-table representing the policy.
        env: Environment object with reset() and step() methods.
        n_episodes: Number of episodes to run.

    Returns:
        Dictionary with evaluation statistics.
    """
    total_rewards = []
    episode_lengths = []
    
    for _ in range(n_episodes):
        state = env.reset()
        total_reward = 0
        steps = 0
        done = False
        
        while not done:
            # Get best action from Q-table
            actions = list(range(env.action_space.n)) if hasattr(env, 'action_space') else [0, 1]
            action = q_table.get_best_action(tuple(state) if isinstance(state, np.ndarray) else state, actions)
            
            # Take action
            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            steps += 1
            state = next_state
        
        total_rewards.append(total_reward)
        episode_lengths.append(steps)
    
    return {
        "mean_reward": np.mean(total_rewards),
        "std_reward": np.std(total_rewards),
        "mean_episode_length": np.mean(episode_lengths),
        "n_episodes": n_episodes
    }

