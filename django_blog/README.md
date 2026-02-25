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
