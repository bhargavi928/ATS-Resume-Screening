def generate_summary(
    ats_score,
    similarity_score,
    skill_score,
    matched_skills,
    missing_skills
):
    """
    Generate an AI-style resume summary.
    """

    # Resume status
    if ats_score >= 85:
        status = "excellent"
    elif ats_score >= 70:
        status = "good"
    elif ats_score >= 50:
        status = "average"
    else:
        status = "poor"

    # Top matched skills
    matched = ", ".join(matched_skills[:5])

    # Top missing skills
    missing = ", ".join(missing_skills[:5])

    summary = f"""
Your resume has an ATS score of {ats_score:.2f}%,
indicating an {status} match for the selected job role.

The resume demonstrates strong knowledge in
{matched}.

However, important skills such as
{missing}
are currently missing.

The similarity score is {similarity_score:.2f}%,
while the skill match score is {skill_score:.2f}%.

Adding the missing technologies through projects,
certifications and practical experience will
significantly improve your ATS score and increase
your chances of getting shortlisted.
"""

    return summary.strip()


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    summary = generate_summary(
        ats_score=58.31,
        similarity_score=68.61,
        skill_score=42.86,
        matched_skills=[
            "Python",
            "SQL",
            "TensorFlow",
            "Git",
            "AWS"
        ],
        missing_skills=[
            "Docker",
            "Power BI",
            "Machine Learning",
            "NumPy",
            "Flask"
        ]
    )

    print(summary)