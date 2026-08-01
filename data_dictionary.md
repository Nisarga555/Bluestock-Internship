# Bluestock Mutual Fund Data Dictionary

## cleaned_nav_history

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## cleaned_investor_transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund code |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | T30/B30 |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual Income |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | Verified/Pending |

---

## cleaned_scheme_performance

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Scheme Code |
| scheme_name | TEXT | Fund Name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Std Dev |
| max_drawdown_pct | REAL | Maximum Drawdown |
| aum_crore | REAL | Assets Under Management |
| expense_ratio_pct | REAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |
| risk_grade | TEXT | Risk Category |