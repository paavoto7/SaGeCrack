from sqlalchemy import create_engine, Table, text

engine = create_engine("sqlite:///test.db")

def login(name, passw):
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
        if not result:
            return False
        if len(result) != 1 or result[0]["password"] != passw:
            return False
        else:
            return result
