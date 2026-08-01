-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM cleaned_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

--------------------------------------------------

-- 2. Average NAV per Month

SELECT
strftime('%Y-%m',date) AS Month,
AVG(nav) AS Avg_NAV
FROM cleaned_nav_history
GROUP BY Month
ORDER BY Month;

--------------------------------------------------

-- 3. SIP Transactions Count

SELECT COUNT(*) AS SIP_Count
FROM cleaned_investor_transactions
WHERE transaction_type='SIP';

--------------------------------------------------

-- 4. Transactions by State

SELECT
state,
COUNT(*) AS Transactions
FROM cleaned_investor_transactions
GROUP BY state
ORDER BY Transactions DESC;

--------------------------------------------------

-- 5. Expense Ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM cleaned_scheme_performance
WHERE expense_ratio_pct<1;

--------------------------------------------------

-- 6. Highest 5-Year Return

SELECT
scheme_name,
return_5yr_pct
FROM cleaned_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

--------------------------------------------------

-- 7. Average Expense Ratio

SELECT
AVG(expense_ratio_pct)
AS Average_Expense
FROM cleaned_scheme_performance;

--------------------------------------------------

-- 8. Risk Grade Distribution

SELECT
risk_grade,
COUNT(*) AS Total
FROM cleaned_scheme_performance
GROUP BY risk_grade;

--------------------------------------------------

-- 9. Morningstar Rating Distribution

SELECT
morningstar_rating,
COUNT(*) AS Total
FROM cleaned_scheme_performance
GROUP BY morningstar_rating
ORDER BY morningstar_rating DESC;

--------------------------------------------------

-- 10. Fund Houses Count

SELECT
fund_house,
COUNT(*) AS Schemes
FROM cleaned_scheme_performance
GROUP BY fund_house
ORDER BY Schemes DESC;