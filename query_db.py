import psycopg2

def get_db_connection():
    return psycopg2.connect(
        database="test_db",
        user="postgres",
        password="password",
        host="database-2.cazthivdigzb.us-east-1.rds.amazonaws.com",
        port="5432"
    )