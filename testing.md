## The Book bar - Testing

Main [README.md](https://github.com/emmahartedev/The-Book-bar/blob/master/README.md) file. 

View site on [Heroku](https://the-book-bar.herokuapp.com/).

### Table of Contents

1. [User Story Testing](#user-stories "goto user stories")
    * [Visitor stories](#visitor-stories)
    * [Business stories](#business-stories)
2. [Manual Testing](#manual-testing "goto manual testing")
    * [Desktop testing](#desktop-testing)
    * [Mobile and Tablet testing](#mobile-and-tablet-testing)
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

### Manual testing
Manual testing was carried out on Desktop, tablet and mobile devices to ensure that the site working as expected. Below is an account of the findings.

#### Desktop testing
The following browsers were inlucded in desktop manual testing:
    - Chrome
    - Firefox 
    - Microsoft Edge

**Elements on all pages**
1. Navbar
    - When user is not logged in:
        - Hover on each link, confirm that hover effects are applied
        - Click The Book bar brand logo, confirm navigation to homepage
        - Click register link, confirm navigation to register page
        - Click Login link, confirm navigation to login page
        - Click Login link, confirm that session cookie is active
        - Attempt to access the profile page, add a book page and manage genres page. Confirm redirect to access denied page.

    - When a user is logged in:
        - Click profile link, confirm navigation to profile page
        - Click Add a Book page, confirm navigation to add book page
        - Click logout, confirm redirect to login page and confirm that session cookie is removed

    - When 'admin' is logged in:
        - Click manage genres link, confirm navigation to genres page

2. Footer
    - Hover over each icon, confirm that hover effects are applied
    - Click on copyright icon, confrim navigation to Github profile
    - Click on copyright text, confrim navigation to Github profile
    - Click on facebook icon, confrim navigation to facebook
    - Click on facebook icon, confrim navigation to instagram
    - Click on twitter icon, confrim navigation to twitter

**Homepage**
1. Search bar functionality
    - Search by author first name, confirm correct results are returned
    - Search by author last name, confirm correct results are returned
    - Search by word in book title, confirm correct results are returned
        - When results are returned, click on 'Reset' button. Confirm navigation to homepage
    - Search by false keyword, confirm 'no results found' message and 'Reset' button are displayed
        - Click on 'Reset' button, confirm navigation to homepage

2. Sort by functionality
    - Sort by 'A-Z', confirm that books are ordered correctly
    - Sort by 'Z-A', confirm that books are ordered correctly
    - Sort by 'New-Old', confirm that books are ordered correctly
    - Search by keyword, confirm that 'Sort by' button dissapears
    

3. Pagination
    - Click on all pages in 'New-Old', confirm that books are ordered correctly
    - Click on all pages in 'A-Z', confirm that books are ordered correctly
    - Click on all pages in 'Z-A', confirm that books are ordered correctly
    - Confirm that each page displays 12 book cards 

3. Book cards
    - Confirm a consistent layout in book cards. All contain, a book image (where link has been successful), an average star rating (if review), book title, author, genre icon and read more button
    - Confirm that the average star rating is correctly aligned with mongodb data
    - Confirm that the book title and author are correctly aligned with mongodb data

**Bookpage**
1. Book section

- For users logged out
  - Confirm that the book information is correctly aligned with mongodb data
  - Confirm that the average star rating is correct
    - Where no review has yet been added, confirm that a toolip is added
    
- For users logged in
  - Confirm that the 'Edit' button is not visable (unless the user is the creater)

- For 'admin' user or content creater user
    - confirm that 'Edit' button is present
    - Click buttonm confirm navigation to edit book page

2. Posted Reviews section

- For users logged out
    - If reviews exist, confirm that review cards are visable
    - If no reviews exist, confirm that a placeholder card is displayed

- For users logged in
    - If reviews exist, confirm that review cards are visable
    - If no reviews exist, confirm that a placeholder card is displayed
    - On reviews, confirm that the 'Edit' button is not visable (unless the user is the creater)
    - Confirm that the review information is correctly aligned with mongodb data
    - Confirm that the date is included

- For 'admin' user or content creater user
    - Confirm that the 'Edit' button is present behind the review card

3. Add a review section
- For users logged out
    - Confirm that the review form is not visable
    - Confirm that a link to the login page is provided
    - Click on link, confirm navigation to login page

- For users (all user types) logged in
    - Confirm that the review form is present
    - Submit a review
        - Attempt posting review without Title or Rating, confirm failure
        - Post a review, confirm that the review card appears in the section above. 
        - Post a review, confirm that the average rating updates in the book section
        - Post a second review, confirm that a error message is displayed.

**Edit book page**
- Test access
    - Attempt to access the edit book page url while logged out. Confirm redirect to access denied page.

- Test pathways
  - Input new data in all fields & click 'Save': 
    - Confirm that success message appears
    - Confirm redirect to bookpage
    - Confirm that data on template is aligned with MongoDB data (updated data)

  - Click 'Cancel'
    - Confirm redirect to bookpage.

  - Click 'Delete'
    - Confirm that warning message appears
    - Click 'No'
        - Confirm that modal closes
    - Click 'Yes
        - Confirm that success message appears
        - Confirm redirect to homepage
        - Confirm that book document is removed from MongoDB collection.
        - Confirm that 'Books Added' count on profile page updates
        - Confirm that 'Your Recent Contributions' - 'Books added' book card dissapears

**Edit review page**
- Test access
    - Attempt to access the edit book page url while logged out. Confirm redirect to access denied page.

- Test pathways
  - Input new data in all fields & click 'Save': 
    - Confirm that success message appears
    - Confirm redirect to bookpage
    - Confirm that data on template is aligned with MongoDB data (updated data)
    - Confirm that average star rating in book section updates

  - Click 'Cancel'
    - Confirm redirect to bookpage.

  - Click 'Delete'
    - Confirm that warning message appears

    - Click 'No'
        - Confirm that modal closes

    - Click 'Yes
        - Confirm that success message appears
        - Confirm redirect to bookpage
        - Confirm that review object arrary is removed from MongoDB collection (book & user document).
        - Confirm that 'Reviews Added' count on profile page updates
        - Confirm that 'Your Recent Contributions' - 'Reviews added' review card dissapears

**Login page**
- Incorrect password
    - Confirm error message 'Password and/or Username is incorrect.' appears

- Incorrect username
    - Confirm error message 'Password and/or Username is incorrect.' appears

- incorrect username and password
    - Confirm error message 'Password and/or Username is incorrect.' appears

- Correct username and password
    - Confirm redirect to profile page

**Register page**

- if the username is in use
  - Confirm error message 'This username is already in use. Please choose another.'

- If the username is not in use
  - A unique hashed password is generated
  - The username and hashed password are inserted as a new document to the users collection
  - The user is redirected to the login page

**Manage genres page**

- Design confirmation
    - Confirm that genre cards show both the title and materialise icon

- Test access
    - Attempt to access the edit book page url while logged out. Confirm redirect to access denied page.
    - Confirm that navlink is not visable to non admin users
    - Confirm that navlnk is visable for 'admin' user

- Test pathways
    - Cllick on 'Add' button, confirm redirect to add genre page
    - Click on 'Edit' button on genre card, confirm redirect to specific edit genre page

**Add genre page** 
- Design confirmation
    - Confirm that two fields are present (genre name and materialise icon)

- Test pathways
    - Add data and click 'Save'
        - Confirm success flash image appears
        - Confirm redirect to manage genres page
        - confirm that newly added genre is present as a genre card, showing both the title and name

    - Click 'Cancel'
        - Confirm redirect to manage genres page


**Edit genre page**
- Design confirmation
    - Confirm that two fields are present and pre-populated(genre name and materialise icon)

- Test pathways
    - Edit data and click 'Save'
        - Confirm success flash image appears
        - Confirm redirect to manage genre page
        - confirm that data on genre card is updated and is aligned with MongoDB
        
    - Click 'Cancel'
        - Confirm redirect to manage genres page
    
    - Click 'Delete'
        - Click 'Yes'
            - Confirm that success flash message appears
            - Confirm redirect to manage genres page
            - confirm that genre card has been removed and is aligned with MongoDB

**Profile page**
- Test access
    - Attempt to access a users profile by url while logged out. Confirm redirect to access denied page.
    - Attempt to access a different users profile by url while logged in. Confirm redirect to access denied page.

- Design confirmation
    - Welcome section
        - Confirm that correct username is displayed in welcome message
        - confirm that duration of member in days is correct
    
    - Profile card
        - Confirm that books count number is correct
        - Confirm that reviews count number is correct
        - Hover over 'Search Books' link, confirm hover effect is applied. 
        - Click on 'Search Books' link, Confirm redirect to homepage.

    - Books added section
        - If 'books added' count is zero
            - Confirm that placeholder image and text are present
            - Hover over the card link, confirm that hover effects are applied 

        - If 'books added' count is greater than zero
            - Confirm that the most recent 4 books are displayed

    - Reviews added section
        - If 'Reviews added' count is zero
            - Confirm that placeholder image and text are present
            - Hover over the card link, confirm that hover effects are applied            

        - If 'Reviews added' count is greater than zero
            - Confirm that the most recent 4 reviews are displayed

**404 page**
Test pathway using a false URL (eg https://the-book-bar.herokuapp.com/get_genres/crime)
    - Confirm redirect to 404 page

**Access denied page**
Test pathway using a false URL (eg https://the-book-bar.herokuapp.com/get_genres/crime)
    - Confirm redirect to 404 page

#### Mobile and Tablet testing

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
