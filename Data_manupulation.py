import pandas as pd
import requests

csv_url = ('/Users/akshaykathuria/Documents/Data Sets/netflix_titles.csv')

try:
    df = pd.read_csv('/Users/akshaykathuria/Documents/Data Sets/netflix_titles.csv')
    rating_map = {'TV-MA': 3.3, 'TV-14': 6.6, 'Other': 9.9}
    df['rating'] = df['rating'].map(rating_map)
    # Replace null values in the 'rating' column with 0
    df['rating'].fillna(0, inplace=True)
    df.to_csv('modified_csv_file1.csv', index=False)
    print("CSV file processed successfully.")
except Exception as e:
    print(f"Error occurred: {e}"
