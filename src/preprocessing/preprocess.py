import fitz
import re
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Cleans and preprocesses the extracted text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Process using spaCy
    doc = nlp(text)

    # Remove stop words and punctuation
    cleaned_words = []

    for token in doc:
        if not token.is_stop and not token.is_punct:
            cleaned_words.append(token.lemma_)

    cleaned_text = " ".join(cleaned_words)

    return cleaned_text
if __name__ == "__main__":

    sample = """
    I am a Data Science student skilled in Python, SQL, Machine Learning and Deep Learning.
    """

    print(preprocess_text(sample))