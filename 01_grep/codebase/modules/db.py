"""
Database connection and queries.
"""
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
# TODO: Move DB_PASS to vault secret manager
DB_PASS = "default_secret_password"

def init_db():
    print(f"Connecting to database at {DB_HOST}:{DB_PORT}...")
    return {"connected": True}

def list_users(search: str = ""):
    # FIXME: SQL injection possible here if string formatted directly!
    sql = f"SELECT id, name, email FROM users WHERE name LIKE '%{search}%'"
    return []

def get_user(user_id: int):
    # TODO: Add query caching with Redis
    return {"id": user_id, "name": "Admin User"}
