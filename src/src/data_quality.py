import pandas as pd

# Load datasets
customers = pd.read_csv("datasets/customers.csv")
orders = pd.read_csv("datasets/orders.csv")
order_items = pd.read_csv("datasets/order_items.csv")
products = pd.read_csv("datasets/products.csv")
payments = pd.read_csv("datasets/payments.csv")
returns = pd.read_csv("datasets/returns.csv")
reviews = pd.read_csv("datasets/customer_reviews.csv")

print("\n========== RELATIONSHIP CHECK ==========\n")

print("Orders with missing customers:",
      (~orders["customer_id"].isin(customers["customer_id"])).sum())

print("Order items with missing orders:",
      (~order_items["order_id"].isin(orders["order_id"])).sum())

print("Order items with missing products:",
      (~order_items["product_id"].isin(products["product_id"])).sum())

print("Payments with missing orders:",
      (~payments["order_id"].isin(orders["order_id"])).sum())

print("Returns with missing orders:",
      (~returns["order_id"].isin(orders["order_id"])).sum())

print("Reviews with missing orders:",
      (~reviews["order_id"].isin(orders["order_id"])).sum())

print("Reviews with missing customers:",
      (~reviews["customer_id"].isin(customers["customer_id"])).sum())

print("\n========== UNIQUE VALUES ==========\n")

print("Order statuses:")
print(orders["order_status"].value_counts())

print("\nPayment statuses:")
print(payments["payment_status"].value_counts())

print("\nPayment methods:")
print(payments["payment_method"].value_counts())

print("\nProduct categories:")
print(products["category"].value_counts())

print("\nCustomer segments:")
print(customers["customer_segment"].value_counts())

print("\nCustomer states:")
print(customers["state"].nunique())

print("\nCustomer cities:")
print(customers["city"].nunique())

print("\nReturn reasons:")
print(returns["return_reason"].value_counts())

print("\nReview ratings:")
print(reviews["rating"].value_counts())

print("\nReview sentiments:")
print(reviews["review_sentiment"].value_counts())