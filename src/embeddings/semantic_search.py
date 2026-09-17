from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from ..document_ingestion.chunker import chunk_document


MODEL_NAME = "all-MiniLM-L6-v2"


model = SentenceTransformer(MODEL_NAME)


# 1. Create chunks
chunks = chunk_document(
    "sample.pdf",
    chunk_size=500,
    overlap=100
)


# 2. Create embeddings for all chunks
chunk_texts = [chunk["text"] for chunk in chunks]

chunk_embeddings = model.encode(
    chunk_texts,
    convert_to_numpy=True
)


# 3. User's question
query = "Where is the numerical representation of document meaning used?"


# 4. Convert question into an embedding
query_embedding = model.encode(
    query,
    convert_to_numpy=True
)


# 5. Compare query with every chunk
similarities = cosine_similarity(
    query_embedding.reshape(1, -1),
    chunk_embeddings
)[0]


# 6. Attach similarity score to each chunk
for chunk, similarity in zip(chunks, similarities):

    chunk["similarity"] = float(similarity)


# 7. Sort by similarity
ranked_chunks = sorted(
    chunks,
    key=lambda x: x["similarity"],
    reverse=True
)


# 8. Display results
print("\nQuery:")
print(query)

print("\nTop relevant chunks:\n")

for chunk in ranked_chunks[:3]:

    print("-" * 60)

    print("Chunk ID:", chunk["chunk_id"])
    print("Similarity:", chunk["similarity"])
    print("Source:", chunk["source"])
    print("Page:", chunk["page_number"])

    print("\nText:")
    print(chunk["text"])