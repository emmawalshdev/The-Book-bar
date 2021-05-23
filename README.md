# The Book bar

## Data Centric Development Milestone Project

[View the Live Site here.]()

![ logo](logo/logo.png) 

![Generated from Am I Responsive](assets/images/readme_files/amiresponsive.jpg)


The Book bar website offers an online book review and recommendation service. 
This project is data focused, allowing users to share their own data with the greater
community of users.

The website has two main goals. For the user, finding a suitable book based on recommendations will be acheived.
For the website owner, a link will be added to each book uploaded which will allow them to earn money through each purchase.
sales pitch

----------------------------

## Contents
1. [UX](#ux "goto-ux")
    * [Overview](#overview "goto overview")
    * [User Stories](#user-stories "goto user stories")
    * [Project Scope](#project-scope "goto project scope")
    * [Design](#design "goto design")
    * [Wireframes](#wireframes "goto wireframes")

2. [Features](#features "goto features")
    * [Existing Features](#existing-features "goto existing features")
    * [Features Left to Implement](#features-left-to-implement "goto features left to implement")

3. [Technology Used](#technology-used "goto technology used")

4. [Testing](https://github.com/emmahartedev/ms2-teachflow/blob/master/testing.md)
    
5. [Deployment](#deployment "goto deployment")

6. [Credits](#credits "goto credits")
    * [Content](#content "goto Content")
    * [Code](#code "goto code")
    * [Media](#media "goto media")
    * [Acknowledgments](#acknowledgments "goto acknowledgments")

----------------------------

## UX

### The five plane

#### The Strategy plane
* The target audience for this website will be book lovers, of an age between 15 and 55.
The website aims to target tech-savy book lovers.
* The content stored on each book will include only relevent fields such as title, author and  a link to a cover image.
* Impportance v Feasibility was studied to ensure the most appropriate feature would be developed in this release.
Below are the results.
![ivf](assets/images/readmeFiles/ivf.jpg) 

### User Stories

#### External user’s goals:
As an external user:
* I want to be able to login or register for an account on the website, so that I can access my profile and add reviews.

* I want to be able to upload a book (which does not already exist) to the website, so that I can then review it.

* I want to be able to add a review for a book and give it a thumbs up or thumbs down, so that other users can quickly see what I thought about it.

* I want to be able to edit and delete books and reviews I have added, in case I have made a mistake.

* I want to be able to search for a book by name of by author, so that I can view it's rating. 

* I want to be able to search the database by genre, so that I can find a suitable book.


#### Site Owner Goals:
As the website owner:
* I want to be able to manage the book genres so that this does not become disorganised.

* I want to add an affiliate link to each book so that I can potentially make money off each book.

* I do not want to allow duplicate book titles to be published, this would lead to a bad customer experience.
 
* I only want registerd users to be able to add reviews and books, for monitoring reasons.

* I want to be able edit and delete all content created on the website, for monitoring reasons.

### Project Scope
Functional and content requirments were examined to define what was in and what was out of scope.
For functional requirements, the problem was examined to find a best-fit solution.
For content requirements, the following were considered: What type of content would fulfil the need 
(image, video, text, mixed) and whether or not adequate resources were available to produce the content.

In scope (features & content)

* user login and account registration, only with this can books and reviews be added.

* An admin account for the website owener, this allows the user to edit & delete all content. The user can also manage the book genres.

* A search bar, where users can search for a book by title or author name.

* A search by book genre functionality. 

* Full CRUD functionality for users when dealing with the content they have created.

* Content will be mostly text and imagery, this data is data-focused with less emphasis on front-end development.

* A link will be added to each new book uploaded. This will demonstrate how the website owner could profit from book sales.

Out of scope (features & content)

* A star stating out of 5 for books. The user will only be able to upvote or downvote a book.

* A sophisticated recommendation algorithm, based on books upvoted by user.  

* A customised dashboard for users. The user will not be shown on their profile: recommendations or past reviews.

* Video banners, striking imagery & dynamic front-end development. 

### Wireframes
All wireframes were created using the software [Balsamiq](https://balsamiq.com/). 
Layouts were created following research on the five planes of UX, and before coding.\
\
<strong>
Please note, the final website layout contains slight variations to the original wireframes.
Each of the following files contain wireframes for desktop, tablet, and mobile devices.
</strong>
 
Users - not admin
* [Home](assets/images/readmeFiles/wireframes/home.png)
* [Login](assets/images/readmeFiles/wireframes/login.png)
* [Register](assets/images/readmeFiles/wireframes/register.png)
* [Profile](assets/images/readmeFiles/wireframes/profile.png)
* [Add a book](assets/images/readmeFiles/wireframes/addABook.png)
* [Book page](assets/images/readmeFiles/wireframes/bookPage.png)

User - admin only
* [Manage categories](assets/images/readmeFiles/wireframes/manageGenresAdmin.png)

### Design
The website structure was designed to be consistent, predictable, learnable, visable and provide user feedback.
A user journey was created to aid stucture design.

![user journey](assets/images/readmeFiles/userjourney.jpg) 


#### Typography
All fonts used are from [Google Fonts](https://fonts.google.com/). 

Fonts used include:
* [Lato](https://fonts.google.com/specimen/Lato?query=lato)
* [Raleway](https://fonts.google.com/specimen/Raleway?query=raleway)

#### Colour Scheme
A pink and blue colour palette was used in this design. Although contrasting, pink is associated with romance and lightness and blue creates a feeling of calmness. Used together, these colours create a positive mood.

The following colour palette was used for inspiration:
![colour palette](assets/images/readmeFiles/colorpal.jpg)


#### Design justifications
* 

--------------------------------------------------------------------------------------------

## Features

### Existing Features 

#### Elements on all pages

* **NavBar**
    - The navigation features The Book bar logo in the top left corner in desktop view. This switches to a center position on smaller screen sizes.

    - '''if 'user' in session''' is used by Python to check the logged-in status of the user, before allowing access to the page. This information is then passed to the jinja template.

    To determine which links are shown to the user, the Flask session object is used.
    Below are the lists of links shown for each user status.

    - For non admin users who **are not** logged in, the following links are viewable:
    1. Home 
    2. Login
    3. Register

    - For non admin users who **are** logged in, the following links are viewable:
    1. Home
    2. Profile
    3. Add a Book
    4. Logout

    - For admin users who **are** logged in, the following links are viewable:
    1. Home
    2. Profile
    3. Add a Book
    4. Manage Genres
    4. Logout


* **Footer**
    - The footer includes:
      - Copyright formation with a Github link
      - Social media links

#### Homepage

* **Search bar**
    - The user is able to search by author or book name
    - To search the entire database, a sort by function is available. The user can sort: 
      1. A-Z
      2. Z-A
      3. New-Old

    - Once a user makes a serach, the following occurs:

    - No results found:
      - No book cars are returned
      - The 'Sort by' button disapears
      - A no results message is displayed
      - A 'Reset' button is displayed, which redirects the user back to the homepage

    - Results found:
    - The matching book cards are returned
    - The 'Sort by' button disapears
    - A 'Reset' button is displayed, which redirects the user back to the homepage

* **Pagination**
    - Pagination is present on all three versions of the homepage. 
    - These include: Sorted by
      1. A-Z
      2. Z-A
      3. New-Old

    - On each page, 12 book cards are displayed 
    - This allows for faster page-load time and a better user experience

* **Book cards**
    - The book cards feature the book image, an average star rating, the book name, author and a genre icon.
    - The average review rating is updated once a review is uploaded or edited.
    - All card information is updated once a book is uploaded or edited.
    - The cards are styled with a dark-mode theme for easy viewing.

#### Bookpage
* **Book section**
  - The book image and book data are displayed in the first section
  - The book data section contains the following:
    * Book title
    * Average star rating
    * 'Buy Now' URL
    * Author
    * Description

  - Only if a **user** or **Admin** is logged in, the 'Edit' button will show. 


* **Posted Reviews section**
  - Each review posted is displayed on a card. The following are included:
    1. Review title
    2. Summary
    3. Review author
    4. Date posted
    5. Star rating

  - If a user is either **'Admin'** or the **review author** and they are logged in, the **edit** button is shown.


* **Add a review section**
- The 'Add a Review' form is only accessible to users who are **logged in**
  - if a user is **not logged in**, a message is displayed stating that they must log in to add a review.

- A user can only review each book, one time. This is noted on the review form. If a user tries to add a second review, they will also be notified
- The form contains the following fields
  1. Title
  2. Summary
  3. Select a star rating

- Upon saving, the average star rating value is also updated through a python function upon rending the bookpage template.


#### Edit book page
- The edit book page for each book is only accessible to logged in users. The user must be either the creater of the book or 'admin'.
- Three pathways are possible on this page: 
  - Save
  - Cancel (go back)
  - Delete
- The 'Save' option updates the book document with the users' input in the form. All of the following fields can be edited and saved:
  - Book Genre
  - Book Title
  - Author
  - Image URL
  - Blurb
  - Buy Now URL
- The cancel button redirects the user back to the bookpage.
- The delete button removes the book document from the collection. on click, a modal apears asking for confirmation of deletion. From here, the user can decide to confirm the deletion or go back to the current page.

- Users who are not logged in or are not the creater or author, will be redirected to an access denied page if entering this page is attempted.

#### Edit review page
- The edit review page for each review is only accessible to logged in users. The user must be either the creater of the review or 'admin'. 
- As the book information may be useful for review editing, this section has been included in the template.
- Three pathways are possible on this page: 
  - Save
  - Cancel (go back)
  - Delete
- The 'Save' option updates the review array object within the book document with the users' input in the form. All of the following fields can be edited and saved:
  - Title
  - Summary
  - Star rating

- Upon saving, the average star rating value is also updated through a python function upon rending the bookpage template. 

- The cancel button redirects the user back to the bookpage

- The delete button removes the review object from the book collection. On click, a modal apears asking for confirmation of deletion. From here, the user can decide to confirm the deletion or go back to the current page.

- Users who are not logged in or are not the creater or author, will be redirected to an access denied page if entering this page is attempted.

#### Login page
- A link to the registration page is displayed for easy access

- If the username exists in db, the password is checked.
  - if the password inputted matches the hashed password, the user is directed to the profile page.
  - If the password inputted does not match the hashed password, an error flash message is displayed and the usr is redirected to the login page

- if the username does not exist in db, an error flash message is displayed and the usr is redirected to the login page

#### Register page
- If the username does not exists in db:
  - A unique hashed password is generated
  - The username and hashed password are inserted as a new document to the users collection
  - The user is redirected to the login page

- if the username exist in db
  - An error flash message is displayed and the user is redirected to the login page

#### Manage genres
- The Manage Genres page is only accessible to the user 'admin', who must be logged in
- Users have the option to 'Add' a genre or manage the existing genres. These are shown on cards

* **Genre cards**
- The genre title & materialise icon is shown on each card, along with an 'Edit button'

#### Profile page
- The profile book page is only accessible to that particular logged in user. Python checks the authentifivation of the user by running if 
''' if username == session["user"]:''''
- Users who are not logged in or are not the creater or author, will be redirected to an access denied page if entering this page is attempted

* **Welcome section**
- The user is adressed by their usrname and is notified of how many days they have been a member of the bookbar

* **Profile card**
- A summary of the users activity is displayed. Two statistics are included:
  - **Books added:** An aggregation operation calcualted the count of books created by the user 
  - **Review:** An aggregation operation calcualted the count of reviews created by the user 
- A quick link to the homepage is provided

* **Books added**
If a user has added books:
- The 4 most recent books added by the user are shown
- This view automatically updates once the user adds a new book

If a user has not added any books:
- A card is dispalyed which notifies the user that the 4 most recent book uploads will appear in this section
- A quick link to the book upload page is added

* **Reviews added**
If a user has added reviews:
- The 4 most recent reviews added by the user are shown
- This view automatically updates once the user adds a new review

If a user has not added any reviews:
- A card is dispalyed which notifies the user that the 4 most recent reviews will appear in this section
- A quick link to the homepage is added

#### 404 page
- The 404 page is returned when a requested page cannot be found. This template incorporates the Book bar website styling and includes a link to the homepage.

#### Access denied page
- The access denied webspage is returned if a user requests a webpage which they do not permission to view. This template incorporates the Book bar website styling and includes a link to the homepage.

### Features Left to Implement
The following are features were not included in this release. These may be developed in the future:

* Email authentication for account registration
  - implement email authentication for users who are registering an account. This would be a requirement.

* Admin role creation
  - Create an 'administrator' role, which would give special permissions to users in this category.
  - Currently there can be only one 'Admin' user, this is the account with the username of 'admin'. Unfortunately, this solution is not scaleable.

* Search bar filters & sort by
  - Attempted to implemented this at the beginning of the project. The plan was to include a fiter for 'category' and a 'sort by' function. After several days, I decided to move on with the project and to come back to it once my knowledge is more advance. 

* Add verification on image, icon and 'Buy now' url:
  - With the current set up, no instant verification is available on working links, images or icons before form submittion. This is true across the add and edit genre and book pages.
  - This would ensure that no errors are made upon upload & would reduce website maintaince work load of the administrator. 

----------------------------

## Technology Used
### Database

* [MongoDB Atlas](https://www.mongodb.com/) - Used as the primary database for storing and retrieving the information in the website

### Languages

* [HTML5](https://www.w3schools.com/html/) - Used for structuring the site pages.

* [CSS](https://www.w3schools.com/css/) - Used for styling the site pages.

* [Javascript](https://www.w3schools.com/js/DEFAULT.asp) - Used to make the website interactive.

* [Python](https://www.python.org/) - Used to create database driven functionalities.

### Libraries

* [jQuery](https://jquery.com/) - Used to make the website interactive.

* [PyMongo](https://pypi.org/project/pymongo/) - Used to make communication between MongoDB and Python.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Used to construct and render pages

* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - used in conjunction with flask to display data from the backend.

* [Google Fonts](https://fonts.google.com/) - Used for typography.

* [Font Awesome](https://fontawesome.com/) - Used for footer Icons.

* [Google Icons](https://fonts.google.com/icons) - Used for all Icons (bar footer icons).

* [LottieFiles](https://lottiefiles.com/) - all free animations are sourced from here.

### Tools

* [Gitpod](https://www.gitpod.io/docs/) - Used as a development environment.

* [PIP](https://pip.pypa.io/en/stable/installing/) - Used for tool installions.

* [Git](https://www.gitpod.io/docs/) - Used to handle version control.

* [Github](https://github.com/) - Used for repository hosting.

* [Github Pages](https://pages.github.com/) - Used for site deployment.

* [Materialize](https://materializecss.com/about.html) - Used to develop the website design system.

* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) - Used to resize and edit images.

* [Favicon.io](https://favicon.io/favicon-converter/) - Used for flavicon creation.

* [Chrome Dev tools](https://developers.google.com/web/tools/chrome-devtools) - Used for monitoring the responsiveness of the website.

* [LamdaTest](https://www.lambdatest.com/) - Used for monitoring the responsiveness of the website.

* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create repsonsive images for different devices.

### Deployment

* [Heroku](https://id.heroku.com/login) - The cloud platform used to deploying the website.
----------------------------
## Testing
All testing documentation is stored in a separate testing file, which can be accessed [here](https://github.com/emmahartedev/The-Book-bar/blob/master/testing.md).

----------------------------

## Deployment
The website was hosted on Github Pages. It was deployed by carrying out the following steps:

1. login into Github.
2. Select the repository from the profile.
3. go to 'settings' in the repository.
4. In 'Github Pages' choose 'Master Branch' as Source and save.

The Live site deployed can be viewed on the following link: 
[TeachFlow](https://emmahartedev.github.io/TeachFlow/)

### Local
To clone this project locally; a Chrome browser and Github account are required. 

The following steps can then be followed:
1. Install the [Gitpod Browser Chrome Extention](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki), restarting the browser after installation.
2. Log into [Gitpod](https://gitpod.io/).
3. Click on the following link to go to the [project repository](https://github.com/emmahartedev/TeachFlow).
4. Click on the green 'Gitpod' button (which is located to the right of the repository) to launch a new workspace.
5. The code can be worked on in this newly launched workspace. 

To clone code within an IDE of your choice:

1. Click on the following link to go to the [project repository](https://github.com/emmahartedev/page).
2. Click 'Code' and in the Clone with HTTPs, copy the provided repository URL. 
3. Open a terminal in your IDE.
4. Change the current working directory to the location you wish to generate the cloned directory.
5. Type ```git clone```, and then paste the URL from step 2. 

```
git clone https://github.com/emmahartedev/ms2-page
```

----------------------------

## Credits 
The following material is not my own. Sources have been listed alongside a description of the content used. 

### Content

### Code
The following websites were used for inspiration and assistance:
*

The following scripts/plugins were used in the project:
* 

The following code has been directly used in this project:

* 

/* CREDIT https://codepen.io/dimitrisraptis96/pen/NWrrRLB*/
body background

https://docs.python.org/3/library/secrets.html
generating passwords

###  Media
The images used on this website were obtained from the following sources:
<strong>
* The image alt attribute is used to describe each image below
</strong>

In README.md:
* Colour palette: [Source](https://www.pinterest.de/pin/490681321896937815/)

In bookpage.html: 
* star [Source](https://www.freepik.com/free-vector/star-rating-with-two-different-backgrounds_1014851.htm#page=1&query=star%20rating&position=2)
user image on profile : https://www.flaticon.com/free-icon/user_747545?term=user&related_id=747545

* lottie file: https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets4.lottiefiles.com%2Fpackages%2Flf20_twYDL9.json

lottie file book: https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets7.lottiefiles.com%2Ftemp%2Flf20_aKAfIn.json

profile - books section boy https://images.pexels.com/photos/3457273/pexels-photo-3457273.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260


### Acknowledgments
* 
