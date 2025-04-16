import streamlit as st
from utils.state_manager import save_section, get_form_data

def certificates_form():
    st.header("📜 Certifications")

    title = st.text_input("Certificate Title")
    issuer = st.text_input("Issuer")
    link = st.text_input("Certificate Link")

    if st.button("➕ Add Certificate"):
        new_entry = {"title": title, "issuer": issuer, "link": link}
        save_section("certifications", new_entry)
        st.success("Certificate added!")

    st.subheader("Saved Certificates")
    for i, cert in enumerate(get_form_data()["certifications"]):
        st.text(f"{i+1}. {cert['title']} by {cert['issuer']}")