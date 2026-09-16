from .document_extractor import extract_document


def chunk_text(text, chunk_size=500, overlap=100):

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk_words = words[start:end]

        chunk = " ".join(chunk_words)

        chunks.append(chunk)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def chunk_document(file_path, chunk_size=500, overlap=100):
    document_content = extract_document(file_path)

    chunks = []

    chunk_id = 1

    for item in document_content:
        text = item["text"]

        text_chunks = chunk_text(
            text,
            chunk_size,
            overlap
        )

        for chunk_index, chunk in enumerate(text_chunks):

            chunks.append({
                "chunk_id": chunk_id,
                "chunk_index": chunk_index,
                "text": chunk,
                "word_count": len(chunk.split()),
                "source": item["source"],
                "file_type": item["file_type"],
                "page_number": item["page_number"]
            })

            chunk_id += 1

    return chunks


if __name__ == "__main__":
    chunks = chunk_document(
        "sample.pdf",
        chunk_size=500,
        overlap=100
    )

    for chunk in chunks[:5]:
        print(f"\n--- Chunk {chunk['chunk_id']} ---")
        print(f"Chunk index: {chunk['chunk_index']}")
        print(f"Word count: {chunk['word_count']}")
        print(f"Source: {chunk['source']}")
        print(f"File type: {chunk['file_type']}")
        print(f"Page: {chunk['page_number']}")
        print(f"Text: {chunk['text']}")