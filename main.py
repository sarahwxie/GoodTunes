from flask import Flask, flash, jsonify, redirect, render_template, request, session, current_app, g

# Configuring the flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/newuser')
def new_user():
    return render_template("signup.html")

# connects /hello path of server to render hello.html
@app.route('/login/')
def login():
    return render_template("login.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
