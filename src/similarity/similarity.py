from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text, job_description):
    """
    Calculates semantic similarity between resume and job description.
    Returns similarity percentage.
    """

    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([job_description])

    score = cosine_similarity(resume_embedding, jd_embedding)[0][0]

    return float(round(score * 100, 2))


if __name__ == "__main__":

    resume = """
    Python SQL Machine Learning Deep Learning Git Pandas NumPy
    """

    job = """
    We are looking for a Data Scientist with Python,
    SQL, Machine Learning, Pandas and Git skills.
    """

    similarity = calculate_similarity(resume, job)

    print(f"Resume Match Score : {similarity}%")