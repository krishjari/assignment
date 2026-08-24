import streamlit as st
import pandas as pd
import joblib
import pickle
from pathlib import Path

# ==========================================
# LOAD MODEL
# ==========================================

# model = joblib.load("loan_model.pkl")
MODEL_PATH = Path(__file__).parent / "loan_model.pkl"

model = joblib.load(MODEL_PATH)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("💰 Loan Approval Prediction")

st.write(
    "Enter applicant information to predict loan approval."
)


st.divider()


# ==========================================
# INPUTS
# ==========================================

col1, col2, col3 = st.columns(3)


# ------------------------------------------
# COLUMN 1
# ------------------------------------------

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=20,
        value=2
    )

    income_annum = st.number_input(
        "Annual Income",
        min_value=0,
        value=500000,
        step=10000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=500000,
        step=10000
    )

    loan_term = st.number_input(
        "Loan Term",
        min_value=1,
        max_value=50,
        value=10
    )


# ------------------------------------------
# COLUMN 2
# ------------------------------------------

with col2:

    cibil_score = st.number_input(
        "CIBIL Score",
        min_value=0,
        max_value=900,
        value=700
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value",
        min_value=0,
        value=500000,
        step=10000
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value",
        min_value=0,
        value=200000,
        step=10000
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value",
        min_value=0,
        value=300000,
        step=10000
    )


# ------------------------------------------
# COLUMN 3
# ------------------------------------------

with col3:

    bank_asset_value = st.number_input(
        "Bank Asset Value",
        min_value=0,
        value=200000,
        step=10000
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes", "No"]
    )


st.divider()


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button(
    "🔍 Predict Loan Status",
    use_container_width=True
):

    # --------------------------------------
    # CREATE DATAFRAME
    # --------------------------------------

    input_data = pd.DataFrame(
        {
            "no_of_dependents": [no_of_dependents],

            "education": [education],

            "self_employed": [self_employed],

            "income_annum": [income_annum],

            "loan_amount": [loan_amount],

            "loan_term": [loan_term],

            "cibil_score": [cibil_score],

            "residential_assets_value": [
                residential_assets_value
            ],

            "commercial_assets_value": [
                commercial_assets_value
            ],

            "luxury_assets_value": [
                luxury_assets_value
            ],

            "bank_asset_value": [
                bank_asset_value
            ]
        }
    )


    # --------------------------------------
    # PREDICT
    # --------------------------------------

    prediction = model.predict(input_data)[0]


    # --------------------------------------
    # RESULT
    # --------------------------------------

    st.subheader("Prediction Result")


    if prediction == "Approved":

        st.success(
            "✅ Loan Approved"
        )

    else:

        st.error(
            "❌ Loan Rejected"
        )


#     # --------------------------------------
#     # SHOW INPUT
#     # --------------------------------------

#     with st.expander("View Applicant Information"):

#         st.dataframe(
#             input_data,
#             use_container_width=True
#         )
