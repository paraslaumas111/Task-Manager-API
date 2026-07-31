# Task Management API

A secure, multi-user REST API for managing tasks. The project provides user authentication, JWT-based authorization, task CRUD operations, pagination, caching, and interactive API documentation.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT
* Argon2 password hashing

## Features

* User registration
* Secure password hashing
* JWT authentication
* Protected task endpoints
* User-specific task ownership
* Create, read, update, and delete tasks
* Task priorities, statuses, and due dates
* Pagination
* In-memory caching
* Swagger API documentation

## Architecture

```text
API Router
    ↓
Service Layer
    ↓
Repository Layer
    ↓
SQLAlchemy
    ↓
PostgreSQL
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create the environment file:

```powershell
Copy-Item .env.example .env
```

Update the values in `.env`.

Run database migrations:

```powershell
alembic upgrade head
```

Start the API:

```powershell
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Authentication

Register a user:

```http
POST /auth/register
```

Log in:

```http
POST /auth/login
```

Use the Swagger **Authorize** button with:

* Username: your registered email
* Password: your registered password
* Client ID: leave empty
* Client Secret: leave empty

## Pagination

```http
GET /tasks?page=1&size=10
```

## Security

* Passwords are hashed using Argon2.
* JWT access tokens are signed and expire after a configured period.
* Users can access only their own tasks.
* Secrets are stored in `.env` and are not committed to Git.
