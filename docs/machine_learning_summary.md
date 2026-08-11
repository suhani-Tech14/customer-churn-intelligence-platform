# Machine Learning Pipeline Summary

## Objective

The objective of this phase was to build and compare multiple machine learning models for predicting customer churn.

## Models Evaluated

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

## Preprocessing

A Scikit-learn Pipeline was implemented to ensure that preprocessing and model training occur consistently.

The pipeline includes:

* StandardScaler for numerical features.
* OneHotEncoder for categorical features.
* Machine learning classifier.

## Model Comparison

Multiple baseline models were trained and compared using the same train-test split.

The comparison enables selection of the most suitable model before hyperparameter tuning.

## Hyperparameter Tuning

GridSearchCV was used to optimize the selected model by evaluating multiple parameter combinations through cross-validation.

## Model Persistence

The final trained model and preprocessing pipeline were saved using Joblib to support future predictions, deployment, and integration with the Streamlit application.

## Outcome

A production-ready machine learning pipeline was developed that can be reused for prediction, evaluation, explainability, and deployment.
