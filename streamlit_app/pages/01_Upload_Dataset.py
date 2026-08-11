import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Upload Dataset",
    page_icon="📂",
    layout="wide"
)


st.title("📂 Upload Customer Dataset")

st.markdown(
    """
    Upload a customer CSV file to analyze churn risk and generate
    data-driven retention insights.
    """
)

st.divider()


uploaded_file = st.file_uploader(
    "Choose a customer CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    st.success("Dataset uploaded successfully.")

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.subheader("Dataset Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Total Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )

    required_features = [
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "InternetService",
        "Contract",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges"
    ]

    missing_columns = [
        column
        for column in required_features
        if column not in df.columns
    ]

    st.subheader("Dataset Validation")

    if missing_columns:

        st.error(
            "The uploaded dataset is missing required columns."
        )

        st.write(
            "Missing columns:",
            missing_columns
        )

    else:

        st.success(
            "Dataset contains all required prediction features."
        )

        st.session_state["uploaded_data"] = df

        st.info(
            "Your dataset is ready for churn prediction."
        )