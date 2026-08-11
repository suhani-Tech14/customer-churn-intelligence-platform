import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Analytics")
st.markdown("Understand churn patterns and model explanations.")
st.divider()

# ------------------
# Load data & models
# ------------------
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent

MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"
PREPROCESSOR_PATH = PROJECT_ROOT / "models" / "preprocessor.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_resource
def load_preprocessor():
    return joblib.load(PREPROCESSOR_PATH)

model = load_model()
preprocessor = load_preprocessor()

if "uploaded_data" not in st.session_state:
    st.warning("Please upload a customer dataset first on the Upload page.")
    st.stop()

df = st.session_state["uploaded_data"].copy()

# Basic cleaning (same as predict page)
numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].replace(" ", None)
        df[col] = df[col].replace("", None)
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

required_features = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
    'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
    'PaperlessBilling', 'PaymentMethod'
]

missing = set(required_features) - set(df.columns)
if missing:
    st.error(f"Uploaded data is missing columns: {missing}")
    st.stop()

X = df[required_features]

predictions = model.predict(X)
proba = model.predict_proba(X)[:, 1]

results = df.copy()
results["Churn Prediction"] = predictions
results["Churn Probability"] = proba
results["Churn Probability (%)"] = (results["Churn Probability"] * 100).round(2)

def assign_risk(probability):
    if probability < 0.30:
        return "Low Risk"
    elif probability < 0.60:
        return "Medium Risk"
    else:
        return "High Risk"

results["Risk Category"] = results["Churn Probability"].apply(assign_risk)

# ------------------
# Overall Analytics
# ------------------
st.subheader("Overall Analytics")

c1, c2, c3 = st.columns(3, gap="small")

with c1:
    st.metric("Total Customers", len(results))
with c2:
    churn_count = int(results["Churn Prediction"].sum())
    st.metric("Predicted Churn", churn_count)
with c3:
    avg_prob = results["Churn Probability"].mean() * 100
    st.metric("Avg Churn Probability", f"{avg_prob:.2f}%")

st.divider()

# ------------------
# Risk Distribution
# ------------------
st.subheader("Risk Distribution")

risk_counts = (
    results["Risk Category"]
    .value_counts()
    .reindex(["Low Risk", "Medium Risk", "High Risk"], fill_value=0)
    .reset_index()
)
risk_counts.columns = ["Risk Category", "Count"]

low_risk = int(risk_counts.loc[risk_counts["Risk Category"] == "Low Risk", "Count"].sum())
medium_risk = int(risk_counts.loc[risk_counts["Risk Category"] == "Medium Risk", "Count"].sum())
high_risk = int(risk_counts.loc[risk_counts["Risk Category"] == "High Risk", "Count"].sum())

r1, r2, r3 = st.columns(3, gap="small")
with r1:
    st.metric("Low Risk", low_risk)
with r2:
    st.metric("Medium Risk", medium_risk)
with r3:
    st.metric("High Risk", high_risk)

fig_risk = px.bar(
    risk_counts,
    y="Risk Category",
    x="Count",
    orientation="h",
    color="Risk Category",
    color_discrete_map={
        "Low Risk": "#2E8B57",
        "Medium Risk": "#DAA520",
        "High Risk": "#B22222"
    },
    height=220
)
fig_risk.update_layout(
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Number of Customers",
    yaxis_title=None
)
st.plotly_chart(fig_risk, width="stretch")

st.divider()

# ------------------
# Churn Probability
# ------------------
st.subheader("Churn Probability")
st.markdown("Distribution of customer risk.")

prob_series = results["Churn Probability (%)"]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = [f"{i}-{i+9}%" for i in bins[:-1]]
prob_binned = pd.cut(prob_series, bins=bins, labels=labels, right=False)

prob_dist = (
    prob_binned.value_counts()
    .reindex(labels, fill_value=0)
    .reset_index()
)
prob_dist.columns = ["Churn Probability", "Count"]

fig_prob = px.bar(
    prob_dist,
    y="Churn Probability",
    x="Count",
    orientation="h",
    color="Count",
    color_continuous_scale="Blues",
    height=260
)
fig_prob.update_layout(
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Number of Customers",
    yaxis_title=None
)
st.plotly_chart(fig_prob, width="stretch")

st.divider()

# ------------------
# Explainable AI (Random Forest)
# ------------------
st.subheader("Explainable AI")
st.markdown("Why are customers predicted to churn?")

# Get feature names after preprocessing
num_features = preprocessor.transformers_[0][2]
cat_features = list(preprocessor.named_transformers_["cat"].get_feature_names_out())
all_features = list(num_features) + cat_features

# Get feature importances from Random Forest
rf = model.named_steps["classifier"]
importances = rf.feature_importances_

importance_df = pd.DataFrame({
    "feature": all_features,
    "importance": importances
}).sort_values(by="importance", ascending=False)

top_n = 10
top_imp = importance_df.head(top_n).copy()

st.markdown("### Global Feature Importance")

fig_imp = px.bar(
    top_imp,
    y="feature",
    x="importance",
    orientation="h",
    color="importance",
    color_continuous_scale="Greens",
    height=320
)
fig_imp.update_layout(
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Importance",
    yaxis_title=None
)
st.plotly_chart(fig_imp, width="stretch")

st.divider()

# ------------------
# Individual Customer Explanation
# ------------------
st.subheader("Individual Customer Explanation")

customer_ids = results["customerID"].unique()
selected_id = st.selectbox("Customer", options=customer_ids)

if selected_id:
    row = results[results["customerID"] == selected_id].iloc[0]
    X_row = X[results["customerID"] == selected_id]

    churn_prob = float(row["Churn Probability (%)"])
    risk = row["Risk Category"]

    st.markdown(f"**Customer:** `{selected_id}`")
    st.markdown(f"**Churn Probability:** `{churn_prob:.1f}%`")
    st.markdown(f"**Risk:** `{risk}`")

    # Local explanation using normalized importances * feature values as proxy
    X_row_scaled = model.named_steps["preprocessor"].transform(X_row)  # (1, n_features)

    norm_imp = importances / importances.sum()
    contrib = X_row_scaled * norm_imp  # (1, n_features)

    contrib_df = pd.DataFrame({
        "feature": all_features,
        "contribution": contrib[0]
    }).sort_values(by="contribution", key=abs, ascending=False)

    top_contrib = contrib_df.head(5).copy()
    top_contrib["direction"] = top_contrib["contribution"].apply(
        lambda x: "increases churn" if x > 0 else "decreases churn"
    )

    st.markdown("### Top factors for this customer")

    for _, r in top_contrib.iterrows():
        st.markdown(
            f"- **{r['feature']}** → {r['direction']}"
        )

st.divider()

# ------------------
# Full Prediction Table
# ------------------
st.subheader("Full Prediction Table")
st.dataframe(results, width="stretch")