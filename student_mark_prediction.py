import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Student Marks Prediction")

hours = st.number_input("Study Hours", min_value=0.0)

if st.button("Predict"):
    prediction = model.predict([[hours]])
    st.success(f"Predicted Marks: {prediction[0\]:.2f}")
