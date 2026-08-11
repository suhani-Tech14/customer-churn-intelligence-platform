# Exploratory Data Analysis Summary

## Dataset Overview
  The dataset contains customer demographic information, account details, subscribed services, billing information, and the target variable Churn. After completing the data cleaning phase, the dataset was free from duplicate records, missing values were handled appropriately, and the data types were corrected to ensure reliable analysis.

The dataset includes both numerical and categorical features, making it suitable for statistical analysis, visualization, feature engineering, and machine learning.


## Churn Distribution
 The target variable analysis shows that the dataset contains both churned and non-  churned customers. The majority of customers have not churned, while a smaller       proportion have left the company.
        
   This indicates that the dataset is moderately imbalanced, which should be considered during model evaluation. Metrics such as Precision, Recall, F1-Score, and ROC-AUC will provide a better assessment than relying only on accuracy.
## Numerical Feature Insights
Tenure

Customers with lower tenure are more likely to churn than customers who have remained with the company for several years. This suggests that customer retention efforts should focus on the early stages of the customer lifecycle.

Monthly Charges

Customers paying higher monthly charges appear to have a higher tendency to churn. Premium-priced plans may require additional customer support or loyalty incentives to improve retention.

Total Charges

Customers with higher total charges generally have longer relationships with the company and exhibit lower churn rates. This indicates that long-term customers are typically more loyal.
## Categorical Feature Insights
Contract Type

Customers on month-to-month contracts experience the highest churn rate compared to customers on one-year or two-year contracts. Longer contract commitments are associated with better customer retention.

Internet Service

Different internet service types exhibit different churn patterns. Customers using Fiber Optic services tend to show higher churn than those using DSL or customers without internet service.

Payment Method

Customers using Electronic Check as their payment method show higher churn compared to other payment methods. This payment method may indicate a customer segment that requires additional retention efforts.

Online Security and Tech Support

Customers who do not subscribe to Online Security or Tech Support services have higher churn rates. These value-added services appear to strengthen customer loyalty.

Paperless Billing

Customers using paperless billing exhibit relatively higher churn. Additional analysis may be required to determine whether this relationship is influenced by other factors such as contract type or payment method.

## Correlation Findings
Correlation analysis indicates that numerical features exhibit varying degrees of relationship with one another.

Monthly Charges and Total Charges show a positive correlation because customers paying higher monthly fees generally accumulate larger total charges over time.

Tenure also demonstrates a positive relationship with Total Charges since customers who remain with the company longer naturally contribute more revenue.

No evidence of severe multicollinearity was observed among the numerical variables, suggesting that the features are suitable for machine learning models


## Top Business Insights

1.Month-to-month customers represent the highest churn risk.

Flexible contracts provide customers with fewer switching barriers, making them more likely to leave.

2.Customer churn is highest during the early stages of the customer lifecycle.

Customers with low tenure require proactive engagement, onboarding assistance, and early support.

3.Customers with higher monthly charges are more likely to churn.

Premium customers should receive additional value through loyalty programs, personalized offers, or enhanced customer support.

4.Customers without Online Security and Tech Support services churn more frequently.

Bundling these services with customer plans could improve long-term retention.

5.Payment behavior is associated with churn.

Customers using Electronic Check demonstrate higher churn and should be monitored through targeted retention campaigns.


## Business Recommendations

1.Introduce discounts or loyalty incentives that encourage customers on month-to-month contracts to upgrade to annual or multi-year contracts.

2.Develop an early customer engagement program during the first twelve months of the customer lifecycle, including onboarding support, educational resources, and proactive customer service.

3.Identify customers with high monthly charges and high predicted churn probability, then provide personalized retention offers such as discounts, bundled services, or dedicated customer support before they decide to leave.