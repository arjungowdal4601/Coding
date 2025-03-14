import streamlit as st
from model import predict_premium

st.title("Health Insurance Cost Predictor")

# 1st Row: Age, Number of Dependants, Income in Lakhs
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
with col2:
    dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0)
with col3:
    income = st.number_input("Income in Lakhs", min_value=0.0, max_value=1000.0, value=5.0)

# 2nd Row: Genetical Risk, Insurance Plan, Employment Status
col4, col5, col6 = st.columns(3)

with col4:
    # Integer from 0 to 10 with step=1, starting at 0
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=10, value=0, step=1)
with col5:
    plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
with col6:
    employment = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Unemployed"])

# 3rd Row: Gender, Marital Status, BMI Category
col7, col8, col9 = st.columns(3)

with col7:
    gender = st.selectbox("Gender", ["Male", "Female"])
with col8:
    marital = st.selectbox("Marital Status", ["Married", "Unmarried"])
with col9:
    bmi = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obesity"])

# 4th Row: Smoking Status, Region, Medical History
col10, col11, col12 = st.columns(3)

with col10:
    smoking = st.selectbox("Smoking Status", ["No Smoking", "Occasional", "Regular"])
with col11:
    region = st.selectbox("Region", ["Northwest", "Southeast", "Southwest", "Northeast"])
with col12:
    medical_options = [
        "No Disease", 
        "Diabetes", 
        "Heart Disease", 
        "High Blood Pressure", 
        "Thyroid", 
        "Diabetes & Heart Disease", 
        "High Blood Pressure & Thyroid"
    ]
    medical_history = st.selectbox("Medical History", medical_options)

# Button
if st.button("Predict"):
    # Build the input dictionary
    input_data = {
        "age": age,
        "number_of_dependants": dependants,
        "income_lakhs": income,
        "genetical_risk": genetical_risk,
        "insurance_plan": plan,
        "gender": gender,
        "region": region,
        "marital_status": marital,
        "bmi_category": bmi,
        "smoking_status": smoking,
        "employment_status": employment,
        "medical_history": medical_history
    }
    
    try:
        prediction = predict_premium(input_data)
        st.success(f"Predicted Health Insurance Cost: {prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
