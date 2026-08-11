import streamlit as st

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# MAIN APPLICATION BACKGROUND
# ============================================================

st.markdown(
    """
<style>

/* Main application background */
.stApp {
    background-color: #F1F5F9;
}

/* Main content width */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
<style>

.hero {
    background: linear-gradient(
        135deg,
        #0F172A,
        #1E3A5F
    );

    padding: 28px 32px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 28px;

    box-shadow:
        0 8px 24px rgba(15, 23, 42, 0.12);
}

.hero-icon {
    font-size: 42px;
}

.hero-title {
    color: #FFFFFF;
    font-size: 30px;
    font-weight: 700;
    line-height: 1.2;
}

.hero-subtitle {
    color: #CBD5E1;
    font-size: 15px;
    margin-top: 6px;
}

</style>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="hero">
    <div class="hero-icon">📊</div>
    <div>
        <div class="hero-title">
            Customer Churn Intelligence Platform
        </div>
        <div class="hero-subtitle">
            AI-Powered Customer Retention & Churn Prediction
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
<style>

.intro {
    text-align: center;
    margin: 20px 0 30px 0;
}

.intro-title {
    font-size: 20px;
    font-weight: 700;
    color: #0F172A;
}

.intro-text {
    font-size: 14px;
    color: #64748B;
    margin-top: 8px;
}

</style>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="intro">
    <div class="intro-title">
        Predict • Explain • Segment • Retain
    </div>
    <div class="intro-text">
        Identify customers at risk of churn, understand the factors
        driving their behavior, and prioritize data-driven retention actions.
    </div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# ORIGINAL INTRODUCTION CONTENT
# ============================================================

st.markdown(
    """
    AI-Powered Customer Retention & Churn Prediction System
    """
)

st.divider()

st.markdown(
    """
    Welcome to the "Customer Churn Intelligence Platform".

    This application predicts whether customers are likely to leave the company,
    estimates their churn probability, classifies their risk level, and provides
    actionable business recommendations.

    The goal is to help organizations reduce customer churn through
    data-driven decision making.
    """
)


# ============================================================
# FEATURE CARD CSS
# ============================================================

st.markdown(
    """
<style>

.feature-card {

    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    border-radius: 14px;

    padding: 26px;

    min-height: 150px;

    margin-bottom: 20px;

    box-shadow:
        0 4px 14px rgba(15, 23, 42, 0.06);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.feature-card:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(15, 23, 42, 0.10);
}

.feature-icon {

    font-size: 28px;

    margin-bottom: 10px;
}

.feature-title {

    font-size: 18px;

    font-weight: 700;

    color: #0F172A;

    margin-bottom: 8px;
}

.feature-text {

    font-size: 13px;

    line-height: 1.6;

    color: #64748B;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# FOUR MAIN FEATURE CARDS
# ============================================================

row1_col1, row1_col2 = st.columns(2)

row2_col1, row2_col2 = st.columns(2)


# ------------------------------------------------------------
# PROJECT OBJECTIVE
# ------------------------------------------------------------

with row1_col1:

    st.markdown(
        """
<div class="feature-card">
    <div class="feature-icon">🎯</div>
    <div class="feature-title">
        Project Objective
    </div>
    <div class="feature-text">
        Predict customer churn and identify customers
        who require proactive retention attention.
    </div>
</div>
""",
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# MACHINE LEARNING
# ------------------------------------------------------------

with row1_col2:

    st.markdown(
        """
<div class="feature-card">
    <div class="feature-icon">🤖</div>
    <div class="feature-title">
        Machine Learning
    </div>
    <div class="feature-text">
        Logistic Regression was selected as the production
        model after comparing model performance using
        Accuracy, Precision, Recall, F1-Score and
        Cross-Validation.
    </div>
</div>
""",
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# BUSINESS VALUE
# ------------------------------------------------------------

with row2_col1:

    st.markdown(
        """
<div class="feature-card">
    <div class="feature-icon">📈</div>
    <div class="feature-title">
        Business Value
    </div>
    <div class="feature-text">
        Help businesses identify high-risk customers,
        understand churn drivers and prioritize
        retention strategies.
    </div>
</div>
""",
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# RETENTION RECOMMENDATIONS
# ------------------------------------------------------------

with row2_col2:

    st.markdown(
        """
<div class="feature-card">
    <div class="feature-icon">💡</div>
    <div class="feature-title">
        Retention Recommendations
    </div>
    <div class="feature-text">
        Generate rule-based retention actions based on
        churn risk, customer characteristics, contract
        type, charges and service usage.
    </div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# TECHNOLOGY STACK TITLE
# ============================================================

st.markdown(
    """
<div style="
    font-size: 22px;
    font-weight: 700;
    color: #0F172A;
    margin-top: 20px;
    margin-bottom: 10px;
">
    Technology Stack
</div>
""",
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# APPLICATION FEATURES
# ============================================================

st.subheader("✨ Application Features")

features = [
    "📂 Upload customer datasets",
    "🤖 Predict customer churn",
    "📊 View churn probability",
    "⚠️ Classify customer risk",
    "💡 Generate retention recommendations",
    "📥 Download prediction results"
]

for feature in features:

    st.markdown(f"- {feature}")


st.divider()


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.markdown(
    """
<div style="
    font-size: 22px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 10px;
">
    Technology Stack
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# TECHNOLOGY COLUMNS
# ============================================================

tech1, tech2, tech3, tech4 = st.columns(4)


with tech1:

    st.markdown("### 🐍 Python")
    st.caption("Pandas • NumPy • Scikit-learn")


with tech2:

    st.markdown("### 🔍 Explainable AI")
    st.caption("SHAP")


with tech3:

    st.markdown("### 📊 BI")
    st.caption("Power BI • SQL")


with tech4:

    st.markdown("### 🌐 Application")
    st.caption("Streamlit")
