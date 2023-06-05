import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class DataVisualizer:
    def plot_line_chart(self, data, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f'output/{title}.png')
        plt.show()

    def plot_distribution(self, data, title="Distribution", xlabel="X-axis", ylabel="Y-axis"):
        # If data is a Series of counts, we use a bar plot
        if isinstance(data, pd.Series):
            data.plot(kind='bar', figsize=(10, 6))
        else:  # If data is raw data, we use a histogram
            sns.histplot(data=data, kde=True, figsize=(10, 6))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f'output/{title}.png')
        plt.show()

    def plot_pie(self, data, title="Pie Chart"):
        data.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6))
        plt.title(title)
        plt.ylabel('')
        plt.savefig(f'output/{title}.png')
        plt.show()

    def plot_scatter(self, data, x, y, title="Scatter plot", xlabel="X-axis", ylabel="Y-axis"):
        sns.scatterplot(data=data, x=x, y=y, figsize=(10, 6))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f'output/{title}.png')
        plt.show()
