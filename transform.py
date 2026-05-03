#transfor.py
import pandas as pd
import os

def build_model():
    df = pd.read_parquet("data/raw/products.parquet")

    df = df[["id", "title", "category", "price"]]

    df = df.drop_duplicates()
    df = df.dropna(subset=["id", "price"])

    df.columns = df.columns.str.lower()

    dim_product = df[["id", "title", "category"]]
    fact_sales = df[["id", "price"]]

    os.makedirs("data/processed", exist_ok=True)

    dim_product.to_parquet("data/processed/dim_product.parquet", index=False)
    fact_sales.to_parquet("data/processed/fact_sales.parquet", index=False)