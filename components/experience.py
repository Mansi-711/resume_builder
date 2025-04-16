import streamlit as st
from utils.state_manager import save_section, get_form_data

def experience_form():
    st.header("💼 Experience")

    role = st.text_input("Role")
    company = st.text_input("Company")
    duration = st.text_input("Duration")
    description = st.text_area("Description")

    if st.button("➕ Add Experience"):
        new_entry = {
            "role": role,
            "company": company,
            "duration": duration,
            "description": description
        }
        save_section("experience", new_entry)
        st.success("Added Experience Entry")

    st.subheader("Saved Entries")
    for i, exp in enumerate(get_form_data()["experience"]):
        st.text(f"{i+1}. {exp['role']} at {exp['company']} - {exp['duration']}")