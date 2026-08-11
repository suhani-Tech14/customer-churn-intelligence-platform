# Explainable AI Summary

## Objective

The objective of this phase was to improve the transparency and interpretability of the customer churn prediction model by identifying how individual features influence model predictions.

## Methodology

The trained machine learning pipeline was loaded from the saved model artifacts. The preprocessing pipeline was used to transform the test dataset, and the appropriate SHAP explainer was selected automatically based on the underlying classifier.

## Global Insights

Global SHAP analysis identified the most influential features affecting customer churn. These insights highlight the primary business drivers of churn and can guide strategic retention initiatives.

## Local Insights

Individual customer explanations demonstrate how specific features contribute to increasing or decreasing churn risk. This enables customer support teams to understand the rationale behind each prediction and recommend targeted retention actions.

## Business Value

Explainable AI increases trust in machine learning predictions by making the model transparent to both technical and non-technical stakeholders. These explanations support better decision-making, improve stakeholder confidence, and facilitate the integration of predictive analytics into business operations.
