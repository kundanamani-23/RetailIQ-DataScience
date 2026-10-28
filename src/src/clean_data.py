import pandas as pd
import os

# -----------------------------
# Load raw datasets
# -----------------------------
base_path = "datasets"

customers = pd.read_csv(f"{base_path}/customers.csv")
orders = pd.read_csv(f"{base_path}/orders.csv")
order_items = pd.read_csv(f"{base_path}/order_items.csv")
products = pd.read_csv(f"{base_path}/products.csv")
payments = pd.read_csv(f"{base_path}/payments.csv")
returns = pd.read_csv(f"{base_path}/returns.csv")
reviews = pd.read_csv(f"{base_path}/customer_reviews.csv")


# -----------------------------
# Convert date columns
# -----------------------------
customers["customer_signup_date"] = pd.to_datetime(
    customers["customer_signup_date"]
)
customers["last_order_date"] = pd.to_datetime(
    customers["last_order_date"]
)

orders["order_date"] = pd.to_datetime(orders["order_date"])

payments["payment_date"] = pd.to_datetime(payments["payment_date"])

returns["return_date"] = pd.to_datetime(returns["return_date"])

reviews["review_date"] = pd.to_datetime(reviews["review_date"])

products["product_launch_date"] = pd.to_datetime(
    products["product_launch_date"]
)


# -----------------------------
# Customers cleaning
# -----------------------------

# Fill missing age using median age
customers["age"] = customers["age"].fillna(
    customers["age"].median()
)

# Missing device = Unknown
customers["preferred_device"] = customers["preferred_device"].fillna(
    "Unknown"
)


# -----------------------------
# Orders cleaning
# -----------------------------

# Missing coupon means no coupon was used
orders["coupon_code"] = orders["coupon_code"].fillna(
    "No Coupon"
)

# Missing campaign means no campaign was associated
orders["campaign_id"] = orders["campaign_id"].fillna(
    "No Campaign"
)


# -----------------------------
# Products cleaning
# -----------------------------

# Fill missing product ratings with overall median
products["rating_average"] = products["rating_average"].fillna(
    products["rating_average"].median()
)


# -----------------------------
# Reviews cleaning
# -----------------------------

# Derive missing sentiment from rating
def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"


reviews["review_sentiment"] = reviews["review_sentiment"].fillna(
    reviews["rating"].apply(get_sentiment)
)


# -----------------------------
# Create output folder
# -----------------------------
output_path = "outputs/cleaned"

os.makedirs(output_path, exist_ok=True)


# -----------------------------
# Save cleaned datasets
# -----------------------------
customers.to_csv(
    f"{output_path}/customers_cleaned.csv", index=False
)

orders.to_csv(
    f"{output_path}/orders_cleaned.csv", index=False
)

order_items.to_csv(
    f"{output_path}/order_items_cleaned.csv", index=False
)

products.to_csv(
    f"{output_path}/products_cleaned.csv", index=False
)

payments.to_csv(
    f"{output_path}/payments_cleaned.csv", index=False
)

returns.to_csv(
    f"{output_path}/returns_cleaned.csv", index=False
)

reviews.to_csv(
    f"{output_path}/customer_reviews_cleaned.csv", index=False
)


# -----------------------------
# Final check
# -----------------------------
print("=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print("\nRemaining missing values:")

datasets = {
    "Customers": customers,
    "Orders": orders,
    "Order Items": order_items,
    "Products": products,
    "Payments": payments,
    "Returns": returns,
    "Reviews": reviews
}

for name, df in datasets.items():
    missing = df.isnull().sum().sum()
    print(f"{name}: {missing}")

print("\nCleaned files saved in:")
print("outputs/cleaned/")