from FabExample.db.connection import get_connection

def fetch_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, email FROM users;")
            return cur.fetchall()
