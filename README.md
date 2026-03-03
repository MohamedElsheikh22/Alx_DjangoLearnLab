# Social Media API

A RESTful API built with Django and Django REST Framework.

## Setup
```bash
git clone <repo-url>
cd social_media_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| POST | /api/accounts/register/ | No | Register new user |
| POST | /api/accounts/login/ | No | Login & get token |
| GET/PUT | /api/accounts/profile/ | Yes | View/update profile |

## Authentication
```
Authorization: Token <your_token>
```

