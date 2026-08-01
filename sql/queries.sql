USE bluestock_db;

-- View all records
SELECT * FROM cleaned_scheme_performance;

-- Total Schemes
SELECT COUNT(*) AS Total_Schemes
FROM cleaned_scheme_performance;

-- Total Fund Houses
SELECT COUNT(DISTINCT fund_house) AS Total_Fund_Houses
FROM cleaned_scheme_performance;

-- Average 5-Year Return by Category
SELECT
    category,
    ROUND(AVG(return_5yr_pct), 2) AS Avg_5Yr_Return
FROM cleaned_scheme_performance
GROUP BY category
ORDER BY Avg_5Yr_Return DESC;

-- Top 5 Funds by AUM
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM cleaned_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Top 5 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM cleaned_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Average Expense Ratio by Category
SELECT
    category,
    ROUND(AVG(expense_ratio_pct), 2) AS Avg_Expense_Ratio
FROM cleaned_scheme_performance
GROUP BY category;

-- Number of Schemes by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS Total_Schemes
FROM cleaned_scheme_performance
GROUP BY risk_grade
ORDER BY Total_Schemes DESC;