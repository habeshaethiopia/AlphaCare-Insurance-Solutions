import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def __init__(self, df):
        """
        Initializes the Visualizer with a pandas DataFrame.
        
        Args:
            df (pandas.DataFrame): The data to visualize.
        """
        self.df = df

    def plot_histogram(self, column, bins=30, title="Histogram", xlabel="Value", ylabel="Frequency", color='blue'):
        """
        Plots a histogram for a given column in the dataframe.
        
        Args:
            column (str): The column to plot.
            bins (int): Number of bins for the histogram.
            title (str): Title of the histogram.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            color (str): Color of the bars.
        """
        plt.figure(figsize=(10, 6))
        self.df[column].hist(bins=bins, alpha=0.7, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_scatter(self, x_column, y_column, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
        """
        Plots a scatter plot for two given columns in the dataframe.
        
        Args:
            x_column (str): The column to use for the x-axis.
            y_column (str): The column to use for the y-axis.
            title (str): Title of the scatter plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_column, y=y_column, data=self.df)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_correlation_heatmap(self, columns, title="Correlation Matrix", cmap='coolwarm'):
        """
        Plots a heatmap of the correlation matrix for the given columns.
        
        Args:
            columns (list): List of columns to include in the correlation matrix.
            title (str): Title of the heatmap.
            cmap (str): Colormap to use for the heatmap.
        """
        correlation_matrix = self.df[columns].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap=cmap)
        plt.title(title)
        plt.show()

    def plot_bar(self, x_column, y_column, title="Bar Plot", xlabel="X-axis", ylabel="Y-axis", color='blue'):
        """
        Plots a bar plot for the given columns in the dataframe.
        
        Args:
            x_column (str): The column to use for the x-axis.
            y_column (str): The column to use for the y-axis.
            title (str): Title of the bar plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            color (str): Color of the bars.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x_column, y=y_column, data=self.df, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()