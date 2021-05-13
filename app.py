import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import math
import datetime
import string
import secrets
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books/new_books")
@app.route("/get_books/new_books/<int:page>")
def books_new(page=1):
    books = list(mongo.db.books.find().sort("_id", -1))
    genres = list(mongo.db.genres.find().sort("genres", 1))
    avgratings = list(mongo.db.avgRatingAgg.find().sort("id", -1))
    if page == 1:
        booklist = books[0:12]
        page = page
    else:
        first = page * 12 - 12
        last = first + 12
        booklist = books[first:last]
        page = page
    counter = math.ceil((len(books))/(12))
    return render_template(
        "books.html", books=booklist,
        genres=genres, pages=counter, avgratings=avgratings, page=page)


@app.route("/search", methods=["GET", "POST"])
def search():
    genres = mongo.db.genres.find().sort("genres", 1)

    booklist = list(mongo.db.books.find(
        {"$text": {"$search": request.form.get("query")}}))
    query = request.form.get("query")
    return render_template(
        "books.html", books=booklist, genres=genres, query=query, post=True)


@app.route("/get_books/a-to-z")
@app.route("/get_books/a-to-z/<int:page>")
def books_a_to_z(page=1):
    books = list(mongo.db.books.find().sort("book_name", 1))
    genres = list(mongo.db.genres.find().sort("genres", 1))

    if page == 1:
        booklist = books[0:12]
        page = page
    else:
        first = page * 12 - 12
        last = first + 12
        booklist = books[first:last]
        page = page
    counter = math.ceil((len(books))/(12))

    return render_template(
        "books-a-to-z.html", books=booklist,
        genres=genres, pages=counter, page=page)


@app.route("/get_books/z-to-a")
@app.route("/get_books/z-to-a/<int:page>")
def books_z_to_a(page=1):
    books = list(mongo.db.books.find().sort("book_name", -1))
    genres = list(mongo.db.genres.find().sort("genres", 1))

    if page == 1:
        booklist = books[0:12]
        page = page
    else:
        first = page * 12 - 12
        last = first + 12
        booklist = books[first:last]
        page = page
    counter = math.ceil((len(books))/(12))

    return render_template(
        "books-z-to-a.html", books=booklist,
        genres=genres, pages=counter, page=page)


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
        print("username found")

        if existing_user:
            # make sure hashed password equals user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"],
                        _external=True, _scheme='https'))
            # if pw input != hashed password
            else:
                flash('Password and/or Username is incorrect', 'error')
                return redirect(url_for("login"))
        # if username does not exist in db
        else:
            flash("Username and/or Password incorrect", 'error')
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from db
    user = mongo.db.users.find_one({"username": session['user']})
    today = datetime.date.today()
    date_joined = user["_id"].generation_time.date()
    diff = "%d days" % (today - date_joined).days
    books = list(mongo.db.books.find().sort("book_name", 1))
    booksbyuser = mongo.db.books.find({"created_by": username})
    bookcount = booksbyuser.count()
    avgrating = list(mongo.db.avgRatingAgg.find().sort("id", -1))
    for book in books:
        if 'review':
            for ereview in 'review':
                reviewcountdict = list(mongo.db.books.aggregate([{
                    "$unwind": "$review"},
                    {"$match": {'review.username': username}},
                    {"$count": "reviewcount"}
                ]))
                if reviewcountdict:
                    reviewcount = reviewcountdict[0]["reviewcount"]
                else:
                    reviewcount = 0
    # if true then return users profile
    if session["user"]:
        return render_template(
            "profile.html", user=user, diff=diff,
            books=books, bookcount=bookcount,
            reviewcount=reviewcount, avgratings=avgrating)
    # if untrue return user back to login
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login", _external=True, _scheme='https'))


@app.route("/bookpage/<book_name>")
def bookpage(book_name):
    get_book = mongo.db.books.find_one({"book_name": book_name})
    reviews = get_book.get("review")
    #  add average rating aggregation to a new collection
    if reviews:
        for review in reviews:
            x = review["bookid"]
            review = list(mongo.db.books.aggregate([{
                "$unwind": "$review"},
                {"$match": {'review.bookid': x}},
                {"$group": {
                    "_id": "$_id", "averageRating": {
                        "$avg": '$review.rating'}}},
                {"$merge": {
                    "into": "avgRatingAgg",
                    "on": "_id",
                    "whenMatched": "replace",
                    "whenNotMatched": "insert"}}
            ]))
            review = mongo.db.avgRatingAgg.find_one({
                "_id": ObjectId(get_book["_id"])
            })
    else:
        review = "No star ratings yet"
    return render_template(
        "bookpage.html", get_book=get_book, review=review
    )


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "buy_url": request.form.get("buy_url"),
            "created_by": session["user"],
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("books_new"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)


@app.route("/edit_book/<book_name>/<id>", methods=["GET", "POST"])
def edit_book(book_name, id):
    get_book = mongo.db.books.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.books.update({"_id": ObjectId(id)}, {"$set": {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "buy_url": request.form.get("buy_url"),
            "created_by": session["user"]
            }}
        )
        flash("Book Successfully Updated")
        return redirect(url_for(
            "bookpage", book_name=get_book.get("book_name")))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template(
        "edit_book.html", get_book=get_book, genres=genres, id=id)


@app.route("/delete_book/<book_name>/<id>")
def delete_book(book_name, id):
    mongo.db.books.remove({"_id": ObjectId(id)})
    flash("Book has sucessfully been deleted")
    return redirect(url_for("books_new"))


@app.route("/bookpage/<book_name>", methods=["POST"])
def review_book(book_name):
    get_book = mongo.db.books.find_one({"book_name": book_name})
    reviews = get_book.get("review")
    date = str(datetime.date.today())
    #  save the review if method is post
    if request.method == "POST":
        if reviews:
            for review in reviews:
                #  if user has already posted a review, stop them
                if review["username"] == session["user"]:
                    flash("You have already reviewed this book.")
                    return redirect(url_for(
                        "bookpage", book_name=get_book.get("book_name")))
        #  else allow user to post review
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        mongo.db.books.update_one(
            {"_id": ObjectId(get_book["_id"])}, {
                "$addToSet": {"review": {
                    "title": request.form.get("review_title"),
                    "description": request.form.get("review"),
                    "rating": int(request.form.get("rate")),
                    "date": date,
                    "review_id": password,
                    "bookid": str(get_book["_id"]),
                    "username": session["user"]}}})
    else:
        review = "No star ratings yet"
        flash("review saved")
    return redirect(url_for("bookpage", book_name=get_book.get("book_name")))


@app.route("/<book_name>/<book_id>/<username>/<id>/editreview", methods=[
    "GET", "POST"])
def edit_review(book_name, book_id, username, id):
    username = mongo.db.users.find_one(
        {"username": session['user']})["username"]
    get_book = mongo.db.books.find_one({"book_name": book_name})
    reviewarray = list(mongo.db.books.find(
        {'review': {"$elemMatch": {"review_id": id}}}, {
            "review.$": 1}))
    new_dict = {}
    for key, value in reviewarray[0].items():
        if key == "review":
            new_dict[key] = value
        for k in new_dict:
            for x in new_dict[k]:
                review = x

    if request.method == "POST":
        mongo.db.books.update(
            {"_id": ObjectId(book_id), "review.review_id": id},
            {"$set": {
                "review.$.title": request.form.get("review_title"),
                "review.$.description": request.form.get("review"),
                "review.$.rating": int(request.form.get("rate")),
                "review.$.bookid": str(get_book["_id"])  # remove this after
                }}
        )
        flash("review Successfully Updated")
        return redirect(url_for(
            "bookpage", book_name=get_book.get("book_name")))

    if session["user"] == username or session["user"] == "admin":
        return render_template(
            "editreview.html",
            get_book=get_book,
            review=review,
        )
    else:
        return redirect(url_for(
            "bookpage", book_name=get_book.get("book_name")))


@app.route("/<book_name>/<book_id>/<username>/<id>/deletereview")
def delete_review(book_name, book_id, username, id):
    mongo.db.books.update(
        {"_id": ObjectId(book_id), "review.review_id": id},
        {"$pull": {"review": {"review_id": id}}})
    flash('Review Successfully Removed')
    {"_id": ObjectId(book_id), "review.review_id": id}
    mongo.db.avgRatingAgg.remove({
        "_id": ObjectId(book_id)
        })
    get_book = mongo.db.books.find_one({"book_name": book_name})
    return redirect(url_for(
        "bookpage", book_name=get_book.get("book_name")))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name"),
            "genre_icon": request.form.get("genre_icon")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        save = {
            "genre_name": request.form.get("genre_name"),
            "genre_icon": request.form.get("genre_icon")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, save)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
