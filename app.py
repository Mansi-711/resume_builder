import streamlit as st
from utils.resume_render import build_resume_html
from utils.pdf_generator import save_pdf
from utils.state_manager import init_session, get_form_data, update_current_section
from components.sidebar import sidebar_navigation

# Component Forms
from components.personal_info import personal_info_section
from components.summary import summary_section
from components.education import education_form
from components.experience import experience_form
from components.projects import projects_form
from components.skills import skills_form
from components.awards import awards_form
from components.certificates import certificates_form
from components.custom_section import custom_section_form

import base64
from utils.state_manager import init_session
init_session()

st.set_page_config(page_title="AI Resume Builder", layout="wide")

# Initialize session state
init_session()

# Sidebar Navigation
section = sidebar_navigation()
update_current_section(section)

# Upload Image
img_base64 = ""
with st.sidebar.expander("🖼️ Upload Profile Photo (Optional)"):
    uploaded_image = st.file_uploader("Upload a passport-size portrait image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        img_bytes = uploaded_image.read()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        st.image(img_bytes, width=150, caption="Profile Photo Preview")

# Section Routing
st.title("🧠 AI-Powered Resume Builder")

if section == "Personal Info":
    personal_info_section()
elif section == "Professional Summary":
    summary_section()
elif section == "Education":
    education_form()
elif section == "Experience":
    experience_form()
elif section == "Projects":
    projects_form()
elif section == "Skills":
    skills_form()
elif section == "Awards":
    awards_form()
elif section == "Certificates":
    certificates_form()
elif section == "Custom Section":
    custom_section_form()

# Template and Theme
st.sidebar.markdown("---")
template = st.sidebar.selectbox("🖋️ Resume Template", ["Modern", "Classic", "Elegant", "Creative"])
theme = st.sidebar.selectbox("🎨 Theme", ["Light", "Dark"])

# Resume Generation
if st.sidebar.button("📄 Generate Resume"):
    form_data = get_form_data()

    resume_html = build_resume_html(
        name=form_data["personal"].get("name", ""),
        email=form_data["personal"].get("email", ""),
        phone=form_data["personal"].get("phone", ""),
        linkedin=form_data["personal"].get("linkedin", ""),
        github=form_data["personal"].get("github", ""),
        website=form_data["personal"].get("website", ""),
        summary=form_data.get("summary", ""),
        education=form_data.get("education", []),
        experience=form_data.get("experience", []),
        projects=form_data.get("projects", []),
        soft_skills=form_data.get("skills", {}).get("soft", []),
        hard_skills=form_data.get("skills", {}).get("hard", []),
        awards=form_data.get("awards", []),
        certificates=form_data.get("certifications", []),
        custom_sections=form_data.get("custom_sections", {}),
        theme=theme,
        template=template,
        img_base64=img_base64
    )

    st.components.v1.html(resume_html, height=1100, scrolling=True)
    pdf_path = save_pdf(resume_html)
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name="resume.pdf")