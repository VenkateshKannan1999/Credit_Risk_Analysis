import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib  # To load the trained model and scaler


# Load your trained model and scaler
# model_path = os.path.join(os.path.dirname(__file__), 'Credit_risk_analysis_model')  # __file__ is not defined in Streamlit
# Use a relative path assuming the model is in the same directory as the script
model_path = 'Credit_risk_analysis_model'  
model = joblib.load(model_path) 


# App title
st.title("Credit Default Prediction App")
st.write("""
This app predicts whether a customer is likely to default on their loan based on their financial and loan-related information.
""")

# Sidebar for user input
st.sidebar.header("Enter Customer Details")

# Input fields
person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30, step=1)
person_income = st.sidebar.number_input("Income", min_value=0, max_value=1_000_000, value=50_000, step=1_000)
person_home_ownership = st.sidebar.selectbox("Home Ownership", options=["RENT", "MORTGAGE", "OWN", "OTHER"])
person_emp_length = st.sidebar.number_input("Employment Length (years)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
loan_intent = st.sidebar.selectbox("Loan Intent", options=["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "DEBTCONSOLIDATION"])
loan_grade = st.sidebar.selectbox("Loan Grade", options=["A", "B", "C", "D", "E", "F", "G"])
loan_amnt = st.sidebar.number_input("Loan Amount", min_value=0.0, max_value=100_000.0, value=10_000.0, step=100.0)
loan_int_rate = st.sidebar.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
cb_person_default_on_file = st.sidebar.selectbox("Previous Default on File", options=["Yes", "No"])
cb_person_cred_hist_length = st.sidebar.number_input("Credit History Length (years)", min_value=0, max_value=50, value=10, step=1)

# Encode categorical features
home_ownership_map = {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3}
loan_intent_map = {"PERSONAL": 0, "EDUCATION": 1, "MEDICAL": 2, "VENTURE": 3, "DEBTCONSOLIDATION": 4}
loan_grade_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
default_on_file_map = {"Yes": 1, "No": 0}

# Prepare data for prediction
input_data = pd.DataFrame([{
    'person_age': person_age,
    'person_income': person_income,
    'person_home_ownership': home_ownership_map[person_home_ownership],
    'person_emp_length': person_emp_length,
    'loan_intent': loan_intent_map[loan_intent],
    'loan_grade': loan_grade_map[loan_grade],
    'loan_amnt': loan_amnt,
    'loan_int_rate': loan_int_rate,
    'cb_person_default_on_file': default_on_file_map[cb_person_default_on_file],
    'cb_person_cred_hist_length': cb_person_cred_hist_length
}])
# Display user inputs
st.subheader("Customer Details")
st.write(input_data)

# Predict default
if st.button("Predict Default"):
    prediction = model.predict(input_data)
    prediction_prob = model.predict_proba(input_data)[:, 1]
    
    if prediction[0] == 1:
        st.error(f"The customer is likely to default! (Probability: {prediction_prob[0] * 100:.2f}%)")
    else:
        st.success(f"The customer is unlikely to default. (Probability: {prediction_prob[0] * 100:.2f}%)")

