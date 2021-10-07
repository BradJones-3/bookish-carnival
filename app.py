import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_terms")
def get_terms():
    terms = mongo.db.terms.find()
    return render_template("terms.html", terms=terms)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user. Username is checked before being 
    registered to ensure it doesn't already exist in db.
    If registration is complete
    the user is logged in.
    """
    if request.method == "POST":
        # checking of users exist in database
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry Username already exist, try again")
            return render_template("register.html")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thank you! You are now registered")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks to see if username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # makes sure hashed password matches users input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Passwords do not match
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/logout')
def logout():
    # Logs the user of the session log out of their profile
    # and redirect the user back to the landing page
    flash("You have Successfully been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/user-profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets the session users username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("user-profile.html", username=username)

    if session["user"]:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)