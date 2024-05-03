import pandas as pd
import numpy as np
import gdown
from datetime import datetime, date
from ..data_utils import download_data, load_data


def preprocess_data(df):
    df.rename(columns=lambda x: x.replace('/', '_').replace('beer/', 'beer_'), inplace=True)
    numeric_cols = ['beer_abv', 'review_appearance', 'review_aroma', 'review_palate', 'review_taste', 'review_overall']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    id_cols = ['beer_beerid', 'beer_brewerid']
    df[id_cols] = df[id_cols].apply(pd.to_numeric, errors='coerce', downcast='integer')
    df['review_time'] = pd.to_datetime(df['review_time'], errors='coerce')
    return df