from app.db.session import engine


def db_status():
    conn = engine.connect()
    conn.close()
