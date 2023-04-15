import PyPDF2


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    num_pages = len(pdf_reader.pages)

    text = ""
    # Iterate through each page and extract the text
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        text = text + page.extract_text()

    return text


def split_text_into_chunks(plain_text, max_chars=2000):
    text_chunks = []
    current_chunk = ""
    for line in plain_text.split("\n"):
        if len(current_chunk) + len(line) + 1 <= max_chars:
            current_chunk += line + " "
        else:
            text_chunks.append(current_chunk.strip())
            current_chunk = line + " "
    if current_chunk:
        text_chunks.append(current_chunk.strip())
    return text_chunks
