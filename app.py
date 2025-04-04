import streamlit as st
from retriever import get_recommendations
from tools import estimate_footprint

st.set_page_config(page_title="EcoAdvisor 🌱", layout="centered")

st.title("🌍 EcoAdvisor")
st.markdown("#### Get personalized tips to live a more sustainable life.")

with st.form("sustainability_form"):
    st.subheader("🏠 Your Lifestyle Details")

    transport = st.selectbox("How do you usually commute?", ["Car", "Public Transport", "Cycle/Walk", "Electric Vehicle"])
    diet = st.selectbox("Your diet type:", ["Meat-heavy", "Mixed", "Vegetarian", "Vegan"])
    electricity = st.slider("Monthly electricity use (kWh)", 50, 1000, 300)
    shopping_freq = st.selectbox("How often do you buy new clothes?", ["Every week", "Monthly", "Rarely", "Only when needed"])

    submitted = st.form_submit_button("Get My Eco Plan")

if submitted:
    footprint_score = estimate_footprint(transport, diet, electricity, shopping_freq)
    recommendations = get_recommendations(transport, diet, electricity, shopping_freq)

    st.success(f"♻️ Your estimated carbon impact score: **{footprint_score}/100** (lower is better)")
    st.markdown("---")
    st.subheader("🌱 Personalized Sustainability Tips")

    for rec in recommendations:
        st.markdown(f"- {rec}")
