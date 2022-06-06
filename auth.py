from flask import redirect, render_template, request, session
from flask import Blueprint

from project.functions import login_required
from project.database import register, login

bp = Blueprint("auth", __name__)


# Ensure that logout actually logs the user out
@bp.after_request
def after_request(response):
    # Make sure no caching
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@bp.route("/register", methods=["POST", "GET"])
def reg():
    # If get return the page
    if request.method == "GET":
        return render_template("register.html")
    # If post then do the registration
    else:
        name = request.form.get("newname")
        newpass = request.form.get("newpass")
        if newpass != request.form.get("confpass"):
            return False
        regstat = register(name, newpass)
        if regstat == True:
            session["user_id"] = login(name, newpass)
            return redirect("/")
        


@bp.route("/login", methods=["GET", "POST"])
def log():

    session.clear()

    if request.method =="GET":
        return render_template("login.html")
        
    else:
        uname = request.form.get("uname")
        passw = request.form.get("passw")
        # check if credidentials provided
        if not uname or not passw:
            return redirect("login")
        
        # Hand them over to the login function
        islogged = login(uname, passw)
        # If not locked or some error
        if islogged == False:
            return redirect("/login")
        else:
            # remember user in session
            session["user_id"] = islogged
            return redirect("/")


@bp.route("/logout", methods=["POST"])
def logout():
    # Forget session
    session.clear()
    return redirect("/login")