from reportlab.pdfgen import canvas
import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(page_title="AI Resume Screening", page_icon="📄")

st.title("AI-Based Resume Screening System")
st.write("Upload your resume and compare it with job requirements.")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Enter Job Description")

skills = [
    "python", "java", "sql", "html", "css",
    "javascript", "react", "flask", "django",
    "machine learning", "data analysis",
    "c++", "c", "excel", "git", "nlp"
]

def find_skills(text):
    text = text.lower()
    found = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            found.append(skill)

    return found


if st.button("Analyze Resume"):

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

        st.subheader("Analysis Results")

        if not required_skills:
            st.warning("No recognized skills found in job description.")

        else:
            matched = [skill for skill in required_skills if skill in resume_skills]

            missing = [ skill for skill in required_skills if skill not in resume_skills]

            percentage = (
                len(matched) / len(required_skills)
            ) * 100

            st.metric("Resume Matching Percentage", f"{percentage:.2f}%")

            st.progress(percentage / 100)
            import io

            pdf_buffer = io.BytesIO()

            pdf = canvas.Canvas(pdf_buffer)

            pdf.drawString(100, 800, "AI Resume Screening Report")
            pdf.drawString(100, 760, f"Matching Score: {percentage:.2f}%")
            pdf.drawString(100, 720, "Matched Skills:")

            y = 690
            for skill in matched:
                pdf.drawString(120, y, skill)
                y -= 25

            y -= 15
            pdf.drawString(100, y, "Missing Skills:")

            y -= 30
            for skill in missing:
                pdf.drawString(120, y, skill)
                y -= 25

            pdf.save()

            st.download_button(
                label="Download PDF Report",
                data=pdf_buffer.getvalue(),
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

            st.subheader("Matched Skills")
            st.text(", ".join(matched)
    if matched else "No matching skills found."
)

 