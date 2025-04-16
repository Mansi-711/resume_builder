# 🧠 AI Resume Builder

An AI-powered, multi-step resume builder built with Streamlit that helps users generate professional resumes effortlessly. It features multiple customizable templates, real-time preview, PDF export, Google Sign-In, and dynamic content entry — all in a sleek and modern UI.

---

## 📸 Preview

![Sidebar Template Preview](https://drive.google.com/file/d/1TWQoEZyi-uFZbbzn70KMpVM_mLTV731r/view?usp=sharing)

---

## ✨ Features

- 🔢 **Multi-step Form Navigation** via Sidebar
- 🎨 **Professional Templates** (Modern, Classic, Elegant, Creative, Sidebar)
- 🖼️ **Profile Photo Support** (Passport-sized)
- 🔄 **Dynamic Sections**: Add multiple entries for education, experience, awards, certifications, and more
- ⚙️ **Custom Sections** support for advanced customization
- 🔐 **Google Sign-In Integration** (via Firebase)
- 👁️ **Live Resume Preview** while filling form
- 📄 **Export as PDF** (High-resolution and print-ready)
- ☁️ **Cloud Save Ready** (Firebase storage-compatible)

---

## 🛠️ Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| 💻 Frontend   | Streamlit           |
| 🎨 Templates  | HTML + Jinja2       |
| 🔐 Auth       | Firebase (Google Sign-In) |
| 📄 Export     | pdfkit / weasyprint |
| 🧠 AI Logic   | Python + Streamlit Session State |
| 📦 Styling    | CSS in `assets/`     |

## ▶️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/ai-resume-builder.git
   cd ai-resume-builder
2. **Create virtual environment**

'''python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies'''

3. **Install dependencies**
'''pip install -r requirements.txt
Run the app'''

4. **Run the app**
'''streamlit run app.py'''
   

