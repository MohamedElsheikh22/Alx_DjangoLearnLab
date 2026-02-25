#Advanced API Project
This project is a simple Book API buitl usin Django REST Framework as part of the ALX backend track.

##Waht this project does
It provides API endpoints to:
List all books
Retrieve a single book by ID
Create a new book
Update a book
Delete a book

Each book is linked to an author.

##Endpoints
GET /api/books/
GET /api/books/<id>/
POST /api/books/create/
PUT /api/books/update/<id>/
DELETE /api/books/delete/<id>/

##Permissions
Anyone can view books
Only authenticated users can crate, update, or delete

##How to run the project
1. Create a virtual enviroment and activate it 
2. Install the requeirements
3. Run migrate
4. Start the server

##Testing
I tested the API using the Django REST Framework browsable API.