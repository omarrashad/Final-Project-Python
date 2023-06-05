import pandas as pd


class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        # Load the data from the CSV file using Pandas
        data = pd.read_csv(self.file_path)
        return data

    def clean_data(self, data):
        # # Fill missing values
        # data['reviewerName'].fillna('Anonymous', inplace=True)
        # data['reviewText'].fillna('No review text provided', inplace=True)

        # Clean the data by removing rows with missing values
        data.dropna(inplace=True)

        # Remove any duplicates
        data.drop_duplicates(inplace=True)

        # Convert 'helpful' from string format "[n, m]" to two separate columns 'helpful_votes' and 'total_votes'
        data[['helpful_votes', 'total_votes']] = data['helpful'].str.strip('[]').str.split(',', expand=True)
        data.drop(columns='helpful', inplace=True)

        # Convert 'helpful_votes' and 'total_votes' to int
        data['helpful_votes'] = data['helpful_votes'].astype(int)
        data['total_votes'] = data['total_votes'].astype(int)

        # Convert 'reviewTime' to datetime format
        data['reviewTime'] = pd.to_datetime(data['reviewTime'])

        return data
