# TBC
# Table of Contents
1. [Introduction](#Introduction)
2. [UX](#UX)
   * [Ideal User Demographic](#Ideal-User-Demographic)
   *  [User Stories](#User-Stories)
   *  [Development Planes](#Development-Planes)
   * [Design](#Design)
3. [Features](#Features)
   * [Design Features](#Design-Features)
   * [Existing Features](#Existing-Features)
   * [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
   * [Main Languages Used](#Main-Languages-Used)
   * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
   * [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
   * [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
8. [Credits](#Credits)
   * [Content](#Content)
   * [Media](#Media)
   * [Code](#Code)
9. [Acknowledgements](#Acknowledgements)

# Introduction
This website was created for fans and players of the game genre MMO(Massively Multiplayer Online) to help them establish what certain terms mean inside the MMO world. The focus
of this website is to allow the users to Create, Edit and search for terms they come across in those games and to help them understand what they mean. MMO's have became increasingly popular as there are a huge variety of genres to play, as well as the game also being open world which gives the players choices of where they want to go and what they want to achieve.

This is the third of four Milestone Projects for the developer that they must complete during their Full Stack Web Development Program at the Code institute.

The main requirements was to create a Full-Stack site that allows the users to manage the database of the website using the technologies of Python, Flask, MongoDB, JavaScript, HTML and CSS. As well as any external API's.

# UX

## Ideal User Demographic

* The main requirements for this project were to create a dictionary for any jargon terms in the gaming world genre of Massively Multiplayer Online Games.

## User Stories

**Developer Goals**
  * The website should have an easy to understand navigation system for the users.
  * A simple and easy registration system for users to create their accounts.
  * Keep the display consistent on all devices with minor changes for ease of access.

**Player Goals**
  * I want to be able to, search for terms I don't quite understand.
  * I want to be able to, navigate through the site with ease.
  * I want to be able to, add, edit and delete my own submitted terms.
  * I want to be able to, give my opinion on terms added by others.

## Development Planes

In order to create the dictionary for the gaming genre of MMO the developer has worked with a community they're involved with, who are all MMO players to ensure that definitions given are correct.

**Roles**
* Fans of the gaming genre wanting to know what certain terms mean when they come across them in-game.
* Players wanting to help any possible players thinking of going to play the MMO genre.
* Players wanting to share their opinion on some of the terms given by other players.

**Demographic**
* Players aged over 13.
* Players and fans of the gaming genre MMO.

**Personalities**
* Fun-Seeking.
* Wanting to help others.
* People wanting to improve their knowledge.

**Values**
* Enjoy Challenging themselves mentally.
* Curious of trying a new genre of game.

**Lifestyles**
* Players and fans of MMO's.
* Newcomers wanting to play and learn the basic jargon of the gaming terms.

The website needs to let the user:
* Allow the user to Register an account.
* Allow the user to log in after creating an account.
* Allow the logged in User to add terms.
* Allow the logged in user to edit their own submissions.
* Allow the logged in user to delete a submission of their own.
* Allow the logged in user to log out.
* Be able to select navigate easily through the website.
* Be able to give their opinions on terms submitted from other players.
* Contact the developer by using the 'Contact Us' Page.
* Find developers GitHub profile, LinkedIn profile and the contact form from the footer.

The website needs to let the developer:
* To be able to view all submitted entries.
* As the Admin to be able to delete terms.

## Skeleton

The developer used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq Homepage") to create the wireframes for the website.

### Home Page

![Homepage Wireframe](assets/readme/Homepage-MS3.png)

### Register User Page

![Game Page Wireframe](assets/readme/Register-User.png)

### Log In

![Game Page Wireframe](assets/readme/Log-In.png)

### Users Profile

![Users Profile Wireframe](assets/readme/Users-Profile.png)

### Add Term

![Add Term Wireframe](assets/readme/Add-Term.png)

### Contact Us

![Contact Us Wireframe](assets/readme/Contact-Us.png)

### Log Out

![Log Out Wireframe](assets/readme/Log-Out.png)

## Design

### Colour Scheme

* The colour scheme I opted to use was based on many taverns within the MMO franchise but the colours specifically chosen was from this picture found from a popular game called Hearthstone. ![Hearthstone Box](assets/testing-images/hearthstone.png)

### Typography

## Features

### Design Features

### Existing Features

### Future Features

* For future features on the website I would like to be able to let people vote on terms to allow other users who visit the website to see what terms are credible.
* I would like to implement a new webpage one that helps any players visiting the website to look for players to play with on certain games.
* I would also like to implement that when a user is registering to the website they can use email, this would also allow them to reset their password if forgotten.

## Issues And Bugs

* When implementing the contact form for the user to email the developer GMail settings for one account I was trying to use wouldn't allow me to link accounts and was blocking any emails from being sent or received. In order to fix this issue i created a new GMail account and allowed 'less secure apps' which would allow the SMTP to send emails to and from the developers email.

* When adding a new term to the db when being redirected back to the homepage of the website the terms just added would show 'None' as both the title and the description. Upon looking back through the form elements I noticed that the id and names was not matching and in turn was not being passed through correctly so in order to fix this issue I renamed all appropriate tags to match one another which allowed the request.form.get() to correctly fetch back the correct data.

## Technologies Used

 * [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki") has been used because it is the standard markup language for documents designed to be displayed in a web browser.
 * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3 "Link to CSS Wiki") has been used to style certain aspects of the website.
 * [Fontawesome](https://fontawesome.com/ "Link to FontAwesome") has been used for the icons used throughout the website.
 * [Materialize](https://materializecss.com/ "Link to Materialize") version 1.0.0 has been used a modern responsive front-end framework.
 * [Googlefonts](https://fonts.google.com/) has been used to style the fonts of the writing on the web site. 
 * [Python](https://www.python.org/ "Link to Python")
   * Python was the main language used throughout the project.
 * [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)"Link to Flask Wiki")
 * [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript")
 * [jQuery](https://jquery.com/ "Link to jQuery") has been used to initialize Materialize functionality.
 * [Jinja](https://jinja.palletsprojects.com/en/2.11.x/ "Link to Jinja") is a modern and designer-friendly templating language for Python3.
 * [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/ "Link to Werkzeug") Werkzeug is a comprehensive WSGI web application library.
 * [Mongo DB Atlas](https://account.mongodb.com/ "Link to MongoDB") is a NoSQL database used to store data.
 * [Pymongo](https://pypi.org/project/pymongo/ "Link to Pymongo") is used to be able to interact with [Mongo DB Atlas](https://account.mongodb.com/) database.
 * [Heroku](https://www.heroku.com/ "Link to Heroku") is used to deploy and host the project.
 * [Git](https://git-scm.com/ "Link to Git Homepage")
   * Git was used to utilise the GitPod terminal to allow the developer to commit and push to GitHub.
 * [GitHub](https://github.com/ "Link to GitHub Homepage")
   * GitHub was used to store the project after pushing.
 * [Balsamiq](https://balsamiq.com/ "Link to Balsamiq Homepage")
   * Balsamiq was used to create the wireframes during the designing stages of the project.

## Credits

Parts of the '/form' function was taken from codemy.com's youtube series https://www.youtube.com/watch?v=U5MBYN6an70&list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn&index=9
Logo for favicon created with https://www.freelogodesign.org/