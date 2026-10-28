import pandas as pd
import os


# ==========================================
# LOAD DATA
# ==========================================

orders = pd.read_csv(
    "outputs/cleaned/orders_cleaned.csv"
)

returns = pd.read_csv(
    "outputs/cleaned/returns_cleaned.csv"
)

payments = pd.read_csv(
    "outputs/cleaned/payments_cleaned.csv"
)

reviews = pd.read_csv(
    "outputs/cleaned/customer_reviews_cleaned.csv"
)

order_items = pd.read_csv(
    "outputs/cleaned/order_items_cleaned.csv"
)

products = pd.read_csv(
    "outputs/cleaned/products_cleaned.csv"
)


# ==========================================
# OUTPUT FOLDER
# ==========================================

os.makedirs(
    "outputs/operations_analysis",
    exist_ok=True
)


# ==========================================
# 1. RETURN ANALYSIS
# ==========================================

# Overall return rate
total_orders = orders["order_id"].nunique()
total_returns = returns["return_id"].nunique()

return_rate = (
    total_returns / total_orders * 100
)

print("=" * 60)
print("RETAILIQ OPERATIONS ANALYSIS")
print("=" * 60)

print("\nRETURN ANALYSIS")

print(f"Total Orders: {total_orders}")
print(f"Total Returns: {total_returns}")
print(f"Overall Return Rate: {return_rate:.2f}%")


# Return reasons
return_reasons = (
    returns["return_reason"]
    .value_counts()
    .reset_index()
)

return_reasons.columns = [
    "return_reason",
    "return_count"
]

return_reasons.to_csv(
    "outputs/operations_analysis/"
    "return_reasons.csv",
    index=False
)


print("\nTop Return Reasons:")
print(return_reasons)


# Return status
return_status = (
    returns["return_status"]
    .value_counts()
    .reset_index()
)

return_status.columns = [
    "return_status",
    "return_count"
]

return_status.to_csv(
    "outputs/operations_analysis/"
    "return_status.csv",
    index=False
)


# ==========================================
# 2. CATEGORY RETURN ANALYSIS
# ==========================================

return_product = returns.merge(
    products[
        [
            "product_id",
            "product_name",
            "category"
        ]
    ],
    on="product_id",
    how="left"
)

category_returns = (
    return_product
    .groupby("category")
    .agg(
        total_returns=("return_id", "count"),
        total_refund=("refund_amount", "sum")
    )
    .reset_index()
    .sort_values(
        "total_returns",
        ascending=False
    )
)

category_returns.to_csv(
    "outputs/operations_analysis/"
    "category_returns.csv",
    index=False
)

print("\nReturns by Category:")
print(category_returns)


# ==========================================
# 3. PAYMENT ANALYSIS
# ==========================================

payment_method = (
    payments
    .groupby("payment_method")
    .agg(
        transactions=("payment_id", "count"),
        amount_paid=("amount_paid", "sum"),
        refund_amount=("refund_amount", "sum")
    )
    .reset_index()
    .sort_values(
        "transactions",
        ascending=False
    )
)

payment_method.to_csv(
    "outputs/operations_analysis/"
    "payment_methods.csv",
    index=False
)

print("\nPAYMENT ANALYSIS")
print(payment_method)


# Payment status
payment_status = (
    payments["payment_status"]
    .value_counts()
    .reset_index()
)

payment_status.columns = [
    "payment_status",
    "transactions"
]

payment_status.to_csv(
    "outputs/operations_analysis/"
    "payment_status.csv",
    index=False
)

print("\nPayment Status:")
print(payment_status)


# ==========================================
# 4. REVIEW ANALYSIS
# ==========================================

rating_summary = (
    reviews["rating"]
    .value_counts()
    .sort_index()
    .reset_index()
)

rating_summary.columns = [
    "rating",
    "review_count"
]

rating_summary.to_csv(
    "outputs/operations_analysis/"
    "rating_summary.csv",
    index=False
)

print("\nREVIEW ANALYSIS")

print("\nRating Distribution:")
print(rating_summary)


# Sentiment
sentiment_summary = (
    reviews["review_sentiment"]
    .value_counts()
    .reset_index()
)

sentiment_summary.columns = [
    "sentiment",
    "review_count"
]

sentiment_summary.to_csv(
    "outputs/operations_analysis/"
    "sentiment_summary.csv",
    index=False
)

print("\nSentiment Distribution:")
print(sentiment_summary)


# ==========================================
# 5. CATEGORY REVIEW ANALYSIS
# ==========================================

review_product = reviews.merge(
    products[
        [
            "product_id",
            "category"
        ]
    ],
    on="product_id",
    how="left"
)

category_reviews = (
    review_product
    .groupby("category")
    .agg(
        review_count=("review_id", "count"),
        average_rating=("rating", "mean")
    )
    .reset_index()
    .sort_values(
        "average_rating",
        ascending=False
    )
)

category_reviews.to_csv(
    "outputs/operations_analysis/"
    "category_reviews.csv",
    index=False
)

print("\nCategory Review Performance:")
print(category_reviews)


# ==========================================
# 6. VERIFIED PURCHASE ANALYSIS
# ==========================================

verified = (
    reviews["verified_purchase"]
    .value_counts()
    .reset_index()
)

verified.columns = [
    "verified_purchase",
    "review_count"
]

verified.to_csv(
    "outputs/operations_analysis/"
    "verified_reviews.csv",
    index=False
)

print("\nVerified Purchase Reviews:")
print(verified)


# ==========================================
# FINAL
# ==========================================

print("\n" + "=" * 60)
print("OPERATIONS ANALYSIS COMPLETED")
print("=" * 60)

print("\nFiles saved in:")
print("outputs/operations_analysis/")