import streamlit as st

def personal_info_section():
    st.header("👤 Personal Information")

    name = st.text_input("Full Name", value=st.session_state.get("form_name", ""))
    email = st.text_input("Email", value=st.session_state.get("form_email", ""))
    phone = st.text_input("Phone", value=st.session_state.get("form_phone", ""))
    linkedin = st.text_input("LinkedIn", value=st.session_state.get("form_linkedin", ""))
    github = st.text_input("GitHub", value=st.session_state.get("form_github", ""))
    website = st.text_input("Website", value=st.session_state.get("form_website", ""))

    if st.button("💾 Save Personal Info"):
        st.session_state.form_name = name
        st.session_state.form_email = email
        st.session_state.form_phone = phone
        st.session_state.form_linkedin = linkedin
        st.session_state.form_github = github
        st.session_state.form_website = website
        st.success("Saved Personal Information")