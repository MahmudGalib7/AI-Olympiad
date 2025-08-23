# NumPy Data Analyzer 📊🔍

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.20+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **A powerful, elegant toolkit for data analysis using NumPy**

## ✨ Overview

The NumPy Data Analyzer is a Python project designed for data processing and visualization using NumPy and other libraries. It provides tools to load, clean, analyze, and visualize data from CSV files, making it easier for users to gain insights from their datasets.

## 🚀 Features

- **Data Management** 📁 - Generate, load, and save datasets effortlessly
- **Statistical Analysis** 📈 - Calculate mean, median, std, min/max, and percentiles
- **Data Normalization** 🧮 - MinMax, Z-score, and Robust scaling options
- **Outlier Detection** 🔎 - Identify and analyze anomalous data points
- **Dimensionality Reduction** 🧩 - Implement PCA to reduce features
- **K-means Clustering** 🔮 - Group similar data points automatically
- **Correlation Analysis** 🔗 - Discover relationships between variables
- **Performance Benchmarking** ⚡ - Measure execution time of operations
- **Data Visualization** 📉 - Create histograms and scatter plots

## 📦 Project Structure

```
numpy-data-analyzer
├── src
│   ├── __init__.py
│   ├── data_processor.py
│   ├── visualizer.py
│   ├── models.py
│   └── utils.py
├── data
│   └── sample_data.csv
├── tests
│   ├── __init__.py
│   ├── test_data_processor.py
│   └── test_visualizer.py
├── notebooks
│   └── analysis_examples.ipynb
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
pip install -e .
```

## Usage

1. Load your data using the `DataProcessor` class from `data_processor.py`.
2. Clean and analyze the data with the provided methods.
3. Visualize the results using the `DataVisualizer` class from `visualizer.py`.
4. Optionally, apply statistical models from `models.py` for predictions.

## Examples
Refer to the Jupyter notebook `notebooks/analysis_examples.ipynb` for practical examples of how to use the classes and methods in this project.

```python
from numpy_data_analyzer import DataAnalyzer

# Initialize the analyzer
analyzer = DataAnalyzer()

# Generate sample data
data = analyzer.generate_sample_data(1000, 5)

# Calculate basic statistics
stats = analyzer.basic_statistics()
print(stats['mean'], stats['std'])

# Normalize data
normalized = analyzer.normalize_data(method='zscore')

# Perform PCA
transformed, eigenvectors, eigenvalues = analyzer.pca(n_components=2)

# Visualize data
analyzer.plot_histogram(column=0)
analyzer.plot_scatter(x_col=0, y_col=1)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.