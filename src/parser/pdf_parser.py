import fitz  # PyMuPDF

import fitz

def extract_text_from_pdf(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        # Extract visible text
        text += page.get_text()

        # Extract hyperlinks
        links = page.get_links()

        for link in links:
            if "uri" in link:
                text += "\n" + link["uri"]

    doc.close()

    return text


# Testing

if __name__ == "__main__":

    pdf_path = "data/resumes/resume.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    print(extracted_text)