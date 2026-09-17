from ..document_ingestion.chunker import chunk_document
from ..embeddings.embedder import Embedder
from .repository import insert_document, insert_chunk


FILE_PATH = "sample.pdf"


def ingest_document(file_path):
    print("Starting document ingestion...")

    # Step 1: Extract and chunk the document
    chunks = chunk_document(
        file_path,
        chunk_size=500,
        overlap=100
    )

    print(f"Created {len(chunks)} chunks.")

    # Step 2: Create embeddings
    embedder = Embedder()

    texts = [chunk["text"] for chunk in chunks]
    embeddings = embedder.embed_texts(texts)

    print(f"Generated {len(embeddings)} embeddings.")

    # Step 3: Insert document metadata
    document_id = insert_document(
        filename=file_path.split("\\")[-1],
        file_path=file_path,
        file_type=".pdf"
    )

    print(f"Inserted document with ID: {document_id}")

    # Step 4: Insert chunks + embeddings
    for chunk, embedding in zip(chunks, embeddings):
        insert_chunk(
            document_id=document_id,
            chunk_index=chunk["chunk_index"],
            text=chunk["text"],
            page_number=chunk["page_number"],
            word_count=chunk["word_count"],
            embedding=embedding
        )

    print(f"Inserted {len(chunks)} chunks into PostgreSQL.")
    print("Document ingestion completed successfully.")


if __name__ == "__main__":
    ingest_document(FILE_PATH)