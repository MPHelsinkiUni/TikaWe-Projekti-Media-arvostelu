import sqlite3, secrets, markupsafe, math, time
from flask import Flask, abort, redirect, render_template, request, session, flash, make_response, g
import config, items, users

app = Flask(__name__, template_folder ='./templates')
app.secret_key = config.secret_key

@app.route("/") # Root
@app.route("/<int:page>")
def index(page=1):
    page_size = 10
    thread_count = items.review_count()
    page_count = math.ceil(thread_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    reviews = items.get_items(page, page_size)
    return render_template("index.html", message = "Welcome to film review site!", page=page, page_count=page_count, items=reviews)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("Error: Passwords were not the same. Please double check your inputs")
        return redirect("/create")
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("Error: Your username has already been chosen. Please pick another one.")
        return redirect("/create")
    user_id = users.verify_user(username, password1)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
    return render_template("registration_success.html")


##################
# This section manages repetitive code

def unauthorised_access_check(item): # Check data integrity and prevent unauthorised access
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

def anonymous_user_check(): # No user_id => no access
    if "user_id" not in session:
        abort(403)

def remove_nonpermitted_inputs(input, upper_length, lower_length):
    if len(input) > upper_length:
        abort(403)
    if len(input) < lower_length:
        abort(403)

def user_not_found(user):
    if not user:
        abort(404)

def no_item_403(item):
    if not item:
        abort(403)

def no_item_404(item):
    if not item:
        abort(404)

def class_dismissal(parts):
    all_classes = items.get_all_classes()
    if parts[0] not in all_classes:
        abort(403)
    if parts[1] not in all_classes[parts[0]]:
        abort(403)

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)


###################
# This section manages logins, and logouts

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = users.verify_user(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("Error: Double-check your username or password.")
            return redirect("/login")

@app.route("/logout")
def logout():
    anonymous_user_check()
    del session["user_id"]
    del session["username"]
    return redirect("/")

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

##################
# This section manages the addition, modification and removal of new reviews themselves.

@app.route("/item/<int:item_id>")
@app.route("/item/<int:item_id>/<int:page>")
def show_item(item_id, page=1):
    item = items.get_item(item_id)
    no_item_404(item)
    classes = items.get_classes(item_id)
    images = items.get_image_id_reviews(item_id)

    page_size = 10
    thread_count = items.comment_count(item_id)
    page_count = math.ceil(thread_count / page_size)
    page_count = max(page_count, 1)
    comments = items.get_comments(item_id, page, page_size)
    if page < 1:
        return redirect("/item/" + str(item_id) + "/1")
    if page > page_count:
        return redirect("/item/" + str(item_id) + "/" + str(page_count))

    return render_template("review_data.html", item=item, classes=classes, comments=comments, images=images, page=page, page_count=page_count)

@app.route("/review_paper")
def new_review():
    anonymous_user_check()
    classes = items.get_all_classes()
    return render_template("review_paper.html", classes=classes)

@app.route("/create_review", methods = ["POST"])
def insert_review():
    anonymous_user_check()
    check_csrf()

    title = request.form["title"]
    username = session["username"]
    user_id = session["user_id"]
    review_body = request.form["review_body"]
    stars = int(request.form["stars"])
    work = request.form["work"]
    imdb_snippet = request.form["imdb_snippet"]

    remove_nonpermitted_inputs(title, 255, 1)
    remove_nonpermitted_inputs(review_body, 5000, 1)
    remove_nonpermitted_inputs(work, 255, 1)
    remove_nonpermitted_inputs(imdb_snippet, 255, 3)

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
    check_csrf()
    anonymous_user_check()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    unauthorised_access_check(item)
    title = request.form["title"]
    review_body = request.form["review_body"]
    stars = request.form["stars"]
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
    anonymous_user_check()
    item = items.get_item(item_id)
    unauthorised_access_check(item)

    all_classes = items.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in items.get_classes(item_id):
        classes[entry["title"]] = entry["value"]

    return render_template("edit_review.html", item=item, classes=classes, all_classes=all_classes)

@app.route("/remove_review/<int:item_id>", methods=["GET", "POST"])
def remove_review(item_id):
    anonymous_user_check()
    item = items.get_item(item_id)
    unauthorised_access_check(item)
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
    user_not_found(user)
    anonymous_user_check()
    if session["user_id"] != user_id:
        abort(403)
    entries = items.get_items_by_user(user_id)
    images = users.get_image_id_users(user_id)
    return render_template("user_profile.html", user=user, entries=entries, images=images)

# And this subsection manages images for users specifically
@app.route("/user/update_image", methods=["POST"])
def add_image_user():
    anonymous_user_check()
    check_csrf()
    user_id = request.form["user_id"]
    user = users.get_user(user_id)
    user_not_found(user)
    if user[0] != session["user_id"]:
        abort(403)
    file = request.files["image"]
    if not file.filename.endswith(".png"):
        flash("Error: PNG only. Sorry")
        return redirect("/user/update_image")
    image = file.read()
    if len(image) > 100 * 1024:
        flash("Error: Picture is too large")
        return redirect("/user/update_image")
    users.update_image_users(user_id, image)
    return redirect("/user/" + str(user_id))

@app.route("/user/image/<int:image_id>")
def show_image_user(image_id):
    image = users.get_image_users(image_id)
    no_item_404(image)
    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/png")
    return response

####################
# This section manages comments
@app.route("/new_comment", methods = ["POST"])
def new_comment():
    anonymous_user_check()
    check_csrf()
    title = request.form["title"]
    comment_body = request.form["review_body"]
    username = session["username"]
    user_id = session["user_id"]
    root_id = request.form["review_id"]
    root_title = request.form["review_title"]
    item = items.get_item(root_id)
    no_item_403(item)
    anonymous_user_check()
    user_not_found(user_id)
    remove_nonpermitted_inputs(comment_body, 5000, 1)
    items.add_comment(title, comment_body, username, user_id, root_id, root_title)
    return redirect("/item/" + str(root_id))

####################
# This section manages images
@app.route("/images/<int:item_id>")
def edit_images(item_id):
    anonymous_user_check()
    item = items.get_item(item_id)
    unauthorised_access_check(item)
    images = items.get_image_id_reviews(item_id)
    return render_template("images.html", item=item, images=images)

@app.route("/add_image", methods=["POST"])
def add_image():
    anonymous_user_check()
    check_csrf()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    unauthorised_access_check(item)
    file = request.files["image"]
    if not file.filename.endswith(".png"):
        flash("Error: PNG only. Sorry")
        return redirect("/add_image")
    image = file.read()
    if len(image) > 100 * 1024:
        flash("Error: Picture is too large")
        return redirect("/add_image")
    items.add_image_reviews(item_id, image)
    return redirect("/images/" + str(item_id))

@app.route("/image/<int:image_id>")
def show_image(image_id):
    image = items.get_image_reviews(image_id)
    no_item_404(image)
    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/png")
    return response

@app.route("/remove_images", methods=["POST"])
def remove_images():
    anonymous_user_check()
    check_csrf()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    unauthorised_access_check(item)
    for image_id in request.form.getlist("image_id"):
        items.remove_image_reviews(item_id, image_id)
    return redirect("/images/" + str(item_id))

##############
# This section deals with time
@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    print("elapsed time:", elapsed_time, "s")
    return response


# Check on 127.0.0.1:5000 or localhost:5000
# Procedure: `source ./venv/bin/activate` -> `flask run` -> check -> CTRL+C -> `deactivate`