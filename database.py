import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

try:
    engine = create_engine("sqlite:///./users.db")
except:
    print("Run create_db.py!")


def login(name, passw):
    # Connect to the database
    with engine.connect() as conn:
        # Get one user
        result = conn.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
        if not result:
            return False
        if len(result) != 3 or not check_password_hash(result["password"], passw):
            return False
        else:
            return result["id"]


def register(name, passw):
    with engine.connect() as conn:
        # Try to register a new user
        try:
            # Create the password hash
            newpass = generate_password_hash(passw)
            conn.execute("INSERT INTO users (username, password) VALUES (?,?)", name, newpass)
            return True
        # Check for usernames already taken
        except IntegrityError as e:
            return "Username already taken"
        # Chekc for other errors
        except Exception:
            return e


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