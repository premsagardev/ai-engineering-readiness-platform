import pdfplumber as read

def extract_text_from_pdf(filepath: str):
    text_chunks = []

    with read.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text_chunks.append(f"/n-- Page {i+1} ---\n")
                text_chunks.append(page_text)
    

    return "\n".join(text_chunks).strip()