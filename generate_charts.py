import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Simulation
raw_orders = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "customer": ["Ali Khan", "Sara Ahmed", "Zayd Malik", "Fatima Noor", "Ali Khan", "Bilal Tariq", "Sara Ahmed", "Hamza Rauf"],
    "product_category": ["Electronics", "Fashion", "Electronics", "Home & Living", "Electronics", "Fashion", "Fashion", "Beauty"],
    "revenue": [120.50, 45.00, np.nan, 85.00, 120.50, -15.00, 45.00, 210.00],
    "ad_channel": ["Meta Ads", "Google Ads", "Organic", "Meta Ads", "Meta Ads", "TikTok Ads", "Google Ads", "Meta Ads"]
}

df = pd.DataFrame(raw_orders)

# 2. Hygiene & Imputation
df_clean = df.drop_duplicates().copy()
df_clean = df_clean[df_clean["revenue"] > 0]
df_clean["revenue"] = df_clean["revenue"].fillna(df_clean["revenue"].median())

# 3. Channel Aggregation
channel_perf = df_clean.groupby("ad_channel").agg(
    total_revenue=("revenue", "sum"),
    order_count=("order_id", "count")
).reset_index().sort_values(by="total_revenue", ascending=False)

# 4. Generate Professional Visual
sns.set_theme(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(8, 4.5), dpi=300)

palette = ["#1f77b4", "#ff7f0e"]
bars = sns.barplot(data=channel_perf, x="ad_channel", y="total_revenue", hue="ad_channel", palette=palette, ax=ax1, width=0.45, legend=False)
# Direct data labeling
for bar in bars.patches:
    ax1.annotate(f"${bar.get_height():,.2f}",
                 (bar.get_x() + bar.get_width() / 2, bar.get_height() / 2),
                 ha='center', va='center', color='white', fontweight='bold', fontsize=12)

ax1.set_title("E-Commerce Revenue Distribution by Acquisition Channel", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Ad Channel", fontsize=11, labelpad=10)
ax1.set_ylabel("Total Revenue ($)", fontsize=11, labelpad=10)
sns.despine(top=True, right=True)

plt.tight_layout()
output_path = "assets/channel_revenue_breakdown.png"
plt.savefig(output_path)
print(f"Chart successfully saved to {output_path}")