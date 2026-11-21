from reportlab.pdfgen import canvas
import streamlit as st
from pypdf import PdfReader
import re
import io
st.set_page_config(page_title="AI Resume Screening", page_icon="📄")
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fc;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

h1 {
    color: #17365d;
    font-weight: 750;
}

.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1746a2;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Resume Screening & Job Matching")
st.write("Smart Resume Analysis | Skill Matching | Career Insights")

st.divider()

st.subheader("📄 Upload Your Resume")
resume = st.file_uploader(
    "Choose your resume",
    type=["pdf"],
    help="Upload your resume in PDF format."
)

st.subheader("📋 Enter Job Description")

job_description = st.text_area(
    "Paste the job requirements here",
    height=180,
    placeholder="Example: Python, Java, SQL, HTML, CSS, React..."
)
skills = [
    "python", "java", "sql", "html", "css",
    "javascript", "react", "flask", "django",
    "machine learning", "data analysis",
    "c++", "c", "excel", "git", "nlp",
    "spring boot", "aws", "docker",
    "rest apis", "microservices", "dbms",
    "oops", "dsa", "github", "api"
]

def find_skills(text):
    text = text.lower()
    found = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            found.append(skill)

    return found

st.divider()

if st.button("🔍 Analyze Resume"):

    if resume is None:
        st.error("Please upload a PDF resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:
        reader = PdfReader(resume)
        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() or ""

        resume_skills = find_skills(resume_text)
        required_skills = find_skills(job_description)

        st.divider()
        st.header("📊 Resume Analysis Results")
        if not required_skills:
            st.warning("No recognized skills found in job description.")

        else:
            matched = [skill for skill in required_skills if skill in resume_skills]
            missing = [skill for skill in required_skills if skill not in resume_skills]
            percentage = (len(matched) / len(required_skills)) * 100
            st.metric("Resume Matching Percentage", f"{percentage:.2f}%")
            st.progress(percentage / 100)

            st.divider()

            st.subheader("✅ Matched Skills")
            st.write(", ".join(matched) if matched else "No matching skills found.")

            st.subheader("❌ Missing Skills")
            st.write(", ".join(missing) if missing else "No missing skills found.")

            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer)

            pdf.drawString(50, 800, "AI Resume Screening Report")
            pdf.drawString(50, 770, f"Matching Percentage: {percentage:.2f}%")
            pdf.drawString(50, 730, "Matched Skills: " + ", ".join(matched))
            pdf.drawString(50, 690, "Missing Skills: " + ", ".join(missing))

            pdf.save()
            buffer.seek(0)

            st.download_button(
                label="📥 Download PDF Report",
                data=buffer,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )
