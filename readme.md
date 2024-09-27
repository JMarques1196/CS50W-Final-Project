# Discussion Board Application.

## Motivation
The idea behind this project was to apply the knowledge gained through the CS50W Lectures and the research behind completing all the projects, but also learn something new.

 ## Distinctiveness and Complexity:
   In this section, I will describe into detail why I think this project fulfills the Distinctiveness and Complexity and requirements.
   ### Disctinctiveness:
   - The idea behind this project was to learn how to build an application that features a chat function. This is something that is not approached in the CS50W lectures, or any of its projects, so it fulfills the distinctiveness condition.
   ### Complexity:
   - This web application utilizes Django as a Backend, as per the requirements. It uses 5 different Models: User, Project, Media, Message and Checklist. It also takes advantage of Django's default Admin Panel to update/modify the information displayed on the Website.
   - This web application utilizes Javascript on the Frontend, as per the requirements, to make API calls, to create animations, and to manage a Websocket.
   - This application is fully responsive.

## Description
This project consists of a discussion board, using the theme of the CS50W Lectures.
Here is a summary of all the features contained in the application:

- **Authentication:**
  - Login Page, which when used will take the user to the homepage
  - Sign Up
  - Logout
    
- **HomePage:**
  - The homepage functions as a Menu that allows a user to select which project he is working on. The projects displayed on the homepage can be modified using Django's admin interface.
    
- **ProjectPage:**
  - Links for the project in question, and also the gradebook to check the progress.
  - Checklist for each task of the project. The status of this checklist is saved for each user whenever something is toggled, using a Django Model and Javascript.
  - A Carousel built using Javascript that contains useful links relevant to each project and a image. This carousel can be updated using Django's Admin Interface (Removing / Adding more links)
  - A Live chat using Websocket. This chat allows communication between logged in users.
    
## Files 

### Views.py
- loginView, logoutView, and signup manage the authentication of the application using Django's default authentication system.
- formLogin, registrationForm are Django Forms used in the Login and Signup pages to get user info. MessageForm is used for the chat function.
- The homepage view gets the current user and all the projects and renders the homepage.
- The project view renders the project homepage using appropriate data.
- The save view saves messages sent in the Live Chat function.
- The check view manages the check status of the checklist items.

### Consumers.py
- Contains the consumers for the chat function. It handles asynchronous requests that will connect and disconnect the Websocket, as well as manage the sending/receiving of messages.

## Project.js
- Contains the Javascript used in the project.
- Controls the Navbar changes from the homepage to the project page.
- Controls the Carousel Animation used in the project page.
- Controls the Toggle Animation for the checklist.
- Creates and manages the websocket using the click and onkeyup event.
- Makes an API call to the save view, to store messages and have a chat history.

### Templates - HTML Files
- Simply contain all the templates for each page of the project.

### Urls.py
- Contains all the urls for the project

### Routing.py
- Contains the routing for the websocket

## Models.py
- Contains 5 Models, User, Project, Media, Message and Checklist

### Styles.css
- This file contains all the styles for the project.

## How to run the application

### Dependencies:
 - Channels
 - Daphne
 
### Run the application:
- Install the dependencies.
- Run > Python3 manage.py makemigrations final
- Run > Python3 manage.py migrate
- Run > Python3 manage.py runserver
