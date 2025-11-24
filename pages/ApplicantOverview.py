# pages/3_ApplicantOverview.py
import streamlit as st

st.header("Applicant Overview")

# Snapshot Card
st.subheader("Applicant Snapshot")
col1, col2 = st.columns(2)
with col1:
    st.metric("Income", "$120,000")
    st.metric("Debt-to-Income", "35%")
    st.metric("Loan Requested", "$50,000")
with col2:
    st.text("Credit History: Good")
    st.text("Business Info: N/A")

# Tabular Data Summary
st.subheader("Key Metrics")
st.dataframe({
    "Metric": ["Credit Score", "Monthly Income", "Monthly Expenses"],
    "Value": [720, 10000, 6500]
})

# Text Data Summary
st.subheader("Text Data Summary")
st.write("Emails: 35, Transaction Logs: 120, Sentiment: Mostly Negative")
