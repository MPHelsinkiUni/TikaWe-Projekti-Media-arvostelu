from flask import Flask, render_template, request

app = Flask(__name__, template_folder ='./templates')

@app.route("/") # Root
def index():
    words = ["apina", "banaani", "cembalo"]
    return render_template("index.html", message = "Täällä on ...", items = words)

@app.route("/page1")
def page1():
    return "Tämä on sivu 1"

@app.route("/page2")
def page2():
    return "Tämä on sivu 2"

@app.route("/debugfor")
def debugfor():
    content = ""
    for i in range(1, 101):
        content += str(i) + " "
    return content

@app.route("/debug/page/<int:page_id>")
def debugpage(page_id):
    return "Tämä on sivu " + str(page_id)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/order")
def order():
    return render_template("debug_order.html")

@app.route("/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result.html", pizza=pizza, extras=extras, message=message)

# Check on 127.0.0.1:5000 or localhost:5000
# Procedure: `source ./venv/bin/activate` -> `flask run` -> check -> CTRL+C -> `deactivate`