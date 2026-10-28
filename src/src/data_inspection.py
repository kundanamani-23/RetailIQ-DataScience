import pandas as pd
import os

DATASET_PATH = "datasets"

files = [
    "customers.csv",
    "orders.csv",
    "order_items.csv",
    "products.csv",
    "payments.csv",
    "returns.csv",
    "customer_reviews.csv"
]

for file in files:
    path = os.path.join(DATASET_PATH, file)
    df = pd.read_csv(path)

    print("\n" + "=" * 70)
    print(file)
    print("=" * 70)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nFirst 3 Rows:")
    print(df.head(3))