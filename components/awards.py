import streamlit as st
from utils.state_manager import save_section, get_form_data

def awards_form():
    st.header("🏆 Awards")

    title = st.text_input("Award Title")
    organization = st.text_input("Awarded By")
    year = st.text_input("Year")

    if st.button("➕ Add Award"):
        new_entry = {"title": title, "organization": organization, "year": year}
        save_section("awards", new_entry)
        st.success("Award added!")

    st.subheader("Saved Awards")
    for i, award in enumerate(get_form_data()["awards"]):
        st.text(f"{i+1}. {award['title']} by {award['organization']} ({award['year']})")
