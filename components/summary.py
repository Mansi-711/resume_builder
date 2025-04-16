import streamlit as st

def summary_section():
    st.header("📄 Professional Summary")

    summary = st.text_area("Write a brief professional summary:", height=200, value=st.session_state.get("form_summary", ""))

    if st.button("💾 Save Summary"):
        st.session_state.form_summary = summary
        st.success("Saved Summary")
