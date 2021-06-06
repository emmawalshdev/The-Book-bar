# The Book bar

## Data Centric Development - Milestone Project

[View the Live Site here.](https://the-book-bar.herokuapp.com/)

![logo](assets/images/readmeFiles/readmeLogo.png) 

![Generated from Am I Responsive](assets/images/readmeFiles/TheBookbar.jpg)


The Book bar was created by Emma Harte to serve readers worldwide.
Data driven, the website assists users in finding their next great read; offering both a book upload and recommendation service.
In this way, users are able to share opinions and knowledge with the greater Book bar community. 

In this project, full CRUD functionality is present. 
Security features are also present. Such include user permissions for the 'admin' user and safe storage of passwords and security-sensitive information.


----------------------------

## Contents
1. [UX](#ux)
      - [Strategy](#strategy)
      - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Project Scope](#project-scope)
      - [In Scope](#in-scope)
      - [Out of Scope](#out-of-scope)
    - [Wireframes](#wireframes)
    - [Design](#design)
      - [User journey](#user-journey)
      - [Typography](#typography)
      - [Color Scheme](color-scheme)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database information](#database-information)
    - [Datatypes](#datatypes)
    - [Collections information](#collection-information)

4. [Technologies Used](#technologies-used)
    - [Database](#database) 
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

5. [Testing](https://github.com/emmahartedev/The-Book-bar/blob/master/testing.md)
    
6. [Deployment](#deployment "goto deployment")

7. [Credits](#credits "goto credits")
    - [Content](#content "goto Content")
    - [Code](#code "goto code")
    - [Media](#media "goto media")
    - [Acknowledgments](#acknowledgments "goto acknowledgments")

----------------------------

## UX

### Strategy
The following information was declared during UX research, as part of the 5 plane investigation:

* The website will be created to target book lovers, of an age between 15 and 55.
  More specifically, the website aims to target tech-savy book lovers.

* Only useful, useable or essential data will be stored within the website.
  E.g., for books, data fields will include title, author, a cover image URL etc.

* In investigating in-scope features for this release, the Impportance v Feasibility was studied. Below is a graphic showcasing the results.

![ivf](assets/images/readmeFiles/ivf.jpg) 

### User Stories

#### Visitor stories:
**As an external user**:

1. I want to be able to search for a book by book title or author, so that I can find out more information. 

2. I want to be able to search the database by genre, so that I can find a suitable book.

3. I want to be able to sort the entire database, so that I can view all books.

4. I want to be able to login or register for an account on the website, so that I can access my profile, upload books and add reviews.

5. I want to see a snapshot of activity on my profile, so that I can quicky see my recent contributions.

6. I want to be able to upload a book to the website, so that I and others can then review it.

7. I want to be able to make changes or delete a book that I have uploaded, in case an error has been made.

8. I want to be able to review and rate any book on the website, so that other users can quickly see what I thought about it.

9. I want to be able to edit and delete reviews that I have added, in case an error has been made.

10. I want to know the average star rating for each book, as this will help me choose my next read.

11. I want to know that my data is securely stored, as this is a worry of mine.


#### Business stories:
**As the website owner**:

1. I want to be able to add new book genres on the website, so that users can select these when uploading a book.

2. I want to be able to edit and delete book genres, in case an error has been made.

3. I want to see a snapshot of activity on my profile, so that I can quicky see my recent contributions.

4. I want to add a 'Buy now' link to each book so that I can potentially make money off click through sales.

5. I do not want to allow duplicate book titles to be published, this would lead to a bad customer experience.
 
6. I only want registered users (logged in) to be able to add reviews and books, for monitoring reasons.

7. I want to be able to edit and delete all content created on the website, for monitoring reasons.

### Project Scope
As part of the 5 plane investigation, the project scrope was defined.
During this process, the functional and content requirments were examined.
In considering the functional requirements, each problem was examined to find a best-fit solution.
In considering the content requirements, the following were questioned: 
  a) What type of content would fulfil the need (image, video, text, mixed)
  b) Whether or not adequate resources were available to produce the content.
The following is a statement of the findings:

#### In scope

* User login and account registration
  - Only if a user is registered and logged in, can the user upload books and add reviews.

* An admin account for the website owener
  - Only with an 'admin' user account, can the user to edit & delete all content.
  - This is essential for website management and maintenace.

* A search bar
  - With search bar functionality, can a user find a book suitable to their needs.

* A search by book genre functionality. (nice to have)
  - By adding a search by genre layer, the user experience will be improved
  - A nice to have, not essential but to be considered if time is not an issue.

* Full CRUD functionality.
  - This should be present for two permission roles: 'admin' and non-admin users.
  - The 'admin' user should have full CRUD functionality for all content. 
  - Non-users should have full CRUD functionality for content they have created themselves.
  - The users actions should be reflected immediately on the front-end.

* Content will be mostly text and imagery
  - As this project is data-focused, less time will be spent on front-end development.

* A 'buy now' link will be added to each new book uploaded.  
  - This will allow the website owner to profit from book sales.

* Users will be able to add books and reviews
  - This is essential in creating a functional book recommendation service 

* A rating functionality will be added as part of each review
  - This is essential in creating a functional book recommendation service 

#### Out of scope

* A sophisticated recommendation algorithm, based on books upvoted by user.
  - Not possible within the current time-frame and due to personal skillset

* A customised dashboard for users. The user will not be shown on their profile: recommendations.
    - Not possible within the current time-frame and due to personal skillset
    - The dashboard will include less sophisticated information such as recent contributions.

* Video banners, striking imagery & dynamic front-end development.
  - As this project is data-focused, less time will be spent on front-end development.

### Wireframes
All wireframes were created using the software [Balsamiq](https://balsamiq.com/). 
These layouts were created following research on the five planes of UX, and before coding.\
\
<strong>
Please note, the final website layout contains slight variations to the original wireframes.
Each of the following files contain wireframes for desktop, tablet, and mobile devices.
</strong>
 
**Users - non admin**
- [Homepage](assets/images/readmeFiles/wireframes/home.png)
- [Login](assets/images/readmeFiles/wireframes/login.png)
- [Register](assets/images/readmeFiles/wireframes/register.png)
- [Profile](assets/images/readmeFiles/wireframes/profile.png)
- [Add a book](assets/images/readmeFiles/wireframes/addABook.png)
  - The edit book page will be a direct copy of the 'add a book' page.
  - The fields will be pre-selected.
- [Book page](assets/images/readmeFiles/wireframes/bookPage.png)

**User - admin only**
- [Manage categories](assets/images/readmeFiles/wireframes/manageGenresAdmin.png)
  - The 'add genre' book page will be a direct copy of the 'add a book' page.
    - It will contain two fields: genre title and an icon name.
  - The 'Edit genre' will be a direct copy of the 'add genre' page. 
    - The fields will be pre-selected.

### Design

#### User journey
- The website structure was designed to be consistent, predictable, learnable, visable and provide user feedback.
- A user journey for non-admin users was created to aid the stuctural design.
  ![user journey](assets/images/readmeFiles/userjourney.jpg) 


#### Typography
- All fonts used in this project derive from [Google Fonts](https://fonts.google.com/). 

- Fonts used include:
  - [Raleway](https://fonts.google.com/specimen/Raleway?query=raleway) - used for h1 - h4
  - [Lato](https://fonts.google.com/specimen/Lato?query=lato) - used for h5 - h6 and all other body text


#### Colour scheme
- A pink and blue colour palette was used in this design.
- Although contrasting, pink is associated with romance and lightness and blue creates a feeling of calmness. Used together, these colours create a positive mood.
- The following colour palette was used for inspiration:
  ![colour palette](assets/images/readmeFiles/colorpal.jpg)

--------------------------------------------------------------------------------------------

## Features

### Existing Features 

#### Elements on all pages

- NavBar
  - The navigation features The Book bar logo in the top left corner in desktop view. This switches to a center position on smaller screen sizes.

  - Access rights:
    - Certain links are viewable only to a logged in user. To check if a user is logged in, ```if 'user' in session``` is used in Python. This information is then passed to the jinja template, to determine access rights.

    - Centain links are only viewable to the 'admin' user. To determine access rights, ```if session.user|lower == "admin"|lower``` is used in the jinja template. 

    - Below is a full list of navbar links shown for each user type.

      - For **all users** who **are not logged in**, the following links are viewable:
        1. Home 
        2. Login
        3. Register

      - For **non admin users** who **are logged in**, the following links are viewable:
        1. Home
        2. Profile
        3. Add a Book
        4. Logout

      - For an **admin user** who **is logged in**, the following links are viewable:
        1. Home
        2. Profile
        3. Add a Book
        4. Manage Genres
        4. Logout


- Footer
  - The footer includes the following:
    - Copyright information with a Github link.
    - Clickable Social media links.

#### Homepage

- Search bar
  - Using the search bar, the user is able to return results by entering an author or book title.
  - To search the entire database, a 'Sort by' function is available. 
    - The user can sort the database in three ways: 
      1. A-Z
      2. Z-A
      3. New-Old

  - Once a user clicks the submit button on the search bar, one of the following occurs:
    - No results found:
      - No book cars are returned.
      - The 'Sort by' button disapears.
      - User feedback is returned. This states that the search was unsuccessful.
      - An animated book gif is displayed.
      - A 'Reset' button is displayed. If clicked, the user is redirected back to the homepage.

    - Results found:
      - All book cards matching the keyword are returned
      - The 'Sort by' button disapears
      - A 'Reset' button is displayed. If clicked, the user is redirected back to the homepage.

- Pagination
  - Pagination is present on all three versions of the homepage (A-Z, Z-A and New-Old).
  - On each page, 12 book cards are displayed.
  - This allows for faster page-load time and a better user experience.

- Book cards
  - All book cards are styled with a dark-mode theme for easy viewing.
  - Each book card includes the following:
    - The book cover image.
    - The Book title and author.
    - An average star rating
    - An icon representing the genre type.

  - The data feaured on each book card derives from user input, which is stored is the database. Fields include:
    - The title, author, book image data is pulled from the books collection.
    - The genre data is pulled from the genres collection.
    - The average review rating is pulled from the AvgRatingAgg (average rating aggregation) collection.
    - Once data is updated in a collection, the information displayed on the book card is automatically updated.

#### Add a book
- Accessibility
  - To access the page, the user must be logged in.
  - Users who are not logged in will be redirected to the access denied page.

- User pathways
  - Two pathways are possible on this page: 
    - Add (submit data)
    - Cancel (go back)

  - Add (submit data)
    - The following fields are included on the form:
      - Book Title (required)
      - Author (required)
      - Blurb (required)
      - Book Genre (required)
      - Image URL (required)
      - Buy Now URL
  
    - Upon submission, the book document is inserted into the books collection

  - Cancel (go back)
    - When clicked, the user is redirected back to the homepage.

#### Bookpage
* **Book section**
  - The relevent book data is displayed in the first section of the page.
  - This data is pulled from the book, genre and AvgRatingAgg (average rating aggregation) collection.
  - This data displayed on the front-end includes:
    * Book title
    * Author
    * Genre
    * Book image
    * Description
    * 'Buy Now' link
    * Average star rating
  
* **Posted Reviews section**
  - Each review posted is displayed on a card within the 'User Reviews' section.
  - This data is pulled from an object of the 'review' array, within the book collection.
  - An 'Edit' button appears behind the card, if the session user is the content creater or 'admin'. 
  - The data displayed on the front-end includes:
    1. Review title
    2. Summary
    3. Review author
    4. Date posted
    5. Star rating


* **Add a review section**
  - Accessibility
    - The 'Add a Review' form is only accessible to users who are **logged in**
    - If a user is not logged in, feedback is returned. This states that the user must be logged in to add a review.

  - Form content
    - The form includes the following fields:
      1. Title (required)
      2. Summary
      3. Select a star rating (required)

  - Submission behaviour
    - First review (per book by user):
      - When submitted, the review lives as an object of the 'review' array within the book document.
      - Upon submission, the user is redirected back to the bookpage. With this, the AvgRatingAgg document is also updated.
      
    - Multiple reviews (per book by user):
      - Only one review per book is permitted by a user.
      - This information is stated on the review form. 
      - If a user attempts to add a second review, error feedback is returned.

#### Edit book
- Accessibility
  - To access the page, the user must be either the content creater or 'admin'. The user must also be logged in.
  - Users who are not logged in, and/or are not the content creater or 'admin', will be redirected to the access denied page.

- User pathways
  - Three pathways are possible on this page: 
    - Save (submit data changes)
    - Cancel (go back)
    - Delete (remove book document from collection)

  - Save (submit data changes)
    - Upon submission, the book document is immediately updated.
    - The following fields can be edited and saved:
      - Book Title
      - Author
      - Blurb
      - Book Genre
      - Image URL
      - Buy Now URL

  - Cancel (go back)
    - When clicked, the user is redirected back to the bookpage.
  
  - Delete (remove book document from collection)
    - A modal appears, asking for confirmation of deletion.
    - if confirmed, the book document is removed from the books collection.
    - If the user does not confirm deletion, the modal closes and the user returns to the edit book page.

#### Edit review
- Accessibility
  - To access the page, the user must be either the content creater or 'admin'. The user must also be logged in.
  - Users who are not logged in, and/or are not the content creater or 'admin', will be redirected to the access denied page.

- Book section
  - As the book information may be useful for review editing, this section has been included in the template.

  - This data displayed here includes:
    * Book title
    * Author
    * Genre
    * Book image
    * Description
    * 'Buy Now' link
    * Average star rating

- User pathways
  - Save (submit data changes)
  - Cancel (go back)
  - Delete (remove object from review array in book document)

  - Save (submit data changes)
    - The following fields can be edited and saved:
      - Review title
      - Summary
      - Star rating
    - Upon submission, the review array object is immediately updated.
    - Upon submission, the user is redirected back to the bookpage. With this, the AvgRatingAgg (average rating aggregation) collection is also updated.

  - Cancel (go back)
    - When clicked, the user is redirected back to the bookpage.

  - Delete (remove object from review array in book document)
    - A modal appears, asking for confirmation of deletion.
    - if confirmed, that object in the review array is removed.
    - If the user does not confirm deletion, the modal closes and the user returns to the edit review page.

#### Login page
 - Content
  - A link to the registration page is displayed for easy access.

- Submission behaviour
  - If the username exists in the database:
    - The password is checked.
    - If the password inputted matches the hashed password, the user is directed to the profile page.
    - If the password inputted does not match the hashed password, an error flash message is displayed and the user is redirected to the login page

  - if the username does not exist in the database:
    - An error flash message is displayed. The user is redirected back to the login page.

#### Register page
- Submission behaviour
  - If the username does not exists in the database:
    - A unique hashed password is generated
    - The username and hashed password are inserted as a new document to the users collection
    - The user is redirected to the login page

  - If the username exist in the database:
    - An error flash message is displayed and the user is redirected back to the register page

#### Manage genres
- Accessibility
  - The Manage Genres page is only accessible to an 'admin' user. The user must also be logged in.

- Content
  - Users have the option to 'Add' a genre or manage the existing genres.
  - Existing genres are displayed on card. Each card contains the following:
    - The genre title & a genre icon.
    - An 'Edit button.'

#### Add genre
- Accessibility
  - To access the page, the user must an 'admin' user. The user must also be logged in.
  - Users who are not an 'admin' user, and/or who are not logged in; will be redirected to the access denied page.

- User pathways
  - Two pathways are possible on this page: 
    - Add (submit data)
    - Cancel (go back)

  - Add (submit data)
    - The following fields are included on the form:
      - Genre Name (required)
      - Icon Name (required)

    - Upon submission, the genre document is inserted into the genres collection

  - Cancel (go back)
    - When clicked, the user is redirected back to the manage genres page.

#### Edit genre
- Accessibility
  - To access the page, the user must be an 'admin' user. The user must also be logged in.
  - Users who do not fulfil this requirement, will be redirected to the access denied page.

- User pathways
  - Three pathways are possible on this page: 
    - Save (submit data changes)
    - Cancel (go back)
    - Delete (remove genre document from collection)

  - Save (submit data changes)
    - Upon submission, the genre document is immediately updated.
    - The following fields can be edited and saved:
      - Genre Name (required)
      - Icon name (required)

  - Cancel (go back)
    - When clicked, the user is redirected back to the manage genres page.
  
  - Delete (remove genre document from collection)
    - A modal appears, asking for confirmation of deletion.
    - if confirmed, the book document is removed from the genres collection.
    - If the user does not confirm deletion, the modal closes and the user returns to the manage genres page.
  
#### Profile page
- Accessibility
  - To access this page, a user must be logged in. 
  - Each user's profile page can only be accessed by that user. To confirm that the user in session does indeed match the profile username, Python runs the following: 
  ```if username == session["user"]:```
  - Users who are not logged in or do not match details with the username stored, will be redirected to the access denied page.

- Welcome section
  - A Welcome, username message is displayed.
  - A date of memebership duration is displayed.

- Profile card
  - A quick link to the homepage is provided
  - A summary of the users activity is displayed. Two statistics are included:
    - **Books added:**
      - An aggregation operation calcualted the count of books created by the user 
    - **Review:** 
      - An aggregation operation calcualted the count of reviews created by the user 

- Books added section
  - If a user has added books:
    - The 4 most recent books added by the user are shown
    - This view automatically updates once the user adds a new book

  - If a user has not added any books:
    - A card is dispalyed which notifies the user that the 4 most recent book uploads will appear in this section
    - A quick link to the book upload page is added

- Reviews added section
  - If a user has added reviews:
    - The 4 most recent reviews added by the user are shown
    - This view automatically updates once the user adds a new review

  - If a user has not added any reviews:
    - A card is dispalyed which notifies the user that the 4 most recent reviews will appear in this section
    - A quick link to the homepage is added

#### 404 page
- Behaviour
  - The 404 page is returned when a requested page cannot be found

- Content
  - This template incorporates the Book bar website styling and includes a link to the homepage.

#### Access denied page
- Behaviour
  - The access denied webspage is returned if a user requests a webpage which they do not permission to view.

- Content
  - This template incorporates the Book bar website styling and includes a link to the homepage.

### Features Left to Implement
The following are features which were not included in this release. Once adequate time and a developed skillset are available, these points will be revisted.

* Email authentication for account registration
  - Implement email authentication for users who are registering an account. This would be a requirement.

* Admin role creation
  - Create an 'administrator' role, which could be applied to several user accounts.
  - The role would grant users special permissions.
  - Currently there can be only one 'Admin' user, this is the account with the username of 'admin'. Unfortunately, this solution is not scaleable.

* Search bar filters & sort by
  - Attempted to implemented this at the beginning of the project. The plan was to include a fiter for 'category' and a 'sort by' function for results. After several days, I decided to move forward with the project and to leave this feature as a 'nice to have'. Unfortunately there was not enough time to revisit the task. 

* Add instant verification on book image, genre icon and 'Buy now' URL upload:
  - With the current set up, no instant verification is available. The user does not know that the link entered is working until the template page has rendered. 
  - With instant verification, the user would recieve feedback before they submit a form.  
  - This would would reduce the workload for content moderation and improve the user experience. 

## Information Architecture

### Database information
- MongoDB (a project requirement):
  - This project utilizes MongoDB; a NoSQL database.
  - MongoDB allows users to use “unstructured data.” This means you can build your application without having to first define the schema.
  - The MongoDB database was chosen, as this is a requirement for the Milestone Three, code institute project.

- Take-away houghts:
  - A pre-defined schema would have simplified the development of the overall project.
  - Due to the drawbacks of the non ACID compliance of NoSQL, an A SQL database structure would have suited this project better.

### Datatypes
  - The datatypes utilized in this project include the following:
    - ObjectId
    - String
    - Boolean
    - DateTime
    - Object

### Collections information
'The Book bar' involves 4 database collections. The details of each collection are detailed below.

  #### Users collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Username | username | text, `maxlength="15"` | string
Password | password | text, `maxlength="15"` | string
Books Added by User | books_added | none | array
Reviews Added by User | reviews_added | none | array

[Example JSON from the users collection](assets/json_structures/users_collection.json)

#### Genres collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Genre ID | _id | None | ObjectId 
Genre name | genre_name |text, `maxlength="50"` | string
Genre icon | genre_icon | text, `maxlength="20"` | string

[Example JSON from the genres collection](assets/json_structures/genres_collection.json)

 #### Books collection

 | Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Book ID | _id | None | ObjectId 
Genre ID | genre_id | None | ObjectId
Book Title | book_name | text, `maxlength="50"` | string
Book Author | author | text, `maxlength="30"` | string 
Book Description | description | text, `maxlength="790"` | string
URL for Cover Image | image_url | text, `maxlength="150"` | string
URL to Shop the Book | buy_url | text, `maxlength="150"` | string
Uploaded by | created_by| none | string 
Password | password | text, `maxlength="15"` | string
Review array | review | none | array

[Example JSON from the genres collection](assets/json_structures/book_collection.json)


 #### avgRatingAgg collection (average rating aggregation))

 | Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Book ID | _id | None | ObjectId 
Average Star Rating | averageRating | radio | double

[Example JSON from the genres collection](aassets/json_structures/avgRatingAgg_collection.json)

----------------------------

## Technologies Used

### Database

* [MongoDB Atlas](https://www.mongodb.com/) - Used as the primary database for storing and retrieving the information in the website.

### Languages

* [HTML5](https://www.w3schools.com/html/) - Used for structuring the site pages.

* [CSS](https://www.w3schools.com/css/) - Used for styling the site pages.

* [Javascript](https://www.w3schools.com/js/DEFAULT.asp) - Used to make the website interactive.

* [Python](https://www.python.org/) - Used to create database driven functionalities.

### Libraries

* [jQuery](https://jquery.com/) - Used to make the website interactive.

* [PyMongo](https://pypi.org/project/pymongo/) - Used to make communication between MongoDB and Python.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Used to construct and render pages.

* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - used in conjunction with flask to display data from the backend.

### Tools

* [Gitpod](https://www.gitpod.io/docs/) - Used as a development environment.

* [PIP](https://pip.pypa.io/en/stable/installing/) - Used for tool installions.

* [Git](https://www.gitpod.io/docs/) - Used to handle version control.

* [Github](https://github.com/) - Used for repository hosting.

* [Github Pages](https://pages.github.com/) - Used for site deployment.

* [Materialize](https://materializecss.com/about.html) - Used to develop the website design system.

* [Canva](https://www.canva.com/) - Used to create the brand logo.

* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) - Used to resize and edit images.

* [Favicon.io](https://favicon.io/favicon-converter/) - Used for flavicon creation.

* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create repsonsive images for different devices.

* [Google Fonts](https://fonts.google.com/) - Used for typography.

* [Font Awesome](https://fontawesome.com/) - Used for footer Icons.

* [Google Icons](https://fonts.google.com/icons) - Used for all Icons (bar footer icons).

* [LottieFiles](https://lottiefiles.com/) - all free animations are sourced from here.

* [Chrome Dev tools](https://developers.google.com/web/tools/chrome-devtools) - Used for monitoring the responsiveness of the website.

* [LamdaTest](https://www.lambdatest.com/) - Used for monitoring the responsiveness of the website.
### Deployment

* [Heroku](https://id.heroku.com/login) - The cloud platform used to deploying the website.
----------------------------
## Testing
All testing documentation is stored in a separate testing file, which can be accessed [here](https://github.com/emmahartedev/The-Book-bar/blob/master/testing.md).

----------------------------

## Deployment

### Local Deployment
To run this project on your own IDE, ensure that the following are installed on your machine:

  * [Python 3](https://www.python.org/download/releases/3.0/)
  * [PIP](https://pypi.org/project/pip/)
  * [Git](https://git-scm.com/)

Additionally, make sure that you also have the following set up: 
  * [A MongoDB Atlas account](https://www.mongodb.com/)

#### Forking the repository
To fork the repository, the following steps must be followed:
1. Navigate to the project repository [project repository](https://github.com/emmahartedev/The-Book-bar).

2. Click "Fork", located on the top right of the screen.

3. You have successfully forked the repository. A copy of the original project will now be copied to your account.

4. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to [.gitignore](https://git-scm.com/docs/gitignore/en) file to ensure it is not uploaded.

5. Run the application using the command: ```python3 app.py```

#### Cloning the repository
To clone the repository, the following steps must be followed:

1. Navigate to the project repository [project repository](https://github.com/emmahartedev/The-Book-bar).

2. Click 'Code' and in the Clone with HTTPs, copy the provided repository URL. 

3. Open a terminal in your IDE.

4. Change the current working directory to the location you wish to generate the cloned directory.

5. Type ```git clone```, and then paste the URL from step 2. 

```
git clone https://github.com/emmahartedev/The-Book-bar.git
```
6. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to [.gitignore](https://git-scm.com/docs/gitignore/en) to ensure it is not uploaded.

7. Run the application using the command: ```python3 app.py```

### Heroku Deployment
To deploy 'The Book bar' to Heroku, the following steps must be followed:
  1. Create a [requirements.txt](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e) file using the command ```pip freeze > requirements.txt```.

  2. Create a [Procfile](https://devcenter.heroku.com/articles/procfile) using the command ```echo web: python app.py > Procfile```.

  3. Add both files to Github by using ```git add```, then ```git commit -m "Add a relevent git message here"``` and finally ```git push```.

  4. Navigate to the [Heroku](https://id.heroku.com/login) website. On the dashboard page, click "New", then click "Create new app". Add a name and a region.

  5. Connect the Heroku app to the Github repository. On the Heroku app dashboard, select the "Deploy" tab. Under "Deployment method", select "Github" and confirm.

  6. Navigate to the "Settings" tab in the app dashboard. Under "Config Vars" click "Reveal Config Vars".

  7. Set the following config vars:

  | Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`
 
8. In the Heroku app click on the "Deploy" tab and navigate to the "Manual Deployment" section. Confirm that the "master" brance is selected and click "Deply Branch".

9. The website is now successfully deployed.

----------------------------

## Credits 
The following material is not my own. Sources have been listed alongside a description of the content used. 

### Content

* [Web Gradients](https://webgradients.com/) - Used for inspiration to create the linear-gradient background.


### Code
The following code was used directly in this project:
  * [Codepen - hesguru](https://codepen.io/hesguru/pen/BaybqXv) - used to create the star rating bar for reviews.
  * [Python - secrets code](https://docs.python.org/3/library/secrets.html) - used to generate random ids for each review.

The following code has been modied in this project:
  * [stackoverflow - dippas](https://stackoverflow.com/questions/37127123/change-color-of-underline-input-and-label-in-materialize-css-framework/37127156) - used to change the color of the materialize input fields.


###  Media
The images used on this website were obtained from the following sources:


README.md:
* Colour palette - [Source](https://www.pinterest.de/pin/490681321896937815/)

Homepage
* No search results (book gif) - [Source](https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets7.lottiefiles.com%2Ftemp%2Flf20_aKAfIn.json)

Bookpage
* Static stars for rating (grey and gold) - [Source](https://www.freepik.com/free-vector/star-rating-with-two-different-backgrounds_1014851.htm#page=1&query=star%20rating&position=2)

* No reviews yet (stars gif) - [Source](https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets4.lottiefiles.com%2Fpackages%2Flf20_twYDL9.json)

Profile page
* Green and blue user icon - [Source](https://www.flaticon.com/free-icon/user_747545?term=user&related_id=747545)

* Stacked books icon - [Source](https://www.flaticon.com/free-icon/books_167756?term=books&page=1&position=35&page=1&position=35&related_id=167756&origin=search)

* Added books section, no books added yet image - [Source](https://images.pexels.com/photos/3457273/pexels-photo-3457273.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)

* Added reviews section, no reviews added yet image - [Source](https://www.pexels.com/photo/selective-focus-photography-of-person-using-iphone-x-1542252/)


### Acknowledgments
* Thank you to Gerald mcBride for his help and guidance thoughout this project.
