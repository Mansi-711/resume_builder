import streamlit as st

def projects_form():
    st.header("🛠️ Projects")

    # Initialize session state for projects
    if 'data' not in st.session_state:
        st.session_state.data = {
            "education": [],
            "experience": [],
            "skills_soft": [],
            "skills_hard": [],
            "projects": [],
            "certificates": [],
            "awards": [],
            "custom_sections": {}
        }

    title = st.text_input("Project Title")
    description = st.text_area("Description")

    if st.button("➕ Add Project"):
        if title and description:
            st.session_state.data['projects'].append({
                "title": title,
                "description": description
            })
            st.success("Added Project")
            st.rerun()  # Optional: Refresh the form

    st.subheader("Saved Entries")
    for i, p in enumerate(st.session_state.data['projects']):
        st.text(f"{i+1}. {p['title']}")
