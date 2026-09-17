from ..document_ingestion.chunker import chunk_document
from .embedder import Embedder


embedder = Embedder()


chunks = chunk_document(
    "sample.pdf",
    chunk_size=500,
    overlap=100
)


texts = [chunk["text"] for chunk in chunks]

embeddings = embedder.embed_texts(texts)


for chunk, embedding in zip(chunks, embeddings):

    chunk["embedding"] = embedding

    print("\n--- Chunk ---")
    print("Chunk ID:", chunk["chunk_id"])
    print("Source:", chunk["source"])
    print("Page:", chunk["page_number"])
    print("Text:", chunk["text"][:200])
    print("Vector dimensions:", len(chunk["embedding"]))
    print("First 10 vector values:", chunk["embedding"][:10])