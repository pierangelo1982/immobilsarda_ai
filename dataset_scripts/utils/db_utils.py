from config.database_postgresql import db
from dotenv import load_dotenv

load_dotenv()

# test db connection
def test_postgres_connection():
    cursor = db.cursor()
    is_postgres_connected = cursor is not None
    if cursor is not None:
        print("Postgres connected")
    else:
        print("Postgres not connected")
    cursor.close()