# pages/5_EvidenceViewer.py
import streamlit as st

st.header("Evidence / Explainability")

st.subheader("SHAP Feature Importance")
st.image("assets/shap_example.png")  # precomputed image of SHAP plot

st.subheader("Text Evidence")
st.write("- 'Customer complained about late refunds.'")
st.write("- 'Supplier email: Invoice overdue for 30 days.'")

st.subheader("LLM Risk Rationale")
st.write("Combined financial stress and high debt ratio → Medium-High Risk")
