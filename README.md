# 🚀 ATS Resume Screening System

An AI-powered **Applicant Tracking System (ATS) Resume Screening** application that evaluates resumes against job descriptions using Natural Language Processing (NLP). The system calculates an ATS match score, extracts important skills, identifies missing keywords, and provides a detailed resume analysis.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 📝 Upload Job Description
- 🎯 ATS Match Score Calculation
- 🔍 Missing Keyword Detection
- 🧠 Resume Summary Generation
- 💼 Skill Extraction
- 📊 Candidate Evaluation Report
- ⚡ Fast and User-Friendly Interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| NLP | spaCy, NLTK |
| PDF Processing | PyPDF2 |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |

---

## 📂 Project Structure

```
ATS-Resume-Screening/
│
├── data/
│
├── src/
│   ├── ats/
│   ├── candidate/
│   ├── parser/
│   ├── preprocessing/
│   ├── recommendation/
│   ├── report/
│   ├── similarity/
│   ├── skills/
│   ├── summary/
│   └── utils/
│
├── uploads/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/bhargavi928/ATS-Resume-Screening.git
```

### Navigate to the Project

```bash
cd ATS-Resume-Screening
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a candidate's resume in PDF format.
2. Upload the job description.
3. The system extracts text from both documents.
4. Resume content is preprocessed using NLP techniques.
5. Skills and keywords are extracted.
6. Resume and job description similarity is calculated.
7. ATS score is generated.
8. A detailed analysis report is displayed.

---

## 📊 Output

The system provides:

- ✅ ATS Match Score
- ✅ Resume Summary
- ✅ Skill Match Analysis
- ✅ Missing Keywords
- ✅ Candidate Recommendations
- ✅ Final Evaluation Report

---

## 🚀 Future Enhancements

- AI-powered Resume Improvement Suggestions
- Resume Ranking for Multiple Candidates
- Dashboard with Analytics
- Recruiter Login System
- Interview Question Recommendations
- Support for DOCX and TXT resumes
- Cloud Deployment

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
    home.png
    result.png
```

```markdown
![Home Page](screenshots/home.png)

![Result Page](screenshots/result.png)
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👩‍💻 Author

**Bhargavi Gujja**

B.Tech Final Year Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Software Development

GitHub: https://github.com/bhargavi928
