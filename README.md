# Foodie Favourites

[Click here to view the live site.]()

![Am I Responsive Image]()

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

Foodie Favourites is a free to use website where UK based food lovers - especially those who enjoy eating out - can share and discover their favourite restaurants and dishes. Once registered, users can create posts of their own favourite restaurants, and can comment and favourite other peoples' restaurant posts. Registered users will have their own profile page where they can share some infomation about themselves if they so desire. The profile page also shows any restaurant posts they have made, and any restaurants they have favourited.

## User Experience

### Strategy

This website is aimed at people who would like to share their favourite restaurants with others, and/ or people who would like to discover some new restaurants. Therefore the age range aimed for is quite wide, essentially anyone who is able to enjoy a nice meal out.

In a very broad sense, their are 3 types of users the website will have: site admins, registered users and non-registered users. For this reason the epics and user stories have been categorised in this way.

#### Epics and User Stories

There are 3 epics, each of which have been split up into multiple user stories. All of which are outlined below.

  - __Epic 1: Admin Setup__
      - As a Site Admin I can create, read, update and delete restaurant posts so that I can manage the site's content
      - As a Site Admin I can approve or disapprove comments on restaurant posts so that I can filter out any questionable comments
      - As a Site Admin I can be notified when a comment needs to be approved so that I do not need to keep checking the admin site for anything to be approved
      - As a Site Admin I can be notified when a user has submitted the contact form so that I do not need to keep checking the admin site for any form submissions to read

  - __Epic 2: All User Functionality__
      - As a Site User I can view a list of restaurant posts so that I can select one to view
      - As a Site User I can view a paginated list of restaurant posts so that I can easily select a post to view
      - As a Site User I can filter the available restaurant posts so that I can see posts which are more specified to my needs
      - As a Site User I can search through the available restaurant posts using keywords so that I can see posts which are more specified to my needs
      - As a Site User I can click on a restaurant post so that I can view the post in its entirety
      - As a Site User I can view the number of times a restaurant post has been favourited so that I can I can see which are the most popular
      - As a Site User I can view comments on an individual restaurant post so that I can I can see what people have had to say about it
      - As a Site User I can view the author's favourite dishes on each individual restaurant post so that I can see which dishes the author of each restaurant post recommends
      - As a Site User I can view registered users' profiles so that I can learn more about them and see which restaurant posts they've favourited and/or which they've posted.
      - As a Site User I can fill in a contact form so that I can get in contact with the site owners to ask any questions I might have
      - As a Site User I can register for an account so that I can contibute to the site

  - __Epic 3: Registered User Functionality__
      - As a Registered Site User I can add my own restaurant posts so that I can share my favourites restaurants and dishes with other users
      - As a Registered Site User I can update restaurant posts that I've previosuly made so that I can amend anything that might be incorrect or add dishes
      - As a Registered Site User I can delete restaurant posts that I've previosuly made so that I can remove any restaurant posts that I no longer wish to share
      - As a Registered Site User I can leave comments on restaurant posts so that I can give my opinion on posts
      - As a Registered Site User I can favourite or unfavourite restaurant posts so that I can keep track of restautant posts that I like
      - As a Registered Site User I can reset my password so that I can still gain access to my account if I've forgotten the current one
      - As a Registered Site User I can update my registered email address or update my password so that I can use a new email address with my account, strengthen my password or user a more memorable password
      - As a Registered Site User I can view my own profile so that I can see what restaurant posts I've posted or favourited
      - As a Registered Site User I can edit my own profile so that I can choose what to share about myself with other users

### Scope

All of the user stories outlined above are all feassible for the first release of the website. Some further features that could be implemented later on include:

- Allowing users to suggest their favourites dishes on other user's restaurant posts
- Adding an autocomplete feature to the location selection when adding a new restaurant
- Giving the user the ability to explicitly request new cuisines (this can currently be done using contact us page)

I don't feel that having these features will impact the user experience too much, so felt it was fine to exclude them for the first release. Each of which would need to be thought about carefully in how they would be implemented in order to not overcomplicate the website too much.

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
- Update Restaurant (registered users only - accessed from restaurant detail page - only post's author can access)
- Delete Restaurant (registered users only - accessed from update restaurant page - only post's author can access)
- Other users' profiles - accessed by clicking on the author's username on restaurant posts or comments
- Edit profile (registered users only - accessed from profile page - users can only edit their own profiles)
- Update Email (registered users only - accessed from profile page - users can only update their own email)
- Update Password (registered users only - accessed from profile page - users can only update their own password)
- Reset Password (registered users only - accessed from sign in page - users can only reset their own password)

### Skeleton

#### Wireframes

Wireframes were created for mobiles, tablets, and desktops using [Balsamiq](https://balsamiq.com/).

Here are links to each of them:

- [Desktop - Home]()

### Surface

#### Imagery

Images are an important part of the look and feel of the website. Each page has a different background image, most of which are of different restaurant settings.

#### Colour Scheme

The colour scheme of the site is very simple, with the main colour's being shade's of black, grey, and white.

![Website's Colours 1]()

The idea was to keep the colours themselves simple, and to use the different background images on each page to provide the more interesting colours. Using shades of black, grey and white meant that most images could be used without clashing.

#### Typography

For my typography choices, I used [Google Fonts](https://fonts.google.com/?sort=popularity) which I sorted by popularity to give me an idea of some fonts that are likely to work well across a number of websites.

I then selected the ones that stood out the most to me. The fonts I chose are as follows:

Open Sans Condensed (italic) - This is used for the Foodie Favourites logo shown on the navbar.

Oswald - This is used for all navbar links. 

Lato - This is used for all other text throughout the site.

Each of them is of the font category Sans Serif which is the font used as a fallback if for any reason the specified font isn't available.

## Features

### Existing Features

## Testing

### User Stories Testing

### Validator Testing

- __HTML__

  - [W3C Markup Validation Service.](https://validator.w3.org/)

- __CSS__

  - [W3C CSS Validation Service - Jigsaw.](https://jigsaw.w3.org/css-validator/)

- __JavaScript__

  -  [JSHint.](https://jshint.com/)

- __Python__

  - [PEP8 linter](http://pep8online.com/)

### Performance Testing

I audited the website for mobile and desktop using Google Chrome's lighthouse feature. All scores were high. It might only be examing the landing page and not the in-game page.

The final lighthouse scores are as follows:

  - Mobile

  ![Mobile Lighthouse]()

  - Desktop

  ![Desktop Lighthouse]()

[WAVE Evaluation Tool](https://wave.webaim.org/)

### Device and Browser Compatibility Testing

To test the site's compatibility across a range of devices I used [Responsinator](https://www.responsinator.com/) and went through all of the user and owner goals on each device it includes in both portrait and landscape modes. The devices included are as follows:

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
  - Internet Explorer 11
  - Edge
  - Firefox

### Bugs

#### Fixed Bugs

- When submitting the add restaurant form the Cuisine field wasn't being saved to the database. This was a problem because it is a required field. This was caused due to the use of 'commit-False' when initially saving the form data, and the Cuisine being a many to many relationship with Restaurant. It was fixed by saving the form using Django's save_m2m() function on the form straight after the Restaurant's object data was saved.

- When updating a restaurant post the dishes get added again when submitting the form. This was solved by deleting all of the current dishes related to the relevant restaurant and then adding the new list of dishes which may or may not contain the original dishes.

- The height of the restaurnt previews on the home page and restaurant page varied based on the height of the images uploaded so different restauarant cards weren't always the same height. This was fixed by amending the y margins on the relevant elements and adding some custom height classes at certain screen widths. One of the custom classes forces the element to be 100% height at certain screen widths, and an other forces the height of the elements to be 180px at certain screen widths.

- When submitting the filter form on restaurants.html it did not work when submitting via the model, but did when not submitting via the modal. This was fixed by submitting the form using Javascript, which is a requirement when using Bootstrap modals.

- When adding pagination to profile.html it wasn't working initially. It was eventually fixed by using page_obj.object_list as the context to be looped over rather than the context that was explicitly defined in ProfileView.

- Custom box shadow is applied to the welcome message area which still appears on smaller screens even though the element's background is transparent on smaller screens. This was solved by adding custom class names to the relevant elements and then adding box shadows using media queries.

- Any logged in user can access the edit and delete pages of any restaurant, and the edit page of any user's profile if they type in the correct url. This was fixed by overiding the get_queryset funcion of the relevant views and returning only objects which the current user is associated with.

#### Unfixed Bugs

- When adding a restaurant, if a restaurant with that same name already exists an error is thrown, but the list of dishes disappear.


## Deployment

[Here's a link to the live site.]()

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
- [GitHub](https://github.com/) - used as an online code repository and for deployment.
- [Google Fonts](https://fonts.google.com/) - for the fonts used throughout the site.
- [Font Awesome](https://fontawesome.com/) - for the icons used throughout the site.
- [Online Image Resizer](https://resizeimage.net/) - for resizing images to improve the site's performance.
- [Eye Dropper](https://eyedropper.org/) - to find the hex code for the game images colour.
- [Adobe's Colour Wheel](https://color.adobe.com/create/color-wheel) - to find the contrasting colours throughout the site.
- [Colormind](http://colormind.io/) - used to obtain colour palette images.

## Credits

### Code

- [YouTube](https://www.youtube.com/)
- [Code Institute's Full Stack Developer Course](https://codeinstitute.net/)
  - Course material and essentials walkthrough projects provided some ideas.

### Media
