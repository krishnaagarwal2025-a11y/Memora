from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "PostgreSQL can store vector embeddings using pgvector.",
    "pgvector allows PostgreSQL to work with vector data.",
    "I went to the cafeteria and had lunch."
]


embeddings = model.encode(sentences)


similarity_matrix = cosine_similarity(embeddings)


print("\nCosine Similarity Matrix:\n")

print(similarity_matrix)