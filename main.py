from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g

# Configuring the flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form["username"] # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/newuser/')
def new_user():
    return render_template("signup.html")

@app.route('/search/')
def search():
    return render_template("search.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
