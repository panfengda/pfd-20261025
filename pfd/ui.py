import streamlit as st


def apply_theme():
    st.markdown("""
    <style>
    .stApp {background:#071321;color:#eaf4fb}
    [data-testid="stSidebar"] {background:#0a1b2b;border-right:1px solid #234559}
    .block-container {max-width:1450px;padding-top:1.2rem}
    .hero {padding:24px 26px;border:1px solid #285064;border-radius:16px;
           background:linear-gradient(120deg,#102b40,#0b1b2a 75%);margin-bottom:18px}
    .hero h1 {font-size:2rem; margin:.35rem 0 .4rem;color:#eefaff}
    .hero p {color:#a8c1d0;margin:0}
    .eyebrow {font-size:.72rem;letter-spacing:2px;font-weight:800;color:#5de0e7}
    div[data-testid="stMetric"] {background:#0d2437;border:1px solid #234559;padding:12px;border-radius:12px}
    .small-note {color:#9bb4c5;font-size:.86rem}
    </style>
    """, unsafe_allow_html=True)
