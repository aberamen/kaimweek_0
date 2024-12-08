import pandas as pd

def clean_data(data):
    # Example: Fill missing values
    data.fillna(0, inplace=True)
    return data
