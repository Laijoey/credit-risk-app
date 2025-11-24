import streamlit as st
import pandas as pd
import numpy as np

st.title("Credit Risk App ✅")

st.write("This is a minimal working version. Replace with your own model and logic.")

# Example user input
age = st.number_input("Enter age", min_value=18, max_value=100, value=30)
income = st.number_input("Enter annual income ($)", min_value=0, value=50000)

# Dummy prediction logic
risk_score = np.random.rand()  # Replace with your model
st.write(f"Predicted credit risk score: {risk_score:.2f}")
