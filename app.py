from flask import Flask, redirect, render_template, request, jsonify

from functions import cracker # generator

# Configure application
app = Flask(__name__)


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
    type = request.args.get("type", default=3, type=int)
    # Check if password provided
    if passw == '':
       return redirect("/cracker")

    # Check if type provided
    if type == 3:
       return redirect("/cracker")

    # Hand the information to the cracker function    
    past = cracker(passw, type)
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


if __name__ == "__main__":
    app.run(ssl_context='adhoc')