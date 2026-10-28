import pandas as pd
import os

# -----------------------------------
# Load data
# -----------------------------------
df = pd.read_csv("outputs/features/retailiq_features.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# -----------------------------------
# Create customer-level dataset
# -----------------------------------
customer_data = df.groupby("customer_id").agg(
    recency=("order_date", lambda x: (
        df["order_date"].max() - x.max()
    ).days),

    frequency=("order_id", "nunique"),

    monetary=("revenue", "sum"),

    total_quantity=("quantity", "sum"),

    average_order_value=("final_amount", "mean"),

    average_profit=("item_profit", "mean"),

    customer_age=("customer_age", "first"),

    gender=("gender", "first"),

    state=("state", "first"),

    city=("city", "first"),

    loyalty_tier=("loyalty_tier", "first"),

    customer_status=("customer_status", "first"),

    preferred_device=("preferred_device", "first"),

    acquisition_channel=("acquisition_channel", "first")
).reset_index()


# -----------------------------------
# RFM Scores
# -----------------------------------

# Recency: lower is better
customer_data["R_score"] = pd.qcut(
    customer_data["recency"],
    5,
    labels=[5, 4, 3, 2, 1],
    duplicates="drop"
)

# Frequency: higher is better
customer_data["F_score"] = pd.qcut(
    customer_data["frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

# Monetary: higher is better
customer_data["M_score"] = pd.qcut(
    customer_data["monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

# Convert scores to integers
customer_data["R_score"] = customer_data["R_score"].astype(int)
customer_data["F_score"] = customer_data["F_score"].astype(int)
customer_data["M_score"] = customer_data["M_score"].astype(int)

# Combined RFM score
customer_data["RFM_score"] = (
    customer_data["R_score"]
    + customer_data["F_score"]
    + customer_data["M_score"]
)


# -----------------------------------
# Customer segments
# -----------------------------------

def classify_customer(row):

    if (
        row["R_score"] >= 4
        and row["F_score"] >= 4
        and row["M_score"] >= 4
    ):
        return "Champions"

    elif (
        row["R_score"] >= 3
        and row["F_score"] >= 3
    ):
        return "Loyal Customers"

    elif (
        row["R_score"] >= 4
        and row["F_score"] <= 2
    ):
        return "New Customers"

    elif (
        row["R_score"] <= 2
        and row["F_score"] >= 3
    ):
        return "At Risk"

    elif (
        row["R_score"] <= 2
        and row["M_score"] >= 4
    ):
        return "High Value At Risk"

    else:
        return "Regular Customers"


customer_data["RFM_segment"] = customer_data.apply(
    classify_customer,
    axis=1
)


# -----------------------------------
# Save customer analysis
# -----------------------------------

os.makedirs("outputs/customer_analysis", exist_ok=True)

output_file = (
    "outputs/customer_analysis/customer_rfm.csv"
)

customer_data.to_csv(
    output_file,
    index=False
)


# -----------------------------------
# Display results
# -----------------------------------

print("=" * 60)
print("CUSTOMER RFM ANALYSIS COMPLETED")
print("=" * 60)

print("\nCustomer dataset shape:")
print(customer_data.shape)

print("\nRFM Segment Distribution:")
print(
    customer_data["RFM_segment"]
    .value_counts()
)

print("\nAverage RFM metrics:")
print(
    customer_data[
        [
            "recency",
            "frequency",
            "monetary"
        ]
    ].mean()
)

print("\nTop 10 customers by monetary value:")

print(
    customer_data[
        [
            "customer_id",
            "recency",
            "frequency",
            "monetary",
            "RFM_score",
            "RFM_segment"
        ]
    ]
    .sort_values("monetary", ascending=False)
    .head(10)
)

print("\nSaved to:")
print(output_file)