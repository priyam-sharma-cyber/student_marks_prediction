import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("student_marks_model.pkl", "rb"))

st.title("🎓 Student Marks Prediction")

st.write("Enter study hours to predict marks.")

hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

if st.button("Predict Marks"):
    prediction = model.predict([[hours]])

    st.success(
        f"Predicted Marks: {prediction[0\]:.2f}"
    )
