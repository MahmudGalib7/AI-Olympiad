import unittest
import numpy as np
import pandas as pd
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor('data/sample_data.csv')

    def test_load_data(self):
        data = self.processor.load_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    def test_clean_data(self):
        raw_data = self.processor.load_data()
        cleaned_data = self.processor.clean_data(raw_data)
        self.assertEqual(cleaned_data.isnull().sum().sum(), 0)

    def test_analyze_data(self):
        data = self.processor.load_data()
        analysis_result = self.processor.analyze_data(data)
        self.assertIn('mean', analysis_result)
        self.assertIn('median', analysis_result)
        self.assertIn('std_dev', analysis_result)

if __name__ == '__main__':
    unittest.main()