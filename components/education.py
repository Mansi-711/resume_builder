import streamlit as st
from utils.state_manager import save_section, update_current_section

def education_form():
    st.header("🎓 Education")

    # Initialize input fields
    degree = st.text_input("Degree")
    institute = st.text_input("Institute")
    year = st.text_input("Year")
    location = st.text_input("Location")

    # Add education entry
    if st.button("➕ Add Education"):
        new_entry = {
            "degree": degree,
            "institute": institute,
            "year": year,
            "location": location
        }
        save_section("education", new_entry)
        st.success("Added Education Entry")
        st.rerun()

    # Display saved education entries
    st.subheader("Saved Entries")
    for i, edu in enumerate(st.session_state.form_data["education"]):
        st.text(f"{i+1}. {edu['degree']} - {edu['institute']} ({edu['year']})")

    if st.button("💾 Save & Continue to Experience"):
        update_current_section("experience")
        st.rerun()