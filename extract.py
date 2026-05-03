#extract.py
import requests
import time

BASE_URL = "https://dummyjson.com/products"

def get_paginated(limit=10, retries=3):
    skip = 0

    while True:
        for attempt in range(retries):
            try:
                url = f"{BASE_URL}?limit={limit}&skip={skip}"
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                break
            except Exception as e:
                if attempt == retries - 1:
                    raise
                time.sleep(2)

        data = response.json()
        products = data.get("products", [])

        if not products:
            break

        yield products
        skip += limit