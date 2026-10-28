import pandas as pd
import os


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "outputs/features/retailiq_features.csv"
)


# ==========================================
# OUTPUT FOLDER
# ==========================================

os.makedirs(
    "outputs/geography_analysis",
    exist_ok=True
)


# ==========================================
# STATE ANALYSIS
# ==========================================

state_analysis = df.groupby(
    "delivery_state"
).agg(
    orders=("order_id", "nunique"),
    customers=("customer_id", "nunique"),
    quantity_sold=("quantity", "sum"),
    revenue=("revenue", "sum"),
    profit=("item_profit", "sum")
).reset_index()


state_analysis["profit_margin"] = (
    state_analysis["profit"]
    / state_analysis["revenue"]
    * 100
)

state_analysis = state_analysis.sort_values(
    "revenue",
    ascending=False
)


# ==========================================
# CITY ANALYSIS
# ==========================================

city_analysis = df.groupby(
    [
        "delivery_state",
        "delivery_city"
    ]
).agg(
    orders=("order_id", "nunique"),
    customers=("customer_id", "nunique"),
    quantity_sold=("quantity", "sum"),
    revenue=("revenue", "sum"),
    profit=("item_profit", "sum")
).reset_index()


city_analysis["profit_margin"] = (
    city_analysis["profit"]
    / city_analysis["revenue"]
    * 100
)

city_analysis = city_analysis.sort_values(
    "revenue",
    ascending=False
)


# ==========================================
# CUSTOMER STATE ANALYSIS
# ==========================================

customer_state = df.groupby(
    "state"
).agg(
    customers=("customer_id", "nunique"),
    total_spend=("total_spend", "sum"),
    average_customer_spend=("total_spend", "mean")
).reset_index()

customer_state = customer_state.sort_values(
    "total_spend",
    ascending=False
)


# ==========================================
# SAVE FILES
# ==========================================

state_analysis.to_csv(
    "outputs/geography_analysis/"
    "state_performance.csv",
    index=False
)

city_analysis.to_csv(
    "outputs/geography_analysis/"
    "city_performance.csv",
    index=False
)

customer_state.to_csv(
    "outputs/geography_analysis/"
    "customer_state_analysis.csv",
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 60)
print("INDIA GEOGRAPHY ANALYSIS COMPLETED")
print("=" * 60)


print("\nTop States by Revenue:")

print(
    state_analysis[
        [
            "delivery_state",
            "orders",
            "customers",
            "revenue",
            "profit",
            "profit_margin"
        ]
    ]
    .head(15)
    .to_string(index=False)
)


print("\nTop Cities by Revenue:")

print(
    city_analysis[
        [
            "delivery_state",
            "delivery_city",
            "orders",
            "customers",
            "revenue",
            "profit"
        ]
    ]
    .head(15)
    .to_string(index=False)
)


print("\nTop States by Customer Spend:")

print(
    customer_state.head(15)
    .to_string(index=False)
)


print("\nFiles saved in:")
print("outputs/geography_analysis/")