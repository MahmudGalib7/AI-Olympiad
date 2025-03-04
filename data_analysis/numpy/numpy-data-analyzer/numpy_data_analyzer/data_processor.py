import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Optional, Union
import time
import os


class DataAnalyzer:
    """
    A comprehensive NumPy-based data analysis toolkit that demonstrates
    various NumPy operations and techniques.
    """
    
    def __init__(self, random_seed: int = 42):
        """Initialize the data analyzer with a random seed for reproducibility."""
        np.random.seed(random_seed)
        self.data = None
    
    def generate_sample_data(self, rows: int = 1000, cols: int = 5) -> np.ndarray:
        """Generate sample data with random values."""
        self.data = np.random.randn(rows, cols)
        return self.data
    
    def load_data(self, filepath: str) -> np.ndarray:
        """Load data from a CSV or text file."""
        try:
            self.data = np.loadtxt(filepath, delimiter=',', skiprows=1)
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            return np.array([])
    
    def save_data(self, filepath: str) -> bool:
        """Save current data to a file."""
        if self.data is None:
            return False
        
        try:
            np.savetxt(filepath, self.data, delimiter=',')
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def basic_statistics(self) -> Dict[str, np.ndarray]:
        """Calculate basic statistics for the dataset."""
        if self.data is None:
            return {}
        
        return {
            'mean': np.mean(self.data, axis=0),
            'median': np.median(self.data, axis=0),
            'std': np.std(self.data, axis=0),
            'min': np.min(self.data, axis=0),
            'max': np.max(self.data, axis=0),
            'percentiles': np.percentile(self.data, [25, 50, 75], axis=0)
        }
    
    def normalize_data(self, method: str = 'minmax') -> np.ndarray:
        """
        Normalize the data using different methods.
        
        Parameters:
        -----------
        method : str
            'minmax' - Scale data to range [0,1]
            'zscore' - Standardize to mean=0, std=1
            'robust' - Scale using median and IQR
        
        Returns:
        --------
        np.ndarray
            Normalized data
        """
        if self.data is None:
            return np.array([])
        
        if method == 'minmax':
            min_vals = np.min(self.data, axis=0)
            max_vals = np.max(self.data, axis=0)
            return (self.data - min_vals) / (max_vals - min_vals)
        
        elif method == 'zscore':
            mean = np.mean(self.data, axis=0)
            std = np.std(self.data, axis=0)
            return (self.data - mean) / std
        
        elif method == 'robust':
            median = np.median(self.data, axis=0)
            q75, q25 = np.percentile(self.data, [75, 25], axis=0)
            iqr = q75 - q25
            return (self.data - median) / iqr
        
        else:
            raise ValueError(f"Unknown normalization method: {method}")
    
    def find_outliers(self, threshold: float = 3.0) -> Tuple[np.ndarray, np.ndarray]:
        """
        Find outliers using z-score method.
        
        Parameters:
        -----------
        threshold : float
            Z-score threshold for outliers
            
        Returns:
        --------
        Tuple[np.ndarray, np.ndarray]
            Indices and values of outliers
        """
        if self.data is None:
            return np.array([]), np.array([])
        
        z_scores = np.abs((self.data - np.mean(self.data, axis=0)) / np.std(self.data, axis=0))
        outlier_mask = z_scores > threshold
        
        outlier_indices = np.where(outlier_mask)
        outlier_values = self.data[outlier_indices]
        
        return outlier_indices, outlier_values
    
    def pca(self, n_components: int = 2) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Perform Principal Component Analysis.
        
        Parameters:
        -----------
        n_components : int
            Number of components to keep
            
        Returns:
        --------
        Tuple[np.ndarray, np.ndarray, np.ndarray]
            Transformed data, eigenvectors, eigenvalues
        """
        if self.data is None:
            return np.array([]), np.array([]), np.array([])
        
        # Center the data
        mean = np.mean(self.data, axis=0)
        centered_data = self.data - mean
        
        # Compute covariance matrix
        cov_matrix = np.cov(centered_data, rowvar=False)
        
        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort eigenvectors by eigenvalues in descending order
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # Keep only n_components
        eigenvalues = eigenvalues[:n_components]
        eigenvectors = eigenvectors[:, :n_components]
        
        # Transform the data
        transformed_data = np.dot(centered_data, eigenvectors)
        
        return transformed_data, eigenvectors, eigenvalues
    
    def kmeans(self, k: int = 3, max_iter: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """
        Implement K-means clustering algorithm using NumPy.
        
        Parameters:
        -----------
        k : int
            Number of clusters
        max_iter : int
            Maximum number of iterations
            
        Returns:
        --------
        Tuple[np.ndarray, np.ndarray]
            Cluster labels and centroids
        """
        if self.data is None or k <= 0:
            return np.array([]), np.array([])
        
        # Initialize centroids randomly
        n_samples, n_features = self.data.shape
        centroids_idx = np.random.choice(n_samples, k, replace=False)
        centroids = self.data[centroids_idx]
        
        # Iterate until convergence or max_iter
        labels = np.zeros(n_samples)
        
        for _ in range(max_iter):
            # Compute distances to centroids
            distances = np.zeros((n_samples, k))
            for i in range(k):
                distances[:, i] = np.sum((self.data - centroids[i]) ** 2, axis=1)
            
            # Assign samples to nearest centroid
            new_labels = np.argmin(distances, axis=1)
            
            # Check for convergence
            if np.array_equal(new_labels, labels):
                break
            
            labels = new_labels
            
            # Update centroids
            for i in range(k):
                cluster_points = self.data[labels == i]
                if len(cluster_points) > 0:
                    centroids[i] = np.mean(cluster_points, axis=0)
        
        return labels, centroids
    
    def correlation_analysis(self) -> np.ndarray:
        """Calculate correlation matrix for the dataset."""
        if self.data is None:
            return np.array([])
        
        return np.corrcoef(self.data, rowvar=False)
    
    def apply_function(self, func, axis: int = 0) -> np.ndarray:
        """Apply a function along an axis of the dataset."""
        if self.data is None:
            return np.array([])
        
        return np.apply_along_axis(func, axis, self.data)
    
    def filter_data(self, condition) -> np.ndarray:
        """Filter data based on a condition."""
        if self.data is None:
            return np.array([])
        
        mask = condition(self.data)
        return self.data[mask]
    
    def performance_benchmark(self, func, *args, **kwargs) -> float:
        """
        Benchmark a function's performance.
        
        Returns:
        --------
        float
            Execution time in seconds
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        
        return end_time - start_time
    
    def plot_histogram(self, column: int = 0, bins: int = 10) -> None:
        """Plot a histogram of a specific column."""
        if self.data is None or column >= self.data.shape[1]:
            print("Invalid data or column index.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[:, column], bins=bins)
        plt.title(f'Histogram of Column {column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def plot_scatter(self, x_col: int = 0, y_col: int = 1, c: Optional[np.ndarray] = None) -> None:
        """Plot a scatter plot of two columns."""
        if self.data is None or x_col >= self.data.shape[1] or y_col >= self.data.shape[1]:
            print("Invalid data or column indices.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[:, x_col], self.data[:, y_col], c=c, alpha=0.6)
        plt.title(f'Scatter Plot: Column {x_col} vs Column {y_col}')
        plt.xlabel(f'Column {x_col}')
        plt.ylabel(f'Column {y_col}')
        plt.grid(True, alpha=0.3)
        if c is not None:
            plt.colorbar(label='Cluster')
        plt.show()