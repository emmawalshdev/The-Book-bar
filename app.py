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

# create instances of flask and asign it to app
app = Flask(__name__)

# mongo db config to build connection from env variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# use PyMongo to connect to the MongoDB server
mongo = PyMongo(app)


# homepage: include pagination pages
@app.route("/")
@app.route("/get_books/new_books")
@app.route("/get_books/new_books/<int:page>")
def books_new(page=1):
    """
    Checks the page number. If page = 1, the first 12 books in db are shown.
    if page != 1, a calculation is preformed which decides the list of books
    to be shown.
    The user is redirected to the books.html page.
    """
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


# homepage search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Returns a list of books once a user searches by book name or author name.

    """
    genres = mongo.db.genres.find().sort("genres", 1)
    books = list(mongo.db.books.find(
        {"$text": {"$search": request.form.get("query")}}))
    query = request.form.get("query")
    return render_template(
        "books.html", books=books, genres=genres, query=query, post=True)


# A-Z sort by in homepage: include pagination pages
@app.route("/get_books/a-to-z")
@app.route("/get_books/a-to-z/<int:page>")
def books_a_to_z(page=1):
    """
    Checks the page number. If page = 1, the first 12 books in db are shown.
    if page != 1, a calculation is preformed which decides the list of books
    to be shown.
    The user is redirected to the books-a-to-z.html page.
    """
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


# A-Z sort by in homepage:: include pagination pages
@app.route("/get_books/z-to-a")
@app.route("/get_books/z-to-a/<int:page>")
def books_z_to_a(page=1):
    """
    Checks the page number. If page = 1, the first 12 books in db are shown.
    if page != 1, a calculation is preformed which decides the list of books
    to be shown.
    The user is redirected to the books-z-to-a.html
    """
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


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks if method is post.
    if true, checks if the username already exists. If also true,
    a flash message is shown & user is reditected back to register page.
    if username is not in use, the data is saved in db & the user is redirected
    to the login page.

    """
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if user exists
        if existing_user:
            flash("This username is already in use." +
                  " Please choose another.", "error")
            return redirect(url_for("register"))

        # else
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful. Please login to continue.", "success")
        return render_template("login.html")
    return render_template("register.html")


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks if method = POST.
    If true, the username & password are checked.
    If both are correct, the user is logged in and redirected to profile.html.
    if one or both are incorrect, the user is redirected back to login.html.
    If the username does not exist in db, the user is redirected to login.html.
    """
    # check if username already exists in db
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

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
                flash("Password and/or username is incorrect", "error")
                return redirect(url_for("login"))
        # if username does not exist in db
        else:
            flash("Username and/or password is incorrect.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Checks if the user is session.
    If true, the member time duration is calculated.
    Next, it is checked if the user document contains 'books_added'.
    If true, the length is calculated & the first 4 books are returned.
    If false, the length is set to 0 & no books are returned.
    This same process if followed for 'reviews_added'.
    Then the user is redirected to profile.html.
    If the user is not in sesion, they are redirected to login.html.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        if username == session["user"]:
            user = mongo.db.users.find_one({"username": session['user']})
            today = datetime.date.today()
            date_joined = user["_id"].generation_time.date()
            user_duration = "%d days" % (today - date_joined).days
            books = list(mongo.db.books.find().sort('_id', -1))
            genres = list(mongo.db.genres.find().sort("genre", 1))
            avgrating = list(mongo.db.avgRatingAgg.find())
            if "books_added" in user:
                books_added = user.get("books_added")
                total_books = len(user['books_added'])
                books_added = books_added[:5]
            else:
                books_added = 0
                total_books = 0
            if "reviews_added" in user:
                reviews_added = user.get("reviews_added")
                total_reviews = len(user['reviews_added'])
                reviews_added = reviews_added[:5]
            else:
                reviews_added = 0
                total_reviews = 0
            return render_template(
                "profile.html",
                user=user,
                books=books,
                user_duration=user_duration,
                books_added=books_added,
                reviews_added=reviews_added,
                bookcount=total_books,
                reviewcount=total_reviews,
                genres=genres,
                avgratings=avgrating)
        else:
            return redirect(url_for("access_denied"))


# logout
@app.route("/logout")
def logout():
    """
    On click, end the users session.
    redirect the user to login.html.
    """
    # remove user from session cookies
    flash("You have successfully been logged out.", "success")
    session.pop("user")
    return redirect(url_for("login", _external=True, _scheme='https'))


# bookpage for each book
@app.route("/bookpage/<book_id>")
def bookpage(book_id):
    """
    Checks in the book has reviews.
    If true, the array is checked and an average rating is calculated.
    If the review array is empty, no average rating is calculated,
    If there is no review document, no average rating is calculated.
    the user is redirected to the bookpage
    """

    get_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    reviews = get_book.get("review")
    genres = list(mongo.db.genres.find())
    for genre in genres:
        if ObjectId(get_book["genre_id"]) == ObjectId(genre["_id"]):
            genre_name = genre["genre_name"]

    #  add average rating aggregation to a new collection
    if reviews:
        for review in reviews:
            if review:
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
                review = "No star ratings added yet"
    else:
        review = "No star ratings added yet."
    return render_template(
        "bookpage.html",
        get_book=get_book,
        review=review,
        genre_name=genre_name
    )


# add a book page
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """
    Checks if method = POST.
    if true, the data entered on the form is saved to db.
    The user is redirected to books.html.
    If method != POST, the user is redirected to add_book.html.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        if request.method == "POST":
            genres = list(mongo.db.genres.find())
            genre_name = request.form.get("genre_name")
            for genre in genres:
                if genre["genre_name"] == genre_name:
                    genre_id = ObjectId(genre["_id"])
            book = {
                "genre_id": genre_id,
                "book_name": request.form.get("book_name"),
                "author": request.form.get("author"),
                "image_url": request.form.get("image_url"),
                "description": request.form.get("description"),
                "buy_url": request.form.get("buy_url"),
                "created_by": session["user"],
            }
            mongo.db.books.insert_one(book)
            update_user_books(book["created_by"], book["_id"])
            flash("Book was successfully added.", "success")
            return redirect(url_for("books_new"))

        genres = mongo.db.genres.find().sort("genre_name", 1)
        return render_template(
            "add_book.html",
            genres=genres)


# add book to user
def update_user_books(username, bookid):
    mongo.db.users.update_one(
                {"username": username}, {
                    "$addToSet": {"books_added": {
                        "book_id": ObjectId(bookid)}}})


# edit a book page
@app.route("/<book_id>/edit_book", methods=["GET", "POST"])
def edit_book(book_id):
    """
    Checks if method = POST.
    If true, the form data is used to update db.
    User is redirected to bookpage.html.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        get_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        if request.method == "POST":
            genres = list(mongo.db.genres.find())
            genre_name = request.form.get("genre_name")
            for genre in genres:
                if genre["genre_name"] == genre_name:
                    genre_id = ObjectId(genre["_id"])
            mongo.db.books.update({"_id": ObjectId(book_id)}, {"$set": {
                "genre_id": genre_id,
                "book_name": request.form.get("book_name"),
                "author": request.form.get("author"),
                "image_url": request.form.get("image_url"),
                "description": request.form.get("description"),
                "buy_url": request.form.get("buy_url"),
                "created_by": session["user"]
                }}
            )
            flash("Book was successfully updated.", "success")
            return redirect(url_for(
                "bookpage", book_id=book_id))

        genres = mongo.db.genres.find().sort("genre_name", 1)
        return render_template(
            "edit_book.html", get_book=get_book, genres=genres)


# delete a book page
@app.route("/<book_id>/delete_book")
def delete_book(book_id):
    """
    On click, deletes the book data from db.
    User is redirected back to the homepage.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        username = session["user"]
        mongo.db.books.remove({"_id": ObjectId(book_id)})
        delete_user_books(username, book_id)
        flash("Book was sucessfully deleted.", "success")
        return redirect(url_for("books_new"))


def delete_user_books(username, book_id):
    mongo.db.users.update_one(
        {"username": username, "books_added.book_id": ObjectId(book_id)},
        {"$pull": {"books_added": {"book_id": ObjectId(book_id)}}}
    )


# add a review in bookpage
@app.route("/bookpage/<book_id>", methods=["POST"])
def review_book(book_id):
    """
    Checks if method = POST.
    If true, checks if user has already posted a review on the book.
    If false, the form data is saved to db
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        get_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        reviews = get_book.get("review")
        date = str(datetime.date.today())
        #  save the review if method is post
        if request.method == "POST":
            if reviews:
                for review in reviews:
                    #  if user has already posted a review, stop them
                    if review["username"] == session["user"]:
                        flash(
                            "You previously reviewed this book." +
                            " Please edit or" +
                            " remove the existing review.", "error")
                        return redirect(url_for(
                            "bookpage",
                            book_id=book_id))
            #  else allow user to post review
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(8))
            mongo.db.books.update_one(
                {"_id": ObjectId(book_id)}, {
                    "$addToSet": {"review": {
                        "title": request.form.get("review_title"),
                        "description": request.form.get("review"),
                        "rating": int(request.form.get("rate")),
                        "date": date,
                        "review_id": password,
                        "bookid": str(ObjectId(book_id)),
                        "username": session["user"]}}})
            username = session["user"]
            update_user_reviews(username, password)
            flash("Review was successfully saved.", "success")
        else:
            review = "No star ratings yet"
        return redirect(url_for(
            "bookpage",
            book_id=book_id))


# update user document with review_id
def update_user_reviews(username, reviewid):
    mongo.db.users.update_one(
        {"username": username}, {
            "$addToSet": {"reviews_added": {
                "review_id": reviewid}}}
    )


# edit a review page
@app.route("/<book_id>/<username>/<review_id>/editreview", methods=[
    "GET", "POST"])
def edit_review(book_id, username, review_id):
    """
    Checks if user is admin or is the review author.
    If true, edit review.html is rendered.
    Checks if method = POST:
    If true, the form data is used to update the review & the user is
    redirected to bookpage.html.
    If user is not admin or review author, redirect to bookpage.html.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        username = mongo.db.users.find_one(
            {"username": session['user']})["username"]
        get_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        reviewarray = list(mongo.db.books.find(
            {'review': {"$elemMatch": {"review_id": review_id}}}, {
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
                {"_id": ObjectId(book_id), "review.review_id": review_id},
                {"$set": {
                    "review.$.title": request.form.get("review_title"),
                    "review.$.description": request.form.get("review"),
                    "review.$.rating": int(request.form.get("rate")),
                    }}
            )
            flash("Review was successfully updated.", "success")
            return redirect(url_for(
                "bookpage",
                book_id=book_id))

        if session["user"] == username or session["user"] == "admin":
            return render_template(
                "editreview.html",
                get_book=get_book,
                review=review,
            )
        else:
            return redirect(url_for(
                "bookpage", book_name=get_book.get("book_name")))


# delete a review
@app.route("/<book_id>/<username>/<review_id>/deletereview")
def delete_review(book_id, username, review_id):
    """
    On click, the review data from the book document is removed.
    the average rating value for that book is also removed.
    The user is redirected to bookpage.html.

    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        get_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        mongo.db.books.update(
            {"_id": ObjectId(book_id), "review.review_id": review_id},
            {"$pull": {"review": {"review_id": review_id}}})
        flash('Review was successfully removed.', "success")
        {"_id": ObjectId(book_id), "review.review_id": review_id}
        mongo.db.avgRatingAgg.remove({
            "_id": ObjectId(book_id)
            })
        username == session["user"]
        delete_user_review(username, review_id)
        return redirect(url_for(
            "bookpage",
            book_id=book_id))


def delete_user_review(username, review_id):
    mongo.db.users.update_one(
        {"username": username, "reviews_added.review_id": review_id},
        {"$pull": {"reviews_added": {"review_id": review_id}}}
    )


# manage genres page
@app.route("/get_genres")
def get_genres():
    """
    Returns a list of gneres sorted alphabetically
    on genres.html.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        genres = list(mongo.db.genres.find().sort("genre_name", 1))
        return render_template("genres.html", genres=genres)


# add a genre page
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """
    Checks if method = POST.
    If true, the data from the form is added to db.
    The user is redirected to genres.html.
    if methos != POST, add_genre.html is rendered.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        if request.method == "POST":
            genre = {
                "genre_name": request.form.get("genre_name"),
                "genre_icon": request.form.get("genre_icon")
            }
            mongo.db.genres.insert_one(genre)
            flash("Genre was successfully added.", "success")
            return redirect(url_for("get_genres"))

        return render_template("add_genre.html")


# edit a  genre page
@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    """
    checks if method = POST.
    if true, the genre is updated with the form data.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        if request.method == "POST":
            save = {
                "genre_name": request.form.get("genre_name"),
                "genre_icon": request.form.get("genre_icon")
            }
            new_genre_name = {
                "genre_name": request.form.get("genre_name")
            }
            mongo.db.genres.update({"_id": ObjectId(genre_id)}, save)
            flash("Genre was successfully updated.", "success")
            return redirect(url_for("get_genres"))

        genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
        return render_template("edit_genre.html", genre=genre)


# delete a genre
@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    """
    on click, remove the genre from db.
    Redirect the user back to genres.html
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for("access_denied"))
    else:
        mongo.db.genres.remove({"_id": ObjectId(genre_id)})
        flash("Genre was successfully deleted.", "success")
        return redirect(url_for("get_genres"))


# 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# access denied page
@app.route("/access_denied.html")
def access_denied():
    return render_template("access_denied.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
