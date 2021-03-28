import os
from flask import (
    Flask, flash, render_template, 
    request, redirect, session, url_for)
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
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if user exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # else
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return render_template("login.html")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # check if username already exists in db
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # make sure hashed password equals user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            # if pw input != hashed password
            else:
                flash("Password and/or Username is incorrect")
                return redirect(url_for("login"))
        # if username does not exist in db
        else:
            flash("Username and/or Password incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # if true then return users profile
    if session["user"]:
        return render_template("profile.html", username=username)
    # if untrue return user back to login
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/bookpage/<book_name>")
def bookpage(book_name):
    get_book = mongo.db.books.find_one({"book_name": book_name})
    return render_template(
        "bookpage.html", get_book=get_book)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        is_upvoted = "on" if request.form.get("is_upvoted") else "off"
        book = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "buy_url": request.form.get("buy_url"),
            "is_upvoted": is_upvoted,
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
