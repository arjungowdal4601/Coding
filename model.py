import joblib
import pandas as pd

# Load artifacts
model = joblib.load("artifact/insurance_premium_model.joblib")
scaler_info = joblib.load("artifact/scaler.joblib")
scaler = scaler_info["scaler"]
cols_to_scale = scaler_info["cols_to_scale"]

# Mappings and constants
insurance_plan_map = {"Bronze": 1, "Silver": 2, "Gold": 3}
risk_scores = {
    "diabetes": 6,
    "heart disease": 8,
    "high blood pressure": 6,
    "thyroid": 5,
    "no disease": 0,
    "none": 0
}
min_risk_score = 0
max_risk_score = 14  # e.g. "diabetes & heart disease" = 6 + 8 = 14

# Final feature order from your training
final_feature_order = [
    "age",
    "number_of_dependants",
    "income_lakhs",
    "insurance_plan",
    "genetical_risk",
    "normalized_risk_score",
    "gender_Male",
    "region_Northwest",
    "region_Southeast",
    "region_Southwest",
    "marital_status_Unmarried",
    "bmi_category_Obesity",
    "bmi_category_Overweight",
    "bmi_category_Underweight",
    "smoking_status_Occasional",
    "smoking_status_Regular",
    "employment_status_Salaried",
    "employment_status_Self-Employed"
]

def predict_premium(data: dict) -> float:
    """Predicts the health insurance cost based on the provided data."""
    # Compute normalized risk score from medical_history
    diseases = [d.strip().lower() for d in data["medical_history"].split("&")]
    total_risk = sum(risk_scores.get(d, 0) for d in diseases)
    normalized_risk_score = (total_risk - min_risk_score) / (max_risk_score - min_risk_score)

    # Map insurance plan
    plan_value = insurance_plan_map.get(data["insurance_plan"], 1)

    # Build the feature row
    row = {
        "age": data["age"],
        "number_of_dependants": data["number_of_dependants"],
        "income_lakhs": data["income_lakhs"],
        "insurance_plan": plan_value,
        "genetical_risk": data["genetical_risk"],
        "normalized_risk_score": normalized_risk_score,
        "gender_Male": 1 if data["gender"].strip().lower() == "male" else 0,
        "region_Northwest": 1 if data["region"].strip().lower() == "northwest" else 0,
        "region_Southeast": 1 if data["region"].strip().lower() == "southeast" else 0,
        "region_Southwest": 1 if data["region"].strip().lower() == "southwest" else 0,
        "marital_status_Unmarried": 1 if data["marital_status"].strip().lower() == "unmarried" else 0,
        "bmi_category_Obesity": 1 if data["bmi_category"].strip().lower() == "obesity" else 0,
        "bmi_category_Overweight": 1 if data["bmi_category"].strip().lower() == "overweight" else 0,
        "bmi_category_Underweight": 1 if data["bmi_category"].strip().lower() == "underweight" else 0,
        "smoking_status_Occasional": 1 if data["smoking_status"].strip().lower() == "occasional" else 0,
        "smoking_status_Regular": 1 if data["smoking_status"].strip().lower() == "regular" else 0,
        "employment_status_Salaried": 1 if data["employment_status"].strip().lower() == "salaried" else 0,
        "employment_status_Self-Employed": 1 if data["employment_status"].strip().lower() == "self-employed" else 0,
    }

    # Create DataFrame with correct column order
    X_inference = pd.DataFrame([row], columns=final_feature_order)

    # Apply scaling
    X_inference[cols_to_scale] = scaler.transform(X_inference[cols_to_scale])

    # Predict
    prediction = model.predict(X_inference)[0]
    return float(prediction)
