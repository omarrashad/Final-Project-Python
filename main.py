import pandas as pd
from data_processor import DataProcessor
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer
from column_analyzer import ColumnAnalyzer

# Create an instance of DataProcessor class
data_processor = DataProcessor('dataset/Musical_instruments_reviews.csv')

# Load the dataset
data = data_processor.load_data()

# Check for missing values
missing_values = data.isnull().sum()
print('Missing Values:\n', missing_values)

# Check for duplicate values
duplicates = data.duplicated().sum()
print('Duplicates: ', duplicates, '\n')

# Check data types
print(data.dtypes)

# Clean the dataset
cleaned_data = data_processor.clean_data(data)


# Define a function that returns 1 if the overall rating is 4 or above, and 0 otherwise
def recommend(rating):
    if rating >= 4:
        return 1
    else:
        return 0


# Create the new 'recommended' column
cleaned_data['recommended'] = cleaned_data['overall'].apply(recommend)

# Create an instance of ColumnAnalyzer class
column_analyzer = ColumnAnalyzer()

# Analyze the 'total_votes' column
column_analyzer.analyze_column(cleaned_data, 'total_votes', 'Distribution of total_votes')

# Transform the 'total_votes' column to 3 categories
# Define the thresholds for 'total_votes'
bins = [-1, 0, 10, cleaned_data['total_votes'].max()]

# Define the labels
labels = ['Low Count', 'Medium Count', 'High Count']

# Create a new column for feedback categories
cleaned_data['Feedback Category'] = pd.cut(cleaned_data['total_votes'], bins=bins, labels=labels, include_lowest=True)

# Create an instance of DataAnalyzer class
data_analyzer = DataAnalyzer()

# Calculate the average rating per month
average_ratings_per_month = data_analyzer.get_average_of_column(cleaned_data, 'overall', 'reviewTime')

# Get the distribution of ratings
ratings_distribution = data_analyzer.get_distribution_of_column(cleaned_data, 'overall')

# Get median and mode of the recommendations
recommendations_median = data_analyzer.get_median_of_column(cleaned_data, 'recommended')
recommendations_mode = data_analyzer.get_mode_of_column(cleaned_data, 'recommended')

# Map the 0s and 1s to 'Not Recommended' and 'Recommended'
cleaned_data['recommended'] = cleaned_data['recommended'].map({0: 'Not Recommended', 1: 'Recommended'})

# Get the distribution of the recommendations
recommendations_distribution = data_analyzer.get_distribution_of_column(cleaned_data, 'recommended')

# Get the distribution of the feedback categories
feedback_category_distribution = data_analyzer.get_distribution_of_column(cleaned_data, 'Feedback Category')
feedback_count_mode = data_analyzer.get_mode_of_column(data, 'total_votes')

# Print Average Rating per Month
print("Average Rating per Month:\n", average_ratings_per_month)

# Print the median and mode of recommendations
print("Median of Recommendations: ", recommendations_median)
print("Mode of Recommendations: ", recommendations_mode)

# Print the mode of the feedback count
print("Mode of Feedback Count: ", feedback_count_mode)

# Create an instance of DataVisualizer class
data_visualizer = DataVisualizer()

# Plot the distribution of ratings
data_visualizer.plot_distribution(ratings_distribution,
                                  title="Distribution of Ratings",
                                  xlabel="Ratings",
                                  ylabel="Count")

# Plot the distribution of recommendations
data_visualizer.plot_pie(recommendations_distribution,
                         title="Distribution of Recommendations")

# Plot the distribution of feedback categories
data_visualizer.plot_pie(feedback_category_distribution, title="Distribution of Feedback Categories")
