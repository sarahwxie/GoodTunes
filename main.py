from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from custom import apology

# Configuring the flask application
app = Flask(__name__)

# Set the SQL database
dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["username"]  # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    """Register user"""
    if request.method == "POST":
        # Make sure they put in their username
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Make sure they put in a password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        fullname = request.form.get("first") + request.form.get("last")
        # Insert all the values into the database
        db.engine.execute(text("INSERT INTO users (username, hash, name) VALUES (:user, :hash, :name);").execution_options(autocommit=True),
                          user=request.form.get("username"),
                          hash=generate_password_hash(request.form.get("password")),
                          name=fullname)

        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route('/search/')
def search():
    return render_template("search.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
