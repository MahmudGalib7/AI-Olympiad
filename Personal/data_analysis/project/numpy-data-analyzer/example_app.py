from numpy_data_analyzer import DataAnalyzer
import numpy as np

def main():
    # Initialize the analyzer
    analyzer = DataAnalyzer()
    
    # Generate some random data
    print("Generating sample data...")
    data = analyzer.generate_sample_data(1000, 4)
    print(f"Data shape: {data.shape}")
    
    # Basic statistics
    print("\nCalculating basic statistics...")
    stats = analyzer.basic_statistics()
    for stat_name, stat_values in stats.items():
        print(f"{stat_name}: {stat_values}")
    
    # Normalize data
    print("\nNormalizing data (Z-score method)...")
    normalized_data = analyzer.normalize_data(method='zscore')
    print(f"Normalized data - first 5 rows:\n{normalized_data[:5]}")
    
    # Find outliers
    print("\nFinding outliers...")
    indices, values = analyzer.find_outliers(threshold=3.0)
    print(f"Found {len(values)} outliers")
    
    # PCA
    print("\nPerforming PCA...")
    transformed_data, eigenvectors, eigenvalues = analyzer.pca(n_components=2)
    print(f"Transformed data shape: {transformed_data.shape}")
    print(f"Explained variance: {eigenvalues / sum(eigenvalues)}")
    
    # K-means
    print("\nPerforming K-means clustering...")
    labels, centroids = analyzer.kmeans(k=3, max_iter=100)
    print(f"Cluster distribution: {np.bincount(labels.astype(int))}")
    
    # Correlation analysis
    print("\nCalculating correlation matrix...")
    corr_matrix = analyzer.correlation_analysis()
    print(f"Correlation matrix:\n{corr_matrix}")
    
    # Plot results
    print("\nCreating visualizations...")
    analyzer.plot_histogram(column=0, bins=20)
    analyzer.plot_scatter(x_col=0, y_col=1, c=labels)
    
    # Example of custom filtering
    print("\nFiltering data...")
    filtered_data = analyzer.filter_data(lambda x: x[:, 0] > 0)
    print(f"Filtered data shape: {filtered_data.shape}")
    
    # Performance benchmark
    print("\nBenchmarking PCA performance...")
    pca_time = analyzer.performance_benchmark(analyzer.pca, n_components=2)
    print(f"PCA execution time: {pca_time:.4f} seconds")
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()