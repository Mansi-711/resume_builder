import streamlit as st
from utils.state_manager import save_section, get_form_data

def custom_section_form():
    st.header("🛠️ Custom Sections")

    title = st.text_input("Section Title")
    content = st.text_area("Section Content")

    if st.button("➕ Add Custom Section"):
        data = {"title": title, "content": content}
        save_section("custom", data)
        st.success("Custom section added!")

    st.subheader("Saved Custom Sections")
    for key, val in get_form_data()["custom_sections"].items():
        st.text(f"{key}: {val[:50]}...")