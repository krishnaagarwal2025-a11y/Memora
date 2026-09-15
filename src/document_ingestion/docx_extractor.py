from docx import Document


def extract_text_from_docx(docx_path):
    document = Document(docx_path)

    pages = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            pages.append({
                "page_number": None,
                "text": text
            })

    return pages


if __name__ == "__main__":
    pages = extract_text_from_docx("sample.docx")

    for page in pages:
        print(f"\n--- Content ---")
        print(page["text"])