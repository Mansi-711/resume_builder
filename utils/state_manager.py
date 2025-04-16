# utils/state_manager.py

import streamlit as st

def init_session():
    if "form_data" not in st.session_state:
        st.session_state.form_data = {
            "personal": {},
            "education": [],
            "experience": [],
            "projects": [],
            "skills": {"soft": [], "hard": []},
            "certifications": [],
            "awards": [],
            "custom_sections": {},
        }
    if "current_section" not in st.session_state:
        st.session_state.current_section = "personal"

def save_section(section_name, data):
    if section_name in ["education", "experience", "projects", "certifications", "awards"]:
        st.session_state.form_data[section_name].append(data)
    elif section_name == "skills":
        st.session_state.form_data["skills"]["soft"] = data.get("soft", [])
        st.session_state.form_data["skills"]["hard"] = data.get("hard", [])
    elif section_name == "custom":
        key = data.get("title", f"custom_{len(st.session_state.form_data['custom_sections'])+1}")
        st.session_state.form_data["custom_sections"][key] = data.get("content", "")
    else:
        st.session_state.form_data[section_name] = data

def update_current_section(section_name):
    st.session_state.current_section = section_name

def get_form_data():
    return st.session_state.form_data
