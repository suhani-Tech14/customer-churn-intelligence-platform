# Feature Engineering Summary

## Objective

The objective of feature engineering was to transform the cleaned customer dataset into a machine-learning-ready format while preserving business information and improving model performance.

## Target Variable

The target variable is **Churn**, where:

* 0 = Customer did not churn
* 1 = Customer churned

## Feature Selection

The `customerID` column was removed because it is a unique identifier and does not contribute to predicting customer churn.

## Numerical Features

The following numerical features were identified:

* tenure
* MonthlyCharges
* TotalCharges

These features will be standardized during model training using StandardScaler.

## Categorical Features

Categorical variables such as Contract, InternetService, PaymentMethod, Partner, and others were identified for encoding.

One-Hot Encoding will be applied to convert these categorical variables into numerical features suitable for machine learning algorithms.

## Data Splitting

The dataset was divided into training and testing datasets using an 80:20 ratio.

Stratified sampling was used to preserve the original churn distribution in both datasets.

## Data Persistence

To ensure reproducibility across the project, the training and testing datasets were saved as separate files after the train-test split.

The following datasets were generated:

* X_train.csv
* X_test.csv
* y_train.csv
* y_test.csv

Saving these datasets ensures that all subsequent phases, including model training, evaluation, explainability, dashboard development, and deployment, use the exact same data split, resulting in consistent and reproducible model performance.


## Preprocessing Pipeline

A ColumnTransformer was created to apply:

* StandardScaler to numerical features.
* OneHotEncoder to categorical features.

This preprocessing pipeline ensures consistency during model training, evaluation, and deployment.

## Outcome

The dataset is now prepared for machine learning model development with a reusable preprocessing pipeline that supports both training and future predictions.
