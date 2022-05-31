
from flask import Flask, redirect, render_template, request, jsonify, session
from flask_session import Session

from functions import cracker, login_required # generator
from database import login, register, save

# Configure application
app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def cracking():
    return render_template("index.html")


@app.route("/cracker")
def crack():
    # Return page if get
    return render_template("cracker.html")


@app.route("/cracked")
def cracked():
    passw = request.args.get("passw", default='')
    type = request.args.get("type", type=int)

    # Hand the information to the cracker function    
    past = cracker(passw, type)
    # Jsonify the result for jquery
    return jsonify(result=past[0], time=past[1])


@app.route("/generator", methods=["GET","POST"])
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


@app.route("/register", methods=["POST", "GET"])
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
            return redirect("/")
        


@app.route("/login", methods=["GET", "POST"])
def log():

    session.clear()

    if request.method =="GET":
        return render_template("login.html")
    else:
        uname = request.form.get("uname")
        passw = request.form.get("passw")
        # check if credidentials provided
        if not uname or not passw:
            return redirect("/login")
        
        # Hand them over to the login function
        islogged = login(uname, passw)
        # If not locked or some error
        if islogged == False:
            return redirect("/login")
        else:
            # remember user in session
            session["user_id"] = islogged["id"]
            return render_template("index.html")

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    # Forget session
    session.clear()
    return redirect("/login")
    

@app.route("/save", methods=["POST", "GET"])
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