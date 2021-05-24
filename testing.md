## The Book bar - Testing

Main [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md) file. 

View site on [Heroku](https://the-book-bar.herokuapp.com/).

### Table of Contents

1. [User Story Testing](#user-story-testing "goto user story testing")
    * [Visitor stories](#Visitor-stories)
    * [Site Owner Goals
2. [Manual Testing](#manual-testing "goto manual testing")
    * [Desktop]()
    * [Mobile and Tablet]()
3. Further Testing 
    * [Browser Compatibility](#browser-compatibility "goto browser compatibility")
    * [Responsiveness](#responsiveness "goto responsiveness")
    * [Code Validation](#code-validation "goto code validation")
    * 
4. [Bugs](#bugs "goto bugs")

### User Stories
The following section re-evaluates the user stories defined in the UX section of [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md).

#### Visitor stories:
**As an external user**:

1. I want to be able to search for a book by book title or author, so that I can find out more information. 
    - A search index has been created
        - This allows for users to search by both book title and author
    - If a search returns results
        - The book cards are returned
        - The book title and author are displayed on each bookcard, for easy readability
        - By clicking on a card the user can visit the bookpage
    - If no results are returned
        - The user if notified of the keywork they used and a 'no results' message is displayed
        - A reset button is displayed

2. I want to be able to search the database by genre, so that I can find a suitable book.
    - This feature has not been developed in this release
        - This is noted in [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md) under the Features Left to Implement.
        - With a more advanced understand of this concept, this feature will be developed at a later stage.

3. I want to be able to sort the entire database, so that I can view all books.
    - A 'Sort by' button is displayed on the homepage
    - The user can sort the collection by:
        - A-Z
        - Z-A
        - New-Old
    - The 'Sort by' feature only sorts the entire collection
        - Once a user searches by keyword, the 'Sort by' button disappears
        - As the database grows, it may become a requirement to add 'Sort by' to the results
        - This development will be considered if the requirment arises

4. I want to be able to login or register for an account on the website, so that I can access my profile, upload books add reviews.
    - Register and login pages are clearly located on the navbar
        - A link to the login page is located on the regsiter page for users who have mistakenly navigated here
        - A link to the register page is located on the login page for users who have mistakenly navigated here

    - Register page contains clear messages
        - Benefits of registering are displayed on the first line
        - A link to the login page is included
        - Username and password criteria are listed

    - Register page contains clear feedback messages for form submission
        - Error message shown if username is aleardy in use
        - Error message shown if password is too short
        - Success message shown if registration is successful

    - Login page contains clear messages
        - A link to the register page is displayed
    
    - Login page contains clear feedback messages for form submission
        - Error message is password or username is incorrect
        - Welcome message dispalyed on profile page is registration is successful


5. I want to see a snapshot of activity on my profile, so that I can quicky see my recent contributions.

    - a Welcome message is displayed:
        - The username is addressed on this page
        - The duration of time the user has been a member is included

    - A snapshort of the user's activity is displayed. This icludes:
        - The total number of books the user has added
        - The total number of reviews the user has added
        - A quick link to the homepage
    
    - A 'Recent Contributions' section is displayed. This includes:
        - The four most recent books added by the user.
            - To quickly navigate to the edit book page, the user can click on the 'Edit Book' button. 
            - if a user has not added any books yet, a placeholder image and some text is displayed
        - The four most recent reviews added by the user.
            - To quickly navigate to edit review page, the user can click on the 'Read More' button. 
            - if a user has not added any reviews yet, a placeholder image and some text is displayed

6. I want to be able to upload a book to the website, so that I and others can then review it.
    - 'Add a Book' navlink is clearly visable on navbar
    - The user can enter the following information on a book:
        - Book title
        - Author
        - An image URL
        - Blurb
        - Buy now url

7. I want to be able to make changes or delete a book that I have uploaded, in case an error has been made.
    - An 'Edit' button is displayed within the bookpage if the user has uploaded the book
    - Within the edit page, the user has the option to delete the book
    - Clicking delete activates a modal which asks for confirmation before deletion

8. I want to be able to review and rate any book on the website, so that other users can quickly see what I thought about it.
    - Any logged in, registered user can add a review to a book
    - The review card cantains the following fields:
        - Title
        - Summary
        - Star rating
    - An average star rating is updated with every review upload. With this aggregation, the user can quickly see what others thought of the book.

9. I want to be able to edit and delete reviews that I have added, in case an error has been made.
    - An 'Edit' button is displayed behind a review card for the user has uploaded the review
    - Within the edit page, the user has the option to delete the review
    - Clicking delete activates a modal which asks for confirmation before deletion

10. I want to know the average star rating for each books, as this will help me choose my next read.
    - An average star rating is displayed for a book if at least one review has been posted
    - This is visable on both the book cards shown on the homepage and profile page, as well as the book page itself
    - The average star rating is updated each time a review is uploaded, editer or deleted

#### Business stories:
**As the website owner**:

1. I want to be able to add new book genres on the website, so that users can select these when uploading a book.
    - A 'Manage Genres' page is accessible only for the 'admin' user
    - The link is clearly located on the navbar
    - within this page, the 'admin' can add, edit, view and delete genres

2. I want to be able to edit and delete book genres, in case an error has been made.
    - On the 'Manage Genres' page, the user is presented with a list of the current genres. The genre title and icon are displayed.
    - by clicking 'Edit' on a genre, the user navigates to the edit genre page. Here the user has the option to save changes, go back or delete the genre
    - Clicking delete activates a modal which asks for confirmation before deletion

3. I want to see a snapshot of activity on my profile, so that I can quicky see my recent contributions.

    - a Welcome message is displayed:
        - The username is addressed on this page
        - The duration of time the user has been a member is included

    - A snapshort of the user's activity is displayed. This icludes:
        - The total number of books the user has added
        - The total number of reviews the user has added
        - A quick link to the homepage
    
    - A 'Recent Contributions' section is displayed. This includes:
        - The four most recent books added by the user.
            - To quickly navigate to the edit book page, the user can click on the 'Edit Book' button. 
            - if a user has not added any books yet, a placeholder image and some text is displayed
        - The four most recent reviews added by the user.
            - To quickly navigate to edit review page, the user can click on the 'Read More' button. 
            - if a user has not added any reviews yet, a placeholder image and some text is displayed

4. I want to add an 'Buy now' link to each book so that I can potentially make money off click through sales.
    - A 'Buy now' input field is provided as part of the upload book form submission
    - If blank, the 'Buy now' link will not appear on the bookpage
    - If provided, the 'Buy now' link will be published on the bookpage
    - Verification of the link as not been developed in this release
        - This is noted in [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md) under the Features Left to Implement.
        - With a more advanced understand of this concept, this feature will be developed at a later stage.

5. I do not want to allow duplicate book titles to be published, this would lead to a bad customer experience.

- This feature has not been developed in this release
        - This is noted in [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md) under the Features Left to Implement.
        - With a more advanced understand of this concept, this feature will be developed at a later stage.
 
6. I only want registered users (logged in) to be able to add reviews and books, for monitoring reasons.
    - Access to the book and review upload links has been restricted
    - If a logged out user attempts to access these pages, they will be redirected to an access denied page
    - On the access denied page, a link to the homepage is displayed to direct users back to the site

7. I want to be able to edit and delete all content created on the website, for monitoring reasons.
    - An 'Edit' button is displayed behind every review card and bookpage for the 'admin' user
    - Within the edit page, the user has the option to delete the review or book
    - Clicking delete activates a modal which asks for confirmation before deletion
    - The 'admin' user has complete control over editing and deleting all content on the site.
    - The 'admin' user also has access to add both books and reviews.


### Browser Compatibility
[LamdaTest](https://www.lambdatest.com/) was used to test the website on the following browsers:

* Google Chrome
* Firefox
* Microsoft Edge
* Safari 
* Opera


### Responsiveness
The website's responsiveness was tested using [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools).
CSS Media Queries were written as required to improve appearances. 

The devices (and screen widths) tested with include: 
* iPhone 5/SE (320px)
* iPhone 6/7/8 (375px)
* iPhone 6/7/8 Plus (414px)
* iPad (768px)
* iPad Pro (1024px)
* Laptop (1200px)
* Desktop (1920px)
    
In addition to this, [Lighthouse](https://developers.google.com/web/tools/lighthouse) was run in Chrome Dev Tools regularly throughout developement, to generate reports on the quality of the website.
Primarily mobile reports were focused upon. 

The following report was generated before changes were made:

![Lighthouse Mobile Report ](assets/images/readme_files/lighthouse-before.png)


### Code Validation
#### HTML 
* All HTML code was checked using [The W3C Markup Validation Service](https://validator.w3.org/).
* 

#### CSS
* All CSS code was checked using [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).
* 

#### Javascript
* All Javascript code was checked using [JSHint](https://jshint.com/). 
* 

#### General 
   * All javascript variables were logged to the console in Testing.

* feature
    * tested how


Test logout by checking session cookie in application tab on dev tools
#### index.html

* feature
    * how tested
    
### Bugs 
delay in modal pop up solved by stack overflow
https://stackoverflow.com/questions/42430062/materialize-model-not-working

overflow:hidden getting added to the page - added script to css


#### Solved
1. <strong>name</strong>
Issue
resolution 

remove top:-9999px from star rating, stops page jumping to the top.

#### Unsolved
1. <strong>name</strong>
Issue
resolution 
----------------------------
