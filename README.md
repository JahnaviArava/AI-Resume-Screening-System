# AI-Based Resume Screening and Job Matching System

## Project Overview
This project is a Python-based web application that analyzes resumes and compares candidates' skills with job description requirements. It helps identify matching and missing skills and calculates a resume matching percentage.

## Features
- Upload resumes in PDF format.
- Extract text from PDF resumes.
- Identify technical skills from resumes.
- Compare resume skills with job requirements.
- Calculate resume matching percentage.
- Display matched skills and missing skills.
- Generate downloadable PDF analysis reports.

## Technologies Used
- Python
- Streamlit
- PyPDF
- ReportLab
- Regular Expressions

## Project Structure
```text
AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/JahnaviArava/AI-Resume-Screening-System.git
```

2. Open the project folder:
```bash
cd AI-Resume-Screening-System
```

3. Install the required libraries:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Live Demo
https://ai-resume-screening-system-5xv74mlfqgudkgxnacdsv3.streamlit.app/

## GitHub Repository
https://github.com/JahnaviArava/AI-Resume-Screening-System

## Future Enhancements
- Improve skill extraction.
- Add support for more resume formats.
- Enhance resume matching accuracy.
- Improve the user interface.

## Note
This project uses keyword-based skill matching. The matching percentage depends on the recognized skills in the resume and job description.

## Author
Arava Jahnavi Sai Sri
