#load.py
import pandas as pd
import os

RAW_PATH = "data/raw/products.parquet"

def save_raw(df):
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(RAW_PATH):
        df.to_parquet(RAW_PATH, index=False, engine="pyarrow", compression="snappy")
    else:
        df.to_parquet(RAW_PATH, index=False)