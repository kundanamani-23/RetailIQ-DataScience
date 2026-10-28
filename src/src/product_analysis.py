import pandas as pd
import os
import matplotlib.pyplot as plt


# -----------------------------------
# Load feature dataset
# -----------------------------------
df = pd.read_csv(
    "outputs/features/retailiq_features.csv"
)


# -----------------------------------
# Product-level analysis
# -----------------------------------
product_analysis = df.groupby(
    [
        "product_id",
        "product_name",
        "category",
        "subcategory",
        "brand"
    ]
).agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("revenue", "sum"),
    total_profit=("item_profit", "sum"),
    average_rating=("rating_average", "mean"),
    rating_count=("rating_count", "max"),
    stock_quantity=("stock_quantity", "max")
).reset_index()


# -----------------------------------
# Product profit margin
# -----------------------------------
product_analysis["profit_margin"] = (
    product_analysis["total_profit"]
    / product_analysis["total_revenue"]
    * 100
)

product_analysis["profit_margin"] = (
    product_analysis["profit_margin"]
    .replace([float("inf"), float("-inf")], 0)
)


# -----------------------------------
# Category analysis
# -----------------------------------
category_analysis = df.groupby("category").agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("revenue", "sum"),
    total_profit=("item_profit", "sum"),
    average_rating=("rating_average", "mean")
).reset_index()

category_analysis["profit_margin"] = (
    category_analysis["total_profit"]
    / category_analysis["total_revenue"]
    * 100
)


# -----------------------------------
# Brand analysis
# -----------------------------------
brand_analysis = df.groupby("brand").agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("revenue", "sum"),
    total_profit=("item_profit", "sum")
).reset_index()

brand_analysis["profit_margin"] = (
    brand_analysis["total_profit"]
    / brand_analysis["total_revenue"]
    * 100
)


# -----------------------------------
# Save results
# -----------------------------------
os.makedirs(
    "outputs/product_analysis",
    exist_ok=True
)

product_analysis.to_csv(
    "outputs/product_analysis/product_performance.csv",
    index=False
)

category_analysis.to_csv(
    "outputs/product_analysis/category_performance.csv",
    index=False
)

brand_analysis.to_csv(
    "outputs/product_analysis/brand_performance.csv",
    index=False
)


# -----------------------------------
# Top 10 products
# -----------------------------------
top_products = product_analysis.sort_values(
    "total_revenue",
    ascending=False
).head(10)

print("=" * 60)
print("PRODUCT INTELLIGENCE COMPLETED")
print("=" * 60)

print("\nTop 10 Products by Revenue:")
print(
    top_products[
        [
            "product_name",
            "category",
            "total_quantity",
            "total_revenue",
            "total_profit"
        ]
    ].to_string(index=False)
)


# -----------------------------------
# Top categories
# -----------------------------------
print("\nTop Categories by Revenue:")

print(
    category_analysis
    .sort_values("total_revenue", ascending=False)
    [
        [
            "category",
            "total_quantity",
            "total_revenue",
            "total_profit",
            "profit_margin"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


# -----------------------------------
# Loss-making products
# -----------------------------------
loss_products = product_analysis[
    product_analysis["total_profit"] < 0
].sort_values("total_profit")

print("\nLoss-Making Products:")
print(f"Total: {len(loss_products)}")

print(
    loss_products[
        [
            "product_name",
            "category",
            "total_revenue",
            "total_profit"
        ]
    ].head(10).to_string(index=False)
)


# -----------------------------------
# Create product revenue chart
# -----------------------------------
plt.figure(figsize=(12, 6))

top_products.sort_values(
    "total_revenue"
).plot(
    x="product_name",
    y="total_revenue",
    kind="barh",
    legend=False
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    "outputs/product_analysis/top_products.png"
)

plt.close()


print("\nFiles saved in:")
print("outputs/product_analysis/")