# Simple FastAPI Py

## My Awesome FastAPI Project

This is a simple REST API built with Python and FastAPI and SQLAlchemy for CRUD operations (Create, Read, Update, Delete) on users.
FastAPI is a powerful web framework for building APIs.

## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/BaseMax/SimpleFastPyAPI
```

Change into the project directory:

```bash
cd SimpleFastPyAPI
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

### Retrieve a list of users:

```http
GET /users
```

Returns a list of all users in the system:

```console
curl http://localhost:8000/users/ -H "Accept: application/json"
```
Response:

```json
[
    {
        "email": "alice@example.com",
        "id": 1,
        "password": "password1",
        "name": "Alice"
    },
    {
        "email": "bob@example.com",
        "id": 2,
        "password": "password2",
        "name": "Bob"
    },
    {
        "email": "charlie@example.com",
        "id": 3,
        "password": "password3",
        "name": "Charlie"
    }
]
```

### Retrieve details for a specific user:

```http
GET /users/{user_id}
```
Returns details for a specific user with the given user_id:

```console
curl http://localhost:8000/users/1 -H "Accept: application/json"
```
Response:
```json
{
    "email": "alice@example.com",
    "id": 1,
    "password": "password1",
    "name": "Alice"
}
```

### Add a new user

```http
POST /users
```

Adds a new user to the system. The request body should include a JSON object with the following properties:

  - `name` (string, required): the name of the user
  - `email` (string, required): the email address of the user
  - `password` (string, required): the password for the user

```console
curl -X POST http://localhost:8000/users/
   -H 'Content-Type: application/json'
   -d '{"name":"Ali","password":"123456", "email": "AliAhmadi@gmail.com"}'
```
Response:

```json
{
    "email": "AliAhmadi@gmail.com",
    "password": "123456", 
    "id": 4, 
    "name": "Ali"
}
```


### Update an existing user
```http
PUT /users/{user_id}
```

Updates an existing user with the given user_id. The request body should include a JSON object with the following properties:

  -  `name` (string): the new name for the user
  -  `email` (string): the new email address for the user

```console
curl -X PUT http://localhost:8000/users/1
     -H "Accept: application/json"
     -d '{"name": "Reza", "email": "reza@yahoo.com"}'
```
Response:
```json
{"message": "User updated successfully"}
```

### Delete a user

```http
DELETE /users/{user_id}
```

Deletes the user with the given user_id:

```console
curl -X DELETE http://localhost:8000/2
```

Response:
```json
{"message": "User deleted successfully"}
```

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

Copyright 2023, Max Base
