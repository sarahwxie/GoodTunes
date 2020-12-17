from flask import Flask, flash, jsonify, redirect, render_template, request, session, current_app, g

# Configuring the flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/landing/<selection>', methods=['GET', 'POST'])
def landing(selection):
    # POST redirection to content page
    if request.method == 'POST':
        form = request.form
        page = form['page']
        return redirect(url_for(page))
    # GET landing page render based off of "selection"
    selected_list = key_2_proj[selection] # selection is "key" used to pull project details from dictionary
    heading = selected_list[TITLE]
    projects = selected_list[PROJECTS]
    return render_template("homesite/landing.html", heading=heading, menus=menus, projects=projects)

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
