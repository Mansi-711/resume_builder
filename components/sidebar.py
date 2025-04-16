import streamlit as st

# Define the default sections
SECTIONS = [
    "Personal Info",
    "Professional Summary",
    "Education",
    "Experience",
    "Skills",
    "Projects",
    "Awards",
    "Certificates",
    "Custom Section"
]

def sidebar_navigation():
    st.sidebar.title("Resume Sections")
    section = st.sidebar.radio("Go to", SECTIONS)
    return section

def add_custom_section():
    st.sidebar.markdown("---")
    if st.sidebar.button("Add Custom Section"):
        custom_label = st.sidebar.text_input("Custom Section Name", key="custom_section")
        if custom_label and custom_label not in SECTIONS:
            SECTIONS.append(custom_label)
            st.experimental_rerun()
