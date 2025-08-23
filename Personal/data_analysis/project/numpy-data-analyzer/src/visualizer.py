class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column, bins=10):
        import matplotlib.pyplot as plt
        plt.hist(self.data[column], bins=bins, alpha=0.7, color='blue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

    def plot_scatter(self, x_column, y_column):
        import matplotlib.pyplot as plt
        plt.scatter(self.data[x_column], self.data[y_column], alpha=0.7, color='red')
        plt.title(f'Scatter plot of {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
        plt.show()

    def show_correlation_matrix(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        correlation_matrix = self.data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()