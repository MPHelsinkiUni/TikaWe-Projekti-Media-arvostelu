import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash
import db
import config
import items
import users

app = Flask(__name__, template_folder ='./templates')
app.secret_key = config.secret_key

@app.route("/") # Root
def index():
    reviews = items.get_items()
    return render_template("index.html", message = "Welcome to film review site!", items=reviews)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    yeet_empty_variable(item)
    classes = items.get_classes(item_id)
    comments = items.get_comments(item_id)
    return render_template("review_data.html", item=item, classes=classes, comments=comments)

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
    
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "Warning: Your username has already been chosen. Please pick another one."

    return render_template("registration_success.html")


##################
# This section manages repetitive code

def sanity_check(item): # Check data integrity and prevent unauthorised access
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

def kill_anons(): # No user_id => no access
    if "user_id" not in session:
        abort(403)

def kill_spaghetti(input, upper_length, lower_length):
    if len(input) > upper_length:
        abort(403)
    if len(input) < lower_length:
        abort(403)

def ghostbust(user):
    if not user:
        abort(404)

def yeet_rotten_apple(item):
    if not item:
        abort(403)

def yeet_empty_variable(item):
    if not item:
        abort(404)

def class_dismissal(parts):
    all_classes = items.get_all_classes()
    if parts[0] not in all_classes:
        abort(403)
    if parts[1] not in all_classes[parts[0]]:
        abort(403)

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
        
        user_id = users.verify_user(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "Warning: Double-check your username or password."

@app.route("/logout")
def logout():
    kill_anons()
    del session["user_id"]
    del session["username"]
    return redirect("/")

##################
# This section manages the addition, modification and removal of new reviews themselves.
@app.route("/review_paper")
def new_review():
    kill_anons()
    classes = items.get_all_classes()
    return render_template("review_paper.html", classes=classes)

@app.route("/create_review", methods = ["POST"])
def insert_review():
    kill_anons()
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

    kill_spaghetti(title, 255, 1)
    kill_spaghetti(review_body, 5000, 1)
    kill_spaghetti(work, 255, 1)
    kill_spaghetti(imdb_snippet, 255, 3)

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            class_dismissal(parts)
            classes.append((parts[0], parts[1]))

    items.add_item(title, username, user_id, review_body, stars, work, imdb_snippet, classes)

    return redirect("/")

@app.route("/edit_review", methods = ["POST"])
def edit_review_auxiliary():
    kill_anons()
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
    sanity_check(item)
    title = request.form["title"]
    review_body = request.form["review_body"]
    stars = int(request.form["stars"])
    work = request.form["work"]
    imdb_snippet = request.form["imdb_snippet"]

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            class_dismissal(parts)
            classes.append((parts[0], parts[1]))

    items.update_item(item_id, title, review_body, stars, work, imdb_snippet, classes)

    return redirect("/item/"+str(item_id))

@app.route("/edit_review/<int:item_id>")
def edit_review(item_id):
    kill_anons()
    item = items.get_item(item_id)
    sanity_check(item)

    # Check item current classes
    all_classes = items.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in items.get_classes(item_id):
        classes[entry["title"]] = entry["value"]

    print(classes, all_classes)

    return render_template("edit_review.html", item=item, classes=classes, all_classes=all_classes)

@app.route("/remove_review/<int:item_id>", methods=["GET", "POST"])
def remove_review(item_id):
    kill_anons()
    item = items.get_item(item_id)
    sanity_check(item)
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

####################
# This section manages user profiling
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get_user(user_id)
    ghostbust(user)
    entries = items.get_items_by_user(user_id)
    return render_template("user_profile.html", user=user, entries=entries)
    
####################
# This section manages comments
@app.route("/new_comment", methods = ["POST"])
def new_comment():
    kill_anons()
    # Input names are: title, review_body, stars, work, imdb_snippet (in HTML page). Linked as such
    # imdb_snippet -> imdb_snippet
    title = request.form["title"]
    comment_body = request.form["review_body"]
    username = session["username"]
    user_id = session["user_id"]
    root_id = request.form["review_id"]
    root_title = request.form["review_title"]

    item = items.get_item(root_id)
    yeet_rotten_apple(item)
    kill_anons()
    ghostbust(user_id)

    kill_spaghetti(comment_body, 5000, 1)

    items.add_comment(title, comment_body, username, user_id, root_id, root_title)

    return redirect("/item/" + str(root_id))
# Check on 127.0.0.1:5000 or localhost:5000
# Procedure: `source ./venv/bin/activate` -> `flask run` -> check -> CTRL+C -> `deactivate`