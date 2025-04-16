import os
from jinja2 import Environment, FileSystemLoader

def build_resume_html(name, email, phone, linkedin, github, website, summary,
                      education, experience, projects, soft_skills, hard_skills,
                      awards, certificates, custom_sections,
                      theme="Light", template="Modern", img_base64=""):

    templates_path = os.path.join("templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template_file = template.lower() + ".html"

    try:
        template = env.get_template(template_file)
    except Exception as e:
        raise FileNotFoundError(f"Template '{template_file}' not found in templates/. {e}")

    # Format Education
    formatted_education = [
        f"{e.get('degree', '')}, {e.get('institute', '')} ({e.get('year', '')}) - {e.get('location', '')}"
        for e in education if isinstance(e, dict)
    ]

    # Format Experience
    formatted_experience = [
        {
            "role": e.get("role", ""),
            "company": e.get("company", ""),
            "duration": e.get("duration", ""),
            "desc": e.get("description", "")
        }
        for e in experience if isinstance(e, dict)
    ]

    # Format Projects
    formatted_projects = [
        {
            "title": p.get("title", ""),
            "desc": p.get("description", "")
        }
        for p in projects if isinstance(p, dict)
    ]

    # Format Custom Sections
    formatted_custom = [
        {"title": k, "content": v} for k, v in custom_sections.items()
    ]

    # Prepare context for the template
    context = {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "website": website,
        "summary": summary,
        "education": formatted_education,
        "experience": formatted_experience,
        "projects": formatted_projects,
        "soft_skills": [s.strip() for s in soft_skills if s.strip()],
        "hard_skills": [s.strip() for s in hard_skills if s.strip()],
        "awards": [a.get("title", "") if isinstance(a, dict) else str(a) for a in awards],
        "certifications": [c.get("title", "") if isinstance(c, dict) else str(c) for c in certificates],
        "custom_sections": formatted_custom,
        "img_base64": img_base64,
        "theme": theme
    }

    return template.render(context)