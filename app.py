from re import X
from flask import Flask, redirect, render_template, request, jsonify, session
from flask_session import Session

from functions import cracker # generator
from database import login

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
#     else:
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
        islogged = login(uname, passw)
        if islogged == False:
            return redirect("/login")
        else:
            session["user_id"] = islogged["id"]
            return render_template("index.html")


if __name__ == "__main__":
    app.run(ssl_context='adhoc')