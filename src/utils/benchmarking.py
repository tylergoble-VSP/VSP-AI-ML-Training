"""
Used in: All algorithm notebooks for performance benchmarking
Purpose:
    Provide performance benchmarking utilities including timing,
    memory profiling, and scalability analysis.
"""

import time  # For timing operations
import numpy as np  # NumPy for numerical operations
import pandas as pd  # Pandas for DataFrame operations
from typing import Dict, List, Any, Callable, Optional  # Type hints
from src.utils.paths import timestamped_path  # For timestamped output files
from src.utils.timing import TimeBlock  # For timing blocks
import sys  # For memory profiling


def benchmark_function(func: Callable, *args, n_runs: int = 5, **kwargs) -> Dict[str, float]:
    """
    Benchmark a function by running it multiple times and collecting statistics.

    Args:
        func: Function to benchmark.
        *args: Positional arguments for the function.
        n_runs: Number of times to run the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        Dictionary with timing statistics (mean, std, min, max, total).
    """
    times = []
    
    for _ in range(n_runs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        times.append(end - start)
    
    return {
        "mean_time": np.mean(times),
        "std_time": np.std(times),
        "min_time": np.min(times),
        "max_time": np.max(times),
        "total_time": np.sum(times),
        "n_runs": n_runs,
        "result": result  # Return the last result
    }


def benchmark_model_training(model: Any, X_train: np.ndarray, y_train: np.ndarray,
                            X_test: Optional[np.ndarray] = None,
                            y_test: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """
    Benchmark model training and prediction times.

    Args:
        model: Model object with fit() and predict() methods.
        X_train: Training features.
        y_train: Training targets.
        X_test: Optional test features for prediction benchmarking.
        y_test: Optional test targets for accuracy calculation.

    Returns:
        Dictionary with training time, prediction time, and optional accuracy.
    """
    # Benchmark training
    with TimeBlock("model_training"):
        model.fit(X_train, y_train)
    
    # Read training time from log (simplified - in practice, TimeBlock logs it)
    train_start = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - train_start
    
    results = {
        "training_time": train_time,
        "n_samples": len(X_train),
        "n_features": X_train.shape[1] if X_train.ndim > 1 else 1
    }
    
    # Benchmark prediction if test data provided
    if X_test is not None:
        pred_start = time.time()
        y_pred = model.predict(X_test)
        pred_time = time.time() - pred_start
        
        results["prediction_time"] = pred_time
        results["predictions_per_second"] = len(X_test) / pred_time if pred_time > 0 else 0
        
        # Calculate accuracy if test labels provided
        if y_test is not None:
            from sklearn.metrics import accuracy_score, mean_squared_error
            if hasattr(model, 'predict_proba') or len(np.unique(y_test)) < 20:
                # Classification
                accuracy = accuracy_score(y_test, y_pred)
                results["test_accuracy"] = accuracy
            else:
                # Regression
                mse = mean_squared_error(y_test, y_pred)
                results["test_rmse"] = np.sqrt(mse)
    
    return results


def scalability_analysis(func: Callable, data_sizes: List[int],
                         data_generator: Callable[[int], tuple],
                         **kwargs) -> pd.DataFrame:
    """
    Analyze how function performance scales with data size.

    Args:
        func: Function to benchmark.
        data_sizes: List of data sizes to test.
        data_generator: Function that takes size and returns (X, y) or just X.
        **kwargs: Additional arguments to pass to func.

    Returns:
        DataFrame with scalability results.
    """
    results = []
    
    for size in data_sizes:
        # Generate data
        data = data_generator(size)
        
        # Benchmark function
        if isinstance(data, tuple):
            benchmark_result = benchmark_function(func, *data, n_runs=3, **kwargs)
        else:
            benchmark_result = benchmark_function(func, data, n_runs=3, **kwargs)
        
        results.append({
            "data_size": size,
            "mean_time": benchmark_result["mean_time"],
            "std_time": benchmark_result["std_time"]
        })
    
    return pd.DataFrame(results)


def compare_algorithms(algorithms: Dict[str, Callable], X: np.ndarray, y: np.ndarray,
                      X_test: Optional[np.ndarray] = None,
                      y_test: Optional[np.ndarray] = None) -> pd.DataFrame:
    """
    Compare multiple algorithms on the same dataset.

    Args:
        algorithms: Dictionary mapping algorithm names to fit functions.
        X: Training features.
        y: Training targets.
        X_test: Optional test features.
        y_test: Optional test targets.

    Returns:
        DataFrame with comparison results.
    """
    results = []
    
    for algo_name, algo_func in algorithms.items():
        # Benchmark this algorithm
        benchmark_result = benchmark_model_training(
            algo_func(), X, y, X_test, y_test
        )
        
        result_row = {
            "algorithm": algo_name,
            **benchmark_result
        }
        results.append(result_row)
    
    return pd.DataFrame(results)


def save_benchmark_results(results: pd.DataFrame, filename_prefix: str = "benchmark") -> str:
    """
    Save benchmark results to a timestamped CSV file.

    Args:
        results: DataFrame with benchmark results.
        filename_prefix: Prefix for the output filename.

    Returns:
        Path to the saved file.
    """
    output_path = timestamped_path("outputs/results", filename_prefix, "csv")
    results.to_csv(output_path, index=False)
    return str(output_path)


def estimate_memory_usage(data: np.ndarray) -> Dict[str, float]:
    """
    Estimate memory usage of a numpy array.

    Args:
        data: NumPy array.

    Returns:
        Dictionary with memory usage in bytes and MB.
    """
    memory_bytes = data.nbytes
    memory_mb = memory_bytes / (1024 * 1024)
    
    return {
        "memory_bytes": memory_bytes,
        "memory_mb": memory_mb,
        "shape": data.shape,
        "dtype": str(data.dtype)
    }

