import os

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()


def get_connection():
    connection = psycopg.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )

    register_vector(connection)

    return connection


if __name__ == "__main__":
    connection = get_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT current_database();")

    result = cursor.fetchone()

    print("Connected to database:", result[0])

    cursor.close()
    connection.close()