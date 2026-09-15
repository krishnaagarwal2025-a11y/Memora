import pymupdf


def extract_text_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        pages.append({
            "page_number": page_number,
            "text": text
        })

    document.close()

    return pages


if __name__ == "__main__":
    pages = extract_text_from_pdf("sample.pdf")

    for page in pages:
        print(f"\n--- Page {page['page_number']} ---")
        print(page["text"])