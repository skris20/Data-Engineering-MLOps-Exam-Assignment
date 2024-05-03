import pandas as pd
import numpy as np
import gdown
from datetime import datetime, date

def download_data(url, output_path):
    gdown.download(url, output_path, quiet=False)
    return output_path

def load_data(file_path):
    columns = ['beer/name', 'beer/beerId', 'beer/brewerId', 'beer/ABV', 'beer/style',
               'review/appearance', 'review/aroma', 'review/palate', 'review/taste',
               'review/overall', 'review/time', 'review/profileName', 'review/text']
    data = {col: [] for col in columns}
    with open(file_path, "r", encoding="ISO-8859-1") as file:
        current_review = {}
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(": ", 1)
                if len(parts) >= 2:  # Ensure there are at least two parts
                    key = parts[0]
                    value = ': '.join(parts[1:])  # Rejoin the remaining parts into the value
                    current_review[key] = value
                else:
                    print(f"Skipping line: {line}")  # Skip lines with unexpected format
            else:
                if current_review:
                    for col in columns:
                        data[col].append(current_review.get(col, np.nan))
                    current_review = {}
        if current_review:  # Check outside the loop for any last entry
            for col in columns:
                data[col].append(current_review.get(col, np.nan))
    return pd.DataFrame(data)