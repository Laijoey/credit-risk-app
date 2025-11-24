# pages/4_RiskDashboard.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.header("Credit Risk Dashboard")

# Top Risk Card
st.markdown("""
<div style='background-color:#2AC3A9; padding:30px; border-radius:15px; color:white; text-align:center'>
    <h1>Risk Score: 63 / 100</h1>
    <h3>Risk Rating: Medium</h3>
</div>
""", unsafe_allow_html=True)

# Three-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Tabular Risk Factors")
    df = pd.DataFrame({
        "Feature": ["Debt-to-income ratio", "Credit inquiries", "Monthly cash flow"],
        "Impact": [24, 13, -10]
    })
    fig = px.bar(df, x="Impact", y="Feature", orientation="h", text="Impact", color="Impact")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Text Intelligence")
    st.write("- Recurring refund disputes detected")
    st.write("- Supplier email indicates delayed invoice payments")
    st.write("- Sentiment trend: 30% negative messages")

with col3:
    st.subheader("Multimodal Fusion")
    st.write("Text signals increase risk by +15%. Tabular features +22%. Final score = 63.")
