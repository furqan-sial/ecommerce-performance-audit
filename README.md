# E-Commerce Channel Performance & Data Hygiene Audit

A data quality audit and revenue attribution script designed to identify ingestion errors, handle null/refund anomalies, and calculate channel contribution metrics for marketing decision-makers.

---

## 📌 Executive Summary

Raw tracking exports frequently contain missing figures, dirty records, and negative adjustments (refunds) that distort true campaign ROAS and top-line figures. This pipeline audits transactional tables, applies data hygiene standards, and aggregates revenue and order share across acquisition channels.

---

## 🛠️ Data Hygiene Rules Applied

1. **Deduplication:** Strips duplicate transactional records while retaining valid sequential purchases.
2. **Refund Isolation:** Segregates negative balance records (`revenue <= 0`) to prevent skewing gross sales baselines.
3. **Null Imputation:** Imputes missing revenue records using median category baselines to preserve sample size without creating artificial outlier inflation.

---

## 📊 Commercial Insights Output

| Ad Channel     | Total Revenue ($) | Order Count | Revenue Share (%) |
| :------------- | :---------------- | :---------- | :---------------- |
| **Meta Ads**   | $536.00           | 4           | 85.62%            |
| **Google Ads** | $90.00            | 2           | 14.38%            |

- **Primary Driver:** Meta Ads accounts for over 85% of verified top-line revenue, indicating high campaign scale.
- **Diversification Need:** Search intent via Google Ads shows consistent conversion value but requires higher budget allocation to mitigate single-channel dependency.

---

## 💻 Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy
- **Environment:** VS Code, Git
