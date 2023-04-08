# Simple FastAPI Py

## My Awesome FastAPI Project

This is a simple REST API built with Python and FastAPI.

## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/BaseMax/SimpleFastPyAPI
```

Change into the project directory:

```bash
cd my-fastapi-project
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

The application will start and be available at http://localhost:8000.

## API Endpoints

- Retrieve a list of users:

```http
GET /users
```

Returns a list of all users in the system.

- Retrieve details for a specific user:

```http
GET /users/{user_id}
```
Returns details for a specific user with the given user_id.

- Add a new user

```http
POST /users
```

Adds a new user to the system. The request body should include a JSON object with the following properties:

  - `name` (string, required): the name of the user
  - `email` (string, required): the email address of the user
  - `password` (string, required): the password for the user

- Update an existing user
```http
PUT /users/{user_id}
```

Updates an existing user with the given user_id. The request body should include a JSON object with the following properties:

  -  `name` (string, optional): the new name for the user
  -  `email` (string, optional): the new email address for the user
  -  `password` (string, optional): the new password for the user

- Delete a user

```http
DELETE /users/{user_id}
```

Deletes the user with the given user_id.

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

Copyright 2023, Max Base
