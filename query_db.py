import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="test-app-db",
        user="jeff",
        password="test"
    )
