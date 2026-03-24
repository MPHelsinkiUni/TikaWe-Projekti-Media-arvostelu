import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config

app = Flask(__name__, template_folder ='./templates')
app.secret_key = config.secret_key

@app.route("/") # Root
def index():
    words = ["Newest movie #1", "Newest movie #2", "Newest movie #3"]
    return render_template("index.html", message = "Welcome to film review site!", items = words)

@app.route("/page1")
def page1():
    return "Tämä on sivu 1"

@app.route("/page2")
def page2():
    return "Tämä on sivu 2"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat. Tarkistaa salasanat uudestaan"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

###################
# This section manages logins, and logouts

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
        # Consider replacing with calling index() itself.

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT password_hash FROM users WHERE username = ?"
        password_hash = db.query(sql, [username])[0][0]

        if check_password_hash(password_hash, password):
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

##################
# This section manages the addition of new reviews themselves.
@app.route("/review_paper")
def new_review():
    return render_template("review_paper.html")


#################### 
# Debugger below
@app.route("/debugfor")
def debugfor():
    content = ""
    for i in range(1, 101):
        content += str(i) + " "
    return content

@app.route("/debug/page/<int:page_id>")
def debugpage(page_id):
    return "Tämä on sivu " + str(page_id)

@app.route("/debug/form")
def form():
    return render_template("form.html")

@app.route("/debug/order")
def order():
    return render_template("debug_order.html")

@app.route("/debug/pizza/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result.html", pizza=pizza, extras=extras, message=message)

# Check on 127.0.0.1:5000 or localhost:5000
# Procedure: `source ./venv/bin/activate` -> `flask run` -> check -> CTRL+C -> `deactivate`