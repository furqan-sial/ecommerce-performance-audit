import sqlite3
import pandas as pd

# 1. Establish in-memory relational database
conn = sqlite3.connect(":memory:")

# 2. Seed clean transactional schema
transactions = pd.DataFrame({
    "order_id": [1001, 1002, 1004, 1005, 1007, 1008],
    "customer": ["Ali Khan", "Sara Ahmed", "Fatima Noor", "Ali Khan", "Sara Ahmed", "Hamza Rauf"],
    "product_category": ["Electronics", "Fashion", "Home & Living", "Electronics", "Fashion", "Beauty"],
    "revenue": [120.50, 45.00, 85.00, 120.50, 45.00, 210.00],
    "ad_channel": ["Meta Ads", "Google Ads", "Meta Ads", "Meta Ads", "Google Ads", "Meta Ads"]
})

transactions.to_sql("transactions", conn, index=False, if_exists="replace")

# 3. SQL Analytics: Common Table Expressions (CTEs), Aggregations, and Window Ranking
sql_query = """
WITH customer_aggregates AS (
    SELECT 
        customer,
        COUNT(order_id) AS total_orders,
        ROUND(SUM(revenue), 2) AS total_spend,
        ROUND(AVG(revenue), 2) AS average_order_value,
        GROUP_CONCAT(DISTINCT ad_channel) AS acquisition_channels
    FROM transactions
    GROUP BY customer
)
SELECT 
    customer,
    total_orders,
    total_spend,
    average_order_value,
    acquisition_channels,
    DENSE_RANK() OVER (ORDER BY total_spend DESC) AS ltv_rank,
    CASE 
        WHEN total_orders > 1 THEN 'Repeat Buyer'
        ELSE 'One-Time Buyer'
    END AS customer_segment
FROM customer_aggregates
ORDER BY total_spend DESC;
"""

ltv_df = pd.read_sql_query(sql_query, conn)

print("--- SQL CUSTOMER LIFETIME VALUE (LTV) AUDIT ---")
print(ltv_df.to_string(index=False))

# Close connection
conn.close()