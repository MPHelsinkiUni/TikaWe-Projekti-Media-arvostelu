import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config
import items

app = Flask(__name__, template_folder ='./templates')
app.secret_key = config.secret_key

@app.route("/") # Root
def index():
    reviews = items.get_items()
    return render_template("index.html", message = "Welcome to film review site!", items = reviews)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    return render_template("review_data.html", item=item)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "Warning: Passwords were not the same. Please double check your inputs"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "Warning: Your username has already been chosen. Please pick another one."

    return render_template("registration_success.html")

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
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "Warning: Double-check your username or password."

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")

##################
# This section manages the addition of new reviews themselves.
@app.route("/review_paper")
def new_review():
    return render_template("review_paper.html")

@app.route("/create_review", methods = ["POST"])
def insert_review():
    # Input names are: title, review_body, stars, work, imdb_snippet (in HTML page). Linked as such
    # title -> title
    # session.username -> poster
    # session.user_id -> poster_id
    # review_body -> review_body
    # stars -> stars
    # work -> work
    # work_id snippet will be worked on later. (WIP!!!)
    # imdb_snippet -> imdb_snippet
    title = request.form["title"]
    username = session["username"]
    user_id = session["user_id"]
    review_body = request.form["review_body"]
    stars = int(request.form["stars"])
    work = request.form["work"]
    imdb_snippet = request.form["imdb_snippet"]

    items.add_item(title, username, user_id, review_body, stars, work, imdb_snippet)

    return redirect("/")

@app.route("/edit_review", methods = ["POST"])
def edit_review_auxiliary():
    # Input names are: title, review_body, stars, work, imdb_snippet (in HTML page). Linked as such
    # title -> title
    # session.username -> poster
    # session.user_id -> poster_id
    # review_body -> review_body
    # stars -> stars
    # work -> work
    # work_id snippet will be worked on later. (WIP!!!)
    # imdb_snippet -> imdb_snippet
    item_id = request.form["item_id"]
    
    item = items.get_item(item_id)
    try: 
        if item["user_id"] != session["user_id"]:
            abort(403)
    except:
        abort(403)
        
    title = request.form["title"]
    review_body = request.form["review_body"]
    stars = int(request.form["stars"])
    work = request.form["work"]
    imdb_snippet = request.form["imdb_snippet"]

    items.update_item(item_id, title, review_body, stars, work, imdb_snippet)

    return redirect("/item/"+str(item_id))

@app.route("/edit_review/<int:item_id>")
def edit_review(item_id):
    item = items.get_item(item_id)

    if item["user_id"] != session["user_id"]:
        abort(403)

    return render_template("edit_review.html", item=item)

@app.route("/remove_review/<int:item_id>", methods=["GET", "POST"])
def remove_review(item_id):
    item = items.get_item(item_id)
    if item["user_id"] != session["user_id"]:
        abort(403)
        
    if request.method == "GET":
        item = items.get_item(item_id)
        return render_template("remove_review.html", item=item)

    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

#################### 
# This section manages search functionality
@app.route("/search_review")
def search_review():
    query = request.args.get("query")
    if query:
        results = items.search_review(query)
    else:
        query = ""
        results = []
    return render_template("search_review.html", query=query, results=results)

# Check on 127.0.0.1:5000 or localhost:5000
# Procedure: `source ./venv/bin/activate` -> `flask run` -> check -> CTRL+C -> `deactivate`