from ..embeddings.embedder import Embedder
from .retrieval import search_similar_chunks


embedder = Embedder()

test_queries = [
    {
        "question": "How does this project use vector embeddings?",
        "expected_page": 4
    },
    {
        "question": "What database does the project use?",
        "expected_page": 4
    },
    {
        "question": "What information is stored about each chunk?",
        "expected_page": 3
    },
    {
        "question": "How will the system evaluate retrieval quality?",
        "expected_page": 5
    },
    {
        "question": "What document formats are supported?",
        "expected_page": 1
    }
]


def evaluate_query(question, expected_page, top_k=3):
    query_embedding = embedder.embed_text(question)

    results = search_similar_chunks(
        query_embedding,
        top_k=top_k
    )

    retrieved_pages = [
        result["page_number"]
        for result in results
    ]

    hit = expected_page in retrieved_pages

    return hit, results


def main():
    total = len(test_queries)
    hits = 0

    print("\n" + "=" * 70)
    print("MORROW RETRIEVAL BASELINE EVALUATION")
    print("=" * 70)

    for test in test_queries:
        question = test["question"]
        expected_page = test["expected_page"]

        hit, results = evaluate_query(
            question,
            expected_page
        )

        if hit:
            hits += 1

        print("\nQuestion:")
        print(question)

        print(f"Expected page: {expected_page}")
        print(
            "Retrieved pages:",
            [result["page_number"] for result in results]
        )

        print("Result:", "PASS" if hit else "FAIL")

        print("\nTop result:")
        print("Chunk ID:", results[0]["chunk_id"])
        print("Similarity:", results[0]["similarity"])
        print("Page:", results[0]["page_number"])

    recall_at_k = hits / total

    print("\n" + "=" * 70)
    print(f"Hits: {hits}/{total}")
    print(f"Recall@3: {recall_at_k:.2%}")
    print("=" * 70)


if __name__ == "__main__":
    main()