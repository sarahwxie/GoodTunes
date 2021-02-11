from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import random

from custom import apology, convert, convertList
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


@app.route('/wrapped')
def wrapped():
    resultproxy = db.engine.execute(
        text("SELECT * FROM users;").execution_options(autocommit=True))

    users = convertList(resultproxy)
    print(users)
    return render_template("wrapped.html", users=users)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]  # using name as dictionary key
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
            username=formUser)

        user = convert(resultproxy)

        # troubleshooting
        if user == False:
            return render_template("login.html", error=True)

        #set the user id
        session.clear()
        session["user_id"] = user["id"]

        # redirects us to the user page
        return redirect(url_for("user1", usr=user["username"]))
    else:
        return render_template("login.html", error=False)


@app.route("/<usr>")
def user1(usr):
    # compute rows
    resultproxy = db.engine.execute(
        text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
        username=usr)

    user = convert(resultproxy)
    if user == False:
        user = {'id': 404, 'username': 'iDontExist',
                'hash': 'password hash',
                'name': 'That user does not exist!', 'bio': "You probably typed a name in the search bar. The user "
                                                            "you searched for either doesn't exist or deleted their "
                                                            "account"}
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

        fullname = request.form.get("name")
        print(request.form.get("bio") == '')

        # Insert all the values into the database
        db.engine.execute(
            text("INSERT INTO users (username, hash, name, bio) VALUES (:user, :hash, :name, :bio);").execution_options(
                autocommit=True),
            user=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
            name=fullname, bio=request.form.get("bio"))

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


@app.route('/apjournal/')
def apjournal():
    return render_template("apjournal.html")

@app.route('/friends/')
def friends():
    return render_template("friends.html")


@app.route('/profile/')
def profile():
    session.clear()
    session["user_id"] = 1

    # compute rows
    resultproxy = db.engine.execute(text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
                                    id=session["user_id"])

    user = convert(resultproxy)
    return render_template("profile.html", user=user)


@app.route('/search', methods=['GET', 'POST'])
def search():
    songs1 = songs.songsdata
    songs1.pop(0)
    return render_template("search.html", songs=songs1)

@app.route('/connect')
def connect():
    return render_template("friends.html")

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=="POST":
        #song1 = request.form["song1"]
        #song2 = request.form["song2"]
        #song3 = request.form["song3"]
        #playlist=[song1,song2,song3]
        print("yo")
        db.engine.execute(
            text("INSERT INTO playlists (hash, songs) VALUES (:hash, :songs);").execution_options(
                autocommit=True),
            #make user field xo
            hash=generate_password_hash(str(random.randrange(100))),
            songs=[request.form.get("song1"),request.form.get("song2"),request.form.get("song3")]
        )
        #print(playlist)
        return redirect("/profile")
    else:
        return render_template("playlistcreate.html", songsdb=songs.songsdata)


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
