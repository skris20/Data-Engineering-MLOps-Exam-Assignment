# Filename: beer_features.py

import pandas as pd
import numpy as np
from datetime import datetime

def average_ratings(df, rating_columns):
    """Calculate average ratings for specified columns."""
    df['average_rating'] = df[rating_columns].mean(axis=1)
    return df

def review_count(df, group_by_column):
    """Count the number of reviews for each unique item in the specified column."""
    review_counts = df.groupby(group_by_column).size().reset_index(name='review_count')
    return review_counts

def parse_dates(df, date_column):
    """Convert timestamps to datetime objects."""
    df[date_column] = pd.to_datetime(df[date_column], unit='s')
    return df

def clean_text(df, text_column):
    """Preprocess text data."""
    df[text_column] = df[text_column].str.lower().str.replace(r'[^\w\s]', '')
    return df

def convert_to_datetime(date_series):
    return pd.to_datetime(date_series, unit='s', errors='coerce')

# Example function to integrate multiple features at once
def prepare_features(df):
    """Run multiple feature preparation steps."""
    df = parse_dates(df, 'review/time')
    df = average_ratings(df, ['review/appearance', 'review/aroma', 'review/palate', 'review/taste'])
    df = clean_text(df, 'review/text')
    return df