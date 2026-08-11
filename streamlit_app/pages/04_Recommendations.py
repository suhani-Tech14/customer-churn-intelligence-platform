import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Retention Recommendations",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Retention Recommendations")
st.markdown("Actionable strategies to reduce churn and retain high‑risk customers.")
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

# Basic cleaning (same as other pages)
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
# Summary KPIs
# ------------------
st.subheader("Retention Opportunity Overview")

c1, c2, c3, c4 = st.columns(4, gap="small")

total = len(results)
high_risk = int((results["Risk Category"] == "High Risk").sum())
medium_risk = int((results["Risk Category"] == "Medium Risk").sum())
churn_count = int(results["Churn Prediction"].sum())

with c1:
    st.metric("Total Customers", total)
with c2:
    st.metric("High Risk Customers", high_risk)
with c3:
    st.metric("Medium Risk Customers", medium_risk)
with c4:
    st.metric("Predicted Churn", churn_count)

st.divider()

# ------------------
# Segment-level recommendations
# ------------------
st.subheader("Segment-Level Retention Strategies")

# Risk-based recommendations
risk_rec = {
    "High Risk": "Urgent retention: offer contract upgrade, targeted discount, or loyalty incentive. Proactive outreach from retention team.",
    "Medium Risk": "Preventive engagement: highlight value, suggest plan optimization, offer small incentives or add‑ons.",
    "Low Risk": "Maintain satisfaction: monitor for changes, reward loyalty, upsell/cross‑sell carefully."
}

risk_df = (
    results["Risk Category"]
    .value_counts()
    .reindex(["High Risk", "Medium Risk", "Low Risk"], fill_value=0)
    .reset_index()
)
risk_df.columns = ["Risk Category", "Count"]

fig_risk = px.bar(
    risk_df,
    y="Risk Category",
    x="Count",
    orientation="h",
    color="Risk Category",
    color_discrete_map={
        "High Risk": "#B22222",
        "Medium Risk": "#DAA520",
        "Low Risk": "#2E8B57"
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

st.markdown("#### Recommended actions by risk segment")

for risk in ["High Risk", "Medium Risk", "Low Risk"]:
    count = int(risk_df.loc[risk_df["Risk Category"] == risk, "Count"].sum())
    st.markdown(f"**{risk} ({count} customers)**")
    st.info(risk_rec[risk])

st.divider()

# Contract-based recommendations
st.subheader("By Contract Type")

contract_rec = {
    "Month-to-month": "Focus on converting to longer contracts: offer 6/12‑month deals with discounts or added benefits.",
    "One year": "Encourage renewal early; offer loyalty perks or service upgrades near contract end.",
    "Two year": "Maintain engagement; ensure service quality; offer upgrades or add‑ons to increase stickiness."
}

contract_grp = (
    results.groupby("Contract")["customerID"]
    .count()
    .reset_index()
    .rename(columns={"customerID": "Count"})
)

fig_contract = px.bar(
    contract_grp,
    y="Contract",
    x="Count",
    orientation="h",
    color="Count",
    color_continuous_scale="Teal",
    height=220
)
fig_contract.update_layout(
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Number of Customers",
    yaxis_title=None
)
st.plotly_chart(fig_contract, width="stretch")

st.markdown("#### Recommended actions by contract")

for contract in contract_grp["Contract"]:
    count = int(contract_grp.loc[contract_grp["Contract"] == contract, "Count"].sum())
    st.markdown(f"**{contract} ({count} customers)**")
    st.info(contract_rec.get(contract, "Tailor retention actions based on usage and risk profile."))

st.divider()

# Tenure-based recommendations
st.subheader("By Tenure Segment")

def tenure_bucket(t):
    if t < 12:
        return "0–12 months"
    elif t < 24:
        return "12–24 months"
    elif t < 48:
        return "2–4 years"
    else:
        return "4+ years"

results["Tenure Bucket"] = results["tenure"].apply(tenure_bucket)

tenure_rec = {
    "0–12 months": "Onboarding & early success: proactive check‑ins, education on features, early‑loyalty offers.",
    "12–24 months": "Stabilize relationship: address pain points, offer plan optimization, highlight value delivered.",
    "2–4 years": "Deepen loyalty: reward long tenure, offer premium features, involve in beta/new products.",
    "4+ years": "Protect core base: executive‑level outreach for top accounts, personalized retention offers."
}

tenure_grp = (
    results.groupby("Tenure Bucket")["customerID"]
    .count()
    .reset_index()
    .rename(columns={"customerID": "Count"})
)

fig_tenure = px.bar(
    tenure_grp,
    y="Tenure Bucket",
    x="Count",
    orientation="h",
    color="Count",
    color_continuous_scale="Purples",
    height=220
)
fig_tenure.update_layout(
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Number of Customers",
    yaxis_title=None
)
st.plotly_chart(fig_tenure, width="stretch")

st.markdown("#### Recommended actions by tenure")

for bucket in tenure_grp["Tenure Bucket"]:
    count = int(tenure_grp.loc[tenure_grp["Tenure Bucket"] == bucket, "Count"].sum())
    st.markdown(f"**{bucket} ({count} customers)**")
    st.info(tenure_rec[bucket])

st.divider()

# ------------------
# Individual customer recommendations
# ------------------
st.subheader("Individual Customer Recommendations")

customer_ids = results["customerID"].unique()
selected_id = st.selectbox("Customer", options=customer_ids)

if selected_id:
    row = results[results["customerID"] == selected_id].iloc[0]
    risk = row["Risk Category"]
    prob = float(row["Churn Probability (%)"])
    contract = row["Contract"]
    tenure = row["tenure"]
    charges = row["MonthlyCharges"]

    st.markdown(f"**Customer:** `{selected_id}`")
    st.markdown(f"**Risk:** `{risk}` | **Churn Probability:** `{prob:.1f}%`")
    st.markdown(f"**Contract:** `{contract}` | **Tenure:** `{tenure}` months | **Monthly Charges:** `${charges:.2f}`")

    st.markdown("#### Suggested actions")

    actions = []

    # Risk-based
    if risk == "High Risk":
        actions.append("Contact within 7 days with a personalized retention offer (discount, upgrade, or loyalty incentive).")
        actions.append("Review service issues or complaints; escalate if needed.")
    elif risk == "Medium Risk":
        actions.append("Send targeted engagement email with plan optimization tips and optional add‑ons.")
        actions.append("Monitor for 30 days; trigger follow‑up if risk increases.")
    else:
        actions.append("Maintain regular communication; offer loyalty benefits or relevant upsells.")

    # Contract-based
    if "Month-to-month" in contract:
        actions.append("Propose a 12‑month contract with a clear discount or added value (e.g., higher speed, more channels).")
    elif "One year" in contract:
        actions.append("Start renewal conversation 60 days before contract end; offer loyalty perk for early renewal.")
    elif "Two year" in contract:
        actions.append("Focus on satisfaction and service quality; consider premium add‑ons to increase dependency.")

    # Tenure-based
    if tenure < 12:
        actions.append("Treat as new customer: onboarding call, education on key features, quick‑win offers.")
    elif tenure < 24:
        actions.append("Check satisfaction, suggest plan optimization, and highlight value so far.")
    elif tenure < 48:
        actions.append("Offer loyalty rewards and involve in beta/new feature programs.")
    else:
        actions.append("Treat as strategic customer: personalized outreach, VIP support options.")

    for i, a in enumerate(actions, 1):
        st.markdown(f"{i}. {a}")

st.divider()

# ------------------
# High-risk customers action list
# ------------------
st.subheader("🚨 High-Risk Customers Action List")

high_risk_df = results[results["Risk Category"] == "High Risk"].copy()

if high_risk_df.empty:
    st.info("No high-risk customers in the current dataset.")
else:
    high_risk_df = high_risk_df.sort_values("Churn Probability", ascending=False)

    display_cols = [
        "customerID", "Contract", "tenure", "MonthlyCharges",
        "Churn Probability (%)", "Risk Category"
    ]

    st.dataframe(high_risk_df[display_cols], width="stretch")

    st.markdown(
        "Prioritize top 10–20 high‑risk customers for immediate outreach this week."
    )

st.divider()

# ------------------
# Download recommendations
# ------------------
st.subheader("Download Retention Plan")

rec_df = results[[
    "customerID", "Contract", "tenure", "MonthlyCharges",
    "Churn Probability (%)", "Risk Category"
]].copy()

rec_df["Suggested Action"] = rec_df["Risk Category"].map({
    "High Risk": "Urgent retention outreach + offer",
    "Medium Risk": "Preventive engagement + plan optimization",
    "Low Risk": "Maintain satisfaction + loyalty/upsell"
})

csv_data = rec_df.to_csv(index=False).encode("utf-8")

c1, c2 = st.columns([3, 2], gap="small")
with c1:
    st.markdown(
        "Download a CSV with each customer’s risk and suggested retention action."
    )
with c2:
    st.download_button(
        label="⬇️ Download Retention Plan (CSV)",
        data=csv_data,
        file_name="retention_recommendations.csv",
        mime="text/csv",
        width="stretch"
    )