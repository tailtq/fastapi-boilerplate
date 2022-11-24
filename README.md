# RESTful API Python FastAPI Boilerplate

A boilerplate for quickly coding and deploying Python API servers using FastAPI, SQL Databases, and Peewee.


## Installation

1. For manually installation, first clone the repository:
```shell
git clone https://github.com/tailtq/fastapi-boilerplate.git
```

2. Install the dependencies:
```shell
pip install -r requirements.txt
```

3. Set the environment variables:
```shell
cp .env.example .env

# open .env and modify the environment variables (if needed)
```

4. Run the server:
```shell
python src/server.py
```

5. Generate migration files & run (optional):
```shell
python src/sync_database.py
```


## Table of Contents

- [Features](#features)
- [Commands](#commands)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Error Handling](#error-handling)
- [Validation](#validation)
- [Authentication](#authentication)
- [Authorization](#authorization)
- [Logging](#logging)
- [Linting](#linting)


## Features

- **SQL databases**: [MySQL](https://www.mysql.com/) and [PostgreSQL](https://www.postgresql.org/) using Peewee as the ORM library
- **NoSQL databases**: coming soon
- **Authentication**: using OAuth2 supported by [FastAPI](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- **Validation**: request data validation using [Pydantic](https://pydantic-docs.helpmanual.io/)
- **Logging**: coming soon
- **API documentation**: with Swagger
- **Dependency management**: with PIP
- **Environment variables**: using [python-dotenv](https://pypi.org/project/python-dotenv/)
- **CORS**: Cross-Origin Resource-Sharing enabled by FastAPI
- **Docker support**: coming soon
- **Code quality**: coming soon
- **Git hooks**: coming soon
- **Linting**: coming soon


## Commands

Run the server:
```shell
python src/server.py
```

Generate migration files & run (optional):
```shell
python src/sync_database.py
```


## Environment Variables

```shell
DB_ENGINE=mysql  # mysql, postgresql
DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=root
DB_NAME=book_db

# detect file changes if the value is "local"
APP_ENV=local
APP_PORT=8000

# directory to store the media files
LOCAL_STORAGE_PATH=resources/media
# s3 configuration
AWS_PUBLIC_KEY=
AWS_SECRET_KEY=
AWS_S3_BUCKET=
```


## Project Structures

```shell
src\
  |--{module_name}
     |--const.py        # Constants (controller layer)
     |--controllers\    # Route controllers (controller layer)
     |--middlewares\    # Custom express middlewares
     |--models\         # Mongoose models (data layer)
     |--services\       # Business logic (service layer)
     |--utils\          # Utility classes and functions
     |--requests\       # Request data validation schemas
 |--server.py           # FastAPI app
 |--sync_database.py    # Sync database (generate migration files & run)
```

**Note**: For simple modules, we can create the files representing their responsibility directly instead of creating directories (please check the `ai_media` as the reference).


## API Documentation
Run the server and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to see a list of accessible APIs and their specs. This documentation page is produced automatically by swagger definitions written as comments in the route files.


## API Endpoints

List of available routes:

**Auth routes:**
- `POST /v1/auth/register` - register
- `POST /v1/auth/login` - login

**Book routes:**
- `POST /v1/books` - create a user
- `GET /v1/books` - get all users
- `GET /v1/books/:book_id` - get user
- `PUT /v1/books/:book_id` - update user
- `DELETE /v1/books/:book_id` - delete user


## Error Handling
## Validation
## Authentication
## Authorization
## Logging
## Linting
