![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
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
### Pages
if un auth
- Index/ Login/Signup
if auth
- Index/ Logout/create_advert/contact/my_posts/inbox
### Architecture
- Consitent navbar and footer
- index.html landing page which includes all posts from the database and displays them in chronolgical order newest first, if the user is not logged in they may view the posts on the database, but cannot send messages, they can login or sign up, if logged in the user can view the home page posts, send the seller a private message, they can create a new advert/post, they can access thier inbox, display a list of thier created adverts, created adverts can be edited or deleted, in the in box, a list of messages are displayed, messages may be clicked to be read, can be replied to, and deleted,
all pages extend ffrom base.html to keep a consistent feel
## Ideation

as a game developer i try to make things a bit fun, a bit imaginative, i was set on making a marketplace, that didnt need any payment methods, like craigslist,facebook marketplace,donedeal,
done deal has a starting page with many filtering options, it was a bit much for my needs, but i liked the lay out of the content once filtering had been entered
## Screenshots of project Board
![Local Image](/static/assets/project%20board.PNG)
### User Stories
User Stories
- As a user, I can easily navigate to the login or sign-up page upon entering the site, ensuring a smooth onboarding experience.
- As a logged-in user, I can access my profile page where I can add a profile picture and update my bio, allowing me to personalize my profile and share information with others.
- As a user, I can filter the database by selecting one of three buttons: workshops, events, or study groups, enabling me to quickly find the type of content I'm interested in.
- As a logged-in user, I can create a new workshop, event, or study group, specifying relevant details such as date, time, location, and description, empowering me to organize and promote activities within the community.
- As a user  I want detailed information about each interdimensional destination, including any potential risks or challenges, to ensure a secure and enjoyable trip.
- As a user, I can edit and delete my own posts (workshops, events, or study groups) to make necessary updates or remove outdated information.
### Future Improvements
- CSS styling would be improved: Responsiveness, Colour Scheming, Layout, Reactive responses
- Further and more clear call to actions
- More interaction ability for user, the ability to set user roles
- More general interactivty could be implemented
- Agile workflow - Implementation and delegation of tasks better tracked.
## Screenshots of wireframing and database schema
![Local Image](/assets/images/20240305_114724.jpg)
![Local Image](/assets/images/Screenshot%202024-03-05%20at%2013.17.30.png)
![Local Image](/assets/images/Screenshot%202024-03-05%20at%2013.17.38.png)
![Local Image](/assets/images/Screenshot%202024-03-05%20at%2016.16.50.png)
## Acknowledgments
### References
django docs: https://docs.djangoproject.com/en/5.0/
Mockplus Example Websites: https://www.mockplus.com/blog/post/travel-website-templates
w3Schools Bootstrap: https://www.w3schools.com/bootstrap/bootstrap_get_started.asp
Bootstrap Documentation: https://getbootstrap.com/docs/5.3/getting-started/introduction/
### Shoutouts
- Staff at Quest for hosting the event and providing refreshments
- Thanks to Martin too.