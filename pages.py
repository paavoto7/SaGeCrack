
from flask import Flask, redirect, render_template, request, jsonify, session
from flask import Blueprint

bp = Blueprint("pages", __name__)

from project.functions import cracker, login_required
from project.database import save, get_saved

# Ensure that caching is disables
@bp.after_request
def after_request(response):
    # Make sure no caching
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response 

@bp.route("/")
@login_required
def cracking():
    return render_template("index.html")


@bp.route("/cracker")
def crack():
    # Return page
    return render_template("cracker.html")


@bp.route("/cracked")
def cracked():
    passw = request.args.get("passw", default='')
    type = request.args.get("type", type=int)

    # Hand the information to the cracker function    
    past = cracker(passw, type)
    # Jsonify the result for jquery
    return jsonify(result=past[0], time=past[1])


@bp.route("/generator")
def gen():
    return render_template("generator.html")
    

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


# Transfer the password over from the register page to the save page
@bp.route("/hidsave", methods=["POST"])
@login_required
def hidsave():
    transfer = request.form.get("copy")
    return render_template("save.html", transfer=transfer)


# Search for the saved passwords
@bp.route("/search")
@login_required
def searching():
    search = request.args.get("q", default='', type=str)
    result = get_saved(search, session["user_id"])
    return jsonify(result)


# Get the passwords and the usernames
@bp.route("/info")
@login_required
def info():
    service = request.args.get("service", default="1", type=str)
    result = get_saved(service, session["user_id"])
    return jsonify(result)