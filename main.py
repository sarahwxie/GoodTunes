from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from custom import apology, convert
import songs

# Configuring the flask application
app = Flask(__name__)

# Set the SQL database
dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

# set up the session
app.secret_key = "According to all known laws of aviation, there is no way a bee should be able to fly."


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]  # using name as dictionary key
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
            username=formUser)

        user = convert(resultproxy)
        # make this unique later
        session["user_id"] = user['id']

        # redirects us to the user page
        return redirect(url_for("user", usr=user["username"], user=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    # compute rows
    resultproxy = db.engine.execute(text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
                                    id=session["user_id"])

    user = convert(resultproxy)
    return render_template("profile.html", user=user)


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
        db.engine.execute(
            text("INSERT INTO users (username, hash, name) VALUES (:user, :hash, :name);").execution_options(
                autocommit=True),
            user=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
            name=fullname)

        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        newuser = request.form["newusername"]  # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("newuser", newusr=newuser))
    else:
        return render_template("login.html")


@app.route('/profile/')
def profile():
    session.clear()
    session["user_id"] = 1

    # compute rows
    resultproxy = db.engine.execute(text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
                                    id=session["user_id"])

    user = convert(resultproxy)
    return render_template("profile.html", user=user)


@app.route("/<usr>")
def newuser(newusr):
    return f"<h1>{newusr}</h1>"


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search = request.form["search"]
        songs1 = [str(song).lower() for song in songs.songsdata]
        for song in songs1:
            if search in song:
                print(song)
                song = song.split("', '")
                print(song)
                song[0] = song[0][2:]
                song[2] = song[2][:-2]
                print(song)
                print(song[0] + song[1] + song[2])
                return render_template("search.html", songsdb=songs.songsdata, song=song)
        return render_template("search.html", songsdb=songs.songsdata, song=None)
    else:
        songs1 = songs.songsdata
        return render_template("search.html", songsdb=songs1, song=None)


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
