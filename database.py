from sqlalchemy import create_engine, Table, text
from werkzeug.security import check_password_hash, generate_password_hash

engine = create_engine("sqlite:///test.db")

def login(name, passw):
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
        if not result:
            return False
        if len(result) != 3 or result["password"] != passw:
            return False
        else:
            return result

def register(name, passw):
    with engine.connect() as conn:
        try:
            newpass = generate_password_hash(passw)
            conn.execute("INSERT INTO users (username, password) VALUES (?,?)", name, passw)
            return True
        except:
            return False


def save(id, name, service, passw):
    with engine.connect() as conn:
        try:
            message = conn.execute("INSERT INTO passwords (id, service, username, password) VALUES(?, ?, ?, ?)", id, service, name, passw)
            return True
        except:
            return False