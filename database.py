from sqlalchemy import create_engine
from werkzeug.security import check_password_hash, generate_password_hash

engine = create_engine("sqlite:///project/test.db")

def login(name, passw):
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
        if not result:
            return False
        if len(result) != 3 or not check_password_hash(result["password"], passw):
            return False
        else:
            return result["id"]


def register(name, passw):
    with engine.connect() as conn:
        try:
            newpass = generate_password_hash(passw)
            conn.execute("INSERT INTO users (username, password) VALUES (?,?)", name, newpass)
            return True
        except:
            return False


def save(id, name, service, passw):
    with engine.connect() as conn:
        if not id or not name or not service or not passw:
            return False
        try:
            conn.execute("INSERT INTO passwords (id, service, username, password) VALUES(?, ?, ?, ?)", id, service, name, passw)
            return True
        except:
            return False


def get_saved(service, id):
    with engine.connect() as conn:

        # Transform tuple rows to dictionaries
        rows = [dict(row) for row in conn.execute("SELECT * FROM passwords WHERE service LIKE ? AND id=?", (service,id)).fetchall()]

        print(rows)
        return rows  