import pandas as pd
import os

def load_raw_data(path="data/raw/loan_data.csv"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    return df