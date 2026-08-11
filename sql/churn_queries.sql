

CREATE DATABASE churn_db;

USE churn_db;

SELECT COUNT(*) AS total_customers
FROM customer_churn;

SELECT *
FROM INFORMATION_SCHEMA.TABLES;

EXEC sp_rename
'WA_Fn-UseC_-Telco-Customer-Churn',
'customer_churn';


SELECT Churn,COUNT(*) AS customer_count
FROM customer_churn
GROUP BY Churn;

SELECT
ROUND(
    SUM(CASE WHEN Churn=1 THEN 1 ELSE 0 END)
    *100.0 / COUNT(*),
    2
) AS churn_rate
FROM customer_churn;

SELECT
    gender,
    COUNT(*) AS customers,
    SUM(CASE WHEN Churn=1 THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn
GROUP BY gender;

SELECT
    SeniorCitizen,
    COUNT(*) AS customers,
    SUM(CASE WHEN Churn=1 THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn
GROUP BY SeniorCitizen;


SELECT
    Contract,
    COUNT(*) AS customers,
    SUM(CASE
    WHEN
    Churn=1 THEN 1 
    ELSE 0
    END) AS churned_customers
FROM customer_churn
GROUP BY Contract;

SELECT
    Contract,
    ROUND(
        SUM(CASE WHEN Churn=1 THEN 1 ELSE 0 END)
        *100.0/COUNT(*),
        2
    ) AS churn_rate
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate DESC;

--REVENUE ANALYSIS

SELECT
ROUND(AVG(MonthlyCharges),2) AS avg_monthly_charges
FROM customer_churn;

--Revenue Lost Due to Churn
SELECT
ROUND(
SUM(CASE WHEN Churn=1 THEN MonthlyCharges
ELSE 0 END),2
) AS revenue_at_risk
FROM customer_churn;