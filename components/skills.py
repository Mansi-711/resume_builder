import streamlit as st
from utils.state_manager import save_section, get_form_data

def skills_form():
    st.header("🧠 Skills")

    soft = st.text_input("Soft Skill")
    hard = st.text_input("Hard Skill")

    if st.button("➕ Add Skills"):
        current_data = get_form_data()["skills"]
        if soft:
            current_data["soft"].append(soft)
        if hard:
            current_data["hard"].append(hard)
        save_section("skills", current_data)
        st.success("Skills added!")

    st.subheader("Soft Skills")
    st.write(", ".join(get_form_data()["skills"]["soft"]))
    st.subheader("Hard Skills")
    st.write(", ".join(get_form_data()["skills"]["hard"]))