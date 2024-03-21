![Local Image](/static/assets/logorusty.png)
# Project Title: Rustys TradingPost
## Description
"Rustys TradingPost is a web application that allows users to sign up, exchange messages, and possibly create listings or advertisements.currently themed to be an apocalyptic marketplace, this could easily and quicky be reskinned to provide a marketplace for any niche, videogame, hunting,sports,cars, etc. It leverages Django's authentication system and integrates with third-party packages like allauth for user management. i took inspiration from dondeal, 


### [Link to the live site](https://cat-beans-cafe-08a84ae29847.herokuapp.com/)

#### - By Joe Mellis

---

## Table of contents 

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

## Technologies Used
- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Django - framework used to build this project
- Heroku PostgreSQL - used as the database
- Font Awesome - for social media icons
- GitHub - for storing the code and for the projects Kanban
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - version control tool
## Website Structure
### Models and Relationships

#### Home Model

| Key | Name            | Field             |
|-----|-----------------|-------------------|
| PK  | id              | AutoField         |
| FK  | user            | ForeignKey(User)  |
| x   | title           | CharField         |
| x   | description     | TextField         |
| x   | image           | CloudinaryField   |
| x   | additional_photos | IntegerField    |
| x   | created_on      | DateTimeField     |
| x   | location        | CharField         |
| x   | category        | CharField         |
| x   | price           | DecimalField      |

#### Message Model

| Key | Name       | Field               |
|-----|------------|---------------------|
| FK  | sender     | ForeignKey(User)    |
| FK  | recipient  | ForeignKey(User)    |
| x   | subject    | CharField           |
| x   | message    | TextField           |
| x   | timestamp  | DateTimeField       |

Home Model: This model  is for creating an advertisement or listing. It contains fields such as title, description, price, location, category, image, and additional_photos.

Message Model: This model represents messages exchanged within the application. It includes fields like subject and content.

User Model: Although not explicitly mentioned, this project utilizes Django's built-in User model for user authentication and management.

Views:

Signup View: This view handles the signup process for new users. It uses the SignupView provided by allauth for user registration.

Message List View: This view displays a list of messages in the user's inbox. It iterates over messages and displays them in cards, including options for deleting messages and replying to them.

Templates:

base.html: This template serves as the base layout for rustys, containing common HTML structure and navigation elements.

signup.html: This template is used for the signup page, allowing users to register for an account. It extends the base.html template and includes a form for user registration.

inbox.html: This template displays the user's inbox, showing a list of messages. It extends base.html and iterates over messages to display them.


Authentication and Authorization:

i am using allauth for user authentication, which provides features like signup, login, logout, and password management out of the box.

## Screenshot wireframe
![Local Image](/static/assets/wireframe.jpg)

## Ideation
as a game developer i try to make things a bit fun, a bit imaginative, i was set on making a marketplace, that didnt need any payment methods, like craigslist,facebook marketplace,donedeal,
done deal has a starting page with many filtering options, it was a bit much for my needs, but i liked the lay out of the content once filtering had been entered

## Screenshots of project Board
![Local Image](/static/assets/project%20board.PNG)

### User Stories
User Stories
    User Registration:
        As a new user, I want to be able to register for an account on the platform.

    User Authentication:
        As a registered user, I want to be able to log in to my account securely.

    User Profile:
        As a user, I want to have a profile where I can view and update my personal information.

    Messaging System:
        As a user, I want to be able to send messages to other users on the platform.
        As a user, I want to receive notifications when I receive a new message.

    Advert Posting:
        As a user, I want to be able to create and post advertisements for items or services I want to sell.

    Advert Management:
        As a user, I want to be able to edit or delete my own advertisements.
        As a user, I want to view a list of all my posted advertisements.

    Search and Filter Adverts:
        As a user, I want to be able to search for specific advertisements based on keywords or categories.
        As a user, I want to filter advertisements based on various criteria such as price, location, and category.

    Inbox Management:
        As a user, I want to be able to view my inbox and read messages sent to me by other users.
        As a user, I want to be able to delete messages from my inbox.

### Features
User Authentication and Authorization:
-Users can register for an account and log in securely.
-Authentication mechanisms ensure that only authorized users can access certain features.

Messaging System:
-Users can send messages to each other through an internal messaging system.
-Notifications alert users when they receive new messages.

Advert Posting and Management:
-Users can create and post advertisements for items or services they want to sell.
-Advertisements can include details like title, description, price, location, and images.
-Users have the ability to edit or delete their own advertisements.
-Advert management features enable users to view a list of all their posted advertisements.

Inbox Management:
-Users can view their inbox and read messages sent by other users.
-Inbox management features enable users to delete messages from their inbox.
-Users can reply to messages sent by other users.

These features collectively provide users with a comprehensive platform for buying, selling, and communicating with each other effectively within the application.

# Manual testing

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | pass |
| User can log into account | Pass |
| User can log out of account | Pass |


---

#### User Navigation Tests

| Test | Result  |
|--|--|
| Authorised User can easily navigate to post | Pass |
| Authorised User can access inbox| Pass|
| Authorised User access their create post|Pass|
| Authorised User can access the home page|Pass|



---

#### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page |Pass|
| Non authorised user cant contact user | Pass |
| Non authorised user won't access inbox| Pass|
| Non authorised user won't access create ad| Pass|
| Authorised user can access inbox| Pass|
| Authorised user can access create ad| Pass|

---

#### posting and Messaging Tests

| Test |Result  |
|--|--|
|User can create a post | Pass |
|User can edit a post | Pass |
|User can delete a post | Pass |
|User can see a list of thier posts | Pass |
|User can create a contact a seller | Pass |
|User can get a reply from seller | Pass |
|User can see a list of recieved mail | Pass |
|User can get a delete a message from recieved mail | Pass |



---

#### Admin Tests

| Test |Result  |
|--|--|
|Items display correctly on front-end when updated / added |Pass|
|Admin can remove created listings and messages |Pass|

# Deployment

#### The deployment stage of the website should follow the steps below:

> Create the Heroku app

- Sign up / Log in to Heroku
- In Heroku Dashboard page select 'New' and then 'Create New App'
- Name a project - I decided on the Cat Beans Café (the app's name must be unique)
- Select EU as that was my region in the moment of creating the app
- Select "Create App"
- In the "Deploy" tab choose GitHub as the deployment method
- Connect your GitHub account/ find and connect your GitHub repository

> Set up enviroment variables

- In the Django app editor create env.py in the top level
- In env.py import os
- In env.py set up necessary enviroment variables:
  - add a secret key using: os.environ['SECRET_KEY'] = 'your secret key'
  - for the database variable the line should include os.environ['DATABASE_URL']= 'Paste the database link in here'
  - in settings.py replace value of SECRET_KEY variable with os.environ.get('SECRET_KEY')
  - in settings.py change the value of DATABASES variable to 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
- In Django app's settings.py on top of the file add:
```
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
- Navigate to the "Settings" tab in Heroku.
- Open the "Config Vars" section and add DATABASE_URL as Key and the database link from app's env.py as Value
- Add SECRET_KEY for the Key value and the secret key value from env.py as the Value
- In the terminal migrate the models over to the new database connection
- In settings.py add the STATIC files settings as follows:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
- Change the templates directory in settings.py to: TEMPLARES_DIR = os.path.join(BASE_DIR, 'templates')
- In TEMPLATES variable change the 'DIRS' key to look like this: 'DIRS': [TEMPLARES_DIR],
- Add Heroku to the ALLOWED_HOSTS list (the format will be your-app-name.herokuapp.com, you can copy it from the Domains section in Settings tab in your Heroku app)
- If you haven't done that up to this point, then create in your Django app's code editor new top level folders: static and templates
- Create a new file on the top level directory - Procfile, remembering to use a capital letter
- Within the Procfile add following:
```
web: guincorn PROJECT_NAME.wsgi
``` 
- In the terminal, add the changed files, commit and push to GitHub

> Heroku deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually 
- Heroku will display a build log- watch the build logs for any errors
- Once the build process is completed Heroku displays 'Your App Was Successfully Deployed' message and a link to the app to visit the live site
- As my first 2 build attempts failed I needed to apply changes to my code (I forgot to set up the static files and templates) to successfully deploy on the 3rd time 

### Issues and Bugs
TemplateDoesNotExist for signup.html: Initially, i encountered a TemplateDoesNotExist error for signup.html. This was likely due to incorrect template paths or misconfigured template loaders. To overcome this, i double-checked the template paths in my views and ensured that the templates were located in the correct directories.

AttributeError for SignupView: i faced an AttributeError indicating that SignupView was not defined. This issue likely occurred because i attempted to reference SignupView without importing it. To resolve this, i imported SignupView from the appropriate module where it was defined.

Unauthorized error for site.webmanifest: i encountered an unauthorized error when trying to access site.webmanifest. This issue may have been caused by incorrect permissions or misconfiguration in my web server or application settings. To fix it, i ensured that the necessary permissions were set correctly and that the file paths were properly configured.

Syntax error in site.webmanifest: There was a syntax error in site.webmanifest, which prevented it from being parsed correctly. To resolve this, i corrected the syntax error in the manifest file to ensure it complied with the required format.

TemplateSyntaxError for trans tag: i faced a TemplateSyntaxError related to the trans tag in your templates. This error occurred because the trans tag was not recognized or parsed correctly. To overcome this, i double-checked the syntax of the trans tag and ensured that it was used appropriately according to the documentation.

TemplateDoesNotExist for account/base.html: Finally, i encountered a TemplateDoesNotExist error for account/base.html. This issue may have occurred due to incorrect template paths or misconfigured template loaders. To fix it, i verified the template paths and loaders to ensure that account/base.html was accessible and properly loaded.

Throughout these challenges, i demonstrated persistence and problem-solving skills by carefully analyzing error messages, double-checking configurations, and making necessary corrections to my code and settings. This iterative approach helped me overcome each bug and improve the stability and functionality of my application.

best way to eat a hippo is 1 small bite at a time

# Future Improvements
### Enhanced CSS Styling:

Implement responsive design to ensure optimal viewing experience across various devices.
Refine color scheme and design elements to create a visually appealing interface.
Improve layout for better organization and navigation.
Incorporate reactive responses to enhance user interaction and engagement.
### Advanced Filtering System:

Develop a comprehensive filtering system to allow users to refine search results based on various criteria such as price range, location, category, and more.
Provide users with the ability to save and customize their preferred filters for future searches.
### Inbox Management Enhancement:

Implement a notification system to alert users about new messages.
Display a badge with the number of unread messages to keep users informed.
Enhance inbox functionality for better organization and management of messages, including features like message categorization and sorting options.
### Sponsored Advertisements:

Introduce the ability for users to create sponsored advertisements, which would appear at the top of search results with a distinct border.
Offer sponsored advert packages with customizable options such as duration and visibility settings.
### Integration and Expansion:

Rusty's provides a solid foundation for further expansion and integration into other projects.
Explore opportunities to integrate Rusty's functionality into other platforms or applications seamlessly.
Continuously evaluate and implement new features or enhancements to meet evolving user needs and preferences.
Overall, Rusty's is a fully functional platform with immense potential for expansion and customization. With ongoing development and refinement, it can serve as a versatile solution for various online marketplace needs or seamlessly integrate into existing projects.

### References
-django docs: https://docs.djangoproject.com/en/5.0/
-donedeal Example Websites: https://www.donedeal.ie/
-chatgpt helped solve many bugs: https://chat.openai.com/
-mid journey for the images: https://miramuseai.net/
-Martin from code institues coding coach

# Screenshots of pages
![Local Image](/static/assets/start.PNG)
![Local Image](/static/assets/signup.PNG)
![Local Image](/static/assets/login.PNG)
![Local Image](/static/assets/logout.PNG)
![Local Image](/static/assets/loggedin%20home.PNG)
![Local Image](/static/assets/create.PNG)
![Local Image](/static/assets/edit%20post.PNG)
![Local Image](/static/assets/your%20posts.PNG)
![Local Image](/static/assets/reply.PNG)
![Local Image](/static/assets/message%20details.PNG)