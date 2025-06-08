import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="fabexample_db",
        user="fabadmin",
        password="fabpass2024",
        host="localhost"
    )
