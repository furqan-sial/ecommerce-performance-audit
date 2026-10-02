import pandas as pd
import numpy as np

# 1. Simulate raw e-commerce client order data with typical real-world errors
raw_orders = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "customer": ["Ali Khan", "Sara Ahmed", "Zayd Malik", "Fatima Noor", "Ali Khan", "Bilal Tariq", "Sara Ahmed", "Hamza Rauf"],
    "product_category": ["Electronics", "Fashion", "Electronics", "Home & Living", "Electronics", "Fashion", "Fashion", "Beauty"],
    "revenue": [120.50, 45.00, np.nan, 85.00, 120.50, -15.00, 45.00, 210.00],  # NaN missing value & negative refund error
    "ad_channel": ["Meta Ads", "Google Ads", "Organic", "Meta Ads", "Meta Ads", "TikTok Ads", "Google Ads", "Meta Ads"]
}

df = pd.DataFrame(raw_orders)
print("--- RAW INCOMING DATA AUDIT ---")
print(df)
print("\nMissing values detected:\n", df.isnull().sum())
print("Duplicate rows detected:", df.duplicated().sum())

# 2. Clean anomalies (Standard Data Analyst Hygiene)
df_clean = df.drop_duplicates().copy()
df_clean = df_clean[df_clean["revenue"] > 0]  # Remove erroneous negative values/refunds
df_clean["revenue"] = df_clean["revenue"].fillna(df_clean["revenue"].median()) # Impute missing revenue

# 3. Core Business Insight: Revenue & Order Contribution by Channel
channel_performance = df_clean.groupby("ad_channel").agg(
    total_revenue=("revenue", "sum"),
    order_count=("order_id", "count")
).reset_index()

channel_performance["revenue_share_%"] = (channel_performance["total_revenue"] / channel_performance["total_revenue"].sum()) * 100
channel_performance = channel_performance.sort_values(by="total_revenue", ascending=False)

print("\n--- COMMERCIAL AD CHANNEL PERFORMANCE ---")
print(channel_performance.to_string(index=False))