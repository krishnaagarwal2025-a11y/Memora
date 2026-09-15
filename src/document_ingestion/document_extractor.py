from pathlib import Path

from pdf_extractor import extract_text_from_pdf
from docx_extractor import extract_text_from_docx
from text_extractor import extract_text_from_file


def extract_document(file_path):
    path = Path(file_path)
    extension = path.suffix.lower()

    if extension == ".pdf":
        content = extract_text_from_pdf(file_path)

    elif extension == ".docx":
        content = extract_text_from_docx(file_path)

    elif extension in [".txt", ".md"]:
        content = extract_text_from_file(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")

    for item in content:
        item["source"] = path.name
        item["file_type"] = extension

    return content


if __name__ == "__main__":
    files = [
        "sample.pdf",
        "sample.docx",
        "sample.txt",
        "sample.md"
    ]

    for file in files:
        print(f"\n===== {file} =====")

        result = extract_document(file)

        for item in result:
            print(item)