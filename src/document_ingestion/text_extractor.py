def extract_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [
        {
            "page_number": None,
            "text": text
        }
    ]


if __name__ == "__main__":
    pages = extract_text_from_file("sample.txt")

    for page in pages:
        print("\n--- Content ---")
        print(page["text"])