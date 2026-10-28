import pandas as pd

# Load datasets
customers = pd.read_csv("datasets/customers.csv")
orders = pd.read_csv("datasets/orders.csv")
order_items = pd.read_csv("datasets/order_items.csv")
products = pd.read_csv("datasets/products.csv")
payments = pd.read_csv("datasets/payments.csv")
returns = pd.read_csv("datasets/returns.csv")
reviews = pd.read_csv("datasets/customer_reviews.csv")


# ---------- CUSTOMERS ----------
print("\n" + "=" * 60)
print("CUSTOMERS")
print("=" * 60)

print("\nAge statistics:")
print(customers["age"].describe())

print("\nGender:")
print(customers["gender"].value_counts())

print("\nCustomer status:")
print(customers["customer_status"].value_counts())

print("\nLoyalty tier:")
print(customers["loyalty_tier"].value_counts())

print("\nPreferred device:")
print(customers["preferred_device"].value_counts(dropna=False))

print("\nAcquisition channel:")
print(customers["acquisition_channel"].value_counts())

print("\nTop states:")
print(customers["state"].value_counts().head(20))

print("\nTop cities:")
print(customers["city"].value_counts().head(20))

print("\nTotal spend statistics:")
print(customers["total_spend"].describe())


# ---------- ORDERS ----------
print("\n" + "=" * 60)
print("ORDERS")
print("=" * 60)

orders["order_date"] = pd.to_datetime(orders["order_date"])

print("\nDate range:")
print(orders["order_date"].min(), "to", orders["order_date"].max())

print("\nOrder status:")
print(orders["order_status"].value_counts())

print("\nShipping method:")
print(orders["shipping_method"].value_counts())

print("\nMarketing channel:")
print(orders["marketing_channel"].value_counts())

print("\nDiscount statistics:")
print(orders["discount_percentage"].describe())

print("\nFinal amount statistics:")
print(orders["final_amount"].describe())

print("\nDelivery states:")
print(orders["delivery_state"].value_counts().head(20))


# ---------- ORDER ITEMS ----------
print("\n" + "=" * 60)
print("ORDER ITEMS")
print("=" * 60)

print("\nQuantity statistics:")
print(order_items["quantity"].describe())

print("\nUnit price statistics:")
print(order_items["unit_price"].describe())

print("\nRevenue statistics:")
print(order_items["item_revenue"].describe())

print("\nProfit statistics:")
print(order_items["profit"].describe())

print("\nNegative quantities:")
print((order_items["quantity"] < 0).sum())

print("\nZero quantities:")
print((order_items["quantity"] == 0).sum())

print("\nNegative profit:")
print((order_items["profit"] < 0).sum())


# ---------- PRODUCTS ----------
print("\n" + "=" * 60)
print("PRODUCTS")
print("=" * 60)

print("\nProduct types:")
print(products["product_type"].value_counts())

print("\nCategories:")
print(products["category"].value_counts())

print("\nBrands:")
print(products["brand"].value_counts().head(20))

print("\nProduct price statistics:")
print(products["price"].describe())

print("\nProduct rating statistics:")
print(products["rating_average"].describe())

print("\nStock statistics:")
print(products["stock_quantity"].describe())


# ---------- PAYMENTS ----------
print("\n" + "=" * 60)
print("PAYMENTS")
print("=" * 60)

print("\nPayment status:")
print(payments["payment_status"].value_counts())

print("\nPayment method:")
print(payments["payment_method"].value_counts())

print("\nAmount paid statistics:")
print(payments["amount_paid"].describe())

print("\nRefund statistics:")
print(payments["refund_amount"].describe())


# ---------- RETURNS ----------
print("\n" + "=" * 60)
print("RETURNS")
print("=" * 60)

print("\nReturn status:")
print(returns["return_status"].value_counts())

print("\nReturn reasons:")
print(returns["return_reason"].value_counts())

print("\nRefund amount statistics:")
print(returns["refund_amount"].describe())


# ---------- REVIEWS ----------
print("\n" + "=" * 60)
print("REVIEWS")
print("=" * 60)

print("\nRating:")
print(reviews["rating"].value_counts().sort_index())

print("\nSentiment:")
print(reviews["review_sentiment"].value_counts(dropna=False))

print("\nVerified purchase:")
print(reviews["verified_purchase"].value_counts())