from flask import Flask
from flask_session import Session

def create_app():
    app = Flask(__name__)
    from . import pages, auth

    app.register_blueprint(pages.bp)
    app.register_blueprint(auth.bp)

    app.add_url_rule("/", endpoint="/")
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    return app