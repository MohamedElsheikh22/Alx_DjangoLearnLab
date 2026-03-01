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

## Comment Functionality

This feature allows users to interact with blog posts through comments.

### Features

- View all comments under each post
- Authenticated users can add comments
- Users can edit and delete their own comments
- Each comment is linked to a specific post and author
- Unauthorized users can only view comments

### URLs

- `/post/<int:pk>/comment/new/` → add comment
- `/comment/<int:pk>/update/` → edit comment
- `/comment/<int:pk>/delete/` → delete comment

# Django Blog

This project is a simple blog application built with Django as part of the ALX Django Learn Lab.

In this phase, tagging and search functionality were added to make it easier to organize posts and find content.

---

## Tagging System

A Tag model was created and connected to the Post model using a ManyToMany relationship.

Each post can have multiple tags, and each tag can belong to multiple posts.

Tags can be added or edited while creating or updating a post.

On the post detail page, the tags are displayed and each tag links to a page that shows all posts related to it.

---

## Search

A search feature was implemented to allow users to search for posts using:

- title
- content
- tags

The search uses Django Q objects to filter results from multiple fields.

Example:
/search/?q=django

If no results are found, a message is displayed.

---

## Main URLs

- `/post/` → list all posts  
- `/post/new/` → create a new post  
- `/post/<id>/` → post details  
- `/post/<id>/update/` → update post  
- `/post/<id>/delete/` → delete post  
- `/tags/<tag_name>/` → posts filtered by tag  
- `/search/?q=keyword` → search results  

---

## How to use

1. Login to your account
2. Create a new post
3. Add tags to the post
4. Open the post to see the tags
5. Click on any tag to see related posts
6. Use the search bar to find posts

---

## Files updated

- models.py → added Tag model and relation with Post  
- views.py → search view and posts by tag view  
- urls.py → added routes for tags and search  
- templates → display tags and search results  

---

## Notes

- Tags are optional when creating a post
- A post can exist without tags
- Search works even if only part of the word is entered

