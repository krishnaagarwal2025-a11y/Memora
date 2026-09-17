from .connection import get_connection


def search_similar_chunks(query_embedding, top_k=5):
    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                chunks.id,
                chunks.document_id,
                chunks.chunk_index,
                chunks.text,
                chunks.page_number,
                chunks.word_count,
                1 - (chunks.embedding <=> %s) AS similarity
            FROM chunks
            WHERE chunks.embedding IS NOT NULL
            ORDER BY chunks.embedding <=> %s
            LIMIT %s;
            """,
            (
                query_embedding,
                query_embedding,
                top_k
            )
        )

        rows = cursor.fetchall()

        results = []

        for row in rows:
            results.append({
                "chunk_id": row[0],
                "document_id": row[1],
                "chunk_index": row[2],
                "text": row[3],
                "page_number": row[4],
                "word_count": row[5],
                "similarity": float(row[6])
            })

        return results

    finally:
        connection.close() 