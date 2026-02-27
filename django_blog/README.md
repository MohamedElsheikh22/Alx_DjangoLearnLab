# Django Blog Authentication

This part of the project adds a basic authentication system to the blog.

## What I implemented

- User registration
- Login and logout
- Profile page for logged in users
- Email update from the profile page

Django built-in authentication views were used for login and logout, and a custom form was created for user registration to include the email field.

## URLs

/register/ → create a new account  
/login/ → log in  
/logout/ → log out  
/profile/ → view and update profile  

## How to test

1. Run the server

   python manage.py runserver

2. Open the browser and go to /register/ and create a new user.

3. Log in from /login/

4. Go to /profile/ and change the email, then save.

5. Use the logout button to log out.

## Notes

- CSRF token is added to all forms.
- Profile page is protected and requires login.
- Passwords are stored using Django’s default hashing.


# Django Blog – Post Management Features

This project is part of the ALX Django learning tasks.

## Overview

In this task, blog post management functionality was implemented using Django class-based views.  
Authenticated users can create posts, and only the author of a post can edit or delete it.

## Features

- View all blog posts
- View a single post in detail
- Create a new post (login required)
- Update an existing post (author only)
- Delete a post (author only)

## URLs

- `/posts/` → list all posts  
- `/posts/<id>/` → post details  
- `/posts/new/` → create a new post  
- `/posts/<id>/edit/` → update a post  
- `/posts/<id>/delete/` → delete a post  

## Permissions

- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.
- All users can view posts.

## How to Test

1. Run the server:
python manage.py runserver
2. Open in browser:
http://127.0.0.1:8000/posts/

3. Create a new post while logged in.

4. Try:
- Editing the post
- Deleting the post
- Logging out and accessing `/posts/new/`

## Notes

- The author of each post is automatically set to the logged-in user.
- After creating, updating, or deleting a post, the user is redirected to the posts list page.