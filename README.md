# Foodie Favourites

[Click here to view the live site.](https://foodie-favourites.onrender.com/)

![Am I Responsive Image](assets/readme-images/am-i-responsive.JPG)

## Contents

- [Overview](#overview)
- [User Experience (UX)](#user-experience)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
    - [Existing Features](#existing-features)
- [Testing](#testing)
    - [User Stories Testing](#user-stories-testing)
    - [Validator Testing](#validator-testing)
    - [Performance Testing](#performance-testing)
    - [Device and Browser Compatibility Testing](#device-and-browser-compatibility-testing)
    - [Bugs](#bugs)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Online Resources](#online-resources)
- [Credits](#credits)
    - [Code](#code)
    - [Media](#media)

## Overview

Foodie Favourites is a free to use website where UK based food lovers - especially those who enjoy eating out - can share and discover their favourite restaurants and dishes. Once registered, users can create posts of their favourite restaurants, and can comment and favourite other peoples' restaurant posts. Registered users will have their own profile page where they can share some information about themselves if they so desire. The profile page also shows any restaurant posts they have made, and any restaurants they have favourited.

## User Experience

### Strategy

This website is aimed at people who would like to share their favourite restaurants with others, and/or people who would like to discover some new restaurants. Therefore the age range aimed for is quite wide, essentially anyone who is able to enjoy a nice meal out.

In a very broad sense, there are 3 types of users the website will have: site admins, registered users and non-registered users. For this reason, the epics and user stories have been categorised in this way.

#### Epics and User Stories

There are 3 epics, each of which have been split up into multiple user stories. All of which are outlined below.

More detail about the user stories including acceptance criteria and tasks associated with each of them can be found in the [issues](https://github.com/AshFoster/foodie-favourites/issues) section of the GitHub repository.

  - __Epic 1: Admin Setup__
      - As a Site Admin I can create, read, update and delete restaurant posts so that I can manage the site's content
      - As a Site Admin I can approve or disapprove comments on restaurant posts so that I can filter out any questionable comments
      - As a Site Admin I can be notified when a comment needs to be approved so that I do not need to keep checking the admin site for anything to be approved
      - As a Site Admin I can be notified when a user has submitted the contact form so that I do not need to keep checking the admin site for any form submissions to read

  - __Epic 2: All User Functionality__
      - As a Site User I can view a list of restaurant posts so that I can select one to view
      - As a Site User I can view a paginated list of restaurant posts so that I can easily select a post to view
      - As a Site User I can filter the available restaurant posts so that I can see posts that are more specified to my needs
      - As a Site User I can type keywords into a search bar so that I can find restaurant posts with titles that contain the keywords that I typed
      - As a Site User I can click on a restaurant post so that I can view the post in its entirety
      - As a Site User I can view the number of times a restaurant post has been favourited so that I can see which are the most popular
      - As a Site User I can view comments on an individual restaurant post so that I can see what people have had to say about it
      - As a Site User I can view the author's favourite dishes on each restaurant post so that I can see which dishes the author of each restaurant post recommends
      - As a Site User I can view registered users' profiles so that I can learn more about them and see which restaurant posts they've favourited and/or which they've posted.
      - As a Site User I can fill in a contact form so that I can get in contact with the site owners to ask any questions I might have
      - As a Site User I can register for an account so that I can contribute to the site

  - __Epic 3: Registered User Functionality__
      - As a Registered Site User I can add my own restaurant posts so that I can share my favourites restaurants and dishes with other users
      - As a Registered Site User I can update restaurant posts that I've previously made so that I can amend anything that might be incorrect or add dishes
      - As a Registered Site User I can delete restaurant posts that I've previously made so that I can remove any restaurant posts that I no longer wish to share
      - As a Registered Site User I can leave comments on restaurant posts so that I can give my opinion on posts
      - As a Registered Site User I can favourite or unfavourite restaurant posts so that I can keep track of restaurant posts that I like
      - As a Registered Site User I can reset my password so that I can still gain access to my account if I've forgotten the current one
      - As a Registered Site User I can view my own profile so that I can see what restaurant posts I've posted or favourited
      - As a Registered Site User I can edit my own profile so that I can choose what to share about myself with other users
      - As a Registered Site User I can update my registered email address or update my password so that I can use a new email address with my account, strengthen my password or use a more memorable password

### Scope

All of the user stories outlined above are feasible for the first release of the website. Some further features that could be implemented later on include:

- Allowing users to suggest their favourite dishes on other user's restaurant posts
- Adding an autocomplete feature to the location selection when adding a new restaurant
- Giving the user the ability to explicitly request new cuisines (this can currently be done using the contact us page)

I don't feel that having these features will impact the user experience too much, so felt it was fine to exclude them for the first release. Each of which would need to be thought about carefully in how they would be implemented to not overcomplicate the website too much.

### Structure

The structure of the website is aimed to be as simple as possible whilst showing all the necessary information. The main parts of the site will be accessible from the navbar, with any other parts easily accessible from the relevant pages. The main parts of the site included within the navbar are as follows:

- Home
- Restaurants (where all restaurant posts can be found)
- Contact Us
- Sign In
- Register
- Profile (registered users only)
- Sign Out (registered users only)

Other parts of the site not included in the navbar are as follows:

- Restaurant detail (accessed from restaurants page and users' profile pages)
- Add Restaurant (registered users only - accessed from home page and restaurant page)
- Edit Restaurant (registered users only - accessed from restaurant detail page - only post's author can access)
- Delete Restaurant (registered users only - accessed from edit restaurant page - only post's author can access)
- Other users' profiles - accessed by clicking on the author's username on restaurant posts or comments
- Edit profile (registered users only - accessed from profile page - users can only edit their own profiles)
- Update Email (registered users only - accessed from profile page - users can only update their own email)
- Update Password (registered users only - accessed from profile page - users can only update their own password)
- Reset Password (registered users only - accessed from sign in page - users can only reset their own password)

The site has been split up into 3 apps: restaurants, accounts and contact. The restaurants app handles everything to do with displaying, adding, updating, deleting and interacting with restaurant posts. The accounts app handles everything to do with user accounts and profiles, and the contact app handles the contact form.

The site map can be seen in the following image:

![Site Map](assets/readme-images/site-map.png)

#### Data Models

##### Restaurants App Models

The restaurants app has 4 database tables associated with it: Restaurant, Cuisine, Comment and Dish.

The Restaurant table has relationships with all of the other tables: Cuisine being a many to many relationship, Comment being a one to many relationship, and Dish also being a one to many relationship (many comments and many dishes can be associated with one restaurant). Each table has some of its own other fields, too. The restaurant table also has a one to many relationship and a many to many relationship with Django's built-in User model: the author field and the favourited field respectively.

All of which can be seen in the image below.

![Restaurant Models](assets/readme-images/restaurant-models.png)

##### Accounts App Models

The accounts app has a single database table associated with it: Profile. This has a one to one relationship with Django's built-in User model and adds some more fields to be used on the user's profiles. The image below shows how this table is structured.

![Profile Model](assets/readme-images/profile-model.png)

### Skeleton

#### Wireframes

Wireframes were created for mobiles, tablets, and desktops using [Balsamiq](https://balsamiq.com/). The actual pages do differ slightly from the original wireframes.

Here are links to each of them:

- [Desktop - Home](assets/wireframes/home-desktop.png)
- [Tablet - Home](assets/wireframes/home-tablet.png)
- [Mobile - Home](assets/wireframes/home-mobile.png)
- [Desktop - Restaurants](assets/wireframes/restaurants-desktop.png)
- [Tablet - Restaurants](assets/wireframes/restaurants-tablet.png)
- [Mobile - Restaurants](assets/wireframes/restaurants-mobile.png)
- [Desktop - Contact](assets/wireframes/contact-desktop.png)
- [Tablet - Contact](assets/wireframes/contact-tablet.png)
- [Mobile - Contact](assets/wireframes/contact-mobile.png)
- [Desktop - Sign In](assets/wireframes/sign-in-desktop.png)
- [Tablet - Sign In](assets/wireframes/sign-in-tablet.png)
- [Mobile - Sign In](assets/wireframes/sign-in-mobile.png)
- [Desktop - Register](assets/wireframes/register-desktop.png)
- [Tablet - Register](assets/wireframes/register-tablet.png)
- [Mobile - Register](assets/wireframes/register-mobile.png)
- [Desktop - Restaurant Detail](assets/wireframes/restaurant-detail-desktop.png)
- [Tablet - Restaurant Detail](assets/wireframes/restaurant-detail-tablet.png)
- [Mobile - Restaurant Detail](assets/wireframes/restaurant-detail-mobile.png)
- [Desktop - Add Restaurant](assets/wireframes/add-restaurant-desktop.png)
- [Tablet - Add Restaurant](assets/wireframes/add-restaurant-tablet.png)
- [Mobile - Add Restaurant](assets/wireframes/add-restaurant-mobile.png)
- [Desktop - Profile](assets/wireframes/profile-desktop.png)
- [Tablet - Profile](assets/wireframes/profile-tablet.png)
- [Mobile - Profile](assets/wireframes/profile-mobile.png)

### Surface

#### Imagery

Images are an important part of the look and feel of the website. Each page has a different background image, most of which are of different restaurant settings.

#### Colour Scheme

The colour scheme of the site is very simple, with the main colours being shades of black, grey, and white.

![Website's Colours](assets/readme-images/colour-scheme.JPG)

The idea was to keep the colours themselves simple and to use the different background images on each page to provide more interesting colours. Using shades of black, grey and white meant that most images could be used without clashing.

#### Typography

For the typography choices, [Google Fonts](https://fonts.google.com/?sort=popularity) was used, sorted by popularity to give an idea of some fonts that are likely to work well across many websites.

The ones that stood out and seemed most suited to the project were chosen. They are as follows:

Roboto (italic) - This is used for the Foodie Favourites logo shown on the navbar.

Oswald - This is used for all navbar links. 

Lato - This is used for all other text throughout the site.

Each of them is of the font category Sans Serif which is the font used as a fallback if for any reason the specified font isn't available.

## Features

### Existing Features

- __Navbar__

  ![Navbar](assets/readme-images/navbar.JPG)

  - The navbar has the website brand on the left-hand side which is also a link to the homepage. It also has links to all the major sections of the website.
  - When on each of the major sections of the site the relevant link is bold and brighter to show the user which part of the site they're currently viewing.
  - When signed in, the section on the right-hand side showing Sign In and Register changes to Profile and Sign Out respectively.
  - The menu items on the right are displayed as a hamburger item on smaller screens which when pressed opens up a menu with all the links below.

- __Footer__

  ![Footer](assets/readme-images/footer.JPG)

  - The footer is split up into 2 main sections. One shows a small paragraph describing what Foodie Favourites is all about, and the other shows links to various social platforms.
  - There is also a smaller section that simply shows copyright-related information.

- __Welcome Message__

  ![Welcome Message](assets/readme-images/welcome-message.JPG)

  - Here, the user is welcomed to the site with a brief description of what the site is aimed to do.
  - If the user is signed in then the welcome message displays their username.
  - On the right-hand side the user is invited to sign in or register via some links.
  - If the user is already signed in the message on the right invites them to have a look at the current list of restaurants instead.

- __Recently Added Restaurants__

  ![Recently Added Restaurants](assets/readme-images/recently-added-restaurants.JPG)

  - This section shows the 2 most recently added restaurants which the user can click on the be taken to the relevant restaurant's detail page.
  - There is also a link below these items which takes the user to the full list of restaurants.
  - If the user is signed in then there is also an 'Add Restaurant' button that takes the user to the add restaurant page.

- __Sign In__

  ![Sign In Page](assets/readme-images/sign-in.JPG)

  - The Sign In page asks the user for their username and password for them to sign in.
  - There is a 'Sign In' button below the form which submits the form.
  - If the username or password is incorrect the user is told.
  - All fields need to be completed and if any are not the user will be asked to complete the empty fields.
  - There is also a 'forgot password' link that takes the user to the 'Reset Password' page.
  - There is a 'Register' button that takes the user to the 'Register' page.

- __Register__

   ![Register Page](assets/readme-images/register.JPG)

  - The Register page asks the user for an email address, a username, a password and to repeat the password.
  - There is a 'Register' button below the form which submits the form.
  - If the email address or username already exists the user is told and must use another email address and/or password.
  - If the repeated password does not match the first one the user is told and will need to type them in again.
  - All fields need to be completed and if any are not the user will be asked to complete the empty fields.
  - There is a 'Sign In' button which takes the user to the 'Sign In' page.

- __Restaurants List__

  ![Restaurants List](assets/readme-images/restaurant-list.JPG)

  - The restaurants list displays all of the current restaurant posts.
  - It is paginated to show 3 restaurants per page, with pagination buttons for each page at the bottom which take the user to the relevant page when clicked.
  - The pagination buttons are currently displayed nicely on all devices. Though, when the number of restaurant pages increases to more than 7 or 8 they will not display as nicely on smaller screens. This will need to be rectified when that happens. The number of restaurants per page could be increased, or how the pagination is displayed could be changed. For now, though, it's fine.
  - Each restaurant post shows the name, author, cuisine, location, number of times favourited, and the author's rating (from 1 to 5) of the restaurant. 
  - There is a search bar above the restaurant posts which allows the user to search for restaurants with titles that contain their search criteria.
  - If the user is logged in, there is an 'Add Restaurant' button above the Restaurants List section which takes the user to the add restaurant page.
  - If the user is signed in and has favourited a restaurant then the little heart icon will be filled in rather than outlined.
  - The user can click on the image or the title to be taken to the detail page of that restaurant.

- __Filters__

  ![Filters](assets/readme-images/filters.JPG)

  - The filters section displays lists of all the different cuisines and locations of all the current restaurants.
  - Next to each cuisine and location a number is displayed on the right-hand side showing how many restaurants match that particular cuisine or location.
  - When the user clicks on one of the cuisines or locations the restaurant list is immediately filtered and reloaded based on what has been clicked.
  - When filtered on a cuisine, the location list is updated to show only locations that match the selected cuisine and vice versa.
  - Both cuisine and location lists are also updated appropriately when the user uses the search bar above the restaurants list described above.
  - When viewing on smaller screens the filters section is hidden and a 'Filters' button is shown instead. When clicked, a modal containing the filters section is shown.

- __Contact Form__

  ![Contact Form](assets/readme-images/contact-form.JPG)

  - The contact form allows the user to contact the admin of the site.
  - It has 3 required fields, name, email and message. If any of them have been missed on submission the user is told.
  - If the user is signed in then the name and email fields will already be completed using information from their account.

- __Profile__

  ![Profile](assets/readme-images/profile.JPG)

  - Each registered user is given a profile page that can be viewed by registered and non-registered users.
  - Users can view other users' profiles by clicking on the user's name that is displayed on restaurant posts or comments that that user has made.
  - Registered users can view their own profile by clicking on the profile link in the navbar.
  - On all profiles, there is a 'Profile Info' section which has 5 fields, name, location, favourite cuisine, bio and image. The name field is automatically completed using the user's username but can be updated by the user to their real name if they wish to. All other fields except image are blank until the user decides to fill them in, the image field having a default image until one has been added.
  - There is also a 'Restaurants Posted' section that displays all of the restaurants that the user has posted. Within this section, a 'Show Favourites' button is shown which changes the 'Restaurants Posted' section to 'Favourited Posts' which shows all the posts which the user has favourited. When viewing the 'Favourited Posts' section the button now shows 'Show Restaurants Posted' which reverts to show the 'Restaurants Posted' section.
  - When users are viewing their own profile there are some extra features. There is an 'edit' button within the 'Profile Info' section which takes the user to a page where they can edit the information that is shown on their profile. There are also 'Update Email' and 'Update Password' buttons which take the user the different pages where they can change the email address registered with their account, or change their current password.

- __Restaurant Detail__

  ![Restaurant Detail](assets/readme-images/restaurant-detail.JPG)

  - Each restaurant post has its own detail page which shows all of the uploaded information about it.
  - The detail page is split up into various sections. An optional image that has a default fallback if no image is chosen. A general information area which shows the name, author and date added, the cuisine, and the location. Then the main description of the restaurant given by the author. Below that is a section displaying the author's favourite dishes from the restaurant. Then, how many times the post has been favourited is shown, along with the rating (out of 5 stars) that the author has given it.
  - There is also a 'Comments' section that allows signed-in users to comment on the post. Comments will need admin approval before being posted so when a user posts a comment an email is sent to the admin. The user is shown a message making them aware of this.
  - Signed in users can also click on the little heart icon next to times favourited to favourite it themselves. Before they have favourited it the icon is the outline of a heart, but once they have favourited it the heart is filled in. They can also unfavourite posts, reverting the heart icon to only an outline.
  - Users cannot favourite their own posts.
  - When users are viewing their own posts, an 'edit' link is displayed near the top of the general information area. This takes them to the edit restaurant page where they can make changes to the post.

- __Add Restaurant__

  ![Add Restaurant](assets/readme-images/add-restaurant.JPG)

  - Registered users can access the add restaurant page where they can add their own restaurant posts.
  - There are 8 fields to complete, 7 of which are required. The image field is not required as a default image is used if no image is uploaded.
  - The 7 required fields are name, description, rating, location, county, cuisine, and favourite dishes.
  - The name, description and location field simply require the user to type their values.
  - The county field is chosen from a large list of all the counties in the UK. This is to aid with filtering by location on the restaurants page.
  - The cuisine field allows the users to select one or multiple items from a list of cuisines. The user cannot add cuisines as the cuisine filter on the restaurants page needs consistency in cuisine names to make sure it appears correctly and that the list does not get too long. Users have the option of selecting 'Other' if none of the listed cuisines matches the cuisine required.
  - The favourite dishes section allows the user to add multiple favourite dishes. They must type one dish at a time and then hit enter or click the 'Add Dish' button which will add each dish to a list below the button.
  - Once everything has been completed the user can click 'Submit Restaurant', and if everything is ok, they will be taken to the detail page of the restaurant they just added.
  - The user will be told if any of the fields are incomplete.
  - When a user chooses to 'edit' one of their posts they will be taken to the add restaurant page, though then the heading will say 'Edit Restaurant' instead of 'Add Restaurant', and there will also be a 'delete' link available which will take the user to another page where they can confirm if they would like to delete the post.

- __Update Email__

  ![Update Email](assets/readme-images/update-email.JPG)

  - This page allows the user to add email addresses to their account, change their primary email address, remove email addresses and to re-send a verification email regarding one of their email addresses.
  - If there is only one email address associated with their account then this will be the primary address. The email used when registering will automatically be assigned as primary, though no confirmation is needed on registration. If the user decides they would like to change their primary email address they will need to add it to their account, then verify it via email, and then set it as the primary email address. They then have the option of leaving the old email address on the account or removing it.
  - Only non-primary email addresses can be removed from an account.

- __Change Password__

  ![Change Password](assets/readme-images/change-password.JPG)

  - This page allows the user to change their password. All they need to do is type in their current password, and then their new password twice.
  - The current password must match the current password, and the repeated new password must match the first new password. If any of these do not match then the user is told accordingly.
  - There is also a 'forgot password' link that takes the user to the 'Reset Password' page.

- __Reset Password__

  ![Reset Password](assets/readme-images/reset-password.JPG)

  - The Reset Password page allows users to reset their password in the case that they have forgotten their current password.
  - The user must enter the email address associated with their account and click 'Reset My Password'. An email will then be sent to their email with a link that takes them to a page where they can reset their password.
  - If the user enters an email address that is not associated with an account then the user is made aware of this.
  - There is also a 'contact us' link that takes the user to the 'Contact Us' page that they can use if they are having trouble resetting their password.

- __Sign Out__

  ![Sign Out](assets/readme-images/sign-out.JPG)

  - When the user clicks on the 'Sign Out' link in the navbar they are taken to this page which simply asks them to confirm that they would like to sign out.
  - When they do sign out they are directed back to the home page.


## Testing

### User Stories Testing

#### Epic 1: Admin Setup

  - __As a Site Admin I can create, read, update and delete restaurant posts so that I can manage the site's content__

    - When signed in as an admin user and viewing the admin panel, each of the models is shown on the left-hand side. Each of them can be clicked to take the user to a list of all objects of that particular model. From here, more objects can be added by clicking the 'Add' button. The user is then taken to a page where they can fill in a form and then add the object to the database. Any of these objects can be updated by clicking on them and then editing the details on the next page. They can all be deleted too.
    - The models available to add, update, or delete are Restaurant, Cuisine, Comment, Dish and Profile. Along with Django's built-in User model.
    - Any Restaurant objects created via the admin panel can be seen on the front end of the website.

  - __As a Site Admin I can approve or disapprove comments on restaurant posts so that I can filter out any questionable comments__
    
    - From the admin panel, admin users can choose to view a list of all comment objects by clicking on the 'Comments' link on the left-hand side of the page.
    - When viewing the list the user can see which comments have been approved and which ones have not by looking in the 'APPROVED' column.
    - Users can then select one or multiple comments to approve via checkboxes, and then select 'Approve Comments' from the drop-down list above.
    - All approved comments can be seen on the relevant restaurant's detail page.

  - __As a Site Admin I can be notified when a comment needs to be approved so that I do not need to keep checking the admin site for anything to be approved__

    - When a registered user leaves a comment on one of the restaurant posts an email is sent to the admin's email address notifying them that a comment has been posted and needs approval.
    - The admin user can then go to the admin panel and approve any comments.

  - __As a Site Admin I can be notified when a user has submitted the contact form so that I do not need to keep checking the admin site for any form submissions to read__

    - When any user submits the contact form successfully, an email is sent to the admin's email address containing the name of who it is from, their email address and the message they have submitted.

#### Epic 2: All User Functionality

  - __As a Site User I can view a list of restaurant posts so that I can select one to view__

    - When viewing the website any user can navigate to the list of restaurants via the navbar or other links on the home page.
    - The home page and profile pages of users who have posted or favourited restaurant posts also display some restaurants for users to view.

  - __As a Site User I can view a paginated list of restaurant posts so that I can easily select a post to view__

    - On the restaurant page and profile pages of users who have posted or favourited restaurant posts, when there are more than 3 posts to be displayed they are split onto multiple pages to prevent there being too many on any one page.
    - There are buttons below the posts for each page of restaurants that take the user to the particular page that each one represents when clicked.
    - If there are a lot of pages (above 7 or 8), on smaller screens the buttons will not display correctly and will extend over their parent element. This is currently not a problem but will need to be rectified when the number of pages increases significantly. The number of restaurants per page could be increased, or how the pagination is displayed could be changed.

  - __As a Site User I can filter the available restaurant posts so that I can see posts that are more specified to my needs__

    - On the restaurant page there is a filter section - to the left of the restaurants list on larger screens and via a button and modal on smaller screens.
    - The filter section is divided into two further sections: Cuisine and Location, which list all of the cuisines and locations associated with all of the current restaurant posts. 
    - The user can see how many restaurants have a particular cuisine and/or location. When the user clicks on any of the items in the filter lists, the restaurant list reloads showing only restaurants that match the selected item.
    - The user can then filter further by clicking on one of the remaining items in the other list.
    - To see all restaurant posts again the user will need to click 'All' on one or both of the filter lists they have already filtered by.
    - When the restaurant list has been filtered, the pagination buttons still work as expected, taking the user to the next or previous page of the filtered posts.

  - __As a Site User I can type keywords into a search bar so that I can find restaurant posts with titles that contain the keywords that I typed__

    - On the restaurants page, there is a search bar above the list of restaurants on the restaurants section.
    - The user can type words into the search bar, then hit enter or click the 'Search' button, and the restaurant list will reload showing any restaurant posts with the typed words contained in their title.
    - If no restaurants are found an appropriate message is displayed.

  - __As a Site User I can click on a restaurant post so that I can view the post in its entirety__

    - When viewing a list of restaurants on the home page, restaurants page or a profile page, when the user clicks on any of the titles or images of the listed restaurants they are taken to the detailed page of that restaurant.

  - __As a Site User I can view the number of times a restaurant post has been favourited so that I can see which are the most popular__

    - When viewing the list of restaurants on the restaurants page, the user can see a little heart icon with a number next to it at the bottom left of each restaurant post. This is number is how many times that particular restaurant post has been favourited. On the restaurant detail page, this can also be seen with the addition of the words 'Times Favourited'. These words are omitted from summary posts on the restaurants page so they do not look overcrowded.

  - __As a Site User I can view comments on an individual restaurant post so that I can see what people have had to say about it__

    - When viewing a restaurant's detail page a list of all the comments made on that particular post can be seen at the bottom of the page. If no comments have been made then a message is displayed explaining this.

  - __As a Site User I can view the author's favourite dishes on each restaurant post so that I can see which dishes the author of each restaurant post recommends__

    - When viewing a restaurant's detail page there is a section titled 'Favourite Dishes' which displays all the dishes that the author has decided to add to this post.

  - __As a Site User I can view registered users' profiles so that I can learn more about them and see which restaurant posts they've favourited and/or which they've posted__

    - When viewing the restaurant lists on the home page or restaurant page, or when viewing a restaurant's detail page there is some text just below the restaurant's title which shows the user who added the post. This text contains a link that takes the current user to that user's profile.
    - When viewing another user's profile page there is a 'Profile Info' section that contains some basic information about the user if they have decided to add any. Each field is blank unless the user has decided to update them except for the 'Name' field which is prepopulated with their username, and the 'Image' field which is prepopulated with a default image.
    - There is also another section that initially shows a list of any restaurant posts that the user has made, but can be toggled to show all the restaurant posts they have favourited by clicking on the 'Show Favourites' button. By doing so the page reloads with the list of favourites. This can be reverted by clicking on the renamed 'Show Restaurants Posted' button.

  - __As a Site User I can fill in a contact form so that I can get in contact with the site owners to ask any questions I might have__

    - When viewing the website any user can navigate to the 'Contact Us' page by clicking on the 'Contact' link in the navbar.
    - This page contains a simple form that requires the user to enter their name, email and a message that they would like to send. All fields are required, and if any are left blank or do not match the necessary criteria the user is made aware.
    - Upon successful submission of the form, the user is shown a message stating that their message has been sent successfully. All the information provided by the user is then sent via email to the main admin's email account.

  - __As a Site User I can register for an account so that I can contribute to the site__

    - When viewing the wesbite any user that is not already signed in can navigate to the 'Register' page by clicking on the 'Register' link in the navbar. There are also links to the register and sign in pages within the 'Welcome Message' section of the home page, and the 'Comments' section of any restaurant's detail page.
    - There is also a link to the register page on the sign in page and vice versa.
    - When viewing the 'Register' page the user can register for an account by filling in their email address, username and password into the relevant fields. The email and username fields must be unique, and the password needs to be entered twice with both entries matching. If any of these requirements are not met, the user is made aware.
    - Upon successful submission of the form, the user is redirected to the home page where a message is displayed stating that have now been signed in.

#### Epic 3: Registered User Functionality

  - __As a Registered Site User I can add my own restaurant posts so that I can share my favourites restaurants and dishes with other users__

    - When viewing the website any registered user can add new restaurant posts. When signed in there is an 'Add Restaurant' button on the home page within the 'Recently added restaurants' section and another button above the list of restaurants on the restaurants page. When either button is clicked the user is taken to the 'Add Restaurant' page where they can complete and submit a form with all the necessary details of the new restaurant they would like to add.
    - The add restaurant page has various fields that must be completed for the form to be submitted. The image field is optional. A default image is used if the user does not add one.
    - All other fields are required, and if the user tries to submit the form when a field has not been completed a message is displayed showing them which field(s) must be completed.
    - Upon successful submission of the form the user is redirected to the detail page of the restaurant post they have just added, and a message is displayed letting them know that the restaurant post has been added.

  - __As a Registered Site User I can update restaurant posts that I've previously made so that I can amend anything that might be incorrect or add dishes__

    - When a registered and signed in user is viewing the detail page of one of their restaurant posts there is an 'Edit' link shown near the restaurants title. To its right on large screens and above it on small screens.
    - When this link is clicked the user is taken to the 'Add Restaurant' page, only now it is titled 'Edit Restaurant' and the form is already completed with all of the current information about the restaurant post.
    - The user can update any of these details and then submit the form again. All of the same rules apply from when adding a restaurant, and the user is told if they have missed any required fields.
    - Upon successful submission of the form the user is redirected to the detail page of the restaurant post they have just updated, and a message is displayed letting them know that the restaurant post has been updated.

  - __As a Registered Site User I can delete restaurant posts that I've previously made so that I can remove any restaurant posts that I no longer wish to share__

    - When a registered and signed in user is viewing the 'Update Restaurant' page of one their restaurant posts there is a 'Delete' link shown near the page title; to its right on large screens and above it on small screens.
    - When this link is clicked the user is taken to the 'Delete Restaurant' page, where the user asked if they are sure they would like to delete the post.
    - If the user decides they would like to go ahead with deleting the post they can click the 'Confirm' button which will delete the post, redirect the user to the restaurants page and display a message letting them know that it has been deleted.

  - __As a Registered Site User I can leave comments on restaurant posts so that I can give my opinion on posts__

    - When a registered and signed in user is viewing the detail page of any restaurant post, within the 'Comments' section there is a text box with the placeholder 'Leave a comment...' which the user can use to type comments that they would like to make on that particular post. Once the user has typed a comment that they are happy to submit they can click on the 'Submit' button which will submit the comment for approval. All comments need to be approved by an admin user before they are displayed on the restaurant's detail page.
    - Upon successful submission of the comment form a message is displayed to the user letting them know that their comment has been sent for approval.
    - The success message replaces the text box and button, but the text box and button will reappear the next time they visit the page, or if they reload the page.
    - Once a comment has been approved it will be shown beneath all other previous comments in the 'Comments' section of the restaurant's detail page.

  - __As a Registered Site User I can favourite or unfavourite restaurant posts so that I can keep track of restaurant posts that I like__

    - When a registered and signed in user is viewing the detail page of any restaurant post, a little heart icon is displayed next to a number and the words 'Times Favourited'. This shows the user how many times the post has been favourited by other users. 
    - The heart icon is originally the outline of a heart, but if the user clicks on the heart then the page will reload, the number will go up by one and the heart icon will now be all one colour (filled in). This shows the user that they have favourited the post. The user can unfavourite the post by clicking on the heart again. This will again reload the page, reduce the number by one and revert the heart icon to the outline of a heart.
    - Only registered users can favourite or unfavourite posts, but any user can see how many times a post has been favourited.
    - Users cannot favourite or unfavourite their own posts.
    - Any post favourited by a user will be displayed on their profile page. This allows them to keep track of their favourite posts and allows other users to see which posts they have favourited.

  - __As a Registered Site User I can reset my password so that I can still gain access to my account if I've forgotten the current one__

    - When a registered user is attempting to sign in but has forgotten their password, from the 'Sign In' page they can click a link labelled 'Forgot Password?' which will take the user to the 'Reset Password' page.
    - On this page, the user is prompted to type in the email address linked to their account. Once they have done this they can click the 'Reset My Password' button which will submit the form and reload the page. A message is now displayed letting them know that an email has been sent to them. The email they receive will have a link that takes them to the 'Password Reset' page where they can choose a new password for their account by typing it in twice and clicking the 'Change Password' button.
    - Both the 'Reset Password' page and the 'Password Reset' page will let the user know if anything they have typed in does not match the forms' requirements.

  - __As a Registered Site User I can view my own profile so that I can see what restaurant posts I've posted or favourited__

    - Registered users who are signed in can access their own profile by clicking the 'Profile' link on the navbar, or by clicking the 'Added by' link on any of the restaurant posts they have made that are shown on various pages across the site.
    - When users are viewing their own profile page much of the information displayed is the same as when viewing other users' profiles - they can see the profile info they have decided to share, and can toggle between seeing any restaurant posts they have made and any restaurants they have favourited. In addition to this though, there is an 'Edit' button displayed at the top of the profile info section, and just below the profile info section two buttons are displayed: 'Update Email' and 'Update Password'.

  - __As a Registered Site User I can edit my own profile so that I can choose what to share about myself with other users__

    - When a registered and signed in user is viewing their own profile and clicks on the 'Edit' link at the top of the profile info section, they are taken to the 'Edit Profile' page.
    - A form is displayed with 5 optional fields that the user can fill in. The user can add their name, location, favourite cuisine, a bio and an image. Once the user is happy with how they have filled in the form they can click the 'Update Profile' button which submits the form and takes them back to their profile page which will now be updated with any of the information they submitted on the form. A message is also displayed letting them know that their profile has been updated.

  - __As a Registered Site User I can update my registered email address or update my password so that I can use a new email address with my account, strengthen my password or use a more memorable password__

    - When a registered and signed in user is viewing their own profile and clicks on the 'Update Email' button just below the profile info section, they are taken to the 'Email Addresses' page.
    - A list of email addresses currently associated with the account is shown with the primary email labelled as such.
    - If there are multiple emails in the list then the user can change the primary email to any other email that has been verified. They can also remove any email addresses from their account as long as they are not the primary email.
    - The user can add another email address to their account by typing in a valid new email address and clicking the 'Add Email' button. Email addresses already linked to another user account cannot be used. If the email address typed in does not match the requirements of the form the user is made aware.
    - Upon successful submission of the form the email address typed in is added to the list of addresses above and is marked as unverified. A message is also displayed letting the user know that a confirmation email has been sent to their account. When the link in the email is followed the user is taken to a page where that can confirm verification of the email address.
    - When a registered and signed in user is viewing their own profile and clicks on the 'Update Password' button just below the profile info section, they are taken to the 'Change Password' page.
    - Here, the user can change their password by correctly typing in their current password, typing a new password twice and then clicking the 'Change Password' button. If the current password does not match, or the new passwords do not match, the user is made aware.
    - Upon successful submission of the form, the page reloads and displays a message letting the user know that they have changed their password successfully.

### Validator Testing

- __HTML__

  - Originally, a few errors were showing up when the site was put through the [W3C Markup Validation Service.](https://validator.w3.org/), but they have all since been rectified and now no errors are showing on any of the pages.

- __CSS__

  - No errors were found when put through the [W3C CSS Validation Service - Jigsaw.](https://jigsaw.w3.org/css-validator/)

- __JavaScript__

  - No errors were found when put through the [JSHint.](https://jshint.com/), though there was a warning.
  - __Warning__: "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics."
    This is referring to the for loop that adds event listeners to the cuisine and location list items on restaurants.html. This should not cause any issues because it is only run once - when the DOM has finished loading - and it simply adds functions to the list items 'click' events. Everything is working as expected.

- __Python__

  - All python files have been put through the [PEP8 linter](http://pep8online.com/). Any issues that were found due to long lines, trailing whitespace etc. have been rectified and no errors are now showing.

### Performance Testing

The website was audited for mobile and desktop using Google Chrome's lighthouse feature. Most scores were high, above 90% for all categories. There were a few exceptions though. On the mobile device audit the restaurants page, profile page, sign in page and register page all scored below 90% on the performance test, with the restaurants page scoring only 75%. They did, however, all score higher than 90% on the other 3 test areas.

[WAVE Evaluation Tool](https://wave.webaim.org/) was used to test the accessibility across all the pages of the site. A few aria labels were missing and there were some contrast issues, but all of those have now been rectified and it all looks good. 

### Device and Browser Compatibility Testing

To test the site's compatibility across a range of devices [Responsinator](https://www.responsinator.com/) was used, going through all of the user stories on each device it includes in both portrait and landscape modes. The devices included are as follows:

  - iPhone X
  - Pixel 2
  - iPhone 6-8
  - iPhone 6-8 Large Version
  - iPad

Chrome Dev Tools was also used to check the site's compatibility across a range of other devices also in both portrait and landscape modes. These devices include:

  - Ipad Pro
  - Galaxy Fold (which has a very narrow viewport of only 280px in portrait mode)

Actual mobile devices belonging to family and friends were also used for testing which includes the following:

  - iPhone 7
  - Pixel 4
  - S10 Plus

A desktop monitor was also used for testing with a couple of different resolutions to check that the site remains to look and act as expected on larger screens. The resolutions were: 1366 x 768 and 1920 x 1080.

Google Chrome was the browser used for the majority of testing during the development process, but once development had neared an end some other browsers were used for testing to make sure the site had cross-browser compatibility. The full list of browsers used for testing are as follows:

  - Chrome
  - Edge
  - Firefox

### Bugs

#### Fixed Bugs

- When submitting the add restaurant form the Cuisine field wasn't being saved to the database. This was a problem because it is a required field. This was caused due to the use of 'commit=False' when initially saving the form data, and the Cuisine being a many to many relationship with Restaurant. It was fixed by saving the form using Django's save_m2m() function on the form straight after the Restaurant's object data was saved.

- When updating a restaurant post the dishes get added again when submitting the form. This was solved by deleting all of the current dishes related to the relevant restaurant and then adding the new list of dishes that may or may not contain the original dishes.

- The height of the restaurant cards on the home page and restaurant page varied based on the height of the images uploaded so different restauarant cards weren't always the same height. This was fixed by amending the y margins on the relevant elements and adding some custom height classes at certain screen widths. One of the custom classes forces the element to be 100% height at certain screen widths, and another one forces the height of the elements to be 250px at certain screen widths.

- When submitting the filter form on restaurants.html it did not work when submitting via the modal but did when not submitting via the modal. This was fixed by submitting the form using Javascript, which is a requirement when using Bootstrap modals.

- When adding pagination to profile.html it wasn't working initially. It was eventually fixed by using page_obj.object_list as the context to be looped over rather than the context that was explicitly defined in ProfileView.

- Custom box-shadow is applied to the welcome message area which still appears on smaller screens even though the element's background is transparent on smaller screens. This was solved by adding custom class names to the relevant elements and then adding box shadows using media queries.

- Any logged-in user can access the edit and delete pages of any restaurant, and the edit page of any user's profile if they type in the correct URL. This was fixed by overriding the get_queryset of the relevant views and returning only objects with which the current user is associated.

- When deploying to Heroku for the first time the background images applied to divs via the CSS file were not loading. This was fixed by uploading all of the images to Cloudinary and then referencing the URLs given to them by Cloudinary in the CSS file.

- When uploading an image to a profile the image was not displaying correctly. This was caused by an if statement being in the wrong place in profile.html. This was easily rectified by moving the if statement to the correct place.

- If a user registers an account with an email address as their username, or chooses any other username with special characters, although the username might be unique, when it is slugified the slug value will not necessarily be unique and would lead to an error. To fix this, when a new profile is being saved, if the slug value being created already exists then a unique number - the id of the most recently added profile object before this one plus 1 - is concatenated with the slug value to make a unique slug value.

#### Unfixed Bugs

- When adding a restaurant, if a restaurant with the same name already exists an error is thrown as expected. But when the form has reloaded the list of dishes added before submission disappear.

- When viewing the forms to add a restaurant or to update your profile, on very small screens (below 360px wide) the image upload element becomes too wide and is not contained within its parent element.


## Deployment

[Here's a link to the live site.](https://foodie-favourites.herokuapp.com/)

### Deploying with Heroku

This project has been deployed on Heroku using the following steps:
 
- Log into Heroku or create an account.
- Create a new Heroku App with an appropriate name and region.
- Once created go to the Resources tab, then under Add-ons search and add 'Heroku Postgres’.
- Then go to the Settings tab and click Reveal Config Vars.
- Add the following variables as config vars:
  - SECRET_KEY - can be any key you like
  - CLOUDINARY_URL - must be a Cloudinary API key
  - SENDGRID_API_KEY - must be a SendGrid API key
  - EMAIL_HOST_USER - must be the email address associated with a SendGrid account
- Now go to the Deploy tab.
- Connect to Github using the relevant repository name.
- Then click 'Deploy a GitHub branch' under the Manual deploy section.
- Once confirmation of deployment is shown, the project is now deployed and can be opened.

### Forking or Cloning the GitHub Repository

To deploy this application, fork or clone the [repository](https://github.com/AshFoster/foodie-favourites), then follow the steps outlined in the '[Deploying with Heroku](#deploying-with-heroku)' section above.

When deploying using a fork or clone, all of the apps in the 'requirements.txt' file will need to be installed.

#### Forking the Repository

To fork the GitHub repository follow these steps:

- Log in to GitHub and navigate to the [repository](https://github.com/AshFoster/foodie-favourites).
- Once the page has loaded look for the "Fork" button near the top right of the page and click it.
- A copy of the original repository should now be in your GitHub account.

#### Cloning the Repository

To clone the GitHub repository follow these steps:

- Log in to GitHub and navigate to the [repository](https://github.com/AshFoster/foodie-favourites).
- Above the repository's list of files, on the right, click on the "Code" button.
- Copy the link that is shown in the drop-down list.
- Open Git Bash and change the current working directory to the location where you want the cloned directory to be made.
- In the terminal, type `git clone`, and then paste the URL you copied earlier and press enter.
- A local clone of the original repository should now be available.

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)

### Online Resources

- [Git](https://en.wikipedia.org/wiki/Git) - for version control.
- [GitPod](https://www.gitpod.io/) - the online IDE (Integrated Development Environment) used for development.
- [GitHub](https://github.com/) - used as an online code repository.
- [Heroku](https://www.heroku.com/) - used for deployment.
- [Google Fonts](https://fonts.google.com/) - for the fonts used throughout the site.
- [Font Awesome](https://fontawesome.com/) - for the icons used throughout the site.
- [Colormind](http://colormind.io/) - used to obtain colour palette images.
- [SendGrid](https://sendgrid.com/) - used to send emails when required.
- [Lucidchart](https://www.lucidchart.com/) - used to create site map and entity relationship diagrams. 

## Credits

### Code

- [YouTube](https://www.youtube.com/)
- [Code Institute's Full Stack Developer Course](https://codeinstitute.net/)
  - Course material and walkthrough projects provided some ideas.
