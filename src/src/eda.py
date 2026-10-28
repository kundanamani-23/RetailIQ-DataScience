import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------
# Load feature dataset
# -----------------------------------
df = pd.read_csv("outputs/features/retailiq_features.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# Create output folder
output_path = "outputs/eda"
os.makedirs(output_path, exist_ok=True)


# -----------------------------------
# 1. MONTHLY REVENUE
# -----------------------------------
monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

plt.figure(figsize=(12, 6))
monthly_revenue.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_path}/monthly_revenue.png")
plt.close()


# -----------------------------------
# 2. MONTHLY PROFIT
# -----------------------------------
monthly_profit = (
    df.groupby(df["order_date"].dt.to_period("M"))["item_profit"]
    .sum()
)

plt.figure(figsize=(12, 6))
monthly_profit.plot(marker="o")
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_path}/monthly_profit.png")
plt.close()


# -----------------------------------
# 3. ORDER STATUS
# -----------------------------------
status_counts = df.drop_duplicates("order_id")["order_status"].value_counts()

plt.figure(figsize=(8, 5))
status_counts.plot(kind="bar")
plt.title("Orders by Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_path}/order_status.png")
plt.close()


# -----------------------------------
# 4. REVENUE BY CATEGORY
# -----------------------------------
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(f"{output_path}/category_revenue.png")
plt.close()


# -----------------------------------
# 5. PROFIT BY CATEGORY
# -----------------------------------
category_profit = (
    df.groupby("category")["item_profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
category_profit.plot(kind="bar")
plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(f"{output_path}/category_profit.png")
plt.close()


# -----------------------------------
# 6. TOP 10 PRODUCTS BY REVENUE
# -----------------------------------
top_products = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(f"{output_path}/top_products_revenue.png")
plt.close()


# -----------------------------------
# 7. TOP 10 STATES BY REVENUE
# -----------------------------------
state_revenue = (
    df.groupby("delivery_state")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
state_revenue.sort_values().plot(kind="barh")
plt.title("Top 10 States by Revenue")
plt.xlabel("Revenue")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(f"{output_path}/state_revenue.png")
plt.close()


# -----------------------------------
# 8. PAYMENT METHOD
# -----------------------------------
payments = pd.read_csv("outputs/cleaned/payments_cleaned.csv")

payment_counts = payments["payment_method"].value_counts()

plt.figure(figsize=(10, 6))
payment_counts.plot(kind="bar")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_path}/payment_methods.png")
plt.close()


# -----------------------------------
# 9. RETURN REASONS
# -----------------------------------
returns = pd.read_csv("outputs/cleaned/returns_cleaned.csv")

return_reasons = returns["return_reason"].value_counts()

plt.figure(figsize=(10, 6))
return_reasons.sort_values().plot(kind="barh")
plt.title("Return Reasons")
plt.xlabel("Number of Returns")
plt.ylabel("Return Reason")
plt.tight_layout()
plt.savefig(f"{output_path}/return_reasons.png")
plt.close()


# -----------------------------------
# 10. CUSTOMER LOYALTY
# -----------------------------------
customer_loyalty = (
    df.drop_duplicates("customer_id")["loyalty_tier"]
    .value_counts()
)

plt.figure(figsize=(8, 5))
customer_loyalty.plot(kind="bar")
plt.title("Customer Loyalty Tier Distribution")
plt.xlabel("Loyalty Tier")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig(f"{output_path}/loyalty_distribution.png")
plt.close()


# -----------------------------------
# 11. CUSTOMER STATUS
# -----------------------------------
customer_status = (
    df.drop_duplicates("customer_id")["customer_status"]
    .value_counts()
)

plt.figure(figsize=(8, 5))
customer_status.plot(kind="bar")
plt.title("Customer Status Distribution")
plt.xlabel("Customer Status")
plt.ylabel("Customers")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{output_path}/customer_status.png")
plt.close()


# -----------------------------------
# 12. RATING DISTRIBUTION
# -----------------------------------
reviews = pd.read_csv(
    "outputs/cleaned/customer_reviews_cleaned.csv"
)

rating_counts = reviews["rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{output_path}/rating_distribution.png")
plt.close()


# -----------------------------------
# SUMMARY
# -----------------------------------
print("=" * 60)
print("EDA COMPLETED")
print("=" * 60)

print("\nCharts created:")

charts = [
    "monthly_revenue.png",
    "monthly_profit.png",
    "order_status.png",
    "category_revenue.png",
    "category_profit.png",
    "top_products_revenue.png",
    "state_revenue.png",
    "payment_methods.png",
    "return_reasons.png",
    "loyalty_distribution.png",
    "customer_status.png",
    "rating_distribution.png"
]

for chart in charts:
    print("-", chart)

print("\nSaved in:")
print("outputs/eda/")