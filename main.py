from flask import Flask, flash, jsonify, redirect, render_template, request, session, current_app, g

# Configuring the flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
