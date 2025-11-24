# pages/1_Home.py
import streamlit as st
from utils.styles import NAVY, TEAL

st.set_page_config(page_title="LLM-Powered Credit Risk Analyzer", layout="wide")

st.markdown(
    f"""
    <div style='text-align:center; padding:50px; font-family:Inter;'>
        <h1 style='color:{NAVY};'>LLM-Powered Credit Risk Analyzer</h1>
        <h3 style='color:{TEAL};'>Multimodal scoring using numbers + unstructured text</h3>
        <p style='color:#333; font-size:16px; max-width:600px; margin:auto;'>
            Analyze financial applicants with explainable AI insights.
        </p>
    </div>
    """, unsafe_allow_html=True
)

if st.button("🚀 Start Analysis"):
    st.session_state.page = "Upload"
