import matplotlib.pyplot as plt

class ColumnAnalyzer:

    def analyze_column(self, data, column, title_histo):

        # Summary statistics
        summary_stats = data[column].describe()
        print(f"Summary Statistics for {column}:\n{summary_stats}\n")

        # Histogram
        plt.figure(figsize=(10, 5))
        plt.hist(data[column], bins=30, edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.savefig(f'output/{title_histo}.png')
        plt.show()

        # Check skewness
        skewness = data[column].skew()
        print(f"Skewness of {column}: {skewness}\n")

