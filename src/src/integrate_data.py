import pandas as pd
import os

# -----------------------------------
# Load cleaned datasets
# -----------------------------------
base_path = "outputs/cleaned"

customers = pd.read_csv(f"{base_path}/customers_cleaned.csv")
orders = pd.read_csv(f"{base_path}/orders_cleaned.csv")
order_items = pd.read_csv(f"{base_path}/order_items_cleaned.csv")
products = pd.read_csv(f"{base_path}/products_cleaned.csv")
payments = pd.read_csv(f"{base_path}/payments_cleaned.csv")
returns = pd.read_csv(f"{base_path}/returns_cleaned.csv")
reviews = pd.read_csv(f"{base_path}/customer_reviews_cleaned.csv")


# -----------------------------------
# Convert dates
# -----------------------------------
orders["order_date"] = pd.to_datetime(orders["order_date"])
customers["customer_signup_date"] = pd.to_datetime(
    customers["customer_signup_date"]
)
customers["last_order_date"] = pd.to_datetime(
    customers["last_order_date"]
)
products["product_launch_date"] = pd.to_datetime(
    products["product_launch_date"]
)


# -----------------------------------
# Merge Orders + Customers
# -----------------------------------
master = orders.merge(
    customers,
    on="customer_id",
    how="left",
    suffixes=("", "_customer")
)

print("After Customers merge:", master.shape)


# -----------------------------------
# Merge Order Items
# -----------------------------------
master = master.merge(
    order_items,
    on="order_id",
    how="left",
    suffixes=("", "_item")
)

print("After Order Items merge:", master.shape)


# -----------------------------------
# Merge Products
# -----------------------------------
master = master.merge(
    products,
    on="product_id",
    how="left",
    suffixes=("", "_product")
)

print("After Products merge:", master.shape)


# -----------------------------------
# Create output folder
# -----------------------------------
os.makedirs("outputs/integrated", exist_ok=True)


# -----------------------------------
# Save master dataset
# -----------------------------------
master.to_csv(
    "outputs/integrated/retailiq_master.csv",
    index=False
)


# -----------------------------------
# Display information
# -----------------------------------
print("\n" + "=" * 60)
print("INTEGRATION COMPLETED")
print("=" * 60)

print("\nMaster dataset shape:")
print(master.shape)

print("\nMaster dataset columns:")
for column in master.columns:
    print("-", column)

print("\nMissing values in master dataset:")
print(master.isnull().sum().sort_values(ascending=False).head(10))

print("\nSaved to:")
print("outputs/integrated/retailiq_master.csv")