import re

def extract_candidate_info(text):

    info = {}

    # -------------------------
    # Name
    # -------------------------
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    info["Name"] = lines[0] if lines else "Not Found"

    # -------------------------
    # Email
    # -------------------------
    email = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text,
        re.IGNORECASE
    )

    info["Email"] = email.group() if email else "Not Found"

    # -------------------------
    # Phone
    # -------------------------
    phone = re.search(
        r'(\+91[\-\s]?)?[6-9]\d{9}',
        text
    )

    info["Phone"] = phone.group() if phone else "Not Found"

    # -------------------------
    # LinkedIn
    # -------------------------
    linkedin = re.search(
        r'(https?://)?(www\.)?linkedin\.com/[^\s]+',
        text,
        re.IGNORECASE
    )

    info["LinkedIn"] = linkedin.group() if linkedin else "Not Found"

    # -------------------------
    # GitHub
    # -------------------------
    github = re.search(
        r'(https?://)?(www\.)?github\.com/[^\s]+',
        text,
        re.IGNORECASE
    )

    info["GitHub"] = github.group() if github else "Not Found"

    return info
if __name__ == "__main__":
    from src.parser.pdf_parser import extract_text_from_pdf

    text = extract_text_from_pdf("uploads/resume.pdf")

    print("========== Extracted Resume Text ==========\n")
    print(text)

    print("\n========== Candidate Info ==========\n")
    print(extract_candidate_info(text))