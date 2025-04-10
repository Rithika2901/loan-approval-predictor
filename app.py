
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('loan_approval_model.pkl')

st.title("Loan Approval Predictor 💰")
st.markdown("Enter your details to check loan eligibility")

# User input
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
loan_amount_term = st.number_input("Loan Amount Term (in days)", min_value=0.0)
credit_history = st.selectbox("Credit History", ["1", "0"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Encode inputs
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
credit_history = int(credit_history)
property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]

# Predict
input_data = np.array([[gender, married, dependents, education, self_employed,
                        applicant_income, coapplicant_income, loan_amount,
                        loan_amount_term, credit_history, property_area]])

if st.button("Check Eligibility"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Loan will likely be **Approved**")
    else:
        st.error("❌ Loan will likely be **Rejected**")
