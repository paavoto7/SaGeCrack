from flask import Flask
app = Flask(__name__)

def create_app():

    from project import database    

    return app