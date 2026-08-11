import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

# ------------------
# Header
# ------------------
st.markdown(
    """
    <div style="text-align:center; padding: 10px 0 20px;">
        <h1>CUSTOMER CHURN INTELLIGENCE PLATFORM</h1>
        <h3>Predict • Explain • Segment • Recommend</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------
# Project Overview
# ------------------
st.subheader("PROJECT OVERVIEW")

st.markdown(
    """
    An end-to-end Data Science platform designed to identify customers at risk of churn  
    and provide actionable retention recommendations.
    """
)

st.divider()

# ------------------
# Business Objective
# ------------------
st.subheader("BUSINESS OBJECTIVE")

c1, c2 = st.columns(2, gap="small")

with c1:
    st.info(
        """
        **Predict Churn**

        Probability + Prediction
        """
    )

with c2:
    st.info(
        """
        **Identify Risk**

        Low / Medium / High
        """
    )

c3, c4 = st.columns(2, gap="small")

with c3:
    st.info(
        """
        **Explain Churn**

        Model explanations & feature importance
        """
    )

with c4:
    st.info(
        """
        **Recommend Action**

        Retention Strategy
        """
    )

st.divider()

# ------------------
# Technology Stack
# ------------------
st.subheader("TECHNOLOGY STACK")

st.markdown(
    """
    - **Languages & Core**: Python, SQL  
    - **ML & Data**: Scikit-learn, Pandas, NumPy  
    - **Explainability**: SHAP (model-agnostic explanations)  
    - **App & Visualization**: Streamlit, Plotly  
    - **BI & Reporting**: Power BI (optional integration)  
    - **Version Control**: Git / GitHub  
    """
)

st.divider()

# ------------------
# Data Science Pipeline
# ------------------
st.subheader("DATA SCIENCE PIPELINE")

st.markdown(
    """
    1. **Data Ingestion & Cleaning**
       - SQL extraction / CSV upload
       - Data cleaning, missing value handling, type conversion

    2. **Exploratory Data Analysis (EDA)**
       - Univariate & bivariate analysis
       - Churn patterns by segment (contract, tenure, charges, etc.)

    3. **Feature Engineering**
       - Encoding categorical variables
       - Scaling numeric features
       - Creating derived features if needed

    4. **Modeling**
       - Train multiple models (e.g., Logistic Regression, Random Forest, Gradient Boosting)
       - Hyperparameter tuning & cross-validation

    5. **Evaluation**
       - Metrics: Precision, Recall, F1-score, ROC-AUC
       - Model selection based on business needs (e.g., recall for churn detection)

    6. **Explainability & Segmentation**
       - Global feature importance
       - Individual customer explanations (SHAP / model-based)
       - Risk segmentation (Low / Medium / High)

    7. **Recommendation & Deployment**
       - Retention strategies by segment
       - Individual action plans
       - Streamlit app for business users
    """
)

st.divider()

# ------------------
# Model Information
# ------------------
st.subheader("MODEL INFORMATION")

st.markdown(
    """
    **Production Model:** Logistic Regression  

    - Selected based on model evaluation across:
      - Precision, Recall, F1-score
      - ROC-AUC
      - Cross-validation performance
    - Chosen for:
      - Interpretability
      - Stable performance
      - Ease of explanation to business stakeholders
    """
)

st.divider()

# ------------------
# Business Value
# ------------------
st.subheader("BUSINESS VALUE")

st.markdown(
    """
    ✓ Early identification of churn-risk customers  
    ✓ Explainable predictions (clear reasons behind churn risk)  
    ✓ Customer segmentation by risk, contract, tenure, and more  
    ✓ Targeted retention recommendations (segment & customer level)  
    ✓ Data-driven decision making for marketing & customer success  
    """
)

st.divider()

# ------------------
# How to Use This App
# ------------------
st.subheader("HOW TO USE THIS APP")

st.markdown(
    """
    1. **Upload Dataset**
       - Go to the **Upload Dataset** page.
       - Upload a CSV with customer data (same schema as training data).

    2. **Predict Churn**
       - Navigate to **Predict Churn**.
       - View churn predictions, probabilities, and risk categories.

    3. **Explore Analytics**
       - Open **Customer Analytics**.
       - See risk distribution, churn probability distribution, and feature importance.
       - Explore individual customer explanations.

    4. **Get Recommendations**
       - Go to **Retention Recommendations**.
       - Review segment-level strategies and individual action plans.
       - Download the retention plan as CSV.

    5. **Learn About the Project**
       - Use this **About Project** page to understand:
         - Objectives
         - Pipeline
         - Models
         - Business value
    """
)

st.divider()

# ------------------
# Credits
# ------------------
st.subheader("CREDITS")

st.markdown(
    """
    This platform was built as an end-to-end churn intelligence solution,  
    combining predictive modeling, explainability, and actionable business recommendations.

    You can extend it further by:
    - Integrating with a CRM or marketing automation tool
    - Scheduling batch predictions
    - Adding more models or advanced segmentation
    """
)