"""
Used in: All algorithm notebooks for performance benchmarking
Purpose:
    Provide performance benchmarking utilities including timing,
    memory profiling, and scalability analysis.
    
Educational Context:
    This module demonstrates:
    1. Performance measurement and profiling
    2. Scalability analysis (how performance changes with data size)
    3. Algorithm comparison
    4. Memory usage estimation
    
    Why benchmark?
    - Compare different algorithms
    - Identify bottlenecks
    - Understand scalability (will it work with 10x more data?)
    - Make informed decisions about which algorithm to use
"""

# Import time: For measuring execution time
import time

# Import NumPy: For numerical operations and array handling
import numpy as np

# Import Pandas: For DataFrame operations (tabular data structures)
import pandas as pd

# Import type hints: Document expected types for better code clarity
# Callable = function type, Optional = can be None
from typing import Dict, List, Any, Callable, Optional

# Import our utility functions
from src.utils.paths import timestamped_path  # For creating timestamped output files
from src.utils.timing import TimeBlock  # For timing code blocks

# Import sys: System-specific parameters and functions
# Used here for memory profiling utilities
import sys


def benchmark_function(func: Callable, *args, n_runs: int = 5, **kwargs) -> Dict[str, float]:
    """
    Benchmark a function by running it multiple times and collecting statistics.
    
    Educational Explanation:
        This function demonstrates:
        1. Function arguments: *args and **kwargs for flexible inputs
        2. Running code multiple times for statistical reliability
        3. Collecting and analyzing timing data
        
        Why run multiple times?
        - First run may be slower (cache warming, JIT compilation)
        - System load varies (other processes running)
        - Multiple runs give more reliable average
        - Can detect outliers (very slow runs)
        
        Statistical measures:
        - Mean: Average time (most representative)
        - Std: Standard deviation (variability)
        - Min/Max: Best/worst case performance
    
    Args:
        func: Function to benchmark (any callable)
        *args: Positional arguments to pass to func
               Example: benchmark_function(my_func, arg1, arg2)
        n_runs: Number of times to run the function (default 5)
                More runs = more reliable but slower
        **kwargs: Keyword arguments to pass to func
                 Example: benchmark_function(my_func, x=1, y=2)
    
    Returns:
        Dictionary with timing statistics:
        - mean_time: Average execution time
        - std_time: Standard deviation (variability)
        - min_time: Fastest run
        - max_time: Slowest run
        - total_time: Sum of all runs
        - n_runs: Number of runs performed
        - result: Return value from last function call
    """
    # List to store execution times from each run
    # We'll calculate statistics from this list
    times = []
    
    # Run the function multiple times
    # range(n_runs) generates numbers 0, 1, 2, ..., n_runs-1
    # _ is a convention meaning "we don't use this variable"
    # We just want to loop n_runs times, we don't need the loop counter
    for _ in range(n_runs):
        # Record start time (seconds since Unix epoch)
        start = time.time()
        
        # Execute the function with all provided arguments
        # *args unpacks positional arguments: func(arg1, arg2, ...)
        # **kwargs unpacks keyword arguments: func(x=1, y=2, ...)
        # This allows us to benchmark any function with any arguments
        result = func(*args, **kwargs)
        
        # Record end time
        end = time.time()
        
        # Calculate duration and add to list
        # end - start gives seconds elapsed
        times.append(end - start)
    
    # Calculate and return statistics
    return {
        "mean_time": np.mean(times),  # Average time (most representative)
        "std_time": np.std(times),  # Standard deviation (measure of variability)
        "min_time": np.min(times),  # Best case (fastest run)
        "max_time": np.max(times),  # Worst case (slowest run)
        "total_time": np.sum(times),  # Total time for all runs
        "n_runs": n_runs,  # Number of runs performed
        "result": result  # Return value from last function call (useful for verification)
    }


def benchmark_model_training(model: Any, X_train: np.ndarray, y_train: np.ndarray,
                            X_test: Optional[np.ndarray] = None,
                            y_test: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """
    Benchmark model training and prediction times.
    
    Educational Explanation:
        This function measures:
        1. Training time: How long it takes to learn from data
        2. Prediction time: How fast the model makes predictions
        3. Throughput: Predictions per second (important for real-time systems)
        4. Accuracy: Model performance (if test labels provided)
        
        Why benchmark training?
        - Some models train in seconds, others take hours
        - Helps choose between algorithms based on time constraints
        - Identifies if training is a bottleneck
        
        Why benchmark prediction?
        - Real-time systems need fast predictions
        - Batch processing needs high throughput
        - Helps estimate infrastructure needs
    
    Args:
        model: Model object with fit() and predict() methods
              (scikit-learn style interface)
        X_train: Training features (2D array: samples × features)
        y_train: Training targets (1D array: one label per sample)
        X_test: Optional test features for prediction benchmarking
        y_test: Optional test targets for accuracy calculation
    
    Returns:
        Dictionary with:
        - training_time: Time to train the model (seconds)
        - n_samples: Number of training samples
        - n_features: Number of features
        - prediction_time: Time to make predictions (if X_test provided)
        - predictions_per_second: Throughput metric (if X_test provided)
        - test_accuracy or test_rmse: Performance metric (if y_test provided)
    """
    # Measure training time
    # We use manual timing here instead of TimeBlock to get the value directly
    # TimeBlock logs to file, but we need the value in our return dictionary
    train_start = time.time()
    
    # Train the model
    # fit() is the standard scikit-learn method for training
    # It learns patterns from X_train and y_train
    model.fit(X_train, y_train)
    
    # Calculate training duration
    train_time = time.time() - train_start
    
    # Build results dictionary with training information
    results = {
        "training_time": train_time,  # How long training took
        "n_samples": len(X_train),  # Number of training examples
        # Number of features (columns in X_train)
        # X_train.ndim checks number of dimensions (1D or 2D)
        # If 2D, shape[1] is number of columns (features)
        # If 1D, there's only 1 feature
        "n_features": X_train.shape[1] if X_train.ndim > 1 else 1
    }
    
    # Benchmark prediction if test data is provided
    # Optional parameters allow flexible usage (can skip prediction timing)
    if X_test is not None:
        # Measure prediction time
        pred_start = time.time()
        
        # Make predictions on test data
        # predict() uses the trained model to make predictions
        y_pred = model.predict(X_test)
        
        # Calculate prediction duration
        pred_time = time.time() - pred_start
        
        # Store prediction metrics
        results["prediction_time"] = pred_time
        # Calculate throughput: how many predictions per second
        # This is important for real-time systems
        # Check pred_time > 0 to avoid division by zero
        results["predictions_per_second"] = len(X_test) / pred_time if pred_time > 0 else 0
        
        # Calculate accuracy if test labels are provided
        # This lets us see both speed AND quality
        if y_test is not None:
            # Import metrics here (lazy import - only when needed)
            from sklearn.metrics import accuracy_score, mean_squared_error
            
            # Determine if this is classification or regression
            # Classification models often have predict_proba() method
            # Or we check if there are few unique values (likely classes)
            # Regression has many unique values (continuous)
            if hasattr(model, 'predict_proba') or len(np.unique(y_test)) < 20:
                # Classification task
                # accuracy_score compares predictions to true labels
                # Returns proportion correct (0.0 to 1.0)
                accuracy = accuracy_score(y_test, y_pred)
                results["test_accuracy"] = accuracy
            else:
                # Regression task
                # mean_squared_error measures average squared difference
                # Lower is better (0 = perfect predictions)
                mse = mean_squared_error(y_test, y_pred)
                # RMSE (Root Mean Squared Error) is in same units as target
                # More interpretable than MSE
                results["test_rmse"] = np.sqrt(mse)
    
    # Return comprehensive benchmark results
    return results


def scalability_analysis(func: Callable, data_sizes: List[int],
                         data_generator: Callable[[int], tuple],
                         **kwargs) -> pd.DataFrame:
    """
    Analyze how function performance scales with data size.
    
    Educational Explanation:
        This function measures how execution time changes as data size increases.
        This is crucial for understanding:
        - Will the algorithm work with 10x more data?
        - Is it O(n), O(n²), or O(n log n)?
        - When will we hit performance limits?
        
        Scalability types:
        - Linear O(n): Time doubles when data doubles
        - Quadratic O(n²): Time quadruples when data doubles
        - Logarithmic O(log n): Time grows slowly
        
        Why test multiple sizes?
        - Small datasets may hide performance issues
        - Large datasets reveal true scalability
        - Helps plan infrastructure needs
    
    Args:
        func: Function to benchmark (the algorithm to test)
        data_sizes: List of data sizes to test
                   Example: [100, 500, 1000, 5000, 10000]
        data_generator: Function that creates data of given size
                       Takes: size (int)
                       Returns: (X, y) tuple or just X
                       Example: lambda n: (np.random.rand(n, 10), np.random.rand(n))
        **kwargs: Additional arguments to pass to func
    
    Returns:
        DataFrame with columns:
        - data_size: Size of data tested
        - mean_time: Average execution time
        - std_time: Standard deviation (variability)
    """
    # List to collect results from each data size
    results = []
    
    # Test function with each data size
    # This shows how performance changes as data grows
    for size in data_sizes:
        # Generate data of the specified size
        # data_generator is a function that creates synthetic or real data
        # This allows testing with different data sizes without manual preparation
        data = data_generator(size)
        
        # Benchmark the function with this data size
        # Check if data is a tuple (X, y) or single array (X)
        if isinstance(data, tuple):
            # Unpack tuple: *data spreads tuple elements as separate arguments
            # Example: func(*(X, y)) becomes func(X, y)
            benchmark_result = benchmark_function(func, *data, n_runs=3, **kwargs)
        else:
            # Single array: pass it directly
            benchmark_result = benchmark_function(func, data, n_runs=3, **kwargs)
        
        # Store results for this data size
        # We use n_runs=3 (fewer than default) because we're testing many sizes
        # This balances accuracy with speed
        results.append({
            "data_size": size,  # Size of data tested
            "mean_time": benchmark_result["mean_time"],  # Average execution time
            "std_time": benchmark_result["std_time"]  # Variability in timing
        })
    
    # Convert results list to DataFrame for easy analysis and plotting
    # DataFrame is a Pandas table structure (like Excel spreadsheet)
    # Makes it easy to plot, filter, and analyze
    return pd.DataFrame(results)


def compare_algorithms(algorithms: Dict[str, Callable], X: np.ndarray, y: np.ndarray,
                      X_test: Optional[np.ndarray] = None,
                      y_test: Optional[np.ndarray] = None) -> pd.DataFrame:
    """
    Compare multiple algorithms on the same dataset.
    
    Educational Explanation:
        This function runs multiple algorithms on the same data for fair comparison.
        Fair comparison requires:
        - Same training data
        - Same test data
        - Same evaluation metrics
        
        Why compare algorithms?
        - Different algorithms have different strengths
        - Some are faster, some are more accurate
        - Helps choose the best algorithm for your specific needs
        - Trade-offs: speed vs accuracy, simplicity vs performance
    
    Args:
        algorithms: Dictionary mapping algorithm names to factory functions
                   Example: {"RandomForest": lambda: RandomForestClassifier(),
                            "SVM": lambda: SVC()}
                   Factory functions (functions that return objects) allow
                   creating fresh models for each comparison
        X: Training features (same for all algorithms)
        y: Training targets (same for all algorithms)
        X_test: Optional test features for prediction benchmarking
        y_test: Optional test targets for accuracy calculation
    
    Returns:
        DataFrame with one row per algorithm, columns include:
        - algorithm: Name of the algorithm
        - training_time: Time to train
        - prediction_time: Time to predict (if X_test provided)
        - test_accuracy or test_rmse: Performance (if y_test provided)
    """
    # List to collect results from each algorithm
    results = []
    
    # Iterate through each algorithm
    # .items() returns (key, value) pairs: (algorithm_name, factory_function)
    for algo_name, algo_func in algorithms.items():
        # Benchmark this algorithm
        # algo_func() calls the factory function to create a fresh model instance
        # This ensures each algorithm starts with a clean model (no leftover state)
        benchmark_result = benchmark_model_training(
            algo_func(),  # Create new model instance
            X, y,  # Training data
            X_test, y_test  # Test data (optional)
        )
        
        # Combine algorithm name with benchmark results
        # **benchmark_result unpacks the dictionary into key-value pairs
        # Example: {"algorithm": "RF", **{"time": 1.0}} becomes {"algorithm": "RF", "time": 1.0}
        result_row = {
            "algorithm": algo_name,  # Name of the algorithm
            **benchmark_result  # All benchmark metrics
        }
        results.append(result_row)
    
    # Convert to DataFrame for easy comparison and visualization
    # DataFrame makes it easy to sort, filter, and plot results
    return pd.DataFrame(results)


def save_benchmark_results(results: pd.DataFrame, filename_prefix: str = "benchmark") -> str:
    """
    Save benchmark results to a timestamped CSV file.
    
    Educational Explanation:
        This function demonstrates:
        1. Saving data to files for later analysis
        2. Using timestamped filenames to prevent overwriting
        3. CSV format for easy sharing and analysis
        
        Why save results?
        - Track performance over time
        - Share results with others
        - Compare runs from different days
        - Build a performance database
    
    Args:
        results: DataFrame with benchmark results (from compare_algorithms, etc.)
        filename_prefix: Prefix for the output filename
                       Example: "benchmark" -> "benchmark_20251230_143022.csv"
    
    Returns:
        Path to the saved file (as string for easy use)
    """
    # Generate timestamped file path
    # This ensures each run gets a unique filename
    # Format: outputs/results/benchmark_YYYYMMDD_HHMMSS.csv
    output_path = timestamped_path("outputs/results", filename_prefix, "csv")
    
    # Save DataFrame to CSV file
    # to_csv() converts DataFrame to CSV format
    # index=False means don't save row numbers (cleaner CSV)
    results.to_csv(output_path, index=False)
    
    # Return path as string (Path objects can be converted to strings)
    return str(output_path)


def estimate_memory_usage(data: np.ndarray) -> Dict[str, float]:
    """
    Estimate memory usage of a numpy array.
    
    Educational Explanation:
        This function calculates how much RAM an array uses.
        
        Memory calculation:
        - Total bytes = number_of_elements × bytes_per_element
        - NumPy arrays store data efficiently (contiguous memory)
        - Different dtypes use different amounts:
          * int8: 1 byte per element
          * int32: 4 bytes per element
          * float64: 8 bytes per element
        
        Why estimate memory?
        - Plan for large datasets
        - Avoid running out of RAM
        - Choose appropriate data types
        - Optimize memory usage
    
    Args:
        data: NumPy array (any shape, any dtype)
    
    Returns:
        Dictionary with:
        - memory_bytes: Memory usage in bytes
        - memory_mb: Memory usage in megabytes (more readable)
        - shape: Array dimensions (e.g., (1000, 10))
        - dtype: Data type (e.g., 'float64', 'int32')
    """
    # Get total memory usage in bytes
    # .nbytes is a NumPy array property that calculates:
    # nbytes = total_elements × bytes_per_element
    # Example: array of shape (1000, 10) with float64:
    #   1000 × 10 × 8 bytes = 80,000 bytes
    memory_bytes = data.nbytes
    
    # Convert bytes to megabytes for readability
    # 1 MB = 1024 × 1024 bytes = 1,048,576 bytes
    # Division converts bytes to MB
    memory_mb = memory_bytes / (1024 * 1024)
    
    # Return comprehensive memory information
    return {
        "memory_bytes": memory_bytes,  # Exact bytes (for precise calculations)
        "memory_mb": memory_mb,  # Megabytes (for human readability)
        "shape": data.shape,  # Array dimensions (helps understand size)
        "dtype": str(data.dtype)  # Data type (affects memory usage)
    }

