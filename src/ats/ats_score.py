from src.parser.pdf_parser import extract_text_from_pdf
from src.preprocessing.preprocess import preprocess_text
from src.skills.extract_skills import load_skills, extract_skills
from src.similarity.similarity import calculate_similarity


def calculate_ats_score(resume_path, job_description_path):
    """
    Calculates the ATS score by combining:
    - Semantic similarity
    - Skill match percentage
    """

    # -----------------------------
    # Read Resume
    # -----------------------------
    resume_text = extract_text_from_pdf(resume_path)

    # -----------------------------
    # Read Job Description
    # -----------------------------
    with open(job_description_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    # -----------------------------
    # Preprocess Text
    # -----------------------------
    clean_resume = preprocess_text(resume_text)
    clean_jd = preprocess_text(job_description)

    # -----------------------------
    # Load Skills
    # -----------------------------
    skills = load_skills("data/skills/skills.csv")

    # -----------------------------
    # Extract Skills
    # -----------------------------
    resume_skills = extract_skills(clean_resume, skills)
    jd_skills = extract_skills(clean_jd, skills)

    # -----------------------------
    # Matching & Missing Skills
    # -----------------------------
    matched_skills = sorted(list(set(resume_skills) & set(jd_skills)))
    missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))

    # -----------------------------
    # Skill Match Score
    # -----------------------------
    if len(jd_skills) > 0:
        skill_score = (len(matched_skills) / len(jd_skills)) * 100
    else:
        skill_score = 0

    # Convert to Python float
    skill_score = float(round(skill_score, 2))

    # -----------------------------
    # Semantic Similarity Score
    # -----------------------------
    similarity_score = calculate_similarity(clean_resume, clean_jd)
    similarity_score = float(round(similarity_score, 2))

    # -----------------------------
    # Final ATS Score
    # -----------------------------
    ats_score = float(
        round(
            (0.6 * similarity_score) +
            (0.4 * skill_score),
            2
        )
    )

    # -----------------------------
    # Return Result
    # -----------------------------
    return {
    "ATS Score": ats_score,
    "Similarity Score": similarity_score,
    "Skill Score": skill_score,
    "Matched Skills": matched_skills,
    "Missing Skills": missing_skills,

    # NEW
    "Resume Text": resume_text,
    "Job Description": job_description
}


# =====================================================
# TESTING
# =====================================================

if __name__ == "__main__":

    result = calculate_ats_score(
        "data/resumes/resume.pdf",
        "data/job_descriptions/data_scientist.txt"
    )

    print("\n========== ATS ANALYSIS ==========\n")

    print(f"ATS Score         : {result['ATS Score']}%")
    print(f"Similarity Score  : {result['Similarity Score']}%")
    print(f"Skill Match Score : {result['Skill Score']}%")

    print("\nMatched Skills")
    print("-------------------------")
    for skill in result["Matched Skills"]:
        print(f"✓ {skill}")

    print("\nMissing Skills")
    print("-------------------------")
    for skill in result["Missing Skills"]:
        print(f"✗ {skill}")