# RESTful API FastAPI Boilerplate

A boilerplate for quickly coding and deploying Python API servers using FastAPI, SQL Databases, and Peewee.

With a single command, you can install and setup a production-ready FastAPI app on your system. Many features are included into the app, such as JWT authentication, request validation, unit and integration tests, continuous integration, docker support, API documentation, and so on. Check out the features list below for more information.


## Installation

1. Clone the repository:
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

[//]: # (- [Authorization]&#40;#authorization&#41;)

[//]: # (- [Logging]&#40;#logging&#41;)

[//]: # (- [Linting]&#40;#linting&#41;)


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

# specify JWT configuration
JWT_SECRET=
JWT_ALGORITHM=
JWT_AUTH_DURATION=86400
```


## Project Structures

```shell
src\
  |--{module_name}
    |--const.py               # Constants (controller layer)
    |--controllers\           # Route controllers (controller layer)
    |--middlewares\           # Custom FastAPI middlewares
    |--models\                # Peewee models (data layer)
    |--services\              # Business logic (service layer)
    |--repositories\          # Data logic
    |--utils\                 # Utility classes and functions
    |--requests\              # Request data validation schemas
  |--core
    |--databases\
      |--migrations\          # Migration files
      |--sql_connect.py       # SQL database connection & base model
    |--repositories\base.py   # Base class for data logic
    |--services\base.py       # Base class for business logic
    |--utils\                 # Utility classes and functions
    |--config.py               # Project configurations
  |--server.py                # FastAPI app
  |--sync_database.py         # Sync database (generate migration files & run)
```

**Note**: For simple modules, we can create the files representing their responsibility directly instead of creating directories (please check the `ai_media` as the reference).


## API Documentation
Run the server and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to see a list of accessible APIs and their specs. This documentation page is produced automatically by swagger definitions written as comments in the route files.


## API Endpoints

List of available routes:

**Auth routes:**
- `POST /v1/auth/register` - register
- `POST /v1/auth/login` - login
- `POST /v1/auth/refresh-token` - refresh token

**Book routes:**
- `POST /v1/books` - create a user
- `GET /v1/books` - get all users
- `GET /v1/books/:book_id` - get user
- `PUT /v1/books/:book_id` - update user
- `DELETE /v1/books/:book_id` - delete user


## Error Handling

We have the centralized error handlers inside the `server.py` file, which are the functionality provided by FastAPI. For example, the code below catches validation errors thrown by FastAPI by default. We can customize the logic to return the data in our own favor.

```python
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, e: RequestValidationError):
    # specify our logic here
    return CustomORJSONResponse(e.errors(), status.HTTP_400_BAD_REQUEST)
```

The error handler sends an error response, which has the following format:
```json
{
    "ok": false,
    "data": {},
    "error": [
        {
            "loc": [
                "body",
                "file"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

We can also define our errors, then freely throw and catch them in the cases we need.


## Validation

Request data is validated using [Pydantic](https://pydantic-docs.helpmanual.io/). Please check the documentation for more details on how to write Pydantic validation schemas. It is similar to defining a model.

```python
from pydantic import BaseModel


class UserRegisterRequest(BaseModel):
    username: str
    password: str
    name: str
```

The validation schemas are defined in the `src/{module_name}/requests` directory and are used in the controllers by providing them as parameters to these functions.

```python
@router.post("/register")
def register(data: UserRegisterRequest):
    # specify our logic
    return None
```


## Authentication

The authentication logic is in the `ai_auth` module, this module is automatically registered inside the `server.py`. To disable the authentication functions, you can comment the line below inside the `server.py`.

```python
app.include_router(auth.router, prefix="/v1")
```

To parse and extract data in users' tokens, you can use `get_current_user_info` function in `middlewares/parse_bearer_token.py`. That function necessitates the inclusion of a valid JWT access token in the Authorization request header via the Bearer schema. An Unauthorized (401) error is thrown if the request does not contain a valid access token.

**Generating Access Tokens:**

A successful call to the register (`POST /v1/auth/register`) or login (`POST /v1/auth/login`) endpoints will generate an access token. These endpoints' responses also include refresh tokens.

An access token is valid for 30 minutes. You can modify this expiration time by changing the `JWT_AUTH_DURATION` environment variable in the .env file.

**Refreshing Access Tokens:**

After the access token expires, a new access token can be generated, by making a call to the refresh token endpoint (POST `/v1/auth/refresh-token`) and sending along a valid refresh token in the request body. This call returns a new access token and a new refresh token.

[//]: # (## Authorization)

[//]: # (## Logging)

[//]: # (## Linting)
