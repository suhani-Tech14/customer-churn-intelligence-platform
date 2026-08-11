import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Predict Churn",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Predict Customer Churn")
st.markdown(
    "Generate churn predictions using the trained Logistic Regression production model."
)
st.divider()

BASE_DIR = Path(__file__).resolve().parent.parent  # this is streamlit_app
PROJECT_ROOT = BASE_DIR.parent                     # go up one more level

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
    st.warning("Please upload a customer dataset first.")
    st.stop()

df = st.session_state["uploaded_data"].copy()

numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].replace(" ", None)
        df[col] = df[col].replace("", None)
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

st.subheader("Customer Data")
st.dataframe(df.head(10), use_container_width=True)

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
churn_probability = model.predict_proba(X)[:, 1]

results = df.copy()
results["Churn Prediction"] = predictions
results["Churn Probability"] = churn_probability
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
# Prediction Summary
# ------------------
st.divider()
st.subheader("Prediction Summary")

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.metric("Total Customers", len(results))
with col2:
    churn_count = int(results["Churn Prediction"].sum())
    st.metric("Predicted Churn", churn_count)
with col3:
    avg_probability = results["Churn Probability"].mean() * 100
    st.metric("Average Churn Probability", f"{avg_probability:.2f}%")
with col4:
    high_risk_count = int((results["Risk Category"] == "High Risk").sum())
    st.metric("High Risk Customers", high_risk_count)

# ------------------
# Prediction Results
# ------------------
st.divider()
st.subheader("Prediction Results")
st.dataframe(results, use_container_width=True)

# ------------------
# Visual Analytics
# ------------------
st.divider()
st.subheader("Customer Risk Distribution")

risk_counts = (
    results["Risk Category"]
    .value_counts()
    .reindex(["Low Risk", "Medium Risk", "High Risk"], fill_value=0)
    .reset_index()
)
risk_counts.columns = ["Risk Category", "Count"]

low_risk = int((results["Risk Category"] == "Low Risk").sum())
medium_risk = int((results["Risk Category"] == "Medium Risk").sum())
high_risk = int((results["Risk Category"] == "High Risk").sum())

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
st.plotly_chart(fig_risk, use_container_width=True)

# ------------------
st.divider()
st.subheader("Churn Probability Distribution")

# Create binned probability distribution
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
st.plotly_chart(fig_prob, use_container_width=True)

# ------------------
st.divider()
st.subheader("Filter Customers")

selected_risk = st.multiselect(
    "Select Risk Category",
    options=["Low Risk", "Medium Risk", "High Risk"],
    default=["Low Risk", "Medium Risk", "High Risk"],
    label_visibility="collapsed"
)

filtered_results = results[results["Risk Category"].isin(selected_risk)]
st.dataframe(filtered_results, use_container_width=True)

# ------------------
st.divider()
st.subheader("🚨 High-Risk Customers")

high_risk_customers = results[
    results["Risk Category"] == "High Risk"
].sort_values(by="Churn Probability", ascending=False)

display_columns = [
    "customerID", "Contract", "tenure", "MonthlyCharges",
    "Churn Probability (%)", "Risk Category"
]

st.dataframe(high_risk_customers[display_columns], use_container_width=True)

# ------------------
st.divider()
st.subheader("Download Predictions")

csv_data = results.to_csv(index=False).encode("utf-8")

c1, c2 = st.columns([3, 2], gap="small")
with c1:
    st.markdown(
        "Download the full prediction results with churn probabilities and risk categories."
    )
with c2:
    st.download_button(
        label="⬇️ Download Prediction Results",
        data=csv_data,
        file_name="customer_churn_predictions.csv",
        mime="text/csv",
        use_container_width=True
    )