import unittest
import numpy as np
import pandas as pd
from src.visualizer import DataVisualizer

class TestDataVisualizer(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'A': np.random.rand(100),
            'B': np.random.rand(100),
            'C': np.random.rand(100)
        })
        self.visualizer = DataVisualizer(self.data)

    def test_plot_histogram(self):
        # Test if histogram plotting works without errors
        try:
            self.visualizer.plot_histogram('A')
            histogram_exists = True
        except Exception:
            histogram_exists = False
        self.assertTrue(histogram_exists)

    def test_plot_scatter(self):
        # Test if scatter plot works without errors
        try:
            self.visualizer.plot_scatter('A', 'B')
            scatter_exists = True
        except Exception:
            scatter_exists = False
        self.assertTrue(scatter_exists)

    def test_show_correlation_matrix(self):
        # Test if correlation matrix is generated correctly
        correlation_matrix = self.visualizer.show_correlation_matrix()
        self.assertEqual(correlation_matrix.shape, (3, 3))  # Check shape for 3 variables

if __name__ == '__main__':
    unittest.main()