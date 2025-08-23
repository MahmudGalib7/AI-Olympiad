class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        import numpy as np
        import pandas as pd
        
        self.data = pd.read_csv(self.filepath)
        return self.data

    def clean_data(self):
        if self.data is not None:
            self.data.dropna(inplace=True)
            self.data = self.data.select_dtypes(include=[np.number])
        return self.data

    def analyze_data(self):
        if self.data is not None:
            mean_values = self.data.mean()
            median_values = self.data.median()
            std_dev_values = self.data.std()
            return {
                'mean': mean_values,
                'median': median_values,
                'std_dev': std_dev_values
            }
        return None