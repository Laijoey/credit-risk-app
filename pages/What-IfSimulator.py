# pages/6_WhatIfSimulator.py
import streamlit as st

st.header("What-If Simulator")

income = st.slider("Monthly Income", 0, 20000, 10000)
debt_ratio = st.slider("Debt-to-Income Ratio (%)", 0, 100, 35)
loan = st.slider("Loan Amount Requested", 0, 100000, 50000)

risk_score = max(0, min(100, 63 - (income-10000)/1000 + (debt_ratio-35)*0.5))
st.metric("Predicted Risk Score", f"{risk_score:.1f}")
