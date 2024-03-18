![Local Image](/static/assets/logorusty.png)
# Project Title: Rustys TradingPost
## Description
"Rustys TradingPost is a web application that allows users to sign up, exchange messages, and possibly create listings or advertisements. It leverages Django's authentication system and integrates with third-party packages like allauth for user management. i took inspiration from dondeal, rustys is set in a future apocalyptic world

## Team 
- [Joe] - Full Stack Developer
## Technologies Used
- Github
- Gitpod
- Chat GPT: https://chat.openai.com
- Django
- Heroku
- Elephant SQL
## Website Structure
### Models and Relationships
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

### Issues and Bugs
TemplateDoesNotExist for signup.html: Initially, i encountered a TemplateDoesNotExist error for signup.html. This was likely due to incorrect template paths or misconfigured template loaders. To overcome this, i double-checked the template paths in my views and ensured that the templates were located in the correct directories.

AttributeError for SignupView: i faced an AttributeError indicating that SignupView was not defined. This issue likely occurred because i attempted to reference SignupView without importing it. To resolve this, i imported SignupView from the appropriate module where it was defined.

Unauthorized error for site.webmanifest: i encountered an unauthorized error when trying to access site.webmanifest. This issue may have been caused by incorrect permissions or misconfiguration in my web server or application settings. To fix it, i ensured that the necessary permissions were set correctly and that the file paths were properly configured.

Syntax error in site.webmanifest: There was a syntax error in site.webmanifest, which prevented it from being parsed correctly. To resolve this, i corrected the syntax error in the manifest file to ensure it complied with the required format.

TemplateSyntaxError for trans tag: i faced a TemplateSyntaxError related to the trans tag in your templates. This error occurred because the trans tag was not recognized or parsed correctly. To overcome this, i double-checked the syntax of the trans tag and ensured that it was used appropriately according to the documentation.

TemplateDoesNotExist for account/base.html: Finally, i encountered a TemplateDoesNotExist error for account/base.html. This issue may have occurred due to incorrect template paths or misconfigured template loaders. To fix it, i verified the template paths and loaders to ensure that account/base.html was accessible and properly loaded.

Throughout these challenges, i demonstrated persistence and problem-solving skills by carefully analyzing error messages, double-checking configurations, and making necessary corrections to my code and settings. This iterative approach helped me overcome each bug and improve the stability and functionality of my application.

best way to eat a hippo is 1 small bite at a time

### Future Improvements
# Enhanced CSS Styling:

Implement responsive design to ensure optimal viewing experience across various devices.
Refine color scheme and design elements to create a visually appealing interface.
Improve layout for better organization and navigation.
Incorporate reactive responses to enhance user interaction and engagement.
# Advanced Filtering System:

Develop a comprehensive filtering system to allow users to refine search results based on various criteria such as price range, location, category, and more.
Provide users with the ability to save and customize their preferred filters for future searches.
# Inbox Management Enhancement:

Implement a notification system to alert users about new messages.
Display a badge with the number of unread messages to keep users informed.
Enhance inbox functionality for better organization and management of messages, including features like message categorization and sorting options.
# Sponsored Advertisements:

Introduce the ability for users to create sponsored advertisements, which would appear at the top of search results with a distinct border.
Offer sponsored advert packages with customizable options such as duration and visibility settings.
# Integration and Expansion:

Rusty's provides a solid foundation for further expansion and integration into other projects.
Explore opportunities to integrate Rusty's functionality into other platforms or applications seamlessly.
Continuously evaluate and implement new features or enhancements to meet evolving user needs and preferences.
Overall, Rusty's is a fully functional platform with immense potential for expansion and customization. With ongoing development and refinement, it can serve as a versatile solution for various online marketplace needs or seamlessly integrate into existing projects.

### References
django docs: https://docs.djangoproject.com/en/5.0/
donedeal Example Websites: https://www.donedeal.ie/

### Screenshots of pages
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