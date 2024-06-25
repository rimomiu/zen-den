## Zen-Den

## Project Members
- Cody Huls
- Miao Jihanyu
- Silva Galstyn

### Functionality 

-   Sign up/Sign in: Users can create an account with a username, password, first name, last name, and email address.
-   View blog posts: Both signed-in users and guest users can view blog posts.
-   Post blog posts: Signed-in users can post a blog with an attached picture and publish date.
-   Edit/Delete blog posts: Signed-in users can edit and delete the blog posts they created. If they did not create the blog post, they will not see the edit/delete button.
-   View comments: Signed-in users can view comments on a single blog post.
-   Post comments under a blog: Signed-in users can post comments under a single blog post.
-   Edit/Delete comments: Signed-in users can edit and delete the comments they created. If they did not create the comment, they will not see the edit/delete button.
-   Contact form: Both signed-in users and guest users can leave a message for the admin in the contact form. The admin will receive an email about their message, and the user will also receive an auto-reply stating they will get a response within 24 hours.


### Project Initialization

1. Clone the repository to local computer
2. CD into the new project directory
3. Run docker volume create zen-den
4. Run docker compose build
5. Run docker compose up
6. Go to http://localhost:8000/docs# in the browser to interact with the backend
7. Go to http://localhost:5173/ in the browser to interact with the frontend
8. Some data has been prefilled into our database to make the website easier to interact with when first navigating to our website.  Please note, you will not be able to sign in or post/delete/update blogs or comments with already existing user accounts because passwords for these prefilled users were saved in the database as is and were not hashed.  Thus, you will need to signup with new accounts to perform these functions.

### Interacting with the Backend
1. While your Docker containers are running, please go to http://localhost:8000/docs# in your browser
2. Click through the /api/auth/signup to create an account
3. Click through the /api/auth/signin & verify you recived a cookie
4. Try out any of the endpoints, such as POST blog or POST comment


### Interacting with the Frontend
1. While your docker containers are running, please go to http://localhost:5173 in your browser
2. Click on blogs to get the list of existing blogs
3. Go back to the homepage by clicking on home
4. Click on Signup in the navbar
5. Signup by using the following info or info of your own:
	username: zenuser
	password: string1
	First Name: Jane 
	Last Name: Smith
	Email: janesmith@gmail.com
6. Logout
7. Signin by entering the following information:
	username: zenuser
	password: string1
8. Try out Post a blog and input the following or your own inputs:
	Title: I love Yoga
	Content: I love to do yoga when I’m stressed.  My favorite pose is downward dog.
	image_url: https://images.pexels.com/photos/6648789/pexels-photo-6648789.jpeg
	date_published: input the date you want
	author: leave the prefilled username as is
9. Hit Post and you will be redirected to the list of blogs with you blog added to the list
10. Click on another blog and post a comment
11.  Click on Profile in the navbar and try to delete the blogs and comments you posted.  
12. Click on blogs in the navbar and try to update or delete someone else's blog.  You should not be able to do this



