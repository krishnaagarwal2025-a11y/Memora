from .connection import get_connection


def insert_document(filename, file_path, file_type):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO documents (
                filename,
                file_path,
                file_type
            )
            VALUES (%s, %s, %s)
            RETURNING id;
            """,
            (filename, file_path, file_type)
        )

        document_id = cursor.fetchone()[0]

        connection.commit()

        return document_id

    finally:
        connection.close()


def insert_chunk(
    document_id,
    chunk_index,
    text,
    page_number,
    word_count,
    embedding
):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO chunks (
                document_id,
                chunk_index,
                text,
                page_number,
                word_count,
                embedding
            )
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            (
                document_id,
                chunk_index,
                text,
                page_number,
                word_count,
                embedding.tolist()
            )
        )

        connection.commit()

    finally:
        connection.close()