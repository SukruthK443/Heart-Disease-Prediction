import streamlit as st
import pandas as pd
import joblib

model = joblib.load('heart_model_pipeline.pkl')

st.title("❤️ Heart Disease Prediction")
st.write("""
This app predicts the likelihood of **Heart Disease** based on several health parameters. 
Please fill in the details below, and click **Predict** to see the results.
""")

normal_values = {
    "Age": 54,
    "Sex": "Male",
    "ChestPainType": "ATA (Typical Angina)",
    "RestingBP": 130,
    "Cholesterol": 220,
    "FastingBS": "No",
    "RestingECG": "Normal",
    "MaxHR": 140,
    "ExerciseAngina": "No",
    "Oldpeak": 1.0,
    "ST_Slope": "Up (Upsloping)"
}

st.subheader("Please enter the following details:")

Age = st.number_input("Age", min_value=1, max_value=120, step=1, value=int(normal_values["Age"]))

Sex = st.selectbox("Sex", ["Male", "Female"], index=["Male", "Female"].index(normal_values["Sex"]))

ChestPainType = st.selectbox("Chest Pain Type", ["ATA (Typical Angina)", "NAP (Atypical Angina)", "ASY (Non-Anginal Pain)", "TA (Tightness of Chest)"],
    index=["ATA (Typical Angina)", "NAP (Atypical Angina)", "ASY (Non-Anginal Pain)", "TA (Tightness of Chest)"].index(normal_values["ChestPainType"]))

RestingBP = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=normal_values["RestingBP"])

Cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=1000, value=normal_values["Cholesterol"])

FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"], index=["No", "Yes"].index(normal_values["FastingBS"]))

RestingECG = st.selectbox("Resting ECG Results", ["Normal", "ST (ST-T wave abnormality)", "LVH (Left Ventricular Hypertrophy)"],
    index=["Normal", "ST (ST-T wave abnormality)", "LVH (Left Ventricular Hypertrophy)"].index(normal_values["RestingECG"]))

MaxHR = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, value=normal_values["MaxHR"])

ExerciseAngina = st.selectbox("Exercise-Induced Angina", ["No", "Yes"], index=["No", "Yes"].index(normal_values["ExerciseAngina"]))

Oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, format="%.1f", value=normal_values["Oldpeak"])

ST_Slope = st.selectbox("ST Slope", ["Up (Upsloping)", "Flat", "Down (Downsloping)"],
    index=["Up (Upsloping)", "Flat", "Down (Downsloping)"].index(normal_values["ST_Slope"]))

input_data = pd.DataFrame([{
    "Age": Age,
    "Sex": 1 if Sex == "Male" else 0,
    "ChestPainType": ChestPainType,
    "RestingBP": RestingBP,
    "Cholesterol": Cholesterol,
    "FastingBS": 1 if FastingBS == "Yes" else 0,
    "RestingECG": RestingECG,
    "MaxHR": MaxHR,
    "ExerciseAngina": 1 if ExerciseAngina == "Yes" else 0,
    "Oldpeak": Oldpeak,
    "ST_Slope": ST_Slope
}])

if st.button("Predict"):
    try:
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("🚨 The model predicts: **Heart Disease Detected**.")
        else:
            st.success("✅ The model predicts: **No Heart Disease**.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
