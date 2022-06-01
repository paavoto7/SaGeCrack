
from flask import Flask, redirect, render_template, request, jsonify, session
from flask_session import Session
from flask import Blueprint

bp = Blueprint("pages", __name__)

from project.functions import cracker, login_required # generator
from project.database import login, register, save

# Configure application
app = Flask(__name__)


@bp.route("/")
def cracking():
    return render_template("index.html")


@bp.route("/cracker")
def crack():
    # Return page if get
    return render_template("cracker.html")


@bp.route("/cracked")
def cracked():
    passw = request.args.get("passw", default='')
    type = request.args.get("type", type=int)

    # Hand the information to the cracker function    
    past = cracker(passw, type)
    # Jsonify the result for jquery
    return jsonify(result=past[0], time=past[1])


@bp.route("/generator", methods=["GET","POST"])
def gen():
    if request.method == "GET":
        return render_template("generator.html")
#    else:
#
#         length = request.form.get("length")
#         # Check if password provided
#         if not length:
#             return redirect("/generator")
# 
#         type = request.form.get("type")
#         # Check if type provided
#         if not type:
#             return redirect("/generator")
# 
#         passw = generator(int(type), int(length))
#         return render_template("generator.html", passw=passw)
    

@bp.route("/save", methods=["POST", "GET"])
def saving():
    # If method get
    if request.method == "GET":
        # Check if logged in
        if session.get("user_id") is None:
            return redirect("/login")
        else:
            return render_template("save.html")
    # if method post
    else:
        # Get the arguments from the user
        service = request.form["service"]
        name = request.form["name"]
        password = request.form["password"]
        id = int(session["user_id"])
        # Pass to the save function
        booli = save(id, name, service, password)
        # Return the boolean value
        return jsonify(result=booli)


if __name__ == "__main__":
    app.run(ssl_context='adhoc')