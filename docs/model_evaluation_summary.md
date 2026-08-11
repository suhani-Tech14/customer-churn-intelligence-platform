# Model Evaluation Summary

## Objective

The objective of this phase was to evaluate the performance of the trained machine learning model using multiple evaluation metrics and determine its suitability for predicting customer churn.

## Evaluation Metrics

The following metrics were used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix
* Classification Report

## Business Interpretation

Accuracy measures the overall correctness of the model.

Precision measures how many customers predicted as churn actually churned.

Recall measures how many actual churning customers were successfully identified. Since retaining customers is the primary business objective, Recall was considered one of the most important evaluation metrics.

The F1 Score provides a balanced assessment of Precision and Recall.

The ROC-AUC Score evaluates the model's ability to distinguish between churning and non-churning customers across different classification thresholds.

## Model Selection

The selected model demonstrated strong predictive performance across multiple evaluation metrics and achieved a suitable balance between identifying churning customers and minimizing false predictions.

## Outcome

The evaluated model is suitable for the next phases of the project, including Explainable AI (SHAP), Customer Segmentation, the Recommendation Engine, Power BI Dashboard integration, and deployment through the Streamlit application.
