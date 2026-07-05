import pandas as pd


def load_skills(csv_path):
    """
    Load all skills from skills.csv
    """
    skills = pd.read_csv(csv_path, header=None)

    skills_list = skills[0].str.lower().tolist()

    return skills_list


def extract_skills(text, skills_list):
    """
    Extract matching skills from text.
    """

    found_skills = []

    text = text.lower()

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))


# Testing

if __name__ == "__main__":

    skills = load_skills("data/skills/skills.csv")

    sample_text = """
    I know Python, SQL, Machine Learning,
    Deep Learning and Git.
    """

    extracted = extract_skills(sample_text, skills)

    print(extracted)