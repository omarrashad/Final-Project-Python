class DataAnalyzer:
    def get_average_of_column(self, data, column, group_by_column):
        # We group the data by group_by_column and calculate average of the column
        return data.groupby(group_by_column)[column].mean()

    def get_distribution_of_column(self, data, column):
        # return data distribution calculated using value_counts
        return data[column].value_counts(normalize=True)

    def get_median_of_column(self, data, column):
        # return the median value of the column
        return data[column].median()

    def get_mode_of_column(self, data, column):
        # return the mode value of the column
        return data[column].mode()[0]
