# main.py
import pandas as pd
from extract import get_paginated
from state import get_last_id, save_last_id
from load import save_raw
from transform import build_model
from storage import upload_to_azure

def run_pipeline():
    last_id = get_last_id()

    for page in get_paginated():
        df = pd.DataFrame(page)

        # incremental
        df = df[df["id"] > last_id]

        if df.empty:
            continue

        save_raw(df)

        last_id = df["id"].max()
        save_last_id(last_id)

    build_model()

    upload_to_azure(
        "data/raw/products.parquet",
        "products/products.parquet"
    )

if __name__ == "__main__":
    run_pipeline()