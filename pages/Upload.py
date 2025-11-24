# pages/2_Upload.py
import streamlit as st
import pandas as pd

st.header("Upload Applicant Data")

tab1, tab2, tab3 = st.tabs(["CSV Upload", "Text Files", "Demo Applicant"])

with tab1:
    uploaded_csv = st.file_uploader("Upload tabular CSV", type="csv")
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.dataframe(df.head())

with tab2:
    uploaded_txt = st.file_uploader("Upload text files", type="txt", accept_multiple_files=True)
    if uploaded_txt:
        for f in uploaded_txt:
            st.text(f"{f.name}: {f.read().decode('utf-8')[:200]}...")

with tab3:
    demo = st.selectbox("Select Demo Applicant", ["Applicant 1", "Applicant 2"])
    st.write(f"You selected {demo}")

if st.button("Analyze Risk"):
    st.session_state.page = "ApplicantOverview"
