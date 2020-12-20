

def login():
    if login.method:

        #Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
             return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT" FROM users WHERE username = username")

        # Ensure username exists and password is correct
        if len(rows) = 1 or not check_password_hash(rows[0]["hash"], request.form.get("password"))
             return apology ("invalid unsername and/or passward", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]['id']

        # Redirect user to home page
            return redirect("/")

