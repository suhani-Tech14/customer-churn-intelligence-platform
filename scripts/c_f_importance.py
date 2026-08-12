import pandas as pd
import matplotlib.pyplot as plt


# Load top 10 feature importance data
df = pd.read_csv(
    r"C:\Users\suhan\Downloads\customer-churn-intelligence-platform\reports\shap\top10_features.csv"
)


# Clean feature names
def clean_feature_name(feature):

    feature = feature.replace("cat__", "")
    feature = feature.replace("num__", "")

    feature = feature.replace("_", " ")

    feature = feature.replace("Contract Month-to-month", "Contract: Month-to-month")
    feature = feature.replace("Contract Two year", "Contract: Two year")
    feature = feature.replace("Contract One year", "Contract: One year")

    feature = feature.replace(
        "InternetService Fiber optic",
        "Internet Service: Fiber optic"
    )

    feature = feature.replace(
        "InternetService DSL",
        "Internet Service: DSL"
    )

    feature = feature.replace(
        "PaymentMethod Electronic check",
        "Payment Method: Electronic check"
    )

    feature = feature.replace(
        "OnlineSecurity No",
        "Online Security: No"
    )

    feature = feature.replace(
        "TechSupport No",
        "Tech Support: No"
    )

    return feature.title()


df["Feature"] = df["Feature"].apply(clean_feature_name)


# Sort for horizontal bar chart
df = df.sort_values(
    by="Importance",
    ascending=True
)


# Create chart
plt.figure(figsize=(10, 6))

plt.barh(
    df["Feature"],
    df["Importance"]
)

plt.xlabel("Feature Importance")
plt.ylabel("")

plt.title(
    "Top 10 Features Influencing Customer Churn",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()


# Save image
plt.savefig(
    "../visuals/images/shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()